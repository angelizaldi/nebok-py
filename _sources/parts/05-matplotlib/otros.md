# Otras Clases

En esta sección se presentan los atributos de otras clases comúnes, que aunque normalmente no se trabaja con ellas directamente, son retornadas por algunas métodos de los objetos `Axes` y `Figure`. 

## Artist

[Artist](https://matplotlib.org/stable/api/artist_api.html#artist-class) es la clase base para todos los elementos visuales en `Matplotlib`.

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - [agg_filter](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_agg_filter.html)
  - una función de filtro, que toma un arreglo _(m, n, 3)_ de `float` y un valor _dpi_, y devuelve un arreglo _(m, n, 3)_ y dos desplazamientos desde la esquina inferior izquierda de la imagen.
* - [alpha](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_alpha.html)
  - escalar o `None`. Para indicar la opacidad de la figura. Es un valor entre 0 y 1, donde 0 es completamente transparente y 1 es completamente opaco.
* - [animated](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_animated.html)
  - `bool`. Indica si la figura se pretende usar en una animación
* - [clip_box](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_box.html)
  - `BboxBase` o `None`. Establece el _clip_ `Bbox`.
* - [clip_on](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_on.html)
  - `bool`. Indica si la figura usa _clipping_.
* - [clip_path](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_path.html)
  - `Patch` o `(Path, Transform)` o `None`. Establece el _clip path_.
* - [figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_figure.html)
  - `Figure`. Instancia `Figure` a la que el _artist_ pertenece.
* - [gid](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_gid.html)
  - `str`. "id" del grupo del _artist_.
* - [in_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_in_layout.html)
  - `bool`. Indica si el _artist_ se debe incluir en el _layout_.
* - [label](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_label.html)
  - `str`. Etiqueta que aparecerá en la leyenda.
* - [mouseover](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_mouseover.html)
  - `bool`. Indica si este _artist_ es _queried_ cuando el cursor del mouse pasa por encima.  
* - [path_effects](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_path_effects.html)
  - `list` de `AbstractPathEffect`. Establece los _path effects_.
* - [picker](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_picker.html)
  - `None`, `bool`, `float` or _callable_. Define el comportamiento _picking_ del _artist_.
* - [rasterized](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_rasterized.html)
  - `bool`. Indica si se debe forzar _rasterizar_ el _output_ para gráficos de vectores.
* - [sketch_params](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_sketch_params.html)
  - (scale: `float`, length: `float`, randomness: `float`). Establece los parámetros del _sketch_.
* - [snap](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_snap.html)
  - `bool` o `None`. Establece el comportamiento del _snapping_.
* - [transform](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_transform.html)
  - `Transform`. Establece el transformador del _artist_.
* - [url](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_url.html)
  - `str`. Establece el url del _artist_.
* - [visible](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_visible.html)
  - `bool`. Indica la visibilidad del _artist_
* - [zorder](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_zorder.html)
  - `float`. Establece el _zorder_ del _artist_. _Artists_ con _zorder_ menores son graficados primero. Útil para establecer la jerarquía de los objetos en el _eje z_.
```

<br/>

---
(matplotlib-line2d)=
## Line2D

[Line2D](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html) es una clase contenida en el módulo `matplotlib.lines`, y es retornada por diversas funciones como `plt.plot()`. Representa líneas 2D en las gráficas.

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - [antialiased | aa](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_antialiased)
  - `bool`. Indica si se debe usar _antialiased rendering_.
* - [color | c](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_color)
  - {ref}`matplotlib-color`. Color de las líneas.
* - [dash_capstyle](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_dash_capstyle)
  - `CapStyle` o `{'butt', 'projecting', 'round'}`. Indica como dibujar las últimas _caps_ si la línea es _is_dashed_.
* - [dash_joinstyle](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_dash_joinstyle)
  - `JoinStyle` o {'miter', 'round', 'bevel'}. Indica como unir los segmentos de las líneas si la línea es _is_dashed_
* - [dashes](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_dashes)
  - `sequence` de `float` (on/off ink in points) o `(None, None)`. Establece el patrón de la línea.
* - [data](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_data)
  - _(2, N) array_ o dos 1D _arrays_. Datos del eje _x_ y _y_.
* - [drawstyle | ds](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_drawstyle)
  - {'default', 'steps', 'steps-pre', 'steps-mid', 'steps-post'}, _default_: 'default'. Determina como se unen los puntos que conforman la línea, por default son interpolaciones lineales.
* - [fillstyle](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_fillstyle)
  - {'full', 'left', 'right', 'bottom', 'top', 'none'}. Indica el estilo de relleno de los marcadores.
* - [gapcolor](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_gapcolor)
  - {ref}`matplotlib-color` o `None`. Establece cómo rellenar los espacios en una línea intermitente.
* - [gid](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_gid.html)
  - `str`. "id" del grupo del _artist_.
* - [linestyle | ls](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_linestyle)
  - {'-', '--', '-.', ':', '', (offset, on-off-seq), ...}. Estilo de las {ref}`matplotlib-lines`. Para no imprimir líneas usar una cadena vacía `''` o `None`. También se puede usar líneas con nombre. 
* - [linewidth | lw](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_linewidth)
  - `float`. Especifica el grueso de la línea en puntos.
* - [marker](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_marker)
  - _marker style string_, `Path` or `MarkerStyle`. Tipo de {ref}`matplotlib-markers` en la gráfica.
* - [markeredgecolor | mec](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_markeredgecolor)
  - {ref}`matplotlib-color`: Color del borde del marker. 
* - [markeredgewidth | mew](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_markeredgewidth)
  - `float`. Ancho del borde del marker en puntos
* - [markerfacecolor | mfc](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_markerfacecolor)
  - {ref}`matplotlib-color`. Color del interior del marker.
* - [markerfacecoloralt | mfcalt](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_markerfacecoloralt)
  - {ref}`matplotlib-color`. Color alternativo del interior del marker.
* - [markersize | ms](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_markersize)
  - `float`. Tamaño del marker en puntos.
* - [markevery](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_markevery)
  - `None`, `int`, `(int, int)`, _slice_, `list[int]`, `float`, `(float, float)` o `list[bool]`. Establece la propiedad _markvery_ para muestras los puntos cuando se usan _markers_.
* - [picker](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_picker)
  - `float` o `callable[[Artist, Event], tuple[bool, dict]]`. Establece el evento _picker_ para la línea.
* - [pickradius](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_pickradius)
  - `float`. Radio del _pick_.
* - [solid_capstyle](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_solid_capstyle)
  - {'butt', 'projecting', 'round'}. Indica como dibujar los extremos de una línea sólida.
* - [solid_joinstyle](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_solid_joinstyle)
  - `JoinStyle` o {'miter', 'round', 'bevel'}. Indica cómo unir los segmentos si la línea es sólida.
* - [xdata](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_xdata)
  - 1D _array_. Datos del eje _x_.
* - [ydata](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_ydata)
  - 1D _array_. Datos del eje _y_.
```

<br/>

---
(matplotlib-text)=
## Text

[Text](https://matplotlib.org/stable/api/text_api.html) es una clase contenida en el módulo `matplotlib.text`, y es retornada por diversas funciones como `plt.title()`, `plt.xlabel()`, `plt.ylabel()`, etc. Representa texto en las gráficas.

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - [antialiased](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_antialiased)
  - `bool`. Indica si se debe usar _antialiased rendering_.
* - [backgroundcolor](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_backgroundcolor)
  - {ref}`matplotlib-color`. Color de fondo del texto. 
* - [bbox](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_bbox)
  - `dict` con propiedades para `patches.FancyBboxPatch`. Rectángulo contenedor del texto.
* - [color | c](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_color)
  - {ref}`matplotlib-color`. Color del texto.
* - [fontfamily | family | fontname](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontfamily)
  - {_fontname_, 'serif', 'sans-serif', 'cursive', 'fantasy', 'monospace'}. Familia del texto
* - [fontproperties 1 font 1 font_properties](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontproperties)
  - `font_manager.FontProperties`, `str` o `pathlib.Path`. Propiedades de la fuente.
* - [fontsize | size](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontsize)
  - `float` o {'xx-small', 'x-small', 'small', 'medium', 'large', 'x-large', 'xx-large'}: Tamaño de la fuente
* - [fontstretch | stretch](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontstretch)
  - {valor numérico entre [0,1000], 'ultra-condensed', 'extra-condensed', 'condensed', 'semi-condensed', 'normal', 'semi-expanded', 'expanded', 'extra-expanded', 'ultra-expanded'}: Expansión horizontal del texto.
* - [fontstyle | style](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontstyle)
  - {'normal', 'italic', 'oblique'}. Estilo del texto.
* - [fontvariant | variant](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontvariant)
  - {'normal', 'small-caps'}. Variación de la fuente.
* - [fontweight 1 weight](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontweight)
  - {valor numérico entre [0,1000], 'ultralight', 'light', 'normal', 'regular', 'book', 'medium', 'roman', 'semibold', 'demibold', 'demi', 'bold', 'heavy', 'extra bold', 'black'}. Ancho de la fuente.
* - [horizontalalignment | ha](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_horizontalalignment)
  - {'left', 'center', 'right'}. Alineación horizontal.
* - [linespacing](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_linespacing)
  - `float`. Espaciamiento del texto, representa un múltiplo del tamaño de la fuente.
* - [math_fontfamily](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_math_fontfamily)
  - `str`. Nombre de la familia para textos matemáticos.
* - [multialignment or ma](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_multialignment)
  - {'left', 'right', 'center'}. Alineación para textos multilíneas
* - [parse_math](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_parse_math)
  - `bool`.
* - [position](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_position)
  - (float, float). Posición del texto
* - [rotation](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_rotation)
  - `float` o {'vertical', 'horizontal'}. Rotación del texto. Si es `float` reprente grados en sentido contrario a las manecillas del reloj.
* - [rotation_mode](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_rotation_mode)
  - {None, 'default', 'anchor'}. Modo de roración del texto.
* - [text](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_text)
  - `object`. Texto.
* - [transform_rotates_text](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_transform_rotates_text)
  - `bool`. Indica de las rotaciones del transformador afectan la dirección del texto.
* - [usetex](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_usetex)
  - `bool` o `None`.
* - [verticalalignment or va](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_verticalalignment)
  - {'baseline', 'bottom', 'center', 'center_baseline', 'top'}. Alineación verticla del texto.
* - [wrap](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_wrap)
  - `bool`. Para indicar si ajustar el texto.
* - [x](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_x)
  - `float`. Posición _x_ del texto.
* - [y](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_y)
  - `float`. Posición _y_ del texto.
```

<br/>

---
(matplotlib-patch)=
## Patch

[Patch](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch) es una clase contenida en el módulo `matplotlib.patches`, y sus propiedades se pueden utilizar en el objeto retornado por `plt.arrow()`. Representa figuras geométricas en las gráficas.

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - [antialiased | aa](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_antialiased)
  - `bool` o `None`. Indica si se debe usar _antialiased rendering_.
* - [capstyle](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_capstyle)
  - `CapStyle` o {'butt', 'projecting', 'round'}. Establece el _capstyle_
* - [color](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_color)
  - {ref}`matplotlib-color`. Color del borde y relleno.
* - [edgecolor | ec](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_edgecolor)
  - {ref}`matplotlib-color` o `None`. Color del borde.
* - [facecolor | fc](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_facecolor)
  - {ref}`matplotlib-color` o `None`. Color del relleno
* - [fill](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_fill)
  - `bool`. Indica si se debe de rellenar.
* - [hatch](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_hatch)
  - {'/', '\', '|', '-', '+', 'x', 'o', 'O', '.', '*'}. Establece el patrón _hatching_.
* - [joinstyle](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_joinstyle)
  - `JoinStyle` o {'miter', 'round', 'bevel'}. Establece el _JoinStyle_.
* - [linestyle | ls](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_linestyle)
  - {'-', '--', '-.', ':', '', (offset, on-off-seq), ...}. Estilo de las {ref}`matplotlib-lines`.
* - [linewidth or lw](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_linewidth)
  - `float` o `None`. Ancho del _patch_ en puntos.
```

<br/>

---
(matplotlib-rectangle)=
## Rectangle

[Rectangle](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html) es una clase contenida en el módulo `matplotlib.patches`, y es retornada por diversas funciones como `plt.hist()`, `plt.bar()`, etc. Es una subclase de `Patch` y representa un rectángulo

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - [antialiased or aa](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html)
  - `bool` o `None`.. `bool` or `None`.
* - [capstyle](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html)
  - `CapStyle` o {'trasero', 'proyectando', 'redondo'}.
* - [color](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html)
  - {ref}`matplotlib-color`.
* - [edgecolor or ec](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html)
  - {ref}`matplotlib-color` o `None`.
* - [facecolor or fc](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html)
  - {ref}`matplotlib-color` o `None`.
* - [fill](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html)
  - `bool`.. `bool`.
* - [hatch](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html)
  - {'/', '\', '|', '-', '+', 'x', 'o', 'O', '.', '*'}.
* - [joinstyle](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html)
  - `JoinStyle` o {'inglete', 'redondo', 'bisel'}.. `JoinStyle` or {'miter', 'round', 'bevel'}.
* - [linestyle | ls](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html)
  - {'-', '--', '-.', ':', '', _(offset, on-off-seq)_, ...}. Estilo de las {ref}`matplotlib-lines`.
* - [linewidth | lw](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html)
  - `float` o `None`.
```