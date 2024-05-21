# A Brief Overview

- This folder contains source code for the [emotion detection backend](./main.py), and the flask web server's backend and frontend.

# Instructions for Use

- First start the emtion detection model:

```bash
python main.py
```
- Then start the flask web server: 

```bash
python web_server.py
```

- Then you can navigate to [http://localhost:8000](http://localhost:8000) in your browser.

# How it works

- `main.py` uses the `fer` python module to detect emotions captured from frames from the webcam. It does not show the user the live webcam feed.
- It detects emotions at variable FPSes (currently 10 FPS), and sends a POST request to the Flask REST API (running in `web_server.py`).
- The web server recieves the emoji required and sebsequently updates the web page to show the respective emoji. (WIP)
