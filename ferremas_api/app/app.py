import os
from flask import Flask, send_from_directory

# Ruta absoluta a la carpeta frontend
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
static_folder_path = os.path.join(BASE_DIR, '..', 'frontend')

app = Flask(__name__, static_folder=static_folder_path, static_url_path='')

@app.route("/")
def home():
    return send_from_directory(static_folder_path, "index.html")

@app.route("/<path:filename>")
def static_files(filename):
    return send_from_directory(static_folder_path, filename)
