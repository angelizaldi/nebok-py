# Índices e iteración

Funciones para generar índices de un arreglo, acceder a elementos, insertar datos en un arreglo e iterar sobre arreglos.

:::{warning}
Para una lista completa visitar la [documentación](https://numpy.org/doc/stable/reference/arrays.indexing.html#indexing-routines) de `numpy`.
:::

---
## Generación de arreglos de índices

Funciones que generan arreglos de índices que cumplen determinadas condiciones. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [diag_indices](https://numpy.org/doc/stable/reference/generated/numpy.diag_indices.html)(n[, ndim])
  - Devuelve los índices para acceder a la diagonal principal de un arreglo.
* - [diag_indices_from](https://numpy.org/doc/stable/reference/generated/numpy.diag_indices_from.html)(arr)
  - Devuelve los índices para acceder a la diagonal principal de un arreglo n-dimensional.
* - [indices](https://numpy.org/doc/stable/reference/generated/numpy.indices.html)(dimensions[, dtype, sparse])
  - Devuelve un arreglo que representa los índices de una cuadrícula.
* - [mask_indices](https://numpy.org/doc/stable/reference/generated/numpy.mask_indices.html)(n, mask_func[, k])
  - Devuelve los índices para acceder a arreglos `(n, n)`, dada una función de enmascaramiento.
* - [nonzero](https://numpy.org/doc/stable/reference/generated/numpy.nonzero.html)(a)
  - Devuelve los índices de los elementos que no son cero.
* - [tril_indices](https://numpy.org/doc/stable/reference/generated/numpy.tril_indices.html)(n[, k, m])
  - Devuelve los índices del triángulo inferior de un arreglo `(n, m)`.
* - [tril_indices_from](https://numpy.org/doc/stable/reference/generated/numpy.tril_indices_from.html)(arr[, k])
  - Devuelve los índices para el triángulo inferior de `arr`.
* - [triu_indices](https://numpy.org/doc/stable/reference/generated/numpy.triu_indices.html)(n[, k, m])
  - Devuelve los índices del triángulo superior de un arreglo `(n, m)`.
* - [triu_indices_from](https://numpy.org/doc/stable/reference/generated/numpy.triu_indices_from.html)(arr[, k])
  - Devuelve los índices del triángulo superior de `arr`.
* - [where](https://numpy.org/doc/stable/reference/generated/numpy.where.html)(condition, [x, y], /)
  - Devuelve los elementos elegidos de `x` o `y` dependiendo de la condición.
```

<br>

## Insertar datos

Funciones para insertar datos en un arreglo. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [fill_diagonal](https://numpy.org/doc/stable/reference/generated/numpy.fill_diagonal.html)(a, val[, wrap])
  - Rellena la diagonal principal del arreglo dado.
* - [place](https://numpy.org/doc/stable/reference/generated/numpy.place.html)(arr, mask, vals)
  - Cambia los elementos de un arreglo en función de los valores condicionales y de entrada.
* - [put](https://numpy.org/doc/stable/reference/generated/numpy.put.html)(a, ind, v[, mode])
  - Reemplaza elementos especificados de un arreglo con valores dados.
* - [put_along_axis](https://numpy.org/doc/stable/reference/generated/numpy.put_along_axis.html)(arr, indices, values, axis)
  - Inserta valores en el arreglo de destino haciendo coincidir `indices` y _slices_ de datos.
* - [putmask](https://numpy.org/doc/stable/reference/generated/numpy.putmask.html)(a, mask, values)
  - Cambia los elementos de un arreglo en función de los valores condicionales y de entrada.
```

<br>

## Iteración

Funciones para iterar sobre arreglos. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [flatiter](https://numpy.org/doc/stable/reference/generated/numpy.flatiter.html)()
  - `iterator` plano para iterar sobre arreglos.
* - [iterable](https://numpy.org/doc/stable/reference/generated/numpy.iterable.html)(y)
  - Compruebe si un objeto se puede iterar o no.
* - [ndenumerate](https://numpy.org/doc/stable/reference/generated/numpy.ndenumerate.html)(arr)
  - `iterator` de índice multidimensional.
* - [ndindex](https://numpy.org/doc/stable/reference/generated/numpy.ndindex.html)(*shape)
  - Un objeto `iterator` n-dimensional para indexar arreglos.
* - [nditer](https://numpy.org/doc/stable/reference/generated/numpy.nditer.html)(op[, flags, op_flags, op_dtypes, ...])
  - Objeto `iterator` multidimensional eficiente para iterar sobre arreglos.
* - [nested_iters](https://numpy.org/doc/stable/reference/generated/numpy.nested_iters.html)(op, axes[, flags, op_flags, ...])
  - Crea `nditers` para usar en bucles anidados.
```

<br>

## Selección de elementos

Funciones que permiten seleccionar elementos de un arreglo. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [choose](https://numpy.org/doc/stable/reference/generated/numpy.choose.html)(a, choices[, out, mode])
  - Construye un arreglo a partir de arreglo de índices y una lista de arreglos para elegir.
* - [compress](https://numpy.org/doc/stable/reference/generated/numpy.compress.html)(condition, a[, axis, out])
  - Devuelve los _slices_ seleccionados de un arreglo a lo largo del eje dado.
* - [diagonal](https://numpy.org/doc/stable/reference/generated/numpy.diagonal.html)(a[, offset, axis1, axis2])
  - Devuelve las diagonales especificadas.
* - [select](https://numpy.org/doc/stable/reference/generated/numpy.select.html)(condlist, choicelist[, default])
  - Devuelve un arreglo extraído de los elementos de `choicelist`, según las condiciones.
* - [take](https://numpy.org/doc/stable/reference/generated/numpy.take.html)(a, indices[, axis, out, mode])
  - Toma elementos de un arreglo a lo largo de un eje.
* - [take_along_axis](https://numpy.org/doc/stable/reference/generated/numpy.take_along_axis.html)(arr, indices, axis)
  - Toma valores del arreglo de entrada al hacer coincidir `indices` y _slices_ de datos.
```

<br>