from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    if request.method == "POST":
        text = request.form["text"]
        if text.strip():
            with open("01.txt", "a", encoding="utf-8") as f:
                f.write(text.strip() + "\n")
            message = "Copied and saved successfully!"
        else:
            message = "Text cannot be empty."
    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(debug=False, port=5000)
