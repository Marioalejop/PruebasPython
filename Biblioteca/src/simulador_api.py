from fastapi import FastAPI
from src.biblioteca import Biblioteca, Multa

app = FastAPI()
biblioteca = Biblioteca()

@app.get("/api/health")
def health():
    return {"status": "ok", "db": "connected"}


@app.post("/api/auth/login")
def login():
    return {
        "access_token": "fake-token",
        "user": {"id": 1, "name": "admin"}
    }


@app.get("/api/libros")
def libros():
    return [
        {"id": 1, "titulo": "Python", "disponible": biblioteca.calcular_disponibilidad(1)},
        {"id": 2, "titulo": "Testing", "disponible": biblioteca.calcular_disponibilidad(2)}
    ]


@app.post("/api/prestamos")
def prestamos():
    biblioteca.registrar_prestamo(1)
    return {"prestamo_id": 1, "libro_id": 1, "fecha_devolucion": "2026-04-20"}


@app.post("/api/devoluciones")
def devoluciones():
    biblioteca.registrar_devolucion(1)
    return {"multa": 0.0, "estado": "devuelto"}


@app.get("/api/multas/{estudiante}")
def multas(estudiante: int):
    multa = Multa.calcular_multa(0)
    return {"multa_total": multa, "prestamos_vencidos": 0}