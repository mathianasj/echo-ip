from flask import Flask, request
from flask import jsonify
import pprint



app = Flask(__name__)

@app.route('/')
def index():
    remote_ip = request.remote_addr
    pprint.pprint(('REQUEST', env), stream=errorlog)
    return jsonify({'ip': request.remote_addr}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0")
