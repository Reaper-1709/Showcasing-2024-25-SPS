# A Brief Overview

- This folder contains source code for the [emotion detection backend](./main.py), and the flask web server's backend and frontend.

# Instructions for Use

- Install all the dependencies:
```bash
pip install -r requirements.txt
```

- First start the emtion detection model:

```bash
python main.py
```
- Then start the flask web server: 

```bash
python web_server.py
```

- Then you can navigate to [http://localhost:2319](http://localhost:2319) in your browser.

# How it works

- `main.py` uses the `fer` python module to detect emotions captured from frames from the webcam. It does not show the user the live webcam feed.
- It detects emotions every 0.1s (10 times/s), and sends a POST request to the Flask REST API (running in `web_server.py`) containing the emotion and the corresponding emoji to display.
- The web server sets the emoji globally in its own scope.
- The web page sends a GET request to the REST API and fetches the emoji and the emotion and its corresponding surety %. This is done with the help of the [HTMX](https://htmx.org) Library, which allows us to use AJAX and other JS functions within HTML. It is [stored locally](./static/htmx.min.js) to avoid the need of an active Internet connection.
- The web server thus sends requests at the same rate (10 times/s) as the fer model, and updates the web page along with it in real time.
