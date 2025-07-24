# Otras clases

Otras clases de utilidad.

(others-ArimaResults)=
## ArimaResults/SARIMAXResults

Es la clase retorna por el método `.fit()` de la clase `ARIMA` y `SARIMAX`.

:::{important}
Aunque en esta sección se presenta únicamente la clase `ArimaResults`, la clase `SARIMAXResults` también tiene la gran mayoría de métodos y atributos aquí presentados, por lo que se puede usar de referencia esta sección para esa clase también. Para más información de `SARIMAXResults` consultar la [documentación](https://www.statsmodels.org/stable/generated/statsmodels.tsa.statespace.sarimax.SARIMAXResults.html).
:::

:::{note}
Para más información de `ArimaResults` consultar la [documentación](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMAResults.html#statsmodels.tsa.arima.model.ARIMAResults) de _statsmodels_.
:::

### Propiedades

Métodos de la clase `ArimaResults`/`SARIMAXResults`.

:::{note}
Los links de esta sección llevan a la documentación de `ArimaResults`. Para más información de `SARIMAXResults` consultar la [documentación](https://www.statsmodels.org/stable/generated/statsmodels.tsa.statespace.sarimax.SARIMAXResults.html).
:::

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [aic](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMAResults.aic.html)
  - (flotante) Criterio de información de Akaike.
* - [aicc](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMAResults.aicc.html)
  - (flotante) Criterio de información de Akaike con una pequeña corrección de muestras.
* - [arfreq](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMAResults.arfreq.html)
  - (arreglo) frecuencia de las raíces de la forma reducida del polinomio desfasado autorregresivo.
* - [arparams](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMAResults.arparams.html)
  - (arreglo) Parámetros autorregresivos realmente estimados en el modelo.
* - [arroots](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMAResults.arroots.html)
  - (arreglo) raíces del polinomio desfasado autorregresivo de forma reducida.
* - [bic](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMAResults.bic.html)
  - (flotante) Criterio de información de Bayes.
* - [bse](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMAResults.bse.html)
  - Los errores estándar de las estimaciones de parámetros.
* - [cov_params_approx](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMAResults.cov_params_approx.html)
  - (arreglo) La matriz de varianza / covarianza.
* - [cov_params_oim](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMAResults.cov_params_oim.html)
  - (arreglo) La matriz de varianza / covarianza.
* - [cov_params_opg](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMAResults.cov_params_opg.html)
  - (arreglo) La matriz de varianza / covarianza.
* - [cov_params_robust](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMAResults.cov_params_robust.html)
  - (arreglo) La matriz de varianza / covarianza QMLE.
* - [cov_params_robust_approx](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMAResults.cov_params_robust_approx.html)
  - (arreglo) La matriz de varianza / covarianza QMLE.
* - [cov_params_robust_oim](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMAResults.cov_params_robust_oim.html)
  - (arreglo) La matriz de varianza / covarianza QMLE.
* - [fittedvalues](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMAResults.fittedvalues.html)
  - (arreglo) Los valores predichos del modelo.
* - [hqic](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMAResults.hqic.html)
  - (flotante) Criterio de información de Hannan-Quinn.
* - [llf](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMAResults.llf.html)
  - (Flotación) El valor de la función Log-Likelilidad evaluada en los parámetros.
* - [llf_obs](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMAResults.llf_obs.html)
  - (Flotación) El valor de la función Log-Likelilidad evaluada en los parámetros.
* - [loglikelihood_burn](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMAResults.loglikelihood_burn.html)
  - (flotante) El número de observaciones durante las cuales no se evalúa la probabilidad.
* - [mae](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMAResults.mae.html)
  - (flotante) Error absoluto medio.
* - [mafreq](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMAResults.mafreq.html)
  - (arreglo) frecuencia de las raíces de la forma reducida del promedio móvil polinomio.
* - [maparams](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMAResults.maparams.html)
  - (arreglo) Parámetros de promedio móvil realmente estimados en el modelo.
* - [maroots](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMAResults.maroots.html)
  - (arreglo) Raíces del polinomio de retraso de promedio móvil de forma móvil reducida.
* - [mse](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMAResults.mse.html)
  - (flotante) Error cuadrado medio.
* - [pvalues](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMAResults.pvalues.html)
  - (arreglo) Los valores p asociados con las estadísticas z de los coeficientes.
* - [resid](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMAResults.resid.html)
  - (arreglo) Los residuales del modelo.
* - [seasonalarparams](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMAResults.seasonalarparams.html)
  - (arreglo) Parámetros autorregresivos estacionales realmente estimados en el modelo.
* - [seasonalmaparams](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMAResults.seasonalmaparams.html)
  - (arreglo) Parámetros de promedio móvil estacional realmente estimados en el modelo.
* - [sse](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMAResults.sse.html)
  - (flotante) Suma de errores al cuadrado.
* - [states](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMAResults.states.html)
  - .
* - [tvalues](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMAResults.tvalues.html)
  - Retorna la estadística T para una estimación de parámetros dada.
* - [use_t](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMAResults.use_t.html)
  - Indica si usar la distribución del estudiante en inferencia.
* - [zvalues](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMAResults.zvalues.html)
  - (arreglo) Las estadísticas z para los coeficientes.
```

<br/>

### Método

Métodos de la clase `ArimaResults`/`SARIMAXResults`.

:::{note}
Los links de esta sección llevan a la documentación de `ArimaResults`. Para más información de `SARIMAXResults` consultar la [documentación](https://www.statsmodels.org/stable/generated/statsmodels.tsa.statespace.sarimax.SARIMAXResults.html).
:::

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [append](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMAResults.append.html)(endog[,  exog,  refit,  fit_kwargs])
  - Recrea el objeto de resultados con nuevos datos adjuntos a los datos originales.
* - [apply](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMAResults.apply.html)(endog[,  exog,  refit,  fit_kwargs,  ...])
  - Aplica los parámetros ajustados a nuevos datos no relacionados con los datos originales.
* - [conf_int](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMAResults.conf_int.html)([alpha,  cols])
  - Construye un intervalo de confianza para los parámetros ajustados.
* - [cov_params](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMAResults.cov_params.html)([r_matrix,  column,  scale,  cov_p,  ...])
  - Calcula la matriz de varianza/covarianza.
* - [extend](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMAResults.extend.html)(endog[,  exog])
  - Recrea el objeto de resultados para nuevos datos que extiendan los datos originales.
* - [f_test](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMAResults.f_test.html)(r_matrix[,  cov_p,  invcov])
  - Calcula la prueba F para una hipótesis lineal articular.
* - [forecast](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMAResults.forecast.html)([steps,  signal_only])
  - Pronósticos fuera de la muestra.
* - [get_forecast](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMAResults.get_forecast.html)([steps,  signal_only])
  - Pronósticos fuera de la muestra e intervalos de predicción.
* - [get_prediction](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMAResults.get_prediction.html)([start,  end,  dynamic,  ...])
  - Predicción en la muestra y pronóstico fuera de la muestra.
* - [get_smoothed_decomposition](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMAResults.get_smoothed_decomposition.html)([...])
  - Descompone la salida suavizada en las contribuciones de las observaciones.
* - [impulse_responses](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMAResults.impulse_responses.html)([steps,  impulse,  ...])
  - Función de respuesta de impulso.
* - [info_criteria](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMAResults.info_criteria.html)(criteria[,  method])
  - Criterios de información.
* - [initialize](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMAResults.initialize.html)(model,  params,  **kwargs)
  - Inicializa (posiblemente reinicializar) una instancia de resultados.
* - [load](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMAResults.load.html)(fname)
  - Cargue una instancia de resultados en _pickle_.
* - [news](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMAResults.news.html)(comparison[,  impact_date,  ...])
  - Calcula los impactos de los datos actualizados (noticias y revisiones).
* - [normalized_cov_params](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMAResults.normalized_cov_params.html)()
  - Ver documento de clase de modelo específico.
* - [plot_diagnostics](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMAResults.plot_diagnostics.html)([variable,  lags,  fig,  ...])
  - Gráficos de diagnóstico para residuos estandarizados de una variable endógena.
* - [predict](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMAResults.predict.html)([start,  end,  dynamic,  ...])
  - Predicción en la muestra y pronóstico fuera de la muestra.
* - [remove_data](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMAResults.remove_data.html)()
  - Elimina las matrices de datos, todas las matrices de observaciones del resultado y el modelo.
* - [save](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMAResults.save.html)(fname[,  remove_data])
  - Guarda un _pickle_ de esta instancia.
* - [simulate](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMAResults.simulate.html)(nsimulations[,  measurement_shocks,  ...])
  - Simula una nueva serie de tiempo siguiendo el modelo de espacio estatal.
* - [summary](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMAResults.summary.html)([alpha,  start])
  - Resumen el modelo.
* - [t_test](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMAResults.t_test.html)(r_matrix[,  cov_p,  use_t])
  - Calcula una prueba t para cada hipótesis lineal de la forma `Rb = q`.
* - [t_test_pairwise](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMAResults.t_test_pairwise.html)(term_name[,  method,  alpha,  ...])
  - Realiza _t_test_ por pares con valores p corregidos por pruebas múltiples.
* - [test_heteroskedasticity](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMAResults.test_heteroskedasticity.html)(method[,  ...])
  - Prueba de heterocedasticidad de residuos estandarizados.
* - [test_normality](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMAResults.test_normality.html)(method)
  - Prueba de normalidad de residuos estandarizados.
* - [test_serial_correlation](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMAResults.test_serial_correlation.html)(method[,  df_adjust,  ...])
  - Prueba Ljung-Box para ninguna correlación en serie de residuos estandarizados.
* - [wald_test](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMAResults.wald_test.html)(r_matrix[,  cov_p,  invcov,  use_f,  ...])
  - Calcula una prueba Wald para una hipótesis lineal articular.
* - [wald_test_terms](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMAResults.wald_test_terms.html)([skip_single,  ...])
  - Calcula una secuencia de pruebas de Wald para términos en múltiples columnas.
```

### Notas de _get_forecast_

[get_forecast](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMAResults.get_forecast.html): Predicciones _out-sample_ e intevalos de predicción.
```python
# Sintaxis de llamada
X.get_forecast(steps=1, signal_only=False, **kwargs)
```
- **Parámetros:**
    - **X** - `SARIMAXresults`/`ArimaResults`: Resultado del modelo SARIMA creado con `SARIMA.fit` o `ARIMA.fit()`.
	- **steps** - `int`, `str` o `datetime`: Si es un entero, el número de pasos a pronosticar desde el final de la muestra. También puede ser una cadena de fecha para analizar o un tipo de fecha y hora. Sin embargo, si el índice de fechas no tiene una frecuencia fija, los pasos deben ser un entero. El valor predeterminado es 1.
- **Retorna:**
    - [PredictionResults](https://www.statsmodels.org/stable/generated/statsmodels.regression.linear_model.PredictionResults.html#statsmodels.regression.linear_model.PredictionResults).

<br>

### Notas de _get_prediction_

[get_prediction](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMAResults.get_prediction.html): Realiza predicciones dentro de la muestra (_in-sample_) y forecasting fuera de la muestra (_out-sample_).
```python
# Sintaxis de llamada
X.get_prediction(start=None, end=None, dynamic=False, information_set='predicted', 
                 signal_only=False, index=None, exog=None, extend_model=None, 
                 extend_kwargs=None, **kwargs)
```
- **Parámetros:**
    - **X** - `SARIMAXresults`/`ArimaResults`: Resultado del modelo SARIMA creado con `SARIMA.fit` o `ARIMA.fit()`.
    - **start**, **end** - `int`, `str` o `datetime`: Número de la observación (indexación comienza en cero) en la cual empezar y terminar el forecasting respectivamente. Pueden ser numeros negativos, para indexar desde el final. También puede ser una cadena con la fecha (formato _YYYY-MM-DD_ o partes de ésta en orden, es decir solo año o solo año y mes) o una fecha. Si el forecasting es _in-sample_ el número debe ser menor al número de observaciones en la serie de tiempo. Si el forecasting será _out-sample_ el número debe ser mayor al número de observaciones en la serie de tiempo.
	- **dynamic** - `bool`, `str`, `int` o `datetime`: Desplazamiento con respecto al comienzo para hacer una predicción dinámica, esto es que se utilizan los valores predichos anterioremente para hacer las predicciones, en caso contrario se utilizan los valores verdaderos.
- **Retorna:**
    - [PredictionResults](https://www.statsmodels.org/stable/generated/statsmodels.regression.linear_model.PredictionResults.html#statsmodels.regression.linear_model.PredictionResults).

<br>

### Notas de _plot_diagnostics_

[plot_diagnostics](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMAResults.plot_diagnostics.html): Gráficos de diagnóstico para residuos estandarizados de una variable endógena.
```python
# Sintaxis de llamada
X.plot_diagnostics(variable=0, lags=10, fig=None, figsize=None, truncate_endog_names=24,
                   auto_ylims=False, bartlett_confint=False, acf_kwargs=None)
```
- **Parámetros:**
    - **X** - `ARIMAresults`: Resultado del modelo SARIMAX creado con `SARIMAX.fit`.
- **Retorna:**
    - `Figure`.
 
**Ejemplo**

```python
# Crear y ajustar el modelo
model = SARIMAX(df, order=(p, d, q))
results=model.fit()

# Graficar diagnóstico
results.plot_diagnostics()
plt.show()
```

<br><br>

<br/>

(others-DecomposeResult)=
## DecomposeResult

Es la clase retorna por la función `seasonal_decompose()`. Representa una descomposición de una serie estacional usando medias móviles.

:::{note}
Para más información consultar la [documentación](https://www.statsmodels.org/stable/generated/statsmodels.tsa.seasonal.DecomposeResult.html#statsmodels.tsa.seasonal.DecomposeResult) de _statsmodels_.
:::

<br/>

### Propiedades

Métodos de la clase `DecomposeResult`. 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [nobs](https://www.statsmodels.org/stable/generated/statsmodels.tsa.seasonal.DecomposeResult.nobs.html)
  - Número de observaciones.
* - [observed](https://www.statsmodels.org/stable/generated/statsmodels.tsa.seasonal.DecomposeResult.observed.html)
  - Datos observados.
* - [resid](https://www.statsmodels.org/stable/generated/statsmodels.tsa.seasonal.DecomposeResult.resid.html)
  - Los residuos estimados.
* - [seasonal](https://www.statsmodels.org/stable/generated/statsmodels.tsa.seasonal.DecomposeResult.seasonal.html)
  - El componente estacional estimado.
* - [trend](https://www.statsmodels.org/stable/generated/statsmodels.tsa.seasonal.DecomposeResult.trend.html)
  - El componente de tendencia estimado.
* - [weights](https://www.statsmodels.org/stable/generated/statsmodels.tsa.seasonal.DecomposeResult.weights.html)
  - Los pesos utilizados en la estimación robusta.
```

### Método

Métodos de la clase `DecomposeResult`. 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [plot](https://www.statsmodels.org/stable/generated/statsmodels.tsa.seasonal.DecomposeResult.plot.html)([observed,  seasonal,  trend,  resid,  weights])
  - Grafica componentes estimados.
```