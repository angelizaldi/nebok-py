# IO

Contiene utilidades para importar y exportar visualizaciones, como guardar gráficos en _HTML_ o mostrar en _notebooks_.

```python
# importar librería
from bokeh.io import Función_name
```
- _func_name_ es el nombre de la función.

:::{warning}
La mayoría de las funciones útiles están en el apartado de funciones, existen además submódulos que extienden las funciones a otras más especializadas.
:::

:::{note}
Para más información de este módulo visitar la [documentación](https://docs.bokeh.org/en/latest/docs/reference/io.html) de `bokeh`.
:::

A continuación se presenta un resumen de los submódulos de _io_, pero recordar que las funciones más importantes están en la sección de funciones.
- **doc**: Proporciona herramientas para trabajar con documentos de _bokeh_, que son contenedores de gráficos y _widgets_.
- **export**: Ofrece funciones para exportar visualizaciones a formatos como PNG o SVG.
- **notebook**: Contiene utilidades para integrar y mostrar visualizaciones de Bokeh en notebooks de Jupyter.
- **output**: Permite configurar dónde y cómo se muestran las visualizaciones, como en navegadores o archivos HTML.
- **saving**: Facilita guardar visualizaciones en archivos HTML o en el servidor de Bokeh.
- **showing**: Proporciona funciones para mostrar visualizaciones en navegadores o en línea.
- **state**: Gestiona el estado de las sesiones de Bokeh, útil para aplicaciones web interactivas.
- **util**: Contiene funciones de utilidad general para el módulo `io`, como manejo de rutas y archivos.

<br/>

## Doc

Proporciona herramientas para trabajar con documentos de _bokeh_, que son contenedores de gráficos y _widgets_.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [curdoc](https://docs.bokeh.org/en/latest/docs/reference/io.html#bokeh.io.doc.curdoc)()
  - Retorna el documento para el estado predeterminado actual.
* - [patch_curdoc](https://docs.bokeh.org/en/latest/docs/reference/io.html#bokeh.io.doc.patch_curdoc)(...)
  - Anula temporalmente el valor de `curdoc()` y luego lo devuelve a su estado original.
* - [set_curdoc](https://docs.bokeh.org/en/latest/docs/reference/io.html#bokeh.io.doc.set_curdoc)(doc: Document)
  - Configura el documento actual (devuelto por `curdoc()`).
```

<br/>

## Export

Ofrece funciones para exportar visualizaciones a formatos como PNG o SVG.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [export_png](https://docs.bokeh.org/en/latest/docs/reference/io.html#bokeh.io.export.export_png)(obj: UIElement | Document, ...)
  - Exporta el objeto o documento `UIElement` como _PNG_.
* - [export_svg](https://docs.bokeh.org/en/latest/docs/reference/io.html#bokeh.io.export.export_svg)(obj: UIElement | Document, ...)
  - Exporta un _layout_ como archivo SVG o un documento como un conjunto de archivos SVG.
* - [export_svgs](https://docs.bokeh.org/en/latest/docs/reference/io.html#bokeh.io.export.export_svgs)(obj: UIElement | Document, ...)
  - Exporta las gráficas habilitadas para SVG dentro de un _layout_. Cada gráfico dará como resultado un archivo SVG distinto.
* - [get_layout_html](https://docs.bokeh.org/en/latest/docs/reference/io.html#bokeh.io.export.get_layout_html)(obj: UIElement | Document, ...)
  - .
* - [get_screenshot_as_png](https://docs.bokeh.org/en/latest/docs/reference/io.html#bokeh.io.export.get_screenshot_as_png)(obj: UIElement | Document, ...)
  - Retorna una captura de pantalla de un objeto `UIElement`.
```

<br/>

## Notebook

Contiene utilidades para integrar y mostrar visualizaciones de Bokeh en notebooks de Jupyter.

### Clases

Clases implementadas en el submódulo _bokeh.io.notebook_.


```{list-table}
:header-rows: 1

* - Constructor
  - Descripción
* - [CommsHandle](https://docs.bokeh.org/en/latest/docs/reference/io.html#bokeh.io.notebook.CommsHandle)(comms: Comm, cell_doc: Document)
  - .
```

### Funciones

Funciones implementadas en el submódulo _bokeh.io.notebook_.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [destroy_server](https://docs.bokeh.org/en/latest/docs/reference/io.html#bokeh.io.notebook.destroy_server)(server_id: ID)
  - Dada un ID de _UUID_ de un _div_ eliminado o reemplazado en el _notebook_ de Jupyter, destruye las sesiones del servidor correspondientes y lo detiene.
* - [get_comms](https://docs.bokeh.org/en/latest/docs/reference/io.html#bokeh.io.notebook.get_comms)(target_name: str)
  - Crea un objeto _comms_ de Jupyter para un objetivo específico, que se puede utilizar para actualizar los documentos bokeh en el _notebook_ de Jupyter.
* - [install_jupyter_hooks](https://docs.bokeh.org/en/latest/docs/reference/io.html#bokeh.io.notebook.install_jupyter_hooks)()
  - .
* - [install_notebook_hook](https://docs.bokeh.org/en/latest/docs/reference/io.html#bokeh.io.notebook.install_notebook_hook)(notebook_type: Literal['jupyter', ...)
  - Instala un nuevo _hook_ de pantalla de _notebook_.
* - [load_notebook](https://docs.bokeh.org/en/latest/docs/reference/io.html#bokeh.io.notebook.load_notebook)(resources: Resources | None = None, ...)
  - Prepare el _notebook_ de IPython para mostrar las graficas de _bokeh_.
* - [publish_display_data](https://docs.bokeh.org/en/latest/docs/reference/io.html#bokeh.io.notebook.publish_display_data)(data: dict[str, Any], ...)
  - .
* - [push_notebook](https://docs.bokeh.org/en/latest/docs/reference/io.html#bokeh.io.notebook.push_notebook)(...)
  - Actualiza los gráficos de bokeh en un _notebook_ de Jupyter con nuevos datos o valores de propiedades.
* - [run_notebook_hook](https://docs.bokeh.org/en/latest/docs/reference/io.html#bokeh.io.notebook.run_notebook_hook)(notebook_type: Literal['jupyter', ...)
  - Ejecuta un _hook_ de _notebook_ instalado con argumentos suministrados.
* - [show_app](https://docs.bokeh.org/en/latest/docs/reference/io.html#bokeh.io.notebook.show_app)(app: Application, state: State, ...)
  - Incrusta una aplicación de servidor _bokeh_ en una celda del _notebook_ de Jupyter.
* - [show_doc](https://docs.bokeh.org/en/latest/docs/reference/io.html#bokeh.io.notebook.show_doc)(obj: Model, state: State)
  - .
```

<br/>

## Output

Permite configurar dónde y cómo se muestran las visualizaciones, como en navegadores o archivos HTML.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [output_file](https://docs.bokeh.org/en/latest/docs/reference/io.html#bokeh.io.output.output_file)(filename: PathLike, ...)
  - Configura el estado de salida predeterminado para generar la salida guardada en un archivo cuando se llama a `show()`.
* - [output_notebook](https://docs.bokeh.org/en/latest/docs/reference/io.html#bokeh.io.output.output_notebook)(resources: Resources | None = None, ...)
  - Configura el estado de salida predeterminado para generar salida en celdas de _notebook_ se llama a `show()`.
* - [reset_output](https://docs.bokeh.org/en/latest/docs/reference/io.html#bokeh.io.output.reset_output)(state: State | None = None)
  - Borra el estado predeterminado de todos los modos de salida.
```

<br/>

## Saving

Facilita guardar visualizaciones en archivos HTML o en el servidor de Bokeh.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [save](https://docs.bokeh.org/en/latest/docs/reference/io.html#bokeh.io.saving.save)(...)
  - Guarda un archivo HTML con los datos para el documento actual.
```

<br/>

## Showing

Proporciona funciones para mostrar visualizaciones en navegadores o en línea.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [show](https://docs.bokeh.org/en/latest/docs/reference/io.html#bokeh.io.showing.show)(...)
  - Muestra inmediatamente un objeto o aplicación _bokeh_.
```

<br/>

## State

Gestiona el estado de las sesiones de Bokeh, útil para aplicaciones web interactivas.

### Clases

Clases implementadas en el submódulo _bokeh.io.state_.


```{list-table}
:header-rows: 1

* - Constructor
  - Descripción
* - [State](https://docs.bokeh.org/en/latest/docs/reference/io.html#bokeh.io.state.State)()
  - Administre el estado relacionado con el control de la salida _bokeh_.
```

<br/>

#### Atributos

Atributos de la clase `State`. 

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - **property document: Document**
  - Un documento predeterminado para usar para todas las operaciones de salida.
* - **property file: FileConfig | None**
  - Una estructura con la configuración predeterminada para la salida del archivo (solo lectura).
* - **property notebook: bool**
  - Indica si se debe generar la salida de _notebook_ en las operaciones de _show_. (solo lectura).
* - **property notebook_type: NotebookType | None**
  - Tipo de _notebook_.
```

<br/>

#### Métodos

Métodos de la clase `State`. 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [output_file](https://docs.bokeh.org/en/latest/docs/reference/io.html#bokeh.io.state.State.output_file)(filename: str | PathLike[str], ...)
  - Configura la salida en un archivo HTML independiente.
* - [output_notebook](https://docs.bokeh.org/en/latest/docs/reference/io.html#bokeh.io.state.State.output_notebook)(...)
  - Genera salida en celdas de _notebooks_.
* - [reset](https://docs.bokeh.org/en/latest/docs/reference/io.html#bokeh.io.state.State.reset)()
  - Desactive todos los modos de salida activos actualmente y establezca `curdoc()` en un documento nuevo vacío.
```

### Funciones

Funciones implementadas en el submódulo _bokeh.io.state_.


```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [curstate](https://docs.bokeh.org/en/latest/docs/reference/io.html#bokeh.io.state.curstate)()
  - Retorna el objeto de estado actual.
```

<br/>

## Util

Contiene funciones de utilidad general para el módulo `io`, como manejo de rutas y archivos.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [default_filename](https://docs.bokeh.org/en/latest/docs/reference/io.html#bokeh.io.util.default_filename)(ext: str)
  - Genera un nombre de archivo predeterminado con una extensión dada, intentando usar el nombre de archivo del proceso de ejecución actualmente, si es posible.
* - [detect_current_filename](https://docs.bokeh.org/en/latest/docs/reference/io.html#bokeh.io.util.detect_current_filename)()
  - Intente devolver el nombre de archivo del proceso de Python que se ejecuta actualmente.
* - [temp_filename](https://docs.bokeh.org/en/latest/docs/reference/io.html#bokeh.io.util.temp_filename)(ext: str)
  - Genera un nombre de archivo temporal y con la extensión dada.
```

<br/>

## Funciones

En esta sección se enlistan las principales funciones para importación y exportación de visualizaciones en _bokeh_. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [curdoc](https://docs.bokeh.org/en/latest/docs/reference/io.html#bokeh.io.curdoc)()
  - Retorna el documento para el estado predeterminado actual.
* - [export_png](https://docs.bokeh.org/en/latest/docs/reference/io.html#bokeh.io.export_png)(obj: UIElement | Document, ...)
  - Exporta el objeto o documento `UIElement` como _PNG_
* - [export_svg](https://docs.bokeh.org/en/latest/docs/reference/io.html#bokeh.io.export_svg)(obj: UIElement | Document, ...)
  - Exporta un _layout_ como archivo SVG o un documento como un conjunto de archivos SVG.
* - [export_svgs](https://docs.bokeh.org/en/latest/docs/reference/io.html#bokeh.io.export_svgs)(obj: UIElement | Document, ...)
  - Exporta las gráficas habilitadas para SVG dentro de un _layout_. Cada gráfico dará como resultado un archivo SVG distinto.
* - [install_notebook_hook](https://docs.bokeh.org/en/latest/docs/reference/io.html#bokeh.io.install_notebook_hook)(notebook_type: Literal['jupyter', ...)
  - Instala un nuevo _hook_ de pantalla de _notebook_.
* - [output_file](https://docs.bokeh.org/en/latest/docs/reference/io.html#bokeh.io.output_file)(filename: PathLike, ...)
  - Configura el estado de salida predeterminado para generar la salida guardada en un archivo cuando se llama a `show()`.
* - [output_notebook](https://docs.bokeh.org/en/latest/docs/reference/io.html#bokeh.io.output_notebook)(resources: Resources | None = None, ...)
  - Configura el estado de salida predeterminado para generar salida en celdas de _notebook_ se llama a `show()`.
* - [push_notebook](https://docs.bokeh.org/en/latest/docs/reference/io.html#bokeh.io.push_notebook)(...)
  - Actualiza los gráficos de bokeh en un _notebook_ de Jupyter con nuevos datos o valores de propiedades.
* - [reset_output](https://docs.bokeh.org/en/latest/docs/reference/io.html#bokeh.io.reset_output)(state: State | None = None)
  - Borra el estado predeterminado de todos los modos de salida.
* - [save](https://docs.bokeh.org/en/latest/docs/reference/io.html#bokeh.io.save)(...)
  - Guarda un archivo HTML con los datos para el documento actual.
* - [show](https://docs.bokeh.org/en/latest/docs/reference/io.html#bokeh.io.show)(...)
  - Muestra inmediatamente un objeto o aplicación _bokeh_.
```