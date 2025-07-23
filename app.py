from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

FILE_PATH = "01.txt"

@app.route("/save", methods=["POST"])
def save_text():
    data = request.get_json()
    if not data:
        return jsonify({"message": "No JSON data received"}), 400

    text = data.get("text", "").strip()
    if not text:
        return jsonify({"message": "Empty text!"}), 400

    try:
        with open(FILE_PATH, "a", encoding="utf-8") as f:
            f.write(text + "\n")
        return jsonify({"message": "Saved successfully!"}), 200
    except Exception as e:
        return jsonify({"message": f"Failed to save text: {str(e)}"}), 500

@app.route("/view", methods=["GET"])
def view_text():
    if not os.path.exists(FILE_PATH):
        return jsonify({"content": ""})
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        content = f.read()
    return jsonify({"content": content})

@app.route("/download", methods=["GET"])
def download_text():
    if not os.path.exists(FILE_PATH):
        return "File not found", 404
    return send_file(FILE_PATH, as_attachment=True)

@app.route("/delete", methods=["DELETE"])
def delete_file():
    if os.path.exists(FILE_PATH):
        os.remove(FILE_PATH)
        return jsonify({"message": "File deleted successfully!"})
    return jsonify({"message": "File does not exist!"}), 404

@app.route("/")
def home():
    return jsonify({"message": "API running"}), 200

if __name__ == "__main__":
    app.run(debug=True)
