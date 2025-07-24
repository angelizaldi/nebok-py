# Anotaciones

Proporciona elementos para añadir anotaciones a gráficos, como títulos, leyendas y etiquetas.

:::{note}
Para más información de esta sección visitar la [documentación](https://docs.bokeh.org/en/latest/docs/reference/models/annotations.html) de _bokeh_.
:::

:::{tip}
Para una visualización de los diferentes tipos de anotaciones visitar la [guía de uso](https://docs.bokeh.org/en/latest/docs/user_guide/basic/annotations.html) de _bokeh_.
:::

## Clases

Clases implementadas en el módulo _models_ del tipo _annotations_. 

```{list-table}
:header-rows: 1

* - Constructor
  - Descripción
* - **Áreas, polígonos y bandas**
  -
* - [Band](https://docs.bokeh.org/en/latest/docs/reference/models/annotations.html#bokeh.models.Band)(*args: Any,  id: ID | None = None, ...)
  - Renderiza una banda (área irregular) de área rellena a lo largo de una dimensión.
* - [BoxInteractionHandles](https://docs.bokeh.org/en/latest/docs/reference/models/annotations.html#bokeh.models.BoxInteractionHandles)(*args: Any,  id: ID | None = None, ...)
  - Define las manijas de interacción para anotaciones similares a la _box_.
* - [PolyAnnotation](https://docs.bokeh.org/en/latest/docs/reference/models/annotations.html#bokeh.models.PolyAnnotation)(*args: Any,  id: ID | None = None, ...)
  - Renderiza una región poligonal sombreada como anotación.
* - **Barras de color y escala**
  - 
* - [ColorBar](https://docs.bokeh.org/en/latest/docs/reference/models/annotations.html#bokeh.models.ColorBar)(*args: Any,  id: ID | None = None, ...)
  - Renderiza una barra de color basada en un mapeador de color.
* - [ContourColorBar](https://docs.bokeh.org/en/latest/docs/reference/models/annotations.html#bokeh.models.ContourColorBar)(*args: Any,  id: ID | None = None, ...)
  - Barra de color utilizada para contornos.
* - [ScaleBar](https://docs.bokeh.org/en/latest/docs/reference/models/annotations.html#bokeh.models.ScaleBar)(*args: Any,  id: ID | None = None, ...)
  - Representa una anotación de barra de escala.
* - **Etiquetas y títulos**
  -
* - [Label](https://docs.bokeh.org/en/latest/docs/reference/models/annotations.html#bokeh.models.Label)(*args: Any,  id: ID | None = None, ...)
  - Renderiza una sola etiqueta de texto como anotación.
* - [LabelSet](https://docs.bokeh.org/en/latest/docs/reference/models/annotations.html#bokeh.models.LabelSet)(*args: Any,  id: ID | None = None, ...)
  - Renderiza múltiples etiquetas de texto como anotaciones.
* - [TextAnnotation](https://docs.bokeh.org/en/latest/docs/reference/models/annotations.html#bokeh.models.TextAnnotation)(*args: Any,  id: ID | None = None, ...)
  - Clase base para modelos de anotación de texto como etiquetas y títulos.
* - [Title](https://docs.bokeh.org/en/latest/docs/reference/models/annotations.html#bokeh.models.Title)(*args: Any,  id: ID | None = None, ...)
  - Renderiza un solo cuadro de título como anotación.
* - **Flechas**
  - 
* - [Arrow](https://docs.bokeh.org/en/latest/docs/reference/models/annotations.html#bokeh.models.Arrow)(*args: Any,  id: ID | None = None, ...)
  - Renderiza flechas como anotación.
* - [ArrowHead](https://docs.bokeh.org/en/latest/docs/reference/models/annotations.html#bokeh.models.ArrowHead)(*args: Any,  id: ID | None = None, ...)
  - Clase base para cabezas de flecha.
* - [NormalHead](https://docs.bokeh.org/en/latest/docs/reference/models/annotations.html#bokeh.models.NormalHead)(*args: Any,  id: ID | None = None, ...)
  - Renderiza una cabeza de flecha de cuerpo cerrado.
* - [OpenHead](https://docs.bokeh.org/en/latest/docs/reference/models/annotations.html#bokeh.models.OpenHead)(*args: Any,  id: ID | None = None, ...)
  - Renderiza una cabeza de flecha de cuerpo abierto.
* - [TeeHead](https://docs.bokeh.org/en/latest/docs/reference/models/annotations.html#bokeh.models.TeeHead)(*args: Any,  id: ID | None = None, ...)
  - Renderiza una cabeza de flecha al estilo de _tee_.
* - [VeeHead](https://docs.bokeh.org/en/latest/docs/reference/models/annotations.html#bokeh.models.VeeHead)(*args: Any,  id: ID | None = None, ...)
  - Renderiza una cabeza de flecha de estilo _vee_.
* - **HTML**
  -
* - [HTMLAnnotation](https://docs.bokeh.org/en/latest/docs/reference/models/annotations.html#bokeh.models.HTMLAnnotation)(*args: Any,  id: ID | None = None, ...)
  - Clase base para anotaciones basadas en HTML.
* - [HTMLLabel](https://docs.bokeh.org/en/latest/docs/reference/models/annotations.html#bokeh.models.HTMLLabel)(*args: Any,  id: ID | None = None, ...)
  - Renderiza una sola etiqueta HTML como anotación.
* - [HTMLLabelSet](https://docs.bokeh.org/en/latest/docs/reference/models/annotations.html#bokeh.models.HTMLLabelSet)(*args: Any,  id: ID | None = None, ...)
  - Renderiza múltiples etiquetas de texto como anotaciones.
* - [HTMLTitle](https://docs.bokeh.org/en/latest/docs/reference/models/annotations.html#bokeh.models.HTMLTitle)(*args: Any,  id: ID | None = None, ...)
  - Renderiza un solo cuadro de título como anotación.
* - **Leyendas**
  -
* - [Legend](https://docs.bokeh.org/en/latest/docs/reference/models/annotations.html#bokeh.models.Legend)(*args: Any,  id: ID | None = None, ...)
  - Renderizar leyendas informativas para una gráfica.
* - [LegendItem](https://docs.bokeh.org/en/latest/docs/reference/models/annotations.html#bokeh.models.LegendItem)(*args: Any,  id: ID | None = None, ...)
  - .
* - **Líneas y rectas**
  -
* - [Slope](https://docs.bokeh.org/en/latest/docs/reference/models/annotations.html#bokeh.models.Slope)(*args: Any,  id: ID | None = None, ...)
  - Renderiza una línea inclinada como anotación.
* - [Span](https://docs.bokeh.org/en/latest/docs/reference/models/annotations.html#bokeh.models.Span)(*args: Any,  id: ID | None = None, ...)
  - Renderiza líneas horizontal o vertical.
* - [Whisker](https://docs.bokeh.org/en/latest/docs/reference/models/annotations.html#bokeh.models.Whisker)(*args: Any,  id: ID | None = None, ...)
  - Renderiza un bigote a lo largo de una dimensión.
* - **Unidades métricas**
  -
* - [Angular](https://docs.bokeh.org/en/latest/docs/reference/models/annotations.html#bokeh.models.Angular)(*args: Any,  id: ID | None = None, ...)
  - Unidades de medición angular.
* - [ImperialLength](https://docs.bokeh.org/en/latest/docs/reference/models/annotations.html#bokeh.models.ImperialLength)(*args: Any,  id: ID | None = None, ...)
  - Unidades imperiales de medición de longitud.
* - [Metric](https://docs.bokeh.org/en/latest/docs/reference/models/annotations.html#bokeh.models.Metric)(*args: Any,  id: ID | None = None, ...)
  - Modelo para definir unidades métricas de medición.
* - [MetricLength](https://docs.bokeh.org/en/latest/docs/reference/models/annotations.html#bokeh.models.MetricLength)(*args: Any,  id: ID | None = None, ...)
  - Unidades métricas de medición de longitud.
* - **Otras**
  -
* - [Annotation](https://docs.bokeh.org/en/latest/docs/reference/models/annotations.html#bokeh.models.Annotation)(*args: Any,  id: ID | None = None, ...)
  - Clase base para todos los modelos de anotación.
* - [ToolbarPanel](https://docs.bokeh.org/en/latest/docs/reference/models/annotations.html#bokeh.models.ToolbarPanel)(*args: Any,  id: ID | None = None, ...)
  - .
```

<br/>

