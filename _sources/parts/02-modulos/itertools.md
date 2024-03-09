---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Itertools

Es un módulo que provee varias funciones para construir `iterators`. Es necesario importarlo. 

```python
# Importar todo el módulo
import itertools

# Importar una función específica
from itertools import function_name
```
- _function_name_ es el nombre de la función que se desea importar.


:::{attention}
En esta sección se presentan ejemplos de unas cuantas funciones seleccionadas. Si se tiene duda de qué hace una función o cómo utilizar una función usar el link que viene en el nombre de cada función para dirigirse a la documentación de Python donde vienen más ejemplos de uso.
:::

<br><br>

---
## Iterators combinatorios

A continuación se presenta una lista de funciones que retornan combinaciones, permutaciones o productos cartesianos de iterables.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [combinations](https://docs.python.org/3/library/itertools.html#itertools.combinations)(iterable, r)
  - Retorna secuencias de todos las combinaciones posibles, sin reemplazo e ignorando el orden, de _r_ de elementos de `iterable`.
* - [combinations_with_replacement](https://docs.python.org/3/library/itertools.html#itertools.combinations_with_replacement)(iterable, r)
  - Retorna combinaciones de longitud `r` de los elementos de `iterable` permitiendo que los elementos individuales se repitan más de una vez.
* - [permutations](https://docs.python.org/3/library/itertools.html#itertools.permutations)(iterable, r=None)
  - Retorna secuencias de todos las combinaciones posibles, donde el orden importa (permutaciones), sin reemplazo, de _r_ elementos consecutivos del `iterable` de entrada.
* - [product](https://docs.python.org/3/library/itertools.html#itertools.product)(*iterables, repeat=1)
  - Crea un `iterator` con el producto cartesiano de los iterables de entrada.
```

<br>

### Ejemplo de `combinations()`

A continuación se presenta un ejemplo de uso de `itertools.combinations()`. Tener en cuenta que la funcionalidad de esta función es similar a la de `itertools.permutations()` y `itertools.combinations_with_replacement()` pero con resultados diferentes.

En este ejemplo se define una cadena con 5 caracteres y se pretende conocer todas las combinaciones tomando 2 elementos.

```{code-cell} python3
# Importar función
from itertools import combinations

# Definir un iterable, en este caso una cadena
X = "abcde"

# Calcular combinaciones
result = combinations(X, 2)

# Visualizar el resultado
for element in result:
    print(element)
```
- El objeto retornado es un `iterator` de `tuple`.

<br>

---
### Ejemplo de `product()`

A continuación se presenta un ejemplo de uso de `itertools.product()`.

En este ejemplo se definen dos cadenas, cada una con 3 caracteres y se pretende conocer el producto cartesiano de ambas cadenas. El producto cartesiano son todas las posibles combinaciones entre los elementos de dos o más iterables donde el primer elemento del producto cartesiano solo pueden ser elementos del primer `iterable`, el segundo elemento solo pueden ser elementos del segundo `iterable`, etc.


Equivale a `for-loops` anidados, por ejemplo `[*product(A, B)]` equivale a `[(a, b) for a in A for b in B]`

```{code-cell} python3
# Importar función
from itertools import product

# Definir los iterables
X = "abc"
Y = "123"

# Calcular el producto cartesiano
result = product(X, Y)

# Visualizar el resultado
for element in result:
    print(element)
```
- El objeto retornado es un `iterator` de `tuple`.

<br><br>

---
## Iterator Infinitos

A continuación se presenta una lista de funciones que generan `iterators` infinitos.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [count](https://docs.python.org/3/library/itertools.html#itertools.count)(start=0, step=1)
  - Crea un `iterator` que retorna valores espaciados uniformemente que comiencen en `start`.
* - [cycle](https://docs.python.org/3/library/itertools.html#itertools.cycle)(iterable)
  - Crea un `iterator` que devuelve los elementos de `iterable` y guarda una copia de cada uno. Cuando se agota el `iterable`, devuelve la copia guardada de los elementos.
* - [repeat](https://docs.python.org/3/library/itertools.html#itertools.repeat)(object[, times])
  - Crea un `iterator` que devuelve `object` una y otra vez.
```

### Ejemplo de `count()`

A continuación se presenta un ejemplo de uso de `itertools.count()`.

En este ejemplo se define un `iterator` que comience en 2 y aumente en 2 en cada elemento.

```{code-cell} python3
# Importar función
from itertools import count

# Definir el iterator
result = count(2, 2)

# Visualizar primeros 3 resultados
print(f"Primer elemento: {next(result)}")
print(f"Segundo elemento: {next(result)}")
print(f"Tercer elemento: {next(result)}")
print("...")
```
- Tener en cuenta que el objeto retornado es un `iterator` infinito.

<br><br>

---
## Iterators finitos

A continuación se presenta una lista de funciones que retornan `iterators` finitos, cuya logitud está determinada por el `iterable` más corto pasado como argumento.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [accumulate](https://docs.python.org/3/library/itertools.html#itertools.accumulate)(iterable[, func, *, initial=None])
  - Crea un `iterator` que devuelve sumas acumuladas, o resultados acumulados de otras funciones binarias (especificadas a través del argumento `func`).
* - [chain](https://docs.python.org/3/library/itertools.html#itertools.chain)(*iterables)
  - Crea un `iterator` que devuelve los elementos desde el primer `iterable` hasta que sea agotado, luego continúa con el siguiente `iterable`, hasta que todos los iterables estén exhaustos. Se utiliza para tratar secuencias consecutivas como una sola secuencia.
* - [compress](https://docs.python.org/3/library/itertools.html#itertools.compress)(data, selectors)
  - Crea un `iterator` que filtra los elementos de `data` y devuelve solo aquellos que tienen un elemento correspondiente en `selectors` que se evalúe como `True`.
* - [dropwhile](https://docs.python.org/3/library/itertools.html#itertools.dropwhile)(predicate, iterable)
  - Crea un `iterator` que elimina elementos del `iterable` siempre que `predicate` sea `True`; después, devuelve todos los elementos.
* - [filterfalse](https://docs.python.org/3/library/itertools.html#itertools.filterfalse)(predicate, iterable)
  - Crea un `iterator` que filtra los elementos de `iterable` y devuelve solo aquellos para cuyo `predicate` es `False`.
* - [groupby](https://docs.python.org/3/library/itertools.html#itertools.groupby)(iterable, key=None)
  - Genera un `iterator` tomando una función y una `iterable` y agrupa elementos consecutivos en el `iterable`, dependiendo del valor retornado por `key`. La `key` por default es una función de identidad y devuelve el elemento sin cambios.
* - [islice](https://docs.python.org/3/library/itertools.html#itertools.islice)(iterable, start, stop[, step])
  - Crea un `iterator` que devuelve elementos específicos de `iterable`.
* - [pairwise](https://docs.python.org/3/library/itertools.html#itertools.pairwise)(iterable)
  - Devuelve pares superpuestos sucesivos tomados de `iterable`.
* - [starmap](https://docs.python.org/3/library/itertools.html#itertools.starmap)(function, iterable)
  - Crea un `iterator` que calcula `function` usando los argumentos obtenidos de `iterable`.
* - [takewhile](https://docs.python.org/3/library/itertools.html#itertools.takewhile)(predicate, iterable)
  - Crea un `iterator` que devuelve elementos de `iterable` siempre que `predicate` sea `True`.
* - [tee](https://docs.python.org/3/library/itertools.html#itertools.tee)(iterable, n=2)
  - Devuelve `n` `iterators` independientes de un solo `iterable`.
* - [zip_longest](https://docs.python.org/3/library/itertools.html#itertools.zip_longest)(*iterables, fillvalue=None)
  - Crea un `iterator` que combina elementos de cada uno de los iterables. Si los iterables tienen una longitud desigual, los valores faltantes se completan con `fillvalue`.
```

### Ejemplo de `groupby()`

A continuación se presenta un ejemplo de uso de `itertools.groupby()`.

En este ejemplo se define un iterable que contiene `tuples` cuyo primer elemento es una letra y el segundo elemento es un número, se pretende agrupar todos los tuples que tienen la misma letra.

```{code-cell} python3
# importar función
from itertools import groupby

# Definir un iterable
data = [('a', 1), ('a', 2), ('b', 3), ('b', 4), ('b', 5)]

# Calcular el groupby
result = groupby(data, lambda x: x[0])

# Ver el resultado
for key, group in result:
    print(f"Key: {key}, Grupo: {list(group)}")
```
- El objeto retornado es un `iterator` de `tuple`.