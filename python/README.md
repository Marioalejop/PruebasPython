````markdown
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
- Mutation Testing.
- Property-Based Testing con Hypothesis.
- Pruebas unitarias para un módulo adicional de bonificación académica.

Todos los módulos alcanzan una cobertura del 100%.

---

## Estructura del Proyecto

```text
python/
├── src/
│   ├── __init__.py
│   ├── ejercicio_1.py
│   ├── ejercicio_2.py
│   ├── ejercicio_3.py
│   ├── ejercicio_4.py
│   └── modulo_bonificacion.py
│
├── tests/
│   ├── test_ejercicio_1.py
│   ├── test_ejercicio_2.py
│   ├── test_ejercicio_3.py
│   ├── test_ejercicio_4.py
│   └── test_modulo_bonificacion.py
│
├── requirements.txt
├── pytest.ini
├── conftest.py
├── QUICK_START.py
└── README.md
````

---

## Requisitos

* Python 3.12 o superior
* pip

---

## Instalación

### 1. Clonar el repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
cd python
```

### 2. Crear entorno virtual (opcional)

```bash
python -m venv venv
```

### 3. Activar entorno virtual

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### 4. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## Dependencias Utilizadas

```txt
pytest
pytest-cov
hypothesis
pytest-mock
```

---

# Ejecución de Pruebas

## Ejecutar todos los tests

```bash
python -m pytest -v
```

## Ejecutar todos los tests con cobertura

```bash
python -m pytest --cov=src --cov-report=term-missing
```

## Generar reporte HTML

```bash
python -m pytest --cov=src --cov-report=html
```

Abrir posteriormente:

```bash
htmlcov/index.html
```

---

# Ejercicio 1 — Clases de Equivalencia y BVA

## Función

```python
calcular_descuento(edad, es_estudiante)
```

## Técnicas aplicadas

* Equivalence Partitioning
* Boundary Value Analysis

## Casos cubiertos

* Edad negativa
* Edad mayor a 120
* Menores de edad estudiantes
* Menores no estudiantes
* Adultos estudiantes
* Adultos no estudiantes
* Adultos mayores

## Resultados

* 14 pruebas ejecutadas
* Cobertura: 100%

### Ejecución

```bash
python -m pytest tests/test_ejercicio_1.py --cov=src.ejercicio_1 --cov-report=term-missing -v
```

---

# Ejercicio 2 — Branch Coverage

## Función

```python
validar_matricula(estudiante)
```

## Ramas evaluadas

* Datos vacíos
* Estudiante inactivo
* Deuda pendiente
* Créditos inválidos
* Matrícula habilitada
* Matrícula condicional

## Resultados

* 16 pruebas ejecutadas
* Branch Coverage: 100%

### Ejecución

```bash
python -m pytest tests/test_ejercicio_2.py --cov=src.ejercicio_2 --cov-report=term-missing -v
```

---

# Ejercicio 3 — Mutation Testing

## Función

```python
promedio_ponderado(notas, pesos)
```

## Mutantes eliminados

| Mutante | Operador   | Estado    |
| ------- | ---------- | --------- |
| M1      | ROR        | Eliminado |
| M2      | ROR        | Eliminado |
| M3      | ROR        | Eliminado |
| M4      | AOR        | Eliminado |
| M5      | AOR        | Eliminado |
| M6      | Validación | Eliminado |

## Resultados

* 5 pruebas ejecutadas
* Mutation Score: 100%

### Ejecución

```bash
python -m pytest tests/test_ejercicio_3.py --cov=src.ejercicio_3 --cov-report=term-missing -v
```

---

# Ejercicio 4 — Property-Based Testing

## Funciones

```python
revertir()
es_palindromo()
concatenar_lista()
```

## Propiedades verificadas

* Involutividad de la reversión.
* Todo texto concatenado con su reverso es palíndromo.
* Concatenar y dividir conserva la lista original.

## Herramienta

* Hypothesis

## Resultados

* 3 propiedades verificadas
* Más de 100 casos automáticos por propiedad

### Ejecución

```bash
python -m pytest tests/test_ejercicio_4.py --cov=src.ejercicio_4 --cov-report=term-missing -v
```

---

# Módulo Adicional — Bonificación Académica

## Función

```python
calcular_bonificacion(promedio, asistencia, semillero=False)
```

## Casos evaluados

* Promedio inválido inferior a 0
* Promedio inválido superior a 5
* Asistencia inválida
* Asistencia inferior al mínimo requerido
* Bonificación máxima
* Bonificación media
* Bonificación básica
* Bonificación con semillero
* Sin bonificación

## Ejecución

```bash
python -m pytest tests/test_modulo_bonificacion.py -v
```

## Cobertura

```bash
python -m pytest tests/test_modulo_bonificacion.py --cov=src.modulo_bonificacion --cov-report=term-missing
```

## Resultado obtenido

```text
9 passed in 0.20s
Coverage: 100%
```

---

# Resumen General

| Módulo       | Tests | Cobertura |
| ------------ | ----- | --------- |
| Ejercicio 1  | 14    | 100%      |
| Ejercicio 2  | 16    | 100%      |
| Ejercicio 3  | 5     | 100%      |
| Ejercicio 4  | 3     | 100%      |
| Bonificación | 9     | 100%      |

---

# Total del Proyecto

```text
47 pruebas ejecutadas
47 pruebas exitosas
0 pruebas fallidas
Cobertura global: 100%
```

---

# Tecnologías Utilizadas

* Python 3.12
* Pytest
* Pytest-Cov
* Hypothesis
* Pytest-Mock

---

# Comandos Útiles

## Ejecutar un archivo específico

```bash
python -m pytest tests/test_modulo_bonificacion.py -v
```

## Ejecutar una prueba específica

```bash
python -m pytest -k bonificacion_maxima -v
```

## Ver versión de Pytest

```bash
python -m pytest --version
```

---

# Autor

**Alejandro Peña**
Estudiante de Ingeniería de Software
Universitaria de Colombia

---

# Docente

**Mg. Sergio Alejandro Burbano Mena**

---

# Licencia

Proyecto académico desarrollado exclusivamente con fines educativos.

---

# Última Actualización

24 de abril de 2026

```
```
