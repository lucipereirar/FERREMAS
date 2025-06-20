import pytest
from ..app import crear_aplicacion

@pytest.fixture
def client():
    app = crear_aplicacion()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_conversion_moneda(client):
    clp = 9500
    response = client.get(f'/api/convertir?clp={clp}')
    assert response.status_code == 200
    data = response.get_json()
    assert "usd" in data
    assert isinstance(data["usd"], float)
    assert data["usd"] > 0 

def test_ruta_inexistente(client):
    response = client.get('/api/404fake')
    assert response.status_code == 404

