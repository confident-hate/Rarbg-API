from flask import Flask, request, jsonify
from rarbg import search
from flask_cors import CORS

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
app.secret_key = "i_am_not_feeling_sleepy_so_i_am_coding_this"
CORS(app)


@app.route('/')
def home():
    return 'A rarbg search API for fun :P'


@app.route('/search')
def Search():
    if request.method == 'GET':
        return jsonify(search(request.args.get('q')))


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=9000, use_reloader=True)
