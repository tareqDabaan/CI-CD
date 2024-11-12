from flask import Flask
import os
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, CI/CD"

if __name__ == "__main__":
    # Get the port from environment variable, or default to 5000 for local dev
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    