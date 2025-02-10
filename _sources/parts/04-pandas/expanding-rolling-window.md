---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---


# _Expanding, Rolling_ y _Window_

Los objetos `Rolling`, `Expanding`, `Window` y `ExponentialMovingWindow` son retornados por llamadas a métodos concretos de `Series` y `DataFrame`, a continuación se resumen los objetos y los métodos que los retornan.
- `Rolling`:
    - Provee de una ventana móvil de tamaño fijo para cálculo de estadísticas móviles.
    - Retornado por: `pandas.DataFrame.rolling()` y `pandas.Series.rolling()`.
- `Expanding`:
    - Provee de una ventana expansiva, partiendo de un primer dato, útil para cálculos acumulados.
    - Retornado por:`pandas.DataFrame.expanding()` y `pandas.Series.expanding()`.
- `ExponentialMovingWindow`:
    - Calcula estadísticas móviles ponderadas exponencialmente utilizando factores de decaímento.
    - Retornado por: `pandas.DataFrame.ewm()` y `pandas.Series.ewm()`.
- `Window`:
    - Objeto generalizado de ventana, que comibina ventanas móviles y expansivas, útil para operaciones personalizadas.
    - Para retornar una instancia de `Window` as necesario definir el argumento `type_win` en el método `.rolling()` de `Series` o `DataFrame`.

En esta sección únicamente se enlistaran los métodos de estos objetos.

---
## Métodos de _Expanding_

Métodos del objeto `Expanding`.

```{list-table}
:header-rows: 1
:name: pandas-expanding-methods

* - Método
  - Descripción
* - [Expanding.aggregate](https://pandas.pydata.org/docs/reference/api/pandas.core.window.expanding.Expanding.aggregate.html)(func, *args, **kwargs)
  - Calcula _aggregates_ usando una o más operaciones sobre el eje especificado.
* - [Expanding.apply](https://pandas.pydata.org/docs/reference/api/pandas.core.window.expanding.Expanding.apply.html)(func[, raw, engine, ...])
  - Calcula la función de agregación personalizada en expansión.
* - [Expanding.corr](https://pandas.pydata.org/docs/reference/api/pandas.core.window.expanding.Expanding.corr.html)([other, pairwise, ddof, ...])
  - Calcula la correlación en expansión.
* - [Expanding.count](https://pandas.pydata.org/docs/reference/api/pandas.core.window.expanding.Expanding.count.html)([numeric_only])
  - Calcula el recuento en expansión de observaciones que no son de `NaN`.
* - [Expanding.cov](https://pandas.pydata.org/docs/reference/api/pandas.core.window.expanding.Expanding.cov.html)([other, pairwise, ddof, ...])
  - Calcula la covarianza muestral en expansión.
* - [Expanding.kurt](https://pandas.pydata.org/docs/reference/api/pandas.core.window.expanding.Expanding.kurt.html)([numeric_only])
  - Calcula la curtosis en expansión.
* - [Expanding.max](https://pandas.pydata.org/docs/reference/api/pandas.core.window.expanding.Expanding.max.html)([numeric_only, engine, ...])
  - Calcula el máximo en expansión.
* - [Expanding.mean](https://pandas.pydata.org/docs/reference/api/pandas.core.window.expanding.Expanding.mean.html)([numeric_only, engine, ...])
  - Calcula la media en expansión.
* - [Expanding.median](https://pandas.pydata.org/docs/reference/api/pandas.core.window.expanding.Expanding.median.html)([numeric_only, engine, ...])
  - Calcula la mediana en expansión.
* - [Expanding.min](https://pandas.pydata.org/docs/reference/api/pandas.core.window.expanding.Expanding.min.html)([numeric_only, engine, ...])
  - Calcula el mínimo en expansión.
* - [Expanding.quantile](https://pandas.pydata.org/docs/reference/api/pandas.core.window.expanding.Expanding.quantile.html)(q[, interpolation, ...])
  - Calcula el cuantil en expansión.
* - [Expanding.rank](https://pandas.pydata.org/docs/reference/api/pandas.core.window.expanding.Expanding.rank.html)([method, ascending, pct, ...])
  - Calcula el ranking en expansión.
* - [Expanding.sem](https://pandas.pydata.org/docs/reference/api/pandas.core.window.expanding.Expanding.sem.html)([ddof, numeric_only])
  - Calcula el error estándar de la media en expansión.
* - [Expanding.skew](https://pandas.pydata.org/docs/reference/api/pandas.core.window.expanding.Expanding.skew.html)([numeric_only])
  - Calcula el sesgo en expansión.
* - [Expanding.std](https://pandas.pydata.org/docs/reference/api/pandas.core.window.expanding.Expanding.std.html)([ddof, numeric_only, engine, ...])
  - Calcula la desviación estándar en expansión.
* - [Expanding.sum](https://pandas.pydata.org/docs/reference/api/pandas.core.window.expanding.Expanding.sum.html)([numeric_only, engine, ...])
  - Calcula la suma en expansión.
* - [Expanding.var](https://pandas.pydata.org/docs/reference/api/pandas.core.window.expanding.Expanding.var.html)([ddof, numeric_only, engine, ...])
  - Calcula la varianza en expansión.
```

