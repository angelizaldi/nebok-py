# Figure

`matplotlib.figure` es un módulo que impleta las clases `Figure` y `SubFigure`. En esta sección únicamente se enlistan las propiedades y algunos métodos de la clase `Figure`. Para información sobre cómo crear y manipular instancias de la clase `Figure` consultar {doc}`./matplotlib-index`.

---
## Constructor de Figure

Es el `Artist` de nivel superior, que contiene todos los elementos de la gráfica. 

:::{warning}
Los usuarios no deben inicializar objetos `Figure` directamente, sino que se deben de utilizar métodos que retornen objetos `Figure` como los del módulo {doc}`./pyplot`.
:::

```{list-table}
:header-rows: 1

* - Constructor
  - Descripción
* - [Figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html)(figsize=None, dpi=None, ...)
  - El contenedor de nivel superior para todos los elementos de la gráfica.
```

<br/>

---
## Atributos

En `matplotlib` no se puede acceder directamente a los atributos por medio de la notación punto. Para modificar o retornar los atributos es necesario usar los métodos `Figure.set_*` y `Figure.get_*`. A continuación se presenta una tabla de los atributos de `Figure`.

```{note}
Los atributos se pueden definir como parámetros dentro de la función `plt.figure()`. Para ver los tipos de datos de los argumentos o las maneras de definirlos consultar [la tabla de parámetros](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure). 
```

```{note}
Muchos atributos son heredados de la clase `Artist`. 
```

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - [agg_filter](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_agg_filter.html)
  - Filtro del gráfico.
* - [alpha](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_alpha.html)
  - Transparencia de la figura (0 es transparente, 1 es opaco).
* - [animated](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_animated.html)
  - Indica si el gráfico es animado o no.
* - [canvas](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.set_canvas.html)
  - Canvas de la figura.
* - [clip_box](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_box.html)
  - Indica el área de recorte para los gráficos.
* - [clip_on](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_on.html)
  - Indica si se aplican recortes al gráfico.
* - [clip_path](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_path.html)
  - Indica la ruta de recorte para los gráficos.
* - [dpi](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.set_dpi.html)
  - Resolución de la figura en puntos por pulgada.
* - [edgecolor](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.FigureBase.set_edgecolor)
  - Color del borde del rectángulo de la figura.
* - [facecolor](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.FigureBase.set_facecolor)
  - Color de fondo del rectángulo de la figura.
* - [figheight](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.set_figheight.html)
  - Altura de la figura en pulgadas.
* - [figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_figure.html)
  - Referencia a la figura contenedora del gráfico.
* - [figwidth](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.set_figwidth.html)
  - Ancho de la figura en pulgadas.
* - [frameon](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.FigureBase.set_frameon)
  - Indica la visibilidad del fondo de la figura.
* - [gid](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_gid.html)
  - ID único para el gráfico, útil para identificaciones.
* - [in_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_in_layout.html)
  - Indica si los ejes participan en el diseño de la figura.
* - [label](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_label.html)
  - Etiqueta del gráfico, utilizada en leyendas.
* - [layout_engine](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.set_layout_engine.html)
  - Indica el _engine_ del diseño de la figura.
* - [linewidth](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.FigureBase.set_linewidth)
  - Grosor de la línea del rectángulo de la figura.
* - [mouseover](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_mouseover.html)
  - Indica si están activos los eventos al pasar el ratón sobre el gráfico.
* - [path_effects](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_path_effects.html)
  - Efectos de estilo aplicados a los gráficos.
* - [picker](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_picker.html)
  - Habilita la selección de elementos en el gráfico.
* - [rasterized](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_rasterized.html)
  - Define cuándo rasterizar según el orden z.
* - [size_inches](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.set_size_inches.html)
  - Establece el tamaño de la figura en pulgadas.
* - [sketch_params](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_sketch_params.html)
  - Parámetros para dar un efecto de boceto al gráfico.
