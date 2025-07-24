# transform

Este módulo contiene funciones auxiliares para aplicar cálculos del lado del cliente, como transformaciones a campos de datos o expresiones `ColumnDataSource`. Ofrece funciones para aplicar transformaciones a datos, como _jitter_, _factor cmap_ y _linear cmap_.

```python
# importar librería
from bokeh.transform import function_name
```
- _func_name_ es el nombre de la función.

:::{note}
Para más información de este módulo visitar la [documentación](https://docs.bokeh.org/en/latest/docs/reference/transform.html) de `bokeh`.
:::

## Funciones

Funciones implementadas en `bokeh.transform` . 

```{list-table}
:header-rows: 1

* - function
  - Descripción
* - [cumsum](https://docs.bokeh.org/en/latest/docs/reference/transform.html#bokeh.transform.cumsum)(field_name: str, ...)
  - Crea un `dict` de `DataSpec` para generar una expresión de `CumSum` para una `ColumnDataSource`.
* - [dodge](https://docs.bokeh.org/en/latest/docs/reference/transform.html#bokeh.transform.dodge)(field_name: str,  value: float, ...)
  - Crea un `dict` de `DataSpec` que aplica una transformación `Dodge` del lado del cliente a una columna `ColumnDataSource`.
* - [eqhist_cmap](https://docs.bokeh.org/en/latest/docs/reference/transform.html#bokeh.transform.eqhist_cmap)(field_name: str, ...)
  - Crea un `dict` de `DataSpec` que aplica una transformación `EqHistColorMapper` del lado del cliente en una columna `ColumnDataSource`.
* - [factor_cmap](https://docs.bokeh.org/en/latest/docs/reference/transform.html#bokeh.transform.factor_cmap)(field_name: str, ...)
  - Crea un `dict` de `DataSpec` que aplica una transformación `CategoricalColorMapper` del lado del cliente a una columna `ColumnDataSource`. Mapea valores de una coluna categórica a colores.
* - [factor_hatch](https://docs.bokeh.org/en/latest/docs/reference/transform.html#bokeh.transform.factor_hatch)(field_name: str, ...)
  - Crea un `dict` de `DataSpec` que aplica una transformación `CategoricalPatternMapper` del lado del cliente en una columna `ColumnDataSource`.
* - [factor_mark](https://docs.bokeh.org/en/latest/docs/reference/transform.html#bokeh.transform.factor_mark)(field_name: str, ...)
  - Crea un `dict` de `DataSpec` que aplica una transformación `CategoricalMarkerMapper` del lado del cliente en una columna `ColumnDataSource`.
* - [jitter](https://docs.bokeh.org/en/latest/docs/reference/transform.html#bokeh.transform.jitter)(field_name: str,  width: float, ...)
  - Crea un `dict` de `DataSpec` que aplica una transformación de `Jitter` del lado del cliente a una columna de `ColumnDataSource`.
* - [linear_cmap](https://docs.bokeh.org/en/latest/docs/reference/transform.html#bokeh.transform.linear_cmap)(field_name: str, ...)
  - Crea un `dict` de `DataSpec` que aplica una transformación `LinearColorMapper` del lado del cliente en una columna `ColumnDataSource`. Mapea valores de una coluna a colores de manera continua.
* - [log_cmap](https://docs.bokeh.org/en/latest/docs/reference/transform.html#bokeh.transform.log_cmap)(field_name: str, ...)
  - Crea un `dict` de `DataSpec` que aplica una transformación `LogColorMapper` del lado del cliente en una columna de `ColumnDataSource`.
* - [stack](https://docs.bokeh.org/en/latest/docs/reference/transform.html#bokeh.transform.stack)(*fields: str)
  - Crea un Crea un `dict` de `DataSpec` para generar una expresión `Stack` para una `ColumnDataSource`.
* - [transform](https://docs.bokeh.org/en/latest/docs/reference/transform.html#bokeh.transform.transform)(field_name: str, ...)
  - Crea un `dict` de `DataSpec` que aplica una transformación `Transform` arbitraria del lado del cliente a una columna `ColumnDataSource`.
```

<br/>

