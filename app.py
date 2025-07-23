from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS so your frontend on Netlify can access this API

@app.route("/save", methods=["POST"])
def save_text():
    data = request.get_json()
    if not data:
        return jsonify({"message": "No JSON data received"}), 400

    text = data.get("text", "").strip()
    if not text:
        return jsonify({"message": "Empty text!"}), 400

    try:
        with open("01.txt", "a", encoding="utf-8") as f:
            f.write(text + "\n")
        return jsonify({"message": "Saved successfully!"}), 200
    except Exception as e:
        return jsonify({"message": f"Failed to save text: {str(e)}"}), 500

@app.route("/")
def home():
    return jsonify({"message": "API running"}), 200

if __name__ == "__main__":
    app.run(debug=True)
