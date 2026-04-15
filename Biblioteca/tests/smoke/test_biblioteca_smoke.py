import pytest
import requests

BASE = 'http://localhost:8000/api'

@pytest.mark.smoke
class TestBibliotecaSmoke:

    def test_01_api_disponible(self):
        r = requests.get(f"{BASE}/health")
        assert r.status_code == 200
        assert r.json()["status"] == "ok"

    def test_02_login_funciona(self):
        r = requests.post(f"{BASE}/auth/login", json={
            "username": "admin",
            "password": "123"
        })
        assert r.status_code == 200
        assert "access_token" in r.json()

    def test_03_listar_libros(self):
        r = requests.get(f"{BASE}/libros")
        assert r.status_code == 200
        assert isinstance(r.json(), list)

    def test_04_db_conectada(self):
        r = requests.get(f"{BASE}/health")
        assert r.json()["db"] == "connected"

    def test_05_modulo_multas(self):
        r = requests.get(f"{BASE}/multas/1")
        assert r.status_code == 200
        assert "multa_total" in r.json()