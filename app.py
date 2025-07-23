from flask import Flask, request, jsonify, make_response
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow frontend requests

@app.route("/save", methods=["POST"])
def save_text():
    data = request.get_json()
    if not data:
        return jsonify({"message": "No JSON data received"}), 400

    text = data.get("text", "").strip()
    if not text:
        return jsonify({"message": "Empty text!"}), 400

    response = make_response(text)
    response.headers.set("Content-Type", "text/plain")
    response.headers.set("Content-Disposition", "attachment", filename="copied.txt")
    return response

@app.route("/")
def home():
    return jsonify({"message": "API running"}), 200

if __name__ == "__main__":
    app.run(debug=True)
