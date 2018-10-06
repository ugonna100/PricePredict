from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import subprocess

app = Flask(__name__)
CORS(app)


@app.route('/', methods=["POST", "OPTION"])
def decision():
    html = "<h3>Hello you're here</h3>"
    content = request.json