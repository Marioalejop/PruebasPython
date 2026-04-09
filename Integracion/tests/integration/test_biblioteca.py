import pytest
from models import Libro

def test_agregar_libro_persiste_en_bd(servicio, session):
    libro = servicio.agregar_libro('El Quijote', 'Cervantes')
    resultado = session.get(Libro, libro.id)
    assert resultado is not None
    assert resultado.titulo == 'El Quijote'
    assert resultado.disponible is True

def test_prestar_libro_cambia_disponibilidad(servicio):
    servicio.agregar_libro('Cien AÃ±os', 'GarcÃ­a MÃ¡rquez')
    prestado = servicio.prestar_libro('Cien AÃ±os')
    assert prestado.disponible is False

def test_prestar_libro_inexistente_lanza_error(servicio):
    with pytest.raises(LookupError):
        servicio.prestar_libro('Libro Fantasma')
