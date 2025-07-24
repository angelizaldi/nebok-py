# IO

Contiene herramientas para importar y exportar gráficos, como guardar en archivos HTML o mostrar en _notebooks_.

```python
# importar función
from bokeh.io import function_name
```

:::{note}
Para más información de esta sección visitar la [documentación](https://plotly.com/python-api-reference/plotly.io.html) de _plotly_.
:::

<br/>

## Funciones

Funciones implementadas en el módulo _io_. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [from_json](https://plotly.com/python-api-reference/generated/plotly.io.from_json.html#plotly.io.from_json)(value[,  output_type,  …])
  - Construye una figura a partir de una cadena JSON.
* - [read_json](https://plotly.com/python-api-reference/generated/plotly.io.read_json.html#plotly.io.read_json)(file[,  output_type, ...)
  - Construye una figura a partir del contenido JSON de un archivo local o objeto Python legible.
* - [renderers](https://plotly.com/python-api-reference/generated/plotly.io.renderers.html#plotly.io.renderers)()
  - Objeto _Singleton_ que contiene las configuraciones de renderizador actuales.
* - [show](https://plotly.com/python-api-reference/generated/plotly.io.show.html#plotly.io.show)(fig[,  renderer,  validate])
  - Muestra una figura utilizando el renderista predeterminado o el renderizador especificado por el argumento del renderizador.
* - [templates](https://plotly.com/python-api-reference/generated/plotly.io.templates.html#plotly.io.templates)()
  - Objeto _Singleton_ que contiene las plantillas de figura actuales (también conocido como temas).
* - [to_html](https://plotly.com/python-api-reference/generated/plotly.io.to_html.html#plotly.io.to_html)(fig[,  config,  auto_play,  …])
  - Convierte una figura en una representación de cadena HTML.
* - [to_image](https://plotly.com/python-api-reference/generated/plotly.io.to_image.html#plotly.io.to_image)(fig[,  format,  width,  height, ...)
  - Convierte una figura en una cadena de bytes de imagen estática.
* - [to_json](https://plotly.com/python-api-reference/generated/plotly.io.to_json.html#plotly.io.to_json)(fig[,  validate,  pretty,  …])
  - Convierte una figura en una representación de cadena JSON.
* - [to_templated](https://plotly.com/python-api-reference/generated/plotly.io.to_templated.html#plotly.io.to_templated)(fig[,  skip])
  - Retorna una copia de una figura donde todas las propiedades de estilo se hayan movido a la plantilla de la figura.
* - [write_html](https://plotly.com/python-api-reference/generated/plotly.io.write_html.html#plotly.io.write_html)(fig,  file[,  config, ...)
  - Escribe una figura en una representación de archivo HTML.
* - [write_image](https://plotly.com/python-api-reference/generated/plotly.io.write_image.html#plotly.io.write_image)(fig,  file[,  format,  scale, ...)
  - Convierte una figura en una imagen estática y la escribe en un archivo o objeto escritable.
* - [write_json](https://plotly.com/python-api-reference/generated/plotly.io.write_json.html#plotly.io.write_json)(fig,  file[,  validate,  pretty, ...)
  - Convierte una figura a JSON y la escribe en un archivo o objeto escritable.
```