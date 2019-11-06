from flask import Flask, jsonify, request

app = Flask(__name__)

densities = []


@app.route("/")
def hello():
    return jsonify({"heel": "llo"})


@app.route("/setDensities")
def setDensities():
    global densities
    densities = [
        request.args.get("l1"),
        request.args.get("l2"),
        request.args.get("l3"),
        request.args.get("l4"),
    ]
    print(request.args.get("l1"))
    return "ok"


@app.route("/getDensities")
def getDensities():
    return jsonify({"dens": densities})


# def server():
app.run(debug=True)
