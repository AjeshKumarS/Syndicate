from flask import Flask, jsonify, request

app = Flask(__name__)

densities = []


@app.route("/")
def hello():
    return jsonify({"heel": "llo"})


@app.route("/setDensities")
def setDensities():
    print(request.args.get("l1"))
    return "ok"


# def server():
app.run(debug=True)
