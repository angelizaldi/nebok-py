# _Figure_

Es el objeto que representa la figura completa, que incluye el _layout_ (_layout_) y los datos (_traces_). Es el contenedor principal para crear gráficos.

```{list-table}
:header-rows: 1

* - Constructor
  - Descripción
* - [plotly.graph_objects.Figure](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure)(data=None, layout=None, ...)
  - Crea una nueva instancia `Figure`.
```

<br/>

```python
# Sintaxis de llamada
go.Figure(data=None, layout=None, frames=None, skip_invalid=False, **kwargs)
```
**Parámetros:** (Importante: En lugar de pasar cada argumento, se puede pasar un diccionario cuyas llaves sean los parámetros y los valores sus valores particulares.)
- **data** - `trace`, `list-like`, `list-like` de `dict`: Establece el tipo de gráfico y los datos (_traces_).
    - `trace`: Una única instancia de _trace_.
    - `list-like`: Instancias de _trace_.
    - `list-like` de `dict`: Indican propiedades de la figura y su valor. Las llaves (`str`) son:
        - _'type'_ - `str`: Indica el tipo de gráfica. Los posibles valores son: _'bar', 'barpolar', 'box', 'candlestick', 'carpet', 'choropleth', 'choroplethmapbox', 'cone', 'contour', 'contourcarpet', 'densitymapbox', 'funnel', 'funnelarea', 'heatmap', 'heatmapgl', 'histogram', 'histogram2d', 'histogram2dcontour', 'icicle', 'image', 'indicator', 'isosurface', 'mesh3d', 'ohlc', 'parcats', 'parcoords', 'pie', 'pointcloud', 'sankey', 'scatter', 'scatter3d', 'scattercarpet', 'scattergeo', 'scattergl', 'scattermapbox', 'scatterpolar', 'scatterpolargl', 'scattersmith', 'scatterternary', 'splom', 'streamtube', 'sunburst', 'surface', 'table', 'treemap', 'violin', 'volume', 'waterfall'_.
        - Argumentos de los constructores de cada _trace_. Ver {doc}`./traces`.
- **layout** - `Layout` o `dict`: Controla el estilo de la figura.
    - `Layout`: Instancia. Ver {doc}`./layout`.
    - `dict`: Parámetros y valores que serán pasados al constructor.
    - `frames`: Para gráficos animados.

<br/>

## Métodos principales

A continuación se presenta una breve lista de los principales métodos.

```{list-table}
:header-rows: 1

* - plotly.graph_objects
  - Descripción
* - [Figure.add_traces](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.add_traces)
  - Agrega _traces_ a la figura.
* - [Figure.show](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.show)
  - Muestra una figura utilizando el renderizador predeterminado o el renderizador especificado por el argumento del renderizador.
* - [Figure.update_layout](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.update_layout)
  - Actualiza las propiedades del _layout_ de la figura con un `dict` y/o con palabras clave de argumentos.
* - [Figure.update_traces](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.update_traces)
  - Realiza una operación de actualización de propiedad en todas los _traces_ que satisfacen los criterios de selección especificados.
```

<br/>

### Métodos

Métodos de la clase `Figure`.

#### Generales

Métodos generales de la clase `Figure`.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [\_\_init__](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.__init__)(data=None, layout=None, ...)
  - Crea una nueva instancia de la clase: `Figure`.
* - [append_trace](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.append_trace)(trace, row, col)
  - Agrega un _trace_ a la figura atada a los ejes en los índices de fila y columna especificados.
* - [batch_animate](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.batch_animate)(duration=500, ...)
  - Administrador de contextos para animar actualizaciones en _traces_/_layout_.
* - [batch_update](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.batch_update)()
  - Un administrador de contextos que combina las operaciones de asignación de _traces_ y _layout_ en un mensaje _plotly_update _ que se ejecuta cuando se sale del contexto.
* - [full_figure_for_development](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.full_figure_for_development)(warn=True, as_dict=False)
  - Calcula los valores predeterminados para todos los atributos no especificados en la figura de entrada y devuelve la salida como una figura _"full"_.
* - [get_subplot](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.get_subplot)(row, col, secondary_y=False)
  - Retorna un objeto que represente el _subplot_ en la fila y columna especificadas. Solo se puede usar en figuras creadas usando `plotly.tools.make_subplots`.
* - [plotly_relayout](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.plotly_relayout)(relayout_data, **kwargs)
  - Realiza una operación de _relayout_ en el _layout_ de la figura.
