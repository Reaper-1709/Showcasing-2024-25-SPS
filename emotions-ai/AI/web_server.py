from flask import Flask, jsonify, redirect, render_template, request, g, url_for, json

app: Flask = Flask(__name__)
app.json.ensure_ascii=False # for sending utf-8/unicode characters (emojis). prolly needed, but i wouldnt touch it
vars = {'emoji': ''} # instead of using the problematic flask.g, (for global variables), a dict is 1000x better.

@app.route('/')
def home():
    return render_template('index.html', emoji=vars['emoji'])

@app.route('/set_emoji', methods=['POST'])
def set_emoji():
    vars['emoji'] = request.form.get('emoji')
    return vars['emoji']

@app.route('/get_emoji', methods=['GET'])
def get_emoji():
    return vars['emoji']

if __name__=="__main__":
    app.run(port=2319, debug=True)
