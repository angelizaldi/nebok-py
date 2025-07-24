# Ejes

Contiene herramientas para crear y personalizar ejes en visualizaciones, como ejes lineales, logarítmicos y de fechas.

:::{note}
Para más información de esta sección visitar la [documentación](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html) de `bokeh`.
:::

<br/>

## Clases

Clases implementadas en el módulo _models_ del tipo _axes_. 

```{list-table}
:header-rows: 1

* - Constructor
  - Descripción
* - [Axis](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis)(*args: Any,  id: ID | None = None,  **kwargs: Any)
  - Una clase base que define propiedades comunes para todos los tipos de eje.
* - [CategoricalAxis](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.CategoricalAxis)(*args: Any,  id: ID | None = None,  **kwargs: Any)
  - Un eje que muestra _ticks_ y etiquetas para rangos categóricos.
* - [ContinuousAxis](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.ContinuousAxis)(*args: Any,  id: ID | None = None,  **kwargs: Any)
  - Una clase base para todos los tipos numéricos de ejes no categóricos.
* - [DatetimeAxis](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.DatetimeAxis)(*args: Any,  id: ID | None = None,  **kwargs: Any)
  - Un `LinearAxis` que elige buenos números para ubicaciones de _ticks_ en una escala de fecha y hora. Configurado con un `DataTimeTickFormatter` de forma predeterminada.
* - [LinearAxis](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.LinearAxis)(*args: Any,  id: ID | None = None,  **kwargs: Any)
  - Un eje que elige buenos números para ubicaciones de _ticks_ a escala lineal. Configurado con un `BasicTickFormatter` de forma predeterminada.
* - [LogAxis](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.LogAxis)(*args: Any,  id: ID | None = None,  **kwargs: Any)
  - Un eje que elige buenos números para ubicaciones de _ticks_ en una escala logarítmica. Configurado con un `LogTickFormatter` de forma predeterminada.
* - [MercatorAxis](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.MercatorAxis)(*args: Any,  id: ID | None = None,  **kwargs: Any)
  - Un eje que elige buenos números para ubicaciones de _ticks_ en una escala de Mercator. Configurado con un `MercatortickFormatter` de forma predeterminada.
```

<br/>

### Axis

Una clase base que define propiedades comunes para todos los tipos de eje.

```{list-table}
:header-rows: 1

* - Constructor
  - Descripción
* - [Axis](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis)(*args: Any,  id: ID | None = None,  **kwargs: Any)
  - Una clase base que define propiedades comunes para todos los tipos de eje.
```

#### Atributos

Atributos de la clase `Axis`. 

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - [axis_label](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.axis_label)
  - Una etiqueta para el eje, que se muestra paralelo al eje.
* - [axis_label_align](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.axis_label_align)
  - La alineación de la etiqueta del eje a lo largo del eje.
* - [axis_label_orientation](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.axis_label_orientation)
  - En qué dirección debe orientarse el texto de la etiqueta del eje. Si se suministra un número, el ángulo del texto se mide desde la horizontal.
* - [axis_label_standoff](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.axis_label_standoff)
  - La distancia en píxeles que las etiquetas del eje deben separarse de las etiquetas de los _ticks_.
* - [axis_label_text_align](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.axis_label_text_align)
  - La alineación del texto de la etiqueta del eje.
* - [axis_label_text_alpha](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.axis_label_text_alpha)
  - El alfa de la etiqueta del eje.
* - [axis_label_text_baseline](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.axis_label_text_baseline)
  - La línea de base de texto de la etiqueta del eje.
* - [axis_label_text_color](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.axis_label_text_color)
  - El color de texto de la etiqueta del eje.
* - [axis_label_text_font](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.axis_label_text_font)
  - La fuente de texto de la etiqueta del eje.
* - [axis_label_text_font_size](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.axis_label_text_font_size)
  - El tamaño de fuente de texto de la etiqueta del eje.
* - [axis_label_text_font_style](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.axis_label_text_font_style)
  - El estilo de fuente de texto de la etiqueta del eje.
* - [axis_label_text_line_height](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.axis_label_text_line_height)
  - La altura de la línea de texto de la etiqueta del eje.
