# Plotting

La API _bokeh.plotting_ es la interfaz principal de _Bokeh_ y permite relacionar _glyphs_ con datos. Reúne automáticamente gráficos con elementos predeterminados, como ejes, cuadrículas y herramientas. Proporciona herramientas para crear gráficos interactivos, como figuras, mapas y gráficos de contorno. En esta sección únicamente se revisa la clase `figure`. Es necesario importarla.

```python
# importar figure
from bokeh.plotting import figure
```

Aparte de _figure_ existen las siguientes funcionalidades en este módulo:

| Sección          | Descripción                                                                                   |
|------------------|-----------------------------------------------------------------------------------------------|
| [contour](https://docs.bokeh.org/en/latest/docs/reference/plotting/contour.html)      | Herramientas para crear gráficos de contorno, útiles para visualizar datos en 3D o mapas de densidad. |
| [gmap](https://docs.bokeh.org/en/latest/docs/reference/plotting/gmap.html)         | Funcionalidades para integrar mapas de Google Maps en visualizaciones interactivas.            |
| [figure](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html)       | Clase principal para crear figuras y gráficos personalizados, como líneas, barras y dispersiones. |
| [helpers](https://docs.bokeh.org/en/latest/docs/reference/plotting/helpers.html)      | Funciones auxiliares para personalizar y mejorar visualizaciones, como añadir herramientas o leyendas. |

Para más información dirigirse a la documentación en el link del nombre de cada sección.

<br/>

## figure

Es una subclase de [Plot](https://docs.bokeh.org/en/latest/docs/reference/models/plots.html#bokeh.models.Plot), es la clase principal para crear figuras y gráficos personalizados, como líneas, barras y dispersiones.

```{list-table}
:header-rows: 1

* - Constructor
  - Descripción
* - [figure](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure)(*args: Any, id: ID | None = None, **kwargs: Any)
  - Crea una nueva figura para graficar.
```
**Parámetros:**
- **x_axis_label** - `str`: Etiqueta del eje _X_.
- **y_axis_label** - `str`: Etiqueta del eje _Y_.
- **title** - `str`: Título de la figura.
- **x_range** - `array-like`: Rango del eje _X_ o valores en caso de ser datos categóricos.
- **y_range** - `array-like`: Rango del eje _Y_ o valores en caso de ser datos categóricos.
- **x_axis_type** - {'auto', 'linear', 'log', 'datetime', 'mercator'}: Tipo de eje _X_.
- **y_axis_type** - {'auto', 'linear', 'log', 'datetime', 'mercator'}: Tipo de eje _Y_.
- **tools** - `str` o `list-like` de `str` o `Tool`: Herramientas que tendrá la gráfica al inicializarse. Los nombres son los que aparecen entre paréntesis en la sección _tools_ de `Models`. Al especificarse este argumento se borran las _tools_ que vienen por default, para mantenerlos y agregar más _tools_ usar el método `.add_tools()` de `figure`.
- **tooltips** - `Template`, `str` o `list` de `2-tuple`: Para configurar los _tooltips_ de la gráfica. Son tuples _('Name', field)_ donde _Name_ es el nombre del _tooltip_, un nombre arbitrario y _field_ empieza con '_@_', que es una columna de _source_, por ejemplo '_@temp_' buscaría la columna '_temp_' en _source_ (argumento de los glyphs (gráficas)).
- **width**, **height** - `int`: Ancho y alto de la figura en pixeles.
- Para más atributos revisar la lista de atributos de esta clase.

**Retorna:**
- `figure`.

### Atributos

Atributos de la clase `figure`. Todos estos atributos se pueden usar como parámetros del constructor `figure()`.

:::{warning}
Las descripciones de los atributos en esta sección están en inglés.
:::

```{list-table}
:header-rows: 1

* - attribute
  - Descripción
* - [above](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.above)
  - A `list` of renderers to occupy the area above of the plot.
* - [align](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.align)
  - The alignment point within the parent container.
* - [aspect_ratio](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.aspect_ratio)
  - Describes the proportional relationship between component’s width and height.
* - [aspect_scale](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.aspect_scale)
  - A value to be given for increased aspect ratio control.
* - [attribution](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.attribution)
  - Allows to acknowledge or give credit to data, tile, etc. providers.
* - [background_fill_alpha](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.background_fill_alpha)
  - The fill alpha for the plot background style.
* - [background_fill_color](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.background_fill_color)
  - The fill color for the plot background style.
* - [below](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.below)
  - A `list` of renderers to occupy the area below of the plot.
* - [border_fill_alpha](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.border_fill_alpha)
  - The fill alpha for the plot border style.
* - [border_fill_color](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.border_fill_color)
  - The fill color for the plot border style.
* - [center](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.center)
  - A `list` of renderers to occupy the center area (frame) of the plot.
* - [context_menu](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.context_menu)
  - A menu to display when user right clicks on the component.
* - [css_classes](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.css_classes)
  - A `list` of additional CSS classes to add to the underlying DOM element.
* - [css_variables](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.css_variables)
  - Allows to define dynamically computed CSS variables.
* - [disabled](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.disabled)
  - Whether the widget will be disabled when rendered.
* - [elements](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.elements)
  - A collection of DOM-based UI elements attached to this pane.
* - [extra_x_ranges](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.extra_x_ranges)
  - Additional named ranges to make available for mapping x-coordinates.
* - [extra_x_scales](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.extra_x_scales)
  - Additional named scales to make available for mapping x-coordinates.
* - [extra_y_ranges](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.extra_y_ranges)
  - Additional named ranges to make available for mapping y-coordinates.
* - [extra_y_scales](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.extra_y_scales)
  - Additional named scales to make available for mapping y-coordinates.
* - [flow_mode](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.flow_mode)
  - Defines whether the layout will flow in the block or inline dimension.
* - [frame_align](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.frame_align)
  - Allows to specify which frame edges to align in multiple-plot layouts.
* - [frame_height](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.frame_height)
  - The height of a plot frame or the inner height of a plot, excluding any axes, titles, border padding, etc.
* - [frame_width](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.frame_width)
  - The width of a plot frame or the inner width of a plot, excluding any axes, titles, border padding, etc.
* - [height](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.height)
  - The height of the component (in pixels).
* - [height_policy](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.height_policy)
  - Describes how the component should maintain its height.
* - [hidpi](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.hidpi)
  - Whether to use HiDPI mode when available.
* - [hold_render](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.hold_render)
  - When set to `True` all requests to repaint the plot will be hold off.
* - [inner_height](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.inner_height)
  - This is the exact height of the plotting canvas, i.e. the height of the actual plot, without toolbars etc. 
* - [inner_width](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.inner_width)
  - This is the exact width of the plotting canvas, i.e. the width of the actual plot, without toolbars etc.
* - [left](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.left)
  - A `list` of renderers to occupy the area to the left of the plot.
* - [lod_factor](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.lod_factor)
  - Decimation factor to use when applying level-of-detail decimation.
* - [lod_interval](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.lod_interval)
  - Interval (in ms) during which an interactive tool event will enable level-of-detail downsampling.
* - [lod_threshold](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.lod_threshold)
  - A number of data points, above which level-of-detail downsampling may be performed by glyph renderers. 
* - [lod_timeout](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.lod_timeout)
  - Timeout (in ms) for checking whether interactive tool events are still occurring. 
* - [margin](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.margin)
  - Allows to create additional space around the component. 
* - [match_aspect](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.match_aspect)
  - Specify the aspect ratio behavior of the plot. Aspect ratio is defined as the ratio of width over height.
* - [max_height](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.max_height)
  - Maximal height of the component (in pixels) if height is adjustable.
* - [max_width](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.max_width)
  - Maximal width of the component (in pixels) if width is adjustable.
* - [min_border](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.min_border)
  - A convenience property to set all all the min_border_X properties to the same value.
* - [min_border_bottom](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.min_border_bottom)
  - Minimum size in pixels of the padding region below the bottom of the central plot region.
* - [min_border_left](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.min_border_left)
  - Minimum size in pixels of the padding region to the left of the central plot region.
* - [min_border_right](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.min_border_right)
  - Minimum size in pixels of the padding region to the right of the central plot region.
* - [min_border_top](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.min_border_top)
  - Minimum size in pixels of the padding region above the top of the central plot region.
* - [min_height](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.min_height)
  - Minimal height of the component (in pixels) if height is adjustable.
* - [min_width](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.min_width)
  - Minimal width of the component (in pixels) if width is adjustable.
* - [name](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.name)
  - An arbitrary, user-supplied name for this model.
* - [outer_height](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.outer_height)
  - This is the exact height of the layout, i.e. the height of the actual plot, with toolbars etc. 
* - [outer_width](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.outer_width)
  - This is the exact width of the layout, i.e. the height of the actual plot, with toolbars etc. 
* - [outline_line_alpha](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.outline_line_alpha)
  - The line alpha for the plot border outline.
* - [outline_line_cap](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.outline_line_cap)
  - The line cap for the plot border outline.
* - [outline_line_color](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.outline_line_color)
  - The line color for the plot border outline.
* - [outline_line_dash](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.outline_line_dash)
  - The line dash for the plot border outline.
* - [outline_line_dash_offset](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.outline_line_dash_offset)
  - The line dash offset for the plot border outline.
* - [outline_line_join](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.outline_line_join)
  - The line join for the plot border outline.
* - [outline_line_width](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.outline_line_width)
  - The line width for the plot border outline.
* - [output_backend](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.output_backend)
  - Specify the output backend for the plot area. Default is HTML5 Canvas.
* - [renderers](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.renderers)
  - A `list` of all glyph renderers for this plot.
* - [reset_policy](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.reset_policy)
  - How a plot should respond to being reset. 
* - [resizable](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.resizable)
  - Whether the layout is interactively resizable, and if so in which dimensions.
* - [right](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.right)
  - A `list` of renderers to occupy the area to the right of the plot.
* - [sizing_mode](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.sizing_mode)
  - How the component should size itself.
* - [styles](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.styles)
  - Inline CSS styles applied to the underlying DOM element.
* - [stylesheets](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.stylesheets)
  - Additional style-sheets to use for the underlying DOM element.
* - [syncable](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.syncable)
  - Indicates whether this model should be synchronized back to a Bokeh server when updated in a web browser. 
* - [tags](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.tags)
  - An optional `list` of arbitrary, user-supplied values to attach to this model.
* - [title](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.title)
  - A title for the plot. Can be a text string or a Title annotation.
* - [title_location](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.title_location)
  - Where the title will be located. Titles on the left or right side will be rotated.
* - [toolbar](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.toolbar)
  - The toolbar associated with this plot which holds all the tools. It is automatically created with the plot if necessary.
* - [toolbar_inner](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.toolbar_inner)
  - Locate the toolbar inside the frame. Setting this property to `True` makes most sense with auto-hidden toolbars.
* - [toolbar_location](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.toolbar_location)
  - Where the toolbar will be located. If set to `None`, no toolbar will be attached to the plot.
* - [toolbar_sticky](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.toolbar_sticky)
  - Stick the toolbar to the edge of the plot. Default: `True`. If `False`, the toolbar will be outside of the axes, titles etc.
* - [visible](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.visible)
  - Whether the component should be displayed on screen.
* - [width](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.width)
  - The width of the component (in pixels).
* - [width_policy](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.width_policy)
  - Describes how the component should maintain its width.
* - [x_range](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.x_range)
  - The (default) data range of the horizontal dimension of the plot.
* - [x_scale](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.x_scale)
  - What kind of scale to use to convert x-coordinates in data space into x-coordinates in screen space.
* - [y_range](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.y_range)
  - The (default) data range of the vertical dimension of the plot.
* - [y_scale](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.y_scale)
  - What kind of scale to use to convert y-coordinates in data space into y-coordinates in screen space.
```

<br/>

### Propiedades

Propiedades de la clase `figure`. Estas propiedades no se usan como parámetros del constructor `figure()`, suelen ser heredadas de otras clases y algunas son de solo lectura, particularmente las que retornan `list` de objetos. 

```{list-table}
:header-rows: 1

* - property
  - Descripción
* - axis
  - `list` de objetos `Axis`.
* - background
  - .
* - coordinates
  - .
* - document
  - El documento al que se adjunta este modelo (puede ser None).
* - grid
  - `list` de objetos `Grid`.
* - hover
  - `list` de objetos `HoverTool`.
* - id
  - .
* - legend
  - `list` de objetos `Legend`.
* - plot
  - .
* - ref
  - .
* - tools
  - .
* - xaxis
  - `list` de objetos `Axis` para la dimensión _X_.
* - xgrid
  - `list` de objetos `Grid` para la dimensión _X_.
* - yaxis
  - `list` de objetos `Axis` para la dimensión _Y_.
* - ygrid
  - `list` de objetos `Grid` para la dimensión _Y_.
```

<br/>

### Métodos de clase

Estos métodos se utilizan sobre la misma clase `figure`, no sobre sus instancias.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [clear_extensions](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.clear_extensions)()
  - Borra las extensiones personalizadas actualmente definidas.
* - [dataspecs](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.dataspecs)()
  - Recopila los nombres de todas las propiedades de _DataSpec_ en esta clase.
* - [descriptors](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.descriptors)()
  - Lista de descriptores de propiedades en el orden de definición.
* - [lookup](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.lookup)(name: str, ...)
  - Encuentra el _PropertyDescriptor_ para una propiedad de bokeh en una clase, dado el nombre de la propiedad.
* - [parameters](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.parameters)()
  - Genera valores de parámetros de Python adecuados para funciones que se derivan del _glyph_.
* - [properties](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.properties)(, ...)
  - Recopila los nombres de las propiedades en esta clase.
* - [properties_with_refs](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.properties_with_refs)()
  - Recopila los nombres de todas las propiedades en esta clase que también tienen referencias.
```

<br/>

### Métodos de instancia

Métodos de la clase `figure`.

#### Glyphs

Los objetos de figura tienen muchos métodos de _glyphs_ que se pueden usar para dibujar _glyphs_ gráficos vectorizados.

:::{warning}
Las descripciones de los métodos en esta sección están en inglés.
:::

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [add_glyph](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.add_glyph)(...)
  - Adds a glyph to the plot with associated data sources and ranges.
* - [annular_wedge](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.annular_wedge)(x=Field(...), y=Field(...), ...)
  - Configure and add AnnularWedge glyphs to this figure.
* - [annulus](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.annulus)(x=Field(...), y=Field(...), ...)
  - Configure and add Annulus glyphs to this figure.
* - [arc](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.arc)(x=Field(...), y=Field(...), ...)
  - Configure and add Arc glyphs to this figure.
* - [asterisk](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.asterisk)(x=Field(...), y=Field(...), size=4, ...)
  - Configure and add Scatter glyphs to this figure.
* - [bezier](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.bezier)(x0=Field(...), y0=Field(...), ...)
  - Configure and add Bezier glyphs to this figure.
* - [block](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.block)(x=Field(...), y=Field(...), ...)
  - Configure and add Block glyphs to this figure.
* - [circle](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.circle)(*args: Any, **kwargs: Any)
  - Configure and add Circle glyphs to this figure.
* - [circle_cross](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.circle_cross)(x=Field(...), y=Field(...), size=4, ...)
  - Configure and add Scatter glyphs to this figure.
* - [circle_dot](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.circle_dot)(x=Field(...), y=Field(...), size=4, ...)
  - Configure and add Scatter glyphs to this figure.
* - [circle_x](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.circle_x)(x=Field(...), y=Field(...), size=4, ...)
  - Configure and add Scatter glyphs to this figure.
* - [circle_y](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.circle_y)(x=Field(...), y=Field(...), size=4, ...)
  - Configure and add Scatter glyphs to this figure.
* - [cross](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.cross)(x=Field(...), y=Field(...), size=4, ...)
  - Configure and add Scatter glyphs to this figure.
* - [dash](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.dash)(x=Field(...), y=Field(...), size=4, ...)
  - Configure and add Scatter glyphs to this figure.
* - [diamond](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.diamond)(x=Field(...), y=Field(...), size=4, ...)
  - Configure and add Scatter glyphs to this figure.
* - [diamond_cross](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.diamond_cross)(x=Field(...), y=Field(...), size=4, ...)
  - Configure and add Scatter glyphs to this figure.
* - [diamond_dot](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.diamond_dot)(x=Field(...), y=Field(...), size=4, ...)
  - Configure and add Scatter glyphs to this figure.
* - [dot](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.dot)(x=Field(...), y=Field(...), size=4, ...)
  - Configure and add Scatter glyphs to this figure.
* - [ellipse](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.ellipse)(x=Field(...), y=Field(...), ...)
  - Configure and add Ellipse glyphs to this figure.
* - [harea](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.harea)(x1=Field(...), x2=Field(...), ...)
  - Configure and add HArea glyphs to this figure.
* - [harea_step](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.harea_step)(x1=Field(...), x2=Field(...), ...)
  - Configure and add HAreaStep glyphs to this figure.
* - [hbar](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.hbar)(y=Field(...), height=1, ...)
  - Configure and add HBar glyphs to this figure.
* - [hex](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.hex)(x=Field(...), y=Field(...), size=4, ...)
  - Configure and add Scatter glyphs to this figure.
* - [hex_dot](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.hex_dot)(x=Field(...), y=Field(...), size=4, ...)
  - Configure and add Scatter glyphs to this figure.
* - [hex_tile](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.hex_tile)(q=Field(...), r=Field(...), ...)
  - Configure and add HexTile glyphs to this figure.
* - [hspan](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.hspan)(y=Field(...), ...)
  - Configure and add HSpan glyphs to this figure.
* - [hstrip](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.hstrip)(y0=Field(...), y1=Field(...), ...)
  - Configure and add HStrip glyphs to this figure.
* - [image](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.image)(image=Field(...), x=Field(...), ...)
  - Configure and add Image glyphs to this figure.
* - [image_rgba](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.image_rgba)(image=Field(...), x=Field(...), ...)
  - Configure and add ImageRGBA glyphs to this figure.
* - [image_stack](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.image_stack)(image=Field(...), x=Field(...), ...)
  - Configure and add ImageStack glyphs to this figure.
* - [image_url](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.image_url)(url, x, y, w, h, angle=0, ...)
  - Configure and add ImageURL glyphs to this figure.
* - [inverted_triangle](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.inverted_triangle)(x=Field(...), y=Field(...), size=4, ...)
  - Configure and add Scatter glyphs to this figure.
* - [line](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.line)(x=Field(...), y=Field(...), ...)
  - Configure and add Line glyphs to this figure.
* - [mathml](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.mathml)(x=Field(...), y=Field(...), ...)
  - Configure and add MathMLGlyph glyphs to this figure.
* - [multi_line](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.multi_line)(xs=Field(...), ys=Field(...), ...)
  - Configure and add MultiLine glyphs to this figure.
* - [multi_polygons](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.multi_polygons)(xs=Field(...), ys=Field(...), ...)
  - Configure and add MultiPolygons glyphs to this figure.
* - [ngon](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.ngon)(x=Field(...), y=Field(...), ...)
  - Configure and add Ngon glyphs to this figure.
* - [patch](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.patch)(x=Field(...), y=Field(...), ...)
  - Configure and add Patch glyphs to this figure.
* - [patches](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.patches)(xs=Field(...), ys=Field(...), ...)
  - Configure and add Patches glyphs to this figure.
* - [plus](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.plus)(x=Field(...), y=Field(...), size=4, ...)
  - Configure and add Scatter glyphs to this figure.
* - [quad](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.quad)(left=Field(...), right=Field(...), ...)
  - Configure and add Quad glyphs to this figure.
* - [quadratic](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.quadratic)(x0=Field(...), y0=Field(...), ...)
  - Configure and add Quadratic glyphs to this figure.
* - [ray](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.ray)(x=Field(...), y=Field(...), ...)
  - Configure and add Ray glyphs to this figure.
* - [rect](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.rect)(x=Field(...), y=Field(...), ...)
  - Configure and add Rect glyphs to this figure.
* - [segment](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.segment)(x0=Field(...), y0=Field(...), ...)
  - Configure and add Segment glyphs to this figure.
* - [square](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.square)(x=Field(...), y=Field(...), size=4, ...)
  - Configure and add Scatter glyphs to this figure.
* - [square_cross](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.square_cross)(x=Field(...), y=Field(...), size=4, ...)
  - Configure and add Scatter glyphs to this figure.
* - [square_dot](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.square_dot)(x=Field(...), y=Field(...), size=4, ...)
  - Configure and add Scatter glyphs to this figure.
* - [square_pin](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.square_pin)(x=Field(...), y=Field(...), size=4, ...)
  - Configure and add Scatter glyphs to this figure.
* - [square_x](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.square_x)(x=Field(...), y=Field(...), size=4, ...)
  - Configure and add Scatter glyphs to this figure.
* - [star](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.star)(x=Field(...), y=Field(...), size=4, ...)
  - Configure and add Scatter glyphs to this figure.
* - [star_dot](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.star_dot)(x=Field(...), y=Field(...), size=4, ...)
  - Configure and add Scatter glyphs to this figure.
* - [step](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.step)(x=Field(...), y=Field(...), ...)
  - Configure and add Step glyphs to this figure.
* - [tex](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.tex)(x=Field(...), y=Field(...), ...)
  - Configure and add TeXGlyph glyphs to this figure.
* - [text](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.text)(x=Field(...), y=Field(...), ...)
  - Configure and add Text glyphs to this figure.
* - [triangle](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.triangle)(x=Field(...), y=Field(...), size=4, ...)
  - Configure and add Scatter glyphs to this figure.
* - [triangle_dot](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.triangle_dot)(x=Field(...), y=Field(...), size=4, ...)
  - Configure and add Scatter glyphs to this figure.
* - [triangle_pin](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.triangle_pin)(x=Field(...), y=Field(...), size=4, ...)
  - Configure and add Scatter glyphs to this figure.
* - [varea](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.varea)(x=Field(...), y1=Field(...), ...)
  - Configure and add VArea glyphs to this figure.
* - [varea_step](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.varea_step)(x=Field(...), y1=Field(...), ...)
  - Configure and add VAreaStep glyphs to this figure.
* - [vbar](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.vbar)(x=Field(...), width=1, ...)
  - Configure and add VBar glyphs to this figure.
* - [vspan](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.vspan)(x=Field(...), ...)
  - Configure and add VSpan glyphs to this figure.
* - [vstrip](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.vstrip)(x0=Field(...), x1=Field(...), ...)
  - Configure and add VStrip glyphs to this figure.
* - [wedge](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.wedge)(x=Field(...), y=Field(...), ...)
  - Configure and add Wedge glyphs to this figure.
* - [x](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.x)(x=Field(...), y=Field(...), size=4, ...)
  - Configure and add Scatter glyphs to this figure.
* - [y](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.y)(x=Field(...), y=Field(...), size=4, ...)
  - Configure and add Scatter glyphs to this figure.
```

<br/>

#### Stack

Métodos especializados para apilar barras.

:::{warning}
Las descripciones de los métodos en esta sección están en inglés.
:::

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [harea_stack](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.harea_stack)(stackers, **kw)
  - Generate multiple HArea renderers for levels stacked left to right.
* - [hbar_stack](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.hbar_stack)(stackers, **kw)
  - Generate multiple HBar renderers for levels stacked left to right.
* - [hline_stack](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.hline_stack)(stackers, **kw)
  - Generate multiple Line renderers for lines stacked horizontally.
* - [varea_stack](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.varea_stack)(stackers, **kw)
  - Generate multiple VArea renderers for levels stacked bottom to top.
* - [vbar_stack](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.vbar_stack)(stackers, **kw)
  - Generate multiple VBar renderers for levels stacked bottom to top.
* - [vline_stack](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.vline_stack)(stackers, **kw)
  - Generate multiple Line renderers for lines stacked vertically.
```

<br/>

#### Especiales

Otros métodos especiales.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [scatter](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.scatter)(*args: Any, **kwargs: Any)
  - Creates a scatter plot of the given x and y items. 
* - [contour](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.contour)(x: ArrayLike | None = None, ...)
  - Creates a contour plot of filled polygons and/or contour lines.
* - [hexbin](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.hexbin)(x, y, size, ...)
  - Perform a simple equal-weight hexagonal binning.
```

<br/>

#### Otros

Otros métodos con diversas utilidades.

:::{warning}
Las descripciones de los métodos en esta sección están en inglés.
:::

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [add_layout](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.add_layout)(obj: Renderer, ...)
  - Adds an object to the plot in a specified place.
* - [add_tile](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.add_tile)(...)
  - Adds new TileRenderer into Plot.renderers.
* - [add_tools](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.add_tools)(*tools: Tool | str)
  - Adds tools to the plot.
* - [apply_theme](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.apply_theme)(property_values: dict[str, Any])
  - Apply a set of theme values which will be used rather than defaults, but will not override application-set values.
* - [clone](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.clone)(**overrides: Any)
  - Duplicate a HasProps object.
* - [column](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.column)(col, gridplot)
  - Return whether this plot is in a given column of a GridPlot.
* - [destroy](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.destroy)()
  - Clean up references to the document and property.
* - [equals](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.equals)(other: HasProps)
  - Structural equality of models.
* - [graph](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.graph)(node_source: ColumnDataSource, ...)
  - Creates a network graph using the given node, edge and layout provider.
* - [hold](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.hold)(, ...)
  - Takes care of turning a property on and off within a scope.
* - [js_link](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.js_link)(attr: str, other: Model, ...)
  - Link two Bokeh model properties using JavaScript.
* - [js_on_change](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.js_on_change)(event: str, ...)
  - Attach a CustomJS callback to an arbitrary BokehJS model event.
* - [js_on_event](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.js_on_event)(event: str | type[Event], ...)
  - .
* - [on_change](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.on_change)(attr: str, ...)
  - Add a callback on this object to trigger when attr changes.
* - [on_event](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.on_event)(event: str | type[Event], ...)
  - Run callbacks when the specified event occurs on this Model.
* - [properties_with_values](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.properties_with_values)(, ...)
  - Collect a `dict` mapping property names to their values.
* - [query_properties_with_values](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.query_properties_with_values)(...)
  - Query the properties values of HasProps instances with a predicate.
* - [references](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.references)()
  - Returns all Models that this object has references to.
* - [remove_on_change](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.remove_on_change)(attr: str, ...)
  - Remove a callback from this object.
* - [remove_tools](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.remove_tools)(*tools: Tool)
  - Removes tools from the plot.
* - [row](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.row)(row, gridplot)
  - Return whether this plot is in a given row of a GridPlot.
* - [select](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.select)(*args, **kwargs)
  - Query this object and all of its references for objects that match the given selector.
* - [select_one](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.select_one)(selector: SelectorType)
  - Query this object and all of its references for objects that match the given selector. 
* - [set_from_json](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.set_from_json)(name: str, value: Any, ...)
  - Set a property value on this object from JSON.
* - [set_select](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.set_select)(...)
  - Update objects that match a given selector with the specified attribute/value updates.
* - [subplot](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.subplot)(, ...)
  - Create a new sub-coordinate system and expose a plotting API.
* - [themed_values](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.themed_values)()
  - Get any theme-provided overrides.
* - [to_serializable](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.to_serializable)(serializer: Serializer)
  - Converts this object to a serializable representation.
* - [trigger](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.trigger)(attr: str, old: Any, new: Any, ...)
  - .
* - [unapply_theme](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.unapply_theme)()
  - Remove any themed values and restore defaults.
* - [update](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.update)(**kwargs: Any)
  - Updates the object’s properties from the given keyword arguments.
```
