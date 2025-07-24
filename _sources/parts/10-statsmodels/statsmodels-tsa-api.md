# API de Series de Tiempo

Especializada en modelos y análisis de series temporales. Entre las funcionalidades principales están:
- Modelos _ARIMA_ y SARIMAX.
- Descomposición de series temporales (tendencia, estacionalidad, residuos).
- Pruebas de estacionariedad (ADF, KPSS).
- Modelos de volatilidad (GARCH, ARCH).

Es necesario importar el módulo:

```python
# Importar api
import statsmodels.tsa.api as sm

# Importar clase específica
from statsmodels.tsa.api import ClassName

# Importar función específica
from statsmodels.tsa.api import func_name
```
- _sm_ es el nombre por convención.
- _ClassName_ o _func_name_ es el nombre de la clase o función respectivamente.

:::{note}
Para más información visitar la [documentación](https://www.statsmodels.org/stable/api.html#statsmodels-tsa-api) de _statsmodels_.
:::

A continuación se presenta un resumen de cada una de las secciones:
- **Suavizado Exponencial**: Técnicas para suavizar series temporales, como el modelo de Holt-Winters, útiles para pronósticos a corto plazo.
- **Filtros y Descomposiciones**: Métodos para descomponer series temporales en tendencia, estacionalidad y residuos, como el filtro Hodrick-Prescott.
- **Pronósticos (Forecasting)**: Herramientas para predecir valores futuros en series temporales.
- **Modelos de Cambio de Régimen de Markov**: Modelos que capturan cambios en el comportamiento de una serie temporal a lo largo del tiempo, como cambios en la media o varianza.
- **Modelos de Series Temporales Multivariadas**: Técnicas para analizar múltiples series temporales relacionadas, como modelos VAR (Vector Autoregression).
- **Estadísticas y Pruebas (Statistics and Tests)**: Pruebas para evaluar propiedades de series temporales, como estacionariedad (ADF, KPSS) o autocorrelación.
- **Herramientas de Series Temporales (Time-Series Tools)**: Funciones auxiliares para manipulación y análisis de series temporales.
- **Análisis de Series Temporales Univariadas (Univariate Time-Series Analysis)**: Métodos para modelar y analizar series temporales individuales, como _AR_, _MA_ y _ARIMA_.
- **Interfaz X12/X13 (X12/X13 Interface)**: Integración con el software _X-12-ARIMA_ y _X-13ARIMA-SEATS_ para descomposición avanzada de series temporales.

<br/>

## Suavizado Exponencial

Técnicas para suavizar series temporales, como el modelo de Holt-Winters, útiles para pronósticos a corto plazo.

:::{note}
Notar que todas son clases.
:::

```{list-table}
:header-rows: 1

* - Constructor
  - Descripción
* - [ETSModel](https://www.statsmodels.org/stable/generated/statsmodels.tsa.exponential_smoothing.ets.ETSModel.html)(endog, ...)
  - Modelos ETS.
* - [ExponentialSmoothing](https://www.statsmodels.org/stable/generated/statsmodels.tsa.statespace.exponential_smoothing.ExponentialSmoothing.html)(endog, ...)
  - Modelos de suavizado exponencial lineal.
* - [ExponentialSmoothing](https://www.statsmodels.org/stable/generated/statsmodels.tsa.holtwinters.ExponentialSmoothing.html)(endog, ...)
  - Alisado exponencial de _Holt Winter_.
* - [Holt](https://www.statsmodels.org/stable/generated/statsmodels.tsa.holtwinters.Holt.html)(endog, ...)
  - El suavizado exponencial de _Holt_.
* - [SimpleExpSmoothing](https://www.statsmodels.org/stable/generated/statsmodels.tsa.holtwinters.SimpleExpSmoothing.html)(endog, ...)
  - Suavizado exponencial simple.
```

<br/>

## Filtros y Descomposiciones

Métodos para descomponer series temporales en tendencia, estacionalidad y residuos, como el filtro _Hodrick-Prescott_.

```{list-table}
:header-rows: 1

* - Constructor/Función
  - Descripción
* - [MSTL](https://www.statsmodels.org/stable/generated/statsmodels.tsa.seasonal.MSTL.html)(endog, ...)
  - Descomposición de tendencia de la estacionalidad usando _LOESS_ para múltiples estacionalidades.
* - [STL](https://www.statsmodels.org/stable/generated/statsmodels.tsa.seasonal.STL.html)(endog, ...)
  - Descomposición de tendencia de la estacionalidad usando _LOESS_.
* - [bkfilter](https://www.statsmodels.org/stable/generated/statsmodels.tsa.filters.bk_filter.bkfilter.html)(x, ...)
  - Filtra una serie temporal utilizando el filtro _bandpass_ _Baxter-King_.
* - [cffilter](https://www.statsmodels.org/stable/generated/statsmodels.tsa.filters.cf_filter.cffilter.html)(x, ...)
  - Filtro asimétrico de caminata aleatoria de _Christiano Fitzgerald_ Asimétrico.
* - [hpfilter](https://www.statsmodels.org/stable/generated/statsmodels.tsa.filters.hp_filter.hpfilter.html)(x, ...)
  - Filtro _Hodrick-Prescott_.
* - [seasonal_decompose](https://www.statsmodels.org/stable/generated/statsmodels.tsa.seasonal.seasonal_decompose.html)(x, ...)
  - Descomposición estacional utilizando promedios móviles.
```

### Notas de _seasonal_decompose_

[seasonal_decompose](https://www.statsmodels.org/stable/generated/statsmodels.tsa.seasonal.seasonal_decompose.html): Descomposición estacional utilizando promedios móviles.

```python
# Sintaxis de llamada
seasonal_decompose(x, model='additive', filt=None, period=None, two_sided=True, extrapolate_trend=0)
```
- **Parámetros:**
    - **x** - `array-like`: La serie de tiempo, debe de contener dos cíclos completos. Si es 2D entonces cada serie debe estar en las columnas.
	- **period** - `int`: Se debe de utilizar si _x_ no es un objeto de `pandas` o si el índice de _x_ no tiene una frecuencia. Si _x_ tiene un `Index` de tiempo, entonces se sobreescribe la periocidad por default.
- **Retorna:**
    - `DecomposeResult`. Ver {ref}``

**Uso**

```python
# Importaciones de funciones
from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib.pyplot as plt

# Aplicar descomposición estacional (modelo aditivo por defecto)
decomposition = seasonal_decompose(series, period=12) # Periodo estacional = 12 (mensual)

# Obtener componentes
trend = decomposition.trend
seasonal = decomposition.seasonal
residual = decomposition.resid

# Graficar todos los componentes
decomposition.plot(decomposition)

# Graficar serie original
plt.figure(figsize=(10, 8))
plt.subplot(411)
plt.plot(series, label='Original')
plt.legend(loc='upper left')

# Graficar componente de tendencia
plt.subplot(412)
plt.plot(trend, label='Tendencia')
plt.legend(loc='upper left')

# Graficar componente estacional
plt.subplot(413)
plt.plot(seasonal, label='Estacionalidad')
plt.legend(loc='upper left')

# Graficar componente residual
plt.subplot(414)
plt.plot(residual, label='Residuo')
plt.legend(loc='upper left')
plt.tight_layout()
plt.show()
```

<br/>

## Forecasting

Herramientas para predecir valores futuros en series temporales.

:::{note}
Notar que todas son clases.
:::

```{list-table}
:header-rows: 1

* - Constructor
  - Descripción
* - [STLForecast](https://www.statsmodels.org/stable/generated/statsmodels.tsa.forecasting.stl.STLForecast.html)(endog, model, ...)
  - Pronóstico basado en modelos utilizando _STL_ para eliminar la estacionalidad.
* - [ThetaModel](https://www.statsmodels.org/stable/generated/statsmodels.tsa.forecasting.theta.ThetaModel.html)(endog, ...)
  - El modelo de pronóstico _Theta_ de _Assimakopoulos y Nikolopoulos (2000)_.
```

<br/>

## Modelos de Cambio de Régimen de Markov

Modelos que capturan cambios en el comportamiento de una serie temporal a lo largo del tiempo, como cambios en la media o varianza. 

:::{note}
Notar que todas son clases.
:::

```{list-table}
:header-rows: 1

* - Constructor
  - Descripción
* - [MarkovAutoregression](https://www.statsmodels.org/stable/generated/statsmodels.tsa.regime_switching.markov_autoregression.MarkovAutoregression.html)(endog, k_regimes, order)
  - Modelo de regresión de conmutación de Markov.
* - [MarkovRegression](https://www.statsmodels.org/stable/generated/statsmodels.tsa.regime_switching.markov_regression.MarkovRegression.html)(endog, k_regimes, ...)
  - Modelo de regresión de conmutación Markov K-Regime de primer orden.
```

<br/>

## Modelos de Series Temporales Multivariadas

Técnicas para analizar múltiples series temporales relacionadas, como modelos VAR (Vector Autoregression).

:::{note}
Notar que todas son clases.
:::

```{list-table}
:header-rows: 1

* - Constructor
  - Descripción
* - [DynamicFactor](https://www.statsmodels.org/stable/generated/statsmodels.tsa.statespace.dynamic_factor.DynamicFactor.html)(endog, k_factors, factor_order)
  - Modelo de factor dinámico.
* - [DynamicFactorMQ](https://www.statsmodels.org/stable/generated/statsmodels.tsa.statespace.dynamic_factor_mq.DynamicFactorMQ.html)(endog, ...)
  - Modelo de factor dinámico con algoritmo EM; Opción para datos mensuales/trimestrales.
* - [SVAR](https://www.statsmodels.org/stable/generated/statsmodels.tsa.vector_ar.svar_model.SVAR.html)(endog, svar_type, ...)
  - Ajusta de VAR y luego estimA los componentes estructurales de A y B.
* - [UnobservedComponents](https://www.statsmodels.org/stable/generated/statsmodels.tsa.statespace.structural.UnobservedComponents.html)(endog, ...)
  - Modelo de series de tiempo de componentes no observados univariados.
* - [VAR](https://www.statsmodels.org/stable/generated/statsmodels.tsa.vector_ar.var_model.VAR.html)(endog, ...)
  - Ajusta _Var(P)_ y realiza la selección de orden de desfases.
* - [VARMAX](https://www.statsmodels.org/stable/generated/statsmodels.tsa.statespace.varmax.VARMAX.html)(endog, ...)
  - Promedio móvil vectorial autorregresivo con modelo de regresores exógenos.
* - [VECM](https://www.statsmodels.org/stable/generated/statsmodels.tsa.vector_ar.vecm.VECM.html)(endog, ...)
  - Clase que representa un modelo de corrección de errores vectoriales (VECM).
```

<br/>

## Estadísticas y Pruebas

Pruebas para evaluar propiedades de series temporales, como estacionariedad (ADF, KPSS) o autocorrelación.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [acf](https://www.statsmodels.org/stable/generated/statsmodels.tsa.stattools.acf.html)(x, ...)
  - Calcula la función de autocorrelación.
* - [acovf](https://www.statsmodels.org/stable/generated/statsmodels.tsa.stattools.acovf.html)(x, ...)
  - Estima las autocovariaciones.
* - [adfuller](https://www.statsmodels.org/stable/generated/statsmodels.tsa.stattools.adfuller.html)(x, ...)
  - Prueba de raíz de la unidad _Dickey-Fuller_ aumentada.
* - [bds](https://www.statsmodels.org/stable/generated/statsmodels.tsa.stattools.bds.html)(x, ...)
  - Estadística de prueba de _BDS_ para la independencia de una serie de tiempo.
* - [ccf](https://www.statsmodels.org/stable/generated/statsmodels.tsa.stattools.ccf.html)(x, y, ...)
  - La función de correlación cruzada.
* - [ccovf](https://www.statsmodels.org/stable/generated/statsmodels.tsa.stattools.ccovf.html)(x, y, ...)
  - Calcula la covarianza cruzada entre dos series.
* - [coint](https://www.statsmodels.org/stable/generated/statsmodels.tsa.stattools.coint.html)(y0, y1, ...)
  - Prueba para la no cointegración de una ecuación univariada.
* - [kpss](https://www.statsmodels.org/stable/generated/statsmodels.tsa.stattools.kpss.html)(x, ...)
  - Prueba _Kwiatkowski-Phillips-Schmidt-Shin_ para estacionariedad.
* - [pacf](https://www.statsmodels.org/stable/generated/statsmodels.tsa.stattools.pacf.html)(x, ...)
  - Estimación parcial de autocorrelación.
* - [pacf_ols](https://www.statsmodels.org/stable/generated/statsmodels.tsa.stattools.pacf_ols.html)(x, ...)
  - Calcula las autocorrelaciones parciales a través de _OLS_.
* - [pacf_yw](https://www.statsmodels.org/stable/generated/statsmodels.tsa.stattools.pacf_yw.html)(x, ...)
  - Autocorrelación parcial estimada con _Yule_walker_ no recursivo.
* - [q_stat](https://www.statsmodels.org/stable/generated/statsmodels.tsa.stattools.q_stat.html)(x, nobs)
  - Calcula la estadística de _Ljung-Box Q_.
* - [range_unit_root_test](https://www.statsmodels.org/stable/generated/statsmodels.tsa.stattools.range_unit_root_test.html)(x, ...)
  - Prueba de raíz unitaria de rango para estacionariedad.
* - [zivot_andrews](https://www.statsmodels.org/stable/generated/statsmodels.tsa.stattools.zivot_andrews.html)()
  - Prueba de raíz de ruptura estructural de _Zivot-Andrews_.
```

<br>

### Notas de _acf_

[acf](https://www.statsmodels.org/stable/generated/statsmodels.tsa.stattools.acf.html): Calcula los valores de la función de autocorrelación (las correlaciones en cada desfase).
```python
# Sintaxis de llamada
acf(x, adjusted=False, nlags=None, qstat=False, fft=True, alpha=None, bartlett_confint=True,
    missing='none')
```
- **Parámetros:**
    - **x** - `array-like`: Array de valores de la serie de tiempo.
- **Retorna:**
    - _acf_ - `ndarray`.
    - _confint_ - `ndarray` si `alpha = None`.
    - qstat - `ndarray` si `qstat = True`.
    - pvalues - `ndarray` si `qstat = True`.

<br>

### Notas de _adfuller_

[adfuller](https://www.statsmodels.org/stable/generated/statsmodels.tsa.stattools.adfuller.html): Realiza una prueba de Dickey-Fuller aumentada (ADF) que es una prueba de raíz unitaria para una muestra de una serie de tiempo. La hipótesis nula es que la serie es una camina aleatoria (no estacionaria). También se puede usar para probar que una serie sea estacionaria, siendo la hipótesis nula que la serie de tiempo no es estacionaria, aunque en este caso la prueba no verifica la que la varianza ni que la autocorrelacioón sean constantes.
```python
# Sintaxis de llamada
adfuller(x, maxlag=None, regression='c', autolag='AIC', store=False, regresults=False)
```
- **Parámetros:**
    - **x** - `1D array-like`: Los datos de la serie.
	- **Tip**: Para imprimir todos los resultados imprimir todo el objeto donde se almacenó los resultados de esta función.
- **Retorna:**
    - `tuple`:
        - _adf_ - `float`: Estadístico de prueba, entre más negativo más probable que no sea una caminata aleatoria (sea estacionaria).
        - _pvalue_ - `float`: Si el valor _p_ es 0.05 o menor entonces se puede rechazar la hipótesis nula (el valor _p_ es el segundo elemento de la tupla retornada).
        - _usedlag_ - `int`
        - _nobs_ - `int`
        - _critical_values_ - `dict`
        - _icbest_ - `float`
        - _resstore_ - `ResultStore`

<br/>

## Herramientas de Series Temporales

Funciones auxiliares para manipulación y análisis de series temporales. 

```{list-table}
:header-rows: 1

* - Constructor/Función
  - Descripción
* - [DeterministicProcess](https://www.statsmodels.org/stable/generated/statsmodels.tsa.deterministic.DeterministicProcess.html)(index, ...)
  - Clase de contenedor para términos deterministas.
* - [add_lag](https://www.statsmodels.org/stable/generated/statsmodels.tsa.tsatools.add_lag.html)(x, ...)
  - Retorna un arreglo con los desfases incluidos dados.
* - [add_trend](https://www.statsmodels.org/stable/generated/statsmodels.tsa.tsatools.add_trend.html)(x, ...)
  - Agrega una tendencia y/o constante a un arreglo.
* - [detrend](https://www.statsmodels.org/stable/generated/statsmodels.tsa.tsatools.detrend.html)(x, ...)
  - Elima la tendencia de un arreglo con una tendencia de orden dado a lo largo del eje 0 o 1.
* - [lagmat](https://www.statsmodels.org/stable/generated/statsmodels.tsa.tsatools.lagmat.html)(x, maxlag, ...)
  - Crea matriz de desfases.
* - [lagmat2ds](https://www.statsmodels.org/stable/generated/statsmodels.tsa.tsatools.lagmat2ds.html)(x, maxlag0, ...)
  - Genera _lagmatrix_ para la matriz 2D, columnas dispuestas como variables.
```

<br/>

## Análisis de Series Temporales Univariadas

Métodos para modelar y analizar series temporales individuales, como AR, MA y _ARIMA_.

### Clases

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [ARDL](https://www.statsmodels.org/stable/generated/statsmodels.tsa.ardl.ARDL.html)(endog, lags, ...)
  - Ajusta un modelo de desfase distribuido autorregresivo (ARDL).
* - [ARIMA](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMA.html)(endog, ...)
  - Ajusta un modelo de promedio móvil integrado autorregresivo (ARIMA) y extensiones.
* - [ArmaProcess](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima_process.ArmaProcess.html)(...)
  - Propiedades teóricas de un proceso _ARMA_ para polinomios de desfase especificados.
* - [AutoReg](https://www.statsmodels.org/stable/generated/statsmodels.tsa.ar_model.AutoReg.html)(endog, lags, ...)
  - Ajusta un modelo AR-X(P) autorregresivo.
* - [SARIMAX](https://www.statsmodels.org/stable/generated/statsmodels.tsa.statespace.sarimax.SARIMAX.html)(endog, ...)
  - Promedio móvil integrado autorregresivo estacional con modelo de regresores exógenos.
* - [UECM](https://www.statsmodels.org/stable/generated/statsmodels.tsa.ardl.UECM.html)(endog, lags, ...)
  - Ajusta un modelo de correlación de error sin restricciones (UECM).
```

#### ARIMA

[ARIMA](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMA.html): Ajusta un modelo autoregresivo integrado de media móvil (por sus siglas en inglés ). Es la interface básica para los modelos de tipo _ARIMA_. La forma más general del modelo es _SARIMAX(p, d, q)x(P, D, Q, s)_. Permite todos las casos especiales:
- autoregressive models: _AR(p)_
- moving average models: _MA(q)_
- mixed autoregressive moving average models: _ARMA(p, q)_
- integration models: _ARIMA(p, d, q)_
- seasonal models: _SARIMA(P, D, Q, s)_

```python
# Sintaxis de llamada
ARIMA(endog, exog=None, order=(0, 0, 0), seasonal_order=(0, 0, 0, 0), trend=None, 
      enforce_stationarity=True, enforce_invertibility=True, concentrate_scale=False, 
      trend_offset=1, dates=None, freq=None, missing='none', validate_specification=True)
```
**Parámetros:**
    - **endog** - `array-like`: El proceso de series de tiempo _y_ observado.
    - **exog** - `array-like`: Variable de regresión exógena. Las variables exógenas son variables independientes de las endógenas pero que guardan cierta relación con ellas, es decir, pueden influir en ellas. Por ejemplo, se tiene una serie de tiempo de productividad, y se tiene una variable exógena de horas de sueño. Idóneameante solo se deben de considerar las variables exógenas relevantes, en caso de que haya, cuidando la multicolinealidad y se deben de tener los valores futuros de esa variable para poder hacer pronósticos.
    - **order** - `tuple` de `int: [0, ∞)`: El orden _(p, d, q)_ del modelo para los componentes de autogresión (_AR_), desfases y y media móvil (_MA_). _d_ siempre es `int` positivo o cero, mientras que _p_ y _q_ pueden ser `int` o `list` de `int` (positivos o cero). Notar que esto establece el orden del modelo, y no tiene nada que ver con los coeficientes $\phi$ o $\theta$. Para omitir un componente simplemente utilizar un cero como valor.
    - **seasonal_order** - `tuple`: El orden _(P, D, Q, S)_ del modelo para los componentes estacionales. _D_ es `int` indica la orden del proceso integrado. _P_ y _Q_ pueden ser `int` que indican la órden de los modelos _MA_ y _AR_ o `iterable` que indican desfases específicos a incluir, _S_ es `int` e indica la periocidad, por ejemplo 12 para cada mes, 4 para cada trimestres, etc.
    - **trend** - {'n','c','t','ct'} o `list-like`: Parámetros que controla la tendencia determnística polinomial.
        - _n_: No incluir un componete de tendencia.
        - _c_: Constante (componente de grado cero del polinomio). Importante cuando la serie no está alrededor del cero.
        - _t_: Tendencia lineal con el tiempo.
        - _ct_: Los dos anteriores.
        - Se puede indicar las constante de los polinomios, en orden ascendente `a, bt, ct2, ...` (no agegar la variable, solo la constante).
**Retorna:**
    - `ARIMAResults`.

:::{tip}
El objeto retornado por el método `.fit` tiene varios atributos y métodos útiles. Ver {ref}`others-ArimaResults`. Entre los más importantes están:
- [.summary()](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMAResults.summary.html): Resumen el modelo.
- [.get_forecast](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMAResults.get_forecast.html): Pronósticos fuera de la muestra e intervalos de predicción.
- [.get_prediction](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMAResults.get_prediction.html): Predicción en la muestra y pronóstico fuera de la muestra.
- [.plot_diagnostics](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMAResults.plot_diagnostics.html): Gráficos de diagnóstico para residuos estandarizados de una variable endógena.
- [.params](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMAResults.aic.html): Parámetros del modelo.
- [.aic](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMAResults.aic.html): Criterio de información de Akaike.
- [.bic](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMAResults.bic.html): Criterio de información de Bayes.
:::

##### Uso

Uso básico de la clase `ARIMA`.


```python
# Importar clase ARIMA  
from statsmodels.tsa.arima.model import ARIMA  

# ==============================================  
# 1. Modelo ARMA(p, q) (sin diferenciación, d=0)  

# Crear y ajustar modelo ARMA(1,1)  
modelo_arma = ARIMA(datos, order=(1, 0, 1))  # AR(1) + MA(1)  
resultados_arma = modelo_arma.fit()  

# Resumen del modelo ARMA  
print(resultados_arma.summary())  

# Predecir siguientes 3 valores  
pred_arma = resultados_arma.forecast(steps=3)  
print("Predicción ARMA(1,1):", pred_arma.predicted_mean)
print("Intervalos de confianza ARMA(1,1):", pred_arma.conf_int())

# Predecir las ultima 5 observaciones
pred_in_arma = resultados_arma.forecast(start=-5)  
print("Predicción ARMA(1,1):", pred_in_arma.predicted_mean)
print("Intervalos de confianza ARMA(1,1):", pred_in_arma.conf_int())

# ==============================================  
# 2. Modelo ARIMA(p, d, q) (con diferenciación)  

# Crear y ajustar modelo ARIMA(1,1,1)  
modelo_arima = ARIMA(datos, order=(1, 1, 1))  # AR(1) + I(1) + MA(1)  
resultados_arima = modelo_arima.fit()  

# Resumen del modelo ARIMA  
print(resultados_arima.summary())  

# Predecir siguientes 3 valores  
pred_arima = resultados_arima.forecast(steps=3)  
print("Predicción ARIMA(1,1,1):", pred_arima)  

# Graficar predicciones vs datos reales  
import matplotlib.pyplot as plt  
plt.plot(datos, label='Datos reales')  
plt.plot(pred_arima, label='Predicción ARIMA', linestyle='--')  
plt.legend()  
plt.show()  
```


<br/>

##### Atributos

Propiedades de la clase `ARIMA`. 

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - [endog_names](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMA.endog_names.html)
  - Nombres de variables endógenas.
* - [exog_names](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMA.exog_names.html)
  - Los nombres de las variables exógenas.
* - [initial_design](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMA.initial_design.html)
  - Matriz de diseño inicial.
* - [initial_selection](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMA.initial_selection.html)
  - Matriz de selección inicial.
* - [initial_state_intercept](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMA.initial_state_intercept.html)
  - Vector de intercepción de estado inicial.
* - [initial_transition](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMA.initial_transition.html)
  - Matriz de transición inicial.
* - [initial_variance](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMA.initial_variance.html)
  - .
* - [initialization](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMA.initialization.html)
  - .
* - [loglikelihood_burn](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMA.loglikelihood_burn.html)
  - .
* - [model_latex_names](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMA.model_latex_names.html)
  - Los nombres como látex de todos los parámetros del modelo posibles.
* - [model_names](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMA.model_names.html)
  - Los nombres de texto sin formato de todos los parámetros del modelo posibles.
* - [model_orders](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMA.model_orders.html)
  - Las órdenes de cada uno de los polinomios en el modelo.
* - [param_names](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMA.param_names.html)
  - Lista de nombres de parámetros legibles por humanos (para parámetros realmente incluidos en el modelo).
* - [param_terms](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMA.param_terms.html)
  - Lista de parámetros realmente incluidos en el modelo, ordenados.
* - [params_complete](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMA.params_complete.html)
  - .
* - [start_params](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMA.start_params.html)
  - Parámetros iniciales para una estimación de máxima probabilidad.
* - [state_names](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMA.state_names.html)
  - Lista de nombres legibles por humanos para estados no observados.
* - [tolerance](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMA.tolerance.html)
  - .
```

##### Métodos

Métodos de la clase `ARIMA`. 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - **Principales métodos**
  -
* - [fit](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMA.fit.html)(...)
  - Ajusta (estima) los parámetros del modelo. Ver {ref}`others-ArimaResults`.
* - [predict](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMA.predict.html)(params, ...)
  - Después de que un modelo se haya ajustado, devuelve los valores ajustados.
* - [score](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMA.score.html)(params, *args, **kwargs)
  - Calcula la función de puntuación en _params_.
* - [simulate](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMA.simulate.html)(params, nsimulations, ...)
  - Simula una nueva serie de tiempo siguiendo el modelo de espacio estatal.
* - **Inicializar**
  -
* - [initialize](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMA.initialize.html)()
  - Inicializa el modelo Sarimax.
* - [initialize_approximate_diffuse](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMA.initialize_approximate_diffuse.html)(...)
  - Inicialización difusa aproximada.
* - [initialize_default](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMA.initialize_default.html)(...)
  - Inicializa el valor predeterminado.
* - [initialize_known](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMA.initialize_known.html)(initial_state, ...)
  - Inicialización conocida.
* - [initialize_statespace](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMA.initialize_statespace.html)(**kwargs)
  - Inicializa la representación del espacio de estado.
* - [initialize_stationary](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMA.initialize_stationary.html)()
  - Inicialización estacionaria.
* - **Otros**
  -
* - [clone](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMA.clone.html)(endog, ...)
  - Clona el modelo con nuevos datos y opcionalmente nueva especificación.
* - [filter](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMA.filter.html)(params, ...)
  - Filtrado de _Kalman_.
* - [fit_constrained](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMA.fit_constrained.html)(constraints, ...)
  - Ajusta el modelo con algunos parámetros sujetos a restricciones de igualdad.
* - [fix_params](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMA.fix_params.html)(params)
  - Corrige los parámetros a valores específicos (Administrador de contexto).
* - [handle_params](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMA.handle_params.html)(params, ...)
  - Se asegura de que los parámetros del modelo satisfagan la forma y otros requisitos.
* - [hessian](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMA.hessian.html)(params, *args, **kwargs)
  - Matriz Hessiana de la función de probabilidad, evaluada en los parámetros dados.
* - [impulse_responses](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMA.impulse_responses.html)(params, ...)
  - Función de respuesta de impulso.
* - [information](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMA.information.html)(params)
  - Matriz de información de _Fisher_ del modelo.
* - [loglike](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMA.loglike.html)(params, *args, **kwargs)
  - Evaluación de _loglikelihood_.
* - [loglikeobs](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMA.loglikeobs.html)(params, ...)
  - Evaluación de _loglikelihood_.
* - [observed_information_matrix](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMA.observed_information_matrix.html)(params, ...)
  - Matriz de información observada.
* - [opg_information_matrix](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMA.opg_information_matrix.html)(params, ...)
  - Producto externo de los gradiantes de la matriz de información.
* - [prepare_data](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMA.prepare_data.html)()
  - Prepara datos para su uso en la representación del espacio de estado.
* - [score_obs](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMA.score_obs.html)(params, ...)
  - Calcula la puntuación por observación, evaluada en _params_
* - [simulation_smoother](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMA.simulation_smoother.html)(...)
  - Recupera una simulación más suave para el modelo de espacio de estado.
* - [smooth](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMA.smooth.html)(params, ...)
  - Suavizando _Kalman_.
* - [transform_jacobian](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMA.transform_jacobian.html)(unconstrained, ...)
  - Matriz jacobiana para la función de transformación de parámetros.
* - [transform_params](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMA.transform_params.html)(unconstrained)
  - Transforma los parámetros sin restricciones utilizados por el optimizador a parámetros restringidos utilizados en la evaluación de probabilidad.
* - [untransform_params](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMA.untransform_params.html)(constrained)
  - Transforma los parámetros restringidos utilizados en la evaluación de probabilidad a los parámetros no restringidos utilizados por el optimizador.
* - [update](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMA.update.html)(params, ...)
  - Actualiza los parámetros del modelo.
* - **Establecer**
  -
* - [set_conserve_memory](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMA.set_conserve_memory.html)(...)
  - Establece el método de conservación de memoria.
* - [set_filter_method](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMA.set_filter_method.html)(...)
  - Establece el método de filtrado.
* - [set_inversion_method](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMA.set_inversion_method.html)(...)
  - Establece el método de inversión.
* - [set_smoother_output](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMA.set_smoother_output.html)(...)
  - Establece la salida más suave.
* - [set_stability_method](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMA.set_stability_method.html)(...)
  - Establece el método de estabilidad numérica.
```

<br/>

#### ArmaProcess

[ArmaProcess](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima_process.ArmaProcess.html): Propiedades teóricas de un proceso _ARMA_ para polinomios de desfase especificados.
```python
# Sintaxis de llamada
ArmaProcess(ar=None, ma=None, nobs=100)
```
**Parámetros:**
- **ar** - `array-like`: Coeficientes de los polinomios desfasados autoregresivos, incluyendo el desface cero (sieple incluir un uno al inicio). En otras palabras, son los valores de los parámetros $\phi_i$ del modelo _AR(p)_. El número de parámetros es proporcional (1:1) al orden del modelo (_n_), es decir si el modelo es de orden 2 entonces tiene dos parámetros $\phi_1$ y$\phi_2$. **Importante**: El parámetro se debe pasar con el signo contrario al que se desea que tenga.
- **ma** - `array-like`: Coeficientes de los polinomios desfadados de media móvil, incluyendo el desfase cero (siempre incluir un uno al inicio). En otras palabras, son los valores de los parámetros $\theta_i$ del modelo MA(q). El número de parámetros es proporcional (1:1) al orden del modelo (_n_), es decir si el modelo es de orden 2 entonces tiene dos parámetros $\theta_1$ y $\theta_2$.
- **nobs** - `1D array-like`: Longitud de la serie de tiempo simulada.

:::{important}
Tener en cuenta las siguientes características al definir los parámetros _ar_ y _ma_:
- El primer elemento en ambos caso debe de ser un uno: `ar = [1, ...]` o `ma = [1, ...]`.
- Si se desea omitir _ar_ o _ma_ se debe de asignar un `array-like` cuyo único elemento sea un uno: `ar=[1]` o `ma=[1]`.
- Los coeficientes del parámetro _ar_ se deben de pasar con el signo contrario al que se desea, por ejemplo, si se desea un $\phi=0.5$, entonces se debe de pasar `ar = [1, -0.5]`.
:::

##### Uso

Uso básico de la clase `ArmaProcess`

:::{tip}
Alternativamente se puede usar la función `arma_generate_sample()` para simular procesos _ARMA_.
:::

```python
# Importar la clase necesaria  
from statsmodels.tsa.arima_process import ArmaProcess  

# Definir coeficientes AR y MA (ejemplo: AR(1) y MA(1))  
ar_coefs = np.array([1, -0.7])  # Coeficientes AR (incluye 1 para el lag 0)  
ma_coefs = np.array([1, 0.4])   # Coeficientes MA (incluye 1 para el lag 0)  

# Crear proceso ARMA  
arma_proceso = ArmaProcess(ar=ar_coefs, ma=ma_coefs)  

# Simular datos del proceso ARMA  
muestras = 1000  
serie_simulada = arma_proceso.generate_sample(nsample=muestras)  

# Graficar la serie simulada  
import matplotlib.pyplot as plt  
plt.plot(serie_simulada)  
plt.title("Serie temporal simulada ARMA")  
plt.show()  

# Calcular función de autocorrelación (ACF)  
acf = arma_proceso.acf(lags=20)  

# Calcular función de autocorrelación parcial (PACF)  
pacf = arma_proceso.pacf(lags=20)  

# Verificar estacionariedad e invertibilidad  
es_estacionario = arma_proceso.isstationary  
es_invertible = arma_proceso.isinvertible  
print(f"¿Es estacionario? {es_estacionario}")  
print(f"¿Es invertible? {es_invertible}")  
```
- Si se desea simular solo un modelo _AR_ o _MA_, usar `[1]` o `None` como coeficientes de _AR_ o _MA_, según se desee omitir.

<br/>

##### Propiedades

Atributos de la clase `ArmaProcess`. 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [arroots](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima_process.ArmaProcess.arroots.html)
  - Raíces del polinomio desfasado autorregresivo.
* - [isinvertible](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima_process.ArmaProcess.isinvertible.html)
  - El proceso _ARMA_ es invertible si las raíces de _MA_ están afuera de un círculo unitario.
* - [isstationary](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima_process.ArmaProcess.isstationary.html)
  - El proceso _ARMA_ es estacionario si las raíces de _AR_ están afuera de un círculo unitario.
* - [maroots](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima_process.ArmaProcess.maroots.html)
  - Raíces de promedio móvil del polinomio desfasado.
```

<br/>

##### Métodos

Métodos de la clase `ArmaProcess`. 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [acf](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima_process.ArmaProcess.acf.html)(...)
  - Función teórica de autocorrelación de un proceso _ARMA_.
* - [acovf](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima_process.ArmaProcess.acovf.html)(...)
  - Autocovarianzas teóricas de procesos _ARMA_ estacionarios..
* - [arma2ar](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima_process.ArmaProcess.arma2ar.html)(...)
  - Una representación AR aproximada de desfases finitos de un proceso _ARMA_.
* - [arma2ma](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima_process.ArmaProcess.arma2ma.html)(...)
  - Una representación MA aproximada de desfases finitos de un proceso _ARMA_.
* - [from_coeffs](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima_process.ArmaProcess.from_coeffs.html)(...)
  - Crea un `ArmaProcess` a partir de una representación _ARMA_.
* - [from_estimation](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima_process.ArmaProcess.from_estimation.html)(model_results, ...)
  - Crea un `ArmaProcess` a partir de los resultados de una estimación _ARIMA_.
* - [from_roots](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima_process.ArmaProcess.from_roots.html)(...)
  - Crea UN `ArmaProcess` a partir de raíces polinomiales _AR_ y _MA_.
* - [generate_sample](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima_process.ArmaProcess.generate_sample.html)(...)
  - Simula datos de un _ARMA_.
* - [impulse_response](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima_process.ArmaProcess.impulse_response.html)(...)
  - Calcula la función de respuesta de impulso (representación de _M_A) para el proceso _ARMA_.
* - [invertroots](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima_process.ArmaProcess.invertroots.html)(...)
  - Hace un polinomial MA invertible, la invertir sus raíces dentro del círculo unitario.
* - [pacf](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima_process.ArmaProcess.pacf.html)(...)
  - Función teórica de autocorrelación parcial de un proceso _ARMA_.
* - [periodogram](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima_process.ArmaProcess.periodogram.html)(...)
  - Periodograma para el proceso _ARMA_ dado por polinomios desfasados _AR_ y _MA_.
```

<br/>

#### SARIMAX

[SARIMAX](https://www.statsmodels.org/stable/generated/statsmodels.tsa.statespace.sarimax.SARIMAX.html): Modelo autoregresivo integrado de media móvil estacional con regresores exógenos.
```python
# Sintaxis de llamada
SARIMAX(endog, exog=None, order=(1, 0, 0), seasonal_order=(0, 0, 0, 0), trend=None, 
        measurement_error=False, time_varying_regression=False, mle_regression=True, 
        simple_differencing=False, enforce_stationarity=True, enforce_invertibility=True, 
        hamilton_representation=False, concentrate_scale=False, trend_offset=1, 
        use_exact_diffuse=False, dates=None, freq=None, missing='none', 
        validate_specification=True, **kwargs)
```

**Parámetros:**
- **endog** - `array-like`: El proceso de series de timepo y observado.
- **exog** - `array-like`: Variables de regresión exógenas.
- **order** - `tuple`: El orden (p, d, q) del modelo para los componentes de autogresión (AR), desfases y y media móvil (MA). d siempre es `int`, mientras que p y q pueden ser `int` o `list` de `int`.
- **seasonal_order** - `tuple`: El orden _(P, D, Q, S)_ del modelo para los componentes estacionales. _D_ es `int` indica la orden del proceso integrado. _P_ y _Q_ pueden ser `int` que indican la órden de los modelos _MA_ y _AR_ o `iterable` que indican desfases específicos a incluir, _S_ es `int` e indica la periocidad, por ejemplo 12 para cada mes, 4 para cada trimestres, etc.
- **trend** - {'n','c','t','ct'} o `list-like`: Parámetros que controla la tendencia determnística polinomial.
    - _n_: No incluir un componete de tendencia.
    - _c_: Constante (componente de grado cero del polinomio). Importante cuando la serie no está alrededor del cero.
    - _t_: Tendencia lineal con el tiempo.
    - _ct_: Los dos anteriores.
    - Se puede indicar las constante de los polinomios, en orden ascendente `a, bt, ct2, ...` (no agegar la variable, solo la constante).

:::{tip}
El objeto retornado por el método `.fit` tiene varios atributos y métodos útiles. Ver {ref}`others-ArimaResults`. Entre los más importantes están:
- [.summary()](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMAResults.summary.html): Resumen el modelo.
- [.get_forecast](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMAResults.get_forecast.html): Pronósticos fuera de la muestra e intervalos de predicción.
- [.get_prediction](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMAResults.get_prediction.html): Predicción en la muestra y pronóstico fuera de la muestra.
- [.plot_diagnostics](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMAResults.plot_diagnostics.html): Gráficos de diagnóstico para residuos estandarizados de una variable endógena.
- [.params](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMAResults.aic.html): Parámetros del modelo.
- [.aic](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMAResults.aic.html): Criterio de información de Akaike.
- [.bic](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMAResults.bic.html): Criterio de información de Bayes.
:::

##### Uso

Uso básico de la clase `SARIMAX`

```python
# Importar la clase SARIMAX  
from statsmodels.tsa.statespace.sarimax import SARIMAX  
import pandas as pd  
 

# ==============================================  
# 1. Modelo SARIMA (sin variables exógenas)  
# ==============================================  
# Crear y ajustar modelo 
modelo_sarima = SARIMAX(  
    datos,  
    order=(p, d, q),            
    seasonal_order=(P, D, Q, s), 
    trend='c'                    
)  
resultados_sarima = modelo_sarima.fit(disp=False)  

# Resumen del modelo  
print(resultados_sarima.summary())  

# Predecir siguientes 3 valores  
pred_sarima = resultados_sarima.forecast(steps=3)  
print("Predicción SARIMA:", pred_sarima)  

# ==============================================  
# 2. Modelo SARIMAX (con variables exógenas)  
# ==============================================  

# Crear y ajustar modelo SARIMAX  
modelo_sarimax = SARIMAX(  
    datos,  
    exog=exog,                   # Variables exógenas  
    order=(p, d, q),            
    seasonal_order=(P, D, Q, s),
    trend='c'  
)  
resultados_sarimax = modelo_sarimax.fit(disp=False)  

# Resumen del modelo  
print(resultados_sarimax.summary())  

# Predecir con nuevos datos exógenos  
nuevo_exog = pd.Series([2, 1, 2])  
pred_sarimax = resultados_sarimax.forecast(steps=3, exog=nuevo_exog)  
print("Predicción SARIMAX:", pred_sarimax)  

# Graficar ajuste del modelo  
resultados_sarima.plot_diagnostics(figsize=(10, 8))  
plt.show()  
```

<br/>

##### Propiedades

Métodos de la clase `SARIMAX`. 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [endog_names](https://www.statsmodels.org/stable/generated/statsmodels.tsa.statespace.sarimax.SARIMAX.endog_names.html)
  - Nombres de variables endógenas.
* - [exog_names](https://www.statsmodels.org/stable/generated/statsmodels.tsa.statespace.sarimax.SARIMAX.exog_names.html)
  - Los nombres de las variables exógenas.
* - [initial_design](https://www.statsmodels.org/stable/generated/statsmodels.tsa.statespace.sarimax.SARIMAX.initial_design.html)
  - Matriz de diseño inicial.
* - [initial_selection](https://www.statsmodels.org/stable/generated/statsmodels.tsa.statespace.sarimax.SARIMAX.initial_selection.html)
  - Matriz de selección inicial.
* - [initial_state_intercept](https://www.statsmodels.org/stable/generated/statsmodels.tsa.statespace.sarimax.SARIMAX.initial_state_intercept.html)
  - Vector de intercepción de estado inicial.
* - [initial_transition](https://www.statsmodels.org/stable/generated/statsmodels.tsa.statespace.sarimax.SARIMAX.initial_transition.html)
  - Matriz de transición inicial.
* - [initial_variance](https://www.statsmodels.org/stable/generated/statsmodels.tsa.statespace.sarimax.SARIMAX.initial_variance.html)
  - .
* - [initialization](https://www.statsmodels.org/stable/generated/statsmodels.tsa.statespace.sarimax.SARIMAX.initialization.html)
  - .
* - [loglikelihood_burn](https://www.statsmodels.org/stable/generated/statsmodels.tsa.statespace.sarimax.SARIMAX.loglikelihood_burn.html)
  - .
* - [model_latex_names](https://www.statsmodels.org/stable/generated/statsmodels.tsa.statespace.sarimax.SARIMAX.model_latex_names.html)
  - Los nombres de látex de todos los parámetros del modelo posibles.. The latex names of all possible model parameters.
* - [model_names](https://www.statsmodels.org/stable/generated/statsmodels.tsa.statespace.sarimax.SARIMAX.model_names.html)
  - Los nombres como látex de todos los parámetros del modelo posibles.
* - [model_orders](https://www.statsmodels.org/stable/generated/statsmodels.tsa.statespace.sarimax.SARIMAX.model_orders.html)
  - Las órdenes de cada uno de los polinomios en el modelo.
* - [param_names](https://www.statsmodels.org/stable/generated/statsmodels.tsa.statespace.sarimax.SARIMAX.param_names.html)
  - Lista de nombres de parámetros legibles por humanos (para parámetros realmente incluidos en el modelo).
* - [param_terms](https://www.statsmodels.org/stable/generated/statsmodels.tsa.statespace.sarimax.SARIMAX.param_terms.html)
  - Lista de parámetros realmente incluidos en el modelo, ordenados.
* - [params_complete](https://www.statsmodels.org/stable/generated/statsmodels.tsa.statespace.sarimax.SARIMAX.params_complete.html)
  - .
* - [start_params](https://www.statsmodels.org/stable/generated/statsmodels.tsa.statespace.sarimax.SARIMAX.start_params.html)
  - Parámetros iniciales para una estimación de máxima probabilidad.
* - [state_names](https://www.statsmodels.org/stable/generated/statsmodels.tsa.statespace.sarimax.SARIMAX.state_names.html)
  - Lista de nombres legibles por humanos para estados no observados.
* - [tolerance](https://www.statsmodels.org/stable/generated/statsmodels.tsa.statespace.sarimax.SARIMAX.tolerance.html)
  - .
```


<br/>

##### Métodos

Métodos de la clase `SARIMAX`. 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - **Principales métodos**
  -
* - [fit](https://www.statsmodels.org/stable/generated/statsmodels.tsa.statespace.sarimax.SARIMAX.fit.html)(...)
  - Ajusta el modelo por máxima verosimilitud a través del filtro Kalman.
* - [predict](https://www.statsmodels.org/stable/generated/statsmodels.tsa.statespace.sarimax.SARIMAX.predict.html)(params, ...)
  - Después de que un modelo se haya ajustado, devuelve los valores ajustados.
* - [score](https://www.statsmodels.org/stable/generated/statsmodels.tsa.statespace.sarimax.SARIMAX.score.html)(params, *args, **kwargs)
  - Calcula la función de puntuación en _params_.
* - [simulate](https://www.statsmodels.org/stable/generated/statsmodels.tsa.statespace.sarimax.SARIMAX.simulate.html)(params, nsimulations, ...)
  - Simula una nueva serie de tiempo siguiendo el modelo de espacio estatal.
* - **Inicializar**
  -
* - [initialize](https://www.statsmodels.org/stable/generated/statsmodels.tsa.statespace.sarimax.SARIMAX.initialize.html)()
  - Inicializa el modelo Sarimax.
* - [initialize_approximate_diffuse](https://www.statsmodels.org/stable/generated/statsmodels.tsa.statespace.sarimax.SARIMAX.initialize_approximate_diffuse.html)(...)
  - Inicialización difusa aproximada.
* - [initialize_default](https://www.statsmodels.org/stable/generated/statsmodels.tsa.statespace.sarimax.SARIMAX.initialize_default.html)(...)
  - Inicializa el valor predeterminado.
* - [initialize_known](https://www.statsmodels.org/stable/generated/statsmodels.tsa.statespace.sarimax.SARIMAX.initialize_known.html)(initial_state, ...)
  - Inicialización conocida.
* - [initialize_statespace](https://www.statsmodels.org/stable/generated/statsmodels.tsa.statespace.sarimax.SARIMAX.initialize_statespace.html)(**kwargs)
  - Inicializa la representación del espacio de estado.
* - [initialize_stationary](https://www.statsmodels.org/stable/generated/statsmodels.tsa.statespace.sarimax.SARIMAX.initialize_stationary.html)()
  - Inicialización estacionaria.
* - **Otros**
  -
* - [clone](https://www.statsmodels.org/stable/generated/statsmodels.tsa.statespace.sarimax.SARIMAX.clone.html)(endog, ...)
  - Clona el modelo con nuevos datos y opcionalmente nueva especificación.
* - [filter](https://www.statsmodels.org/stable/generated/statsmodels.tsa.statespace.sarimax.SARIMAX.filter.html)(params, ...)
  - Filtrado de _Kalman_.
* - [fit_constrained](https://www.statsmodels.org/stable/generated/statsmodels.tsa.statespace.sarimax.SARIMAX.fit_constrained.html)(constraints, ...)
  - Filtrado de _Kalman_.
* - [fix_params](https://www.statsmodels.org/stable/generated/statsmodels.tsa.statespace.sarimax.SARIMAX.fix_params.html)(params)
  - Corrige los parámetros a valores específicos (Administrador de contexto).
* - [handle_params](https://www.statsmodels.org/stable/generated/statsmodels.tsa.statespace.sarimax.SARIMAX.handle_params.html)(params, ...)
  - Se asegura de que los parámetros del modelo satisfagan la forma y otros requisitos.
* - [hessian](https://www.statsmodels.org/stable/generated/statsmodels.tsa.statespace.sarimax.SARIMAX.hessian.html)(params, *args, **kwargs)
  - Matriz Hessiana de la función de probabilidad, evaluada en los parámetros dados.
* - [impulse_responses](https://www.statsmodels.org/stable/generated/statsmodels.tsa.statespace.sarimax.SARIMAX.impulse_responses.html)(params, ...)
  - Función de respuesta de impulso.
* - [information](https://www.statsmodels.org/stable/generated/statsmodels.tsa.statespace.sarimax.SARIMAX.information.html)(params)
  - Matriz de información de _Fisher_ del modelo.
* - [loglike](https://www.statsmodels.org/stable/generated/statsmodels.tsa.statespace.sarimax.SARIMAX.loglike.html)(params, *args, **kwargs)
  - Evaluación de _loglikelihood_.
* - [loglikeobs](https://www.statsmodels.org/stable/generated/statsmodels.tsa.statespace.sarimax.SARIMAX.loglikeobs.html)(params, ...)
  - Evaluación de _loglikelihood_.
* - [observed_information_matrix](https://www.statsmodels.org/stable/generated/statsmodels.tsa.statespace.sarimax.SARIMAX.observed_information_matrix.html)(params, ...)
  - Matriz de información observada.
* - [opg_information_matrix](https://www.statsmodels.org/stable/generated/statsmodels.tsa.statespace.sarimax.SARIMAX.opg_information_matrix.html)(params, ...)
  - Producto externo de los gradiantes de la matriz de información.
* - [prepare_data](https://www.statsmodels.org/stable/generated/statsmodels.tsa.statespace.sarimax.SARIMAX.prepare_data.html)()
  - Prepara datos para su uso en la representación del espacio de estado.
* - [score_obs](https://www.statsmodels.org/stable/generated/statsmodels.tsa.statespace.sarimax.SARIMAX.score_obs.html)(params, ...)
  - Calcula la puntuación por observación, evaluada en _params_
* - [simulation_smoother](https://www.statsmodels.org/stable/generated/statsmodels.tsa.statespace.sarimax.SARIMAX.simulation_smoother.html)(...)
  - Recupera una simulación más suave para el modelo de espacio de estado.
* - [smooth](https://www.statsmodels.org/stable/generated/statsmodels.tsa.statespace.sarimax.SARIMAX.smooth.html)(params, ...)
  - Suavizando _Kalman_.
* - [transform_jacobian](https://www.statsmodels.org/stable/generated/statsmodels.tsa.statespace.sarimax.SARIMAX.transform_jacobian.html)(unconstrained, ...)
  - Matriz jacobiana para la función de transformación de parámetros.
* - [transform_params](https://www.statsmodels.org/stable/generated/statsmodels.tsa.statespace.sarimax.SARIMAX.transform_params.html)(unconstrained)
  - Transforma los parámetros sin restricciones utilizados por el optimizador a parámetros restringidos utilizados en la evaluación de probabilidad.
* - [untransform_params](https://www.statsmodels.org/stable/generated/statsmodels.tsa.statespace.sarimax.SARIMAX.untransform_params.html)(constrained)
  - Transforma los parámetros restringidos utilizados en la evaluación de probabilidad a los parámetros no restringidos utilizados por el optimizador.
* - [update](https://www.statsmodels.org/stable/generated/  - Actualiza los parámetros del modelo.
  - Actualiza los parámetros del modelo.
* - **Establecer**
  -
* - [set_conserve_memory](https://www.statsmodels.org/stable/generated/statsmodels.tsa.statespace.sarimax.SARIMAX.set_conserve_memory.html)(...)
  - Establece el método de conservación de memoria.. Set the memory conservation method.
* - [set_filter_method](https://www.statsmodels.org/stable/generated/statsmodels.tsa.statespace.sarimax.SARIMAX.set_filter_method.html)(...)
  - Establece el método de filtrado.. Set the filtering method.
* - [set_inversion_method](https://www.statsmodels.org/stable/generated/statsmodels.tsa.statespace.sarimax.SARIMAX.set_inversion_method.html)(...)
  - Establece el método de inversión.. Set the inversion method.
* - [set_smoother_output](https://www.statsmodels.org/stable/generated/statsmodels.tsa.statespace.sarimax.SARIMAX.set_smoother_output.html)(...)
  - Establece la salida más suave.. Set the smoother output.
* - [set_stability_method](https://www.statsmodels.org/stable/generated/statsmodels.tsa.statespace.sarimax.SARIMAX.set_stability_method.html)(...)
  - Establece el método de estabilidad numérica.. Set the numerical stability method.
```

<br/>

### Funciones

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [ardl_select_order](https://www.statsmodels.org/stable/generated/statsmodels.tsa.ardl.ardl_select_order.html)(endog, maxlag, exog, maxorder)
  - Selección de orden ARDL.
* - [arma_generate_sample](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima_process.arma_generate_sample.html)(ar, ma, nsample, ...)
  - Simular datos de un _ARMA_.
* - [arma_order_select_ic](https://www.statsmodels.org/stable/generated/statsmodels.tsa.stattools.arma_order_select_ic.html)(y, ...)
  - Calcula los criterios de información para muchos modelos _ARMA_.
```

#### Notas de _arma_generate_sample_

[arma_generate_sample](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima_process.arma_generate_sample.html): Simular datos de un modelo _ARMA_.

```python
# Sintaxis de llamada
arma_generate_sample(ar, ma, nsample, scale=1, distrvs=None, axis=0, burnin=0)
```
- **Parámetros:**
    - **ar** - `array-like`: Coeficientes de los polinomios desfasados autoregresivos, incluyendo el desface cero (siempre incluir un uno al inicio). En otras palabras, son los valores de los parámetros $\phi_i$ del modelo _AR(p)_. El número de parámetros es proporcional (1:1) al orden del modelo (n), es decir si el modelo es de orden 2 entonces tiene dos parámetros $\phi_1$ y $\phi_2$. El array sería sentonces `[1, -ϕ1, -ϕ2]`. Notar que los coeficientes $\phi$ se ponen con el signo contrario al que se desea.
	- **ma** - `array-like`: Coeficientes de los polinomios desfadados de media móvil, incluyendo el desfase cero (siempre incluir un uno al inicio). En otras palabras, son los valores de los parámetros $\theta_i$ del modelo MA(q). El número de parámetros es proporcional (1:1) al orden del modelo (n), es decir si el modelo es de orden 2 entonces tiene dos parámetros $\theta_1$ y $\theta_2$. El array sería entonces `[1, θ1, θ2.]`.
	- **nsample** - `int` o `tuple de int`: Número de muestras a generar, si es entero genera una array de 1D si es `tuple` genera un array de 2D+.
	- **scale** - `float`: Desviación estándar del ruido.
- **Retorna:**
    - `ndarray`.

**Uso**

```python
# Importación de funciones
from statsmodels.tsa.arima_process import arma_generate_sample
import numpy as np
import matplotlib.pyplot as plt

# Definir parámetros AR
ar_params = np.array([1, -0.75]) # Coeficientes AR, signo opuesto

# Definir parámetros MA
ma_params = np.array([1, 0.5])  # Coeficientes MA

# Definir número de muestras
num_samples = 100

# Generar muestra ARMA
arma_sample = arma_generate_sample(ar_params, ma_params, num_samples)

# Graficar muestra generada
plt.figure()
plt.plot(arma_sample)
plt.title('Muestra generada por ARMA')
plt.xlabel('Tiempo')
plt.ylabel('Valor')
plt.show()
```

<br/>

## Interfaz X12/X13

Integración con el software X-12-ARIMA y X-13ARIMA-SEATS para descomposición avanzada de series temporales.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [x13_arima_analysis](https://www.statsmodels.org/stable/generated/statsmodels.tsa.x13.x13_arima_analysis.html)(endog, ...)
  - Realiza el análisis X13-ARIMA para datos mensuales o trimestrales.
* - [x13_arima_select_order](https://www.statsmodels.org/stable/generated/statsmodels.tsa.x13.x13_arima_select_order.html)(endog, ...)
  - Realiza la identificación automática de orden de _ARIMA_ de estacional utilizando _ARIMA X12/X13_.
```

<br/>

