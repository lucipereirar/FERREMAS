from flask import Blueprint, request, jsonify

contacto_api = Blueprint('contacto_api', __name__)

@contacto_api.route('/api/contacto', methods=['POST'])
def recibir_mensaje():
    data = request.get_json()
    
    if not data or not all(k in data for k in ("nombre", "email", "mensaje")):
        return jsonify({"mensaje": "Faltan datos"}), 400
    
    nombre = data['nombre']
    email = data['email']   
    mensaje = data.get('mensaje')
    fecha = data.get('fecha', None)

    with open('contacto.txt', 'a', encoding="utf-8") as archivo:
        archivo.write(f"[{fecha}] {nombre} ({email}): {mensaje}\n")
    return jsonify({"mensaje": "Mensaje recibido exitosamente"}), 200