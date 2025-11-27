<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Music Space — README</title>

  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&family=Merriweather:wght@300;400;700&display=swap" rel="stylesheet">

  <style>
    :root{
      --bg: #0f1724;
      --card: #0b1220;
      --accent: linear-gradient(90deg,#7c3aed,#06b6d4);
      --muted: #9aa6b2;
      --glass: rgba(255,255,255,0.03);
    }
    html,body{height:100%;margin:0;font-family:Poppins, system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial; background: radial-gradient(1200px 600px at 10% 10%, rgba(124,58,237,0.08), transparent), var(--bg); color:#e6eef6;}
    .container{max-width:920px;margin:36px auto;padding:28px;background: linear-gradient(180deg, rgba(255,255,255,0.02), transparent);border-radius:14px;box-shadow:0 8px 30px rgba(2,6,23,0.7);border:1px solid rgba(255,255,255,0.03);} 
    header{display:flex;gap:16px;align-items:center}
    .logo{width:72px;height:72px;border-radius:12px;background:var(--accent);display:flex;align-items:center;justify-content:center;font-weight:700;box-shadow:0 6px 20px rgba(12,11,31,0.6);} 
    .title h1{margin:0;font-size:22px;letter-spacing:0.4px}
    .title p{margin:6px 0 0;color:var(--muted);font-size:13px}

    .badges{margin-left:auto;display:flex;gap:8px}
    .badges img{height:20px;border-radius:6px}

    .hero{display:flex;gap:24px;margin-top:20px;align-items:center}
    .hero .left{flex:1}
    .hero .right{width:260px}

    .card{background:linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01));padding:18px;border-radius:12px;border:1px solid rgba(255,255,255,0.02);}

    h2{font-size:16px;margin:12px 0}
    ul.features{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px;list-style:none;padding:0;margin:0}
    ul.features li{background:var(--glass);padding:12px;border-radius:10px;color:#dfe9f3;border:1px solid rgba(255,255,255,0.02);box-shadow:0 6px 18px rgba(2,6,23,0.45);}

    .section{margin-top:22px}
    pre,code{background:#071026;padding:10px;border-radius:8px;color:#dbeafe;overflow:auto;font-family:ui-monospace, SFMono-Regular, Menlo, Monaco, 'Roboto Mono', 'Courier New', monospace;font-size:13px}

    .columns{display:grid;grid-template-columns:1fr 1fr;gap:16px}

    .how{line-height:1.55;color:var(--muted)}

    .screenshot{width:100%;height:150px;background:linear-gradient(90deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01));border-radius:8px;display:flex;align-items:center;justify-content:center;color:var(--muted);}

    footer{display:flex;justify-content:space-between;align-items:center;margin-top:26px;color:var(--muted);font-size:13px}
    ul.features li:hover{transform:translateY(-6px);transition:all .25s ease;box-shadow:0 16px 40px rgba(4,8,16,0.6)}

    @media(max-width:720px){.columns{grid-template-columns:1fr}.hero{flex-direction:column}.badges{display:none}}
  </style>
</head>
<body>
  <div class="container">
    <header>
      <div class="logo">MS</div>
      <div class="title">
        <h1>Music Space</h1>
        <p>A real‑time music room I built — small, clean, and fun to demo full‑stack skills.</p>
      </div>

      <div class="badges">
        <img src="https://img.shields.io/badge/Flask-000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask">
        <img src="https://img.shields.io/badge/Socket.IO-010101?style=for-the-badge&logo=socket.io&logoColor=white" alt="Socket.IO">
        <img src="https://img.shields.io/badge/Postgres-316192?style=for-the-badge&logo=postgresql&logoColor=white" alt="Postgres">
      </div>
    </header>

    <div class="hero">
      <div class="left">
        <div class="card">
          <h2>About the project</h2>
          <p style="color:var(--muted);margin-top:6px;">I built <strong>Music Space</strong> to explore realtime synchronization over the web. Using Flask + Flask-SocketIO, the app lets a group of users listen to the same YouTube audio stream together — actions like play, pause, seek, and resume are broadcast to everyone in the room so playback stays in sync.</p>

          <div class="section">
            <h2>Key highlights</h2>
            <ul class="features">
              <li><strong>Create / Join rooms</strong><br/><span style="color:var(--muted)">Unique 5‑character codes for sessions</span></li>
              <li><strong>Realtime sync</strong><br/><span style="color:var(--muted)">Play/pause/seek/resume via Socket.IO</span></li>
              <li><strong>YouTube audio</strong><br/><span style="color:var(--muted)">yt-dlp extracts the best audio stream without storing video</span></li>
              <li><strong>Server-side persistence</strong><br/><span style="color:var(--muted)">PostgreSQL stores sessions & users</span></li>
              <li><strong>Vanilla frontend</strong><br/><span style="color:var(--muted)">HTML / CSS / JS for simplicity & control</span></li>
              <li><strong>Lightweight</strong><br/><span style="color:var(--muted)">Small codebase easy to extend</span></li>
            </ul>
          </div>

        </div>

        <div class="section card" style="margin-top:14px">
          <h2>Quick install</h2>
          <p style="color:var(--muted)">Run locally — these are the commands I use.</p>
          <pre><code>git clone https://github.com/Kartheek-78/musicspace.git
cd musicspace
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
export YOUTUBE_COOKIES=/path/to/cookies.txt  # optional
python app.py
</code></pre>
        </div>

      </div>

      <div class="right">
        <div class="card">
          <h2>Tech stack</h2>
          <p style="color:var(--muted);margin-top:6px">Flask · Flask-SocketIO · psycopg · yt-dlp · PostgreSQL · HTML/CSS/JS</p>

          <h2 style="margin-top:14px">How it works</h2>
          <p class="how">Host creates a room → users join with code → when a YouTube link is shared, server extracts audio URL via <code>yt-dlp</code> → server broadcasts <em>play</em> with the extracted URL → clients play the stream and share playback updates (time/pause/seek) back to the server for others.</p>
        </div>

        <div class="card" style="margin-top:14px">
          <h2>Screenshots</h2>
          <div class="screenshot">Drop screenshots here (e.g. <code>/static/img/room.png</code>)</div>
        </div>
      </div>
    </div>

    <div class="section columns">
      <div class="card">
        <h2>API & Sockets (notes)</h2>
        <pre><code># Socket events implemented (examples)
join, leave
play -> server extracts audio via yt-dlp and emits play_audio
pause, resume, seek, time_update
get_current -> sends current audio state to requester
</code></pre>
      </div>

      <div class="card">
        <h2>DB schema (summary)</h2>
        <p style="color:var(--muted);margin-top:6px">You need tables to store <code>sessions(code)</code> and <code>session_users(session_code, user_name)</code>. Keep the schema minimal — the app removes sessions with zero users automatically.</p>
        <pre><code>-- example SQL (postgres)
CREATE TABLE sessions(code VARCHAR(8) PRIMARY KEY);
CREATE TABLE session_users(id SERIAL PRIMARY KEY, session_code VARCHAR(8) REFERENCES sessions(code), user_name TEXT);
</code></pre>
      </div>
    </div>

    <div class="section card">
      <h2>Future ideas</h2>
      <ul>
        <li>Upgrade frontend to React for better state management</li>
        <li>Add playlists, moderation, and voting for next song</li>
        <li>Authentication (JWT) & persistent user profiles</li>
        <li>Deploy with Docker + managed Postgres and add CI badges</li>
      </ul>
    </div>

    <footer>
      <div>Made with ☕ and 🎧 — <strong>Kartheek Reddy</strong></div>
      <div>License: <span style="color:var(--muted)">MIT (or change as you like)</span></div>
    </footer>

  </div>
</body>
</html>
