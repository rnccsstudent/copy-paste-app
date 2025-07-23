from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow access from frontend (Netlify)

@app.route("/save", methods=["POST"])
def save_text():
    data = request.json
    text = data.get("text", "").strip()
    if text:
        with open("01.txt", "a", encoding="utf-8") as f:
            f.write(text + "\n")
        return {"message": "Saved successfully!"}
    return {"message": "Empty text!"}, 400

@app.route("/")
def home():
    return "API running"

