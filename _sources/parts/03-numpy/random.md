# Módulo random

`numpy.random` es un módulo que provee de funciones útiles para generar números aleatorios, muestras aleatorias de distribuciones de probabilidad, muestreo aleatorio, entre otras funcionalidades. Es posible importar solo el módulo o una función específica.

```python
# Importar el módulo
from numpy import random

# Importar una función específica
from numpy.random import function_name
```
- _function_name_ es el nombre de la función que se desea importar.
- Si se importa todo el módulo es necesario usar `random.function_name()` cada vez que se llame a una función el módulo.
- Si se usa `import numpy as np` y se desea usar una función del módulo `random`, entonces se debe usar `np.random.function_name()`.


:::{attention}
Para más información de este módulo visitar la [documentación](https://numpy.org/doc/stable/reference/random/index.html) de `numpy`.
:::

<br>

---
## Uso

Existen dos formas pricipales de usar este módulo, aunque solo una de ella es recomendada:

- **Random generator** (método recomendado): Se crea una {ref}`clase-generator` con la función `default_rng()` y se utilizan los métodos de esta clase para crear números y muestras aleatorias.
- **Legacy random generator**: Se crea una instancia de la clase `RandomState`. La mayoría de los métodos de esta clase están exportadas como funciones en el módulo `numpy.random`, por lo que no es necesario inicializar la instancia, basta con utilizar las {ref}`funciones` del módulo.


<br>

---
(clase-generator)=
## Clase Generator

La forma básica de usar _Random Generator_ (método recomendado) es:

```python
# Importar módulo
from numpy import random

# Crear instancia de la clase "Generator"
rng = random.default_rng()

# Utilizar los métodos de la clase
rng.method_name()
```
- _method_name_ es el nombre del método que se desea usar, los cuales se enlistan a continuación.

---
### Distribuciones

Métodos para la generación de muestras aleatorias de distribuciones de probabilidad. 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [beta](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.beta.html)(a, b[, size])
  - Genera muestras de una distribución Beta.
* - [binomial](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.binomial.html)(n, p[, size])
  - Genera muestras de una distribución binomial.
* - [chisquare](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.chisquare.html)(df[, size])
  - Genera muestras de una distribución de chi-cuadrada.
* - [dirichlet](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.dirichlet.html)(alpha[, size])
  - Genera muestras de la distribución de Dirichlet.
* - [exponential](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.exponential.html)([scale, size])
  - Genera muestras de una distribución exponencial.
* - [f](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.f.html)(dfnum, dfden[, size])
  - Genera muestras de una distribución F.
* - [gamma](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.gamma.html)(shape[, scale, size])
  - Genera muestras de una distribución Gamma.
* - [geometric](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.geometric.html)(p[, size])
  - Genera muestras de la distribución geométrica.
* - [gumbel](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.gumbel.html)([loc, scale, size])
  - Genera muestras de una distribución de Gumbel.
* - [hypergeometric](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.hypergeometric.html)(ngood, nbad, nsample[, size])
  - Genera muestras de una distribución hipergeométrica.
* - [laplace](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.laplace.html)([loc, scale, size])
  - Genera muestras de la distribución exponencial doble o de Laplace
* - [logistic](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.logistic.html)([loc, scale, size])
  - Genera muestras de una distribución logística.
* - [lognormal](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.lognormal.html)([mean, sigma, size])
  - Genera muestras de una distribución logarítmica normal.
* - [logseries](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.logseries.html)(p[, size])
  - Genera muestras de una distribución de serie logarítmica.
* - [multinomial](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.multinomial.html)(n, pvals[, size])
  - Genera muestras de una distribución multinomial.
* - [multivariate_hypergeometric](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.multivariate_hypergeometric.html)(colors, nsample)
  - Genera muestras de una distribución hipergeométrica multivariante.
* - [multivariate_normal](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.multivariate_normal.html)(mean, cov[, size, ...])
  - Genera muestras aleatorias de una distribución normal multivariada.
* - [negative_binomial](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.negative_binomial.html)(n, p[, size])
  - Genera muestras de una distribución binomial negativa.
* - [noncentral_chisquare](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.noncentral_chisquare.html)(df, nonc[, size])
  - Genera muestras de una distribución de chi-cuadrada no central.
* - [noncentral_f](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.noncentral_f.html)(dfnum, dfden, nonc[, size])
  - Genera muestras de la distribución F no central.
* - [normal](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.normal.html)([loc, scale, size])
  - Genera muestras aleatorias de una distribución normal (gaussiana).
* - [pareto](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.pareto.html)(a[, size])
  - Genera muestras de una distribución Pareto II o Lomax.
* - [poisson](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.poisson.html)([lam, size])
  - Genera muestras de una distribución de Poisson.
* - [power](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.power.html)(a[, size])
  - Genera muestras entre [0, 1] de una distribución de potencia con exponente positivo `a - 1`.
* - [rayleigh](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.rayleigh.html)([scale, size])
  - Genera muestras de una distribución de Rayleigh.
* - [standard_cauchy](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.standard_cauchy.html)([size])
  - Genera muestras de una distribución de Cauchy estándar con moda = 0.
* - [standard_exponential](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.standard_exponential.html)([size, dtype, method, out])
  - Genera muestras de la distribución exponencial estándar.
* - [standard_gamma](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.standard_gamma.html)(shape[, size, dtype, out])
  - Genera muestras de una distribución Gamma estándar.
* - [standard_normal](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.standard_normal.html)([size, dtype, out])
  - Genera muestras de una distribución normal estándar (media = 0, desviación estándar = 1).
* - [standard_t](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.standard_t.html)(df[, size])
  - Genera muestras de una distribución t de Student estándar con `df` grados de libertad.
* - [triangular](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.triangular.html)(left, mode, right[, size])
  - Genera muestras de la distribución triangular sobre el intervalo `[left, right]`.
* - [uniform](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.uniform.html)([low, high, size])
  - Genera muestras de una distribución uniforme.
* - [vonmises](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.vonmises.html)(mu, kappa[, size])
  - Genera muestras de una distribución de von Mises.
* - [wald](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.wald.html)(mean, scale[, size])
  - Genera muestras de una distribución de Wald o Gaussiana inversa.
* - [weibull](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.weibull.html)(a[, size])
  - Genera muestras de una distribución de Weibull.
* - [zipf](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.zipf.html)(a[, size])
  - Genera muestras de una distribución Zipf.
```

<br>

---
### Números aleatorios

Métodos para la generación básica de números aleatorios. 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [choice](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.choice.html)(a[, size, replace, p, axis, shuffle])
  - Genera una muestra aleatoria de un arreglo 1D.
* - [integers](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.integers.html)(low[, high, size, dtype, endpoint])
  - Retorna números enteros aleatorios de `low` (inclusivo) a `high` (exclusivo), o si `endpoint=True`, de `low` (inclusivo) a `high` (inclusivo).
* - [random](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.random.html)([size, dtype, out])
  - Devuelve flotantes aleatorios en el intervalo semiabierto [0.0, 1.0).
```

<br>

---
### Permutaciones

Métodos para permutaciones aleatorias. 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [permutation](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.permutation.html)(x[, axis])
  - Permuta aleatoriamente una secuencia o devuelve un rango permutado.
* - [permuted](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.permuted.html)(x[, axis, out])
  - Permuta aleatoriamente `x` a lo largo del eje `axis`.
* - [shuffle](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.shuffle.html)(x[, axis])
  - Modifica una secuencia _in-place_ ordenando su contenido aleatoriamente.
```

<br><br>

---
(funciones)=
## Funciones

:::{warning}
El uso de las funciones del módulo `numpy.random` está desaconsejado, ya que utilizan la clase `RandomState` para generar los números y muestras aletorias, en su lugar, es recomendado usar la {ref}`clase-generator` .
:::

Para utilizar las funciones del módulo `random` basta con importar el módulo o hacer referencia a él cuando se importe `numpy`

```python
# Importar módulo
from numpy import random

# Utilizar funciones del módulo
random.function_name()
```
- _function_name_ es el nombre de la función que se desea usar, las cuales se enlistan a continuación.


---
### Distribuciones

Funciones para la generación de muestras aleatorias de distribuciones de probabilidad. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [beta](https://numpy.org/doc/stable/reference/random/generated/numpy.random.beta.html)(a, b[, size])
  - Genera muestras de una distribución Beta.
* - [binomial](https://numpy.org/doc/stable/reference/random/generated/numpy.random.binomial.html)(n, p[, size])
  - Genera muestras de una distribución binomial.
* - [chisquare](https://numpy.org/doc/stable/reference/random/generated/numpy.random.chisquare.html)(df[, size])
  - Genera muestras de una distribución de chi-cuadrada.
* - [dirichlet](https://numpy.org/doc/stable/reference/random/generated/numpy.random.dirichlet.html)(alpha[, size])
  - Genera muestras de la distribución de Dirichlet.
* - [exponential](https://numpy.org/doc/stable/reference/random/generated/numpy.random.exponential.html)([scale, size])
  - Genera muestras de una distribución exponencial.
* - [f](https://numpy.org/doc/stable/reference/random/generated/numpy.random.f.html)(dfnum, dfden[, size])
  - Genera muestras de una distribución F.
* - [gamma](https://numpy.org/doc/stable/reference/random/generated/numpy.random.gamma.html)(shape[, scale, size])
  - Genera muestras de una distribución Gamma.
* - [geometric](https://numpy.org/doc/stable/reference/random/generated/numpy.random.geometric.html)(p[, size])
  - Genera muestras de la distribución geométrica.
* - [gumbel](https://numpy.org/doc/stable/reference/random/generated/numpy.random.gumbel.html)([loc, scale, size])
  - Genera muestras de una distribución de Gumbel.
* - [hypergeometric](https://numpy.org/doc/stable/reference/random/generated/numpy.random.hypergeometric.html)(ngood, nbad, nsample[, size])
  - Genera muestras de una distribución hipergeométrica.
* - [laplace](https://numpy.org/doc/stable/reference/random/generated/numpy.random.laplace.html)([loc, scale, size])
  - Genera muestras de la distribución exponencial doble o de Laplace
* - [logistic](https://numpy.org/doc/stable/reference/random/generated/numpy.random.logistic.html)([loc, scale, size])
  - Genera muestras de una distribución logística.
* - [lognormal](https://numpy.org/doc/stable/reference/random/generated/numpy.random.lognormal.html)([mean, sigma, size])
  - Genera muestras de una distribución logarítmica normal.
* - [logseries](https://numpy.org/doc/stable/reference/random/generated/numpy.random.logseries.html)(p[, size])
  - Genera muestras de una distribución de serie logarítmica.
* - [multinomial](https://numpy.org/doc/stable/reference/random/generated/numpy.random.multinomial.html)(n, pvals[, size])
  - Genera muestras de una distribución multinomial.
* - [multivariate_normal](https://numpy.org/doc/stable/reference/random/generated/numpy.random.multivariate_normal.html)(mean, cov[, size, ...])
  - Genera muestras aleatorias de una distribución normal multivariada.
* - [negative_binomial](https://numpy.org/doc/stable/reference/random/generated/numpy.random.negative_binomial.html)(n, p[, size])
  - Genera muestras de una distribución binomial negativa.
* - [noncentral_chisquare](https://numpy.org/doc/stable/reference/random/generated/numpy.random.noncentral_chisquare.html)(df, nonc[, size])
  - Genera muestras de una distribución de chi-cuadrada no central.
* - [noncentral_f](https://numpy.org/doc/stable/reference/random/generated/numpy.random.noncentral_f.html)(dfnum, dfden, nonc[, size])
  - Genera muestras de la distribución F no central.
* - [normal](https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html)([loc, scale, size])
  - Genera muestras aleatorias de una distribución normal (gaussiana).
* - [pareto](https://numpy.org/doc/stable/reference/random/generated/numpy.random.pareto.html)(a[, size])
  - Genera muestras de una distribución Pareto II o Lomax.
* - [poisson](https://numpy.org/doc/stable/reference/random/generated/numpy.random.poisson.html)([lam, size])
  - Genera muestras de una distribución de Poisson.
* - [power](https://numpy.org/doc/stable/reference/random/generated/numpy.random.power.html)(a[, size])
  - Genera muestras entre [0, 1] de una distribución de potencia con exponente positivo `a - 1`.
* - [rayleigh](https://numpy.org/doc/stable/reference/random/generated/numpy.random.rayleigh.html)([scale, size])
  - Genera muestras de una distribución de Rayleigh.
* - [standard_cauchy](https://numpy.org/doc/stable/reference/random/generated/numpy.random.standard_cauchy.html)([size])
  - Genera muestras de una distribución de Cauchy estándar con moda = 0.
* - [standard_exponential](https://numpy.org/doc/stable/reference/random/generated/numpy.random.standard_exponential.html)([size])
  - Genera muestras de la distribución exponencial estándar.
* - [standard_gamma](https://numpy.org/doc/stable/reference/random/generated/numpy.random.standard_gamma.html)(shape[, size])
  - Genera muestras de una distribución Gamma estándar.
* - [standard_normal](https://numpy.org/doc/stable/reference/random/generated/numpy.random.standard_normal.html)([size])
  - Genera muestras de una distribución normal estándar (media = 0, desviación estándar = 1).
* - [standard_t](https://numpy.org/doc/stable/reference/random/generated/numpy.random.standard_t.html)(df[, size])
  - Genera muestras de una distribución t de Student estándar con `df` grados de libertad.
* - [triangular](https://numpy.org/doc/stable/reference/random/generated/numpy.random.triangular.html)(left, mode, right[, size])
  - Genera muestras de la distribución triangular sobre el intervalo `[left, right]`.
* - [uniform](https://numpy.org/doc/stable/reference/random/generated/numpy.random.uniform.html)([low, high, size])
  - Genera muestras de una distribución uniforme.
* - [vonmises](https://numpy.org/doc/stable/reference/random/generated/numpy.random.vonmises.html)(mu, kappa[, size])
  - Genera muestras de una distribución de von Mises.
* - [wald](https://numpy.org/doc/stable/reference/random/generated/numpy.random.wald.html)(mean, scale[, size])
  - Genera muestras de una distribución de Wald o Gaussiana inversa.
* - [weibull](https://numpy.org/doc/stable/reference/random/generated/numpy.random.weibull.html)(a[, size])
  - Genera muestras de una distribución de Weibull.
* - [zipf](https://numpy.org/doc/stable/reference/random/generated/numpy.random.zipf.html)(a[, size])
  - Genera muestras de una distribución Zipf.
```

<br>

---
### Numeros aleatorios

Funciones para la generación básica de números aleatorios. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [bytes](https://numpy.org/doc/stable/reference/random/generated/numpy.random.bytes.html)(length)
  - Devuelve bytes aleatorios.
* - [rand](https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html)(d0, d1, ..., dn)
  - Retorna un arreglo con valores aleatorios en un _shape_ determinado.
* - [randint](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randint.html)(low[, high, size, dtype])
  - Devuelve números enteros aleatorios entre `low` y `high` (exclusivo).
* - [randn](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html)(d0, d1, ..., dn)
  - Devuelva una muestra (o muestras) de la distribución "normal estándar".
* - [random](https://numpy.org/doc/stable/reference/random/generated/numpy.random.random.html)([size])
  - Devuelve flotantes aleatorios en el intervalo semiabierto [0.0, 1.0).
* - [random_integers](https://numpy.org/doc/stable/reference/random/generated/numpy.random.random_integers.html)(low[, high, size])
  - Números enteros aleatorios de tipo `np.int_` entre `low` y `high`, inclusivos.
* - [random_sample](https://numpy.org/doc/stable/reference/random/generated/numpy.random.random_sample.html)([size])
  - Devuelve flotantes aleatorios en el intervalo semiabierto [0.0, 1.0).
```

<br>

---
### Permutaciones

Funciones para permutaciones aleatorias. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [choice](https://numpy.org/doc/stable/reference/random/generated/numpy.random.choice.html)(a[, size, replace, p])
  - Genera una muestra aleatoria de un arreglo 1D.
* - [permutation](https://numpy.org/doc/stable/reference/random/generated/numpy.random.permutation.html)(x)
  - Permuta aleatoriamente una secuencia o devuelve un rango permutado.
* - [shuffle](https://numpy.org/doc/stable/reference/random/generated/numpy.random.shuffle.html)(x)
  - Modifica una secuencia _in-place_ ordenando su contenido aleatoriamente.
```

<br>

---
### Semillas y estados

Funciones para establecer la semilla del generador o recuperar y establecer el estado del generador. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [get_state](https://numpy.org/doc/stable/reference/random/generated/numpy.random.get_state.html)([legacy])
  - Devuelve un `tuple` que representa el estado interno del generador.
* - [seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html)([seed])
  - Vuelva a inicializar la instancia de `RandomState`.
* - [set_state](https://numpy.org/doc/stable/reference/random/generated/numpy.random.set_state.html)(state)
  - Establece el estado interno del generador a partir de un `tuple`.
```

<br>