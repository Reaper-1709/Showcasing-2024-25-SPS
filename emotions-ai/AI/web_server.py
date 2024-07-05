"""This module contains code to run the web server and REST API"""

from typing import Dict, List
from flask import Flask, render_template, request

app: Flask = Flask(__name__)
global_variables: Dict[str, str] = {'emoji': '😎',
                                    # instead of using the problematic flask.g, (for global variables), a dict
                                    'emotion': 'sad',
                                    'surety': '100',  # is 1000x better.
                                    'no_face': 'False',
                                    }

books: Dict[str, List[str]] = {'sad': ['Someone Like You (by Adele)', 'Stay With Me (by Sam Smith)', 'Muskurane Ki Wajah Tum Ho (by Arijit Singh)'],
                               'happy': ['Happy (by Pharrell Williams)', 'Can\'t Stop the Feeling! (by Justin Timberlake)', 'Khwabon Ke Parinde (by A.R. Rahman)'],
                               'neutral': [],
                               'angry': ['The Way I Am (by Eminem)', 'In The End (by Linkin Park)', 'Jee Karda (by Divya Kumar)'],
                               'fear': ['Thriller (by Michael Jackson)', 'Disturbia (by Rihanna)', 'Aayega Aanewala (by Lata Mangeshkar)'],
                               'surprise': [],
                               'disgust': []}

songs: Dict[str, List[str]] = {'sad': ['The Kite Runner (by Khaled Hosseini)', 'A Little Life (by Hanya Yanagihara'],
                               'happy': ['The Alchemist (by Paulo Coelho)', 'To Kill a Mockingbird (by Harper Lee)'],
                               'neutral': [],
                               'angry': ['Anger Management For Dummies', 'Why We Get Mad (by Daniel H. Pink'],
                               'fear': ['The Exorcist (by William Blatty)', 'Salem\'s Lot (by Stephen King)'],
                               'surprise': [],
                               'disgust': []}


@app.route('/')
def home() -> str:
    """Renders the main homepage (index.html) with the specified emoji"""
    return render_template('index.html', emoji=global_variables['emoji'], )


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


@app.route('/get_books', methods=['GET'])
def get_books() -> str:
    return tablize(content=books[global_variables['emotion']], html_id='booktable', title='Books')


@app.route('/get_songs', methods=['GET'])
def get_songs() -> str:
    return tablize(content=songs[global_variables['emotion']], html_id='songtable', title='Songs')


def tablize(content: List[str], html_id: str, title: str) -> str:
    fin_str: str = f'''<table id="{html_id}"><thead><tr><th>{title}</th></tr></thead><body>'''
    for el in content:
        fin_str += f'''<tr><td>{el}</td></tr>'''
        continue
    fin_str += '''</tbody></table>'''
    return fin_str


if __name__ == "__main__":
    app.run(port=2319, debug=True)
