# Información

Funciones para obtener información sobre _arrays_ que retornan _arrays_ booleanos y funciones para trabajar con _arrays_ booleanos.

:::{warning}
Para una lista completa visitar la [documentación](https://numpy.org/doc/stable/reference/routines.logic.html#logic-functions) de `numpy`.
:::

---
## Contenido del array

Funciones que retornan información sobre el contenido del _array_. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [isfinite](https://numpy.org/doc/stable/reference/generated/numpy.isfinite.html)(x, /[, out, where, casting, order, ...])
  - Prueba la finitud de los elementos (no `inf` y no `NaN`).
* - [isinf](https://numpy.org/doc/stable/reference/generated/numpy.isinf.html)(x, /[, out, where, casting, order, ...])
  - Prueba por elementos para infinito positivo o negativo.
* - [isnan](https://numpy.org/doc/stable/reference/generated/numpy.isnan.html)(x, /[, out, where, casting, order, ...])
  - Prueba los elementos para `NaN` y devuelva el resultado como un arreglo booleano.
* - [isnat](https://numpy.org/doc/stable/reference/generated/numpy.isnat.html)(x, /[, out, where, casting, order, ...])
  - Prueba elementos para `NaT` (no un tiempo) y devuelva el resultado como un arreglo booleano.
* - [isneginf](https://numpy.org/doc/stable/reference/generated/numpy.isneginf.html)(x[, out])
  - Prueba los elementos para infinito negativo, devuelve el resultado como un arreglo booleano.
* - [isposinf](https://numpy.org/doc/stable/reference/generated/numpy.isposinf.html)(x[, out])
  - Prueba elementos para infinito positivo, devuelve el resultado como un arreglo booleano.
```

<br>

## Tipo de array

Funciones que retornan información sobre el tipo de _array_. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [iscomplex](https://numpy.org/doc/stable/reference/generated/numpy.iscomplex.html)(x)
  - Devuelve un arreglo `bool`, donde `True` si el elemento de entrada es complejo.
* - [iscomplexobj](https://numpy.org/doc/stable/reference/generated/numpy.iscomplexobj.html)(x)
  - Verifica si es un arreglo de números complejos.
* - [isfortran](https://numpy.org/doc/stable/reference/generated/numpy.isfortran.html)(a)
  - Comprueba si el arreglo es contiguo Fortran.
* - [isreal](https://numpy.org/doc/stable/reference/generated/numpy.isreal.html)(x)
  - Devuelve un arreglo `bool`, donde `True` si el elemento de entrada es real.
* - [isrealobj](https://numpy.org/doc/stable/reference/generated/numpy.isrealobj.html)(x)
  - Verifica si es un arreglo de números reales.
* - [isscalar](https://numpy.org/doc/stable/reference/generated/numpy.isscalar.html)(element)
  - Devuelve `True` si el tipo de elemento es un tipo escalar.
```

<br>