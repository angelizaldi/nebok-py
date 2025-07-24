# Bokeh

Es una librería para crear visualizaciones interactivas para navegadores. Permite crear visualizaciones de JavaScript sin tener que escribir JavaScript. Es necesario importarlo.

Para utilizar `bokeh` es necesario instalarlo. Desde la terminal usar:
```
# Con pip
pip install bokeh

# Con conda
conda install bokeh
```

Una vez instalado se debe de importar, es recomendado ir importando las funciones y/o clases de cada módulo:
```python
# importar librería
from bokeh.module_name import function_name

from bokeh.module_name import ClassName
```
- _module_name_ es el nombre del módulo.
- _ClassName_ o _func_name_ es el nombre de la clase o función respectivamente.

:::{note}
Para más información de esta librería visitar la [documentación](https://docs.bokeh.org/en/latest/docs/reference.html) y [guía de usuario](https://docs.bokeh.org/en/latest/docs/user_guide.html) de `bokeh`.
:::

Los principales módulos que se revisarán en este sitio son los siguientes:

| Módulo          | Descripción                                                                                   |
|-----------------|-----------------------------------------------------------------------------------------------|
| {doc}`./io`          | Contiene utilidades para importar y exportar visualizaciones, como guardar gráficos en HTML o mostrar en _notebooks_. |
| {doc}`./layouts`      | Permite organizar y estructurar visualizaciones mediante _layouts_, como filas, columnas y pestañas. |
| {doc}`./models/models-index` | Define los componentes básicos de _Bokeh_, como figuras, herramientas, leyendas y fuentes de datos. |
| {doc}`./plotting`    | Proporciona herramientas para crear gráficos interactivos, como figuras, mapas y gráficos de contorno. |
| {doc}`./transform`   | Ofrece funciones para aplicar transformaciones a datos, como _jitter_, _factor cmap_ y _linear cmap_.  |


## Gráficas de bokeh

A continuación se presenta un ejemplo de una gráfica en bokeh, para describir sus elementos.

De arriba abajo las herramientas (_tools_) son;
- Pan (_pan_):
- BoxZoomTool (_box_zoom_):
- WheelZoomTool (_wheel_zoom_):
- Save (_save_):
- Reset (_reset_):
- Es posible agregar más herramientas con el método _.add_tool()_ de `Figure`.

## Uso

1. Se crea una figura con la función `bokeh.plotting.figure()`, en esta función no se definen los datos aún, solo información como el título, etiquetas de los ejes, rangos de los ejes, _tooltips_, entre otros.
2. Se usan los métodos de `bokeh.plotting.figure` para definir el tipo de gráfica y los datos de la figura. Se pueden añadir muchas gráficas a una misma figura. 

### Subplots y gráficas encimadas

Para crear una gráfica con _subplots_ existen las siguientes opciones.

**1.** Una fila o columnas de gráficas: 
- Crear una figura por cada gráfica.
- Después en la función `show()` agregar la función `row()` o `column()` de `bokeh.layouts` para agregar una fila o columnas de gráficas:

```python
# Fila de gráficas
show(row(fig_1, fig_2, ..., fig_n))

# Columna de gráficas
show(column(fig_1, fig_2, ..., fig_n))
```

**2.** Una malla de gráficas: Se debe de crear una lista de figuras, una figura por gráfica y posteriormente dentro de la función `show()` usar la función `gridplot()` de `bokeh.layouts`. Por ejemplo, donde _plots_ es `list` de `Figure`:

```python
show(gridplot(plots, ncols))
```

**3.** Encimar gráficas.
Para encimas gráficas simplementes crear varios _glyphs_ con una misma figura.

## Servidor

Es posible ejecutar las apps desde un servidor de _bokeh_, algunos cambios que se tienen que hacer son:
- En lugar de usar `io.show()` y `io.outout_file()`, se usa `io.curdoc.add_root()`.
- Desde la consola ejecutar el comando: <br/> `bokeh serve --show myapp.py`
    - donde _myapp\.py_ es un _script_ de _bokeh_.

---
## Tabla de contenido

```{tableofcontents}
````