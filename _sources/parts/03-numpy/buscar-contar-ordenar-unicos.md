# Buscar, contar, ordenar y valores únicos

Funciones para ordenar _arrays_, buscar valores, contar valores y encontrar los valores únicos.

:::{warning}
Para una lista completa visitar la [documentación](https://numpy.org/doc/stable/reference/routines.sort.html#sorting-searching-and-counting) de `numpy`.
:::

---
## Buscar

Funciones útiles para determinar índices o elementos que cumplen ciertas características como valores iguales a cero, máximos, mínimos o alguna otra característica específica. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [argmax](https://numpy.org/doc/stable/reference/generated/numpy.argmax.html)(a[, axis, out, keepdims])
  - Devuelve los índices de los valores máximos a lo largo de un eje.
* - [argmin](https://numpy.org/doc/stable/reference/generated/numpy.argmin.html)(a[, axis, out, keepdims])
  - Devuelve los índices de los valores mínimos a lo largo de un eje.
* - [argwhere](https://numpy.org/doc/stable/reference/generated/numpy.argwhere.html)(a)
  - Determina los índices de los elementos del arreglo que no son cero.
* - [extract](https://numpy.org/doc/stable/reference/generated/numpy.extract.html)(condition, arr)
  - Devuelve los elementos de un arreglo que cumplen alguna condición.
* - [flatnonzero](https://numpy.org/doc/stable/reference/generated/numpy.flatnonzero.html)(a)
  - Devuelve los índices que no son cero en la versión 1D de _a_.
* - [nanargmax](https://numpy.org/doc/stable/reference/generated/numpy.nanargmax.html)(a[, axis, out, keepdims])
  - Devuelve los índices de los valores máximos en el eje especificado ignorando `NaN`s.
* - [nanargmin](https://numpy.org/doc/stable/reference/generated/numpy.nanargmin.html)(a[, axis, out, keepdims])
  - Devuelve los índices de los valores mínimos en el eje especificado ignorando `NaN`s.
```

<br>

## Contar

Funciones para contar valores en _arrays_. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [count_nonzero](https://numpy.org/doc/stable/reference/generated/numpy.count_nonzero.html)(a[, axis, keepdims])
  - Cuenta el número de valores distintos de cero en la arreglo _a_.
```

<br>

## Ordenar

Funciones útiles para ordenar valores en _arrays_, determinar los índices de los valores ordenados, determinar índices para insertar valores y mantener el orden. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [argpartition](https://numpy.org/doc/stable/reference/generated/numpy.argpartition.html)(a, kth[, axis, kind, order])
  - Devuelve los índices en el que los valores de los primeros _k-1_ elementos, serán menores al valor del elemento _k_ y el resto serán mayores o iguales que el valor del elemento _k_. Cada partición no estrictamente estará ordenada. Lo mismo se puede aplicar para varias posiciones.
* - [argsort](https://numpy.org/doc/stable/reference/generated/numpy.argsort.html)(a[, axis, kind, order])
  - Devuelve los índices que ordenarían un arreglo.
* - [partition](https://numpy.org/doc/stable/reference/generated/numpy.partition.html)(a, kth[, axis, kind, order])
  - Devuelve una copia del arreglo en el que los valores de los primeros _k-1_ elementos, serán menores al valor del elemento _k_ y el resto serán mayores o iguales que el valor del elemento _k_. Cada partición no estrictamente estará ordenada. Lo mismo se puede aplicar para varias posiciones.
* - [searchsorted](https://numpy.org/doc/stable/reference/generated/numpy.searchsorted.html)(a, v[, side, sorter])
  - Determina los índices donde se deben insertar elementos para mantener el orden, bajo el supuesto de que _a_ está ordenado. En caso de múltiples valores, los índices se determinan solo con respecto al _array_ original _a_.
* - [sort](https://numpy.org/doc/stable/reference/generated/numpy.sort.html)(a[, axis, kind, order])
  - Devuelve una copia ordenada de un arreglo. Es posible ordenar algún eje en específico.
```

<br>

## Valores únicos

Funciones para encontrar los valores únicos en _arrays_. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [unique](https://numpy.org/doc/stable/reference/generated/numpy.unique.html)(ar[, return_index, return_inverse, ...])
  - Encuentra los elementos únicos de un arreglo.
```

<br>