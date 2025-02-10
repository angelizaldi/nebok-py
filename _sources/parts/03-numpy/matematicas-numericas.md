# Matemáticas y numéricas

En esta sección se enlistan las funciones para realizar cálculos matemáticos y para trabajar con _arrays_ numéricos/booleanos.

:::{warning}
Para una lista completa visitar la [documentación](https://numpy.org/doc/stable/reference/routines.math.html#mathematical-functions) de `numpy`.
:::

---
## Cálculos acumulados y diferencias

Funciones para cálculos acumulados y diferencias con desfases.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
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
```

<br>

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

## Enteros

Funciones para calcular el máximo común divisor y el mínimo común múltiplo de dos números enteros. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [gcd](https://numpy.org/doc/stable/reference/generated/numpy.gcd.html)(x1, x2, /[, out, where, casting, order, ...])
  - Devuelve el máximo común divisor de _|x1|_ y _|x2|_.
* - [lcm](https://numpy.org/doc/stable/reference/generated/numpy.lcm.html)(x1, x2, /[, out, where, casting, order, ...])
  - Devuelve el mínimo común múltiplo de _|x1|_ y _|x2|_.
```

<br>

## Exponentes y logaritmos

Funciones relacionadas con exponentes y logaritmos para cálculos vectorizados. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [exp](https://numpy.org/doc/stable/reference/generated/numpy.exp.html)(x, /[, out, where, casting, order, ...])
  - Calcula la exponencial (`e**x`) de todos los elementos en el arreglo de entrada.
* - [exp2](https://numpy.org/doc/stable/reference/generated/numpy.exp2.html)(x, /[, out, where, casting, order, ...])
  - Calcula `2**p` para todo _p_ en el arreglo de entrada.
* - [expm1](https://numpy.org/doc/stable/reference/generated/numpy.expm1.html)(x, /[, out, where, casting, order, ...])
  - Calcula `exp(x) - 1` para todos los elementos del arreglo. Útil cuando _x_ tiene valores muy pequeños.
* - [log](https://numpy.org/doc/stable/reference/generated/numpy.log.html)(x, /[, out, where, casting, order, ...])
  - Logaritmo natural, por elementos.
* - [log10](https://numpy.org/doc/stable/reference/generated/numpy.log10.html)(x, /[, out, where, casting, order, ...])
  - Logaritmo base 10, por elementos.
* - [log1p](https://numpy.org/doc/stable/reference/generated/numpy.log1p.html)(x, /[, out, where, casting, order, ...])
  - Devuelve el `ln(1+x)` para el arreglo de entrada, por elementos. Útil cuando _x_ tiene valores muy pequeños.
* - [log2](https://numpy.org/doc/stable/reference/generated/numpy.log2.html)(x, /[, out, where, casting, order, ...])
  - Logaritmo base 2, por elementos.
* - [logaddexp](https://numpy.org/doc/stable/reference/generated/numpy.logaddexp.html)(x1, x2, /[, out, where, casting, ...])
  - Logaritmo de la suma de exponenciaciones de las entradas.
* - [logaddexp2](https://numpy.org/doc/stable/reference/generated/numpy.logaddexp2.html)(x1, x2, /[, out, where, casting, ...])
  - Logaritmo de la suma de exponenciaciones de las entradas en base-2.
```

<br>

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

## Lógicas

Funciones útiles en _arrays_ booleanos. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [all](https://numpy.org/doc/stable/reference/generated/numpy.all.html)(a[, axis, out, keepdims, where])
  - Prueba si todos los elementos del arreglo a lo largo de un eje dado se evalúan como `True`.
* - [any](https://numpy.org/doc/stable/reference/generated/numpy.any.html)(a[, axis, out, keepdims, where])
  - Prueba si algún elemento del arreglo a lo largo de un eje dado se evalúa como `True`.
```

<br>

## Mínimos y máximos

Funciones relacionadas con valores mínimos y máximos de arreglos o entre arreglos.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [amax](https://numpy.org/doc/stable/reference/generated/numpy.amax.html)(a[, axis, out, keepdims, initial, where])
  - Devuelve el valor máximo de un arreglo o el valor máximo a lo largo de un eje. Es igual a la función `np.max()`.
* - [amin](https://numpy.org/doc/stable/reference/generated/numpy.amin.html)(a[, axis, out, keepdims, initial, where])
  - Devuelve el valor mínimo de un arreglo o el valor mínimo a lo largo de un eje. `np.min()`.
* - [fmax](https://numpy.org/doc/stable/reference/generated/numpy.fmax.html)(x1, x2, /[, out, where, casting, ...])
  - Valor máximo entre dos arreglos, por elementos, ignorando `NaN`s.
* - [fmin](https://numpy.org/doc/stable/reference/generated/numpy.fmin.html)(x1, x2, /[, out, where, casting, ...])
  - Valor mínimo entre dos arreglos, por elementos, ignorando `NaN`s.
* - [maximum](https://numpy.org/doc/stable/reference/generated/numpy.maximum.html)(x1, x2, /[, out, where, casting, ...])
  - Valor máximo entre dos arreglos, por elementos.
* - [minimum](https://numpy.org/doc/stable/reference/generated/numpy.minimum.html)(x1, x2, /[, out, where, casting, ...])
  - Valor mínimo entre dos arreglos, por elementos.
* - [nanmax](https://numpy.org/doc/stable/reference/generated/numpy.nanmax.html)(a[, axis, out, keepdims, initial, where])
  - Devuelve el valor máximo de un arreglo o el valor máximo a lo largo de un eje, ignorando cualquier `NaN`.
* - [nanmin](https://numpy.org/doc/stable/reference/generated/numpy.nanmin.html)(a[, axis, out, keepdims, initial, where])
  - Devuelve el valor mínimo de un arreglo o el valor mínimo a lo largo de un eje, ignorando cualquier `NaN`.
```

<br>

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
* - [convolve](https://numpy.org/doc/stable/reference/generated/numpy.convolve.html)(a, v[, mode])
  - Devuelve la convolución lineal discreta de dos secuencias unidimensionales.
* - [fabs](https://numpy.org/doc/stable/reference/generated/numpy.fabs.html)(x, /[, out, where, casting, order, ...])
  - Calcula los valores absolutos, por elementos. No soporta números complejos, usar `np.absolute()` en su lugar.
* - [interp](https://numpy.org/doc/stable/reference/generated/numpy.interp.html)(x, xp, fp[, left, right, period])
  - Interpolación lineal unidimensional para puntos de muestra que aumentan monótonamente.
* - [nan_to_num](https://numpy.org/doc/stable/reference/generated/numpy.nan_to_num.html)(x[, copy, nan, posinf, neginf])
  - Reemplaza `NaN` con cero e `inf` con números finitos grandes (default) o con los números definidos por el usuario usando _nan_, _posinf_ y/o _neginf_.
* - [sign](https://numpy.org/doc/stable/reference/generated/numpy.sign.html)(x, /[, out, where, casting, order, ...])
  - Devuelve una indicación por elementos del signo de un número.
* - [sqrt](https://numpy.org/doc/stable/reference/generated/numpy.sqrt.html)(x, /[, out, where, casting, order, ...])
  - Devuelve la raíz cuadrada no negativa de un arreglo, por elementos.
* - [square](https://numpy.org/doc/stable/reference/generated/numpy.square.html)(x, /[, out, where, casting, order, ...])
  - Devuelve el cuadrado de los elementos de la entrada.
```

<br>

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

<br/>

## Polinomios

Funciones para trabajar con polinomios.

### Ajustar

Funciones ajustar un polinomio a un conjunto de datos. 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [polyfit](https://numpy.org/doc/stable/reference/generated/numpy.polyfit.html)(x,  y,  deg[,  rcond,  full,  w,  cov])
  - Ajuste polinomial de mínimos cuadrados.
```

<br/>

### Aritméticas

Funciones para realizar operaciones algebraicas con polinomios. 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [polyadd](https://numpy.org/doc/stable/reference/generated/numpy.polyadd.html)(a1,  a2)
  - Encuentra la suma de dos polinomios.
* - [polydiv](https://numpy.org/doc/stable/reference/generated/numpy.polydiv.html)(u,  v)
  - Retorna el cociente y el resto de la división polinomial.
* - [polymul](https://numpy.org/doc/stable/reference/generated/numpy.polymul.html)(a1,  a2)
  - Encuentra el producto de dos polinomios.
* - [polysub](https://numpy.org/doc/stable/reference/generated/numpy.polysub.html)(a1,  a2)
  - Diferencia (resta) de dos polinomios.
```

<br/>

### Básicos

Funciones básicas para trabajar con polinomios como definir, evaluar, encontrar raices y determinar coeficientes.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [poly](https://numpy.org/doc/stable/reference/generated/numpy.poly.html)(seq_of_zeros)
  - Encuentra los coeficientes de un polinomio con la secuencia de raíces dada.
* - [poly1d](https://numpy.org/doc/stable/reference/generated/numpy.poly1d.html)(c_or_r[,  r,  variable])
  - Una clase polinomial unidimensional.
* - [polyval](https://numpy.org/doc/stable/reference/generated/numpy.polyval.html)(p,  x)
  - Evaluar un polinomio en valores específicos.
* - [roots](https://numpy.org/doc/stable/reference/generated/numpy.roots.html)(p)
  - Retorna las raíces de un polinomio con coeficientes dados en _p_.
```

<br/>

### Cálculo

Funciones para realizar derivadas e integrales indefinidas sobre polinomios. 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [polyder](https://numpy.org/doc/stable/reference/generated/numpy.polyder.html)(p[,  m])
  - Retorna la derivada del orden especificado de un polinomio.
* - [polyint](https://numpy.org/doc/stable/reference/generated/numpy.polyint.html)(p[,  m,  k])
  - Retorna una antiderivada (integral indefinida) de un polinomio.
```

<br/>

## Redondeo y truncamiento

Funciones relacionadas con redondear y truncar _arrays_ numéricos.  

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [around](https://numpy.org/doc/stable/reference/generated/numpy.around.html)(a[, decimals, out])
  - Redondea uniformemente al número dado de decimales.
* - [ceil](https://numpy.org/doc/stable/reference/generated/numpy.ceil.html)(x, /[, out, where, casting, order, ...])
  - Devuelve el techo de la entrada, por elementos.
* - [clip](https://numpy.org/doc/stable/reference/generated/numpy.clip.html)(a, a_min, a_max[, out])
  - Limita los valores en un arreglo a _a_min_ y _a_max_.
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

## Sumas y productos

Funciones para realizar sumas, productos y diferencias en _arrays_ numéricos, así como cálculos acumulados.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
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
