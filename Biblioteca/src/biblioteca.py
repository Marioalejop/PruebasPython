from datetime import datetime

class Multa:
    TARIFA_DIARIA = 500

    @staticmethod
    def calcular_multa(dias_retraso):
        return dias_retraso * Multa.TARIFA_DIARIA


class Biblioteca:
    def __init__(self):
        self.prestamos = {}

    def registrar_prestamo(self, libro_id, fecha_prestamo=None):
        if fecha_prestamo is None:
            fecha_prestamo = datetime.now()

        self.prestamos[libro_id] = {
            "fecha_prestamo": fecha_prestamo,
            "devuelto": False
        }

    def registrar_devolucion(self, libro_id):
        if libro_id in self.prestamos:
            self.prestamos[libro_id]["devuelto"] = True

    def calcular_disponibilidad(self, libro_id):
        if libro_id not in self.prestamos:
            return True

        prestamo = self.prestamos[libro_id]

        if prestamo["devuelto"]:
            return True

        return False