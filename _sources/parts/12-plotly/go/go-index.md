# _Graph Objects_

Proporciona una interfaz de bajo nivel para crear gráficos altamente personalizables y complejos.

```python
# importar librería
import bokeh.graph_objects as go
```
- _go_ es el nombres por convención.

:::{note}
Para más información de esta sección visitar la [documentación](https://plotly.com/python-api-reference/plotly.graph_objects.html) de _plotly_.
:::

<br/>

A continuación se enlistas las secciones de este módulo:
- {doc}`./figure`: Es el objeto que representa la figura completa, que incluye el diseño (_layout_) y los datos (_traces_). Es el contenedor principal para crear gráficos.
- {doc}`./layout`: Define la apariencia y estructura del gráfico, como títulos, ejes, leyendas y márgenes.
- {doc}`./traces`: Contiene los elementos que representan los datos en el gráfico, como líneas, barras, dispersiones y mapas.

## Uso

Uso básico del módulo _graph_objects_

1. Se definie un un diccionario cuyas llaves son:
    - _'data'_ - `list` de `dict`: Define los datos de la gráfica. Las llaves del diccionario son:
        - _type_ - `str`: Tipo de gráfica.
        - _x_ - `list-like`: Datos del eje _x_.
        - _y_ - `list-like`: Datos del eje _y_.
    - _'layout'_ - `dict`: Define el _layout_ general de la gráfica. Algunas llaves del diccionario son:
        - _'title'_ - `dict`: Define las propiedades del título. Algunas llaves son:
            - _'text'_ - `str`: Título de la gráfica.
2. Posteriormente se crea una figura con la función `go.Figure()` cuyo argumento será el diccionario.

<br/>

---
## Tabla de contenido

```{tableofcontents}
````