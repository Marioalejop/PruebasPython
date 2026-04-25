# Soluciones Ejercicios Resueltos — Sesión 12
## Testing Dinámico · Mutation Testing · Property-Based Testing

**Materia:** Pruebas de Software (7mo Semestre)  
**Universidad:** Universitaria de Colombia  
**Docente:** Mg. Sergio Alejandro Burbano Mena  
**Estudiante:** Alejandro Peña  
**Fecha:** Abril de 2026  

---

## Descripción

Este repositorio contiene la solución completa del taller de la Sesión 12 de Pruebas de Software. Se implementaron y validaron diferentes técnicas de testing utilizando Python y Pytest, incluyendo:

- Clases de Equivalencia (Equivalence Partitioning).
- Análisis de Valores Límite (Boundary Value Analysis).
- Cobertura de Ramas (Branch Coverage).
- Property-Based Testing con Hypothesis.
- Pruebas unitarias para un módulo adicional de bonificación académica.

> **Nota:** Mutation Testing fue analizado conceptualmente. La herramienta `mutmut` requiere WSL en Windows, por lo que no se ejecutó en el entorno local.

Todos los módulos alcanzan una cobertura del 100%.

---

## Resultados Globales

```text
49 pruebas ejecutadas
49 pruebas exitosas
0 pruebas fallidas
Cobertura global: 100%
```

---

## Property-Based Testing

Se implementaron cinco propiedades utilizando Hypothesis:

- Revertir una cadena dos veces devuelve el texto original.
- Toda cadena concatenada con su reverso forma un palíndromo.
- La concatenación preserva la cantidad de elementos.
- Revertir conserva la longitud de la cadena.
- Concatenar y luego dividir recupera la lista original.

Cada propiedad fue validada automáticamente con cientos de casos generados por Hypothesis.

---

## Mutation Testing

Se intentó ejecutar Mutation Testing con:

```bash
python -m mutmut run
```

Sin embargo, :contentReference[oaicite:0]{index=0} no ofrece soporte nativo para Windows y requiere el uso de :contentReference[oaicite:1]{index=1}.

Por esta razón, la validación de robustez se respaldó mediante:

- Cobertura de código del 100%.
- Cobertura de ramas del 100%.
- Cinco propiedades con Hypothesis.
- Casos límite y excepciones exhaustivamente evaluados.

---

## Resumen General

| Módulo | Tests | Cobertura |
|--------|-------|-----------|
| Ejercicio 1 | 14 | 100% |
| Ejercicio 2 | 16 | 100% |
| Ejercicio 3 | 5 | 100% |
| Ejercicio 4 | 5 | 100% |
| Bonificación | 9 | 100% |

---

## Tecnologías Utilizadas

- Python 3.12
- Pytest
- Pytest-Cov
- Hypothesis
- Pytest-Mock

---

## Autor

**Alejandro Peña**  
Estudiante de Ingeniería de Software  
Universitaria de Colombia

---

## Licencia

Proyecto académico desarrollado exclusivamente con fines educativos.