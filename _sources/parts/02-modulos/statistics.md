# Statistics

Es un módulo que provee de funciones estadísticas y además del objeto `NormalDist` para crear y manipular variables aleatorias con distribución normal. Es necesario importar el módulo.
```python
# Importar todo el módulo
import statistics

# Importar una función específica
from statistics import function_name
```
- _function_name_ es el nombre de la función que se desea importar.

:::{attention}
Para un tratado más completo de este módulo visitar la [documentación](https://docs.python.org/3/library/statistics.html) de Python.
:::


<br>

---
## Correlaciones

Funciones para cálculos de correlaciones y covarianzas. Estas funciones están disponibles en Python 3.10+.


```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [correlation](https://docs.python.org/3/library/statistics.html#statistics.correlation)(x, y, /)
  - Devuelve el coeficiente de correlación de Pearson para dos entradas. El coeficiente de correlación de Pearson r toma valores entre -1 y +1.
* - [covariance](https://docs.python.org/3/library/statistics.html#statistics.covariance)(x, y, /)
  - Devuelve la covarianza muestral de dos entradas _x_ e _y_.
```

<br>

## Cuantiles

Funciones para calcular cuantiles. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [quantiles](https://docs.python.org/3/library/statistics.html#statistics.quantiles)(data, *, n=4, method='exclusive')
  - Divide _data_ (`sequence` o `iterable`) en _n_ intervalos continuos con igual probabilidad. Devuelve una lista de _n - 1_ puntos de corte que separan los intervalos.
```

<br>

## Medidas de tendencia central

Funciones para cálculos de medidas de tendencia central, como medias, medianas, modas, etc. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [fmean](https://docs.python.org/3/library/statistics.html#statistics.fmean)(data, weights=None)
  - Convierte _data_ (`sequence` o `iterable`) en `float` y calcula la media aritmética.
* - [geometric_mean](https://docs.python.org/3/library/statistics.html#statistics.geometric_mean)(data)
  - Convierta _data_ (`sequence` o `iterable`) en `float` y calcula la media geométrica.
* - [harmonic_mean](https://docs.python.org/3/library/statistics.html#statistics.harmonic_mean)(data, weights=None)
  - Devuelve la media armónica de _data_ (`sequence` o `iterable`).
* - [mean](https://docs.python.org/3/library/statistics.html#statistics.mean)(data)
  - Devuelve la media aritmética de _data_ (`sequence` o `iterable`).
* - [median](https://docs.python.org/3/library/statistics.html#statistics.median)(data)
  - Devuelve la mediana de _data_ (`sequence` o `iterable`).
* - [median_grouped](https://docs.python.org/3/library/statistics.html#statistics.median_grouped)(data, interval=1)
  - Devuelve la mediana de _data_ (`sequence` o `iterable`) calculada como el percentil 50, mediante interpolación.
* - [median_high](https://docs.python.org/3/library/statistics.html#statistics.median_high)(data)
  - Devuelve la mediana alta de _data_ (`sequence` o `iterable`).
* - [median_low](https://docs.python.org/3/library/statistics.html#statistics.median_low)(data)
  - Devuelve la mediana baja de _data_ (`sequence` o `iterable`).
* - [mode](https://docs.python.org/3/library/statistics.html#statistics.mode)(data)
  - Devuelve la moda de _data_ (`sequence` o `iterable`).
* - [multimode](https://docs.python.org/3/library/statistics.html#statistics.multimode)(data)
  - Devuelve una lista de los valores que ocurren con más frecuencia en el orden en que se encontraron por primera vez en _data_ (`sequence` o `iterable`). 
```

<br>

## Medidas de dispersión

Medidas de dispersión como varianzas y desviaciones estándar. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [pstdev](https://docs.python.org/3/library/statistics.html#statistics.pstdev)(data, mu=None)
  - Devuelve la desviación estándar de la población.
* - [pvariance](https://docs.python.org/3/library/statistics.html#statistics.pvariance)(data, mu=None)
  - Devuelve la varianza de la población de _data_ (`sequence` o `iterable`).
* - [stdev](https://docs.python.org/3/library/statistics.html#statistics.stdev)(data, xbar=None)
  - Devuelve la desviación estándar de la muestra.
* - [variance](https://docs.python.org/3/library/statistics.html#statistics.variance)(data, xbar=None)
  - Devuelve la varianza muestral de _data_ (`sequence` o `iterable`) de al menos dos valores reales.
```

<br>

## Regresión

Función para regresiones lineales. Esta función está disponible en Python 3.10+.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [linear_regression](https://docs.python.org/3/library/statistics.html#statistics.linear_regression)(x, y, /, *, proportional=False)
  - Devuelve la pendiente y la intersección de la regresión lineal simple usando mínimos cuadrados ordinarios.
```

<br><br>

## Clase NormalDist

`NormalDist` es una clase para crear y manipular distribuciones normales.

```{list-table}
:header-rows: 1

* - Constructor
  - Descripción
* - [NormalDist](https://docs.python.org/3/library/statistics.html#statistics.NormalDist)(mu=0.0, sigma=1.0)
  - Devuelve un nuevo objeto `NormalDist` donde _mu_ representa la media y _sigma_ representa la desviación estándar.
```

Una vez creada una instancia de `NormalDist` se pueden usar sus métodos y atributos.

<br>

---
### Métodos de clase

A continuación se enlistan los métodos de clase de la clase `NormaDist`. 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [from_samples](https://docs.python.org/3/library/statistics.html#statistics.NormalDist.from_samples)(data)
  - Crea una instancia `NormalDist` con parámetros _mu_ y _sigma_ estimados a partir de _data_ (`sequence` o `iterable`) utilizando `fmean()` y `stdev()`.
```

<br>

### Atributos de instancia

A continuación se enlistan los atributos de instancia de las instancias de `NormalDist`. 

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - [mean](https://docs.python.org/3/library/statistics.html#statistics.NormalDist.mean)
  - Media aritmética de la distribución.
* - [median](https://docs.python.org/3/library/statistics.html#statistics.NormalDist.median)
  - Mediana de la distribución.
* - [mode](https://docs.python.org/3/library/statistics.html#statistics.NormalDist.mode)
  - Moda de la distribución.
* - [stdev](https://docs.python.org/3/library/statistics.html#statistics.NormalDist.stdev)
  - Desviación estándar de la distribución.
* - [variance](https://docs.python.org/3/library/statistics.html#statistics.NormalDist.variance)
  - Varianza de la distribución.
```

<br>

### Métodos de instancia

A continuación se enlistan los métodos de instancia de las instancias de `NormalDist`. 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [cdf](https://docs.python.org/3/library/statistics.html#statistics.NormalDist.cdf)(x)
  - Función de distribución acumulativa, calcula la probabilidad de que una variable aleatoria X sea menor que o igual a _x_.
* - [inv_cdf](https://docs.python.org/3/library/statistics.html#statistics.NormalDist.inv_cdf)(p)
  - Función de distribución acumulativa inversa, calcula `1-cdf(x)`.
* - [overlap](https://docs.python.org/3/library/statistics.html#statistics.NormalDist.overlap)(other)
  - Mide la concordancia entre dos distribuciones de probabilidad normales. Devuelve un valor entre 0.0 y 1.0.
* - [pdf](https://docs.python.org/3/library/statistics.html#statistics.NormalDist.pdf)(x)
  - Función de densidad de probabilidad, calcula la probabilidad relativa de que una variable aleatoria X esté cerca de la valor dado _x_.
* - [quantiles](https://docs.python.org/3/library/statistics.html#statistics.NormalDist.quantiles)(n=4)
  - Divide la distribución normal en _n_ intervalos continuos con igual probabilidad. Devuelve una lista de _n - 1_ puntos de corte que separan los intervalos.
* - [samples](https://docs.python.org/3/library/statistics.html#statistics.NormalDist.samples)(n, *, seed=None)
  - Genera _n_ muestras aleatorias de una distribución normal para una media y una desviación estándar dadas.
* - [zscore](https://docs.python.org/3/library/statistics.html#statistics.NormalDist.zscore)(x)
  - Calcula el valor _z_ de _x_ en términos del número de desviaciones estándar por encima o por debajo de la media de la distribución normal: `(x - µ) / σ`.
```

