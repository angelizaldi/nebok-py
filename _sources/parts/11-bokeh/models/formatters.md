# _Formatters_

Proporciona herramientas para dar formato y personalizar la visualización de datos en gráficos, como el formato de números, fechas y categorías en ejes y _tooltips_.

:::{note}
Para más información de esta sección visitar la [documentación](https://docs.bokeh.org/en/latest/docs/reference/models/formatters.html) de `bokeh`.
:::


## Clases

Clases implementadas en el módulo _models_ del tipo _formatters_. 

```{list-table}
:header-rows: 1

* - Constructor
  - Descripción
* - [BasicTickFormatter](https://docs.bokeh.org/en/latest/docs/reference/models/formatters.html#bokeh.models.BasicTickFormatter)(*args: Any,  id: ID | None = None, ...)
  - Muestra los valores de los _ticks_ de rangos continuos como "números básicos", utilizando notación científica cuando sea apropiado de forma predeterminada.
* - [CategoricalTickFormatter](https://docs.bokeh.org/en/latest/docs/reference/models/formatters.html#bokeh.models.CategoricalTickFormatter)(*args: Any,  id: ID | None = None, ...)
  - Muestra los valores de los _ticks_ de los rangos categóricos como valores de cadena.
* - [CustomJSTickFormatter](https://docs.bokeh.org/en/latest/docs/reference/models/formatters.html#bokeh.models.CustomJSTickFormatter)(*args: Any,  id: ID | None = None, ...)
  - Muestra valores de los _ticks_ que están formateados por una función definida por el usuario.
* - [DatetimeTickFormatter](https://docs.bokeh.org/en/latest/docs/reference/models/formatters.html#bokeh.models.DatetimeTickFormatter)(*args: Any,  id: ID | None = None, ...)
  - Un `TickFormatter` para mostrar valores de fecha y hora en un rango de escalas.
* - [LogTickFormatter](https://docs.bokeh.org/en/latest/docs/reference/models/formatters.html#bokeh.models.LogTickFormatter)(*args: Any,  id: ID | None = None, ...)
  - Muestra los valores de los _ticks_ de los rangos continuos como potencias de alguna base.
* - [MercatorTickFormatter](https://docs.bokeh.org/en/latest/docs/reference/models/formatters.html#bokeh.models.MercatorTickFormatter)(*args: Any,  id: ID | None = None, ...)
  - Un `TickFormatter` para los valores en las unidades de _WebMercator_.
* - [NumeralTickFormatter](https://docs.bokeh.org/en/latest/docs/reference/models/formatters.html#bokeh.models.NumeralTickFormatter)(*args: Any,  id: ID | None = None, ...)
  - Un `TickFormatter` basado en una cadena de formato legible por humanos.
* - [PrintfTickFormatter](https://docs.bokeh.org/en/latest/docs/reference/models/formatters.html#bokeh.models.PrintfTickFormatter)(*args: Any,  id: ID | None = None, ...)
  - Un `TickFormatter` basado en una cadena de formato de estilo _Printf_.
* - [TickFormatter](https://docs.bokeh.org/en/latest/docs/reference/models/formatters.html#bokeh.models.TickFormatter)(*args: Any,  id: ID | None = None, ...)
  - Una clase base para todos los tipos de `TickFormatter`.
```