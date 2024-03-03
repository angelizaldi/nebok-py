# Buscar, contar, ordenar y valores únicos

Funciones para ordenar arrays, buscar valores, contar valores y encontrar los valores únicos.

:::{warning}
Para una lista completa visitar la [documentación](https://numpy.org/doc/stable/reference/routines.sort.html#sorting-searching-and-counting) de `numpy`.
:::

---
## Buscar

Funciones para buscar valores en arrays. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [argmax](https://numpy.org/doc/stable/reference/generated/numpy.argmax.html)(a[, axis, out, keepdims])
  - Devuelve los índices de los valores máximos a lo largo de un eje.
* - [argmin](https://numpy.org/doc/stable/reference/generated/numpy.argmin.html)(a[, axis, out, keepdims])
  - Devuelve los índices de los valores mínimos a lo largo de un eje.
* - [argwhere](https://numpy.org/doc/stable/reference/generated/numpy.argwhere.html)(a)
  - Determina los índices de los elementos del arreglo que no sean cero, agrupados por elemento.
* - [extract](https://numpy.org/doc/stable/reference/generated/numpy.extract.html)(condition, arr)
  - Devuelve los elementos de un arreglo que cumplen alguna condición.
* - [flatnonzero](https://numpy.org/doc/stable/reference/generated/numpy.flatnonzero.html)(a)
  - Devuelve los índices que no son cero en la versión 1D de `a`.
* - [nanargmax](https://numpy.org/doc/stable/reference/generated/numpy.nanargmax.html)(a[, axis, out, keepdims])
  - Devuelve los índices de los valores máximos en el eje especificado ignorando `NaN`s.
* - [nanargmin](https://numpy.org/doc/stable/reference/generated/numpy.nanargmin.html)(a[, axis, out, keepdims])
  - Devuelve los índices de los valores mínimos en el eje especificado ignorando `NaN`s.
* - [searchsorted](https://numpy.org/doc/stable/reference/generated/numpy.searchsorted.html)(a, v[, side, sorter])
  - Determina los índices donde se deben insertar elementos para mantener el orden.
```

<br>

---
## Contar

Funciones para contar valores en arrays. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [count_nonzero](https://numpy.org/doc/stable/reference/generated/numpy.count_nonzero.html)(a[, axis, keepdims])
  - Cuenta el número de valores distintos de cero en la arreglo `a`.
```

<br>

---
(numpy-funciones-ordenar)=
## Ordenar

Funciones para ordenar valores en arrays. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [argpartition](https://numpy.org/doc/stable/reference/generated/numpy.argpartition.html)(a, kth[, axis, kind, order])
  - Realiza una partición indirecta a lo largo del eje dado utilizando el algoritmo especificado por la palabra clave `kind`.
* - [argsort](https://numpy.org/doc/stable/reference/generated/numpy.argsort.html)(a[, axis, kind, order])
  - Devuelve los índices que ordenarían un arreglo.
* - [partition](https://numpy.org/doc/stable/reference/generated/numpy.partition.html)(a, kth[, axis, kind, order])
  - Devuelve una copia particionada de un arreglo.
* - [sort](https://numpy.org/doc/stable/reference/generated/numpy.sort.html)(a[, axis, kind, order])
  - Devuelve una copia ordenada de un arreglo.
```

<br>

---
(numpy-funciones-unicos)=
## Valores únicos

Funciones para encontrar los valores únicos en arrays. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [unique](https://numpy.org/doc/stable/reference/generated/numpy.unique.html)(ar[, return_index, return_inverse, ...])
  - Encuentra los elementos únicos de un arreglo.
```

<br>