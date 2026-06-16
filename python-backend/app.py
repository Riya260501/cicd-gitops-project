from flask import Flask, jsonify
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route("/")
def hello():
    logger.info("GET / called")
    return jsonify({"message": "Python Backend is running!"})

@app.route("/health")
def health():
    logger.info("Health check called")
    return jsonify({"status": "OK"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