* - [axis_label_text_outline_color](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.axis_label_text_outline_color)
  - El el color del borde del texto de la etiqueta del eje.. The text outline color of the axis label.
* - [axis_line_alpha](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.axis_line_alpha)
  - El alfa de la línea del eje.
* - [axis_line_cap](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.axis_line_cap)
  - El límite de la línea de la línea del eje.
* - [axis_line_color](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.axis_line_color)
  - El color de la línea de la línea del eje.
* - [axis_line_dash](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.axis_line_dash)
  - El tipo de línea de la línea del eje.
* - [axis_line_dash_offset](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.axis_line_dash_offset)
  - La separación de los _dashes_ de la línea de la línea del eje.
* - [axis_line_join](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.axis_line_join)
  - La unión de la línea de la línea del eje.
* - [axis_line_width](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.axis_line_width)
  - El ancho de la línea de la línea del eje.
* - [background_fill_alpha](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.background_fill_alpha)
  - El alfa de llenado del fondo del eje.
* - [background_fill_color](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.background_fill_color)
  - El color de llenado del fondo del eje.
* - [bounds](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.bounds)
  - Límites para el eje renderizado. Si no lo establece, el eje abarcará toda la gráfica en la dimensión dada.
* - [context_menu](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.context_menu)
  - Un menú para mostrar cuando el usuario hace clic derecho en el componente.
* - [css_classes](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.css_classes)
  - Un ´list´ de clases CSS adicionales para agregar al elemento DOM subyacente.
* - [css_variables](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.css_variables)
  - Permite definir variables CSS calculadas dinámicamente.
* - [dimension](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.dimension)
  - Permite sobreescribir las dimensiones inferidas en contextos que respaldan esto. Esta propiedad no tiene efecto cuando se usa un ejes como eje de marco.
* - [face](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.face)
  - La dirección hacia la que se dirigirá el eje.
* - [fixed_location](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.fixed_location)
  - Establece para especificar una ubicación de coordenada fija para dibujar el eje. La dirección de los _ticks_ y las principales etiquetas está determinada por el panel lateral al que pertenece el eje.
* - [formatter](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.formatter)
  - Un `TickFormatter` para usar para formatear la apariencia visual de los _ticks_.
* - [group](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.group)
  - .
* - [level](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.level)
  - Especifica el nivel para pintar este renderizador.
* - [major_label_orientation](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.major_label_orientation)
  - En qué dirección debe orientarse el texto principal de la etiqueta. Si se suministra un número, el ángulo del texto se mide desde la horizontal.
* - [major_label_overrides](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.major_label_overrides)
  - Proporcione valores explícitos de la etiqueta de los _ticks_ para ubicaciones de _ticks_ específicas que sobreescriban el formato normal.
* - [major_label_policy](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.major_label_policy)
  - Permite filtrar las etiquetas.
* - [major_label_standoff](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.major_label_standoff)
  - La distancia en píxeles de que las principales etiquetas de _ticks_ se deben separarar de los _ticks_ asociados.
* - [major_label_text_align](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.major_label_text_align)
  - La alineación del texto de las principales etiquetas de los _ticks_.
* - [major_label_text_alpha](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.major_label_text_alpha)
  - El alfa del texto de las principales etiquetas de los _ticks_.
* - [major_label_text_baseline](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.major_label_text_baseline)
  - La línea de base del texto de las principales etiquetas de los _ticks_.
* - [major_label_text_color](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.major_label_text_color)
  - El color de texto de las principales etiquetas de los _ticks_.
* - [major_label_text_font](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.major_label_text_font)
  - La fuente de texto de las principales etiquetas de los _ticks_.
* - [major_label_text_font_size](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.major_label_text_font_size)
  - El tamaño de fuente de texto de las principales etiquetas de los _ticks_.
* - [major_label_text_font_style](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.major_label_text_font_style)
  - El estilo de fuente de texto de las principales etiquetas de los _ticks_.
* - [major_label_text_line_height](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.major_label_text_line_height)
  - La altura de la línea de texto de las principales etiquetas de los _ticks_.
* - [major_label_text_outline_color](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.major_label_text_outline_color)
  - El color del borde de las principales etiquetas de los _ticks_
