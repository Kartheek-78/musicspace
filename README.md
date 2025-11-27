# Music Space — A Real-Time Shared Listening App

Music Space is a full-stack web project I built during my training to understand real-time audio streaming and synchronization across multiple users. The app creates a virtual music room experience where friends can join using a session code and listen to the same YouTube audio together, in perfect sync.

The frontend is built with plain HTML, CSS, and JavaScript to directly work with the DOM and keep control at the basics. The backend runs on Flask, using Flask-SocketIO for WebSocket events, while PostgreSQL stores session codes and active users.

---

## What the app supports right now

- Create or join a room using a unique 5-character session code  
- Instant streaming of best YouTube audio using `yt-dlp`  
- Real-time sync of playback controls: Play, Pause, Resume, Seek  
- Live updates of connected users without page refresh  
- Automatic clean-up of empty rooms from the database  

---

## Tech stack used in this project

| Part | Technology |
|---|---|
| Frontend | HTML, CSS, JavaScript |
| Backend | Python, Flask, Flask-SocketIO |
| Audio Streaming | yt-dlp (extracts best audio stream URL) |
| Database | PostgreSQL, psycopg |
| Real-Time Communication | Socket.IO rooms and WebSocket events |

---

## How the real-time room flow works

```
Host creates room → Session code stored in database  
Users join via code → Names saved to session users  
YouTube link shared → Server extracts best audio URL  
Server broadcasts play → All clients start streaming  
Clients send playback time → Pause/Seek/Resume synced  
Room empties → Session auto-deleted from database
```

---

## Run this project locally

```
git clone (your repo link)
cd musicspace
pip install -r requirements.txt
python app.py
```

Open in browser:
```
localhost:5000
```

---

## Testing approach

APIs and YouTube audio extraction were tested using Postman. Real-time synchronization was validated by opening multiple client tabs and devices connected to the same session.

---

## Things I plan to add next

- Upgrade UI using React  
- Playlist support  
- Song voting for next track  
- Volume and playback speed sync  
- Authentication using JWT  
- Docker container support  
- A proper deployment guide  

---

This project was one of the most hands-on parts of my training and helped me understand complete full-stack flow, especially the real-time and streaming side.

Kartheek Reddy
