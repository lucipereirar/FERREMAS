from flask import Flask, jsonify, request
import models

app = Flask(__name__)

@app.route('/productos', methods=['GET'])
def listar_productos():
    productos = models.listar_todos_los_productos()
    return jsonify(productos)

if __name__ == '__main__':
    app.run(debug=True, host=' ')