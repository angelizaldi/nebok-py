# _Express_

Proporciona una interfaz de alto nivel para crear gráficos de manera rápida y sencilla con una sola línea de código.

```python
# importar librería
import bokeh.express as px
```
- _px_ es el nombres por convención.

:::{note}
Para más información de esta sección visitar la [documentación](https://plotly.com/python-api-reference/plotly.express.html) de _plotly_.
:::

:::{warning}
_express_ tiene los siguientes submódulos que no se revisarán en este sitio:
- [data](https://plotly.com/python-api-reference/generated/plotly.express.data.html): Contiene conjuntos de datos de muestra que se pueden usar para generar gráficos rápidamente.
- [colors](https://plotly.com/python-api-reference/generated/plotly.express.colors.html): Proporciona herramientas para manejar colores en gráficos, incluyendo escalas de colores (_sequential_, _diverging_, _categorical_), funciones para interpolar colores y conversiones de formatos de color.
- [trendline_functions](https://plotly.com/python-api-reference/generated/plotly.express.trendline_functions.html): Contiene funciones internas usadas para calcular y agregar líneas de tendencia a gráficos, como ajustes de regresión lineal o polinómica.
:::

<br/>

## Funciones

Funciones implementadas en el módulo _express_. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - **Comunes**
  -
* - [area](https://plotly.com/python-api-reference/generated/plotly.express.area.html)([data_frame,  x,  y, ...)
  - Gráfico de área basado en una serie de líneas apiladas, útil para mostrar acumulaciones de valores a lo largo del tiempo.
* - [bar](https://plotly.com/python-api-reference/generated/plotly.express.bar.html)([data_frame,  x,  y,  color,  ...])
  - Gráfico de barras estándar para comparar valores entre diferentes categorías.
* - [imshow](https://plotly.com/python-api-reference/generated/plotly.express.imshow.html)(img[,  zmin,  zmax,  origin, ...)
  - Muestra una imagen o matriz de datos como un mapa de calor.
* - [line](https://plotly.com/python-api-reference/generated/plotly.express.line.html)([data_frame,  x,  y, ...)
  - Gráfico de líneas estándar para representar series temporales o tendencias en datos continuos.
* - [pie](https://plotly.com/python-api-reference/generated/plotly.express.pie.html)([data_frame,  names,  values, ...)
  - Gráfico de pastel que muestra la proporción de cada categoría en un total.
* - [scatter](https://plotly.com/python-api-reference/generated/plotly.express.scatter.html)([data_frame,  x,  y,  color, ...)
  - Gráfico de dispersión para visualizar relaciones entre dos variables.
* - [strip](https://plotly.com/python-api-reference/generated/plotly.express.strip.html)([data_frame,  x,  y,  color, ...)
  - Gráfico de dispersión unidimensional que muestra la distribución de valores en una sola dimensión.
* - **Distribución**
  -
* - [box](https://plotly.com/python-api-reference/generated/plotly.express.box.html)([data_frame,  x,  y,  color, ...)
  - Gráfico de cajas y bigotes que muestra la distribución de un conjunto de datos, incluyendo cuartiles y valores atípicos. (_boxplots_).
* - [ecdf](https://plotly.com/python-api-reference/generated/plotly.express.ecdf.html)([data_frame,  x,  y,  color, ...)
  - Gráfico de función de distribución acumulativa empírica, útil para visualizar la distribución de datos.
* - [histogram](https://plotly.com/python-api-reference/generated/plotly.express.histogram.html)([data_frame,  x,  y,  color,  ...])
  - Gráfico de histogramas que agrupa datos en intervalos para visualizar la distribución de frecuencias.
* - [violin](https://plotly.com/python-api-reference/generated/plotly.express.violin.html)([data_frame,  x,  y,  color, ...)
  - Gráfico de violín que combina la visualización de una distribución (como un histograma) con un gráfico de caja y bigotes.
* - **Especializados**
  -
* - [bar_polar](https://plotly.com/python-api-reference/generated/plotly.express.bar_polar.html)([data_frame,  r,  theta,  color, ...)
  - Variante del gráfico de barras en coordenadas polares, útil para mostrar datos cíclicos o radiales.
* - [density_contour](https://plotly.com/python-api-reference/generated/plotly.express.density_contour.html)([data_frame,  x,  y,  z,  ...])
  - Gráfico de contornos de densidad que muestra la distribución de datos en dos dimensiones con líneas de nivel.
* - [icicle](https://plotly.com/python-api-reference/generated/plotly.express.icicle.html)([data_frame,  names,  values, ...)
  - Gráfico jerárquico similar a un `treemap()`, pero en formato de barras anidadas.
* - [line_3d](https://plotly.com/python-api-reference/generated/plotly.express.line_3d.html)([data_frame,  x,  y,  z,  color, ...)
  - Variante del gráfico de líneas en un espacio tridimensional.
* - [line_polar](https://plotly.com/python-api-reference/generated/plotly.express.line_polar.html)([data_frame,  r,  theta,  color, ...)
  - Gráfico de líneas en coordenadas polares, ideal para datos cíclicos como direcciones o velocidades angulares.
* - [line_ternary](https://plotly.com/python-api-reference/generated/plotly.express.line_ternary.html)([data_frame,  a,  b,  c,  color, ...)
  - Gráfico de líneas en coordenadas ternarias, útil para visualizar composiciones de tres variables.
* - [parallel_categories](https://plotly.com/python-api-reference/generated/plotly.express.parallel_categories.html)([data_frame,  ...])
  - Gráfico de categorías paralelas que muestra relaciones entre variables categóricas.
* - [parallel_coordinates](https://plotly.com/python-api-reference/generated/plotly.express.parallel_coordinates.html)([data_frame,  ...])
  - Gráfico de coordenadas paralelas para visualizar múltiples variables numéricas en un mismo eje.
* - [scatter_3d](https://plotly.com/python-api-reference/generated/plotly.express.scatter_3d.html)([data_frame,  x,  y,  z,  color, ...)
  - Variante del gráfico de dispersión en tres dimensiones.
* - [scatter_polar](https://plotly.com/python-api-reference/generated/plotly.express.scatter_polar.html)([data_frame,  r,  theta,  color, ...)
  - Gráfico de dispersión en coordenadas polares, útil para representar datos cíclicos.
* - [scatter_ternary](https://plotly.com/python-api-reference/generated/plotly.express.scatter_ternary.html)([data_frame,  a,  b,  c,  ...])
  - Gráfico de dispersión en coordenadas ternarias, utilizado para analizar mezclas de tres variables.
* - [sunburst](https://plotly.com/python-api-reference/generated/plotly.express.sunburst.html)([data_frame,  names,  values, ...)
  - Gráfico jerárquico en forma de diagrama de anillos concéntricos.
* - [timeline](https://plotly.com/python-api-reference/generated/plotly.express.timeline.html)([data_frame,  x_start,  x_end, ...)
  - Gráfico de barras especial para representar eventos a lo largo del tiempo.
* - [treemap](https://plotly.com/python-api-reference/generated/plotly.express.treemap.html)([data_frame,  names,  values, ...)
  - Gráfico jerárquico en forma de rectángulos anidados, útil para representar proporciones dentro de una jerarquía.
* - **Financieros**
  -
* - [funnel](https://plotly.com/python-api-reference/generated/plotly.express.funnel.html)([data_frame,  x,  y,  color, ...)
  - Gráfico de embudo, comúnmente usado para representar procesos de conversión o reducción de datos en etapas.
* - [funnel_area](https://plotly.com/python-api-reference/generated/plotly.express.funnel_area.html)([data_frame,  names,  values, ...)
  - Variante del gráfico de embudo donde el área de cada sección es proporcional al valor correspondiente.
* - **Mapas**
  -
* - [choropleth](https://plotly.com/python-api-reference/generated/plotly.express.choropleth.html)([data_frame,  lat,  lon,  ...])
  - Mapa coroplético que representa valores con colores en regiones geográficas usando datos geométricos integrados.
* - [choropleth_map](https://plotly.com/python-api-reference/generated/plotly.express.choropleth_map.html)([data_frame,  geojson,  ...])
  - Similar a `choropleth()`, pero con más opciones de personalización.
* - [density_map](https://plotly.com/python-api-reference/generated/plotly.express.density_map.html)([data_frame,  lat,  lon,  z,  ...])
  - Muestra la densidad de puntos sobre un mapa geográfico.
* - [line_geo](https://plotly.com/python-api-reference/generated/plotly.express.line_geo.html)([data_frame,  lat,  lon, ...)
  - Gráfico de líneas sobre un mapa geográfico sin usar _Mapbox_.
* - [line_map](https://plotly.com/python-api-reference/generated/plotly.express.line_map.html)([data_frame,  lat,  lon,  color, ...)
  - Similar a `line_geo()`, pero con opciones adicionales de personalización.
* - [scatter_geo](https://plotly.com/python-api-reference/generated/plotly.express.scatter_geo.html)([data_frame,  lat,  lon,  ...])
  - Gráfico de dispersión sobre un mapa geográfico sin usar _Mapbox_.
* - [scatter_map](https://plotly.com/python-api-reference/generated/plotly.express.scatter_map.html)([data_frame,  lat,  lon,  color, ...)
  - Similar a `scatter_geo()`, pero con opciones adicionales.
* - **Matriciales**
  -
* - [density_heatmap](https://plotly.com/python-api-reference/generated/plotly.express.density_heatmap.html)([data_frame,  x,  y,  z,  ...])
  - Mapa de calor de densidad que representa la distribución de puntos en dos dimensiones con colores.
* - [scatter_matrix](https://plotly.com/python-api-reference/generated/plotly.express.scatter_matrix.html)([data_frame,  dimensions,  ...])
  - Matriz de gráficos de dispersión para visualizar correlaciones entre múltiples variables.
```