* - [major_tick_in](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.major_tick_in)
  - La distancia en píxeles que los _ticks_ principales deben extenderse al área principal de la gráfica.
* - [major_tick_line_alpha](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.major_tick_line_alpha)
  - El alfa de lass línea de los _ticks_ principales.
* - [major_tick_line_cap](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.major_tick_line_cap)
  - El límite de línea de los _ticks_ principales.s.
* - [major_tick_line_color](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.major_tick_line_color)
  - El color de la línea de los _ticks_ principales.
* - [major_tick_line_dash](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.major_tick_line_dash)
  - El tipo de línea de la línea de los _ticks_ principales.
* - [major_tick_line_dash_offset](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.major_tick_line_dash_offset)
  - La separación de los _dashes_ de la línea de los _ticks_ principales.
* - [major_tick_line_join](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.major_tick_line_join)
  - La unión de la línea de los _ticks_ principales.
* - [major_tick_line_width](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.major_tick_line_width)
  - El ancho de línea de los _ticks_ principales.
* - [major_tick_out](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.major_tick_out)
  - La distancia en píxeles que los _ticks_ principales deben extenderse fuera del área principal de la trama.
* - [minor_tick_in](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.minor_tick_in)
  - La distancia en píxeles que los _ticks_ menores deben extenderse en el área principal de la gráfica.
* - [minor_tick_line_alpha](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.minor_tick_line_alpha)
  - El alfa del texto de los _ticks_ menores.
* - [minor_tick_line_cap](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.minor_tick_line_cap)
  - El límite de línea de los _ticks_ menores.
* - [minor_tick_line_color](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.minor_tick_line_color)
  - El color de la línea de los _ticks_ menores.
* - [minor_tick_line_dash](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.minor_tick_line_dash)
  - El tipo de línea de la línea de los _ticks_ menores.
* - [minor_tick_line_dash_offset](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.minor_tick_line_dash_offset)
  - La separación de los _dashes_ de la línea de los _ticks_ menores.
* - [minor_tick_line_join](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.minor_tick_line_join)
  - La unión de la línea de los _ticks_ menores.
* - [minor_tick_line_width](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.minor_tick_line_width)
  - El ancho de línea de los _ticks_ menores.
* - [minor_tick_out](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.minor_tick_out)
  - La distancia en píxeles que los _ticks_ menores deben extenderse fuera del área principal de la gráfica.
* - [name](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.name)
  - Un nombre arbitrario suministrado por el usuario para este modelo.
* - [propagate_hover](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.propagate_hover)
  - Permite propagar eventos de desplazamiento al renderizador padre, marco o lienzo.
* - [styles](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.styles)
  - Estilos CSS en línea aplicados al elemento DOM subyacente.
* - [stylesheets](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.stylesheets)
  - Hojas de estilo adicionales para usar para el elemento DOM subyacente.
* - [syncable](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.syncable)
  - Indica si este modelo debe sincronizarse de nuevo a un servidor bokeh cuando se actualiza en un navegador web.
* - [tags](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.tags)
  - Un ´list´ opcional de valores arbitrarios, proporcionados por el usuario para adjuntar a este modelo.
* - [ticker](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.ticker)
  - Un _Ticker_ para calcular las ubicaciones de los componentes del eje.
* - [visible](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.visible)
  - Indica si es visible.
* - [x_range_name](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.x_range_name)
  - Un rango _y_ particular (nombrado) para calcular las ubicaciones en la pantalla al representar _glyphs_ en la gráfica. Si no se establece, se usa el rango _y_ predeterminado.
* - [y_range_name](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.y_range_name)
  - Un rango _y_ particular (nombrado) para calcular las ubicaciones en la pantalla al representar _glyphs_ en la gráfica. Si no se establece, se usa el rango _y_ predeterminado.
```

<br/>

#### Propiedades

Propiedades de la clase `Axis`. 

```{list-table}
:header-rows: 1

* - Propiedad
  - Descripción
* - **document: Document | None**
  - El documento al que se adjunta este modelo (puede ser `None`).
