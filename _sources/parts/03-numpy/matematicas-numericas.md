# Matemáticas y numéricas

En esta sección se enlistan las funciones para realizar cálculos matetmáticos y para trabajar con arrays numéricos.

:::{warning}
Para una lista completa visitar la [documentación](https://numpy.org/doc/stable/reference/routines.math.html#mathematical-functions) de `numpy`.
:::


---
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

---
## Derivadas e integrales

Funciones para calcular derivadas (gradientes) e integrales.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [gradient](https://numpy.org/doc/stable/reference/generated/numpy.gradient.html)(f, *varargs[, axis, edge_order])
  - Devuelve el gradiente de un arreglo N-dimensional.
* - [trapz](https://numpy.org/doc/stable/reference/generated/numpy.trapz.html)(y[, x, dx, axis])
  - Integra a lo largo del eje dado usando la regla trapezoidal compuesta.
```

<br>

---
## Enteros

Funciones para calcular el máximo común divisor y el mínimo común múltiplo de dos números enteros. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [gcd](https://numpy.org/doc/stable/reference/generated/numpy.gcd.html)(x1, x2, /[, out, where, casting, order, ...])
  - Devuelve el máximo común divisor de `|x1|` y `|x2|`.
* - [lcm](https://numpy.org/doc/stable/reference/generated/numpy.lcm.html)(x1, x2, /[, out, where, casting, order, ...])
  - Devuelve el mínimo común múltiplo de `|x1|` y `|x2|`.
```

<br>

---
## Exponentes y logaritmos

Funciones relacionadas con exponentes y logaritmos para cálculos vectorizados. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [exp](https://numpy.org/doc/stable/reference/generated/numpy.exp.html)(x, /[, out, where, casting, order, ...])
  - Calcula la exponencial (`e**x`) de todos los elementos en el arreglo de entrada.
* - [exp2](https://numpy.org/doc/stable/reference/generated/numpy.exp2.html)(x, /[, out, where, casting, order, ...])
  - Calcula `2**p` para todo `p` en el arreglo de entrada.
* - [expm1](https://numpy.org/doc/stable/reference/generated/numpy.expm1.html)(x, /[, out, where, casting, order, ...])
  - Calcula `exp(x) - 1` para todos los elementos del arreglo.
* - [log](https://numpy.org/doc/stable/reference/generated/numpy.log.html)(x, /[, out, where, casting, order, ...])
  - Logaritmo natural, por elementos.
* - [log10](https://numpy.org/doc/stable/reference/generated/numpy.log10.html)(x, /[, out, where, casting, order, ...])
  - Logaritmo base 10, por elementos.
* - [log1p](https://numpy.org/doc/stable/reference/generated/numpy.log1p.html)(x, /[, out, where, casting, order, ...])
  - Devuelve el `ln(1)+x` para el arreglo de entrada, por elementos.
* - [log2](https://numpy.org/doc/stable/reference/generated/numpy.log2.html)(x, /[, out, where, casting, order, ...])
  - Logaritmo base 2, por elementos.
* - [logaddexp](https://numpy.org/doc/stable/reference/generated/numpy.logaddexp.html)(x1, x2, /[, out, where, casting, ...])
  - Logaritmo de la suma de exponenciaciones de las entradas.
* - [logaddexp2](https://numpy.org/doc/stable/reference/generated/numpy.logaddexp2.html)(x1, x2, /[, out, where, casting, ...])
  - Logaritmo de la suma de exponenciaciones de las entradas en base-2.
```

<br>

---
## Hiperbólicas

Funciones relacionadas con funciones hiperbólicas para cálculos vectorizados. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [arccosh](https://numpy.org/doc/stable/reference/generated/numpy.arccosh.html)(x, /[, out, where, casting, order, ...])
  - Coseno hiperbólico inverso, por elementos.
* - [arcsinh](https://numpy.org/doc/stable/reference/generated/numpy.arcsinh.html)(x, /[, out, where, casting, order, ...])
  - Seno hiperbólico inverso, por elementos.
* - [arctanh](https://numpy.org/doc/stable/reference/generated/numpy.arctanh.html)(x, /[, out, where, casting, order, ...])
  - Tangente hiperbólica inversa, por elementos.
* - [cosh](https://numpy.org/doc/stable/reference/generated/numpy.cosh.html)(x, /[, out, where, casting, order, ...])
  - Coseno hiperbólico, por elementos.
* - [sinh](https://numpy.org/doc/stable/reference/generated/numpy.sinh.html)(x, /[, out, where, casting, order, ...])
  - Seno hiperbólico, por elementos.
* - [tanh](https://numpy.org/doc/stable/reference/generated/numpy.tanh.html)(x, /[, out, where, casting, order, ...])
  - Tangente hiperbólica, por elementos.
```

<br>

---
## Misceláneos

Funciones matemáticas generales como raíces cuadradas y cúbicas, valores absolutos, entre otras.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [absolute](https://numpy.org/doc/stable/reference/generated/numpy.absolute.html)(x, /[, out, where, casting, order, ...])
  - Calcula el valor absoluto, por elementos.
* - [cbrt](https://numpy.org/doc/stable/reference/generated/numpy.cbrt.html)(x, /[, out, where, casting, order, ...])
  - Devuelve la raíz cúbica de un arreglo, por elementos.
* - [clip](https://numpy.org/doc/stable/reference/generated/numpy.clip.html)(a, a_min, a_max[, out])
  - Limita los valores en un arreglo a `a_min` y `a_max`.
* - [convolve](https://numpy.org/doc/stable/reference/generated/numpy.convolve.html)(a, v[, mode])
  - Devuelve la convolución lineal discreta de dos secuencias unidimensionales.
* - [fabs](https://numpy.org/doc/stable/reference/generated/numpy.fabs.html)(x, /[, out, where, casting, order, ...])
  - Calcula los valores absolutos, por elementos.
* - [interp](https://numpy.org/doc/stable/reference/generated/numpy.interp.html)(x, xp, fp[, left, right, period])
  - Interpolación lineal unidimensional para puntos de muestra que aumentan monótonamente.
* - [nan_to_num](https://numpy.org/doc/stable/reference/generated/numpy.nan_to_num.html)(x[, copy, nan, posinf, neginf])
  - Reemplaza `NaN` con cero e `inf` con números finitos grandes (default) o con los números definidos por el usuario usando `nan`, `posinf` y/o `neginf`.
* - [sign](https://numpy.org/doc/stable/reference/generated/numpy.sign.html)(x, /[, out, where, casting, order, ...])
  - Devuelve una indicación por elementos del signo de un número.
* - [sqrt](https://numpy.org/doc/stable/reference/generated/numpy.sqrt.html)(x, /[, out, where, casting, order, ...])
  - Devuelve la raíz cuadrada no negativa de un arreglo, por elementos.
* - [square](https://numpy.org/doc/stable/reference/generated/numpy.square.html)(x, /[, out, where, casting, order, ...])
  - Devuelve el cuadrado de los elementos de la entrada.
```

<br>

---
## Números complejos

Funciones relacionadas con números complejos para cálculos vectorizados. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [angle](https://numpy.org/doc/stable/reference/generated/numpy.angle.html)(z[, deg])
  - Devuelve el ángulo del argumento complejo.
* - [conj](https://numpy.org/doc/stable/reference/generated/numpy.conj.html)(x, /[, out, where, casting, order, ...])
  - Devuelve el complejo conjugado, por elementos.
* - [conjugate](https://numpy.org/doc/stable/reference/generated/numpy.conjugate.html)(x, /[, out, where, casting, ...])
  - Devuelve el complejo conjugado, por elementos.
* - [imag](https://numpy.org/doc/stable/reference/generated/numpy.imag.html)(val)
  - Devuelve la parte imaginaria del argumento complejo.
* - [real](https://numpy.org/doc/stable/reference/generated/numpy.real.html)(val)
  - Devuelve la parte real del argumento complejo.
```

<br>

---
## Redondeo y truncamiento

Funciones relacionadas con redondear y truncar arrays numéricos.  

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [around](https://numpy.org/doc/stable/reference/generated/numpy.around.html)(a[, decimals, out])
  - Redondea uniformemente al número dado de decimales.
* - [ceil](https://numpy.org/doc/stable/reference/generated/numpy.ceil.html)(x, /[, out, where, casting, order, ...])
  - Devuelve el techo de la entrada, por elementos.
* - [fix](https://numpy.org/doc/stable/reference/generated/numpy.fix.html)(x[, out])
  - Redondea al entero más cercano hacia cero.
* - [floor](https://numpy.org/doc/stable/reference/generated/numpy.floor.html)(x, /[, out, where, casting, order, ...])
  - Devuelve el piso de la entrada, por elementos.
* - [rint](https://numpy.org/doc/stable/reference/generated/numpy.rint.html)(x, /[, out, where, casting, order, ...])
  - Redondea los elementos de la arreglo al entero más cercano.
* - [trunc](https://numpy.org/doc/stable/reference/generated/numpy.trunc.html)(x, /[, out, where, casting, order, ...])
  - Devuelve el valor truncado de la entrada, por elementos.
```

<br>

---
## Sumas, productos, diferencias y cálculos acumulados

Funciones para realizar sumas, productos y diferencias en arrays numéricos, así como cálculos acumulados.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [cross](https://numpy.org/doc/stable/reference/generated/numpy.cross.html)(a, b[, axisa, axisb, axisc, axis])
  - Devuelve el producto cruz de dos vectores.
* - [cumprod](https://numpy.org/doc/stable/reference/generated/numpy.cumprod.html)(a[, axis, dtype, out])
  - Devuelve el producto acumulativo de elementos a lo largo de un eje dado.
* - [cumsum](https://numpy.org/doc/stable/reference/generated/numpy.cumsum.html)(a[, axis, dtype, out])
  - Devuelve la suma acumulada de los elementos a lo largo de un eje dado.
* - [diff](https://numpy.org/doc/stable/reference/generated/numpy.diff.html)(a[, n, axis, prepend, append])
  - Calcula la n-ésima diferencia discreta a lo largo del eje dado.
* - [ediff1d](https://numpy.org/doc/stable/reference/generated/numpy.ediff1d.html)(ary[, to_end, to_begin])
  - Calcula las diferencias entre elementos consecutivos de un arreglo.
* - [nancumprod](https://numpy.org/doc/stable/reference/generated/numpy.nancumprod.html)(a[, axis, dtype, out])
  - Devuelve el producto acumulativo de los elementos de la arreglo sobre un eje determinado tratando `NaN` como uno.
* - [nancumsum](https://numpy.org/doc/stable/reference/generated/numpy.nancumsum.html)(a[, axis, dtype, out])
  - Devuelve la suma acumulativa de los elementos de la arreglo sobre un eje determinado tratando `NaN` como cero.
* - [nanprod](https://numpy.org/doc/stable/reference/generated/numpy.nanprod.html)(a[, axis, dtype, out, keepdims, ...])
  - Devuelve el producto de los elementos de la arreglo sobre un eje determinado tratando `NaN` como uno.
* - [nansum](https://numpy.org/doc/stable/reference/generated/numpy.nansum.html)(a[, axis, dtype, out, keepdims, ...])
  - Devuelve la suma de los elementos de la arreglo sobre un eje determinado tratando `NaN` como cero.
* - [prod](https://numpy.org/doc/stable/reference/generated/numpy.prod.html)(a[, axis, dtype, out, keepdims, ...])
  - Devuelve el producto de los elementos de la arreglo sobre un eje dado.
* - [sum](https://numpy.org/doc/stable/reference/generated/numpy.sum.html)(a[, axis, dtype, out, keepdims, ...])
  - Suma de elementos del arreglo sobre un eje dado.
```

<br>

---
## Trigonométricas

Funciones relacionadas con funciones trigonométricas para cálculos vectorizados. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [arccos](https://numpy.org/doc/stable/reference/generated/numpy.arccos.html)(x, /[, out, where, casting, order, ...])
  - Coseno inverso, por elementos.
* - [arcsin](https://numpy.org/doc/stable/reference/generated/numpy.arcsin.html)(x, /[, out, where, casting, order, ...])
  - Seno inverso, por elementos.
* - [arctan](https://numpy.org/doc/stable/reference/generated/numpy.arctan.html)(x, /[, out, where, casting, order, ...])
  - Tangente inversa, por elementos.
* - [arctan2](https://numpy.org/doc/stable/reference/generated/numpy.arctan2.html)(x1, x2, /[, out, where, casting, ...])
  - Tangente inversa por elementos de `x1/x2` eligiendo el cuadrante correctamente.
* - [cos](https://numpy.org/doc/stable/reference/generated/numpy.cos.html)(x, /[, out, where, casting, order, ...])
  - Coseno trigonométrico, por elementos.
* - [deg2rad](https://numpy.org/doc/stable/reference/generated/numpy.deg2rad.html)(x, /[, out, where, casting, order, ...])
  - Convierte ángulos de grados a radianes.
* - [degrees](https://numpy.org/doc/stable/reference/generated/numpy.degrees.html)(x, /[, out, where, casting, order, ...])
  - Convierte ángulos de radianes a grados.
* - [hypot](https://numpy.org/doc/stable/reference/generated/numpy.hypot.html)(x1, x2, /[, out, where, casting, ...])
  - Dados los "catetos" de un triángulo rectángulo, devuelva su hipotenusa.
* - [rad2deg](https://numpy.org/doc/stable/reference/generated/numpy.rad2deg.html)(x, /[, out, where, casting, order, ...])
  - Convierte ángulos de radianes a grados.
* - [radians](https://numpy.org/doc/stable/reference/generated/numpy.radians.html)(x, /[, out, where, casting, order, ...])
  - Convierte ángulos de grados a radianes.
* - [sin](https://numpy.org/doc/stable/reference/generated/numpy.sin.html)(x, /[, out, where, casting, order, ...])
  - Seno trigonométrico, por elementos.
* - [tan](https://numpy.org/doc/stable/reference/generated/numpy.tan.html)(x, /[, out, where, casting, order, ...])
  - Tangente trigonométrica, por elementos.
```

<br>

---
## Valores extremos

Lorem ipsum dolor sit amet, consectetur adipiscing elit. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [amax](https://numpy.org/doc/stable/reference/generated/numpy.amax.html)(a[, axis, out, keepdims, initial, where])
  - Devuelve el valor máximo de un arreglo o el valor máximo a lo largo de un eje.
* - [amin](https://numpy.org/doc/stable/reference/generated/numpy.amin.html)(a[, axis, out, keepdims, initial, where])
  - Devuelve el valor mínimo de un arreglo o el valor mínimo a lo largo de un eje.
* - [fmax](https://numpy.org/doc/stable/reference/generated/numpy.fmax.html)(x1, x2, /[, out, where, casting, ...])
  - Valor máximo del arreglo.
* - [fmin](https://numpy.org/doc/stable/reference/generated/numpy.fmin.html)(x1, x2, /[, out, where, casting, ...])
  - Valor mínimo del arreglo.
* - [maximum](https://numpy.org/doc/stable/reference/generated/numpy.maximum.html)(x1, x2, /[, out, where, casting, ...])
  - Valor máximo del arreglo.
* - [minimum](https://numpy.org/doc/stable/reference/generated/numpy.minimum.html)(x1, x2, /[, out, where, casting, ...])
  - Valor mínimo del arreglo.
* - [nanmax](https://numpy.org/doc/stable/reference/generated/numpy.nanmax.html)(a[, axis, out, keepdims, initial, where])
  - Devuelve el valor máximo de un arreglo o el valor máximo a lo largo de un eje, ignorando cualquier `NaN`.
* - [nanmin](https://numpy.org/doc/stable/reference/generated/numpy.nanmin.html)(a[, axis, out, keepdims, initial, where])
  - Devuelve el valor mínimo de un arreglo o el valor mínimo a lo largo de un eje, ignorando cualquier `NaN`.
```

<br>