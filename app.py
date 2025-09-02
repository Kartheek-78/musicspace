from flask import Flask, render_template, request, redirect, url_for
from flask_socketio import SocketIO, join_room, leave_room, emit
from yt_dlp import YoutubeDL
import random, string
import psycopg
import psycopg.rows
import os

# ---------------- PostgreSQL settings ----------------
DB_HOST = "dpg-d2i9e3fdiees73d3ggd0-a"
DB_PORT = 5432
DB_USER = "kartheekreddy78"
DB_PASSWORD = "vzrBm8pGEzqrGnbkggvoh8U45unyZur9"
DB_NAME = "musicspace"
# -----------------------------------------------------

app = Flask(__name__)
socketio = SocketIO(app, async_mode="gevent")

# Store current state per room
# e.g. {'ABCD1': {'url': 'https://...', 'position': 42.8, 'is_playing': True}}
current_audio_state = {}


# ---------------- Utility Functions ----------------
def random_code():
    return "".join(random.choices(string.ascii_uppercase + string.digits, k=5))


def get_db():
    return psycopg.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        dbname=DB_NAME,
        row_factory=psycopg.rows.dict_row,  # ✅ FIXED
    )
# ---------------------------------------------------


# ---------------- Routes ----------------
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/create")
def create():
    code = random_code()
    con = get_db()
    with con.cursor() as cur:
        cur.execute("INSERT INTO sessions(code) VALUES(%s)", (code,))
    con.commit()
    return redirect(url_for("room", code=code, name="Host"))


@app.route("/join", methods=["POST"])
def join():
    name = request.form["name"]
    code = request.form["code"]

    con = get_db()
    with con.cursor() as cur:
        cur.execute("SELECT * FROM sessions WHERE code=%s", (code,))
        session = cur.fetchone()
        if not session:
            return "Error: Room code does not exist!", 400

    return redirect(url_for("room", code=code, name=name))


@app.route("/room/<code>")
def room(code):
    name = request.args.get("name")
    return render_template("room.html", code=code, name=name)
# ---------------------------------------------------


# ---------------- Socket.IO Events ----------------
@socketio.on("join")
def on_join(data):
    code = data["room"]
    name = data["name"]

    con = get_db()
    with con.cursor() as cur:
        cur.execute(
            "SELECT * FROM session_users WHERE session_code=%s AND user_name=%s",
            (code, name),
        )
        exists = cur.fetchone()
        if not exists:
            cur.execute(
                "INSERT INTO session_users(session_code, user_name) VALUES(%s, %s)",
                (code, name),
            )
            msg = "joined"
        else:
            msg = "rejoined"
    con.commit()

    join_room(code)
    users = get_users(code)

    emit("joined", {"name": name, "users": users, "type": msg}, room=code)

    socketio.sleep(0.05)

    if code in current_audio_state:
        emit("sync_state", current_audio_state[code], room=request.sid)


@socketio.on("leave")
def on_leave(data):
    code = data["room"]
    name = data["name"]

    remove_user(code, name)
    leave_room(code)

    users = get_users(code)
    emit("left", {"name": name, "users": users}, room=code)

    if not users:
        delete_session(code)
        current_audio_state.pop(code, None)


@socketio.on("play")
def on_play(data):
    raw_url = data["url"].split("&")[0]
    url = (
        raw_url.replace("youtu.be/", "www.youtube.com/watch?v=")
        if "youtu.be/" in raw_url
        else raw_url
    )

    cookies_path = os.environ.get("YOUTUBE_COOKIES")

    ydl_opts = {
        "format": "bestaudio/best",
        "quiet": True,
        "noplaylist": True,
    }
    if cookies_path:
        ydl_opts["cookiefile"] = cookies_path

    try:
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            audio_url = info["url"]
    except Exception as e:
        emit("error", {"message": f"Failed to fetch video: {str(e)}"}, room=data["room"])
        return

    current_audio_state[data["room"]] = {
        "url": audio_url,
        "position": 0,
        "is_playing": True,
    }
    emit("play_audio", {"url": audio_url}, room=data["room"])


@socketio.on("time_update")
def on_time_update(data):
    code = data["room"]
    if code in current_audio_state:
        current_audio_state[code]["position"] = data["time"]


@socketio.on("pause")
def on_pause(data):
    code = data["room"]
    t = data["time"]
    if code in current_audio_state:
        current_audio_state[code]["position"] = t
        current_audio_state[code]["is_playing"] = False
    emit("pause_from_server", {"time": t}, room=code, include_self=False)


@socketio.on("resume")
def on_resume(data):
    code = data["room"]
    t = data["time"]
    if code in current_audio_state:
        current_audio_state[code]["position"] = t
        current_audio_state[code]["is_playing"] = True
    emit("resume_from_server", {"time": t}, room=code, include_self=False)


@socketio.on("get_current")
def on_get_current(data):
    code = data["room"]
    if code in current_audio_state:
        emit("current_state", current_audio_state[code], room=request.sid)


@socketio.on("seek")
def on_seek(data):
    code = data["room"]
    t = data["time"]
    if code in current_audio_state:
        current_audio_state[code]["position"] = t
    emit(
        "seek_from_server",
        {
            "time": t,
            "is_playing": current_audio_state[code].get("is_playing", False),
        },
        room=code,
        include_self=False,
    )
# ---------------------------------------------------


# ---------------- Helpers ----------------
def get_users(code):
    con = get_db()
    with con.cursor() as cur:
        cur.execute("SELECT user_name FROM session_users WHERE session_code=%s", (code,))
        return [row["user_name"] for row in cur.fetchall()]


def remove_user(code, name):
    con = get_db()
    with con.cursor() as cur:
        cur.execute(
            "DELETE FROM session_users WHERE session_code=%s AND user_name=%s",
            (code, name),
        )
    con.commit()


def delete_session(code):
    con = get_db()
    with con.cursor() as cur:
        cur.execute("DELETE FROM sessions WHERE code=%s", (code,))
    con.commit()
# ---------------------------------------------------


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    socketio.run(app, host="0.0.0.0", port=port)