```

<br/>

#### Métodos

Métodos de instancia de la clase `Axis`. 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [apply_theme](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.apply_theme)(property_values: dict[str,  Any])
  - Aplica un conjunto de valores del tema que se utilizarán en lugar de los valores predeterminados, pero no anularán los valores del conjunto de aplicaciones.
* - [clone](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.clone)(**overrides: Any)
  - Duplica un objeto `HasProps`.
* - [destroy](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.destroy)()
  - Limpia las referencias al documento y la propiedad.
* - [equals](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.equals)(other: HasProps)
  - Igualdad estructural de modelos.
* - [js_link](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.js_link)(attr: str,  other: Model, ...)
  - Enlaza dos propiedades del modelo bokeh usando JavaScript.
* - [js_on_change](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.js_on_change)(event: str, ...)
  - Adjunta una devolución de llamada `CustomJS` a un evento arbitrario de modelo de _BokehJS_.
* - [on_change](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.on_change)(attr: str, ...)
  - Agrega una devolución de llamada en este objeto para activar cuando _attr_ cambia.
* - [on_event](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.on_event)(event: str | type[Event], ...)
  - Ejecuta devoluciones de llamada cuando el evento especificado ocurre en este modelo.
* - [properties_with_values](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.properties_with_values)(...)
  - Retorna un ´dict´ que mapea nombres de propiedad a sus valores.
* - [query_properties_with_values](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.query_properties_with_values)(...)
  - Consulta los valores de propiedades de las instancias de `HaSprops^ con un predicado.
* - [references](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.references)()
  - Retorna todos los modelos a los que este objeto tiene referencias.
* - [remove_on_change](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.remove_on_change)(attr: str, ...)
  - Elimina una devolución de llamada de este objeto.
* - [select](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.select)(selector: SelectorType)
  - Consulta este objeto y todas sus referencias para objetos que coincidan con el selector dado.
* - [select_one](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.select_one)(selector: SelectorType)
  - Consulta este objeto y todas sus referencias para objetos que coincidan con el selector dado. Plantea un error si se encuentra más de un objeto. Retorna un solo objeto coincidente, o ´None´ si no se encuentra nada.
* - [set_from_json](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.set_from_json)(name: str,  value: Any, ...)
  - Establece un valor de propiedad en este objeto de JSON.
* - [set_select](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.set_select)(...)
  - Actualiza objetos que coincidan con un selector dado con las actualizaciones de atributo/valor especificadas.
* - [themed_values](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.themed_values)()
  - Retorna cualquier sobreescritura proporcionada por el tema.
* - [to_serializable](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.to_serializable)(serializer: Serializer)
  - Convierte este objeto en una representación serializable.
* - [trigger](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.trigger)(attr: str,  old: Any,  new: Any, ...)
  - .
* - [unapply_theme](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.unapply_theme)()
  - Elimina los valores temáticos y restaura los valores predeterminados.
* - [update](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.update)(**kwargs: Any)
  - Actualiza las propiedades del objeto de los argumentos de palabras clave dados.
```

<br/>

#### Métodos de Clase

Métodos de clase de la clase `Axis`. Estos métodos se utilizan directamente sobre `Axis` y no sobre sus instancias.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [classmethod clear_extensions](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.clear_extensions)()
  - Borra las extensiones personalizadas actualmente definidas.
* - [classmethod dataspecs](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.dataspecs)()
  - Recopila los nombres de todas las propiedades de _DataSpec_ en esta clase.
* - [classmethod descriptors](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.descriptors)()
  - Lista de descriptores de propiedades en el orden de definición.
* - [classmethod lookup](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.lookup)(name: str, ...)
  - Encuentra el _PropertyDescriptor_ para una propiedad bokeh en una clase, dado el nombre de la propiedad.
* - [classmethod parameters](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.parameters)()
  - Genera valores de parámetros de Python adecuados para funciones que se derivan del _glyph_.
* - [classmethod properties](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.properties)(...)
  - Recopila los nombres de las propiedades en esta clase.
* - [classmethod properties_with_refs](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html#bokeh.models.Axis.properties_with_refs)()
  - Recopila los nombres de todas las propiedades en esta clase que también tienen referencias.
```