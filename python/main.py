from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import subprocess
import Regressor

app = Flask(__name__)
CORS(app)


@app.route('/', methods=["POST", "OPTION"])
def decision():
    content = request.form.get("desc")
    if content is not "":
        #resultPrice = pricePrediction(content)
        resultPrice = 32
        resultSend = {'price': resultPrice}
        return jsonify(resultSend)
    else:
        resultSend = {'price': -1}
        return jsonify(resultSend)

def pricePrediction(description):
    return Regressor.predict(description)

app.run('0.0.0.0')