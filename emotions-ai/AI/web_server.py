from flask import Flask, jsonify, redirect, render_template, request, g, url_for, json

app: Flask = Flask(__name__)
app.json.ensure_ascii=False # for sending utf-8/unicode characters (emojis). prolly needed, but i wouldnt touch it
vars = {'emoji': '',
        'emotion': '',
        'surety': '',
        'no_face': ''} # instead of using the problematic flask.g, (for global variables), a dict is 1000x better.

@app.route('/')
def home():
    return render_template('index.html', emoji=vars['emoji'])

@app.route('/set_emoji', methods=['POST'])
def set_emoji():
    vars['emoji'] = request.form.get('emoji')
    vars['surety'] = request.form.get('surety')
    vars['emotion'] = request.form.get('emotion')
    vars['no_face'] = request.form.get('no_face')
    if vars['no_face']=='True':
        return f"<span class='emoji'>❔</span>\n<span class='text'> No faces found!</span>"
    return f"<span class='emoji'>{vars['emoji']}</span>\n<span class='text'>{vars['surety']}% sure that you are <span class='emotion'>{vars['emotion']}</span>.</span>"

@app.route('/get_emoji', methods=['GET'])
def get_emoji():
    if vars['no_face']=='True':
        return f"<span class='emoji'>❔</span>\n<span class='text'> No faces found!</span>"
    return f"<span class='emoji'>{vars['emoji']}</span>\n<span class='text'>{vars['surety']}% sure that you are <span class='emotion'>{vars['emotion']}</span>.</span>"

if __name__=="__main__":
    app.run(port=2319, debug=True)