* - [plotly_restyle](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.plotly_restyle)(restyle_data, ...)
  - Realiza una operación de _restyle_ en los _traces_ de la figura.
* - [plotly_update](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.plotly_update)(restyle_data=None, ...)
  - Realiza una operación de actualización en la figura.
* - [pop](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.pop)(key, *args)
  - Elimina el valor asociado con la llave especificada y la retorna.
* - [print_grid](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.print_grid)()
  - Imprime un _layout_ visual de la disposición de los ejes de la figura. Esto solo es válido para figuras creadas usando `plotly.tools.make_subplots`.
* - [propertydata](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.data)()
  - _Thedataproperty_ es un `tuple` de los objetos _trace_ de la figura.
* - [propertyframes](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.frames)()
  - _Theframesproperty_ es un `tuple` de los objetos de _frame_ de la figura.
* - [propertylayout](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.layout)()
  - _Thelayoutproperty_ es un `tuple` de los objetos de _layout_ de la figura.
* - [set_subplots](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.set_subplots)(rows=None, cols=None, ...)
  - Agrega _subplots_ a esta figura. Si la figura ya contiene _subplots_, esto arroja un error. Acepta cualquier argumento de palabras clave que `plotly.subplots.make_subplots` acepta.
* - [show](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.show)(*args, **kwargs)
  - Muestra una figura utilizando el renderizador predeterminado o el renderizador especificado por el argumento de _renderer_.
```

<br/>

#### Actualizar elementos

Estos métodos permiten actualizar propiedades de la figura o sus componentes.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - **Principales métodos**
  -
* - [update](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.update)(dict1=None, overwrite=False, ...)
  - Actualiza las propiedades de la figura con un `dict` y/o con palabras clave de argumentos.
* - [update_annotations](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.update_annotations)(patch=None, selector=None, ...)
  - Realiza una operación de actualización de propiedad en todas las anotaciones que satisfagan los criterios de selección especificados.
* - [update_layout](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.update_layout)(dict1=None, overwrite=False, ...)
  - Actualiza las propiedades del _layout_ de la figura con un `dict` y/o con palabras clave de argumentos.
* - [update_traces](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.update_traces)(patch=None, selector=None, ...)
  - Realiza una operación de actualización de propiedad en todas los _traces_ que satisfacen los criterios de selección especificados.
* - [update_xaxes](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.update_xaxes)(patch=None, selector=None, ...)
  - Realiza una operación de actualización de propiedad en todos los objetos _xaxis_ que satisfacen los criterios de selección especificados.
* - [update_yaxes](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.update_yaxes)(patch=None, selector=None, ...)
  - Realiza una operación de actualización de propiedad en todos los objetos _yaxis_ que satisfacen los criterios de selección especificados.
* - **Otros métodos**
  -
* - [update_coloraxes](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.update_coloraxes)(patch=None, selector=None, ...)
  - Realiza una operación de actualización de propiedad en todos los objetos _coloraxis_ que satisfagan los criterios de selección especificados.
* - [update_geos](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.update_geos)(patch=None, selector=None, ...)
  - Realiza una operación de actualización de propiedad en todos los objetos _geo_ que satisfagan los criterios de selección especificados.
* - [update_layout_images](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.update_layout_images)(patch=None, selector=None, ...)
  - Realiza una operación de actualización de propiedad en todas las imágenes que satisfagan los criterios de selección especificados.
* - [update_legends](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.update_legends)(patch=None, selector=None, ...)
  - Realiza una operación de actualización de propiedad en todos los objetos _legend_ que satisfagan los criterios de selección especificados.
* - [update_mapboxes](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.update_mapboxes)(patch=None, selector=None, ...)
  - Realiza una operación de actualización de propiedad en todos los objetos _mapbox_ que satisfagan los criterios de selección especificados.
* - [update_maps](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.update_maps)(patch=None, selector=None, ...)
  - Realiza una operación de actualización de propiedad en todos los objetos _map_ que satisfagan los criterios de selección especificados.
* - [update_polars](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.update_polars)(patch=None, selector=None, ...)
  - Realiza una operación de actualización de propiedad en todos los objetos _polar_ que satisfagan los criterios de selección especificados.
* - [update_scenes](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.update_scenes)(patch=None, selector=None, ...)
  - Realiza una operación de actualización de propiedad en todos los objetos _scene_ que satisfagan los criterios de selección especificados.
* - [update_selections](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.update_selections)(patch=None, selector=None, ...)
  - Realiza una operación de actualización de propiedad en todas las selecciones que satisfagan los criterios de selección especificados.
* - [update_shapes](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.update_shapes)(patch=None, selector=None, ...)
  - Realiza una operación de actualización de propiedad en todas las formas (_shapes_) que satisfagan los criterios de selección especificados.
* - [update_smiths](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.update_smiths)(patch=None, selector=None, ...)
  - Realiza una operación de actualización de propiedad en todos los objetos _smith_ que satisfacen los criterios de selección especificados.
* - [update_ternaries](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.update_ternaries)(patch=None, selector=None, ...)
  - Realiza una operación de actualización de propiedad en todos los objetos _ternary_ que satisfagan los criterios de selección especificados.
```

