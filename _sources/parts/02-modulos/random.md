# Random

Es un módulo que provee de funciones para muestreos aleatorios y generación de números pseudo aleatorios de distintas distribuciones de probabilidad. Es necesario importar el módulo.
```python
# Importar todo el módulo
import random

# Importar una función específica
from random import function_name
```
- _function_name_ es el nombre de la función que se desea importar.

:::{warning}
Esta sección no cubre todas las funciones y clases disponibles del módulo `random`. Para más información de este módulo visitar la [documentación](https://docs.python.org/3/library/random.html#module-random) de Python.
:::

---
## Distribuciones

Funciones para generar números aleatorios de distribuciones de probabilidad específicas. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [betavariate](https://docs.python.org/3/library/random.html#random.betavariate)(alpha, beta)
  - Distribución beta. Con _alpha > 0_ y _beta > 0_. Los valores devueltos oscilan entre 0 y 1.
* - [expovariate](https://docs.python.org/3/library/random.html#random.expovariate)(lambd)
  - Distribución exponencial. _lambd_ debe ser igual a 1.0 entre la media deseada (_1/theta_), con _thetha != 0_.
* - [gammavariate](https://docs.python.org/3/library/random.html#random.gammavariate)(alpha, beta)
  - Distribución gamma. Con _alpha > 0_ y _beta > 0_.
* - [gauss](https://docs.python.org/3/library/random.html#random.gauss)(mu=0.0, sigma=1.0)
  - Distribución normal, _mu_ es la media, y _sigma_ es la desviación estándar, con _sigma > 0_. Es un poco más rápida que la función `normalvariate()`.
* - [lognormvariate](https://docs.python.org/3/library/random.html#random.lognormvariate)(mu, sigma)
  - Distribución lognormal. El logaritmo natural de este distribución es una distribución normal con media _mu_ y desviación estándar _sigma_. , con _sigma > 0_.
* - [normalvariate](https://docs.python.org/3/library/random.html#random.normalvariate)(mu=0.0, sigma=1.0)
  - Distribución normal. _mu_ es la media y _sigma_ es la desviación estándar.
* - [paretovariate](https://docs.python.org/3/library/random.html#random.paretovariate)(alpha)
  - Distribución de Pareto. _alpha_ es el parámetro de forma.
* - [triangular](https://docs.python.org/3/library/random.html#random.triangular)(low, high, mode)
  - Devuelve un número `float` aleatorio N tal que _low <= N <= high_ y con _mode_ especificado entre esos límites. El argumento de _mode_ por defecto es el punto medio.
* - [uniform](https://docs.python.org/3/library/random.html#random.uniform)(a, b)
  - Retorna un número `float` aleatorio _N_ tal que _a <= N <= b_ para _a <= b_ y _b <= N <= a_ para _b < a_.
* - [vonmisesvariate](https://docs.python.org/3/library/random.html#random.vonmisesvariate)(mu, kappa)
  - _mu_ es el ángulo medio, expresado en radianes entre 0 y _2\*pi_, y _kappa_ es el parámetro de concentración, que debe ser mayor o igual a cero. Si _kappa_ es igual a cero, esta distribución se reduce a un ángulo aleatorio uniforme en el rango de 0 a 2\*pi.
* - [weibullvariate](https://docs.python.org/3/library/random.html#random.weibullvariate)(alpha, beta)
  - Distribución Weibull. _alpha_ es el parámetro de escala y _beta_ es el parámetro de forma.
```

<br>

## Numeros-aleatorios

Funciones para generar números aleatorios. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [randint](https://docs.python.org/3/library/random.html#random.randint)(a, b)
  - Devuelve un entero aleatorio _N_ tal que _a <= N <= b_. Alias para `randrange(a, b+1)`.
* - [random](https://docs.python.org/3/library/random.html#random.random)()
  - Devuelve un número `float` aleatorio en el rango _[0.0, 1.0)_.
* - [randrange](https://docs.python.org/3/library/random.html#random.randrange)(start, stop[, step])
  - Devuelve un número aleatorio del rango `range(start, stop, step)`.
```

<br>

## Muestreo y _Shuffle_

Funciones para hacer muestreo aleatorio con reemplazado o sin reemplazo y para reordenar aleatoriamente secuencias. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [choice](https://docs.python.org/3/library/random.html#random.choice)(seq)
  - Devuelve un elemento aleatorio de la secuencia no vacía _seq_. Si _seq_ está vacía, genera `IndexError`.
* - [choices](https://docs.python.org/3/library/random.html#random.choices)(population, weights=None, *, cum_weights=None, k=1)
  - Devuelve una lista de tamaño _k_ de elementos aleatorios de _population_ (`sequence` o `iterable`) con reemplazo. Si _population_ está vacía, genera `IndexError`.
* - [sample](https://docs.python.org/3/library/random.html#random.sample)(population, k, *, counts=None)
  - Devuelve una lista de longitud _k_ de elementos únicos elegidos de _population_ (`sequence` o `iterable`). Se utiliza para muestreo aleatorio sin reemplazo.
* - [shuffle](https://docs.python.org/3/library/random.html#random.shuffle)(x)
  - Reordena los elementos de _x_ (`sequence` o `iterable`) de manera aleatoria _in-place_.
```

<br>

## Semillas

Función para establecer la semilla del generados de números aleatorios para reproducibilidad. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [seed](https://docs.python.org/3/library/random.html#random.seed)(a=None, version=2)
  - Inicializa el generador de números aleatorios.
```
