from flask import Flask, render_template, request, g

app: Flask = Flask(__name__)


@app.route('/')
def home():
    g.emoji = 'hello'
    return render_template('index.html')

@app.route('/set_emoji', methods=['POST', 'GET'])
def get_emoji():
    g.emoji = request.args.get('emoji')
    set_emoji()
    return g.emoji

@app.context_processor
def set_emoji():
    return {'emoji': g.emoji}


if __name__=="__main__":
    app.run(port=2319, debug=True)
