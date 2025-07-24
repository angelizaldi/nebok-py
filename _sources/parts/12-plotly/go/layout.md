# _Layout_

Define la apariencia y estructura del gráfico, como títulos, ejes, leyendas y márgenes. En esta sección se revisan tanto la clase `Layout` como el módulo _layout_. Ambos se relacionan ya que una instancia de `Layout` se define con las clases implementadas en el módulo _layout_.

:::{warning}
El módulo _layout_ tiene múltiples submódulos que se pueden revisar en la [documentación](https://plotly.com/python-api-reference/generated/plotly.graph_objects.layout.html#subpackages). Notar que el módulo se divide en múltiples submódulos, y estos a su vez estos pueden tener otros submódulos.

En las clases documentadas en este sitio que tienen submódulos se enlistarán sus submódulos.
:::

## Layout

Objeto que establece el estilo de una figura.

```{list-table}
:header-rows: 1

* - Constructor
  - Descripción
* - [go.Layout](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.Layout)(arg=None, ...)
  - Construye un nuevo objeto de diseño.
```

<br/>

`plotly.graph_object.Layout()`: Objeto que establece el estilo de una figura.
```python
# Sintaxis de llamada
go.Layout(*args, , **kwargs)
```
**Parámetros:**
- **legend** - `layout.Legend` o `dict`: Propiedades de la leyenda de la gráfica.
- **xaxis**, **yaxis** - `layout.XAxis`, `layout.Yaxis` o `dict`: Propiedades de los ejes _x_ y _y_ respectivamente.
- **title** - `layout.Title` o `dict`: Propiedades del título de la gráfica.
- **annotations** - `tuple` de `layout.Annotation` o `dict`: Instancias o `dict` con propiedades compatibles.

<br/>

## Clases

Clases implementadas en el submódulo _graph_objects.layout_. Las instancias de estas clases se utilizan como argumentos del constructor de `Layout`.

```{list-table}
:header-rows: 1

* - Constructor
  - Descripción
* - **Anotaciones, etiquetas, leyendas y títulos**
  -
* - [go.layout.Annotation](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Annotation)(arg=None, align=None, ...)
  - Agrega texto y marcas en una ubicación específica del gráfico.
* - [go.layout.Font](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Font)(arg=None, color=None, ...)
  - Define el tipo de fuente, tamaño y color para los textos en el gráfico.
* - [go.layout.Legend](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Legend)(arg=None, bgcolor=None, ...)
  - Configura la apariencia y posición de la leyenda del gráfico.
* - [go.layout.Title](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Title)(arg=None, automargin=None, ...)
  - Especifica las propiedades del título del gráfico.
* - [go.layout.Uniformtext](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Uniformtext)(arg=None, minsize=None, ...)
  - Controla la apariencia uniforme del texto en las etiquetas de la gráfica.
* - **Colores y escalas**
  -
* - [go.layout.Coloraxis](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Coloraxis)(arg=None, autocolorscale=None, ...)
  - Maneja el mapeo de valores a colores en gráficos que usan escala de colores.
* - [go.layout.Colorscale](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Colorscale)(arg=None, diverging=None, ...)
  - Define una escala de colores específica para representar datos en el gráfico.
* - **Diseño y estructura del gráfico**
  -
* - [go.layout.Grid](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Grid)(arg=None, columns=None, ...)
  - Define la disposición de una cuadrícula en el diseño de subgráficos.
* - [go.layout.Margin](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Margin)(arg=None, autoexpand=None, ...)
  - Controla los márgenes alrededor de la gráfica.
* - **Coordenadas y sistemas de referencia**
  -
* - [go.layout.Polar](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Polar)(arg=None, angularaxis=None, ...)
  - Configura gráficos en coordenadas polares.
* - [go.layout.Scene](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Scene)(arg=None, annotations=None, ...)
  - Controla la configuración de gráficos en 3D, como `scatter_3d` o `surface`.
* - [go.layout.Smith](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Smith)(arg=None, bgcolor=None, ...)
  - Define gráficos de tipo Smith (usados en ingeniería eléctrica para impedancias).
* - [go.layout.Ternary](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Ternary)(arg=None, aaxis=None, ...)
  - Define gráficos en un sistema de coordenadas ternarias.
* - **Ejes**
  -
* - [go.layout.XAxis](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.XAxis)(arg=None, anchor=None, ...)
  - Configura el eje _x_ del gráfico (etiquetas, rango, escala, etc.).
* - [go.layout.YAxis](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.YAxis)(arg=None, anchor=None, ...)
  - Configura el eje Y del gráfico.
* - **Interactividad y controles**
  -
* - [go.layout.Hoverlabel](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Hoverlabel)(arg=None, align=None, ...)
  - Personaliza la apariencia de las etiquetas emergentes (tooltip) al pasar el mouse.
* - [go.layout.Modebar](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Modebar)(arg=None, activecolor=None, ...)
  - Controla la barra de herramientas flotante de la figura interactiva.
* - [go.layout.Slider](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Slider)(arg=None, active=None, ...)
  - Configura barras deslizantes para explorar diferentes estados del gráfico.
* - [go.layout.Transition](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Transition)(arg=None, duration=None, ...)
  - Especifica efectos de transición entre estados del gráfico.
* - [go.layout.Updatemenu](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Updatemenu)(arg=None, active=None, ...)
  - Agrega menús interactivos para actualizar la visualización de datos.
* - **Mapas**
  -
* - [go.layout.Geo](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Geo)(arg=None, bgcolor=None, ...)
  - Configura mapas geoespaciales (sin _Mapbox_), como choropleth y scatter geográfico.
* - [go.layout.Map](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Map)(arg=None, bearing=None, ...)
  - Define configuraciones para gráficos de mapas. (No ampliamente documentado en _Plotly_).
* - [go.layout.Mapbox](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Mapbox)(arg=None, accesstoken=None, ...)
  - Especifica la configuración de mapas interactivos basados en _Mapbox_.
* - **Otras clases**
  -
* - [go.layout.Image](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Image)(arg=None, layer=None, ...)
  - Permite agregar imágenes dentro de la gráfica.
* - [go.layout.Shape](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Shape)(arg=None, editable=None, ...)
  - Define formas geométricas dentro del gráfico, como líneas, rectángulos y círculos.
* - [go.layout.Template](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Template)(arg=None, data=None, ...)
  - Permite definir un estilo de gráfico reutilizable.
* - **Selección y formas**
  -
* - [go.layout.Activeselection](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Activeselection)(arg=None, fillcolor=None, ...)
  - Representa la selección actualmente activa en una figura interactiva.
* - [go.layout.Activeshape](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Activeshape)(arg=None, fillcolor=None, ...)
  - Define la forma actualmente activa en una figura cuando se está editando interactivamente.
* - [go.layout.Newselection](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Newselection)(arg=None, line=None, mode=None, ...)
  - Configura el comportamiento de una nueva selección en la gráfica.
* - [go.layout.Newshape](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Newshape)(arg=None, drawdirection=None, ...)
  - Configura el comportamiento de una nueva forma creada en la figura.
* - [go.layout.Selection](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Selection)(arg=None, line=None, name=None, ...)
  - Define una selección específica dentro del gráfico.
```

<br/>

### Annotation

Clase `Annotation`.

```{list-table}
:header-rows: 1

* - Constructor
  - Descripción
* - [go.layout.Annotation](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Annotation)(arg=None, align=None, ...)
  - Agrega texto y marcas en una ubicación específica del gráfico.
```

:::{important}
El módulo asociado a esta clase es [layout.annotation](https://plotly.com/python-api-reference/generated/plotly.graph_objects.layout.annotation.html) y sus submódulos son los siguientes:
- [annotation.hoverlabel](https://plotly.com/python-api-reference/generated/plotly.graph_objects.layout.annotation.hoverlabel.html)
:::

<br/>

#### Atributos de _Annotation_

Atributos de la clase `Annotation`.

:::{caution}
Las descripciones de los atributos de esta clase están en inglés.
:::

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - [align](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Annotation.align)
  - Sets the horizontal alignment of the text within the box.
* - [arrowcolor](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Annotation.arrowcolor)
  - Sets the color of the annotation arrow.
* - [arrowhead](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Annotation.arrowhead)
  - Sets the end annotation arrow head style.
* - [arrowside](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Annotation.arrowside)
  - Sets the annotation arrow head position.
* - [arrowsize](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Annotation.arrowsize)
  - Sets the size of the end annotation arrow head, relative to arrow width.
* - [arrowwidth](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Annotation.arrowwidth)
  - Sets the width (in px) of annotation arrow line.
* - [axref](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Annotation.axref)
  - Indicates in what coordinates the tail of the annotation (ax,ay) is specified.
* - [ax](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Annotation.ax)
  - Sets the _x_ component of the arrow tail about the arrow head.
* - [ayref](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Annotation.ayref)
  - Indicates in what coordinates the tail of the annotation (ax,ay) is specified.
* - [ay](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Annotation.ay)
  - Sets the _y_ component of the arrow tail about the arrow head.
* - [bgcolor](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Annotation.bgcolor)
  - Sets the background color of the annotation.
* - [bordercolor](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Annotation.bordercolor)
  - Sets the color of the border enclosing the annotation text.
* - [borderpad](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Annotation.borderpad)
  - Sets the padding (in px) between the text and the enclosing border.
* - [borderwidth](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Annotation.borderwidth)
  - Sets the width (in px) of the border enclosing the annotation text.
* - [captureevents](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Annotation.captureevents)
  - Determines whether the annotation text box captures mouse move and click events, or allows those events to pass through to data points in the plot that may be behind the annotation.
* - [clicktoshow](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Annotation.clicktoshow)
  - Makes this annotation respond to clicks on the plot.
* - [font](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Annotation.font)
  - Sets the annotation text font.
* - [height](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Annotation.height)
  - Sets an explicit height for the text box.
* - [hoverlabel](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Annotation.hoverlabel)
  - The `hoverlabel` property is an instance of [HoverLabel](https://plotly.com/python-api-reference/generated/plotly.graph_objects.layout.annotation.hoverlabel.html).
* - [hovertext](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Annotation.hovertext)
  - Sets text to appear when hovering over this annotation.
* - [name](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Annotation.name)
  - When used in a template, named items are created in the output figure in addition to any items the figure already has in this array.
* - [opacity](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Annotation.opacity)
  - Sets the opacity of the annotation (text + arrow).
* - [showarrow](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Annotation.showarrow)
  - Determines whether or not the annotation is drawn with an arrow.
* - [standoff](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Annotation.standoff)
  - Sets a distance, in pixels, to move the end arrowhead away from the position it is pointing at, for example to point at the edge of a marker independent of zoom.
* - [startarrowhead](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Annotation.startarrowhead)
  - Sets the start annotation arrow head style.
* - [startarrowsize](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Annotation.startarrowsize)
  - Sets the size of the start annotation arrow head, relative to arrow width.
* - [startstandoff](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Annotation.startstandoff)
  - Sets a distance, in pixels, to move the start arrow head away from the position it is pointing at, for example to point at the edge of a marker independent of zoom.
* - [templateitemname](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Annotation.templateitemname)
  - Used to refer to a named item in this array in the template.
* - [textangle](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Annotation.textangle)
  - Sets the angle at which the text is drawn with respect to the horizontal.
* - [text](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Annotation.text)
  - Sets the text associated with this annotation.
* - [valign](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Annotation.valign)
  - Sets the vertical alignment of the text within the box.
* - [visible](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Annotation.visible)
  - Determines whether or not this annotation is visible.
* - [width](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Annotation.width)
  - Sets an explicit width for the text box.
* - [xanchor](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Annotation.xanchor)
  - Sets the text box’s horizontal position anchor. This anchor binds thexposition to the "left", "center" or "right" of the annotation.
* - [xclick](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Annotation.xclick)
  - Toggle this annotation when clicking a data point whosexvalue isxclickrather than the annotation’sxvalue.
* - [xref](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Annotation.xref)
  - Sets the annotation’s _x_ coordinate axis.
* - [xshift](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Annotation.xshift)
  - Shifts the position of the whole annotation and arrow to the right (positive) or left (negative) by this many pixels.
* - [x](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Annotation.x)
  - Sets the annotation’s _x_ position.
* - [yanchor](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Annotation.yanchor)
  - Sets the text box’s vertical position anchor. This anchor binds the y position to the "top", "middle" or "bottom" of the annotation.
* - [yclick](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Annotation.yclick)
  - Toggle this annotation when clicking a data point whose y value is yclick rather than the annotation’s yvalue.
* - [yref](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Annotation.yref)
  - Sets the annotation’s _y_ coordinate axis.
* - [yshift](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Annotation.yshift)
  - Shifts the position of the whole annotation and arrow up (positive) or down (negative) by this many pixels.
* - [y](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Annotation.y)
  - Sets the annotation’s _y_ position.
```

<br/>

### Coloraxis

Clase `Coloraxis`.

```{list-table}
:header-rows: 1

* - Constructor
  - Descripción
* - [go.layout.Coloraxis](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Coloraxis)(arg=None, autocolorscale=None, ...)
  - Maneja el mapeo de valores a colores en gráficos que usan escala de colores.
```

:::{important}
El módulo asociado a esta clase es [layout.coloraxis](https://plotly.com/python-api-reference/generated/plotly.graph_objects.layout.coloraxis.html) y sus submódulos son los siguientes:
- [coloraxis.colorbar](https://plotly.com/python-api-reference/generated/plotly.graph_objects.layout.coloraxis.colorbar.html).
    - [colorbar.title](https://plotly.com/python-api-reference/generated/plotly.graph_objects.layout.coloraxis.colorbar.title.html).
:::

<br/>

#### Atributos de Coloraxis

Atributos de la clase `Coloraxis`.

:::{caution}
Las descripciones de los atributos de esta clase están en inglés.
:::

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - [autocolorscale](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Coloraxis.autocolorscale)
  - Determines whether the colorscale is a default palette (autocolorscale:true) or the palette determined by color scale.
* - [cauto](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Coloraxis.cauto)
  - Determines whether or not the color domain is computed with respect to the input data (here corresponding trace color array(s)) or the bounds set in cmin and cmax Defaults to false when cmin and cmax are set by the user.
* - [cmax](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Coloraxis.cmax)
  - Sets the upper bound of the color domain.
* - [cmid](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Coloraxis.cmid)
  - Sets the mid-point of the color domain by scaling cmin and/or cmax to be equidistant to this point.
* - [cmin](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Coloraxis.cmin)
  - Sets the lower bound of the color domain.
* - [colorbar](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Coloraxis.colorbar)
  - The `colorbar` property is an instance of [ColorBar](https://plotly.com/python-api-reference/generated/plotly.graph_objects.layout.coloraxis.colorbar.html).
* - [colorscale](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Coloraxis.colorscale)
  - Sets the colorscale.
* - [reversescale](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Coloraxis.reversescale)
  - Reverses the color mapping if true.
* - [showscale](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Coloraxis.showscale)
  - Determines whether or not a colorbar is displayed for this trace.
```

<br/>

### Colorscale

Clase `Colorscale`.

```{list-table}
:header-rows: 1

* - Constructor
  - Descripción
* - [go.layout.Colorscale](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Colorscale)(arg=None, diverging=None, ...)
  - Define una escala de colores específica para representar datos en el gráfico.
```

<br/>

#### Atributos de Colorscale

Atributos de la clase `Colorscale`.

:::{caution}
Las descripciones de los atributos de esta clase están en inglés.
:::

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - [diverging](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Colorscale.diverging)
  - Sets the default diverging colorscale.
* - [sequentialminus](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Colorscale.sequentialminus)
  - Sets the default sequential colorscale for negative values.
* - [sequential](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Colorscale.sequential)
  - Sets the default sequential colorscale for positive values.
```

<br/>

### Font

Clase `Font`.

```{list-table}
:header-rows: 1

* - Constructor
  - Descripción
* - [go.layout.Font](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Font)(arg=None, color=None, ...)
  - Define el tipo de fuente, tamaño y color para los textos en el gráfico.
```

<br/>

#### Atributos de Font

Atributos de la clase `Font`.

:::{caution}
Las descripciones de los atributos de esta clase están en inglés.
:::

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - [color](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Font.color)
  - A hex string (e.g. '#ff0000').
* - [family](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Font.family)
  - HTML font family - the typeface that will be applied by the web browser.
* - [lineposition](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Font.lineposition)
  - Sets the kind of decoration line(s) with text, such as an "under", "over" or "through" as well as combinations e.g. "under+over", etc.
* - [shadow](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Font.shadow)
  - Sets the shape and color of the shadow behind text.
* - [size](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Font.size)
  - An `int` or `float` in the interval _[1, inf]_.
* - [style](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Font.style)
  - Sets whether a font should be styled with a normal or italic face from its family.
* - [textcase](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Font.textcase)
  - Sets capitalization of text.
* - [variant](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Font.variant)
  - Sets the variant of the font.
* - [weight](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Font.weight)
  - Sets the weight (or boldness) of the font.
```

<br/>

### Grid

Clase `Grid`.

```{list-table}
:header-rows: 1

* - Constructor
  - Descripción
* - [go.layout.Grid](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Grid)(arg=None, columns=None, ...)
  - Define la disposición de una cuadrícula en el diseño de subgráficos.
```

:::{important}
El módulo asociado a esta clase es [layout.grid](https://plotly.com/python-api-reference/generated/plotly.graph_objects.layout.grid.html).
:::

<br/>

#### Atributos de Grid

Atributos de la clase `Grid`.

:::{caution}
Las descripciones de los atributos de esta clase están en inglés.
:::

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - [columns](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Grid.columns)
  - The number of columns in the grid.
* - [domain](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Grid.domain)
  - The `domain` property is an instance of `Domain`.
* - [pattern](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Grid.pattern)
  - If no subplots, xaxes, or _y_ axes are given but we do have rows and columns, we can generate defaults using consecutive axis IDs.
* - [roworder](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Grid.roworder)
  - Is the first row the top or the bottom? Note that columns are always enumerated from left to right.
* - [rows](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Grid.rows)
  - The number of rows in the grid.
* - [subplots](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Grid.subplots)
  - Used for freeform grids, where some axes may be shared across subplots but others are not.
* - [xaxes](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Grid.xaxes)
  - Used with _y_ axes when the _x_ and _y_ axes are shared across columns and rows.
* - [xgap](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Grid.xgap)
  - Horizontal space between grid cells, expressed as a fraction of the total width available to one cell.
* - [xside](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Grid.xside)
  - Sets where the _x_ axis labels and titles go.
* - [yaxes](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Grid.yaxes)
  - Used with yaxes when the _x_ and _y_ axes are shared across columns and rows.
* - [ygap](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Grid.ygap)
  - Vertical space between grid cells, expressed as a fraction of the total height available to one cell.
* - [yside](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Grid.yside)
  - Sets where the _y_ axis labels and titles go.
```

<br/>

### Legend

Clase `Legend`.

```{list-table}
:header-rows: 1

* - Constructor
  - Descripción
* - [go.layout.Legend](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Legend)(arg=None, bgcolor=None, ...)
  - Configura la apariencia y posición de la leyenda del gráfico.
```

:::{important}
El módulo asociado a esta clase es [layout.legend](https://plotly.com/python-api-reference/generated/plotly.graph_objects.layout.legend.html) y sus submódulos son los siguientes:
- [legend.title](https://plotly.com/python-api-reference/generated/plotly.graph_objects.layout.legend.title.html)
:::


<br/>

#### Atributos de Legend

Atributos de la clase `Legend`.

:::{caution}
Las descripciones de los atributos de esta clase están en inglés.
:::


```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - [bgcolor](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Legend.bgcolor)
  - Sets the legend background color.
* - [bordercolor](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Legend.bordercolor)
  - Sets the color of the border enclosing the legend.
* - [borderwidth](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Legend.borderwidth)
  - Sets the width (in px) of the border enclosing the legend.
* - [entrywidthmode](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Legend.entrywidthmode)
  - Determines what entrywidth means.
* - [entrywidth](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Legend.entrywidth)
  - Sets the width (in px or fraction) of the legend.
* - [font](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Legend.font)
  - Sets the font used to text the legend items.
* - [groupclick](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Legend.groupclick)
  - Determines the behavior on legend group item click.
* - [grouptitlefont](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Legend.grouptitlefont)
  - Sets the font for group titles in legend.
* - [indentation](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Legend.indentation)
  - Sets the indentation (in px) of the legend entries.
* - [itemclick](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Legend.itemclick)
  - Determines the behavior on legend item click.
* - [itemdoubleclick](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Legend.itemdoubleclick)
  - Determines the behavior on legend item double-click.
* - [itemsizing](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Legend.itemsizing)
  - Determines if the legend items symbols scale with their corresponding "trace" attributes or remain "constant" independent of the symbol size on the graph.
* - [itemwidth](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Legend.itemwidth)
  - Sets the width (in px) of the legend item symbols (the part other than the title.
* - [orientation](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Legend.orientation)
  - Sets the orientation of the legend.
* - [title](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Legend.title)
  - The `title` property is an instance of [Title](https://plotly.com/python-api-reference/generated/plotly.graph_objects.layout.legend.title.html).
* - [tracegroupgap](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Legend.tracegroupgap)
  - Sets the amount of vertical space (in px) between legend groups.
* - [traceorder](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Legend.traceorder)
  - Determines the order at which the legend items are displayed.
* - [uirevision](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Legend.uirevision)
  - Controls persistence of legend-driven changes in trace and pie label visibility.
* - [valign](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Legend.valign)
  - Sets the vertical alignment of the symbols with respect to their associated text.
* - [visible](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Legend.visible)
  - Determines whether or not this legend is visible.
* - [xanchor](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Legend.xanchor)
  - Sets the legend’s horizontal position anchor.
* - [xref](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Legend.xref)
  - Sets the container x refers to.
* - [x](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Legend.x)
  - Sets the _x_ position with respect to xref (in normalized coordinates) of the legend.
* - [yanchor](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Legend.yanchor)
  - Sets the legend’s vertical position anchor. This anchor binds theyposition to the "top", "middle" or "bottom" of the legend.
* - [yref](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Legend.yref)
  - Sets the container y refers to.
* - [y](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Legend.y)
  - Sets the _y_ position with respect to yref (in normalized coordinates) of the legend.
```

<br/>

### Selection

Clase `Selection`.

```{list-table}
:header-rows: 1

* - Constructor
  - Descripción
* - [go.layout.Selection](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Selection)(arg=None, line=None, name=None, ...)
  - Define una selección específica dentro del gráfico.
```

:::{important}
El módulo asociado a esta clase es [layout.selection](https://plotly.com/python-api-reference/generated/plotly.graph_objects.layout.selection.html).
:::

<br/>

#### Atributos de Selection

Atributos de la clase `Selection`.

:::{caution}
Las descripciones de los atributos de esta clase están en inglés.
:::

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - [line](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Selection.line)
  - The `line` property is an instance of `Line`.
* - [name](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Selection.name)
  - When used in a template, named items are created in the output figure in addition to any items the figure already has in this array.
* - [opacity](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Selection.opacity)
  - Sets the opacity of the selection.
* - [path](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Selection.path)
  - For type "path" - a valid SVG path similar to shapes.
* - [templateitemname](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Selection.templateitemname)
  - Used to refer to a named item in this array in the template.
* - [type](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Selection.type)
  - Specifies the selection type to be drawn.
* - [x0](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Selection.x0)
  - Sets the selection’s starting _x_ position.
* - [x1](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Selection.x1)
  - Sets the selection’s end _x_ position.
* - [xref](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Selection.xref)
  - Sets the selection’s _x_ coordinate axis.
* - [y0](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Selection.y0)
  - Sets the selection’s starting _y_ position.
* - [y1](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Selection.y1)
  - Sets the selection’s end _y_ position.
* - [yref](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Selection.yref)
  - Sets the selection’s _y_ coordinate axis.
```

<br/>

### Slider

Clase `Slider`.

```{list-table}
:header-rows: 1

* - Constructor
  - Descripción
* - [go.layout.Slider](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Slider)(arg=None, active=None, ...)
  - Configura barras deslizantes para explorar diferentes estados del gráfico.
```

:::{important}
El módulo asociado a esta clase es [layout.slider](https://plotly.com/python-api-reference/generated/plotly.graph_objects.layout.slider.html) y su submódulo es el siguiente:
- [slider.currentvalue](https://plotly.com/python-api-reference/generated/plotly.graph_objects.layout.slider.currentvalue.html).
:::

<br/>

#### Atributos de Slider

Atributos de la clase `Slider`.

:::{caution}
Las descripciones de los atributos de esta clase están en inglés.
:::

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - [activebgcolor](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Slider.activebgcolor)
  - Sets the background color of the slider grip while dragging.
* - [active](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Slider.active)
  - Determines which button (by index starting from 0) is considered active.
* - [bgcolor](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Slider.bgcolor)
  - Sets the background color of the slider.
* - [bordercolor](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Slider.bordercolor)
  - Sets the color of the border enclosing the slider.
* - [borderwidth](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Slider.borderwidth)
  - Sets the width (in px) of the border enclosing the slider.
* - [currentvalue](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Slider.currentvalue)
  - The `currentvalue` property is an instance of [Currentvalue](https://plotly.com/python-api-reference/generated/plotly.graph_objects.layout.slider.currentvalue.html).
* - [font](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Slider.font)
  - Sets the font of the slider step labels.
* - [lenmode](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Slider.lenmode)
  - Determines whether this slider length is set in units of plot "fraction" or in *pixels.
* - [len](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Slider.len)
  - Sets the length of the slider. This measure excludes the padding of both ends.
* - [minorticklen](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Slider.minorticklen)
  - Sets the length in pixels of minor step tick marks.
* - [name](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Slider.name)
  - When used in a template, named items are created in the output figure in addition to any items the figure already has in this array.
* - [pad](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Slider.pad)
  - Set the padding of the slider component along each side.
* - [stepdefaults](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Slider.stepdefaults)
  - When used in a template (as layout.template.layout.slider.stepdefaults) sets the default property values to use for elements of layout.slider.steps.
* - [steps](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Slider.steps)
  - The `steps` property is a `tuple` of instances of `Step`.
* - [templateitemname](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Slider.templateitemname)
  - Used to refer to a named item in this array in the template.
* - [tickcolor](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Slider.tickcolor)
  - Sets the color of the border enclosing the slider.
* - [ticklen](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Slider.ticklen)
  - Sets the length in pixels of step tick marks.
* - [tickwidth](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Slider.tickwidth)
  - Sets the tick width (in px).
* - [transition](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Slider.transition)
  - The `transition` property is an instance of `Transition`.
* - [visible](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Slider.visible)
  - Determines whether or not the slider is visible.
* - [xanchor](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Slider.xanchor)
  - Sets the slider’s horizontal position anchor.
* - [x](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Slider.x)
  - Sets the _x_ position (in normalized coordinates) of the slider.
* - [yanchor](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Slider.yanchor)
  - Sets the slider’s vertical position anchor. This anchor binds theyposition to the "top", "middle" or "bottom" of the range selector.
* - [y](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Slider.y)
  - Sets the _y_ position (in normalized coordinates) of the slider.
```

<br/>

### Title

Clase `Title`.

```{list-table}
:header-rows: 1

* - Constructor
  - Descripción
* - [go.layout.Title](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Title)(arg=None, automargin=None, ...)
  - Especifica las propiedades del título del gráfico.
```

:::{important}
El módulo asociado a esta clase es [layout.title](https://plotly.com/python-api-reference/generated/plotly.graph_objects.layout.title.html) y sus submódulos son los siguientes:
- [title.subtitle](https://plotly.com/python-api-reference/generated/plotly.graph_objects.layout.title.subtitle.html)
:::

<br/>

#### Atributos de Title

Atributos de la clase `Title`.

:::{caution}
Las descripciones de los atributos de esta clase están en inglés.
:::

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - [automargin](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Title.automargin)
  - Determines whether the title can automatically push the figure margins.
* - [font](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Title.font)
  - Sets the title font.
* - [pad](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Title.pad)
  - Sets the padding of the title.
* - [subtitle](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Title.subtitle)
  - The `subtitle` property is an instance of [Subtitle](https://plotly.com/python-api-reference/generated/plotly.graph_objects.layout.title.subtitle.html).
* - [text](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Title.text)
  - Sets the plot’s title.
* - [xanchor](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Title.xanchor)
  - Sets the title’s horizontal alignment with respect to its _x_ position.
* - [xref](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Title.xref)
  - Sets the container _x_ refers to.
* - [x](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Title.x)
  - Sets the _x_ position with respect to _xref_ in normalized coordinates from 0 (left) to 1 (right).
* - [yanchor](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Title.yanchor)
  - Sets the title’s vertical alignment with respect to its _y_ position.
* - [yref](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Title.yref)
  - Sets the container _y_ refers to.
* - [y](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Title.y)
  - Sets the _y_ position with respect to _yref_ in normalized coordinates from 0 (bottom) to 1 (top).
```

<br/>

### Updatemenu

Clase `Updatemenu`.

```{list-table}
:header-rows: 1

* - Constructor
  - Descripción
* - [go.layout.Updatemenu](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Updatemenu)(arg=None, active=None, ...)
  - Agrega menús interactivos para actualizar la visualización de datos.
```

:::{important}
El módulo asociado a esta clase es [layout.updatemenu](https://plotly.com/python-api-reference/generated/plotly.graph_objects.layout.updatemenu.html).
:::

<br/>

#### Atributos de Updatemenu

Atributos de la clase `Updatemenu`.

:::{caution}
Las descripciones de los atributos de esta clase están en inglés.
:::

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - [active](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Updatemenu.active)
  - Determines which button (by index starting from 0) is considered active.
* - [bgcolor](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Updatemenu.bgcolor)
  - Sets the background color of the update menu buttons.
* - [bordercolor](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Updatemenu.bordercolor)
  - Sets the color of the border enclosing the update menu.
* - [borderwidth](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Updatemenu.borderwidth)
  - Sets the width (in px) of the border enclosing the update menu.
* - [buttondefaults](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Updatemenu.buttondefaults)
  - When used in a template (as _layout.template.layout.updatemenu.buttondefaults_), sets the default property values to use for elements of _layout.updatemenu.buttons_.
* - [buttons](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Updatemenu.buttons)
  - The `buttons` property is a `tuple` of instances of `Button`.
* - [direction](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Updatemenu.direction)
  - Determines the direction in which the buttons are laid out, whether in a dropdown menu or a row/column of buttons.
* - [font](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Updatemenu.font)
  - Sets the font of the update menu button text.
* - [name](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Updatemenu.name)
  - When used in a template, named items are created in the output figure in addition to any items the figure already has in this array.
* - [pad](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Updatemenu.pad)
  - Sets the padding around the buttons or dropdown menu.
* - [showactive](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Updatemenu.showactive)
  - Highlights active dropdown item or active button if true.
* - [templateitemname](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Updatemenu.templateitemname)
  - Used to refer to a named item in this array in the template.
* - [type](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Updatemenu.type)
  - Determines whether the buttons are accessible via a dropdown menu or whether the buttons are stacked horizontally or vertically.
* - [visible](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Updatemenu.visible)
  - Determines whether or not the update menu is visible.
* - [xanchor](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Updatemenu.xanchor)
  - Sets the update menu’s horizontal position anchor.
* - [x](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Updatemenu.x)
  - Sets the _x_ position (in normalized coordinates) of the update menu.
* - [yanchor](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Updatemenu.yanchor)
  - Sets the update menu’s vertical position anchor. This anchor binds theyposition to the "top", "middle" or "bottom" of the range selector.
* - [y](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.Updatemenu.y)
  - Sets the _y_ position (in normalized coordinates) of the update menu.

```

<br/>

### XAxis

Clase `XAxis`.

```{list-table}
:header-rows: 1

* - Constructor
  - Descripción
* - [go.layout.XAxis](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.XAxis)(arg=None, anchor=None, ...)
  - Configura el eje _x_ del gráfico (etiquetas, rango, escala, etc.).
```

:::{important}
El módulo asociado a esta clase es [layout.xaxis](https://plotly.com/python-api-reference/generated/plotly.graph_objects.layout.xaxis.html) y sus submódulos son los siguientes:
- [xaxis.rangeselector](https://plotly.com/python-api-reference/generated/plotly.graph_objects.layout.xaxis.rangeselector.html).
- [xaxis.rangeslider](https://plotly.com/python-api-reference/generated/plotly.graph_objects.layout.xaxis.rangeslider.html).
- [xaxis.title](https://plotly.com/python-api-reference/generated/plotly.graph_objects.layout.xaxis.title.html)
:::

<br/>

#### Atributos de XAxis

Atributos de la clase `XAxis`.

:::{caution}
Las descripciones de los atributos de esta clase están en inglés.
:::

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - [anchor](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.XAxis.anchor)
  - If set to an opposite-letter axis id (e.g. _x2_, _y_), this axis is bound to the corresponding opposite-letter axis.
* - [automargin](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.XAxis.automargin)
  - Determines whether long tick labels automatically grow the figure margins.
* - [autorangeoptions](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.XAxis.autorangeoptions)
  - The `autorangeoptions` property is an instance of `Autorangeoptions`.
* - [autorange](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.XAxis.autorange)
  - Determines whether or not the range of this axis is computed in relation to the input data.
* - [autotickangles](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.XAxis.autotickangles)
  - When _tickangle_ is set to "auto", it will be set to the first angle in this array that is large enough to prevent label overlap.
* - [autotypenumbers](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.XAxis.autotypenumbers)
  - Using "strict" a numeric string in trace data is not converted to a number.
* - [calendar](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.XAxis.calendar)
  - Sets the calendar system to use for _range_ and _tick0_ if this is a date axis.
* - [categoryarraysrc](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.XAxis.categoryarraysrc)
  - Sets the source reference on Chart Studio Cloud for _categoryarray_.
* - [categoryarray](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.XAxis.categoryarray)
  - Sets the order in which categories on this axis appear.
* - [categoryorder](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.XAxis.categoryorder)
  - Specifies the ordering logic for the case of categorical variables.
* - [color](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.XAxis.color)
  - Sets default for all colors associated with this axis all at once: line, font, tick, and grid colors.
* - [constraintoward](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.XAxis.constraintoward)
  - If this axis needs to be compressed (either due to its own _scaleanchor_ and _scaleratio_ or those of the other axis), determines which direction we push the originally specified plot area.
* - [constrain](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.XAxis.constrain)
  - If this axis needs to be compressed (either due to its own _scaleanchor_ and _scaleratio_ or those of the other axis), determines how that happens: by increasing the "range", or by decreasing the "domain".
* - [dividercolor](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.XAxis.dividercolor)
  - Sets the color of the dividers. Only has an effect on "multicategory" axes.
* - [dividerwidth](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.XAxis.dividerwidth)
  - Sets the width (in px) of the dividers. Only has an effect on "multicategory" axes.
* - [domain](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.XAxis.domain)
  - Sets the domain of this axis (in plot fraction).
* - [dtick](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.XAxis.dtick)
  - Sets the step in-between ticks on this axis.
* - [exponentformat](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.XAxis.exponentformat)
  - Determines a formatting rule for the tick exponents.
* - [fixedrange](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.XAxis.fixedrange)
  - Determines whether or not this axis is zoom-able.
* - [gridcolor](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.XAxis.gridcolor)
  - Sets the color of the grid lines.
* - [griddash](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.XAxis.griddash)
  - Sets the dash style of lines.
* - [gridwidth](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.XAxis.gridwidth)
  - Sets the width (in px) of the grid lines.
* - [hoverformat](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.XAxis.hoverformat)
  - Sets the hover text formatting rule using d3 formatting mini-languages which are very similar to those in Python.
* - [insiderange](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.XAxis.insiderange)
  - Could be used to set the desired inside range of this axis
* - [labelalias](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.XAxis.labelalias)
  - Replacement text for specific tick or hover labels.
* - [layer](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.XAxis.layer)
  - Sets the layer on which this axis is displayed.
* - [linecolor](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.XAxis.linecolor)
  - Sets the axis line color.
* - [linewidth](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.XAxis.linewidth)
  - Sets the width (in px) of the axis line.
* - [matches](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.XAxis.matches)
  - If set to another axis id (e.g. _x2_, _y_), the range of this axis will match the range of the corresponding axis in data-coordinates space.
* - [maxallowed](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.XAxis.maxallowed)
  - Determines the maximum range of this axis.
* - [minallowed](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.XAxis.minallowed)
  - Determines the minimum range of this axis.
* - [minexponent](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.XAxis.minexponent)
  - Hide SI prefix for 10^n if|n|is below this number.
* - [minor](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.XAxis.minor)
  - The `minor` property is an instance of `Minor`.
* - [mirror](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.XAxis.mirror)
  - Determines if the axis lines or/and ticks are mirrored to the opposite side of the plotting area.
* - [nticks](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.XAxis.nticks)
  - Specifies the maximum number of ticks for the particular axis.
* - [overlaying](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.XAxis.overlaying)
  - If set a same-letter axis id, this axis is overlaid on top of the corresponding same-letter axis, with traces and axes visible for both axes.
* - [position](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.XAxis.position)
  - Sets the position of this axis in the plotting space (in normalized coordinates).
* - [rangebreakdefaults](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.XAxis.rangebreakdefaults)
  - When used in a template (as _layout.template.layout.xaxis.rangebreakdefaults_), sets the default property values to use for elements of _layout.xaxis.rangebreaks_.
* - [rangebreaks](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.XAxis.rangebreaks)
  - The `rangebreaks` property is a `tuple` of instances of `Rangebreak`.
* - [rangemode](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.XAxis.rangemode)
  - If "normal", the range is computed in relation to the extrema of the input data.
* - [rangeselector](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.XAxis.rangeselector)
  - The `rangeselector` property is an instance of [Rangeselector](https://plotly.com/python-api-reference/generated/plotly.graph_objects.layout.xaxis.rangeselector.html).
* - [rangeslider](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.XAxis.rangeslider)
  - The `rangeslider` property is an instance of [Rangeslider](https://plotly.com/python-api-reference/generated/plotly.graph_objects.layout.xaxis.rangeslider.html).
* - [range](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.XAxis.range)
  - Sets the range of this axis
* - [scaleanchor](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.XAxis.scaleanchor)
  - If set to another axis id (e.g. _x2_, _y_), the range of this axis changes together with the range of the corresponding axis such that the scale of pixels per unit is in a constant ratio.
* - [scaleratio](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.XAxis.scaleratio)
  - If this axis is linked to another by _scaleanchor_, this determines the pixel to unit scale ratio.
* - [separatethousands](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.XAxis.separatethousands)
  - If "true", even 4-digit integers are separated.
* - [showdividers](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.XAxis.showdividers)
  - Determines whether or not a dividers are drawn between the category levels of this axis.
* - [showexponent](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.XAxis.showexponent)
  - If "all", all exponents are shown besides their significands.
* - [showgrid](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.XAxis.showgrid)
  - Determines whether or not grid lines are drawn.
* - [showline](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.XAxis.showline)
  - Determines whether or not a line bounding this axis is drawn.
* - [showspikes](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.XAxis.showspikes)
  - Determines whether or not spikes (aka droplines) are drawn for this axis.
* - [showticklabels](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.XAxis.showticklabels)
  - Determines whether or not the tick labels are drawn.
* - [showtickprefix](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.XAxis.showtickprefix)
  - If "all", all tick labels are displayed with a prefix.
* - [showticksuffix](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.XAxis.showticksuffix)
  - Same as _showtickprefix_ but for tick suffixes.
* - [side](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.XAxis.side)
  - Determines whether a _x_ (y) axis is positioned at the "bottom" ("left") or "top" ("right") of the plotting area.
* - [spikecolor](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.XAxis.spikecolor)
  - Sets the spike color.
* - [spikedash](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.XAxis.spikedash)
  - Sets the dash style of lines.
* - [spikemode](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.XAxis.spikemode)
  - Determines the drawing mode for the spike line. If "toaxis", the line is drawn from the data point to the axis the series is plotted on.
* - [spikesnap](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.XAxis.spikesnap)
  - Determines whether _spikelines_ are stuck to the cursor or to the closest datapoints.
* - [spikethickness](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.XAxis.spikethickness)
  - Sets the width (in px) of the zero line.
* - [tick0](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.XAxis.tick0)
  - Sets the placement of the first tick on this axis.
* - [tickangle](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.XAxis.tickangle)
  - Sets the angle of the tick labels with respect to the horizontal.
* - [tickcolor](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.XAxis.tickcolor)
  - Sets the tick color.
* - [tickfont](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.XAxis.tickfont)
  - Sets the tick font.
* - [tickformatstopdefaults](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.XAxis.tickformatstopdefaults)
  - When used in a template (as _layout.template.layout.xaxis.tickformatstopdefaults_), sets the default property values to use for elements of _layout.xaxis.tickformatstops_.
* - [tickformatstops](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.XAxis.tickformatstops)
  - The `tickformatstops` property is a `tuple` of instances of `Tickformatstop`.
* - [tickformat](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.XAxis.tickformat)
  - Sets the tick label formatting rule using d3 formatting mini- languages which are very similar to those in Python.
* - [ticklabelindexsrc](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.XAxis.ticklabelindexsrc)
  - Sets the source reference on Chart Studio Cloud for _ticklabelindex_.
* - [ticklabelindex](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.XAxis.ticklabelindex)
  - Only for axes with type "date" or "linear".
* - [ticklabelmode](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.XAxis.ticklabelmode)
  - Determines where tick labels are drawn with respect to their corresponding ticks and grid lines.
* - [ticklabeloverflow](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.XAxis.ticklabeloverflow)
  - Determines how we handle tick labels that would overflow either the graph div or the domain of the axis.
* - [ticklabelposition](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.XAxis.ticklabelposition)
  - Determines where tick labels are drawn with respect to the axis. Please note that top or bottom has no effect on _x_ axes or when _ticklabelmode_ is set to "period".
* - [ticklabelshift](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.XAxis.ticklabelshift)
  - Shifts the tick labels by the specified number of pixels in parallel to the axis.
* - [ticklabelstandoff](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.XAxis.ticklabelstandoff)
  - Sets the standoff distance (in px) between the axis tick labels and their default position.
* - [ticklabelstep](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.XAxis.ticklabelstep)
  - Sets the spacing between tick labels as compared to the spacing between ticks.
* - [ticklen](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.XAxis.ticklen)
  - Sets the tick length (in px).
* - [tickmode](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.XAxis.tickmode)
  - Sets the tick mode for this axis.
* - [tickprefix](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.XAxis.tickprefix)
  - Sets a tick label prefix.
* - [tickson](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.XAxis.tickson)
  - Determines where ticks and grid lines are drawn with respect to their corresponding tick labels.
* - [ticksuffix](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.XAxis.ticksuffix)
  - Sets a tick label suffix.
* - [ticks](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.XAxis.ticks)
  - Determines whether ticks are drawn or not.
* - [ticktextsrc](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.XAxis.ticktextsrc)
  - Sets the source reference on Chart Studio Cloud for _ticktext_.
* - [ticktext](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.XAxis.ticktext)
  - Sets the text displayed at the ticks position via _tickvals_.
* - [tickvalssrc](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.XAxis.tickvalssrc)
  - Sets the source reference on Chart Studio Cloud for _tickvals_.
* - [tickvals](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.XAxis.tickvals)
  - Sets the values at which ticks on this axis appear.
* - [tickwidth](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.XAxis.tickwidth)
  - Sets the tick width (in px).
* - [title](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.XAxis.title)
  - The `title` property is an instance of [Title](https://plotly.com/python-api-reference/generated/plotly.graph_objects.layout.xaxis.title.html).
* - [type](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.XAxis.type)
  - Sets the axis type.
* - [uirevision](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.XAxis.uirevision)
  - Controls persistence of user-driven changes in axis _range_, _autorange_, and _title_ if `ineditable:trueconfiguration`.
* - [visible](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.XAxis.visible)
  - A single toggle to hide the axis while preserving interaction like dragging.
* - [zerolinecolor](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.XAxis.zerolinecolor)
  - Sets the line color of the zero line.
* - [zerolinewidth](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.XAxis.zerolinewidth)
  - Sets the width (in px) of the zero line.
* - [zeroline](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.XAxis.zeroline)
  - Determines whether or not a line is drawn at along the 0 value of this axis.
```

<br/>

### YAxis

Clase `YAxis`.

```{list-table}
:header-rows: 1

* - Constructor
  - Descripción
* - [go.layout.YAxis](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.YAxis)(arg=None, anchor=None, ...)
  - Configura el eje Y del gráfico.
```

:::{important}
El módulo asociado a esta clase es [layout.yaxis](https://plotly.com/python-api-reference/generated/plotly.graph_objects.layout.yaxis.html) y sus submódulos son los siguientes:
- [yaxis.title](https://plotly.com/python-api-reference/generated/plotly.graph_objects.layout.yaxis.title.html)
:::

<br/>

#### Atributos de YAxis

Atributos de la clase ``.

:::{caution}
Las descripciones de los atributos de esta clase están en inglés.
:::

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - [anchor](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.YAxis.anchor)
  - If set to an opposite-letter axis id (e.g. _x2_, _y_), this axis is bound to the corresponding opposite-letter axis.
* - [automargin](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.YAxis.automargin)
  - Determines whether long tick labels automatically grow the figure margins.
* - [autorangeoptions](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.YAxis.autorangeoptions)
  - The `autorangeoptions` property is an instance of `Autorangeoptions`.
* - [autorange](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.YAxis.autorange)
  - Determines whether or not the range of this axis is computed in relation to the input data.
* - [autoshift](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.YAxis.autoshift)
  - Automatically reposition the axis to avoid overlap with other axes with the same _overlaying_ value.
* - [autotickangles](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.YAxis.autotickangles)
  - When _tickangle_ is set to "auto", it will be set to the first angle in this array that is large enough to prevent label overlap.
* - [autotypenumbers](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.YAxis.autotypenumbers)
  - Using "strict" a numeric string in trace data is not converted to a number.
* - [calendar](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.YAxis.calendar)
  - Sets the calendar system to use forrangeandtick0if this is a date axis.
* - [categoryarraysrc](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.YAxis.categoryarraysrc)
  - Sets the source reference on Chart Studio Cloud for _categoryarray_.
* - [categoryarray](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.YAxis.categoryarray)
  - Sets the order in which categories on this axis appear.
* - [categoryorder](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.YAxis.categoryorder)
  - Specifies the ordering logic for the case of categorical variables.
* - [color](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.YAxis.color)
  - Sets default for all colors associated with this axis all at once: line, font, tick, and grid colors.
* - [constraintoward](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.YAxis.constraintoward)
  - If this axis needs to be compressed (either due to its own _scaleanchor_ and _scaleratio_ or those of the other axis), determines which direction we push the originally specified plot area.
* - [constrain](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.YAxis.constrain)
  - If this axis needs to be compressed (either due to its own _scaleanchor_ and _scaleratio_ or those of the other axis), determines how that happens: by increasing the "range", or by decreasing the "domain".
* - [dividercolor](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.YAxis.dividercolor)
  - Sets the color of the dividers Only has an effect on "multicategory" axes.
* - [dividerwidth](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.YAxis.dividerwidth)
  - Sets the width (in px) of the dividers Only has an effect on "multicategory" axes.
* - [domain](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.YAxis.domain)
  - Sets the domain of this axis (in plot fraction).
* - [dtick](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.YAxis.dtick)
  - Sets the step in-between ticks on this axis.
* - [exponentformat](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.YAxis.exponentformat)
  - Determines a formatting rule for the tick exponents.
* - [fixedrange](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.YAxis.fixedrange)
  - Determines whether or not this axis is zoom-able.
* - [gridcolor](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.YAxis.gridcolor)
  - Sets the color of the grid lines.
* - [griddash](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.YAxis.griddash)
  - Sets the dash style of lines.
* - [gridwidth](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.YAxis.gridwidth)
  - Sets the width (in px) of the grid lines.
* - [hoverformat](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.YAxis.hoverformat)
  - Sets the hover text formatting rule using d3 formatting mini-languages which are very similar to those in Python.
* - [insiderange](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.YAxis.insiderange)
  - Could be used to set the desired inside range of this axis
* - [labelalias](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.YAxis.labelalias)
  - Replacement text for specific tick or hover labels.
* - [layer](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.YAxis.layer)
  - Sets the layer on which this axis is displayed.
* - [linecolor](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.YAxis.linecolor)
  - Sets the axis line color.
* - [linewidth](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.YAxis.linewidth)
  - Sets the width (in px) of the axis line.
* - [matches](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.YAxis.matches)
  - If set to another axis id (e.g. _x2_, _y_), the range of this axis will match the range of the corresponding axis in data-coordinates space.
* - [maxallowed](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.YAxis.maxallowed)
  - Determines the maximum range of this axis.
* - [minallowed](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.YAxis.minallowed)
  - Determines the minimum range of this axis.
* - [minexponent](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.YAxis.minexponent)
  - Hide SI prefix for 10^n if|n|is below this number.
* - [minor](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.YAxis.minor)
  - The `minor` property is an instance of `Minor`.
* - [mirror](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.YAxis.mirror)
  - Determines if the axis lines or/and ticks are mirrored to the opposite side of the plotting area.
* - [nticks](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.YAxis.nticks)
  - Specifies the maximum number of ticks for the particular axis.
* - [overlaying](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.YAxis.overlaying)
  - If set a same-letter axis id, this axis is overlaid on top of the corresponding same-letter axis, with traces and axes visible for both axes.
* - [position](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.YAxis.position)
  - Sets the position of this axis in the plotting space (in normalized coordinates).
* - [rangebreakdefaults](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.YAxis.rangebreakdefaults)
  - When used in a template (as _layout.template.layout.yaxis.rangebreakdefaults_), sets the default property values to use for elements of _layout.yaxis.rangebreaks_.
* - [rangebreaks](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.YAxis.rangebreaks)
  - The `rangebreaks` property is a `tuple` of instances of `Rangebreak`.
* - [rangemode](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.YAxis.rangemode)
  - If "normal", the range is computed in relation to the extrema of the input data.
* - [range](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.YAxis.range)
  - Sets the range of this axis
* - [scaleanchor](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.YAxis.scaleanchor)
  - If set to another axis id (e.g. _x2_, _y_), the range of this axis changes together with the range of the corresponding axis such that the scale of pixels per unit is in a constant ratio.
* - [scaleratio](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.YAxis.scaleratio)
  - If this axis is linked to another by _scaleanchor_, this determines the pixel to unit scale ratio.
* - [separatethousands](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.YAxis.separatethousands)
  - If "true", even 4-digit integers are separated.
* - [shift](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.YAxis.shift)
  - Moves the axis a given number of pixels from where it would have been otherwise.
* - [showdividers](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.YAxis.showdividers)
  - Determines whether or not a dividers are drawn between the category levels of this axis.
* - [showexponent](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.YAxis.showexponent)
  - If "all", all exponents are shown besides their significands.
* - [showgrid](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.YAxis.showgrid)
  - Determines whether or not grid lines are drawn.
* - [showline](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.YAxis.showline)
  - Determines whether or not a line bounding this axis is drawn.
* - [showspikes](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.YAxis.showspikes)
  - Determines whether or not spikes (aka droplines) are drawn for this axis.
* - [showticklabels](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.YAxis.showticklabels)
  - Determines whether or not the tick labels are drawn.
* - [showtickprefix](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.YAxis.showtickprefix)
  - If "all", all tick labels are displayed with a prefix.
* - [showticksuffix](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.YAxis.showticksuffix)
  - Same as _showtickprefix_ but for tick suffixes.
* - [side](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.YAxis.side)
  - Determines whether a _x_ (y) axis is positioned at the "bottom" ("left") or "top" ("right") of the plotting area.
* - [spikecolor](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.YAxis.spikecolor)
  - Sets the spike color.
* - [spikedash](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.YAxis.spikedash)
  - Sets the dash style of lines.
* - [spikemode](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.YAxis.spikemode)
  - Determines the drawing mode for the spike line. If "toaxis", the line is drawn from the data point to the axis the series is plotted on.
* - [spikesnap](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.YAxis.spikesnap)
  - Determines whether _spikelines_ are stuck to the cursor or to the closest datapoints.
* - [spikethickness](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.YAxis.spikethickness)
  - Sets the width (in px) of the zero line.
* - [tick0](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.YAxis.tick0)
  - Sets the placement of the first tick on this axis.
* - [tickangle](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.YAxis.tickangle)
  - Sets the angle of the tick labels with respect to the horizontal.
* - [tickcolor](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.YAxis.tickcolor)
  - Sets the tick color.
* - [tickfont](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.YAxis.tickfont)
  - Sets the tick font.
* - [tickformatstopdefaults](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.YAxis.tickformatstopdefaults)
  - When used in a template (as _layout.template.layout.yaxis.tickformatstopdefaults_), sets the default property values to use for elements of _layout.yaxis.tickformatstops_.
* - [tickformatstops](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.YAxis.tickformatstops)
  - The `tickformatstops` property is a `tuple` of instances of `Tickformatstop`.
* - [tickformat](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.YAxis.tickformat)
  - Sets the tick label formatting rule using d3 formatting mini-languages which are very similar to those in Python.
* - [ticklabelindexsrc](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.YAxis.ticklabelindexsrc)
  - Sets the source reference on Chart Studio Cloud _ticklabelindex_.
* - [ticklabelindex](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.YAxis.ticklabelindex)
  - Only for axes with type "date" or "linear".
* - [ticklabelmode](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.YAxis.ticklabelmode)
  - Determines where tick labels are drawn with respect to their corresponding ticks and grid lines.
* - [ticklabeloverflow](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.YAxis.ticklabeloverflow)
  - Determines how we handle tick labels that would overflow either the graph div or the domain of the axis.
* - [ticklabelposition](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.YAxis.ticklabelposition)
  - Determines where tick labels are drawn with respect to the axis. Please note that top or bottom has no effect on _x_ axes or when _ticklabelmode_ is set to "period".
* - [ticklabelshift](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.YAxis.ticklabelshift)
  - Shifts the tick labels by the specified number of pixels in parallel to the axis.
* - [ticklabelstandoff](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.YAxis.ticklabelstandoff)
  - Sets the standoff distance (in px) between the axis tick labels and their default position.
* - [ticklabelstep](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.YAxis.ticklabelstep)
  - Sets the spacing between tick labels as compared to the spacing between ticks.
* - [ticklen](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.YAxis.ticklen)
  - Sets the tick length (in px).
* - [tickmode](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.YAxis.tickmode)
  - Sets the tick mode for this axis.
* - [tickprefix](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.YAxis.tickprefix)
  - Sets a tick label prefix.
* - [tickson](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.YAxis.tickson)
  - Determines where ticks and grid lines are drawn with respect to their corresponding tick labels.
* - [ticksuffix](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.YAxis.ticksuffix)
  - Sets a tick label suffix.
* - [ticks](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.YAxis.ticks)
  - Determines whether ticks are drawn or not.
* - [ticktextsrc](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.YAxis.ticktextsrc)
  - Sets the source reference on Chart Studio Cloud _ticktext_.
* - [ticktext](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.YAxis.ticktext)
  - Sets the text displayed at the ticks position via _tickvals_.
* - [tickvalssrc](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.YAxis.tickvalssrc)
  - Sets the source reference on Chart Studio Cloud for _tickvals_.
* - [tickvals](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.YAxis.tickvals)
  - Sets the values at which ticks on this axis appear.
* - [tickwidth](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.YAxis.tickwidth)
  - Sets the tick width (in px).
* - [title](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.YAxis.title)
  - The `title` property is an instance of [Title](https://plotly.com/python-api-reference/generated/plotly.graph_objects.layout.yaxis.title.html).
* - [type](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.YAxis.type)
  - Sets the axis type.
* - [uirevision](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.YAxis.uirevision)
  - Controls persistence of user-driven changes in axis _range_, _autorange_, and _title_ if `ineditable:trueconfiguration`.
* - [visible](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.YAxis.visible)
  - A single toggle to hide the axis while preserving interaction like dragging.
* - [zerolinecolor](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.YAxis.zerolinecolor)
  - Sets the line color of the zero line.
* - [zerolinewidth](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.YAxis.zerolinewidth)
  - Sets the width (in px) of the zero line.
* - [zeroline](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html#plotly.graph_objects.layout.YAxis.zeroline)
  - Determines whether or not a line is drawn at along the 0 value of this axis.
```