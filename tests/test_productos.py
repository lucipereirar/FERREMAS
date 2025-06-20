import pytest_lazyfixture
from app import crear_aplicacion

@pytest.fixture
def client():
    app = crear_aplicacion()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# 1. Obtener productos (esperado 200)
def test_get_productos(client):
    response = client.get('/api/productos')
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)

# 2. Obtener productos con mal método (esperado 405)
def test_post_in_get_productos(client):
    response = client.post('/api/productos')
    assert response.status_code == 405

# 3. Agregar producto con datos válidos
def test_add_producto_valido(client):
    response = client.post('/api/productos', json={
        "codigo": "H001",
        "marca": "Truper",
        "nombre": "Martillo",
        "precio": 4500,
        "modelo": "PRO",
        "stock": 25
    })
    assert response.status_code in [200, 201]

# 4. Agregar producto con JSON inválido
def test_add_producto_invalido(client):
    response = client.post('/api/productos', data="no json")
    assert response.status_code in [400, 422]
