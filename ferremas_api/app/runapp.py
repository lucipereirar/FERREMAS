from flask import Flask
from routes import productos_api
import db as database
from flask import Flask, send_from_directory

app = Flask(__name__)
app.register_blueprint(productos_api)

@app.route('/')
def home():
    return send_from_directory('frontend', 'index.html')

@app.route('/<path:archivo>')
def servir_estaticos(archivo):
    return send_from_directory('frontend', archivo)

@app.route('/js/<path:archivo>')
def servir_js(archivo):
    return send_from_directory('frontend/js', archivo)

if __name__ == "__main__":
    from app import app
    app.run(debug=True)