<br/>

#### Añadir elementos

Estos métodos permiten añadir elementos (_traces_) o anotaciones a la figura.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - **Otros elementos**
  - _Anotaciones, rectas y áreas, etc._
* - [add_annotation](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.add_annotation)(arg=None, align=None, ...)
  - Crea y agrega una nueva anotación al _layout_ de la figura.
* - [add_hline](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.add_hline)(y, row='all', col='all', ...)
  - Agrega una línea horizontal a una gráfica o _subplot_ que se extiende infinitamente en la dimensión _x_.
* - [add_hrect](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.add_hrect)(y0, y1, row='all', col='all', ...)
  - Agrega un rectángulo a una gráfica o _subplot_ que se extiende infinitamente en la dimensión _x_.
* - [add_layout_image](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.add_layout_image)(arg=None, layer=None, ...)
  - Crea y agrega una nueva imagen al _layout_ de la figura.
* - [add_selection](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.add_selection)(arg=None, line=None, name=None, ...)
  - Crea y agrega una nueva _selection_ al _layout_ de la figura.
* - [add_shape](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.add_shape)(arg=None, editable=None, ...)
  - Crea y agrega una nueva forma (_shape_) al _layout_ de la figura.
* - [add_trace](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.add_trace)(trace, row=None, col=None, ...)
  - Agrega un _trace_ a la figura.
* - [add_traces](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.add_traces)(data, rows=None, cols=None, ...)
  - Agrega _traces_ a la figura.
* - [add_vline](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.add_vline)(x, row='all', col='all', ...)
  - Agrega una línea vertical a una gráfica o _subplot_ que se extiende infinitamente en la dimensión _y_.
* - [add_vrect](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.add_vrect)(x0, x1, row='all', col='all', ...)
  - Agrega un rectángulo a una gráfica o _subplot_ que se extiende infinitamente en la dimensión _y_.
* - **_Traces_**
  - Ver {doc}`./traces`
* - [add_bar](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.add_bar)(alignmentgroup=None, ...)
  - Agrega un nuevo _trace_ de _Bar_.
* - [add_barpolar](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.add_barpolar)(base=None, basesrc=None, ...)
  - Agrega un nuevo _trace_ de _Barpolar_.
* - [add_box](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.add_box)(alignmentgroup=None, ...)
  - Agrega un nuevo _trace_ de _Box_.
* - [add_candlestick](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.add_candlestick)(close=None, closesrc=None, ...)
  - Agrega un nuevo _trace_ de _Candlestick_.
* - [add_carpet](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.add_carpet)(a=None, a0=None, aaxis=None, ...)
  - Agrega un nuevo _trace_ de _Carpet_.
* - [add_choropleth](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.add_choropleth)(autocolorscale=None, ...)
  - Agrega un nuevo _trace_ de _Choropleth_.
* - [add_choroplethmap](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.add_choroplethmap)(autocolorscale=None, ...)
  - Agrega un nuevo _trace_ de _Choroplethmap_.
* - [add_cone](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.add_cone)(anchor=None, ...)
  - Agrega un nuevo _trace_ de _Cone_.
* - [add_contour](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.add_contour)(autocolorscale=None, ...)
  - Agrega un nuevo _trace_ de _Contour_.
* - [add_contourcarpet](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.add_contourcarpet)(a=None, a0=None, asrc=None, ...)
  - Agrega un nuevo _trace_ de _Contourcarpet_.
* - [add_densitymap](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.add_densitymap)(autocolorscale=None, ...)
  - Agrega un nuevo _trace_ de _Densitymap_.
* - [add_funnel](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.add_funnel)(alignmentgroup=None, ...)
  - Agrega un nuevo _trace_ de _Funnel_.
