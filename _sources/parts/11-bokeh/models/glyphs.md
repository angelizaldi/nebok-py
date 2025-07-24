# _Glyphs_

Ofrece los elementos básicos para representar datos en gráficos, como líneas, círculos, barras y áreas.

:::{note}
Para más información de esta sección visitar la [documentación](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs.html) de `bokeh`.
:::

## Clases

Clases implementadas en el módulo _models_ del tipo _glyphs_. 

```{list-table}
:header-rows: 1

* - Constructor
  - Descripción
* - [XYGlyph](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/xy_glyph.html)(*args:Any,id:ID|None=None, ...)
  - Clase base de _glyphs_ con atributos de coordenadas _x_ y _y_.
* - **Áreas, líneas y rectas**
  -
* - [HArea](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/harea.html)(*args:Any,id:ID|None=None, ...)
  - Renderiza un área sombreada horizontalmente entre dos curvas.
* - [HAreaStep](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/harea_step.html)(*args:Any,id:ID|None=None, ...)
  - Variante de `HArea` con escalonamientos entre los valores.
* - [HSpan](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/hspan.html)(*args:Any,id:ID|None=None, ...)
  - Bandas horizontales de ancho infinito.
* - [HStrip](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/hstrip.html)(*args:Any,id:ID|None=None, ...)
  - Franjas horizontales de ancho infinito.
* - [MultiLine](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/multi_line.html)(*args:Any,id:ID|None=None, ...)
  - Renderiza varias líneas. Conjunto de múltiples líneas independientes.
* - [Ray](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/ray.html)(*args:Any,id:ID|None=None, ...)
  - Renderiza _rays_. Línea infinita con un punto de inicio y un ángulo de dirección.
* - [Segment](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/segment.html)(*args:Any,id:ID|None=None, ...)
  - Renderiza segmentos. Línea entre pares de puntos.
* - [Step](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/step.html)(*args:Any,id:ID|None=None, ...)
  - Renderiza líneas de pasos. Línea escalonada entre valores, útil para series temporales.
* - [VSpan](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/vspan.html)(*args:Any,id:ID|None=None, ...)
  - Líneas verticales de altura infinita.
* - [VStrip](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/vstrip.html)(*args:Any,id:ID|None=None, ...)
  - Franjas verticales de altura infinita.
* - [VArea](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/varea.html)(*args:Any,id:ID|None=None, ...)
  - Renderiza un área dirigida verticalmente entre dos secuencias de igual longitud de coordenadas y con las mismas coordenadas _x_.
* - [VAreaStep](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/varea_step.html)(*args:Any,id:ID|None=None, ...)
  - Renderiza un área sombreada verticalmente entre dos curvas.
of y-coordinates with the same x-coordinates using step lines.
* - **Cónicas y curvas**
  -
* - [Annulus](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/annulus.html)(*args:Any,id:ID|None=None, ...)
  - Renderiza _annuli_. Un anillo, definido por un radio interno y externo.
* - [Annular Wedge](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/annular_wedge.html)(*args:Any,id:ID|None=None, ...)
  - Renderiza cuñas anulares. Un sector de un anillo, definido por un ángulo inicial y final.
* - [Arc](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/arc.html)(*args:Any,id:ID|None=None, ...)
  - Renderiza _arcs_. Un arco de círculo definido por un centro, radio y ángulos de inicio y fin.
* - [Bezier](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/bezier.html)(*args:Any,id:ID|None=None, ...)
  - Renderiza curvas de Bezier. Una curva de Bézier definida por puntos de control.
* - [Circle](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/circle.html)(*args:Any,id:ID|None=None, ...)
  - Renderiza marcadores de círculo. Un círculo simple definido por su radio.
* - [Ellipse](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/ellipse.html)(*args:Any,id:ID|None=None, ...)
  - Renderiza elipses. Una elipse definida por sus ejes mayor y menor.
* - [Quad](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/quad.html)(*args:Any,id:ID|None=None, ...)
  - Renderiza _quads_ alineados al eje. Cuadrilátero definido por coordenadas de cada lado.
* - [Quadratic](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/quadratic.html)(*args:Any,id:ID|None=None, ...)
  - Renderiza parábolas. Curva cuadrática definida por un punto de inicio, fin y control.
* - [Wedge](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/wedge.html)(*args:Any,id:ID|None=None, ...)
  - Renderiza _wedges_. Un sector de un círculo definido por un ángulo inicial y final.
* - **Barras**
  -
* - [HBar](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/hbar.html)(*args:Any,id:ID|None=None, ...)
  - Renderiza barras horizontales, dada una coordenada central, altura y (izquierda, derecha) coordenadas.
* - [VBar](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/vbar.html)(*args:Any,id:ID|None=None, ...)
  - Renderiza barras verticales, dada una coordenada central, ancho y coordenadas (arriba, inferior).
* - **Gráficas clásicas**
  -
* - [Line](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/line.html)(*args:Any,id:ID|None=None, ...)
  - Renderiza una sola línea. Línea simple entre puntos consecutivos.
* - [Marker](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/marker.html)(*args:Any,id:ID|None=None, ...)
  - Clase base para _glyphs_ que son marcadores simples con línea y propiedades de relleno, ubicadas en una ubicación _(x, y)_ con un tamaño especificado.
* - [Scatter](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/scatter.html)(*args:Any,id:ID|None=None, ...)
  - Renderiza marcadores de dispersión seleccionados de una lista predefinida de diseños.
* - **Imágenes**
  -
* - [Image](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/image.html)(*args:Any,id:ID|None=None, ...)
  - Renderiza las imágenes dadas como datos escalares en escala de grises o en color.
* - [ImageRGBA](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/image_rgba.html)(*args:Any,id:ID|None=None, ...)
  - Renderiza imágenes con valores RGBA por píxel, permitiendo transparencia.
* - [ImageStack](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/image_stack.html)(*args:Any,id:ID|None=None, ...)
  - Renderiza imágenes dadas como matrices 3D apiladas aplanando cada pila en una imagen RGBA usando un `StackColorMapper`.
* - [ImageURL](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/image_url.html)(*args:Any,id:ID|None=None, ...)
  - Renderiza imágenes cargadas de URL dadas.
* - **Texto y anotaciones**
  -
* - [MathMLGlyph](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/math_ml.html)(*args:Any,id:ID|None=None, ...)
  - Renderiza contenido matemático usando `MathMLnotation`.
* - [MathTextGlyph](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/math_text.html)(*args:Any,id:ID|None=None, ...)
  - Clase base para _glyphs_ de texto de matemáticas.
* - [TeXGlyph](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/tex.html)(*args:Any,id:ID|None=None, ...)
  - Renderiza contenido matemático usando _LaTeXnotation_.
* - [Text](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/text.html)(*args:Any,id:ID|None=None, ...)
  - Renderiza texto en una ubicación específica.
* - **Polígonos**
  -
* - [Block](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/block.html)(*args:Any,id:ID|None=None, ...)
  - Renderiza regiones rectangulares, dada una coordenada de esquina inferior izquierda, ancho y altura.
* - [HexTile](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/hex_tile.html)(*args:Any,id:ID|None=None, ...)
  - Renderiza baldosas horizontales en una cuadrícula hexagonal regular.
* - [MultiPolygons](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/multi_polygons.html)(*args:Any,id:ID|None=None, ...)
  - Renderiza varios `MultiPolygon`.
* - [Ngon](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/ngon.html)(*args:Any,id:ID|None=None, ...)
  - Renderiza polígonos regulares de n-lados.
* - [Patch](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/patch.html)(*args:Any,id:ID|None=None, ...)
  - Renderiza un solo _patch_. Un solo polígono definido por una secuencia de puntos.
* - [Patches](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/patches.html)(*args:Any,id:ID|None=None, ...)
  - Renderiza varios _patches_. Conjunto de múltiples polígonos independientes.
* - [Rect](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/rect.html)(*args:Any,id:ID|None=None, ...)
  - Renderiza rectángulos, caracterizados por la posición central _(x, y)_, ancho, altura y ángulo de rotación.
```