* - [snap](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_snap.html)
  - Ajuste de las coordenadas a los píxeles más cercanos.
* - [transform](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_transform.html)
  - Transformación aplicada a los datos del gráfico.
* - [url](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_url.html)
  - URL asociada al gráfico, útil para interactividad.
* - [visible](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_visible.html)
  - Indica si el gráfico es visible.
* - [zorder](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_zorder.html)
  - Orden de dibujo del gráfico sobre otros elementos.
```

<br/>

(matplotlib-figure-metodos)=
## Métodos

A continuación se enlistas los métodos de la clase `Figure` por categorías.

```{attention}
Al utilizar los métodos tener en cuenta:
- Para utilizar los métodos, _fig_ tuvo que haber sido asignada a una variable. 
- En esta sección se enlistan solo algunos de los métodos de la clase `Figure`. Para una lista completa consultar la [documentación](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.Figure) de `matplotlib`. Tener en cuenta que en la documentación los métodos no están resumidos en una tabla, sino que se presentan a lo largo de toda la sección.
```

### Apariencia

Métodos para recuperar o modificar la apariencia de la figura.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - **Establecer**
  -
* - [Figure.set_edgecolor](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.set_edgecolor.html)(color)
  - Establece el color del borde de la `Figure`.
* - [Figure.set_facecolor](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.set_facecolor.html)(color)
  - Establece el color de la cara del `Figure` rectángulo.
* - [Figure.set_frameon](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.set_frameon.html)(b)
  - Establece la visibilidad del fondo de la figura.
* - [Figure.set_linewidth](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.set_linewidth.html)(linewidth)
  - Establece el ancho de línea del rectángulo de la `Figure`.
* - **Recuperar**
  -
* - [Figure.get_edgecolor](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.get_edgecolor.html)()
  - Retorna el color del borde de la `Figure`.
* - [Figure.get_facecolor](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.get_facecolor.html)()
  - Retorna el color de la cara de la `Figure`.
* - [Figure.get_frameon](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.get_frameon.html)()
  - Retorna la visibilidad del fondo de la figura.
* - [Figure.get_linewidth](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.get_linewidth.html)()
  - Retorna el ancho de línea del rectángulo la `Figure`.
```

### Artists

Son métodos relacionados con agregar o retornar _artists_ existentes en la figura. 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [Figure.add_artist](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_artist.html)(artist, clip=False)
  - Agrega un `Artist` a la figura.
* - [Figure.figimage](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.figimage.html)(X, xo=0, yo=0, alpha=None, norm=None, cmap=None, vmin=None, vmax=None, origin=None, resize=False, **kwargs)
  - Añade una imagen _non-resampled_ a la figura.
* - [Figure.get_children](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.get_children.html)()
  - Retorna una `list` de los _artists_ contenidos en la figura.
```

<br/>

---
### Diseño de _subplots_

Funciones para establecer el _layout_ de múltiples gráficas.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - **Establecer**
  -
* - [Figure.set_layout_engine](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.set_layout_engine.html)(layout=None, **kwargs)
  - Establece el motor de diseño para esta figura.
* - [Figure.subplots_adjust](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots_adjust.html)(left=None, bottom=None, right=None, top=None, wspace=None, hspace=None)
  - Ajusta los parámetros de diseño de los _subplots_.
* - [Figure.tight_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.tight_layout.html)(*, pad=1.08, h_pad=None, w_pad=None, rect=None)
  - Ajusta de la mejor manera el espacio entre y alrededor de los _subplots_.
* - **Recuperar**
  -
* - [Figure.get_constrained_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.get_constrained_layout.html)()
  - Indica si se está utilizando un diseño restringido.
* - [Figure.get_tight_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.get_tight_layout.html)()
  - Indica si `Figure.tight_layout` es llamado al graficarse la figura.
```

<br/>

### Ejes y subfiguras

Son métodos relacionados con añadir y retornar _axes_ de la figura. 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [Figure.add_axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_axes.html)(*args, **kwargs)
  - Agrega un `Axes` a la figura.
