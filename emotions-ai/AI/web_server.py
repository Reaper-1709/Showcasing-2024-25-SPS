"""This module contains code to run the web server and REST API"""

from typing import Dict, List
from flask import Flask, render_template, request

app: Flask = Flask(__name__)
global_variables: Dict[str, str] = {'emoji': '😎',
                         # instead of using the problematic flask.g, (for global variables), a dict
                                    'emotion': 'sad',
                                    'surety': '100%',  # is 1000x better.
                                    'no_face': 'False',
                                    }

songs: Dict[str, List[str]] = {'sad': ['arijit singh']}

@app.route('/')
def home() -> str:
    """Renders the main homepage (index.html) with the specified emoji"""
    return render_template('index.html', emoji=global_variables['emoji'], movies=global_variables['movies'])


@app.route('/set_emoji', methods=['POST'])
def set_emoji() -> str:
    """POST /set_emoji endpoint to set the emoji and other data"""
    global_variables['emoji'] = str(request.form.get('emoji'))
    global_variables['surety'] = str(request.form.get('surety'))
    global_variables['emotion'] = str(request.form.get('emotion'))
    global_variables['no_face'] = str(request.form.get('no_face'))
    if global_variables['no_face'] == 'True':
        return "<span class='emoji'>❔</span>\n<span class='text'> No faces found!</span>"
    return f"<span class='emoji'>{global_variables['emoji']}</span>\n<span class='text'>" \
        "{global_variables['surety']}% sure that you are <span class='emotion'>" \
        "{global_variables['emotion']}</span>.</span>"


@app.route('/get_emoji', methods=['GET'])
def get_emoji() -> str:
    """GET /get_emoji enpoint to fetch current emoji and other data"""
    if global_variables['no_face'] == 'True':
        return "<span class='emoji'>❔</span>\n<span class='text'> No faces found!</span>"
    return f"<span class='emoji'>{global_variables['emoji']}</span>\n<span class='text'>" \
        f"{global_variables['surety']}% sure that you are <span class='emotion'>" \
        f"{global_variables['emotion']}</span>.</span>"

@app.route('/get_songs', methods=['GET'])
def get_songs() -> str:
    pass

def tablize(content: List[str], html_class: str) -> str:
    fin_str: str = f'<table class="{html_class}>'



if __name__ == "__main__":
    app.run(port=2319, debug=True)
