from flask import Flask, jsonify, request, make_response

app = Flask(__name__)

densities = []
fixed = []


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
    return "Density successfully set"


@app.route("/setFixed")
def setFixed():
    global fixed
    fixed = [
        request.args.get("l1"),
        request.args.get("l2"),
        request.args.get("l3"),
        request.args.get("l4"),
    ]
    return "Fixed timing density successfully set"


@app.route("/getDensities")
def getDensities():
    res = make_response(jsonify({"dens": densities}))
    res.headers["Access-Control-Allow-Origin"] = "*"
    return res


@app.route("/getFixed")
def getFixed():
    res = make_response(jsonify({"dens": fixed}))
    res.headers["Access-Control-Allow-Origin"] = "*"
    return res


# def server():
app.run(debug=True)
