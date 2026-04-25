import pytest
from src.modulo_bonificacion import calcular_bonificacion


def test_promedio_invalido_bajo():
    with pytest.raises(ValueError):
        calcular_bonificacion(-1, 80, False)


def test_promedio_invalido_alto():
    with pytest.raises(ValueError):
        calcular_bonificacion(5.1, 80, False)


def test_asistencia_invalida():
    with pytest.raises(ValueError):
        calcular_bonificacion(4.0, 120, False)


def test_asistencia_menor_70():
    assert calcular_bonificacion(5.0, 69, False) == 0.0


def test_bonificacion_maxima():
    assert calcular_bonificacion(4.8, 98, False) == 0.5


def test_bonificacion_media():
    assert calcular_bonificacion(4.2, 90, False) == 0.3


def test_bonificacion_basica():
    assert calcular_bonificacion(3.7, 80, False) == 0.15


def test_bonificacion_semillero():
    assert calcular_bonificacion(4.5, 95, True) == 0.6


def test_sin_bonificacion():
    assert calcular_bonificacion(3.0, 90, True) == 0.0