from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import subprocess
import regressor

app = Flask(__name__)
CORS(app)


@app.route('/', methods=["POST", "OPTION"])
def decision():
    content = request.json
    if content['desc'] != "":
        resultPrice = pricePrediction(content['desc'])
        resultSend = {'price': resultPrice}
        return jsonify(resultSend)
    else:
        resultSend = {'price': -1}
        return jsonify(resultSend)

def pricePrediction(description):
    return regressor.input(description)
