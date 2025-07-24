# Traces

Contiene los elementos que representan los datos en el gráfico, como líneas, barras, dispersiones y mapas.

A continuación se presenta una breve lista de la clasificación de _traces_:
- **Trazos de Distribución (Distribution Traces)**: Gráficos para visualizar distribuciones de datos, como histogramas, gráficos de caja (_boxplots_) y gráficos de violín.
- **Trazos Financieros (Finance Traces)**: Gráficos especializados para datos financieros, como velas japonesas (_candlestick_) y gráficos de área financiera.
- **Trazos de Mapas (Map Traces)**: Gráficos para representar datos geográficos, como mapas de dispersión, mapas de líneas y mapas coropléticos.
- **Trazos Simples (Simple Traces)**: Gráficos básicos y comunes, como dispersiones (_scatter_), líneas, barras y áreas.
- **Trazos Especializados (Specialized Traces)**: Gráficos avanzados para casos específicos, como gráficos de contorno, mapas de calor, gráficos de pastel (_pie_) y gráficos de embudo (_funnel_).

<br/>

## Distribución

Gráficos para visualizar distribuciones de datos, como histogramas, gráficos de caja (_boxplots_) y gráficos de violín.

```{list-table}
:header-rows: 1

* - Constructor
  - Descripción
* - [Box](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Box.html)([arg,  alignmentgroup, ...)
  - Construye un nuevo objeto de _Box_.
* - [Histogram](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Histogram.html)([arg,  alignmentgroup, ...)
  - Construye un nuevo objeto de _Histogram_.
* - [Histogram2d](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Histogram2d.html)([arg,  autobinx,  autobiny,  …])
  - Construye un nuevo objeto de _Histogram2d_.
* - [Histogram2dContour](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Histogram2dContour.html)([arg,  autobinx,  …])
  - Construye un nuevo objeto de _Histogram2dContour_.
* - [Violin](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Violin.html)([arg,  alignmentgroup, ...)
  - Construye un nuevo objeto de _Violin_.
```

<br/>

## Financieros

Gráficos especializados para datos financieros, como velas japonesas (_candlestick_) y gráficos de área financiera.

```{list-table}
:header-rows: 1

* - Constructor
  - Descripción
* - [Candlestick](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Candlestick.html)([arg,  close,  closesrc,  …])
  - Construye un nuevo objeto de _Candlestick_. _Candlestick_ es un estilo de gráfico financiero que describe _open, high, low_ y _close_ para un coordenada.
* - [Funnel](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Funnel.html)([arg,  alignmentgroup, ...)
  - Construye un nuevo objeto de _Funnel_. Útil para visualizar las etapas en un proceso utilizando barras codificadas por longitud.
* - [Funnelarea](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Funnelarea.html)([arg,  aspectratio,  baseratio, ...)
  - Construye un nuevo objeto de _Funnelarea_. Útil para visualizar las etapas en un proceso utilizando trapecios codificados por el área.
* - [Indicator](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Indicator.html)([arg,  align,  customdata,  …])
  - Construye un nuevo objeto de _Indicator_. Se utiliza un indicador para visualizar un único valor con cierta información contextual.
* - [Ohlc](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Ohlc.html)([arg,  close,  closesrc, ...)
  - Construye un nuevo objeto de _OHLC_. El OHLC es un estilo de gráfico financiero que describe _open, high, low_ y _close_ para un coordenada.
* - [Waterfall](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Waterfall.html)([arg,  alignmentgroup,  base, ...)
  - Construye un nuevo objeto de _Waterfall_. Es un gráfico útil para mostrar la contribución de varios elementos (positivos o negativos) en un gráfico de barras.
```

<br/>

## Mapas

Gráficos para representar datos geográficos, como mapas de dispersión, mapas de líneas y mapas coropléticos.

:::{note}
Se omiten las clases obsoletas.
:::

```{list-table}
:header-rows: 1

* - Constructor
  - Descripción
* - [Choropleth](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Choropleth.html)([arg,  autocolorscale, ...)
  - Construye un nuevo objeto de _Choropleth_. Mapea colores a mapas geográficos.
* - [Choroplethmap](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Choroplethmap.html)([arg,  autocolorscale,  below, ...)
  - Construye un nuevo objeto _Choroplethmap_. Mapea colores a mapas geográficos.
* - [Densitymap](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Densitymap.html)([arg,  autocolorscale,  below, ...)
  - Construye un nuevo objeto de _Densitymap_. GRafica una estimación de densidad de núcleo bivariada con un núcleo gaussiano de coordenados _lon_ y _lat_ y valores opcionales utilizando una escala de colores.
* - [Scattergeo](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Scattergeo.html)([arg,  connectgaps, ...)
  - Construye un nuevo objeto de _ScatterGeo_. Visualiza puntos de dispersión o líneas en un mapa geográfico.
* - [Scattermap](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Scattermap.html)([arg,  below,  cluster,  …])
  - Construye un nuevo objeto de _ScatterMap_. Visualiza puntos de dispersión, líneas o símbolos de marcador en un mapa geográfico.
```

