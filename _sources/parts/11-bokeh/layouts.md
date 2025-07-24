# _Layouts_

Permite organizar y estructurar visualizaciones mediante layouts, como filas, columnas y pestañas.

```python
# importar librería
from bokeh.layouts import function_name
```
- _func_name_ es el nombre de la función.

:::{note}
Para más información de este módulo visitar la [documentación](https://docs.bokeh.org/en/latest/docs/reference/layouts.html) de `bokeh`.
:::


## Clases

Clases implementadas en el módulo _layouts_.

```{list-table}
:header-rows: 1

* - Constructor
  - Descripción
* - [Spacer](https://docs.bokeh.org/en/latest/docs/reference/layouts.html#spacer)(*args: Any,  id: ID | None = None,  **kwargs: Any)
  - Un contenedor para el espacio utilizado para llenar un lugar vacío en una fila o columna.
```

<br/>

## Funciones

Funciones implementadas en el módulo _layouts_. 

```{list-table}
:header-rows: 1

* - function
  - Descripción
* - [column](https://docs.bokeh.org/en/latest/docs/reference/layouts.html#bokeh.layouts.column)(children: list[UIElement], ...)
  - Crea una columna de objetos _Layout_. Obliga a todos los objetos a tener el mismo _sizing_mode_, lo que se requiere para que funcionen diseños complejos.
* - [grid](https://docs.bokeh.org/en/latest/docs/reference/layouts.html#bokeh.layouts.grid)(...)
  - Crea una cuadrícula de objetos _Layout_.
* - [gridplot](https://docs.bokeh.org/en/latest/docs/reference/layouts.html#bokeh.layouts.gridplot)(children: list[UIElement | None], ...)
  - Crea una cuadrícula de gráficos representadas en lienzos separados.
* - [layout](https://docs.bokeh.org/en/latest/docs/reference/layouts.html#bokeh.layouts.layout)(*args: UIElement, ...)
  - Crea una disposición basada en la cuadrícula de objetos _Layout_.
* - [row](https://docs.bokeh.org/en/latest/docs/reference/layouts.html#bokeh.layouts.row)(children: list[UIElement], ...)
  - Crea una fila de objetos _Layout_. Obliga a todos los objetos a tener el mismo _sizing_mode_, lo que se requiere para que funcionen diseños complejos.
```