# Callbacks

Permite definir comportamientos interactivos mediante callbacks de JavaScript o Python.

:::{note}
Para más información de esta sección visitar la [documentación](https://docs.bokeh.org/en/latest/docs/reference/models/callbacks.html) de `bokeh`.
:::

## Clases

Clases implementadas en el módulo _models_ del tipo _callbacks_. 

```{list-table}
:header-rows: 1

* - Constructor
  - Descripción
* - [Callback](https://docs.bokeh.org/en/latest/docs/reference/models/callbacks.html#bokeh.models.Callback)(*args: Any,  id: ID | None = None, ...)
  - Clase base para _callbacks_ interactivos.
* - [CloseDialog](https://docs.bokeh.org/en/latest/docs/reference/models/callbacks.html#bokeh.models.CloseDialog)(*args: Any,  id: ID | None = None, ...)
  - Cierra un cuadro de diálogo.
* - [CustomJS](https://docs.bokeh.org/en/latest/docs/reference/models/callbacks.html#bokeh.models.CustomJS)(*args: Any,  id: ID | None = None, ...)
  - Ejecuta una función de JavaScript.
* - [OpenDialog](https://docs.bokeh.org/en/latest/docs/reference/models/callbacks.html#bokeh.models.OpenDialog)(*args: Any,  id: ID | None = None, ...)
  - Abre un cuadro de diálogo.
* - [OpenURL](https://docs.bokeh.org/en/latest/docs/reference/models/callbacks.html#bokeh.models.OpenURL)(*args: Any,  id: ID | None = None, ...)
  - Abre una URL en una pestaña o ventana nueva o actual.
* - [SetValue](https://docs.bokeh.org/en/latest/docs/reference/models/callbacks.html#bokeh.models.SetValue)(*args: Any,  id: ID | None = None, ...)
  - Permite actualizar una propiedad de un objeto.
* - [ToggleVisibility](https://docs.bokeh.org/en/latest/docs/reference/models/callbacks.html#bokeh.models.ToggleVisibility)(*args: Any,  id: ID | None = None, ...)
  - Alterna la visibilidad de un elemento UI.
```