<br/>

## Comunes

Gráficos básicos y comunes, como dispersiones (_scatter_), líneas, barras y áreas.

```{list-table}
:header-rows: 1

* - Constructor
  - Descripción
* - [Bar](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Bar.html)([arg,  alignmentgroup,  base, ...)
  - Construye un nuevo objeto de _Bar_.
* - [Contour](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Contour.html)([arg,  autocolorscale, ...)
  - Construye un nuevo objeto de _Contour_.
* - [Heatmap](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Heatmap.html)([arg,  autocolorscale, ...)
  - Construye un nuevo objeto de _Heatmap_.
* - [Image](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Image.html)([arg,  colormodel,  customdata, ...)
  - Construye un nuevo objeto de _Image_. Muestra una imagen, es decir, datos en un ráster regular 2D.
* - [Pie](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Pie.html)([arg,  automargin,  customdata, ...)
  - Construye un nuevo objeto de _Pie_.
* - [Scatter](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Scatter.html)([arg,  alignmentgroup, ...)
  - Construye un nuevo objeto de _Scatter_.
* - [Scattergl](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Scattergl.html)([arg,  connectgaps, ...)
  - Construye un nuevo objeto de _Scattergl_.
* - [Table](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Table.html)([arg,  cells,  columnorder,  …])
  - Construye un nuevo objeto de _Table_. Vista de tabla para la visualización detallada de datos. Los datos se organizan en una cuadrícula de filas y columnas. La mayoría del estilo se puede especificar para columnas, filas o celdas individuales.
```

<br/>

## Especializados

Gráficos avanzados para casos específicos, como gráficos de contorno, mapas de calor, gráficos de tarta (_pie_) y gráficos de embudo (_funnel_).

```{list-table}
:header-rows: 1

* - Constructor
  - Descripción
* - [Barpolar](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Barpolar.html)([arg,  base,  basesrc, ...)
  - Construye un nuevo objeto de _Barpolar_.
* - [Carpet](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Carpet.html)([arg,  a,  a0,  aaxis,  asrc,  b, ...)
  - Construye un nuevo objeto de _Carpet_.
* - [Contourcarpet](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Contourcarpet.html)([arg,  a,  a0,  asrc,  atype,  …])
  - Construye un nuevo objeto de _Contourcarpet_.
* - [Icicle](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Icicle.html)([arg,  branchvalues,  count, ...)
  - Construye un nuevo objeto de _Icicle_. Visualiza datos jerárquicos de las hojas (y/o ramas externas) hacia la raíz con rectángulos.
* - [Parcats](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Parcats.html)([arg,  arrangement, ...)
  - Construye un nuevo objeto de _Parcats_. Diagrama de categorías paralelas para datos categóricos multidimensionales.
* - [Parcoords](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Parcoords.html)([arg,  customdata, ...)
  - Construye un nuevo objeto de _Parcoords_. Coordenadas paralelas para el análisis de datos exploratorios multidimensionales.
* - [Sankey](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Sankey.html)([arg,  arrangement, ...)
  - Construye un nuevo objeto de _Sankey_. Para el análisis de datos de flujo de _networks_.
* - [Scattercarpet](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Scattercarpet.html)([arg,  a,  asrc,  b,  bsrc,  …])
  - Construye un nuevo objeto de _Scattercarpet_.
* - [Scatterpolar](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Scatterpolar.html)([arg,  cliponaxis, ...)
  - Construye un nuevo objeto de _Scatterpolar_.
* - [Scatterpolargl](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Scatterpolargl.html)([arg,  connectgaps,  …])
  - Construye un nuevo objeto _Scatterpolargl_. Abarca gráficos de línea, gráficos de dispersión y gráficos de burbujas en coordenadas polares.
* - [Scatterternary](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Scatterternary.html)([arg,  a,  asrc,  b,  bsrc,  c, ...)
  - Construye un nuevo objeto Scatterternary_. Proporciona una funcionalidad similar al tipo de "dispersión" pero en un diagrama de fase ternario.
* - [Splom](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Splom.html)([arg,  customdata, ...)
  - Construye un nuevo objeto _Splom_. Generan visualizaciones de matriz de gráficos de dispersión.
* - [Sunburst](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Sunburst.html)([arg,  branchvalues,  count, ...)
  - Construye un nuevo objeto _Sunburst_. Visualiza datos jerárquicos que se extienden hacia afuera radialmente desde la raíz hasta las hojas.
* - [Treemap](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Treemap.html)([arg,  branchvalues,  count, ...)
  - Construye un nuevo objeto _Treemap_. Visualiza datos jerárquicos de las hojas (y/o ramas externas) hacia la raíz con rectángulos.
```