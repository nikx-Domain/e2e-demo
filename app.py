from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>i am a devops engineer</h1><p>Deploys automatically via GitHub & Docker.</p>"

if __name__ == "__main__":
    # Render uses the 'PORT' environment variable
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