* - [Figure.add_gridspec](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_gridspec.html)(nrows=1, ncols=1, **kwargs)
  - API de bajo nivel para crear un `GridSpec` que tiene a esta figura como padre.
* - [Figure.add_subfigure](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subfigure.html)(subplotspec, **kwargs)
  - Agrega un `SubFigure` a la figura como parte de un arreglo de subgráficas.
* - [Figure.add_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html)(*args, **kwargs)
  - Agrega un `Axes` a la figura como parte de un arreglo de subgráficas.
* - [Figure.axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.axes.html)()
  - Enlista los `Axes` en el `Figure`.
* - [Figure.delaxes](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.delaxes.html)(ax)
  - Elimina el `Axes` _ax_ de la figura o actualiza el actual `Axes`.
* - [Figure.get_axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.get_axes.html)()
  - Enlista de `Axes` en el `Figure`.
* - [Figure.subfigures](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subfigures.html)(nrows=1, ncols=1, squeeze=True, wspace=None, ...)
  - Agrega un `set` de subfiguras a esta figura.
* - [Figure.subplot_mosaic](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplot_mosaic.html)(mosaic, ...)
  - Construye un diseño de `Axes` basado en arte ASCII o listas anidadas.
* - [Figure.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots.html)(nrows=1, ncols=1, ...)
  - Agrega un `set` de subgráficas a esta figura.
```

<br/>

### Etiquetas y Anotaciones

A continuación se enlistan los métodos relacionados con etiquetas, títulos y otras anotaciones que se pueden hacer a las figuras. 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [Figure.align_labels](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.align_labels.html)(axs=None)
  - Alinea las etiquetas _x_ y _y_ de los _subplots_ con la misma fila o columna (respectivamente).
* - [Figure.align_titles](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.align_titles.html)(axs=None)
  - Alinea los títulos de los _subplots_ en la misma fila.
* - [Figure.align_xlabels](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.align_xlabels.html)(axs=None)
  - Alinea las etiquetas _x_ de los _subplots_ en la misma fila 
* - [Figure.align_ylabels](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.align_ylabels.html)(axs=None)
  - Alinee las etiquetas _y_ de los _subplots_ en la misma columna.
* - [Figure.autofmt_xdate](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.autofmt_xdate.html)(bottom=0.2, rotation=30, ha='right', which='major')
  - Rota y alinea a la derecha las etiquetas de los _ticks_ de fechas para evitar que se solapen.
* - [Figure.colorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.colorbar.html)(mappable, cax=None, ax=None, use_gridspec=True, **kwargs)
  - Agrega una barra de colores a un gráfico.
* - [Figure.get_suptitle](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.get_suptitle.html)()
  - Retorna el subtítulo como cadena o una cadena vacía si no se estableció.
* - [Figure.get_supxlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.get_supxlabel.html)()
  - Retorna la _supxlabel_ como cadena o una cadena vacía si no `estableció.
* - [Figure.get_supylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.get_supylabel.html)()
  - Retorna la etiqueta _supylabel_ como cadena o una cadena vacía si no estableció.
* - [Figure.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.legend.html)(*args, **kwargs)
  - Añade una leyenda a la figura.
* - [Figure.suptitle](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.suptitle.html)(t, **kwargs)
  - Añade un subtítulo centrado a la figura.
* - [Figure.supxlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.supxlabel.html)(t, **kwargs)
  - Añade una etiqueta _supxlabel_ centrada a la figura.
* - [Figure.supylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.supylabel.html)(t, **kwargs)
  - Añade una etiqueta _supylabel_ centrada a la figura.
* - [Figure.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.text.html)(x, y, s, fontdict=None, **kwargs)
  - Añade texto a la figura.
```

<br/>

### Guardar

Métodos relacionados para guardar la figura. 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [Figure.savefig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_axobserver.html)(fname, *, transparent=None, **kwargs)
  - Almacena la figura como una imagen o un gráfico de vectores. Por default se guarda en la ruta activa.
```

