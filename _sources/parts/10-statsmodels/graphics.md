# Gráficos

Proporciona herramientas para visualización de datos y diagnósticos de modelos. Entre las principales funcionalidades están:
- Gráficos de diagnóstico de residuos.
- Visualización de autocorrelación y autocorrelación parcial.
- Gráficos de regresión parcial y componentes aditivos.

Es necesario importar el módulo:

```python
# Importar api
import statsmodels.graphics as sm

# Importar función específica
from statsmodels.graphics import func_name
```
- _sm_ es el nombre por convención.
- _func_name_ es el nombre de la función.

:::{warning}
Algunas funciones forman parte de submódulos dentro de _graphics_, por los que al importarlos es necesario especificar esos submódulos. Para revisar la manera de importarlos revisar la documentación de cada función.

Para más información visitar la [documentación](https://www.statsmodels.org/stable/graphics.html) de _statsmodels_.
:::

:::{caution}
Para poder visualizar los gráficos es necesario usar la función `plt.show()` de _matplotlib.pyplot_.
:::

<br/>

## Boxplots

Visualización de la distribución de datos mediante diagramas de caja, útiles para identificar valores atípicos y comparar grupos.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [beanplot](https://www.statsmodels.org/stable/generated/statsmodels.graphics.boxplots.beanplot.html)(data, ...)
  - Gráfico de frijoles de cada conjunto de datos en una secuencia.
* - [violinplot](https://www.statsmodels.org/stable/generated/statsmodels.graphics.boxplots.violinplot.html)(data, ...)
  - Hace una gráfica de violín de cada conjunto de datos en la secuencia de datos.
```

<br/>

## Correlación

Representación gráfica de la correlación entre variables, como matrices de correlación o gráficos de dispersión.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [plot_corr](https://www.statsmodels.org/stable/generated/statsmodels.graphics.correlation.plot_corr.html)(dcorr, ...)
  - La correlación de muchas variables en una cuadrícula de color.
* - [plot_corr_grid](https://www.statsmodels.org/stable/generated/statsmodels.graphics.correlation.plot_corr_grid.html)(dcorrs, ...)
  - Crea una cuadrícula de gráficas de correlación.
* - [scatter_ellipse](https://www.statsmodels.org/stable/generated/statsmodels.graphics.plot_grids.scatter_ellipse.html)(data, ...)
  - Crea una cuadrícula de gráficos de dispersión con elipses de confianza.
```

<br/>

## Dot Plots

Visualización de datos categóricos o discretos mediante puntos, ideal para comparar frecuencias o proporciones.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [dot_plot](https://www.statsmodels.org/stable/generated/statsmodels.graphics.dotplots.dot_plot.html)(points, ...)
  - Graficado de puntos (también conocido como bosque y _blobbogram_).
```

<br/>

## Functional Plots

Gráficos para explorar relaciones funcionales entre variables, como gráficos de regresión parcial o componentes aditivos.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [banddepth](https://www.statsmodels.org/stable/generated/statsmodels.graphics.functional.banddepth.html)(data, ...)
  - Calcula la profundidad de la banda para un conjunto de curvas funcionales.
* - [fboxplot](https://www.statsmodels.org/stable/generated/statsmodels.graphics.functional.fboxplot.html)(data, ...)
  - Crea un boxplot funcional.
* - [hdrboxplot](https://www.statsmodels.org/stable/generated/statsmodels.graphics.functional.hdrboxplot.html)(data, ...)
  - Boxplot de región de alta densidad.
* - [rainbowplot](https://www.statsmodels.org/stable/generated/statsmodels.graphics.functional.rainbowplot.html)(data, ...)
  - Crea un _rainbow plot_ para un conjunto de curvas.
```

<br/>

## Bondad de Ajuste

Herramientas para evaluar la calidad del ajuste de un modelo, como gráficos de residuos o _Q-Q_ plots.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [ProbPlot](https://www.statsmodels.org/stable/generated/statsmodels.graphics.gofplots.ProbPlot.html)(data, ...)
  - Gráficos de probabilidad _Q-Q_ y _P-P_.
* - [qqline](https://www.statsmodels.org/stable/generated/statsmodels.graphics.gofplots.qqline.html)(ax, line, ...)
  - Grafica una línea de referencia para un _qqplot_.
* - [qqplot](https://www.statsmodels.org/stable/generated/statsmodels.graphics.gofplots.qqplot.html)(data, ...)
  - Gráfico _Q-Q_ de los cuantiles de _x_ versus los cuantiles/ppf de una distribución.
* - [qqplot_2samples](https://www.statsmodels.org/stable/generated/statsmodels.graphics.gofplots.qqplot_2samples.html)(data1, data2, ...)
  - Gráfico _Q-Q_ de cuantiles de dos muestras.
```

<br/>

## Regresión

Visualización de resultados de modelos de regresión, como gráficos de predicción vs. observación o gráficos de influencia.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [abline_plot](https://www.statsmodels.org/stable/generated/statsmodels.graphics.regressionplots.abline_plot.html)(...)
  - Grafica una línea dada una intersección y pendiente.
* - [influence_plot](https://www.statsmodels.org/stable/generated/statsmodels.graphics.regressionplots.influence_plot.html)(results, ...)
  - Gráfica de la influencia en la regresión.
* - [plot_ccpr](https://www.statsmodels.org/stable/generated/statsmodels.graphics.regressionplots.plot_ccpr.html)(results, exog_idx, ...)
  - Grafica CCPR contra un regresor.
* - [plot_ccpr_grid](https://www.statsmodels.org/stable/generated/statsmodels.graphics.regressionplots.plot_ccpr_grid.html)(results, ...)
  - Genera gráficos de CCPR contra un conjunto de regresores, traza en una cuadrícula.
* - [plot_ceres_residuals](https://www.statsmodels.org/stable/generated/statsmodels.graphics.regressionplots.plot_ceres_residuals.html)(results, focus_exog, ...)
  - Grafica _Conditional Expectation Partial Residuals (CERES)_
* - [plot_fit](https://www.statsmodels.org/stable/generated/statsmodels.graphics.regressionplots.plot_fit.html)(results, exog_idx, ...)
  - Grafica el ajusta contra un regresor.
* - [plot_leverage_resid2](https://www.statsmodels.org/stable/generated/statsmodels.graphics.regressionplots.plot_leverage_resid2.html)(results, ...)
  - Grafica _leverage statistics vs._
* - [plot_partregress](https://www.statsmodels.org/stable/generated/statsmodels.graphics.regressionplots.plot_partregress.html)(endog, exog_i, exog_others)
  - Grafica regresión parcial para un solo regresor.
* - [plot_partregress_grid](https://www.statsmodels.org/stable/generated/statsmodels.graphics.regressionplots.plot_partregress_grid.html)(results, ...)
  - Grafica regresión parcial para un conjunto de regresores.
* - [plot_regress_exog](https://www.statsmodels.org/stable/generated/statsmodels.graphics.regressionplots.plot_regress_exog.html)(results, exog_idx, ...)
  - Grafica los resultados de la regresión contra un regresor.
```

<br/>

## Series de Tiempo

Representación gráfica de patrones en series temporales, como autocorrelación, descomposición y tendencias. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [month_plot](https://www.statsmodels.org/stable/generated/statsmodels.graphics.tsaplots.month_plot.html)(x, ...)
  - Grafica estacional de datos mensuales.
* - [plot_accf_grid](https://www.statsmodels.org/stable/generated/statsmodels.graphics.tsaplots.plot_accf_grid.html)(x, ...)
  - Gráfica una malla _auto/cross-correlation_.
* - [plot_acf](https://www.statsmodels.org/stable/generated/statsmodels.graphics.tsaplots.plot_acf.html)(x, ...)
  - Grafica la función de autocorrelación.
* - [plot_ccf](https://www.statsmodels.org/stable/generated/statsmodels.graphics.tsaplots.plot_ccf.html)(x, y, ...)
  - Grafica la función de correlación cruzada.
* - [plot_pacf](https://www.statsmodels.org/stable/generated/statsmodels.graphics.tsaplots.plot_pacf.html)(x, ...)
  - Grafica la función de autocorrelación parcial.
* - [quarter_plot](https://www.statsmodels.org/stable/generated/statsmodels.graphics.tsaplots.quarter_plot.html)(x, ...)
  - Grafica estacional de datos trimestrales.
```

<br/>

### Notas de _plot_acf_

[plot_acf](https://www.statsmodels.org/stable/generated/statsmodels.graphics.tsaplots.plot_acf.html): Grafica la función de autocorrelación.
```python
# Sintaxis de llamada
plot_acf(x, ax=None, lags=None, *, alpha=0.05, use_vlines=True, adjusted=False, fft=False, 
         missing='none', title='Autocorrelation', zero=True, auto_ylims=False, 
         bartlett_confint=True, vlines_kwargs=None, **kwargs)
```
**Parámetros:**
- **x** - `array-like`: Arreglo de valores de la serie de tiempo.
- **lags** - `int` o `array-like`: Número de _lags_ (desfases) en la autocorrelación o los desfases en los que se quiere calcular la autocorrelación.
- **alpha** - `scalar`: Para indicar que se calcule el (_1 - alpha_) intervalos de confianza. IMPORTANTE: Para no mostar el intervalor establecer `alpha = 1`.
- **zero** - `bool`: Para indicar si incluir el desfase cero.

**Uso**:

```python
# Importación
from statsmodels.graphics.tsaplots import plot_acf

# Uso básico
plot_acf(x, lags, alpha) 
```


<br/>

### Notas de _plot_pacf_

[plot_pacf](https://www.statsmodels.org/stable/generated/statsmodels.graphics.tsaplots.plot_pacf.html): Grafica la función de autocorrelación parcial.
```python
# Sintaxis de llamada
plot_pacf(x, ax=None, lags=None, alpha=0.05, method='ywm', use_vlines=True, 
          title='Partial Autocorrelation', zero=True, vlines_kwargs=None, **kwargs)
```
**Parámetros:**
- **x** - `array-like`: Arreglo de valores de la serie de tiempo.
- **lags** - `int` o `array-like`: Número de _lags_ (desfases) en la autocorrelación o los desfases en los que se quiere calcular la autocorrelación parcial.
- **alpha** - `scalar`: Para indicar que se calcule el (_1 - alpha_) intervalos de confianza. IMPORTANTE: Para no mostar el intervalor establecer `alpha = 1`.
- **zero** - `bool`: Para indicar si incluir el desfase cero.

**Uso**:

```python
# Importación
from statsmodels.graphics.tsaplots import plot_pacf

# Uso básico
plot_pacf(x, lags, alpha) 
```