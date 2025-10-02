import os
from flask import Flask, render_template, jsonify

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # project root
TEMPLATE_DIR = os.path.join(BASE_DIR, "frontend", "templates")
STATIC_DIR = os.path.join(BASE_DIR, "frontend", "static")

app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/message")
def get_message():
    return jsonify({"message": "Hello from Flask Backend!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
