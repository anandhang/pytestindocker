from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/ping", methods=["GET"])
def ping():
    return jsonify({"message":"pong"}), 200

@app.route("/add", methods=["POST"])
def add():
    data = request.get_json(silent=True)
    print("DEBUG: received data:", data)
    if not data or "a" not in data or "b" not in data:
        return jsonify({"error": "Invalid input"}), 400
    try:
        result = int(data["a"]) + int(data["b"])
        return jsonify({"result": result}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)