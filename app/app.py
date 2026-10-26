from flask import Flask, jsonify

app = Flask(__name__)

VERSION = "1.0.0"

@app.route("/demo")
def demo():
    return jsonify({
        "application": "demo-microservice",
        "version": VERSION,
        "status": "running"
    })

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