* - [add_funnelarea](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.add_funnelarea)(aspectratio=None, ...)
  - Agrega un nuevo _trace_ de _Funnelarea_.
* - [add_heatmap](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.add_heatmap)(autocolorscale=None, ...)
  - Agrega un nuevo _trace_ de mapa de calor_Heatmap_.
* - [add_histogram](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.add_histogram)(alignmentgroup=None, ...)
  - Agrega un nuevo _trace_ de _Histogram_.
* - [add_histogram2d](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.add_histogram2d)(autobinx=None, autobiny=None, ...)
  - Agrega un nuevo _trace_ de _Histogram2d_.
* - [add_histogram2dcontour](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.add_histogram2dcontour)(autobinx=None, autobiny=None, ...)
  - Agrega un nuevo _trace_ de _Histogram2dContour_.
* - [add_icicle](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.add_icicle)(branchvalues=None, count=None, ...)
  - Agrega un nuevo _trace_ de _Icicle_.
* - [add_image](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.add_image)(colormodel=None, ...)
  - Agrega un nuevo _trace_ de _Image_.
* - [add_indicator](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.add_indicator)(align=None, customdata=None, ...)
  - Agrega un nuevo _trace_ de _Indicator_.
* - [add_isosurface](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.add_isosurface)(autocolorscale=None, ...)
  - Agrega un nuevo _trace_ de _Isosurface_.
* - [add_mesh3d](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.add_mesh3d)(alphahull=None, ...)
  - Agrega un nuevo _trace_ de _Mesh3d_.
* - [add_ohlc](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.add_ohlc)(close=None, closesrc=None, ...)
  - Agrega un nuevo _trace_ de _Ohlc_.
* - [add_parcats](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.add_parcats)(arrangement=None, ...)
  - Agrega un nuevo _trace_ de _Parcats_.
* - [add_parcoords](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.add_parcoords)(customdata=None, ...)
  - Agrega un nuevo _trace_ de _Parcoords_.
* - [add_pie](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.add_pie)(automargin=None, ...)
  - Agrega un nuevo _trace_ de _Pie_.
* - [add_sankey](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.add_sankey)(arrangement=None, ...)
  - Agrega un nuevo _trace_ de _Sankey_.
* - [add_scatter](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.add_scatter)(alignmentgroup=None, ...)
  - Agrega un nuevo _trace_ de _Scatter_.
* - [add_scatter3d](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.add_scatter3d)(connectgaps=None, ...)
  - Agrega un nuevo _trace_ de _Scatter3d_.
* - [add_scattercarpet](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.add_scattercarpet)(a=None, asrc=None, b=None, ...)
  - Agrega un nuevo _trace_ de _Scattercarpet_.
* - [add_scattergeo](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.add_scattergeo)(connectgaps=None, ...)
  - Agrega un nuevo _trace_ de _Scattergeo_.
* - [add_scattergl](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.add_scattergl)(connectgaps=None, ...)
  - Agrega un nuevo _trace_ de _Scattergl_.
* - [add_scattermap](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.add_scattermap)(below=None, cluster=None, ...)
  - Agrega un nuevo _trace_ de _Scattermap_.
* - [add_scattermapbox](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.add_scattermapbox)(below=None, cluster=None, ...)
  - Agrega un nuevo _trace_ de _Scattermapbox_.
* - [add_scatterpolar](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.add_scatterpolar)(cliponaxis=None, ...)
  - Agrega un nuevo _trace_ de _Scatterpolar_.
* - [add_scatterpolargl](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.add_scatterpolargl)(connectgaps=None, ...)
  - Agrega un nuevo _trace_ de _Scatterpolargl_.
* - [add_scattersmith](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.add_scattersmith)(cliponaxis=None, ...)
  - Agrega un nuevo _trace_ de _Scattersmith_.
* - [add_scatterternary](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.add_scatterternary)(a=None, asrc=None, b=None, ...)
  - Agrega un nuevo _trace_ _Scatterternary_.
* - [add_splom](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.add_splom)(customdata=None, ...)
  - Agrega un nuevo _trace_ de _Splom_.
* - [add_streamtube](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.add_streamtube)(autocolorscale=None, ...)
  - Agrega un nuevo _trace_ de _Streamtube_.
* - [add_sunburst](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.add_sunburst)(branchvalues=None, count=None, ...)
  - Agrega un nuevo _trace_ de _Sunburst_.
* - [add_surface](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.add_surface)(autocolorscale=None, ...)
  - Agrega un nuevo _trace_ de _Surface_.
