# _Models_

Define los componentes básicos de _Bokeh_, como figuras, herramientas, leyendas y fuentes de datos.

```python
# importar función
from bokeh.models import function_name

# importar clase
from bokeh.models import ClassName
```
- _ClassName_ o _func_name_ es el nombre de la clase o función respectivamente.

:::{note}
Para más información de esta librería visitar la [documentación](https://docs.bokeh.org/en/latest/docs/reference/models.html) de `bokeh`.
:::

![](https://docs.bokeh.org/en/latest/_images/document.svg)

Todos los modelos conforman un `Document`, tomar como referencia la imagen, que considera un _layout_ de columna con _widgest_ `Slider` y `Select`, y un gráfico con algunas herramientas, un eje y una cuadrícula, y un _glyph_ de glifos para círculos. 

:::{caution}
En este sitio no se documentan todos los tipos de modelos, para una lista completa visitar la documentación oficial.
:::

Los principales tipos de modelos que se revisarán en este sitio son los siguientes:
- {doc}`./annotations`: Proporciona elementos para añadir anotaciones a gráficos, como títulos, leyendas y etiquetas.
- {doc}`./axes`: Contiene herramientas para crear y personalizar ejes en visualizaciones, como ejes lineales, logarítmicos y de fechas.
- {doc}`./callbacks`: Permite definir comportamientos interactivos mediante callbacks de JavaScript o Python.
- {doc}`./formatters`: Proporciona herramientas para dar formato y personalizar la visualización de datos en gráficos, como el formato de números, fechas y categorías en ejes y _tooltips_.
- {doc}`./glyphs`: Ofrece los elementos básicos para representar datos en gráficos, como líneas, círculos, barras y áreas.
- {doc}`./sources`: Proporciona fuentes de datos para alimentar visualizaciones, como `ColumnDataSource` y `GeoJSONDataSource`.
- {doc}`./tools`: Contiene herramientas interactivas para gráficos, como zoom, selección, guardado y _hover_.
- {doc}`./widgets`: Incluye controles interactivos, como botones, deslizadores y menús, para crear interfaces de usuario.

---
## Tabla de contenido

```{tableofcontents}
````