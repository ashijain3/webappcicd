from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Home page -> load frontend (index.html)
@app.route("/")
def home():
    return render_template("index.html")

# Simple API endpoint
@app.route("/api/message")
def get_message():
    return jsonify({"message": "Hello from Flask Backend!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
