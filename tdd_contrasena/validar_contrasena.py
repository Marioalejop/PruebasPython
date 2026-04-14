import re

def validar_contrasena(password: str) -> dict:
    reglas = [
        (len(password) < 8, "Debe tener minimo 8 caracteres"),
        (not re.search(r'[A-Z]', password), "Debe tener al menos una mayuscula"),
        (not re.search(r'[a-z]', password), "Debe tener al menos una minuscula"),
        (not re.search(r'\d', password), "Debe tener al menos un numero"),
        (not re.search(r'[!@#$%^&*]', password), "Debe tener al menos un caracter especial"),
    ]

    errores = [mensaje for condicion, mensaje in reglas if condicion]

    return {
        'es_valida': len(errores) == 0,
        'errores': errores
    }