<br>

## Métodos de _ExponentialMovingWindow_

Métodos del objeto `ExponentialMovingWindow`.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [ExponentialMovingWindow.corr](https://pandas.pydata.org/docs/reference/api/pandas.core.window.ewm.ExponentialMovingWindow.corr.html)([other, ...])
  - Calcula la correlación muestral ewm (momento ponderado exponencial).
* - [ExponentialMovingWindow.cov](https://pandas.pydata.org/docs/reference/api/pandas.core.window.ewm.ExponentialMovingWindow.cov.html)([other, ...])
  - Calcula la covarianza muestral ewm (momento ponderado exponencial).
* - [ExponentialMovingWindow.mean](https://pandas.pydata.org/docs/reference/api/pandas.core.window.ewm.ExponentialMovingWindow.mean.html)([numeric_only, ...])
  - Calcula la media ewm (momento ponderado exponencial).
* - [ExponentialMovingWindow.std](https://pandas.pydata.org/docs/reference/api/pandas.core.window.ewm.ExponentialMovingWindow.std.html)([bias, numeric_only])
  - Calcula la desviación estándar ewm (momento ponderado exponencial).
* - [ExponentialMovingWindow.sum](https://pandas.pydata.org/docs/reference/api/pandas.core.window.ewm.ExponentialMovingWindow.sum.html)([numeric_only, ...])
  - Calcula la suma ewm (momento ponderado exponencial).
* - [ExponentialMovingWindow.var](https://pandas.pydata.org/docs/reference/api/pandas.core.window.ewm.ExponentialMovingWindow.var.html)([bias, numeric_only])
  - Calcula la varianza ewm (momento ponderado exponencial).
```

<br>

---
## Métodos de _Rolling_

Métodos del objeto `Rolling`.

```{list-table}
:header-rows: 1
:name: pandas-rolling-methods

* - Método
  - Descripción
* - [Rolling.aggregate](https://pandas.pydata.org/docs/reference/api/pandas.core.window.rolling.Rolling.aggregate.html)(func, *args, **kwargs)
  - Calcula un _aggregate_ usando una o más operaciones sobre el eje especificado.
* - [Rolling.apply](https://pandas.pydata.org/docs/reference/api/pandas.core.window.rolling.Rolling.apply.html)(func[, raw, engine, ...])
  - Calcula la función de agregación personalizada móvil.
* - [Rolling.corr](https://pandas.pydata.org/docs/reference/api/pandas.core.window.rolling.Rolling.corr.html)([other, pairwise, ddof, ...])
  - Calcula la correlación móvil.
* - [Rolling.count](https://pandas.pydata.org/docs/reference/api/pandas.core.window.rolling.Rolling.count.html)([numeric_only])
  - Calcula el recuento móvil de observaciones que no son de `NaN`.
* - [Rolling.cov](https://pandas.pydata.org/docs/reference/api/pandas.core.window.rolling.Rolling.cov.html)([other, pairwise, ddof, ...])
  - Calcula la covarianza de la muestra móvil.
* - [Rolling.kurt](https://pandas.pydata.org/docs/reference/api/pandas.core.window.rolling.Rolling.kurt.html)([numeric_only])
  - Calcula lacurtosis  móvil.
* - [Rolling.max](https://pandas.pydata.org/docs/reference/api/pandas.core.window.rolling.Rolling.max.html)([numeric_only, engine, ...])
  - Calcula el máximo móvil.
* - [Rolling.mean](https://pandas.pydata.org/docs/reference/api/pandas.core.window.rolling.Rolling.mean.html)([numeric_only, engine, ...])
  - Calcula la media móvil.
* - [Rolling.median](https://pandas.pydata.org/docs/reference/api/pandas.core.window.rolling.Rolling.median.html)([numeric_only, engine, ...])
  - Calcula la mediana móvil.
* - [Rolling.min](https://pandas.pydata.org/docs/reference/api/pandas.core.window.rolling.Rolling.min.html)([numeric_only, engine, ...])
  - Calcula el mínimo móvil.
* - [Rolling.quantile](https://pandas.pydata.org/docs/reference/api/pandas.core.window.rolling.Rolling.quantile.html)(q[, interpolation, ...])
  - Calcula el cuantil móvil.
* - [Rolling.rank](https://pandas.pydata.org/docs/reference/api/pandas.core.window.rolling.Rolling.rank.html)([method, ascending, pct, ...])
  - Calcula el ranking móvil.
* - [Rolling.sem](https://pandas.pydata.org/docs/reference/api/pandas.core.window.rolling.Rolling.sem.html)([ddof, numeric_only])
  - Calcula el error estándar de la medi amóvil.
* - [Rolling.skew](https://pandas.pydata.org/docs/reference/api/pandas.core.window.rolling.Rolling.skew.html)([numeric_only])
  - Calcula el sesgo móvil.
* - [Rolling.std](https://pandas.pydata.org/docs/reference/api/pandas.core.window.rolling.Rolling.std.html)([ddof, numeric_only, engine, ...])
  - Calcula la desviación estándar móvil.
* - [Rolling.sum](https://pandas.pydata.org/docs/reference/api/pandas.core.window.rolling.Rolling.sum.html)([numeric_only, engine, ...])
  - Calcula la suma móvil.
* - [Rolling.var](https://pandas.pydata.org/docs/reference/api/pandas.core.window.rolling.Rolling.var.html)([ddof, numeric_only, engine, ...])
  - Calcula la varianza móvil.
```

<br>

---
## Métodos de _Window_

Métodos del objeto `Window`.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [Window.mean](https://pandas.pydata.org/docs/reference/api/pandas.core.window.rolling.Window.mean.html)([numeric_only])
  - Calcula la media de la ventana móvil ponderada.
* - [Window.std](https://pandas.pydata.org/docs/reference/api/pandas.core.window.rolling.Window.std.html)([ddof, numeric_only])
  - Calcula la desviación estándar de la ventana móvil ponderada.
* - [Window.sum](https://pandas.pydata.org/docs/reference/api/pandas.core.window.rolling.Window.sum.html)([numeric_only])
  - Calcula la suma de la ventana móvil ponderada.
* - [Window.var](https://pandas.pydata.org/docs/reference/api/pandas.core.window.rolling.Window.var.html)([ddof, numeric_only])
  - Calcula la varianza de la ventana móvil ponderada.
```