* - [add_table](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.add_table)(cells=None, columnorder=None, ...)
  - Agrega un nuevo _trace_ de _Table_.
* - [add_treemap](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.add_treemap)(branchvalues=None, count=None, ...)
  - Agrega un nuevo _trace_ de _Treemap_.
* - [add_violin](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.add_violin)(alignmentgroup=None, ...)
  - Agrega un nuevo _trace_ de _Violin_.
* - [add_volume](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.add_volume)(autocolorscale=None, ...)
  - Agrega un nuevo _trace_ de _Volume_.
* - [add_waterfall](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.add_waterfall)(alignmentgroup=None, ...)
  - Agrega un nuevo _trace_ de _Waterfall_.
```

<br/>

#### Conversión

Estos métodos convierten la figura a otros formatos o representaciones.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [to_dict](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.to_dict)()
  - Convierte la figura a un diccionario.
* - [to_html](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.to_html)(*args, **kwargs)
  - Convierte una figura en una representación de cadena HTML.
* - [to_image](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.to_image)(*args, **kwargs)
  - Convierte una figura en una cadena de bytes de imagen estática.
* - [to_json](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.to_json)(*args, **kwargs)
  - Convierte una figura en una representación de cadena JSON.
* - [to_plotly_json](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.to_plotly_json)()
  - Convierte la figura a una representación JSON como `dict`.
```

<br/>

#### Exportar

Estos métodos permiten guardar la figura en diferentes formatos.

```{list-table}
:header-rows: 1

* - Método
  - Descripción{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [write_html](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.write_html)(*args, **kwargs)
  - Escribe una figura en una representación de archivo HTML.
* - [write_image](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.write_image)(*args, **kwargs)
  - Convierte una figura en una imagen estática y lo escribe en un archivo o objeto escritable.
* - [write_json](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.write_json)(*args, **kwargs)
  - Convierte una figura a JSON y lo escribe en un archivo o objeto escritable.
```

<br/>

#### Iterar por elementos

Estos métodos permiten iterar sobre elementos de la figura, como _traces_ o anotaciones

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [for_each_annotation](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.for_each_annotation)(fn, selector=None, row=None, ...)
  - Aplica una función a todas las anotaciones que satisfagan los criterios de selección especificados.
* - [for_each_coloraxis](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.for_each_coloraxis)(fn, selector=None, row=None, ...)
  - Aplica una función a todos los objetos _coloraxis_ que satisfagan los criterios de selección especificados.
* - [for_each_geo](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.for_each_geo)(fn, selector=None, row=None, ...)
  - Aplica una función a todos los objetos _geo_ que satisfagan los criterios de selección especificados.
* - [for_each_layout_image](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.for_each_layout_image)(fn, selector=None, row=None, ...)
  - Aplica una función a todas las imágenes (_images_) que satisfagan los criterios de selección especificados.
* - [for_each_legend](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.for_each_legend)(fn, selector=None, row=None, ...)
  - Aplica una función a todos los objetos de leyenda (_legend_) que satisfagan los criterios de selección especificados.
* - [for_each_map](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.for_each_map)(fn, selector=None, row=None, ...)
  - Aplica una función a todos los objetos de _map_ que satisfagan los criterios de selección especificados.. Apply a function to all map objects that satisfy the specified selection criteria.
* - [for_each_mapbox](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.for_each_mapbox)(fn, selector=None, row=None, ...)
  - Aplica una función a todos los objetos _mapbox_ que satisfagan los criterios de selección especificados.
* - [for_each_polar](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.for_each_polar)(fn, selector=None, row=None, ...)
  - Aplica una función a todos los objetos _polar_ que satisfagan los criterios de selección especificados.. Apply a function to all polar objects that satisfy the specified selection criteria.
* - [for_each_scene](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.for_each_scene)(fn, selector=None, row=None, ...)
  - Aplica una función a todos los objetos de _scene_ que satisfagan los criterios de selección especificados.. Apply a function to all scene objects that satisfy the specified selection criteria.
* - [for_each_selection](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.for_each_selection)(fn, selector=None, row=None, ...)
  - Aplica una función a todas las selecciones (_selections_) que satisfagan los criterios de selección especificados.
* - [for_each_shape](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.for_each_shape)(fn, selector=None, row=None, ...)
  - Aplica una función a todas las formas (_shapes_) que satisfagan los criterios de selección especificados.
