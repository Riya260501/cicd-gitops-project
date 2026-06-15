import logging
import os
from flask import Flask, jsonify

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s - %(message)s"
)
logger = logging.getLogger("python-backend")
app = Flask(__name__)

@app.route("/")
def home():
    logger.info("GET / called")
    return jsonify({"service": "python-backend", "status": "running"})

@app.route("/health")
def health():
    logger.info("Health check OK")
    return jsonify({"status": "healthy"}), 200

@app.route("/api/data")
def data():
    logger.info("GET /api/data called")
    return jsonify({
        "source": "python-backend",
        "message": "Hello from Python Flask service",
        "items": ["item-1", "item-2", "item-3"]
    })

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    logger.info(f"Starting Python backend on port {port}")
    app.run(host="0.0.0.0", port=port)
