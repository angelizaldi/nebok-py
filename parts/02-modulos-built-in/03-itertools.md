# Itertools

Es un módulo que provee varias funciones para construir iterators. Es necesario importarlo. 

```python
# Importar todo el módulo
import itertools

# Importar una clase específica
from itertools import function_name
```
- _function_name_ es el nombre de la clase que se desea importar.

```{warning}
En esta sección solo se presentarán algunas funciones de este módulo. Para una lista completa visitar la [documentación](https://docs.python.org/3/library/itertools.html) de Python.
```

---
## Combinatorios

```{list-table} TITLE
:header-rows: 1

* - Funciones
  - Descripción
* - [combinations](#combinations)(`iterable, r`)
  - Retorna secuencias de todos las combinaciones posibles, sin reemplazo...
* - [permutations](#permutations)(`iterable, r`)
  - Retorna secuencias de todos las combinaciones posibles, donde el...
* - [product](#product)(`*iterables, repeat = 1`)
  - Retorna un producto cartesiano de los iterables de entrada. Equivale...
```

---
<a name='combinations'></a>
**combinations**:

`itertools.combinations()`: Retorna secuencias de todos las combinaciones posibles, sin reemplazo e ignorando el orden, de _r_ de elementos del iterable de entrada.
```python
itertools.combinations(iterable, r)
```

```{toggle}
**Parámetros:**
- **`iterable`** \- `iterable`: Secuencia de entrada.
- **`r`** \- `int`: Tamaño de secuencias de salida.

**Retorna:**
- `iterator`.
```

<br><br>

---
<a name='permutations'></a>
**permutations**:

`itertools.permutations()`: Retorna secuencias de todos las combinaciones posibles, donde el orden importa (permutaciones), sin reemplazo, de _r_ elementos consecutivos del `iterable` de entrada.
```python
itertools.permutations(iterable, r)
```

```{toggle}
**Parámetros:**
- **`iterable`** \- `iterable`: Objeto de entrada.
- **`k`** \- `int`: Tamaño de secuencias de salida.

**Retorna:**
- `iterator`.
```

<br><br>

---
<a name='product'></a>
**product**:

`itertools.product()`: Retorna un producto cartesiano de los iterables de entrada. Equivale a `for-loops` anidados, por ejemplo `product(A,B)` es lo mismo que `((x, y) for x in A for y in B)`.
```python
itertools.combinations(*iterables, repeat = 1)
```

```{toggle}
**Parámetros:**
- **`*iterables`** \- `iterable`: Objetos de entrada.
- **`repeat`** \- `int`: Se utiliza cuando solo se usa un solo `iterable` y es para indicar que retorne el producto cartesiano consigo mismo `repeat` cantidad de veces.


**Retorna:**
- `iterator`.
```
