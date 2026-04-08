import unittest
from unittest.mock import Mock
# ============================================================
# EJERCICIO 2: Código a probar
# ============================================================

class CarritoCompras:
    """
    Carrito que verifica disponibilidad en un servicio de inventario externo.
    """
    def __init__(self, servicio_inventario):
        self.inventario = servicio_inventario
        self.items = []

    def agregar_producto(self, producto_id, cantidad):
        """Agrega producto si hay stock disponible."""
        stock = self.inventario.consultar_stock(producto_id)
        if stock < cantidad:
            raise ValueError(f"Stock insuficiente. Disponible: {stock}")
        self.items.append({"producto_id": producto_id, "cantidad": cantidad})
        return True

    def total_items(self):
        return sum(item["cantidad"] for item in self.items)

    def vaciar(self):
        self.items = []

# TODO: Escribe tus pruebas aquí usando Mock
class TestCarritoCompras(unittest.TestCase):

    def setUp(self):
        # Se crea un mock del servicio de inventario
        self.mock_inventario = Mock()
        self.carrito = CarritoCompras(self.mock_inventario)

    def test_agregar_producto_con_stock_suficiente(self):
        # Se simula que hay stock suficiente
        self.mock_inventario.consultar_stock.return_value = 10

        resultado = self.carrito.agregar_producto("producto1", 3)

        self.assertTrue(resultado)
        self.assertEqual(self.carrito.total_items(), 3)

    def test_agregar_producto_sin_stock(self):
        # Se simula poco stock
        self.mock_inventario.consultar_stock.return_value = 2

        with self.assertRaises(ValueError):
            self.carrito.agregar_producto("producto1", 5)

    def test_total_items_varios_productos(self):
        self.mock_inventario.consultar_stock.return_value = 10

        self.carrito.agregar_producto("p1", 2)
        self.carrito.agregar_producto("p2", 3)

        self.assertEqual(self.carrito.total_items(), 5)

    def test_vaciar_carrito(self):
        self.mock_inventario.consultar_stock.return_value = 10

        self.carrito.agregar_producto("p1", 2)
        self.carrito.vaciar()

        self.assertEqual(self.carrito.total_items(), 0)

    def test_se_llama_consultar_stock(self):
        self.mock_inventario.consultar_stock.return_value = 10

        self.carrito.agregar_producto("p1", 1)

        # Verificación de que se llamó correctamente
        self.mock_inventario.consultar_stock.assert_called_with("p1")
        
suite = unittest.TestLoader().loadTestsFromTestCase(TestCarritoCompras)
unittest.TextTestRunner(verbosity=2).run(suite)

