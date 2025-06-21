from flask import Blueprint, request, jsonify

contacto_api = Blueprint('contacto_api', __name__)

@contacto_api.route('/api/contacto', methods=['POST'])
def recibir_mensaje():
    data = request.json
    if data and all(k in data for k in ("nombre", "email", "mensaje")):
        return jsonify({"mensaje": "Mensaje recibido correctamente"})
    return jsonify({"mensaje": "Faltan datos"}), 400