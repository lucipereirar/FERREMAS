import os
from flask import Flask, send_from_directory

# Ruta absoluta al folder "frontend"
STATIC_FOLDER_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "frontend"))

app = Flask(__name__, static_folder=STATIC_FOLDER_PATH, static_url_path="")

@app.route("/")
def home():
    return send_from_directory(app.static_folder, "index.html")

@app.route("/<path:filename>")
def static_files(filename):
    return send_from_directory(app.static_folder, filename)
