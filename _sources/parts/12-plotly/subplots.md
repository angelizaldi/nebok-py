# Subplots

Facilita la creación de gráficos con múltiples _subplots_ (varios gráficos en una sola figura).

:::{note}
Este módulo tiene una única función
:::

```python
# importar función
from bokeh.subplots import make_subplots
```

<br/>

[plotly.subplots.make_subplots](https://plotly.com/python-api-reference/plotly.subplots.html): Configura una figura para poder agregar _subplots_.
```python
# Sintaxis de llamada
make_subplots(rows=1, cols=1, shared_xaxes=False, shared_yaxes=False, start_cell='top-left', 
              print_grid=False, horizontal_spacing=None, vertical_spacing=None, 
              subplot_titles=None, column_widths=None, row_heights=None, specs=None, insets=None, 
              column_titles=None, row_titles=None, x_title=None, y_title=None, figure=None, **kwargs)
```
**Parámetros:**
- **rows** - `int`: Número de filas de _subplots_ en la figura.
- **cols** - `int`: Número de columnas de _subplots_ en la figura.
- **shared_xaxes**, **shared_yaxes** - `bool` o `str`: Para indicar cómo deben de compartir el eje _x_/_y_ los _subplots_.
    - `True` o 'colums': Los _subplots_ de las columnas compartirán el eje _x_/_y_.
    - _'rows'_: Los _subplots_ de las filas compartirán el eje _x_/_y_.
    - _'all'_: Todos los _subplots_ compatirán el eje _x_/_y_.
    - `False`: Cada _subplot_ tendrá su propio eje _x_/_y_.
- **subplot_titles** - `list de str`: Título de cada _subplot_.
