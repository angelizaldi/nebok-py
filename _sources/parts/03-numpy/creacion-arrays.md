# Creación de arrays

En esta sección se enlistas funciones relacionadas con la creación de arrays.

:::{warning}
Para una lista completa visitar la [documentación](https://numpy.org/doc/stable/reference/routines.array-creation.html#array-creation-routines) de `numpy`.
:::

---
## Datos existentes

Funciones para crear arrays desde otros objetos. Para importar datos desde archivos consultar {doc}`lectura-escritura`. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [array](https://numpy.org/doc/stable/reference/generated/numpy.array.html)(object[, dtype, copy, order, subok, ...])
  - Crea un arreglo desde un objeto.
* - [copy](https://numpy.org/doc/stable/reference/generated/numpy.copy.html)(a[, order, subok])
  - Devuelve una copia del arreglo del objeto dado.
* - [fromfunction](https://numpy.org/doc/stable/reference/generated/numpy.fromfunction.html)(function, shape, *[, dtype, like])
  - Construye un arreglo ejecutando una función sobre cada coordenada.
* - [fromiter](https://numpy.org/doc/stable/reference/generated/numpy.fromiter.html)(iter, dtype[, count, like])
  - Crea un arreglo nuevo unidimensional a partir de un objeto iterable.
* - [fromstring](https://numpy.org/doc/stable/reference/generated/numpy.fromstring.html)(string[, dtype, count, like])
  - Crea un arreglo nuevo 1D inicializado a partir de datos de texto en una cadena.
```

<br>

---
## Forma o valor

Funciones para crear arrays indicando la forma (_shape_) del array y valores por default que deben de tener. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [empty](https://numpy.org/doc/stable/reference/generated/numpy.empty.html)(shape[, dtype, order, like])
  - Devuelve un arreglo nuevo de forma y tipo determinados, sin inicializar las entradas.
* - [empty_like](https://numpy.org/doc/stable/reference/generated/numpy.empty_like.html)(prototype[, dtype, order, subok, ...])
  - Devuelve un arreglo nuevo con la misma forma y tipo que un arreglo determinado.
* - [eye](https://numpy.org/doc/stable/reference/generated/numpy.eye.html)(N[, M, k, dtype, order, like])
  - Devuelve un arreglo 2D con unos en la diagonal y ceros en el resto de los elementos.
* - [full](https://numpy.org/doc/stable/reference/generated/numpy.full.html)(shape, fill_value[, dtype, order, like])
  - Devuelve un arreglo nuevo de forma y tipo dados, relleno con `fill_value`.
* - [full_like](https://numpy.org/doc/stable/reference/generated/numpy.full_like.html)(a, fill_value[, dtype, order, ...])
  - Devuelve un arreglo relleno con `fill_value` con la misma forma y tipo que un arreglo determinado.
* - [identity](https://numpy.org/doc/stable/reference/generated/numpy.identity.html)(n[, dtype, like])
  - Devuelve una matriz identidad.
* - [ones](https://numpy.org/doc/stable/reference/generated/numpy.ones.html)(shape[, dtype, order, like])
  - Devuelve un arreglo nuevo de forma y tipo dados, llena de unos.
* - [ones_like](https://numpy.org/doc/stable/reference/generated/numpy.ones_like.html)(a[, dtype, order, subok, shape])
  - Devuelve un arreglo de unos con la misma forma y tipo que un arreglo dado.
* - [zeros](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html)(shape[, dtype, order, like])
  - Devuelve un arreglo nuevo de forma y tipo dados, llena de ceros.
* - [zeros_like](https://numpy.org/doc/stable/reference/generated/numpy.zeros_like.html)(a[, dtype, order, subok, shape])
  - Devuelve un arreglo de ceros con la misma forma y tipo que un arreglo determinado.
```

<br>

---
## Matrices

Funciones para crear matrices (arreglos bidimensionales) o extraer partes de matrices existentes. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [diag](https://numpy.org/doc/stable/reference/generated/numpy.diag.html)(v[, k])
  - Extrae la diagonal de una matriz o construye una matriz diagonal.
* - [diagflat](https://numpy.org/doc/stable/reference/generated/numpy.diagflat.html)(v[, k])
  - Crea una matriz con la entrada aplanada como una diagonal de la matriz.
* - [tri](https://numpy.org/doc/stable/reference/generated/numpy.tri.html)(N[, M, k, dtype, like])
  - Un arreglo con unos en y debajo de la diagonal dada y ceros en cualquier otro lugar.
* - [tril](https://numpy.org/doc/stable/reference/generated/numpy.tril.html)(m[, k])
  - Extrae el triángular inferior de un arreglo.
* - [triu](https://numpy.org/doc/stable/reference/generated/numpy.triu.html)(m[, k])
  - Extrae el triángular superior de un arreglo.
```

<br>

---
## Rangos numéricos

Funciones para crear arreglos de rangos numéricos.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html)([start,] stop[, step,][, dtype, like])
  - Devuelve valores espaciados uniformemente dentro de un intervalo dado.
* - [geomspace](https://numpy.org/doc/stable/reference/generated/numpy.geomspace.html)(start, stop[, num, endpoint, ...])
  - Devuelve números espaciados uniformemente en una escala logarítmica (una progresión geométrica).
* - [linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html)(start, stop[, num, endpoint, ...])
  - Devuelve números espaciados uniformemente en un intervalo específico.
* - [logspace](https://numpy.org/doc/stable/reference/generated/numpy.logspace.html)(start, stop[, num, endpoint, base, ...])
  - Devuelve números espaciados uniformemente en una escala logarítmica.
* - [meshgrid](https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html)(*xi[, copy, sparse, indexing])
  - Devuelve las coordenadas individuales del producto cartesiano de vectores de coordenadas.
```

<br>