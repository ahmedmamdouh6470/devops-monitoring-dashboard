from flask import Flask, jsonify
from datetime import datetime
import os
import platform
import time

app = Flask(__name__)

START_TIME = time.time()


@app.route("/")
def home():
    return """
    <h1>DevOps Monitoring Dashboard</h1>
    <p>Application is running successfully!</p>
    <p>Available endpoints:</p>
    <ul>
        <li><a href="/health">Health Check</a></li>
        <li><a href="/system-info">System Information</a></li>
    </ul>
    """


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now().isoformat()
    })


@app.route("/system-info")
def system_info():
    return jsonify({
        "hostname": platform.node(),
        "operating_system": platform.system(),
        "python_version": platform.python_version(),
        "uptime_seconds": round(time.time() - START_TIME, 2),
        "environment": os.getenv("APP_ENV", "development")
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
