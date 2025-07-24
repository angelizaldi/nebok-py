# Plotly

Plotly es una biblioteca de visualización interactiva para Python que permite crear gráficos dinámicos y de alta calidad. Es especialmente útil para:
- **Gráficos interactivos**: Zoom, desplazamiento, hover (información al pasar el cursor).
- **Diversos tipos de gráficos**: Líneas, barras, dispersión (scatter), mapas, heatmaps, gráficos 3D y más.
- **Integración con Jupyter Notebooks y Dash**: Ideal para análisis de datos y dashboards web.
- **Exportación fácil**: A HTML, imágenes (PNG, SVG) o para uso en aplicaciones web.

Para utilizar `plotly` es necesario instalarlo. Desde la terminal usar:
```
# Con pip
pip install plotly

# Con conda
conda install plotly
```

Una vez instalado se debe de importar, es recomendado ir importando las funciones y/o clases de cada módulo:
```python
# importar librería
from plotly.module_name import function_name

from plotly.module_name import ClassName
```
- _module_name_ es el nombre del módulo.
- _ClassName_ o _func_name_ es el nombre de la clase o función respectivamente.

:::{note}
Para más información de esta librería visitar la [documentación](https://plotly.com/python-api-reference/) y [guía de usuario](https://plotly.com/python/) de `bokeh`.
:::

Los principales módulos que se revisarán en este sitio son los siguientes:

| Módulo | Descripción |
| ------ | ----------- |
| {doc}`./express` | Proporciona una interfaz de alto nivel para crear gráficos de manera rápida y sencilla con una sola línea de código. |
| {doc}`./figure-factory` | Ofrece funciones para crear figuras especializadas, como gráficos de dispersión matricial, diagramas de violín y mapas de calor. |
| {doc}`./go/go-index` | Proporciona una interfaz de bajo nivel para crear gráficos altamente personalizables y complejos. |
| {doc}`./io` | Contiene herramientas para importar y exportar gráficos, como guardar en archivos HTML o mostrar en _notebooks_. |
| {doc}`./subplots` | Facilita la creación de gráficos con múltiples _subplots_ (varios gráficos en una sola figura). |

<br/>

## Uso

Existen dos formas principales de crear una gráfica en _plotly_, con el módulo _express_ y con el módulo _graph_objects_.

### _graph_objects_

1. Se definie un un diccionario cuyos keys son:
    - _data_ - `list` de `dict`: Define los datos de la gráfica. Las llaves del diccionario son:
        - _type_ - `str`: Tipo de gráfica.
        - _x_ - `list-like`: Datos del eje _x_.
        - _y_ - `list-like`: Datos del eje _y_.
        - _layout_ - `dict`: Define el _layout_ general de la gráfica. Algunas llaves del diccionario son:
            - _title_ - `dict`: Define las propiedades del título. Algunas llaves son:
                - _text_ - `str`: Título de la gráfica.
2. Posteriormente se crea una figura con la función `go.Figure()` cuyo argumento será el diccionario.

<br/>

---
## Tabla de contenido

```{tableofcontents}
````