<br/>

### Glyph

Clase base para todos los modelos de _glyph_.

```{list-table}
:header-rows: 1

* - class
  - Descripción
* - [Glyph](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs.html#bokeh.models.Glyph)(*args: Any, id: ID | None = None, ...)
  - Clase base para todos los modelos de _glyph_.
```

#### Atributos

Atributos de la clase `Glyph`. 

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - [decorations](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs.html#bokeh.models.Glyph.decorations)
  - Una colección de decoraciones del _glyph_, ejm. cabeza de flechas.
* - [name](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs.html#bokeh.models.Glyph.name)
  - Un nombre arbitrario y suministrado por el usuario para este modelo.
* - [syncable](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs.html#bokeh.models.Glyph.syncable)
  - Indica si este modelo debe sincronizarse de nuevo a un servidor _bokeh_ cuando se actualiza en un navegador web.
* - [tags](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs.html#bokeh.models.Glyph.tags)
  - Una `list` opcional de valores arbitrarios, proporcionados por el usuario para adjuntar a este modelo.
```

<br/>

#### Propiedades

Propiedades de la clase `Glyph`. 

```{list-table}
:header-rows: 1

* - Propiedad
  - Descripción
* - **document: Document | None**
  - El documento al que se adjunta este modelo (puede ser `None`).
```

(Glyph-methods)=
#### Métodos

Métodos de la clase `Glyph`. 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [apply_theme](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs.html#bokeh.models.Glyph.apply_theme)(property_values: dict[str, Any])
  - Aplica un conjunto de valores del tema que se utilizará en lugar de los valores predeterminados, pero no sobreescribirán los valores del conjunto de aplicaciones.
* - [clone](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs.html#bokeh.models.Glyph.clone)(**overrides: Any)
  - Duplica un objeto _HasProps_.
* - [destroy](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs.html#bokeh.models.Glyph.destroy)()
  - Limpia las referencias al documento y la propiedad.
* - [equals](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs.html#bokeh.models.Glyph.equals)(other: HasProps)
  - Igualdad estructural de modelos.
* - [js_link](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs.html#bokeh.models.Glyph.js_link)(attr: str, other: Model, ...)
  - Enlaza dos propiedades del modelo bokeh usando JavaScript.
* - [js_on_change](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs.html#bokeh.models.Glyph.js_on_change)(event: str, ...)
  - Adjunta una devolución de llamada CustomJS a un evento de modelo arbitrario.
* - [on_change](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs.html#bokeh.models.Glyph.on_change)(attr: str, ...)
  - Agrega una devolución de llamada en este objeto para activar cuando _attr_ cambia.
* - [on_event](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs.html#bokeh.models.Glyph.on_event)(event: str | type[Event], ...)
  - Ejecuta devoluciones de llamada cuando el evento especificado ocurre en este modelo.
* - [properties_with_values](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs.html#bokeh.models.Glyph.properties_with_values)(, ...)
  - Colecta un `dict` de nombres de propiedad a sus valores.
* - [query_properties_with_values](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs.html#bokeh.models.Glyph.query_properties_with_values)(...)
  - Consulta los valores de propiedades de las instancias de _HasProps_ con un predicado.
* - [references](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs.html#bokeh.models.Glyph.references)()
  - Retorna todos los modelos a los que este objeto tiene referencias.
* - [remove_on_change](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs.html#bokeh.models.Glyph.remove_on_change)(attr: str, ...)
  - Elimina una devolución de llamada de este objeto.
* - [select](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs.html#bokeh.models.Glyph.select)(selector: SelectorType)
  - Consulta este objeto y todas sus referencias para objetos que coincidan con el selector dado.
* - [select_one](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs.html#bokeh.models.Glyph.select_one)(selector: SelectorType)
  - Consulta este objeto y todas sus referencias para objetos que coincidan con el selector dado. Plantea un error si se encuentra más de un objeto. Retorna un solo objeto coincidente, o `None` si no se encuentra nada.
* - [set_from_json](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs.html#bokeh.models.Glyph.set_from_json)(name: str, value: Any, ...)
  - Establece un valor de propiedad en este objeto de JSON.
* - [set_select](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs.html#bokeh.models.Glyph.set_select)(...)
  - Actualiza objetos que coincidan con un selector dado con las actualizaciones de atributo/valor especificadas.
* - [themed_values](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs.html#bokeh.models.Glyph.themed_values)()
  - Retorna cualquier sobreescritura proporcionada por el tema.
* - [to_serializable](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs.html#bokeh.models.Glyph.to_serializable)(serializer: Serializer)
  - Convierte este objeto en una representación serializable.
* - [trigger](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs.html#bokeh.models.Glyph.trigger)(attr: str, old: Any, new: Any, ...)
  - .
* - [unapply_theme](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs.html#bokeh.models.Glyph.unapply_theme)()
  - Elimina los valores temáticos y restaura los valores predeterminados.
* - [update](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs.html#bokeh.models.Glyph.update)(**kwargs: Any)
  - Actualiza las propiedades del objeto de los argumentos de palabras clave dados.
```

<br/>

(Glyph-class-methods)=
#### Métodos de Clase

Métodos de clase de la clase `Glyph`. Estos métodos se aplican sobre la clase misma y no sobre sus instancias.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [clear_extensions](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs.html#bokeh.models.Glyph.clear_extensions)()
  - Borra las extensiones personalizadas actualmente definidas.
* - [dataspecs](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs.html#bokeh.models.Glyph.dataspecs)()
  - Recopila los nombres de todas las propiedades de _DataSpec_ en esta clase.
* - [descriptors](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs.html#bokeh.models.Glyph.descriptors)()
  - Lista de descriptores de propiedades en el orden de definición.
* - [lookup](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs.html#bokeh.models.Glyph.lookup)(name: str, ...)
  - Encuentra el `PropertyDescriptor` para una propiedad en una clase, dado el nombre de la propiedad.
* - [parameters](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs.html#bokeh.models.Glyph.parameters)()
  - Genera valores de parámetros de Python adecuados para funciones que se derivan del _glyph_.
* - [properties](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs.html#bokeh.models.Glyph.properties)(, ...)
  - Recopila los nombres de las propiedades en esta clase.
* - [properties_with_refs](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs.html#bokeh.models.Glyph.properties_with_refs)()
  - Recopila los nombres de todas las propiedades en esta clase que también tienen referencias.
```

<br/>

### Circle

Renderiza marcadores de círculo.

```{list-table}
:header-rows: 1

* - class
  - Descripción
* - [Circle](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/circle.html#bokeh.models.Circle)(*args: Any, id: ID | None = None, ...)
  - Renderiza marcadores de círculo.
```


#### Atributos

Atributos de la clase `Circle`. 

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - [decorations](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/circle.html#bokeh.models.Circle.decorations)
  - Una colección de decoraciones del _glyph_, ejm. cabeza de flechas.
* - [fill_alpha](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/circle.html#bokeh.models.Circle.fill_alpha)
  - Los valores alfa de relleno para los círculos.
* - [fill_color](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/circle.html#bokeh.models.Circle.fill_color)
  - Los valores de color de relleno para los círculos.
* - [hatch_alpha](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/circle.html#bokeh.models.Circle.hatch_alpha)
  - Los valores alfa del _hatch_ para los círculos.
* - [hatch_color](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/circle.html#bokeh.models.Circle.hatch_color)
  - El color del _hatch_ para los círculos.
* - [hatch_extra](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/circle.html#bokeh.models.Circle.hatch_extra)
  - Valores adicionales del _hatch_ para los círculos.
* - [hatch_pattern](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/circle.html#bokeh.models.Circle.hatch_pattern)
  - Los valores del patrón del _hatch_ para los círculos.
* - [hatch_scale](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/circle.html#bokeh.models.Circle.hatch_scale)
  - Los valores de la escala del _hatch_ para los círculos.
* - [hatch_weight](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/circle.html#bokeh.models.Circle.hatch_weight)
  - Los valores de peso del _hatch_ para los círculos.
* - [hit_dilation](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/circle.html#bokeh.models.Circle.hit_dilation)
  - El factor para dilatar el radio de _hit_ para las herramientas de desplazamiento y toque. Hacer este valor más grande hace que las herramientas sean "más sensibles".
* - [line_alpha](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/circle.html#bokeh.models.Circle.line_alpha)
  - El alfa de las líneas para los círculos.
* - [line_cap](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/circle.html#bokeh.models.Circle.line_cap)
  - Los valores de _cap_ de línea para los círculos.
* - [line_color](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/circle.html#bokeh.models.Circle.line_color)
  - Los valores de color de línea para los círculos.
* - [line_dash](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/circle.html#bokeh.models.Circle.line_dash)
  - El tipo de línea para los círculos.
* - [line_dash_offset](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/circle.html#bokeh.models.Circle.line_dash_offset)
  - Las separaciones en los _dashes_ de línea para los círculos.
* - [line_join](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/circle.html#bokeh.models.Circle.line_join)
  - Los valores de unión de línea para los círculos.
* - [line_width](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/circle.html#bokeh.models.Circle.line_width)
  - Los valores de ancho de línea para los círculos.
* - [name](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/circle.html#bokeh.models.Circle.name)
  - Un nombre arbitrario y suministrado por el usuario para este modelo.
* - [radius](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/circle.html#bokeh.models.Circle.radius)
  - Los valores de radio para círculos (en unidades de datos, por defecto).
* - [radius_dimension](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/circle.html#bokeh.models.Circle.radius_dimension)
  - Qué dimensión medir los radios del círculo a lo largo.
* - [radius_units](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/circle.html#bokeh.models.Circle.radius_units)
  - Unidades para usar para la propiedad asociada: _screen_ o _data_.
* - [syncable](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/circle.html#bokeh.models.Circle.syncable)
  - Indica si este modelo debe sincronizarse de nuevo a un servidor bokeh cuando se actualiza en un navegador web.
* - [tags](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/circle.html#bokeh.models.Circle.tags)
  - Una `list` opcional de valores arbitrarios, proporcionados por el usuario para adjuntar a este modelo.
* - [x](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/circle.html#bokeh.models.Circle.x)
  - Las coordenadas _x_ del centro de los círculos.
* - [y](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/circle.html#bokeh.models.Circle.y)
  - Las coordenadas _y_ del centro de los círculos. The y-coordinates of the center of the circles.
```
<br/>

#### Propiedades

Propiedades de la clase `Circle`. 

```{list-table}
:header-rows: 1

* - Propiedad
  - Descripción
* - **document: Document | None**
  - El documento al que se adjunta este modelo (puede ser `None`).. The Document this model is attached to (can be None).
```

<br/>

#### Métodos

Métodos de la clase `Circle`. 

:::{note}
Ver {ref}`Glyph-methods`
:::


<br/>

#### Métodos de Clase

Métodos de clase de la clase `Circle`. Estos métodos se aplican sobre la clase misma y no sobre sus instancias.

:::{note}
Ver {ref}`Glyph-class-methods`
:::

<br/>

## Line

Renderiza una sola línea.

```{list-table}
:header-rows: 1

* - class
  - Descripción
* - [Line](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/line.html#bokeh.models.Line)(*args: Any, id: ID | None = None, **kwargs: Any)
  - Renderiza una sola línea.
```

<br/>

### Atributos

Atributos de la clase `Line`. 

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - [decorations](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/line.html#bokeh.models.Line.decorations)
  - Una colección de decoraciones del _glyph_, ejm. cabeza de flechas.
* - [line_alpha](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/line.html#bokeh.models.Line.line_alpha)
  - El alfa de las líneas para la línea.
* - [line_cap](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/line.html#bokeh.models.Line.line_cap)
  - Los valores de _cap_ de línea para la línea.
* - [line_color](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/line.html#bokeh.models.Line.line_color)
  - Los valores de color de línea para la línea.
* - [line_dash](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/line.html#bokeh.models.Line.line_dash)
  - El tipo de línea para para la línea.
* - [line_dash_offset](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/line.html#bokeh.models.Line.line_dash_offset)
  - Las separaciones en los _dashes_ de línea para la línea.
* - [line_join](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/line.html#bokeh.models.Line.line_join)
  - Los valores de unión de línea para la línea.
* - [line_width](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/line.html#bokeh.models.Line.line_width)
  - Los valores de ancho de línea para la línea.
* - [name](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/line.html#bokeh.models.Line.name)
  - Un nombre arbitrario y suministrado por el usuario para este modelo.
* - [syncable](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/line.html#bokeh.models.Line.syncable)
  - Indica si este modelo debe sincronizarse de nuevo a un servidor bokeh cuando se actualiza en un navegador web.
* - [tags](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/line.html#bokeh.models.Line.tags)
  - Una `list` opcional de valores arbitrarios, proporcionados por el usuario para adjuntar a este modelo.
* - [x](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/line.html#bokeh.models.Line.x)
  - Las coordenadas _x_ para los puntos de la línea.
* - [y](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/line.html#bokeh.models.Line.y)
  - Las coordenadas _y_ para los puntos de la línea.
```

<br/>

### Propiedades

Propiedades de la clase `Line`. 

```{list-table}
:header-rows: 1

* - Propiedad
  - Descripción
* - **document: Document | None**
  - El documento al que se adjunta este modelo (puede ser `None`).
```

<br/>

### Métodos

Métodos de la clase `Line`. 

:::{note}
Ver {ref}`Glyph-methods`
:::

<br/>

### Métodos de Clase

Métodos de clase de la clase `Line`. Estos métodos se aplican sobre la clase misma y no sobre sus instancias.

:::{note}
Ver {ref}`Glyph-class-methods`
:::