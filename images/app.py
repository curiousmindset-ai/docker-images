from flask import Flask
import os

app = Flask(__name__)

@app.get("/")
def home():
    return {
        "message": "Greetings Dom Iorfino 🚀",
        "hostname": os.uname().nodename
    }

@app.get("/healthz")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    # Bind to all interfaces for containers
    app.run(host="0.0.0.0", port=8080)