Patrones útiles
```python
# Como png
fig.savefig("path/to/file.png")

# Como jpg
fig.savefig("path/to/file.jpg")

# Como svg
fig.savefig("path/to/file.svg")
```

<br/>

### Interactividad

Métodos relacionados con crear gráficas interactivas. 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [Figure.add_axobserver](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_axobserver.html)(func)
  - Se llama a _func_ cada que el estado de la figura se modifica.
* - [Figure.ginput](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.ginput.html)(n=1, timeout=30, show_clicks=True, ...)
  - Llamada de bloqueo para interactuar con la figura.
* - [Figure.pick](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.pick.html)(mouseevent)
  - Procesa un evento de selección.
* - [Figure.waitforbuttonpress](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.waitforbuttonpress.html)(timeout=-1)
  - Llamada de bloqueo para interactuar con la figura.
```

<br/>

### Modificación del estado

Métodos para graficar la figura, limpiarla, manipular los _axes_, entre otros. 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [Figure.clear](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.clear.html)(keep_observers=False)
  - Limpia la figura.
* - [Figure.draw](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.draw.html)(renderer)
  - Grafica al Artista (y sus hijos) usando el renderizador dado.
* - [Figure.draw_artist](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.draw_artist.html)(a)
  - Grafica un solo `Artist`.
* - [Figure.draw_without_rendering](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.draw_without_rendering.html)()
  - Grafica la figura sin _output_.
* - [Figure.gca](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.gca.html)()
  - Retorna el `Axes` actual.
* - [Figure.get_tightbbox](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.get_tightbbox.html)(renderer=None, ...)
  - Retorna un cuadro delimitador (estrecho) de la figura en pulgadas.
* - [Figure.get_window_extent](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.get_window_extent.html)(renderer=None)
  - Retorna el cuadro delimitador del artista en el espacio de visualización.
* - [Figure.sca](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.sca.html)(a)
  - Establece el `Axes` _a_ como el actual y lo retorna.
* - [Figure.set_canvas](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.set_canvas.html)(canvas)
  - Establece el lienzo que contiene la figura.
* - [Figure.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.show.html)(warn=True)
  - Imprime la figura en pantalla.
```

<br/>

### Tamaño y resolución

Métodos relacionados con el tañamo y resolución de la figura. 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [Figure.dpi](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.dpi.html)()
  - La resolución en puntos por pulgada.
* - **Establecer**
  -
* - [Figure.set_dpi](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.set_dpi.html)(val)
  - Establece la resolución de la figura en puntos por pulgada.
* - [Figure.set_dpi](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.set_dpi.html)(val)
  - Establece la resolución de la figura en puntos por pulgada.
* - [Figure.set_figheight](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.set_figheight.html)(val, forward=True)
  - Establece la altura de la figura en pulgadas.
* - [Figure.set_figwidth](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.set_figwidth.html)(val, forward=True)
  - Establece el ancho de la figura en pulgadas.
* - [Figure.set_size_inches](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.set_size_inches.html)(w, h=None, forward=True)
  - Establece el tamaño de la figura en pulgadas.
* - **Recuperar**
  -
* - [Figure.get_figheight](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.get_figheight.html)()
  - Retorna la altura de la figura en pulgadas.
* - [Figure.get_figwidth](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.get_figwidth.html)()
  - Retorna el ancho de la figura en pulgadas.
* - [Figure.get_size_inches](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.get_size_inches.html)()
  - Retorna el tamaño actual de la figura en pulgadas.
```

<br/>

---
## Funciones útiles

A continuación se presentan algunas funciones útiles al trabajar con instancias de la clase `Figure`.

- `plt.clf()`: Limpia la figura que se está manejando actualmente.
- `plt.gcf()`:  Retorna la figura actual, si no hay una figura actual entonces crea una.

