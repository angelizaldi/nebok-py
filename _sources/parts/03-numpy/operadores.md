# Operadores

Funciones equivalentes a operadores binarios.

:::{warning}
Para una lista completa visitar la [documentación](https://numpy.org/doc/stable/reference/routines.array-manipulation.html#array-manipulation-routines) de `numpy`.
:::

## Aritméticas

Funciones para hacer operaciones aritméticas vectorizadas. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [add](https://numpy.org/doc/stable/reference/generated/numpy.add.html)(x1, x2, /[, out, where, casting, order, ...])
  - Suma `x1` y `x2`, por elementos.
* - [divide](https://numpy.org/doc/stable/reference/generated/numpy.divide.html)(x1, x2, /[, out, where, casting, ...])
  - Divide `x1` y `x2`, por elementos.
* - [divmod](https://numpy.org/doc/stable/reference/generated/numpy.divmod.html)(x1, x2[, out1, out2], / [[, out, ...])
  - Devuelve el cociente y el residuo de la división de `x1` y `x2`, simultáneamente.
* - [float_power](https://numpy.org/doc/stable/reference/generated/numpy.float_power.html)(x1, x2, /[, out, where, ...])
  - Calcula `x1**x2`, por elementos.
* - [floor_divide](https://numpy.org/doc/stable/reference/generated/numpy.floor_divide.html)(x1, x2, /[, out, where, ...])
  - División entera de `x1` y `x2`, por elementos.
* - [fmod](https://numpy.org/doc/stable/reference/generated/numpy.fmod.html)(x1, x2, /[, out, where, casting, ...])
  - Módulo de `x1` y `x2`, por elementos.
* - [mod](https://numpy.org/doc/stable/reference/generated/numpy.mod.html)(x1, x2, /[, out, where, casting, order, ...])
  - Módulo de `x1` y `x2`, por elementos.
* - [modf](https://numpy.org/doc/stable/reference/generated/numpy.modf.html)(x[, out1, out2], / [[, out, where, ...])
  - Devuelve las partes fraccionaria y entera de un arreglo, por elementos.
* - [multiply](https://numpy.org/doc/stable/reference/generated/numpy.multiply.html)(x1, x2, /[, out, where, casting, ...])
  - Multiplica `x1` y `x2`, por elementos.
* - [negative](https://numpy.org/doc/stable/reference/generated/numpy.negative.html)(x, /[, out, where, casting, order, ...])
  - Negativo numérico, por elementos.
* - [positive](https://numpy.org/doc/stable/reference/generated/numpy.positive.html)(x, /[, out, where, casting, order, ...])
  - Positivo numérico, por elementos.
* - [power](https://numpy.org/doc/stable/reference/generated/numpy.power.html)(x1, x2, /[, out, where, casting, ...])
  - Calcula `x1**x2`, por elementos.
* - [reciprocal](https://numpy.org/doc/stable/reference/generated/numpy.reciprocal.html)(x, /[, out, where, casting, ...])
  - Devuelve el recíproco de `x`, por elementos.
* - [remainder](https://numpy.org/doc/stable/reference/generated/numpy.remainder.html)(x1, x2, /[, out, where, casting, ...])
  - Módulo de `x1` y `x2`, por elementos.
* - [subtract](https://numpy.org/doc/stable/reference/generated/numpy.subtract.html)(x1, x2, /[, out, where, casting, ...])
  - Resta `x1` y `x2`, por elementos.
* - [true_divide](https://numpy.org/doc/stable/reference/generated/numpy.true_divide.html)(x1, x2, /[, out, where, ...])
  - Divide `x1` y `x2`, por elementos.
```

<br>

## Bitwise

Operadores bitwise vectorizados. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [bitwise_and](https://numpy.org/doc/stable/reference/generated/numpy.bitwise_and.html)(x1, x2, /[, out, where, ...])
  - Calcula `&` bit a bit de dos arreglos.
* - [bitwise_or](https://numpy.org/doc/stable/reference/generated/numpy.bitwise_or.html)(x1, x2, /[, out, where, casting, ...])
  - Calcula `|` bit a bit de dos arreglos.
* - [bitwise_xor](https://numpy.org/doc/stable/reference/generated/numpy.bitwise_xor.html)(x1, x2, /[, out, where, ...])
  - Calcula `^` bit a bit de dos arreglos.
* - [invert](https://numpy.org/doc/stable/reference/generated/numpy.invert.html)(x, /[, out, where, casting, order, ...])
  - Calcula `~` bit a bit de un arreglo.
```

<br>

(comparacion)=
## Comparación

Funciones de comparación vectorizadas y otras funciones para comparar arrays. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [allclose](https://numpy.org/doc/stable/reference/generated/numpy.allclose.html)(a, b[, rtol, atol, equal_nan])
  - Devuelve `True` si dos arreglos son iguales en cuanto a elementos dentro de una tolerancia.
* - [array_equal](https://numpy.org/doc/stable/reference/generated/numpy.array_equal.html)(a1, a2[, equal_nan])
  - Devuelve `True` si dos arreglos tienen la misma forma y elementos, `False` en caso contrario.
* - [array_equiv](https://numpy.org/doc/stable/reference/generated/numpy.array_equiv.html)(a1, a2)
  - Devuelve `True` si los arreglos de entrada son consistentes en forma y todos los elementos son iguales.
* - [equal](https://numpy.org/doc/stable/reference/generated/numpy.equal.html)(x1, x2, /[, out, where, casting, ...])
  - Devuelve `(x1 == x2)` por elementos.
* - [greater](https://numpy.org/doc/stable/reference/generated/numpy.greater.html)(x1, x2, /[, out, where, casting, ...])
  - Devuelve `(x1 > x2)` por elementos.
* - [greater_equal](https://numpy.org/doc/stable/reference/generated/numpy.greater_equal.html)(x1, x2, /[, out, where, ...])
  - Devuelve `(x1 >= x2)` por elementos.
* - [isclose](https://numpy.org/doc/stable/reference/generated/numpy.isclose.html)(a, b[, rtol, atol, equal_nan])
  - Devuelve un arreglo booleano que indica si dos arreglos son iguales por elementos dentro de una tolerancia.
* - [less](https://numpy.org/doc/stable/reference/generated/numpy.less.html)(x1, x2, /[, out, where, casting, ...])
  - Devuelve `(x1 < x2)` por elementos.
* - [less_equal](https://numpy.org/doc/stable/reference/generated/numpy.less_equal.html)(x1, x2, /[, out, where, casting, ...])
  - Devuelve `(x1 <= x2)` por elementos.
* - [not_equal](https://numpy.org/doc/stable/reference/generated/numpy.not_equal.html)(x1, x2, /[, out, where, casting, ...])
  - Devuelve `(x1 != x2)` por elementos.
```

<br>

## Comparación (cadenas)

Funciones de comparación vectorizadas. Estas funciones, a diferencia de {ref}`comparacion` primero eliminan los espacios en blanco al inicio y al final de cada elemento antes de realizar la comparación.

:::{attention}
Estas funciones son del módulo `numpy.char`.
:::

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [char.equal](https://numpy.org/doc/stable/reference/generated/numpy.char.equal.html)(x1, x2)
  - Devuelve `(x1 == x2)` por elementos.
* - [char.greater](https://numpy.org/doc/stable/reference/generated/numpy.char.greater.html)(x1, x2)
  - Devuelve `(x1 > x2)` por elementos.
* - [char.greater_equal](https://numpy.org/doc/stable/reference/generated/numpy.char.greater_equal.html)(x1, x2)
  - Retorna `(x1 >= x2)` por elementos.
* - [char.less](https://numpy.org/doc/stable/reference/generated/numpy.char.less.html)(x1, x2)
  - Devuelve `(x1 < x2)` por elementos.
* - [char.less_equal](https://numpy.org/doc/stable/reference/generated/numpy.char.less_equal.html)(x1, x2)
  - Retorna `(x1 <= x2)` por elementos.
* - [char.not_equal](https://numpy.org/doc/stable/reference/generated/numpy.char.not_equal.html)(x1, x2)
  - Devuelve `(x1 != x2)` por elementos.
```

<br>

## Lógicas

Operadores lógicos vectorizados. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [logical_and](https://numpy.org/doc/stable/reference/generated/numpy.logical_and.html)(x1, x2, /[, out, where, ...])
  - Calcula el valor de verdad de `x1 and x2` por elementos.
* - [logical_not](https://numpy.org/doc/stable/reference/generated/numpy.logical_not.html)(x, /[, out, where, casting, ...])
  - Calcula el valor de verdad de `not x` por elementos.
* - [logical_or](https://numpy.org/doc/stable/reference/generated/numpy.logical_or.html)(x1, x2, /[, out, where, casting, ...])
  - Calcula el valor de verdad de `x1 or x2` por elementos.
* - [logical_xor](https://numpy.org/doc/stable/reference/generated/numpy.logical_xor.html)(x1, x2, /[, out, where, ...])
  - Calcula el valor de verdad de `x1 xor x2`, por elementos.
```

<br>

## Sets

Operadores para trabajar con arrays que representan _sets_ (arrays con valores únicos). 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [in1d](https://numpy.org/doc/stable/reference/generated/numpy.in1d.html)(ar1, ar2[, assume_unique, invert, kind])
  - Verifica si cada elemento de un arreglo 1D también está presente en un segundo arreglo. 
* - [intersect1d](https://numpy.org/doc/stable/reference/generated/numpy.intersect1d.html)(ar1, ar2[, assume_unique, ...])
  - Determina la intersección de dos arreglos.
* - [isin](https://numpy.org/doc/stable/reference/generated/numpy.isin.html)(element, test_elements[, ...])
  - Verifica si `element` se encuentra en `test_elements`.
* - [setdiff1d](https://numpy.org/doc/stable/reference/generated/numpy.setdiff1d.html)(ar1, ar2[, assume_unique])
  - Determina la diferencia de conjuntos de dos arreglos.
* - [setxor1d](https://numpy.org/doc/stable/reference/generated/numpy.setxor1d.html)(ar1, ar2[, assume_unique])
  - Determina la diferencia simétrica (`XOR`) de conjuntos de dos arreglos.
* - [union1d](https://numpy.org/doc/stable/reference/generated/numpy.union1d.html)(ar1, ar2)
  - Determina la unión de dos arreglos.
```

<br>