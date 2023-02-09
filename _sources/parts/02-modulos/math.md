# Math

Es un módulo que provee de funciones matemáticas. Es necesario importarlo.
```python
# Importar todo el módulo
import math

# Importar una clase específica
from math import function_name
```
- _function_name_ es el nombre de la función que se desea importar.

<br>

---
## Constantes

Constantes disponibles del módulo `math`. 

```{list-table}
:header-rows: 1

* - Constante
  - Descripción
* - [e](https://docs.python.org/3/library/math.html#math.e)
  - La constante matemática e = 2.718281….
* - [inf](https://docs.python.org/3/library/math.html#math.inf)
  - Un infinito positivo. (Para infinito negativo, utilice `-math.inf`).
* - [nan](https://docs.python.org/3/library/math.html#math.nan)
  - Retorna un `NaN` (Not a Number).
* - [pi](https://docs.python.org/3/library/math.html#math.pi)
  - La constante matemática π = 3.141592….
* - [tau](https://docs.python.org/3/library/math.html#math.tau)
  - La constante matemática τ = 6.283185….
```

<br>

---
## Conteo

Funciones relacionadas con técnicas de conteo.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [comb](https://docs.python.org/3/library/math.html#math.comb)(n, k)
  - Devuelve el número de formas de elegir `k` elementos de `n` elementos sin repetición y sin orden.
* - [factorial](https://docs.python.org/3/library/math.html#math.factorial)(n)
  - Devuelve `n` factorial como un número entero. Genera `ValueError` si `n` no es entero o es negativo.
* - [perm](https://docs.python.org/3/library/math.html#math.perm)(n, k=None)
  - Devuelve el número de formas de elegir `k` elementos de `n` elementos sin repetición y con orden.
```

<br>

---
## Conversion de ángulos

Funciones para conversiones entre ángulos (radianes a grados o viceversa).

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [degrees](https://docs.python.org/3/library/math.html#math.degrees)(x)
  - Convierta el ángulo `x` de radianes a grados.
* - [radians](https://docs.python.org/3/library/math.html#math.radians)(x)
  - Convierta el ángulo `x` de grados a radianes.
```

<br>

---
## Especiales

Funciones relacionadas con la función [gamma](https://es.wikipedia.org/wiki/Funci%C3%B3n_gamma) y la función [error](https://es.wikipedia.org/wiki/Funci%C3%B3n_error). 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [erf](https://docs.python.org/3/library/math.html#math.erf)(x)
  - Devuelve la función de error en `x`.
* - [erfc](https://docs.python.org/3/library/math.html#math.erfc)(x)
  - Devuelve la función de error complementaria en `x`.
* - [gamma](https://docs.python.org/3/library/math.html#math.gamma)(x)
  - Devuelve la función Gamma en `x`.
* - [lgamma](https://docs.python.org/3/library/math.html#math.lgamma)(x)
  - Devuelve el logaritmo natural del valor absoluto de la función Gamma en `x`.
```

<br>

---
## Hiperbólicas

Funciones relacionadas con las funciones hiperbólicas y sus inversas. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [acosh](https://docs.python.org/3/library/math.html#math.acosh)(x)
  - Devuelve el coseno hiperbólico inverso de `x`.
* - [asinh](https://docs.python.org/3/library/math.html#math.asinh)(x)
  - Devuelve el seno hiperbólico inverso de `x`.
* - [atanh](https://docs.python.org/3/library/math.html#math.atanh)(x)
  - Devuelve la tangente hiperbólica inversa de `x`.
* - [cosh](https://docs.python.org/3/library/math.html#math.cosh)(x)
  - Devuelve el coseno hiperbólico de `x`.
* - [sinh](https://docs.python.org/3/library/math.html#math.sinh)(x)
  - Devuelve el seno hiperbólico de `x`.
* - [tanh](https://docs.python.org/3/library/math.html#math.tanh)(x)
  - Devuelve la tangente hiperbólica de `x`.
```

<br>

---
## Información

Función que retornan información sobre objetos numéricos. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [isfinite](https://docs.python.org/3/library/math.html#math.isfinite)(x)
  - Retorna `True` si `x` no es ni infinito ni un `NaN`, y `False` en caso contrario.
* - [isinf](https://docs.python.org/3/library/math.html#math.isinf)(x)
  - Devuelve `True` si `x` es un infinito positivo o negativo, y `False` en caso contrario.
* - [isnan](https://docs.python.org/3/library/math.html#math.isnan)(x)
  - Devuelve `True` si `x` es un `NaN` (not a number) y `False` en caso contrario.
```

<br>

---
## Iterables numéricos

Funciones para hacer cálculos en objetos iterables numéricos. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [fsum](https://docs.python.org/3/library/math.html#math.fsum)(iterable)
  - Devuelve una suma de valores de coma flotante en `iterable`. Evita pérdida de precisión al rastrear múltiples sumas parciales intermedias.
* - [prod](https://docs.python.org/3/library/math.html#math.prod)(iterable, *, start=1)
  - Calcula el producto de todos los elementos de `iterable`.
```

<br>

---
## Logaritmos

Funciones para calcular logaritmos.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [log](https://docs.python.org/3/library/math.html#math.log)(x[, base])
  - Con un argumento, devuelva el logaritmo natural de `x` (base e). Se puede indicar otra base del logaritmo en el parámetro `base`.
* - [log10](https://docs.python.org/3/library/math.html#math.log10)(x)
  - Devuelve el logaritmo en base 10 de `x`. Suele ser más preciso que `log(x, 10)`.
* - [log1p](https://docs.python.org/3/library/math.html#math.log1p)(x)
  - Devuelve el logaritmo natural de `1+x`.
* - [log2](https://docs.python.org/3/library/math.html#math.log2)(x)
  - Devuelve el logaritmo base 2 de `x`. Esto suele ser más preciso que `log(x, 2)`.
```

<br>

---
## Misceláneo

Otras funciones de diversas categorías. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [copysign](https://docs.python.org/3/library/math.html#math.copysign)(x, y)
  - Devuelve un número con la magnitud (valor absoluto) de `x` pero el signo de `y`.
* - [cbrt](https://docs.python.org/3/library/math.html#math.cbrt)(x)
  - Devuelve la raíz cúbica de `x`.
* - [fabs](https://docs.python.org/3/library/math.html#math.fabs)(x)
  - Devuelve el valor absoluto de `x`.
* - [fmod](https://docs.python.org/3/library/math.html#math.fmod)(x, y)
  - Cálcula el módulo de `x` y `y`. Igual a `x - n*y` para algún entero `n` tal que el resultado tiene el mismo signo que `x` y magnitud menor que `abs(y)`. La expresión de Python `x % y` puede no devolver el mismo resultado.
* - [frexp](https://docs.python.org/3/library/math.html#math.frexp)(x)
  - Devuelve la mantisa y el exponente de `x` como el par `(m, e)`. `m` es un número flotante y `e` es un número entero tal que `x == m * 2**e`.
* - [isqrt](https://docs.python.org/3/library/math.html#math.isqrt)(n)
  - Devuelve la raíz cuadrada entera del entero no negativo `n`.
* - [ldexp](https://docs.python.org/3/library/math.html#math.ldexp)(x, i)
  - Devuelve `x * (2**i)`. Esta es esencialmente la inversa de la función `frexp()`.
* - [modf](https://docs.python.org/3/library/math.html#math.modf)(x)
  - Devuelve las partes fraccionaria y entera de `x`. Ambos resultados llevan el signo de `x` y son `float`.
* - [remainder](https://docs.python.org/3/library/math.html#math.remainder)(x, y)
  - Devuelve el resto de `x` al estilo IEEE 754 con respecto a `y`.
* - [sqrt](https://docs.python.org/3/library/math.html#math.sqrt)(x)
  - Devuelve la raíz cuadrada de `x`.
```

<br>

---
## Números enteros

Funciónes para calcular GCD y LCM (máximo común dividor y mínimo cómun múltiplo respectivamente).

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [gcd](https://docs.python.org/3/library/math.html#math.gcd)(*integers)
  - Devuelve el máximo común divisor de los argumentos enteros especificados. El valor devuelto es el mayor entero positivo que es un divisor de todos los argumentos.
* - [lcm](https://docs.python.org/3/library/math.html#math.lcm)(*integers)
  - Devuelve el mínimo común múltiplo de los argumentos enteros especificados. El valor devuelto es el menor entero positivo que es múltiplo de todos los argumentos.
```

<br>

---
## Otras

Otras funciones. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [isclose](https://docs.python.org/3/library/math.html#math.isclose)(a, b, *, rel_tol=1e-09, abs_tol=0.0)
  - Retorna `True` si los valores `a` y `b` están cerca uno del otro y `False` en caso contrario.
* - [nextafter](https://docs.python.org/3/library/math.html#math.nextafter)(x, y)
  - Devuelve el siguiente valor de punto flotante después de `x` hacia `y`.
* - [ulp](https://docs.python.org/3/library/math.html#math.ulp)(x)
  - Devuelve el valor del bit menos significativo del `float` `x`.
```

<br>

---
## Potencias

Funciones para cálculos de potencias. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [exp](https://docs.python.org/3/library/math.html#math.exp)(x)
  - Devuelve e elevado a la potencia `x`, donde e = 2.718281… es la base de logaritmos naturales.
* - [exp2](https://docs.python.org/3/library/math.html#math.exp2)(x)
  - Devuelve 2 elevado a `x`.
* - [expm1](https://docs.python.org/3/library/math.html#math.expm1)(x)
  - Retorna e elevado a `x` menos 1 (`exp(x) - 1`).
* - [pow](https://docs.python.org/3/library/math.html#math.pow)(x, y)
  - Devuelve `x` elevado a la potencia `y`.
```

<br>

---
## Redondeo

Funciones para redondear números. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [ceil](https://docs.python.org/3/library/math.html#math.ceil)(x)
  - Devuelve el techo de `x`, el entero más pequeño mayor o igual que `x`.
* - [floor](https://docs.python.org/3/library/math.html#math.floor)(x)
  - Devuelve el piso de `x`, el entero más grande menor o igual que `x`.
* - [trunc](https://docs.python.org/3/library/math.html#math.trunc)(x)
  - Devuelve `x` con la parte fraccionaria eliminada, dejando la parte entera.
```

<br>

---
## Trigonométricas

Funciones relacionadas con las funciones trigonométricas y sus inversas. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [acos](https://docs.python.org/3/library/math.html#math.acos)(x)
  - Devuelve el coseno inverso de `x`, en radianes. El resultado está entre 0 y Pi.
* - [asin](https://docs.python.org/3/library/math.html#math.asin)(x)
  - Devuelve el seno inverso de `x`, en radianes. El resultado está entre -pi/2 y pi/2.
* - [atan](https://docs.python.org/3/library/math.html#math.atan)(x)
  - Devuelve el la tangente inversa de `x`, en radianes. El resultado está entre -pi/2 y pi/2.
* - [atan2](https://docs.python.org/3/library/math.html#math.atan2)(y, x)
  - Devuelve `atan(y/x)`, en radianes. El resultado está entre -pi y pi.
* - [cos](https://docs.python.org/3/library/math.html#math.cos)(x)
  - Devuelve el coseno de `x` radianes.
* - [dist](https://docs.python.org/3/library/math.html#math.dist)(p, q)
  - Devuelve la distancia euclidiana entre dos puntos `p` y `q`, cada uno dado como una secuencia (o iterable) de coordenadas. los dos puntos debe tener la misma dimensión.
* - [hypot](https://docs.python.org/3/library/math.html#math.hypot)(*coordinates)
  - Devuelve la norma euclidiana, `sqrt(sum(x**2 for x in coordenadas))`. Esta es la longitud del vector desde el origen hasta el punto dado por las coordenadas.
* - [sin](https://docs.python.org/3/library/math.html#math.sin)(x)
  - Devuelve el seno de `x` radianes.
* - [tan](https://docs.python.org/3/library/math.html#math.tan)(x)
  - Devuelve la tangente de `x` radianes.
```