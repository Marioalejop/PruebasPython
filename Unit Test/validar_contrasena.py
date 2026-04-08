import unittest

# ============================================================
# EJERCICIO 1: Código a probar
# ============================================================

def validar_contrasena(contrasena):
    """
    Valida que una contraseña cumpla los requisitos:
    - Al menos 8 caracteres
    - Al menos una mayúscula
    - Al menos un número
    - Al menos un carácter especial: !@#$%

    Retorna (True, 'OK') si es válida,
    o (False, 'mensaje de error') si no lo es.
    """
    if len(contrasena) < 8:
        return False, "Mínimo 8 caracteres"
    if not any(c.isupper() for c in contrasena):
        return False, "Debe tener al menos una mayúscula"
    if not any(c.isdigit() for c in contrasena):
        return False, "Debe tener al menos un número"
    if not any(c in "!@#$%" for c in contrasena):
        return False, "Debe tener al menos un carácter especial (!@#$%)"
    return True, "OK"

# TODO: Escribe tu clase de pruebas aquí
class TestValidarContrasena(unittest.TestCase):
    def test_contrasena_valida(self):
        resultado, mensaje = validar_contrasena("Abcdef1!")
        self.assertTrue(resultado)
        self.assertEqual(mensaje, "OK")

    def test_muy_corta(self):
        resultado, mensaje = validar_contrasena("Ab1!")
        self.assertFalse(resultado)
        self.assertEqual(mensaje, "Mínimo 8 caracteres")

    def test_sin_mayuscula(self):
        resultado, mensaje = validar_contrasena("abcdef1!")
        self.assertFalse(resultado)
        self.assertEqual(mensaje, "Debe tener al menos una mayúscula")

    def test_sin_numero(self):
        resultado, mensaje = validar_contrasena("Abcdefg!")
        self.assertFalse(resultado)
        self.assertEqual(mensaje, "Debe tener al menos un número")

    def test_sin_caracter_especial(self):
        resultado, mensaje = validar_contrasena("Abcdefg1")
        self.assertFalse(resultado)
        self.assertEqual(mensaje, "Debe tener al menos un carácter especial (!@#$%)")

    def test_otro_caracter_especial_no_valido(self):
        resultado, mensaje = validar_contrasena("Abcdefg1*")
        self.assertFalse(resultado)
        self.assertEqual(mensaje, "Debe tener al menos un carácter especial (!@#$%)")
    

suite = unittest.TestLoader().loadTestsFromTestCase(TestValidarContrasena)
unittest.TextTestRunner(verbosity=2).run(suite)