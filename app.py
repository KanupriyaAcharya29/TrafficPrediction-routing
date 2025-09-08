from flask import Flask, request, jsonify
from router import build_graph, get_best_route

app = Flask(_name_)
G = build_graph()

@app.route("/route", methods=["GET"])
def route():
    source = int(request.args.get("source", 0))
    target = int(request.args.get("target", 4))
    path = get_best_route(G, source, target)
    return jsonify({"best_path": path})

if _name_ == "_main_":
    app.run(port=5000, debug=True)