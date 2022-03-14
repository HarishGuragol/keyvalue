from flask import Flask, render_template, request
from flask_cors import CORS

import json

app=Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route(f'/fetch', methods=['GET', 'POST'])
def fetch_data():
    with open('data.json', 'r') as f:
        data = f.read()
    return json.dumps(data), 200, {'ContentType':'application/json'}

@app.route('/store', methods=['POST'])
def store_data():
    data = request.get_json()
    with open('data.json', 'w') as f:
        f.write(json.dumps(data))

    return json.dumps({'success':True}), 200, {'ContentType':'application/json'}

if __name__=="__main__":
    app.run()
