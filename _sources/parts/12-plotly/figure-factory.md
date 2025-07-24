# _Figure Factory_

Ofrece funciones para crear figuras especializadas, como gráficos de dispersión matricial, diagramas de violín y mapas de calor.

```python
# importar función
from bokeh.figure_factory import function_name
```
- _function_name_ es el nombre de la función.

:::{note}
Para más información de esta sección visitar la [documentación](https://plotly.com/python-api-reference/plotly.figure_factory.html) de _plotly_.
:::

<br/>

## Funciones

Funciones implementadas en el módulo _figure_factory_. 

:::{note}
En el siguiente lista se omiten todas las funciones obsoletas.
:::

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [create_dendrogram](https://plotly.com/python-api-reference/generated/plotly.figure_factory.create_dendrogram.html)(hist_data,  group_labels[,  ...])
  - Función que devuelve un objeto de figura de dendrograma.
* - [create_hexbin_mapbox](https://plotly.com/python-api-reference/generated/plotly.figure_factory.create_hexbin_mapbox.html)([data_frame,  lat,  lon,  ...])
  - Retorna una figura agregando puntos dispersos en hexágonos conectados.
* - [create_quiver](https://plotly.com/python-api-reference/generated/plotly.figure_factory.create_quiver.html)(x,  y,  u,  v[,  scale,  ...])
  - Retorna datos para un gráfico _quiver_ (carjaj, vectores como flechas).
* - [create_streamline](https://plotly.com/python-api-reference/generated/plotly.figure_factory.create_streamline.html)(x,  y,  u,  v[,  density,  ...])
  - Retorna datos para una gráfica _streamline_.
* - [create_table](https://plotly.com/python-api-reference/generated/plotly.figure_factory.create_table.html)(table_text[,  colorscale,  ...])
  - Función que crea tablas de datos.
* - [create_ternary_contour](https://plotly.com/python-api-reference/generated/plotly.figure_factory.create_ternary_contour.html)(coordinates,  values)
  - Gráfica de contorno ternario.
* - [create_trisurf](https://plotly.com/python-api-reference/generated/plotly.figure_factory.create_trisurf.html)(x,  y,  z,  simplices[,  ...])
  - Retorna una figura para una gráfica de superficie triangulada.
```