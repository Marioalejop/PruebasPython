import pytest
from datetime import datetime, timedelta
from src.biblioteca import Biblioteca, Multa

@pytest.mark.regression
class TestPrestamosRegression:

    def setup_method(self):
        self.biblioteca = Biblioteca()

    def test_libro_prestado_no_disponible(self):
        self.biblioteca.registrar_prestamo(1)
        assert self.biblioteca.calcular_disponibilidad(1) == False

    def test_libro_disponible_tras_devolucion(self):
        self.biblioteca.registrar_prestamo(2)
        self.biblioteca.registrar_devolucion(2)
        assert self.biblioteca.calcular_disponibilidad(2) == True

    def test_bug_2024_031(self):
        fecha = datetime.now() - timedelta(days=45)
        self.biblioteca.registrar_prestamo(3, fecha)
        assert self.biblioteca.calcular_disponibilidad(3) == False

    def test_multa_no_afecta_otro_libro(self):
        self.biblioteca.registrar_prestamo(4)
        assert self.biblioteca.calcular_disponibilidad(5) == True

    def test_calculo_multa(self):
        assert Multa.calcular_multa(3) == 1500