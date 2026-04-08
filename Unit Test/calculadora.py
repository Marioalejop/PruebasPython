class Calculadora:
    """Calculadora básica con operaciones aritméticas."""

    def sumar(self, a, b):
        """Retorna la suma de a y b."""
        return a + b

    def restar(self, a, b):
        """Retorna la diferencia de a y b."""
        return a - b

    def multiplicar(self, a, b):
        """Retorna el producto de a y b."""
        return a * b

    def dividir(self, a, b):
        """Retorna la división de a entre b."""
        if b == 0:
            raise ValueError("No se puede dividir entre cero")
        return a / b

    def potencia(self, base, exponente):
        """Retorna base elevada al exponente."""
        return base ** exponente

    def es_par(self, numero):
        """Retorna True si el número es par."""
        return numero % 2 == 0

print("✅ Clase Calculadora definida correctamente")

