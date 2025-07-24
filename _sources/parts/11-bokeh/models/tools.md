# _Tools_

Contiene herramientas interactivas para gráficos, como zoom, selección, guardado y _hover_.

:::{note}
Para más información de esta sección visitar la [documentación](https://docs.bokeh.org/en/latest/docs/reference/models/tools.html) de `bokeh`.
:::

## Clases

Clases implementadas en el módulo _models_ del tipo _tools_. 

```{list-table}
:header-rows: 1

* - Constructor
  - Descripción
* - [ActionTool](https://docs.bokeh.org/en/latest/docs/reference/models/tools.html#bokeh.models.ActionTool)(*args: Any,  id: ID | None = None, ...)
  - Una clase base para herramientas que son botones en la barra de herramientas.
* - [BoxEditTool](https://docs.bokeh.org/en/latest/docs/reference/models/tools.html#bokeh.models.BoxEditTool)(*args: Any,  id: ID | None = None, ...)
  - Permite dibujar, desplazar y eliminar _glyphs_ en forma de caja (por ejemplo, `Block`, `Rect`, `HStrip`) en uno o más renderistas editando los datos subyacentes de `ColumnDataSource`.
* - [BoxSelectTool](https://docs.bokeh.org/en/latest/docs/reference/models/tools.html#bokeh.models.BoxSelectTool)(*args: Any,  id: ID | None = None, ...)
  - La herramienta de selección de cuadros permite a los usuarios hacer selecciones en una gráfica mostrando una región rectangular arrastrando el mouse o un dedo sobre el área de la parcela.
* - [BoxZoomTool](https://docs.bokeh.org/en/latest/docs/reference/models/tools.html#bokeh.models.BoxZoomTool)(*args: Any,  id: ID | None = None, ...)
  - La herramienta de zoom de cuadros permite a los usuarios definir una región rectangular de una gráfica para hacer zoom arrastrando el mouse o un dedo sobre la región de la parcela.
* - [ClickPanTool](https://docs.bokeh.org/en/latest/docs/reference/models/tools.html#bokeh.models.ClickPanTool)(*args: Any,  id: ID | None = None, ...)
  - Una herramienta que permite desplazarse dentro de una gráfica por una cantidad fija haciendo clic en un botón.
* - [CopyTool](https://docs.bokeh.org/en/latest/docs/reference/models/tools.html#bokeh.models.CopyTool)(*args: Any,  id: ID | None = None, ...)
  - La herramienta _copy_ es una herramienta de acción, que permite copiar el contenido de renderizador de una gráfica o una colección de gráficas para el portapapeles del sistema. Esta herramienta depende del navegador y puede no funcionar en ciertos navegadores, o requerir permisos adicionales para otorgarse a la página web.
* - [CrosshairTool](https://docs.bokeh.org/en/latest/docs/reference/models/tools.html#bokeh.models.CrosshairTool)(*args: Any,  id: ID | None = None, ...)
  - La herramienta _crosshair_ es una herramienta de inspector pasivo. Generalmente está encendido en todo momento, pero se puede configurar en el menú del inspector asociado con el icono de la barra de herramientas que se muestra arriba.
* - [CustomAction](https://docs.bokeh.org/en/latest/docs/reference/models/tools.html#bokeh.models.CustomAction)(*args: Any,  id: ID | None = None, ...)
  - Ejecuta una acción personalizada, ejm. un _callback_ `CustomJS` cuando se activa un icono de la barra de herramientas.
* - [CustomJSHover](https://docs.bokeh.org/en/latest/docs/reference/models/tools.html#bokeh.models.CustomJSHover)(*args: Any,  id: ID | None = None, ...)
  - Defina un formateador personalizado para aplicar a un campo de herramientas _hover_.
* - [Drag](https://docs.bokeh.org/en/latest/docs/reference/models/tools.html#bokeh.models.Drag)(*args: Any,  id: ID | None = None, ...)
  - Una clase base para herramientas que responden a los eventos de arrastre.
* - [EditTool](https://docs.bokeh.org/en/latest/docs/reference/models/tools.html#bokeh.models.EditTool)(*args: Any,  id: ID | None = None, ...)
  - Una clase base para todos los tipos de herramientas de dibujo interactivo.
* - [ExamineTool](https://docs.bokeh.org/en/latest/docs/reference/models/tools.html#bokeh.models.ExamineTool)(*args: Any,  id: ID | None = None, ...)
  - Una herramienta que permite inspeccionar y configurar un modelo.
* - [FreehandDrawTool](https://docs.bokeh.org/en/latest/docs/reference/models/tools.html#bokeh.models.FreehandDrawTool)(*args: Any,  id: ID | None = None, ...)
  - Permite el dibujo a mano alzada _patches_ y _glyphs_ multilíneas. El _glyph_ para dibujar puede definirse a través de la propiedad _renderers_.
* - [FullscreenTool](https://docs.bokeh.org/en/latest/docs/reference/models/tools.html#bokeh.models.FullscreenTool)(*args: Any,  id: ID | None = None, ...)
  - Una herramienta que permite ampliar un elemento UI a la pantalla completa.
* - [GestureTool](https://docs.bokeh.org/en/latest/docs/reference/models/tools.html#bokeh.models.GestureTool)(*args: Any,  id: ID | None = None, ...)
  - Una clase base para herramientas que responden a los eventos de arrastre.
* - [HelpTool](https://docs.bokeh.org/en/latest/docs/reference/models/tools.html#bokeh.models.HelpTool)(*args: Any,  id: ID | None = None, ...)
  - Una herramienta de botón para proporcionar un enlace de "ayuda" a los usuarios.
* - [HoverTool](https://docs.bokeh.org/en/latest/docs/reference/models/tools.html#bokeh.models.HoverTool)(*args: Any,  id: ID | None = None, ...)
  - La herramienta _hover_ es una herramienta de inspector pasivo.
* - [InspectTool](https://docs.bokeh.org/en/latest/docs/reference/models/tools.html#bokeh.models.InspectTool)(*args: Any,  id: ID | None = None, ...)
  - Una clase base para herramientas que realizan "inspecciones", ejm. `Hovertool`.
* - [LassoSelectTool](https://docs.bokeh.org/en/latest/docs/reference/models/tools.html#bokeh.models.LassoSelectTool)(*args: Any,  id: ID | None = None, ...)
  - La herramienta de selección de lazo permite a los usuarios hacer selecciones en una gráfica al indicar una región de "lazo" dibujada libre arrastrando el mouse o un dedo sobre la región de la gráfica.
* - [LineEditTool](https://docs.bokeh.org/en/latest/docs/reference/models/tools.html#bokeh.models.LineEditTool)(*args: Any,  id: ID | None = None, ...)
  - Permite editar los puntos de intersección de uno o más _glyphs_ de línea. Los _glyphs_ que se editarán se definen a través de la propiedad _renderers_ y un renderizador para las intersecciones se establece a través de la propiedad _intersection_renderer_ (debe representar un _glyph_ puntual (una subclase de `XYGlyph`).
* - [PanTool](https://docs.bokeh.org/en/latest/docs/reference/models/tools.html#bokeh.models.PanTool)(*args: Any,  id: ID | None = None, ...)
  - La herramienta _pan_ permite al usuario arrastar una gráfica con el click izquierdo del _mouse_, o en dispositivos táctiles arrastrando un dedo o lápiz óptico, a través de la región de la gráfica.
* - [PointDrawTool](https://docs.bokeh.org/en/latest/docs/reference/models/tools.html#bokeh.models.PointDrawTool)(*args: Any,  id: ID | None = None, ...)
  - Permite agregar, desplazar y eliminar los _glyphs_ puntuales (es decir, subclases de `XYGlyph`) en uno o más renderizadores editando los datos subyacentes de `ColumnDataSource`. Los renderizadores que se editarán deben suministrarse explícitamente como un ´list´.
* - [PolyDrawTool](https://docs.bokeh.org/en/latest/docs/reference/models/tools.html#bokeh.models.PolyDrawTool)(*args: Any,  id: ID | None = None, ...)
  - Permite dibujar, seleccionar y eliminar _patches_ y _glyphs_ múltiples en uno o más renderizadores editando los datos subyacentes de `ColumnDataSource`. Los renderizadores que se editarán deben suministrarse explícitamente.
* - [PolyEditTool](https://docs.bokeh.org/en/latest/docs/reference/models/tools.html#bokeh.models.PolyEditTool)(*args: Any,  id: ID | None = None, ...)
  - Permite editar los vértices de uno o más _patches_ o _glyphs_ multilíneas. Los _glyphs_ que se editarán se definen a través de la propiedad _renderers_ y un renderizador para los vértices se establece a través de la propiedad _vertex_renderer_ (debe representar un _glyph_ puntual (una subclase de `XYGlyph`).
* - [PolySelectTool](https://docs.bokeh.org/en/latest/docs/reference/models/tools.html#bokeh.models.PolySelectTool)(*args: Any,  id: ID | None = None, ...)
  - La herramienta de selección de polígono permite a los usuarios hacer selecciones en un diagrama indicando una región poligonal con clics del mouse. Los clics únicos (o TAPS) agregan puntos sucesivos a la definición del polígono, y un clic (o toque) de presión indica que la región de selección está lista.
* - [RangeTool](https://docs.bokeh.org/en/latest/docs/reference/models/tools.html#bokeh.models.RangeTool)(*args: Any,  id: ID | None = None, ...)
  - La herramienta de rango permite al usuario actualizar objetos de rango para cualquiera o ambas dimensiones _x_ o _y_ arrastrando una anotación sombreada correspondiente para moverlo o cambiar sus límites.
* - [RedoTool](https://docs.bokeh.org/en/latest/docs/reference/models/tools.html#bokeh.models.RedoTool)(*args: Any,  id: ID | None = None, ...)
  - La herramienta de rehacer invierte la última acción realizada por la herramienta _undo_.
* - [ResetTool](https://docs.bokeh.org/en/latest/docs/reference/models/tools.html#bokeh.models.ResetTool)(*args: Any,  id: ID | None = None, ...)
  - La herramienta de reinicio es una acción. Cuando se activa en la barra de herramientas, la herramienta restablece los límites de datos de la gráfica a sus valores cuando se creó inicialmente el gráfico.
* - [SaveTool](https://docs.bokeh.org/en/latest/docs/reference/models/tools.html#bokeh.models.SaveTool)(*args: Any,  id: ID | None = None, ...)
  - La herramienta _save_ es una acción. Cuando se activa, la herramienta abre un cuadro de diálogo de descarga que permite guardar una reproducción de imagen del gráfico en formato PNG. Si la descarga automática no es compatible con un navegador web, la herramienta recurre a abrir la imagen generada en una nueva pestaña o ventana. El usuario puede guardarlo manualmente haciendo clic derecho en la imagen y eligiendo el elemento de menú "Guardar" (o similar).
* - [Scroll](https://docs.bokeh.org/en/latest/docs/reference/models/tools.html#bokeh.models.Scroll)(*args: Any,  id: ID | None = None, ...)
  - Una clase base para herramientas que responden a los eventos de desplazamiento.
* - [Tap](https://docs.bokeh.org/en/latest/docs/reference/models/tools.html#bokeh.models.Tap)(*args: Any,  id: ID | None = None, ...)
  - Una clase base para herramientas que responden a los eventos de toque/clic.
* - [TapTool](https://docs.bokeh.org/en/latest/docs/reference/models/tools.html#bokeh.models.TapTool)(*args: Any,  id: ID | None = None, ...)
  - La herramienta de selección _tap_ permite al usuario seleccionar en puntos individuales haciendo clic izquierdo en un mouse o golpeando con un dedo.
* - [Tool](https://docs.bokeh.org/en/latest/docs/reference/models/tools.html#bokeh.models.Tool)(*args: Any,  id: ID | None = None, ...)
  - Una clase base para todos los tipos de herramientas interactivas.
* - [ToolProxy](https://docs.bokeh.org/en/latest/docs/reference/models/tools.html#bokeh.models.ToolProxy)(*args: Any,  id: ID | None = None, ...)
  - .
* - [Toolbar](https://docs.bokeh.org/en/latest/docs/reference/models/tools.html#bokeh.models.Toolbar)(*args: Any,  id: ID | None = None, ...)
  - Recopila herramientas para mostrar para una sola gráfica.
* - [UndoTool](https://docs.bokeh.org/en/latest/docs/reference/models/tools.html#bokeh.models.UndoTool)(*args: Any,  id: ID | None = None, ...)
  - La herramienta _undo_ permite restaurar el estado anterior de la gráfica.
* - [WheelPanTool](https://docs.bokeh.org/en/latest/docs/reference/models/tools.html#bokeh.models.WheelPanTool)(*args: Any,  id: ID | None = None, ...)
  - La herramienta de _wheel pan_ permite al usuario desplazarse dentro de la gráfica a lo largo de la dimensión configurada utilizando la rueda de desplazamiento.
* - [WheelZoomTool](https://docs.bokeh.org/en/latest/docs/reference/models/tools.html#bokeh.models.WheelZoomTool)(*args: Any,  id: ID | None = None, ...)
  - La herramienta _wheel zoom_ acercará la gráfica dentro y fuera, centrada en la ubicación actual del mouse.
* - [ZoomInTool](https://docs.bokeh.org/en/latest/docs/reference/models/tools.html#bokeh.models.ZoomInTool)(*args: Any,  id: ID | None = None, ...)
  - La herramienta de _zoom-in_ permite a los usuarios hacer clic en un botón para acercarse en una cantidad fija.
* - [ZoomOutTool](https://docs.bokeh.org/en/latest/docs/reference/models/tools.html#bokeh.models.ZoomOutTool)(*args: Any,  id: ID | None = None, ...)
  - La herramienta _zoom-out_ permite a los usuarios hacer clic en un botón para alejarse en una cantidad fija.
```