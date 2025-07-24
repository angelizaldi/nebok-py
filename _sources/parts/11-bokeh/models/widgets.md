# _Widgets_

Incluye controles interactivos, como botones, deslizadores y menús, para crear interfaces de usuario.

:::{note}
Para más información de esta sección visitar la [documentación](https://docs.bokeh.org/en/latest/docs/reference/models/widgets.html) de `bokeh`.
:::

## Clases

Clases implementadas en el módulo _models_ del tipo _widgets_. 

A continuación se enlistan la clasificación de las clases:
- **Botones**: Contiene _widgets_ interactivos como botones, menús desplegables y botones de selección para acciones del usuario.
- **Grupos**: Proporciona _widgets_ para agrupar otros controles, como paneles, pestañas y grupos de botones.
- **Entrada**: Ofrece _widgets_ de entrada de datos, como campos de texto, selectores de fechas y áreas de texto.
- **_Markups_**: Incluye _widgets_ para mostrar contenido estático, como HTML, párrafos y divisores.
- **_Sliders_**: Contiene controles deslizantes para seleccionar valores numéricos dentro de un rango.
- **Tablas**: Proporciona _widgets_ para mostrar y manipular datos en formato tabular.
- **Widget**: Define la clase base para todos los _widgets_, permitiendo la creación de controles personalizados.

### Botones

Contiene _widgets_ interactivos como botones, menús desplegables y botones de selección para acciones del usuario.

```{list-table}
:header-rows: 1

* - Constructor
  - Descripción
* - [AbstractButton](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/buttons.html#bokeh.models.AbstractButton)(*args: Any,  id: ID | None = None, ...)
  - Una clase base que define propiedades comunes para todos los tipos de botones.
* - [Button](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/buttons.html#bokeh.models.Button)(*args: Any,  id: ID | None = None, ...)
  - Un botón de clic.
* - [ButtonLike](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/buttons.html#bokeh.models.widgets.buttons.ButtonLike)(*args,  **kwargs)
  - Propiedades compartidas para _widgets_ tipo botones.
* - [Dropdown](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/buttons.html#bokeh.models.Dropdown)(*args: Any,  id: ID | None = None, ...)
  - Un botón desplegable.
* - [HelpButton](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/buttons.html#bokeh.models.HelpButton)(*args: Any,  id: ID | None = None, ...)
  - Un botón con un símbolo de ayuda que muestra texto adicional cuando se desplaza o hace clic.
* - [Toggle](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/buttons.html#bokeh.models.Toggle)(*args: Any,  id: ID | None = None, ...)
  - Un botón de alternancia de dos estados.
```


### Grupos

Proporciona _widgets_ para agrupar otros controles, como paneles, pestañas y grupos de botones.

```{list-table}
:header-rows: 1

* - Constructor
  - Descripción
* - [AbstractGroup](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/groups.html#bokeh.models.AbstractGroup)(*args: Any,  id: ID | None = None, ...)
  - Clase base abstracta para todo tipo de grupos.
* - [CheckboxButtonGroup](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/groups.html#bokeh.models.CheckboxButtonGroup)(*args: Any,  id: ID | None = None, ...)
  - Un grupo de casillas de verificación renderizadas como botones de alternación.
* - [CheckboxGroup](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/groups.html#bokeh.models.CheckboxGroup)(*args: Any,  id: ID | None = None, ...)
  - Un grupo de casillas de verificación.
* - [RadioButtonGroup](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/groups.html#bokeh.models.RadioButtonGroup)(*args: Any,  id: ID | None = None, ...)
  - Un grupo de cajas de radio representadas como botones de alternar.
* - [RadioGroup](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/groups.html#bokeh.models.RadioGroup)(*args: Any,  id: ID | None = None, ...)
  - Un grupo de cajas de radio.
* - [ToggleButtonGroup](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/groups.html#bokeh.models.ToggleButtonGroup)(*args: Any,  id: ID | None = None, ...)
  - Clase base abstracta para grupos con elementos representados como botones.
* - [ToggleInputGroup](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/groups.html#bokeh.models.ToggleInputGroup)(*args: Any,  id: ID | None = None, ...)
  - Clase base abstracta para grupos con elementos representados como cuadros de verificación/radio.
```

<br/>

### Entrada

Ofrece _widgets_ de entrada de datos, como campos de texto, selectores de fechas y áreas de texto.

```{list-table}
:header-rows: 1

* - Constructor
  - Descripción
* - [AutocompleteInput](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/inputs.html#bokeh.models.AutocompleteInput)(*args: Any,  id: ID | None = None, ...)
  - Widget de entrada de una sola línea con _auto-completion_.
* - [Checkbox](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/inputs.html#bokeh.models.Checkbox)(*args: Any,  id: ID | None = None, ...)
  - Un _widget_ de casilla de verificación.
* - [ColorPicker](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/inputs.html#bokeh.models.ColorPicker)(*args: Any,  id: ID | None = None, ...)
  - Widget de selección de color.
* - [FileInput](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/inputs.html#bokeh.models.FileInput)(*args: Any,  id: ID | None = None, ...)
  - Presenta un cuadro de diálogo de selección de archivos a los usuarios y devuelva el contenido de los archivos seleccionados.
* - [InputWidget](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/inputs.html#bokeh.models.InputWidget)(*args: Any,  id: ID | None = None, ...)
  - Clase base abstracta para _widgets_ de entrada.
* - [MultiChoice](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/inputs.html#bokeh.models.MultiChoice)(*args: Any,  id: ID | None = None, ...)
  - Widget _MultiChoice_.
* - [MultiSelect](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/inputs.html#bokeh.models.MultiSelect)(*args: Any,  id: ID | None = None, ...)
  - Widget _Multi-select_.
* - [NumericInput](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/inputs.html#bokeh.models.NumericInput)(*args: Any,  id: ID | None = None, ...)
  - Widget de entrada numérica.
* - [PaletteSelect](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/inputs.html#bokeh.models.PaletteSelect)(*args: Any,  id: ID | None = None, ...)
  - Widget de selección de paleta de colores.
* - [PasswordInput](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/inputs.html#bokeh.models.PasswordInput)(*args: Any,  id: ID | None = None, ...)
  - Widget de entrada de contraseña de una sola línea.
* - [Select](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/inputs.html#bokeh.models.Select)(*args: Any,  id: ID | None = None, ...)
  - Widget de selección única.
* - [Spinner](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/inputs.html#bokeh.models.Spinner)(*args: Any,  id: ID | None = None, ...)
  - Widget de entrada de spinner numérico.
* - [Switch](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/inputs.html#bokeh.models.Switch)(*args: Any,  id: ID | None = None, ...)
  - Un _widget_ de caja de verificación.
* - [TextAreaInput](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/inputs.html#bokeh.models.TextAreaInput)(*args: Any,  id: ID | None = None, ...)
  - Widget de entrada de múltiples líneas.
* - [TextInput](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/inputs.html#bokeh.models.TextInput)(*args: Any,  id: ID | None = None, ...)
  - Widget de entrada de una sola línea.
```

<br/>


### _Markups_

Incluye _widgets_ para mostrar contenido estático, como HTML, párrafos y divisores.

```{list-table}
:header-rows: 1

* - Constructor
  - Descripción
* - [Div](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/markups.html#bokeh.models.Div)(*args: Any,  id: ID | None = None, ...)
  - Un bloque (_div_) de texto.
* - [Markup](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/markups.html#bokeh.models.Markup)(*args: Any,  id: ID | None = None, ...)
  - Clase base para modelos bokeh que representan elementos de marcado de HTML.
* - [Paragraph](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/markups.html#bokeh.models.Paragraph)(*args: Any,  id: ID | None = None, ...)
  - Un bloque (párrafo) de texto.
* - [PreText](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/markups.html#bokeh.models.PreText)(*args: Any,  id: ID | None = None, ...)
  - Un bloque (párrafo) de texto preformateado.
```

<br/>

### _Sliders_

Contiene controles deslizantes para seleccionar valores numéricos dentro de un rango.

```{list-table}
:header-rows: 1

* - Constructor
  - Descripción
* - [AbstractSlider](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/sliders.html#bokeh.models.AbstractSlider)(*args: Any,  id: ID | None = None, ...)
  - .
* - [CategoricalSlider](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/sliders.html#bokeh.models.CategoricalSlider)(*args: Any,  id: ID | None = None, ...)
  - Control deslizante discreto que permite la selección de una colección de valores.
* - [DateRangeSlider](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/sliders.html#bokeh.models.DateRangeSlider)(*args: Any,  id: ID | None = None, ...)
  - Widget de selección de rango de fechas basado en el control deslizante.
* - [DateSlider](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/sliders.html#bokeh.models.DateSlider)(*args: Any,  id: ID | None = None, ...)
  - Widget de selección de fechas basado en el control deslizante.
* - [DatetimeRangeSlider](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/sliders.html#bokeh.models.DatetimeRangeSlider)(*args: Any,  id: ID | None = None, ...)
  - Widget de selección de rango de fecha y tiempo basado en un control deslizante.
* - [RangeSlider](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/sliders.html#bokeh.models.RangeSlider)(*args: Any,  id: ID | None = None, ...)
  - Widget de selección de rangos numéricos basado en un control deslizante.
* - [Slider](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/sliders.html#bokeh.models.Slider)(*args: Any,  id: ID | None = None, ...)
  - Widget de selección de números basado en un control deslizante.
```

<br/>


### Tablas

Proporciona _widgets_ para mostrar y manipular datos en formato tabular.

```{list-table}
:header-rows: 1

* - Constructor
  - Descripción
* - [AvgAggregator](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/tables.html#bokeh.models.AvgAggregator)(*args: Any,  id: ID | None = None, ...)
  - Promedio simple en múltiples filas.
* - [BooleanFormatter](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/tables.html#bokeh.models.BooleanFormatter)(*args: Any,  id: ID | None = None, ...)
  - Formateador de celda booleana (marca de verificación).
* - [CellEditor](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/tables.html#bokeh.models.CellEditor)(*args: Any,  id: ID | None = None, ...)
  - Clase base abstracta para los editores de celdas de la tabla de datos.
* - [CellFormatter](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/tables.html#bokeh.models.CellFormatter)(*args: Any,  id: ID | None = None, ...)
  - Clase base abstracta para los formateadores de celdas de la tabla de datos.
* - [CheckboxEditor](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/tables.html#bokeh.models.CheckboxEditor)(*args: Any,  id: ID | None = None, ...)
  - Editor de celdas de valor booleano.
* - [DataCube](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/tables.html#bokeh.models.DataCube)(*args: Any,  id: ID | None = None, ...)
  - _DataTable_ especializada con grupos agrupables, totales y subtotales.
* - [DataTable](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/tables.html#bokeh.models.DataTable)(*args: Any,  id: ID | None = None, ...)
  - Cuadrícula bidimensional para visualización y edición de grandes cantidades de datos.
* - [DateEditor](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/tables.html#bokeh.models.DateEditor)(*args: Any,  id: ID | None = None, ...)
  - Editor de celdas de fecha basado en calendario.
* - [DateFormatter](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/tables.html#bokeh.models.DateFormatter)(*args: Any,  id: ID | None = None, ...)
  - Formateador de celdas de fecha.
* - [GroupingInfo](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/tables.html#bokeh.models.GroupingInfo)(*args: Any,  id: ID | None = None, ...)
  - Describe cómo calcular los totales y los subtotales.
* - [HTMLTemplateFormatter](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/tables.html#bokeh.models.HTMLTemplateFormatter)(*args: Any,  id: ID | None = None, ...)
  - Formateador HTML usando una plantilla.
* - [IntEditor](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/tables.html#bokeh.models.IntEditor)(*args: Any,  id: ID | None = None, ...)
  - Editor de celdas de enteros basado en _spinner_.
* - [MaxAggregator](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/tables.html#bokeh.models.MaxAggregator)(*args: Any,  id: ID | None = None, ...)
  - Valor más grande en múltiples filas.
* - [MinAggregator](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/tables.html#bokeh.models.MinAggregator)(*args: Any,  id: ID | None = None, ...)
  - Valor más pequeño en múltiples filas.
* - [NumberEditor](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/tables.html#bokeh.models.NumberEditor)(*args: Any,  id: ID | None = None, ...)
  - Editor de celdas numéricas basada en _spinner_.
* - [NumberFormatter](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/tables.html#bokeh.models.NumberFormatter)(*args: Any,  id: ID | None = None, ...)
  - Formateador de celdas numéricas.
* - [PercentEditor](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/tables.html#bokeh.models.PercentEditor)(*args: Any,  id: ID | None = None, ...)
  - `IntEditor` optimizado para editar porcentajes.
* - [ScientificFormatter](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/tables.html#bokeh.models.ScientificFormatter)(*args: Any,  id: ID | None = None, ...)
  - Muestra valores numéricos de rangos continuos como "números básicos", utilizando notación científica cuando sea apropiado de forma predeterminada.
* - [SelectEditor](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/tables.html#bokeh.models.SelectEditor)(*args: Any,  id: ID | None = None, ...)
  - Selecciona el editor de celdas.
* - [StringEditor](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/tables.html#bokeh.models.StringEditor)(*args: Any,  id: ID | None = None, ...)
  - Editor de celdas de cadena básica con _ auto-completion_.
* - [StringFormatter](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/tables.html#bokeh.models.StringFormatter)(*args: Any,  id: ID | None = None, ...)
  - Formateador de celda de cadena básica.
* - [SumAggregator](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/tables.html#bokeh.models.SumAggregator)(*args: Any,  id: ID | None = None, ...)
  - Suma simple en múltiples filas.
* - [TableColumn](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/tables.html#bokeh.models.TableColumn)(*args: Any,  id: ID | None = None, ...)
  - Widget de columna de tabla.
* - [TableWidget](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/tables.html#bokeh.models.TableWidget)(*args: Any,  id: ID | None = None, ...)
  - Clase base abstracta para _widgets_ de tabla de datos (cuadrícula de datos).
* - [TextEditor](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/tables.html#bokeh.models.TextEditor)(*args: Any,  id: ID | None = None, ...)
  - Editor de celdas de cadena de múltiples líneas.
* - [TimeEditor](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/tables.html#bokeh.models.TimeEditor)(*args: Any,  id: ID | None = None, ...)
  - Editor de tiempos basado en _spinner_.
```

<br/>

### Widget

Define la clase base para todos los _widgets_, permitiendo la creación de controles personalizados.

```{list-table}
:header-rows: 1

* - Constructor
  - Descripción
* - [Widget](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/widget.html#bokeh.models.Widget)(*args: Any,  id: ID | None = None, ...)
  - Una clase base para todos los tipos de _widgets_ interactivos.
```

#### Atributos

Atributos de la clase `Widget`. 

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - [align](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/widget.html#bokeh.models.Widget.align)
  - El punto de alineación dentro del contenedor principal.
* - [aspect_ratio](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/widget.html#bokeh.models.Widget.aspect_ratio)
  - Describe la relación proporcional entre el ancho y la altura del componente.
* - [context_menu](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/widget.html#bokeh.models.Widget.context_menu)
  - Un menú para mostrar cuando el usuario hace clic derecho en el componente.
* - [css_classes](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/widget.html#bokeh.models.Widget.css_classes)
  - Un `list` de clases CSS adicionales para agregar al elemento DOM subyacente.
* - [css_variables](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/widget.html#bokeh.models.Widget.css_variables)
  - Permite definir variables CSS calculadas dinámicamente.
* - [disabled](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/widget.html#bokeh.models.Widget.disabled)
  - Indica si el _widget_ se deshabilitará cuando se renderice.
* - [elements](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/widget.html#bokeh.models.Widget.elements)
  - Una colección de elementos de UI basados ​​en DOM conectados a este panel.
* - [flow_mode](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/widget.html#bokeh.models.Widget.flow_mode)
  - Define si el _layout_ fluirá en el bloque o en la dimensión _inline_.
* - [height](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/widget.html#bokeh.models.Widget.height)
  - La altura del componente (en píxeles).
* - [height_policy](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/widget.html#bokeh.models.Widget.height_policy)
  - Describe cómo el componente debe mantener su altura.
* - [margin](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/widget.html#bokeh.models.Widget.margin)
  - Permite crear espacio adicional alrededor del componente. Los valores en el `tuple` se ordenan de la siguiente manera: _Margin-Top_, _Margin-Right_, _Margin-Bottom_ and _Margin-Left_, similar a los estándares CSS.
* - [max_height](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/widget.html#bokeh.models.Widget.max_height)
  - Altura máxima del componente (en píxeles) si la altura es ajustable.
* - [max_width](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/widget.html#bokeh.models.Widget.max_width)
  - Ancho máximo del componente (en píxeles) si el ancho es ajustable.
* - [min_height](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/widget.html#bokeh.models.Widget.min_height)
  - Altura mínima del componente (en píxeles) si la altura es ajustable.
* - [min_width](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/widget.html#bokeh.models.Widget.min_width)
  - Ancho mínimo del componente (en píxeles) si el ancho es ajustable.
* - [name](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/widget.html#bokeh.models.Widget.name)
  - Un nombre arbitrario y suministrado por el usuario para este modelo.
* - [resizable](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/widget.html#bokeh.models.Widget.resizable)
  - Si el _layout_ es interactivamente redimensionable y, de ser así, en qué dimensiones.
* - [sizing_mode](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/widget.html#bokeh.models.Widget.sizing_mode)
  - Cómo se debe dimensionar el componente.
* - [styles](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/widget.html#bokeh.models.Widget.styles)
  - Estilos CSS _inline_ aplicados al elemento DOM subyacente.
* - [stylesheets](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/widget.html#bokeh.models.Widget.stylesheets)
  - Hojas de estilo adicionales para usar para el elemento DOM subyacente.
* - [syncable](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/widget.html#bokeh.models.Widget.syncable)
  - Indica si este modelo debe sincronizarse de nuevo a un servidor bokeh cuando se actualiza en un navegador web.
* - [tags](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/widget.html#bokeh.models.Widget.tags)
  - Un `list` opcional de valores arbitrarios, proporcionados por el usuario para adjuntar a este modelo.
* - [visible](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/widget.html#bokeh.models.Widget.visible)
  - Indica si el componente debe mostrarse en la pantalla.
* - [width](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/widget.html#bokeh.models.Widget.width)
  - El ancho del componente (en píxeles).
* - [width_policy](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/widget.html#bokeh.models.Widget.width_policy)
  - Describe cómo el componente debe mantener su ancho.
```

<br/>

#### Propiedades

Propiedades de la clase `Widget`. 

```{list-table}
:header-rows: 1

* - Propiedad
  - Descripción
* - **document: Document | None**
  - El documento al que se adjunta este modelo (puede ser `None`).
```

<br/>

#### Métodos

Métodos de la clase `Widget`. 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [apply_theme](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/widget.html#bokeh.models.Widget.apply_theme)(property_values: dict[str,  Any])
  - Aplica un conjunto de valores del tema que se utilizará en lugar de los valores predeterminados, pero no sobreescribirán los valores del conjunto de aplicaciones.
* - [clone](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/widget.html#bokeh.models.Widget.clone)(**overrides: Any)
  - Duplica un objeto _HasProps_.
* - [destroy](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/widget.html#bokeh.models.Widget.destroy)()
  - Limpia las referencias al documento y la propiedad.
* - [equals](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/widget.html#bokeh.models.Widget.equals)(other: HasProps)
  - Igualdad estructural de modelos.
* - [js_link](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/widget.html#bokeh.models.Widget.js_link)(attr: str,  other: Model, ...)
  - Enlaza dos propiedades del modelo bokeh usando JavaScript.
* - [js_on_change](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/widget.html#bokeh.models.Widget.js_on_change)(event: str, ...)
  - Adjunta una devolución de llamada CustomJS a un evento de modelo arbitrario.
* - [on_change](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/widget.html#bokeh.models.Widget.on_change)(attr: str, ...)
  - Agrega una devolución de llamada en este objeto para activar cuando _attr_ cambia.
* - [on_event](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/widget.html#bokeh.models.Widget.on_event)(event: str | type[Event], ...)
  - Ejecuta devoluciones de llamada cuando el evento especificado ocurre en este modelo.
* - [properties_with_values](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/widget.html#bokeh.models.Widget.properties_with_values)(...)
  - Colecta un `dict` de nombres de propiedad a sus valores.
* - [query_properties_with_values](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/widget.html#bokeh.models.Widget.query_properties_with_values)(...)
  - Consulta los valores de propiedades de las instancias de _HasProps_ con un predicado.
* - [references](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/widget.html#bokeh.models.Widget.references)()
  - Retorna todos los modelos a los que este objeto tiene referencias.
* - [remove_on_change](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/widget.html#bokeh.models.Widget.remove_on_change)(attr: str, ...)
  - Elimina una devolución de llamada de este objeto.
* - [select](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/widget.html#bokeh.models.Widget.select)(selector: SelectorType)
  - Consulta este objeto y todas sus referencias para objetos que coincidan con el selector dado.
* - [select_one](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/widget.html#bokeh.models.Widget.select_one)(selector: SelectorType)
  - Consulta este objeto y todas sus referencias para objetos que coincidan con el selector dado. Plantea un error si se encuentra más de un objeto. Retorna un solo objeto coincidente, o `None` si no se encuentra nada.
* - [set_from_json](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/widget.html#bokeh.models.Widget.set_from_json)(name: str,  value: Any, ...)
  - Establece un valor de propiedad en este objeto de JSON.
* - [set_select](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/widget.html#bokeh.models.Widget.set_select)(...)
  - Actualiza objetos que coincidan con un selector dado con las actualizaciones de atributo/valor especificadas.
* - [themed_values](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/widget.html#bokeh.models.Widget.themed_values)()
  - Retorna cualquier sobreescritura proporcionada por el tema.
* - [to_serializable](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/widget.html#bokeh.models.Widget.to_serializable)(serializer: Serializer)
  - Convierte este objeto en una representación serializable.
* - [trigger](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/widget.html#bokeh.models.Widget.trigger)(attr: str,  old: Any,  new: Any, ...)
  - .
* - [unapply_theme](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/widget.html#bokeh.models.Widget.unapply_theme)()
  - Elimina los valores temáticos y restaura los valores predeterminados.
* - [update](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/widget.html#bokeh.models.Widget.update)(**kwargs: Any)
  - Actualiza las propiedades del objeto de los argumentos de palabras clave dados.
```

<br/>

#### Métodos de Clase

Métodos de clase de la clase `Widget`. Estos métodos se utilizan directamente sobre `Axis` y no sobre sus instancias.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [clear_extensions](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/widget.html#bokeh.models.Widget.clear_extensions)()
  - Borra las extensiones personalizadas actualmente definidas.
* - [dataspecs](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/widget.html#bokeh.models.Widget.dataspecs)()
  - Recopila los nombres de todas las propiedades de _DataSpec_ en esta clase.
* - [descriptors](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/widget.html#bokeh.models.Widget.descriptors)()
  - Lista de descriptores de propiedades en el orden de definición.
* - [lookup](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/widget.html#bokeh.models.Widget.lookup)(name: str, ...)
  - Encuentra el `PropertyDescriptor` para una propiedad en una clase, dado el nombre de la propiedad.
* - [parameters](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/widget.html#bokeh.models.Widget.parameters)()
  - Genera valores de parámetros de Python adecuados para funciones que se derivan del _glyph_.
* - [properties](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/widget.html#bokeh.models.Widget.properties)(...)
  - Recopila los nombres de las propiedades en esta clase.
* - [properties_with_refs](https://docs.bokeh.org/en/latest/docs/reference/models/widgets/widget.html#bokeh.models.Widget.properties_with_refs)()
  - Recopila los nombres de todas las propiedades en esta clase que también tienen referencias.
```