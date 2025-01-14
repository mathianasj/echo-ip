from flask import Flask, request
from flask import jsonify


app = Flask(__name__)

@app.route('/')
def index():
    remote_ip = request.remote_addr
    return jsonify({'ip': request.remote_addr}), 200
