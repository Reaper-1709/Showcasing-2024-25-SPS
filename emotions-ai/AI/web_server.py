"""This module contains code to run the web server and REST API"""

from typing import Dict
from flask import Flask, render_template, request

app: Flask = Flask(__name__)
global_variables: Dict[str, str] = {'emoji': '',
                         # instead of using the problematic flask.g, (for global variables), a dict
                                    'emotion': '',
                                    'surety': '',  # is 1000x better.
                                    'no_face': ''}


@app.route('/')
def home():
    """Renders the main homepage (index.html) with the specified emoji"""
    return render_template('index.html', emoji=global_variables['emoji'])


@app.route('/set_emoji', methods=['POST'])
def set_emoji():
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
def get_emoji():
    """GET /get_emoji enpoint to fetch current emoji and other data"""
    if global_variables['no_face'] == 'True':
        return "<span class='emoji'>❔</span>\n<span class='text'> No faces found!</span>"
    return f"<span class='emoji'>{global_variables['emoji']}</span>\n<span class='text'>" \
        f"{global_variables['surety']}% sure that you are <span class='emotion'>" \
        f"{global_variables['emotion']}</span>.</span>"


if __name__ == "__main__":
    app.run(port=2319, debug=True)
