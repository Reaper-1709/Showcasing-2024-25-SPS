from flask import Flask, jsonify, redirect, render_template, request, g, url_for, json

app: Flask = Flask(__name__)
app.json.ensure_ascii=False # for sending utf-8/unicode characters (emojis). prolly needed, but i wouldnt touch it
vars = {'emoji': '',
        'emotion': '',
        'surety': ''} # instead of using the problematic flask.g, (for global variables), a dict is 1000x better.

@app.route('/')
def home():
    return render_template('index.html', emoji=vars['emoji'])

@app.route('/set_emoji', methods=['POST'])
def set_emoji():
    vars['emoji'] = request.form.get('emoji')
    vars['surety'] = request.form.get('surety')
    vars['emotion'] = request.form.get('emotion')
    return f"<span class='emoji'>{vars['emoji']}</span>\n<span class='text'>{vars['surety']}% sure that you are {vars['emotion']}.</span>"

@app.route('/get_emoji', methods=['GET'])
def get_emoji():
    return f"<span class='emoji'>{vars['emoji']}</span>\n<span class='text'>{vars['surety']}% sure that you are {vars['emotion']}.</span>"


if __name__=="__main__":
    app.run(port=2319, debug=True)
