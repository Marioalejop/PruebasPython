"""
Tests Ejercicio 4 — Property-Based Testing con Hypothesis
revertir, es_palindromo, concatenar_lista
"""

from hypothesis import given, strategies as st
from src.ejercicio_4 import (
    revertir,
    es_palindromo,
    concatenar_lista,
)


# PROPIEDAD 1: revertir es involutiva
@given(st.text())
def test_propiedad_revertir_dos_veces(texto):
    """
    Revertir una cadena dos veces devuelve la original.
    """
    assert revertir(revertir(texto)) == texto


# PROPIEDAD 2: texto + su reverso siempre es palíndromo
@given(
    st.text(
        alphabet=st.characters(
            whitelist_categories=("L",),
            max_codepoint=127,
        ),
        min_size=1,
    )
)
def test_propiedad_cadena_mas_reverso(texto):
    """
    Toda cadena concatenada con su reverso
    debe formar un palíndromo.
    """
    palindromo = texto + revertir(texto)
    assert es_palindromo(palindromo) is True


# PROPIEDAD 3: concatenar conserva la cantidad de elementos
@given(
    st.lists(
        st.text(
            alphabet="ABCDEFGHIJKLMN",
            min_size=1,
        ),
        min_size=1,
    ),
    st.sampled_from(["-", "|", ",", "/"]),
)
def test_propiedad_concatenar_preserva_cantidad(lista, separador):
    """
    La cantidad de elementos se conserva al concatenar y dividir,
    siempre que el separador no aparezca en los elementos.
    """
    resultado = concatenar_lista(lista, separador)
    assert len(resultado.split(separador)) == len(lista)


# PROPIEDAD 4: revertir conserva la longitud
@given(st.text())
def test_propiedad_revertir_preserva_longitud(texto):
    """
    Revertir una cadena no altera su longitud.
    """
    assert len(revertir(texto)) == len(texto)


# PROPIEDAD 5: concatenar y luego split recupera la lista
@given(
    st.lists(
        st.text(
            alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ",
            min_size=1,
        ),
        min_size=0,
    ),
    st.sampled_from(["-", "|", ",", "/", ";"]),
)
def test_propiedad_concatenar_split_recupera_lista(lista, separador):
    """
    Si el separador no aparece en los elementos,
    concatenar y luego dividir recupera la lista original.
    """
    resultado = concatenar_lista(lista, separador)

    if lista:
        assert resultado.split(separador) == lista
    else:
        assert resultado == ""