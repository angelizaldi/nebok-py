# _Sources_

Proporciona fuentes de datos para alimentar visualizaciones, como `ColumnDataSource` y `GeoJSONDataSource`.

:::{note}
Para más información de esta sección visitar la [documentación](https://docs.bokeh.org/en/latest/docs/reference/models/sources.html) de `bokeh`.
:::

## Clases

Clases implementadas en el módulo _models_ del tipo _sources_. 

```{list-table}
:header-rows: 1

* - Constructor
  - Descripción
* - [AjaxDataSource](https://docs.bokeh.org/en/latest/docs/reference/models/sources.html#bokeh.models.AjaxDataSource)(*args: Any,  id: ID | None = None, ...)
  - Una fuente de datos que puede llenar columnas haciendo llamadas _calls_ a _REST endpoints_.
* - [CDSView](https://docs.bokeh.org/en/latest/docs/reference/models/sources.html#bokeh.models.CDSView)(*args: Any,  id: ID | None = None, ...)
  - Un _view_ de una `ColumnDataSource` que representa un subconjunto de filas.
* - [ColumnDataSource](https://docs.bokeh.org/en/latest/docs/reference/models/sources.html#bokeh.models.ColumnDataSource)(*args: Any,  id: ID | None = None, ...)
  - Mapea nombres de columnas a secuencias o matrices.
* - [ColumnarDataSource](https://docs.bokeh.org/en/latest/docs/reference/models/sources.html#bokeh.models.ColumnarDataSource)(*args: Any,  id: ID | None = None, ...)
  - Una clase base para los tipos de fuente de datos, que se pueden asignar en un formato columnar.
* - [DataSource](https://docs.bokeh.org/en/latest/docs/reference/models/sources.html#bokeh.models.DataSource)(*args: Any,  id: ID | None = None, ...)
  - Una clase base para tipos de fuente de datos.
* - [GeoJSONDataSource](https://docs.bokeh.org/en/latest/docs/reference/models/sources.html#bokeh.models.GeoJSONDataSource)(*args: Any,  id: ID | None = None, ...)
  - .
* - [ServerSentDataSource](https://docs.bokeh.org/en/latest/docs/reference/models/sources.html#bokeh.models.ServerSentDataSource)(*args: Any,  id: ID | None = None, ...)
  - Una fuente de datos que puede llenar columnas al recibir del servidor enviios de eventos _endpoints_.
* - [WebDataSource](https://docs.bokeh.org/en/latest/docs/reference/models/sources.html#bokeh.models.WebDataSource)(*args: Any,  id: ID | None = None, ...)
  - Clase base para fuentes de datos de columna web que pueden actualizarse desde una URL.
```