from validar_contrasena import validar_contrasena

def test_contrasena_valida():
    r = validar_contrasena('Secure#123')
    assert r['es_valida'] == True
    assert r['errores'] == []

def test_contrasena_muy_corta():
    r = validar_contrasena('Ab1!')
    assert r['es_valida'] == False
    assert any('8' in e or 'longitud' in e.lower() for e in r['errores'])

def test_contrasena_sin_mayusculas():
    r = validar_contrasena('secure#123')
    assert r['es_valida'] == False
    assert any('mayusc' in e.lower() for e in r['errores'])

def test_contrasena_sin_numeros():
    r = validar_contrasena('Secure#abc')
    assert r['es_valida'] == False
    assert any('numero' in e.lower() for e in r['errores'])

def test_contrasena_sin_especiales():
    r = validar_contrasena('Secure123')
    assert r['es_valida'] == False
    assert any('especial' in e.lower() for e in r['errores'])

def test_contrasena_multiples_errores():
    r = validar_contrasena('abc')
    assert r['es_valida'] == False
    assert len(r['errores']) >= 3