* - [for_each_smith](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.for_each_smith)(fn, selector=None, row=None, ...)
  - Aplica una función a todos los objetos _smith_ que satisfagan los criterios de selección especificados.
* - [for_each_ternary](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.for_each_ternary)(fn, selector=None, row=None, ...)
  - Aplica una función a todos los objetos _ternary_ que satisfagan los criterios de selección especificados.
* - [for_each_trace](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.for_each_trace)(fn, selector=None, row=None, ...)
  - Aplica una función a todas los _traces_ que satisfagan los criterios de selección especificados.
* - [for_each_xaxis](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.for_each_xaxis)(fn, selector=None, row=None, ...)
  - Aplica una función a todos los objetos de _xaxis_ que satisfagan los criterios de selección especificados.
* - [for_each_yaxis](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.for_each_yaxis)(fn, selector=None, row=None, ...)
  - Aplica una función a todos los objetos de _yaxis_ que satisfagan los criterios de selección especificados.
```

<br/>

#### Seleccionar elementos

Estos métodos permiten seleccionar elementos específicos de la figura.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [select_annotations](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.select_annotations)(selector=None, row=None, ...)
  - Selecciona anotaciones de un _subplot_ particular y/o anotaciones que satisfagan los criterios de selección personalizados.
* - [select_coloraxes](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.select_coloraxes)(selector=None, row=None, ...)
  - Selecciona objetos _coloraxis_ de una celda de un _subplot_ particular y/o objetos que satisfagan los criterios de selección personalizados.
* - [select_geos](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.select_geos)(selector=None, row=None, ...)
  - Selecciona objetos _geo_ de una celda de un _subplot_ particular y/o objetos que satisfagan los criterios de selección personalizados.
* - [select_layout_images](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.select_layout_images)(selector=None, row=None, ...)
  - Selecciona imágenes de una celda de un _subplot_ particular y/o imágenes que satisfagan los criterios de selección personalizados.
* - [select_legends](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.select_legends)(selector=None, row=None, ...)
  - Selecciona objetos _legend_ de una celda de un _subplot_ particular y/o objetos que satisfagan los criterios de selección personalizados.
* - [select_mapboxes](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.select_mapboxes)(selector=None, row=None, ...)
  - Selecciona objetos _mapbox_ de una celda de un _subplot_ particular y/o objetos que satisfagan los criterios de selección personalizados.
* - [select_maps](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.select_maps)(selector=None, row=None, ...)
  - Selecciona objetos _map_ de una celda de un _subplot_ particular y/o objetos que satisfagan los criterios de selección personalizados.
* - [select_polars](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.select_polars)(selector=None, row=None, ...)
  - Selecciona objetos _polar_ de una celda de un _subplot_ particular y/o objetos que satisfagan los criterios de selección personalizados.
* - [select_scenes](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.select_scenes)(selector=None, row=None, ...)
  - Selecciona objetos _scene_ de una celda de un _subplot_ particular y/o objetos que satisfagan los criterios de selección personalizados.
* - [select_selections](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.select_selections)(selector=None, row=None, ...)
  - Selecciona _selections_ de una celda de un _subplot_ particular y/o _selections_ que satisfagan los criterios de selección personalizados.
* - [select_shapes](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.select_shapes)(selector=None, row=None, ...)
  - Selecciona _shapes_ de una celda de un _subplot_ particular y/o _shapes_ que satisfagan los criterios de selección personalizados.
* - [select_smiths](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.select_smiths)(selector=None, row=None, ...)
  - Selecciona objetos _smith_ de una celda de un _subplot_ particular y/o objetos que satisfagan los criterios de selección personalizados.
* - [select_ternaries](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.select_ternaries)(selector=None, row=None, ...)
  - Selecciona objetos _ternary_ de una celda de un _subplot_ particular y/o objetos que satisfagan los criterios de selección personalizados.
* - [select_traces](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.select_traces)(selector=None, row=None, ...)
  - Selecciona _traces_ de una celda de un _subplot_ particular y/o _traces_ que satisfagan los criterios de selección personalizados.
* - [select_xaxes](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.select_xaxes)(selector=None, row=None, ...)
  - Selecciona objetos _xaxis_ de una celda de un _subplot_ particular y/o objetos que satisfagan los criterios de selección personalizados.
* - [select_yaxes](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.select_yaxes)(selector=None, row=None, ...)
  - Selecciona objetos _yaxis_ de una celda de un _subplot_ particular y/o objetos que satisfagan los criterios de selección personalizados.
```