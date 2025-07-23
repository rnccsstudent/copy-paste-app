from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

FILE_PATH = "01.txt"

@app.route("/save", methods=["POST"])
def save_text():
    data = request.json
    text = data.get("text", "").strip()
    if text:
        with open(FILE_PATH, "a", encoding="utf-8") as f:
            f.write(text + "\n")
        return {"message": "Saved successfully!"}
    return {"message": "Empty text!"}, 400

@app.route("/download", methods=["GET"])
def download_text():
    if os.path.exists(FILE_PATH):
        return send_file(FILE_PATH, as_attachment=True, download_name="copy.txt")
    return {"message": "File not found"}, 404

@app.route("/view", methods=["GET"])
def view_text():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r", encoding="utf-8") as f:
            return jsonify({"content": f.read()})
    return jsonify({"content": ""})

@app.route("/delete", methods=["DELETE"])
def delete_file():
    if os.path.exists(FILE_PATH):
        os.remove(FILE_PATH)
        return {"message": "File deleted"}
    return {"message": "File not found"}, 404

@app.route("/")
def home():
    return "API running"
