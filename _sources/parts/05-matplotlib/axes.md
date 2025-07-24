---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Axes

```{code-cell} ipython3
:tags: ["remove-input"]

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

azul="#30adb9"
cafe="#ba6a30"
cafe_claro="#cf9975"
```

`matplotlib.axes` es un módulo que contiene la clase `Axes` la cual representa una gráfica en una figura. En esta sección únicamente se enlistan las propiedades y algunos métodos de la clase `Axes`. Para información sobre cómo crear y manipular instancias de la clase `Axes` consultar {doc}`./matplotlib-index`.

:::{warning}
Los usuarios no deben inicializar objetos `Axes` directamente, sino que se deben de utilizar métodos que retornen objetos `Axes` como los del módulo {doc}`./pyplot`.
:::

## Interfaz orienta a objetos

En esta Interfaz se crean dos objetos _fig_ y _ax_. Hay dos formas principales de crear estos objetos que se revisan a continuación.

Para los ejemplos de esta sección se utilizará el _dataset_ "flights" de la librería {doc}`../06-seaborn/seaborn-index`, además se agrupan los datos por año para las visualizaciones de un solo _axes_. Para las figuras con más de un _axes_ se crean dos _datasets_ uno para el años 1950 y otro para 1960.

```{code-cell} ipython3
# Cargar el dataset
flights=sns.load_dataset("flights")

# Agrupar datos por año
yearly_data=flights.groupby('year')['passengers'].sum().reset_index()

# Filtrar datos para 1950 y 1960
flights_1950=flights[flights['year'] == 1950]
flights_1960=flights[flights['year'] == 1960]
```

### 1. Usar las funciones _plt.figure_ y _plt.axes_

Se pueden crear los objetos directamente con las funciones `plt.figure()` y `plt.axes()` y utilizar los métodos de estos objetos para conformar las gráficas:

```python
# Importar módulo
import matplotlib.pyplot as plt

# Crear objetos
fig=plt.figure()
ax=plt.axes()

# Utilizar métodos de ax y/o fig para agregar elementos a la gráfica
ax.method_name()
...
ax.method_name ()
...

# Imprimir la gráfica
plt.show()
```
**Notas**:
- _fig_ será una instancia de la clase {doc}`./figure`.
- _ax_ será una instancia de la clase {doc}`./axes`.
- Las grafícas se crean usando los objetos _fig_ y  _ax_ y sus métodos, ver {ref}`Métodos de Figure <matplotlib-figure-metodos>` y {ref}`Métodos de Axes <matplotlib-axes-metodos>`.
- Se pueden agregar tantos métodos como sean necesarios para personalizar las gráficas.
- Al finalizar para mostrar la gráfica usar `plt.show()`.

<br/>

**Ejemplo**:
En este ejemplo se utiliza las funciones `plt.figure()` y `plt.axes()` para crear una figura con un _axes_.

```{code-cell} ipython3
# Crear objetos
fig=plt.figure()
ax=plt.axes()

# Graficar los datos
ax.plot(yearly_data['year'], 
        yearly_data['passengers'], 
        label='Passengers', 
        marker='o', 
        color=azul)

# Añadir elementos a la gráfica
ax.set_xlabel('Año')
ax.set_ylabel('Total de pasajeros')
ax.set_title('Tendencia de total de pasajeros')
ax.legend()

# Show the plot
plt.show()
```

<br/>

### 2. Usar la función _plt.subplots_ 

Se recomienda utilizar este método porque es más simple y versátil. En este caso la función `plt.subplots()` retorna un objeto _fig_ y un objecto _ax_ y posteriormente se pueden utilizar los métodos de estos objetos para conformar las gráficas:

```python
# Importar módulo
import matplotlib.pyplot as plt

# Crear objetos
fig, ax=plt.subplots(nrows=1, ncols=1, [sharey], [sharex])

# Utilizar métodos de ax y/o fig para agregar elementos a la gráfica
ax.method_name()
...
ax. method_name ()
...

# Imprimir la gráfica
plt.show()
```
**Notas**:
- Se puede indicar cuántas filas y columnas de gráficas tendrá la figura, si no se indican se utilizan los valores por default que es 1 en ambos casos, es decir, una figura con una sola gráfica (un solo _axes_).
- _fig_ será una instancia de la clase {doc}`./figure`
- Dependiendo de los argumentos _n_ y _m_, el objeto _ax_ puede ser:
    - Una instancia de la clase {doc}`./axes` (`n=1` y `m=1`, default)
    - Un `ndarray` de instancias de la clase {doc}`./axes` (`n>1` o `m>1`).
    - **IMPORTANTE**: En lugar de definir _ax_ como _array_, se podrían definir tantos _ax_i_ dentro de un tuple, como sean necesarios (_unpacking_). <br> `fig, (ax0, ax1)=plt.subplots(nrows=1, ncols=2) # ejm. 2 axes`
- Las grafícas se crean usando los objetos _fig_ y  _ax_ y sus métodos, {ref}`Métodos de Figure <matplotlib-figure-metodos>` y {ref}`Métodos de Axes <matplotlib-axes-metodos>`.
- **IMPORTANTE**: En caso de que _ax_ sea _ndarray_, para utilizar los métodos propios de la clase `Axes` se tiene que indicar el índice del elemento usando `ax[i]` o `ax[i, j]`, dependiendo de las dimensiones del _array_, donde _i_ es el índice de las filas y _j_ es el índice de las columnas, ambos empienzan en cero.
- Se pueden agregar tantos métodos como sean necesarios para personalizar las gráficas.
- Al finalizar para mostrar la gráfica usar `plt.show()`.

<br/>

**Ejemplo 1**:
En este ejemplo se utiliza la función `plt.subplots()` con los argumentos _nrows=1_ y _ncols=1_ para crear una figura con un _axes_.

```{code-cell} ipython3
# Crear figura y axes
fig, ax=plt.subplots(1, 1)

# Graficar datos
ax.plot(yearly_data['year'], 
        yearly_data['passengers'], 
        label='Passengers', 
        marker='o', 
        color=azul)

# Añadir elementos a la gráfica
ax.set_xlabel('Año')
ax.set_ylabel('Total de pasajeros')
ax.set_title('Tendencia de total de pasajeros')
ax.legend()

# Imprimir la figura
plt.show()
```

<br/>

**Ejemplo 2**:
En este ejemplo se utiliza la función `plt.subplots()` con los argumentos _nrows=1_ y _ncols=2_ para crear una figura con dos _axes_.

```{code-cell} ipython3
# Crear figura y axes
fig, axes=plt.subplots(1, 2, figsize=(12, 5), sharey=True)

# Graficar datos de 1950
axes[0].bar(flights_1950['month'], flights_1950['passengers'], color=azul)
axes[0].set_title('Pasajeros en 1950')
axes[0].set_xlabel('Mes')
axes[0].set_ylabel('Números de Pasajeros')
axes[0].tick_params(axis='x', rotation=45)

# Graficar datos de 1960
axes[1].bar(flights_1960['month'], flights_1960['passengers'], color=cafe)
axes[1].set_title('Pasajeros en 1960')
axes[1].set_xlabel('Mes')
axes[1].tick_params(axis='x', rotation=45)

# Imprimir la figura
plt.tight_layout()

# Imprimir la figura
plt.show()
```

<br/>

## Atributos

En `matplotlib` no se puede acceder directamente a los atributos por medio de la notación punto. Para modificar o retornar los atributos es necesario usar los métodos `Axes.set_*` y `Axes.get_*`. A continuación se presenta una tabla de los atributos de `Axes`.

```{note}
Los atributos se pueden definir como parámetros dentro de la función `plt.axes()`. Para ver los tipos de datos de los argumentos o las maneras de definirlos consultar [la tabla de parámetros](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib-axes-axes). 
```

```{note}
Muchos atributos son heredados de la clase `Artist`. 
```

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - [adjustable](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_adjustable.html)
  - Indica como se ajusta el tamaño del gráfico cuando cambia el aspecto.
* - [agg_filter](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_agg_filter.html)
  - Filtro del gráfico.
* - [alpha](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_alpha.html)
  - Transparencia del gráfico (0 es transparente, 1 es opaco).
* - [anchor](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_anchor.html)
  - La posición del gráfico dentro del área de dibujo.
* - [animated](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_animated.html)
  - Indica si el gráfico es animado o no.
* - [aspect](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_aspect.html)
  - Relación de aspecto del gráfico (‘auto’, ‘equal’, numérico).
* - [autoscale_on](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_autoscale_on.html)
  - Indica el estatus de la autoescala del gráfico.
* - [autoscalex_on](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_autoscalex_on.html)
  - Indica el estatus de la autoescala del eje _x_.
* - [autoscaley_on](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_autoscaley_on.html)
  - Indica el estatus de la autoescala del eje _y_.
* - [axes_locator](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_axes_locator.html)
  - Posición del gráfico.
* - [axisbelow](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_axisbelow.html)
  - Indica si los ejes se dibujan debajo o encima del gráfico.
* - [box_aspect](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_box_aspect.html)
  - Proporción de aspecto de la caja de los ejes.
* - [clip_box](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_box.html)
  - Indica el área de recorte para los gráficos.
* - [clip_on](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_on.html)
  - Indica si se aplican recortes al gráfico.
* - [clip_path](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_path.html)
  - Indica la ruta de recorte para los gráficos.
* - [facecolor or fc](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_facecolor.html)
  - Color de fondo del gráfico.
* - [figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_figure.html)
  - Referencia a la figura contenedora del gráfico.
* - [forward_navigation_events](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_forward_navigation_events.html)
  - Indica si hay eventos de navegación para avanzar.
* - [frame_on](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_frame_on.html)
  - Indica si el marco de los ejes es visible.
* - [gid](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_gid.html)
  - ID único para el gráfico, útil para identificaciones.
* - [in_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_in_layout.html)
  - Indica si los ejes participan en el diseño de la figura.
* - [label](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_label.html)
  - Etiqueta del gráfico, utilizada en leyendas.
* - [mouseover](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_mouseover.html)
  - Indica si están activos los eventos al pasar el ratón sobre el gráfico.
* - [navigate](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_navigate.html)
  - Indica si está activa la navegación con el gráfico.
* - [navigate_mode](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_navigate_mode.html)
  - Define el modo de navegación (_pan, zoom_).
* - [path_effects](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_path_effects.html)
  - Efectos de estilo aplicados a los gráficos.
* - [picker](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_picker.html)
  - Habilita la selección de elementos en el gráfico.
* - [position](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_position.html)
  - Posición del gráfico en la figura.
* - [prop_cycle](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_prop_cycle.html)
  - ´Ciclo de propiedades (colores, estilos) para gráficos.
* - [rasterization_zorder](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_rasterization_zorder.html)
  - Define cuándo rasterizar según el orden z.
* - [rasterized](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_rasterized.html)
  - Indica si el gráfico se rasteriza.
* - [sharex](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.sharex.html)
  - Indica si se debe de compartir el eje _x_ con otra gráfica.
* - [sharey](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.sharey.html)
  - Indica si se debe de compartir el eje _y_ con otra gráfica.
* - [sketch_params](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_sketch_params.html)
  - Parámetros para dar un efecto de boceto al gráfico.
* - [sketch_params](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_sketch_params.html)
  - Parámetros para dar un efecto de boceto al gráfico.
* - [snap](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_snap.html)
  - Ajuste de las coordenadas a los píxeles más cercanos.
* - [subplotspec](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_subplotspec.html)
  - Especifica la posición del gráfico en una cuadrícula.
* - [title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html)
  - Título del gráfico.
* - [transform](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_transform.html)
  - Transformación aplicada a los datos del gráfico.
* - [url](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_url.html)
  - URL asociada al gráfico, útil para interactividad.
* - [visible](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_visible.html)
  - Indica si el gráfico es visible.
* - [xbound](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xbound.html)
  - Límites del eje _X_ (inferior, superior).
* - [xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html)
  - Etiqueta del eje _X_.
* - [xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html)
  - Límite de valores del eje _X_ (inferior, superior)..
* - [xmargin](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xmargin.html)
  - Margen adicional alrededor del eje _X_.
* - [xscale](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xscale.html)
  - Escala del eje _X_ (lineal, logarítmica, etc.).
* - [xticklabels](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticklabels.html)
  - Etiquetas de los _ticks_ en el eje _X_.
* - [xticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticks.html)
  - Posiciones de los _ticks_ en el eje _X_.
* - [ybound](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ybound.html)
  - Límites del eje _Y_ (inferior, superior).
* - [ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html)
  - Etiqueta del eje _Y_.
* - [ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html)
  - Límite de valores del eje _Y_ (inferior, superior).
* - [ymargin](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ymargin.html)
  - Margen adicional alrededor del eje _Y_.
* - [yscale](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yscale.html)
  - Escala del eje _Y_ (lineal, logarítmica, etc.).
* - [yticklabels](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yticklabels.html)
  - Etiquetas de los _ticks_ en el eje _Y_.
* - [yticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yticks.html)
  - Posiciones de los _ticks_ en el eje _Y_.
* - [zorder](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_zorder.html)
  - Orden de dibujo del gráfico sobre otros elementos.
```

<br/>

---
(matplotlib-axes-metodos)=
## Métodos

A continuación se presentan los métodos del objeto `axes`.

<br/>

### Gráficos Básico

Funciones útiles para crear gráficas básicas. 

#### Líneas y marcadores

Métodos útiles para gráficas que involucran líneas y marcadores, como gráficas de líneas y gríficas de dispersión.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [Axes.errorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.errorbar.html)(x, y, yerr=None, xerr=None, fmt='', ...)
  - Grafica _x_ contra _y_ como línea o _markers_, junto con _errorbars_. Los errores se indican como escalar (el mismo para todas las observaciones), como 1D `ndarray` el error para cada observación o como 2D `ndarray` la parte positiva y negativa del error individualmente para cada observación.
* - [Axes.eventplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.eventplot.html)(positions, orientation='horizontal', ...)
  - Grafica líneas paralelas idénticas en las posiciones dadas.
* - [Axes.loglog](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.loglog.html)(*args, **kwargs)
  - Crea una gráfica con escala logarítmica en los ejes _x_ e _y_.
* - [Axes.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html)(*args, scalex=True, scaley=True, data=None, **kwargs)
  - Grafica _y_ versus _x_ como líneas y/o marcadores.
* - [Axes.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html)(x, y, s=None, c=None, marker=None, cmap=None, norm=None, vmin=None, vmax=None, alpha=None, linewidths=None, ...)
  - Realiza una gráfica de dispersión dando los valores de los ejes _x_ y _y_.
* - [Axes.semilogx](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.semilogx.html)(*args, **kwargs)
  - Crea un gráfico con escala logarítmica en el eje _x_.
* - [Axes.semilogy](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.semilogy.html)(*args, **kwargs)
  - Crea un gráfico con escala logarítmica en el eje _y_.
* - [Axes.stem](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.stem.html)(*args, linefmt=None, markerfmt=None, basefmt=None, bottom=0, label=None, orientation='vertical', data=None)
  - Crea un gráfica con rectas verticales para cada observación desde _base_ hasta _head_, y con un marcador en _head_.
* - [Axes.step](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.step.html)(x, y, *args, where='pre', data=None, **kwargs)
  - Crea una gráfica de _pasos_.
```

##### Notas de _Axes.plot_

[Axes.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html): Realiza una gráfica dando los valores de los ejes _x_ y _x_, ya sean líneas o puntos.
```python
# Sintaxis de llamada
ax.plot([x], y, [fmt], *, data=None, **kwargs)
ax.plot([x], y, [fmt], [x2], y2, [fmt2], ..., **kwargs)
```
- **Parámetros:**
    - **x**, **y** - `array-like` o `scalar`: Coordenadas de los puntos horizontales y verticales, respectivamente. Si no se especifica _x_ será un rango de _0_ a `len(y) - 1`.
    - **data** - `indexable object`: Objeto que se pueda aplicar `obj['label']` y retorne un 1D `array-like`, lo más común que sea un `DataFrame`.
    - **fmt** - `str`: Es una cadena de formato, para indicar cierto formato que debe de tener la gráfica especificamente, el tipo de linea, tipo de marker y el color de los mismos. Ver {ref}`matplotlib-fmt`.
    - **\*\*kwargs**: Propiedades de {ref}`matplotlib-line2d`.
    - Parámetros en la segunda forma de llamar la función:
        - **xi**, **yi** - `array-like` o `scalar`: Cordenadas de los puntos horizontales y verticales, respectivamente.
        - **fmti** - `str`: Es una cadena de formato, para indicar cierto formato que debe de tener la gráfica.
- **Retorna:**
    - `list` de [Line2D](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D).

:::{note}
Notar que también se pueden usar como argumentos propiedades de la clase [PathCollection](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PatchCollection.set).
:::


**Ejemplo**:
En este ejemplo se utiliza directamente la función `plt.plot()` para crear una figura con un _axes_, además se hacen llamadas a las funciones `plt.xlabel()`, `plt.ylabel()`, `plt.title()` y `plt.legend()` para añadir elementos a la gráfica.

```{code-cell} ipython3
fig, ax=plt.subplots(figsize=(8, 6))

# Graficar los datos
ax.plot(yearly_data['year'], 
        yearly_data['passengers'], 
        marker='o', 
        color=azul)

# Agregar etiquetas y título
ax.set_title("Passengers per year", fontsize=14)
ax.set_xlabel("Year", fontsize=11)
ax.set_ylabel("Passengers", fontsize=11)

# Imprimir la figura
plt.show()
```

<br/>

##### Notas de de _Axes.scatter_

[Axes.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html): Realiza una gráfica de dispersión dando los valores de los ejes X y Y.
```python
# Sintaxis de llamada
Axes.scatter(x, y, s=None, c=None, *, marker=None, cmap=None, norm=None, vmin=None, 
             vmax=None, alpha=None, linewidths=None, edgecolors=None, colorizer=None, 
             plotnonfinite=False, data=None, **kwargs)
```
**Parámetros:**
    - **x**, **y** - `array-like` o `float`: Cordenadas de los puntos horizontales y verticales, respectivamente.
    - **s** - `float` o `array-like`: Tamaño de los markers en puntos, al cuadrado.
    - **c** - `array-like`, `list` de `color` o `color`: Color de los markers.
        - `scalar` o `secuencia` de números: Esos números serán mapeados con _cmap_, dependiendo del valor se le asignará un color del mapa de color, los número se emparejarán por posición con los valores de _x_ y _y_, para determinar qué color usar en cada coordenada. Por lo tanto la longitud de la secuencia debe de ser igual que la de _x_ y _y_.
        - `secuencia` de `color`: Colores a usar para cada valor de _x_ y _y_, se empatan por posición y debe de tener la misma longitud que _x_ y _y_. Ver {ref}`matplotlib-color`.
        - `color`: Un solo color para usar en todos lo puntos. Ver {ref}`matplotlib-color`.
        - Se puede usar los valores de una variable categórica para que cada uno tenga un valor diferente. Ver {ref}`matplotlib-colormap`.
    - **marker** - `MarkeyStyle`: Revisar {ref}`matplotlib-markers`.
    - **cmap** - `str` o `ColorMap`: Mapa de color. Solo se usa si c es un `array-like` de `float`. Ver {ref}`matplotlib-colormap`.
    - **alpha** - `float`: Para indicar la opacidad de la gráfica. Es un valor entre 0 y 1, donde 0 es completamente transparente y 1 es completamente opaco.
    - **linewidths** - `float` o `array-like`: Grueso del borde de los markers.
    - **edgecolors** - {'face', 'none', None}, `color` o `secuencia` de `color`: Color del borde de los markers. Si es 'face' será el mismo que el fondo del marker, si es 'none' no tendrá color o se puede especificar el color. Ver Color.
    - **\*\*kwargs**: Propiedades de los objetos [PathCollection](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PatchCollection.set).
**Retorna:**
    - [PathCollection](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PatchCollection).

:::{note}
Notar que también se pueden usar como argumentos propiedades de la clase [PathCollection](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PatchCollection.set).
:::


**Ejemplo**:

```{code-cell} ipython3
# Importar el dataset iris
data=sns.load_dataset("iris")

# Crear figura y axes
fig, ax=plt.subplots(figsize=(5, 4))

# Crear scatterplot: petal length vs petal width
scatter=ax.scatter(
    data["petal_length"], 
    data["petal_width"], 
    c=data["species"].astype('category').cat.codes,  # Color por species
    s=data["sepal_length"] * 10,  # Tamaño proporcional a sepal length
    cmap="Dark2", 
    alpha=0.7
)

# Agregar etiquetas, título y leyenda
ax.set_title("Iris Petal Dimensions", fontsize=14)
ax.set_xlabel("Petal Length (cm)", fontsize=12)
ax.set_ylabel("Petal Width (cm)", fontsize=12)

# Crear leyenda para "species"
species_labels=data["species"].unique()
colors=scatter.cmap(np.linspace(0, 1, len(species_labels)))
handles=[plt.Line2D([0], [0], marker="o", color="w", markersize=10, markerfacecolor=colors[i]) for i in range(len(species_labels))]
ax.legend(handles, species_labels, title="Species", loc="upper left")

# Imprimir la figura
plt.tight_layout()
plt.show()
```


<br/>

#### Barras

Métodos útiles para gráficas de barras, como barras verticales u horizontales.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [Axes.bar](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bar.html)(x, height, width=0.8, bottom=None, ...)
  - Crea una gráfica de barras.
* - [Axes.bar_label](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bar_label.html)(container, labels=None, ...)
  - Genera etiquetas para una gráfica de barras.
* - [Axes.barh](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.barh.html)(y, width, height=0.8, left=None, ...)
  - Crea una gráfica de barras horizontales.
* - [Axes.broken_barh](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.broken_barh.html)(xranges, yrange, ...)
  - Grafica una secuencia horizontal de rectángulos.
```

##### Notas de _ax.bar_

[Axes.bar](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bar.html): Crea una gráfica de barras.
```python
ax.bar(x, height, width=0.8, bottom=None, *, align='center', data=None, **kwargs)
```
**Parámetros:**
- **x** - `float` o `array-like`: Coordenadas del eje _x_, pueden ser las categorías a grafícar o solo una etiqueta.
- **height** - `float` o `array-like`: Valores que tienen la altura de las barras. Tiene que ser de la misma longitud que _x_.
- **width** - `float` o `array-like`: Ancho de las barras.
- **bottom** - `float` o `array-like`: Coordenas de _y_, de las bases de las barras. Útil en caso de que quieres apilar varios valores.
- **align** - {'center', 'edge'}: Alineación de las etiquetas de las barras en la coordenada _x_.
- **kwargs**: Propiedades de {ref}`matplotlib-rectangle`.
    - `tick_label` - `str` o `list` de `str`: Para modificar las etiquetas de las barras. Debe ser igual a la longitude de _x_.
    - `xerr`, `yerr` - `float` o `array-like` de shape _(N)_ o _(2, N)_.
        - Si es un escalar: Agrega +/- el valor a todas las barras.
        - shape(N): Agrega +/- los valores a cada barra.
        - shape(2, N): Valores separados para la parte negativa y la parte positiva para cada barra. La primer fila son los negativos y la segunda los positivos.
    - **ecolor** - `color`: Color de las _errorbars_.

**Retorna:**
- [BarContainer](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.BarContainer).

Patrones útles
```python
# Barras apiladas
ax.bar(df.index, df['col1'])
ax.bar(df.index, df['col2'], bottom=df['col1'])

# Barras de dos cantidades independientes
ax.bar("Cat 1", df["col"].agg_func()) # Usar str con nombre de la categoría
ax.bar("Cat 2", df2["col"].agg_func())
```

**Ejemplo:**

En este ejemplo se grafican barras apiladas, para el número de pasajeros en 1950 y 1960.

```{code-cell} ipython3
# Crear figura y axes
fig, ax=plt.subplots(figsize=(8, 6))

# Crear gráfica
ax.bar(flights_1950['month'], 
        flights_1950['passengers'], 
        color=azul, 
        label='1950')

# Crear gráfica apilada
ax.bar(flights_1950['month'], 
        flights_1960['passengers'], 
        bottom=flights_1950['passengers'], 
        color=cafe, 
        label='1960')

# Añadir leyenda
ax.legend()

# Imprimir gráfica
plt.show()
```

<br/>

(axes-rectas-areas)=
#### Rectas y áreas

Métodos útiles para crear rectas en intervalos y áreas.

:::{warning}
Considerar lo siguiente:
- Las rectas aquí presentadas son múltiples rectas en un intervalo. Para graficar una única recta revisar funciones en {ref}`pyplot-funciones-spans`.
- Las áreas aquí presentadas son para rellenar áreas entre curvas o gráficas de áreas. Para generar _spans_ (rectángulos para resaltar zonas en gráficas) ver funciones en {ref}`axes-metodos-spans`.
:::

:::{note}
Los valores usados en estos métodos deben de coincidir con los valores del índice o de la columna que se use en el eje correspondiente. Por ejemplo, si uno de los ejes es de tipo fecha se debe de usar un valor que represente una fecha, por ejemplo `'2020-06-21'`.
:::

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [Axes.fill](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.fill.html)(*args, data=None, **kwargs)
  - Grafica polígonos rellenos.
* - [Axes.fill_between](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.fill_between.html)(x, y1, y2=0, where=None, interpolate=False, step=None, ...)
  - Rellena el área entre dos curvas horizontales ($y=f(x)$).
* - [Axes.fill_betweenx](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.fill_betweenx.html)(y, x1, x2=0, where=None, step=None, interpolate=False, ...)
  - Rellena el área entre dos curvas verticales ($x=g(y)$).
* - [Axes.hlines](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hlines.html)(y, xmin, xmax, colors=None, linestyles='solid', label='', ...)
  - Grafica líneas horizontales en cada _y_ desde _xmin_ hasta _xmax_.
* - [Axes.stackplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.stackplot.html)(x, *args, labels=(), colors=None, baseline='zero', data=None, **kwargs)
  - Crea una gráfica de áreas apiladas.
* - [Axes.vlines](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.vlines.html)(x, ymin, ymax, colors=None, linestyles='solid', label='', ...)
  - Grafica líneas verticales en cada _x_ desde _ymin_ hasta _ymax_.
```

<br/>

#### Circulares

Gráficas circulares.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [Axes.pie](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pie.html)(x, ...)
  - Grafica un gráfico circular.
```

<br/>

### Gráficos de Bins

Métodos útiles para visualizar datos en _bins_ como histogramas. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [Axes.hexbin](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hexbin.html)(x, y, ...)
  - Crea un gráfico de agrupación hexagonal 2D de los puntos _x_, _y_.
* - [Axes.hist](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hist.html)(x, bins=None, range=None, density=False, weights=None, cumulative=False, ...)
  - Calcula y grafica un histograma.
* - [Axes.hist2d](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hist2d.html)(x, y, bins=10, range=None, density=False, ...)
  - Crea un gráfico de histograma 2D.
* - [Axes.stairs](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.stairs.html)(values, edges=None, ...)
  - Grafica de escalera como una línea con bordes delimitadores o un gráfico relleno.
```

<br/>

#### Notas de _Axes.hist_

[Axes.hist](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hist.html): Realiza un histograma.
```python
# Sintaxis de llamada
ax.hist(x, bins=None, *, range=None, density=False, weights=None, cumulative=False, 
        bottom=None, histtype='bar', align='mid', orientation='vertical', rwidth=None, 
        log=False, color=None, label=None, stacked=False, data=None, **kwargs)
```
**Parámetros:**
- **x** - `array-like` o `secuencia` de `array-like`: Datos de entrada. Si es una secuencia, los _arrays_ pueden ser de diferentes tamaños.
- **bins** - `int`, `secuencia` o `str`: .
    - `int`: Número de _bins_ en el rango.
    - `secuencia`: Define los limites de cada _bin_. Es inclusivo.
    - `str`: El nombre de una estrategia para hacer los bins, las posibles opciones son 'auto', 'fd', 'doane', 'scott', 'stone', 'rice', 'sturges', o 'sqrt'.
- **range** - `tuple` o `None`: Rango de los bins. Ignorado si _bins_ es `secuencia`. Por default es `(x.min(), x.max())`.
- **density** - `bool`: Para indicar que retorne la densidad de probabilidad (eje _y_ entre 0 y 1).
- **cumulative** - `bool`: Para indicar si realizar el histograma cumulativo. Si es -1 entonces la acumulación es al revés (empieza acumulado y se van restando los nuevos valores).
- **histtype** - {'bar', 'barstacked', 'step', 'stepfilled'}: Tipo de histograma.
- **align** - {'left', 'mid', 'right'}: Alineación de las barras.
- **orientation** - {'vertical', 'horizontal'}: Orientación de las barras.
- **stacked** - `bool`: Para indicar, en caso de múltiples datos, que las barras se apilen.
- **kwargs**: Propiedades de {ref}`matplotlib-patch`.

**Retorna:**
- **n** -`array` o `list` de `array`: VAlores de los _bins_ (alturas de las barras).
- **bins** -`array`: Extremos de los bins.
- **patches** - `BarContainer`, `list` de `Polygon` o `list` de esos objetos: Contenedor de los artistas individuales usados para crear el histograma.

**Ejemplo:**

```{code-cell} ipython3
# Importar el dataset
tips=sns.load_dataset("tips")

# Crear figura y axez
fig, ax=plt.subplots(1, 1, figsize=(8, 6))

# Graficar el histograma
ax.hist(tips['total_bill'], bins=20, color=azul, edgecolor='black', alpha=0.7)
ax.set_title('Histograma de Total Bill', fontsize=14)
ax.set_xlabel('Total Bill ($)', fontsize=12)
ax.set_ylabel('Frecuencia', fontsize=12)

# Imprimir la figura
plt.show()
```

<br/>

### Gráficos de Campos Vectoriales

Métodos para graficar campos vectoriales.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [Axes.barbs](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.barbs.html)(*args, data=None, **kwargs)
  - Grafica un campo 2D de púas.
* - [Axes.quiver](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.quiver.html)(*args, data=None, **kwargs)
  - Grafica un campo 2D de flechas.
* - [Axes.quiverkey](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.quiverkey.html)(Q, X, Y, U, label, **kwargs)
  - Agrega una clave a una gráfica _quiver_.
* - [Axes.streamplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.streamplot.html)(x, y, u, v, density=1, linewidth=None, color=None, cmap=None, ...)
  - rafica líneas de corriente de un flujo vectorial.
```

<br/>

### Gráficos de Contornos

Métodos para gráficar de contornos. Útiles para representaciones 2D de gráficas 3D.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [Axes.clabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.clabel.html)(CS, levels=None, **kwargs)
  - Etiqueta un una gráfica de contorno.
* - [Axes.contour](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.contour.html)(*args, data=None, **kwargs)
  - Grafica líneas de contorno.
* - [Axes.contourf](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.contourf.html)(*args, data=None, **kwargs)
  - Grafica contornos rellenos.
```

<br/>

### Gráficos Espectrales

Métodos útiles para diagramas espectrales, utilizados para analizar frecuencias y estructuras cíclicas.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [Axes.acorr](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.acorr.html)(x, ...)
  - Grafica la autocorrelación de _x_.
* - [Axes.angle_spectrum](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.angle_spectrum.html)(x, ...)
  - Grafica el espectro de ángulos.
* - [Axes.cohere](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.cohere.html)(x, y, ...)
  - Grafica la coherencia entre _x_ y _y_.
* - [Axes.csd](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.csd.html)(x, y, ...)
  - Grafica la densidad espectral cruzada.
* - [Axes.magnitude_spectrum](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.magnitude_spectrum.html)(x, ...)
  - Grafica el espectro de magnitudes.
* - [Axes.phase_spectrum](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.phase_spectrum.html)(x, ...)
  - TGrafica el espectro de fases.
* - [Axes.psd](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.psd.html)(x, ...)
  - Grafica la densidad espectral de potencia.
* - [Axes.specgram](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.specgram.html)(x, ...)
  - Grafica un espectrograma.
* - [Axes.xcorr](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.xcorr.html)(x, y, ...)
  - Grafica la correlación cruzada entre _x_ y _y_.
```

<br/>

### Gráficos Estadísticos

Métodos útiles para graficar información estadística como _boxplots_ y distribuciones acumuladas.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [Axes.boxplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.boxplot.html)(x, ...)
  - Genera una gráfica de caja y bigotes. Retorna un diccionario que contiene las siguientes _keys_: _boxes_, _medians_, _whiskers_, _caps_, _fliers_, _means_.
* - [Axes.bxp](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bxp.html)(bxpstats, positions=None, widths=None
  - Función de grafica para diagramas de caja y bigotes.
* - [Axes.ecdf](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.ecdf.html)(x, weights=None, ...)
  - Calcula y grafica la función de distribución acumulada de _x_.
* - [Axes.violin](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.violin.html)(vpstats, ...)
  - Función de grafica para graficas de violín.
* - [Axes.violinplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.violinplot.html)(dataset, ...)
  - Genera una gráfica de violín.
```

#### Notas de _plt.boxplot_

[Axes.boxplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.boxplot.html): Crea un boxplot por cada columna que se le pase.
```python
Axes.boxplot(x, *, notch=None, sym=None, vert=None, orientation='vertical', whis=None, positions=None, 
             widths=None, patch_artist=None, bootstrap=None, usermedians=None, conf_intervals=None, 
             meanline=None, showmeans=None, showcaps=None, showbox=None, showfliers=None, boxprops=None, 
             tick_labels=None, flierprops=None, medianprops=None, meanprops=None, capprops=None, 
             whiskerprops=None, manage_ticks=True, autorange=False, zorder=None, capwidths=None, 
             label=None, data=None)
```
**Parámetros:**
- **x** - `array` o `secuencia` de `2D array`: Los datos.
- **notch** - `bool`: `False` para que se la figura sean rectángulos. `True` para que tengan hendiduras en la media.
- **vert** - `bool`: Para indicar si los boxes deben ser verticales (True) u horizontales (False).

**Retorna:**
- `dict`: Diccionario que contiene las siguientes keys: _boxes_ (`list` de `PathPatch`), _medians_ (`list` de `Line2D`), _whiskers_ (`2-list` de `Line2D`), _caps_ (`2-list` de `Line2D`), _fliers_ (`list` de `Line2D`), _means_ (opcional, `list` de `Line2D`).

Patrones útles
```python
# Cambiar colores
_ = ax.boxplot(df['col'], patch_artist=True)
for box in _['boxes']:
    box.set(facecolor, edgecolor)
for median in _['medians']:
    median.set(color)
```
- Colores:
    - Asegurarse de usar `patch_artist=True` en `plt.boxplot()`.
    - También se puede cambiar el color de cualquier otro elemento, simplemente usar los parámetros correctos para el tipo de dato del elemento.

**Ejemplo:**
En este ejemplo se gráfica el histograma de la columna _total_bill_ del dataset _tips_.

```{code-cell} ipython3
# Crear la figura
fig, ax=plt.subplots(1, 1, figsize=(8, 6))

# Graficar el histograma
_ = ax.boxplot(tips['total_bill'], patch_artist=True)

# Cambiar colores
for box in _['boxes']:
    box.set(facecolor=azul, edgecolor='black', linewidth=1)
for median in _['medians']:
    median.set(color=cafe, linewidth=2)

# Añadir título
ax.set_title('Boxplot of Total Bill', fontsize=14)

# Imprimir la figura
plt.show()
```

<br/>

### Gráficos de Arreglos

Métodos para generar visualizaciones a partir de datos contenidos en arreglos. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [Axes.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html)(X, cmap=None, norm=None, ...)
  - Muestra un array como una imagen.
* - [Axes.matshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.matshow.html)(Z, **kwargs)
  - Grafica los valores de un arreglo o matriz 2D como imagen codificada por colores.
* - [Axes.pcolor](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pcolor.html)(*args, ...)
  - Crea un diagrama de pseudocolor con una cuadrícula rectangular no regular.. Create a pseudocolor plot with a non-regular rectangular grid.
* - [Axes.pcolorfast](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pcolorfast.html)(*args, ..)
  - Crea una gráfica de pseudocolor con una cuadrícula rectangular no regular.
* - [Axes.pcolormesh](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pcolormesh.html)(*args, ...)
  - Crea una gráfica de pseudocolor con una cuadrícula rectangular no regular.
* - [Axes.spy](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.spy.html)(Z, ...)
  - Traza el patrón de un arreglo 2D _sparse_.
```

<br/>

(axes-metodos-spans)=
### Rectas y Áreas

Métodos para añadir rectas y áreas rectángulares a gráficas.

:::{caution}
Para añadir _n_ rectas en un intervalo o agregar áreas entre curvas o áreas con formas más complejas (polígonos) revisar métodos de {ref}`axes-rectas-areas`.
:::

:::{note}
Los valores usados en estos métodos deben de coincidir con los valores del índice o de la columna que se use en el eje correspondiente. Por ejemplo, si uno de los ejes es de tipo fecha se debe de usar un valor que represente una fecha, por ejemplo `'2020-06-21'`.
:::

:::{note}
Los métodos de abajo también pueden recibir como argumentos propiedades de los objetos retornados, ya sean `Line2D`, `Rectangle` (ver {doc}`./otros`) o [AxLine](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.AxLine.html#matplotlib.lines.AxLine.set).
:::

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [Axes.axhline](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axhline.html)(y=0, xmin=0, xmax=1, **kwargs)
  - Añade una línea horizontal a la gráfica.
* - [Axes.axhspan](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axhspan.html)(ymin, ymax, xmin=0, xmax=1, **kwargs)
  - Agrega un área (rectángulo horizontal) a la gráfica.
* - [Axes.axline](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axline.html)(xy1, xy2=None, ...)
  - Agrega una línea recta infinitamente larga.
* - [Axes.axvline](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axvline.html)(x=0, ymin=0, ymax=1, **kwargs)
  - Añade una línea vertical a la gráfica.
* - [Axes.axvspan](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axvspan.html)(xmin, xmax, ymin=0, ymax=1, **kwargs)
  -  Agrega un tramo vertical (rectángulo) a la gráfica.
```

:::{tip}
Es posible añadir una recta con pendiente, sin embargo para ello se usa una función de otro módulo: <br/> `from matplotlib.lines import Line2D`

Para añadir la recta a una gráfica, se tiene que asignar el objeto a una variable `l`, posteriormente se debe de utilizar el método `.add_line()` de `Axes`, cuyo argumento será el objeto de tipo `Line2D`. <br/>
<code> l=matplotlib.lines.Line2D(xdata, ydata, **kwargs) <br/> ax.add_line(l) </code>

Para más información revisar la [documentación](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html).
:::

**Ejemplo**
En el siguiente ejemplo se añade una recta horizontal en y un área entre 1953 y 1954:

```{code-cell} ipython3
fig=plt.figure()
ax=plt.axes()

# Graficar los datos
ax.plot(yearly_data['year'], 
        yearly_data['passengers'], 
        marker='o', 
        color=azul)

# Añadir recta horizontal
ax.axhline(4500, color=cafe)

# Añadir área vertical
ax.axvspan(1953, 1954, color=cafe_claro, alpha=.3)

# Imprimir la figura
plt.show()
```

<br/>

### Texto y Anotaciones

Funciones útiles para añadir texto y otras anotaciones a las gráficas. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [Axes.annotate](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html)(text, xy, ...)
  - Agrega un texto a una gráfica para resaltar algún punto. Es posible agregar una flecha que apunte hacia un punto en particular y se agrege un texto.
* - [Axes.arrow](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.arrow.html)(x, y, dx, dy, **kwargs)
  - Añade una flecha al `Axes`.
* - [Axes.indicate_inset](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.indicate_inset.html)(bounds, inset_ax=None, ...)
  - Agrega un indicador _insert_ al `Axes`.
* - [Axes.indicate_inset_zoom](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.indicate_inset_zoom.html)(inset_ax, **kwargs)
  - Agrega indicador rectangular _insert_ al `Axes` basado en los límites del eje para un _inset_ax_ y grafica conectores entre _inset_ax_ y el rectángulo.
* - [Axes.inset_axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.inset_axes.html)(bounds, ...)
  - Agrega un _inset_ hijo `Axes` al `Axes`.
* - [Axes.secondary_xaxis](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.secondary_xaxis.html)(location, ...)
  - Agrega un segundo eje _x_ al `Axes`.
* - [Axes.secondary_yaxis](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.secondary_yaxis.html)(location, ...)
  - Agrega un segundo eje _y_ al `Axes`.
* - [Axes.table](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.table.html)(cellText=None, ...)
  - Agrega una tabla a un `Axes`.
* - [Axes.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html)(x, y, s, fontdict=None, **kwargs)
  - Agrega un texto al `Axes`.
```

<br/>

#### Ejemplo de _ax.annotate_

[Axes.annotate](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html): Agrega un texto a una gráfica para resaltar algún punto de la gráfica bajo una condición. Es posible agregar una flecha que apunte hacia un punto en particular y se agrege un texto.
```python
# Sintaxis de llamada
Axes.annotate(text, xy, xytext=None, xycoords='data', textcoords=None, arrowprops=None, 
              annotation_clip=None, **kwargs)
```

**Parámetros:**
- **text** - `str`: La cadena que se mostará en la gráfica.
- **xy** - `secuencia` de `float`: Es la posición del punto a resaltar, debe ser la misma escala que usan los ejes.
- **xytext** - `secuencia` de `float`: Es para indicar la posición del texto, es útil en caso de que en _xy_ se sobre encime con muchas cosas.
- **xycoords** - `str`, `Artist`, `Transform` o `callable`: Sistema de coordenadas para el argumetno _xy_. Consultar la documentación para más información.
- **arrowprops** - `dict`: Es para crear una fecha que una el texto (_xytext_) con el punto _xy_, es útil en caso de que moviste de lugar el texto con _xytext_, se utiliza un diccionario para cambiar las propiedades de la flecha (la key es el nombre de la propiedad values el es valor de la propiedad). Si se quiere la flecha en su formato por default poner un diccionario vacío (con '' o `dict()`). Para ver las posibles _keys_ consultar los parámetros de [FancyArrowPatch](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyArrowPatch.html#matplotlib-patches-fancyarrowpatch).
- **\*\*kwargs**: Propiedades de {ref}`matplotlib-text`.

**Retorna:**
- `Annotation`.

**Ejemplo**

En este ejemplo se añade el número de pasajeros exactos en el año 1954 por medio de una flecha.

```{code-cell} ipython3
# Crear objetos
fig=plt.figure()
ax=plt.axes()

# Graficar los datos
ax.plot(yearly_data['year'], 
        yearly_data['passengers'], 
        marker='o', 
        color=azul)

# Añadir elementos a la gráfica
ax.set_xlabel('Año')
ax.set_ylabel('Total de pasajeros')
ax.set_title('Tendencia de total de pasajeros')

# Añadir texto en el punto 1954
ax.annotate("2,867", 
            xy=[1954, 2867], 
            xytext=[1954, 2000], 
            arrowprops={"arrowstyle":"->", "color":"gray"})

# Show the plot
plt.show()
```

#### Ejemplo de _ax.text_

[Axes.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html): Agrega texto a un `Axes` en las coordenadas de _x_ y _y_.
```python
# Sintaxis de llamada
Axes.text(x, y, s, fontdict=None, **kwargs)
```
**Parámetros:**
- **x**, **y** - `float`: Posición en el cual colocar el texto. Los valores son en la misma escala que los ejes. Excepto si se aplica una transformación, con el parámetro _transform_.
- **s** - `str`: El texto a mostrar.
- **fontdict** - `dict`: Diccionario que sirve para especificar la apariencia del texto (propiedades de `Text`), los _keys_ son los nombres de las propiedades y _values_ sus respectivos valores.
- **\*\*kwargs**: Propiedades de {ref}`matplotlib-text`.


**Retorna:**
- `Text`.

**Ejemplo:**

En este ejemplo se añade el número de pasajeros exactos en el año 1954.

```{code-cell} ipython3
# Crear objetos
fig=plt.figure()
ax=plt.axes()

# Graficar los datos
ax.plot(yearly_data['year'], 
        yearly_data['passengers'], 
        marker='o', 
        color=azul)

# Añadir elementos a la gráfica
ax.set_xlabel('Año')
ax.set_ylabel('Total de pasajeros')
ax.set_title('Tendencia de total de pasajeros')

# Añadir texto en el punto 1954
ax.text(1954, 2650, "2,867")

# Show the plot
plt.show()
```

<br/>

### Triangulos no Estructurados

Métodos para crear gráficas de mallas no estructuradas. Este tipo de mallas se componen de puntos espaciados de manera irregular conectados por elementos triangulares, una aplicación común es visualización de datos geoespaciales.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [Axes.tricontour](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tricontour.html)(*args, **kwargs)
  - Grafica líneas de contorno en una cuadrícula triangular no estructurada.
* - [Axes.tricontourf](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tricontourf.html)(*args, **kwargs)
  - Grafica regiones de contorno en una cuadrícula triangular no estructurada.
* - [Axes.tripcolor](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tripcolor.html)(*args, ...)
  - Crea una gráfica de pseudocolor de una cuadrícula triangular no estructurada.
* - [Axes.triplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.triplot.html)(*args, **kwargs)
  - Grafica una cuadrícula triangular no estructurada como líneas y/o marcadores.
```

<br/>

### Gráficos interactivos

Métodos útiles para realizar y manipular gráficos interactivos. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [Axes.can_pan](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.can_pan.html)()
  - Indica si este `Axes` admite cualquier funcionalidad de botón de _pan/zoom_.
* - [Axes.can_zoom](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.can_zoom.html)()
  - Indica si este `Axes` admite la funcionalidad del botón _zoom_.
* - [Axes.contains](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.contains.html)(mouseevent)
  - Verifica si el _artist_ contiene el evento _mouse_.
* - [Axes.contains_point](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.contains_point.html)(point)
  - Indica si el "punto" (par de coordenadas de píxeles) está dentro del _patch_ del `Axes`.
* - [Axes.drag_pan](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.drag_pan.html)(button, key, x, y)
  - Se llama cuando el mouse se mueve durante una operación _pan_.
* - [Axes.end_pan](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.end_pan.html)()
  - Se llama cuando se completa una operación _pan_.
* - [Axes.format_coord](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.format_coord.html)(x, y)
  - Retorna una cadena de formato que formatea las coordenadas _x_, _y_.
* - [Axes.format_cursor_data](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.format_cursor_data.html)(data)
  - Retorna una representación de cadena de los datos.
* - [Axes.format_xdata](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.format_xdata.html)(x)
  - Retorna _x_ formateado como un _valor de x_.
* - [Axes.format_ydata](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.format_ydata.html)(y)
  - Retorna _y_ formateado como un _valor de y_.
* - [Axes.in_axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.in_axes.html)(mouseevent)
  - Indica si el evento dado (en coordenadas de visualización) está en el `Axes`.
* - [Axes.mouseover](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.mouseover.html)()
  - Indica si se solicita a este _artist_ información de contexto personalizada cuando el cursor del mouse se mueve sobre él.
* - [Axes.start_pan](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.start_pan.html)(x, y, button)
  - Se llama cuando ha comenzado una operación de _pan_.
* - **Establecer**
  -
* - [Axes.set_navigate](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_navigate.html)(b)
  - Establece si el `Axes` responde a los comandos de la barra de herramientas de navegación.
* - [Axes.set_navigate_mode](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_navigate_mode.html)(b)
  - Establece el estado del botón de la barra de herramientas de navegación.
* - **Recuperar**
  -
* - [Axes.get_cursor_data](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_cursor_data.html)(event)
  - Retorna los datos del cursor para un evento determinado.
* - [Axes.get_navigate](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_navigate.html)()
  - Indica si el `Axes` responde a los comandos de navegación.
* - [Axes.get_navigate_mode](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_navigate_mode.html)()
  - Recupa el estado del botón de la barra de herramientas de navegación -> 'PAN', 'ZOOM' o `None`.
```

<br/>

### Limpieza

Métodos para eliminar la configuración del objeto y limpiar el mismo. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [Axes.cla](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.cla.html)()
  - Limpia el `Axes`.
* - [Axes.clear](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.clear.html)()
  - Limpiar el `Axes`.
```

<br/>

### Otros

Otros métodos.

#### Artists

Métodos útiles para añadir otra clase de elemetos a un _axes_ o consultar los _artists_ en el _axes_. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [Axes.add_artist](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_artist.html)(a)
  - Añade un `Artist` al `Axes`, retorna el `Artist`. 
* - [Axes.add_child_axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_child_axes.html)(ax)
  - Añade un `AxesBase` a un hijo del `Axes`; Retorna el hijo `Axes`.
* - [Axes.add_collection](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_collection.html)(collection, autolim=True)
  - Agrega un `Collection` al `Axes`; Retorna la colección.
* - [Axes.add_container](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_container.html)(container)
  - Agrega un `Container` a los contenedores del `Axes`; Retorna el contenedor.
* - [Axes.add_image](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_image.html)(image)
  - Añade un `AxesImage` al `Axes`; Retorna la imagen.
* - [Axes.add_line](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_line.html)(line)
  - Agrega un `Line2D` al `Axes`; Retorna la línea.
* - [Axes.add_patch](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_patch.html)(p)
  - Agrega un `Patch` al `Axes`; Retorna el _patch_.
* - [Axes.add_table](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_table.html)(tab)
  - Agrega un `Table` al `Axes`; Retorna la tabla.
* - [Axes.get_default_bbox_extra_artists](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_default_bbox_extra_artists.html)()
  - Retorna una `list` default de _artists_ que se utilizan para el cálculo del cuadro delimitador.
* - [Axes.has_data](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.has_data.html)()
  - Indica si se ha agregado algún _artist_ al `Axes`.
* - [Axes.zorder](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.zorder.html)()
  - .
```

<br/>

#### Callbacks

Métodos para trabajar con _callbacks_.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [Axes.add_callback](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_callback.html)(func)
  - Agrega una función _callback_ que se llamará cada vez que una propiedad de los `Artist` cambia.
* - [Axes.pchanged](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pchanged.html)()
  - Llama a todas las _callbacks_ registradas.
* - [Axes.remove_callback](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.remove_callback.html)(oid)
  - Elimina una _callback_ según su id.
* - [Axes.stale](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.stale.html)()
  - Indica si el _artist_ está "obsoleto" y es necesario volver a dibujarlo para que el resultado coincida con el estado interno del _artist_.
```

<br/>

#### Graficado

Métodos útiles para imprimir (dibujar) la gráfica.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [Axes.draw](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.draw.html)(renderer)
  - Dibuja al _artist_ (y sus hijos) usando el renderizador proporcionado.
* - [Axes.draw_artist](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.draw_artist.html)(a)
  - Vuelva a dibujar eficientemente a un solo _artist_.
* - [Axes.get_rasterization_zorder](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_rasterization_zorder.html)()
  - Retorna el valor _zorder_ debajo del cual se rasterizarán los _artists_.
* - [Axes.get_tightbbox](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_tightbbox.html)(renderer=None, ...)
  - Retorna el cuadro delimitador ajustado del `Axes`, incluido los ejes y sus decoradores (xlabel, título, etc.).
* - [Axes.get_window_extent](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_window_extent.html)(renderer=None)
  - Retorna el cuadro delimitador del `Axes` en el espacio de visualización.
* - [Axes.redraw_in_frame](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.redraw_in_frame.html)()
  - Redibuja eficientemente los datos del `Axes`, pero no los _ticks_ de ejes, etiquetas, etc.
* - [Axes.set_rasterization_zorder](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_rasterization_zorder.html)(z)
  - Establece el _zorder threshold_ para la rasterización de la salida de gráficos vectoriales.
```

<br/>

#### Objetos hijos

Métodos útiles para recuperar objetos hijos de un `Artist` o `Axes`.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [Axes.findobj](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.findobj.html)(match=None, include_self=True)
  - Encuentra objetos de _artist_.
* - [Axes.get_children](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_children.html)()
  - Retorna un `list` de los hijos `Artist`  de este `Artist`.
* - [Axes.get_images](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_images.html)()
  - Retorna un `list` de `AxesImage` contenidos por el `Axes`.
* - [Axes.get_lines](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_lines.html)()
  - Retorna un `list` de líneas contenidas por el `Axes`.
```

<br/>

(axes-methods-customization)=
### Personalización

Funciones útiles para personalizar las gráficar como modificar, añadir o quitar elementos.

#### Generales

Métodos generales de personalización.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [Axes.axis](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axis.html)(arg=None, /, ...)
  - Método de conveniencia para obtener o establecer algunas propiedades de los eje.
* - [Axes.set](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set.html)(*, ...)
  - Establece varias propiedades del `Axes`a la vez. Para ver cuáles propiedades se pueden establecer visitar el link.
```

<br/>

#### Grid

Métodos para establecer o configurar el _grid_ (líneas de cruadrículas) en las gráficas.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [Axes.grid](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.grid.html)(visible=None, which='major', axis='both', **kwargs)
  - Configura las líneas de la cuadrícula.
```

<br/>

#### Ejes

Métodos útiles para personalización de los ejes en las gráficas.

##### Autoescala

Métodos para autoescalamiento y manipulación de los ejes

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [Axes.autoscale](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.autoscale.html)(enable=True, axis='both', tight=None)
  - Escala automáticamente la vista de los ejes a los datos (_toggle_).
* - [Axes.autoscale_view](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.autoscale_view.html)(tight=None, scalex=True, scaley=True)
  - Escala automáticamente los límites de la vista utilizando los límites de datos.
* - [Axes.margins](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.margins.html)(*margins, x=None, y=None, tight=True)
  - Establece o recupera márgenes de escala automática.
* - [Axes.relim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.relim.html)(visible_only=False)
  - Recalcula los límites de datos en función de los _artists_ actuales.
* - [Axes.use_sticky_edges](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.use_sticky_edges.html)()
  - Al realizar el escalado automático, indica si se deben obedecer todos los `Artist.sticky_edges`.
* - **Establecer**
  -
* - [Axes.set_autoscale_on](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_autoscale_on.html)(b)
  - Establece si el escalado automático se aplica a cada eje en el siguiente _draw_ o se llama a `Axes.autoscale_view`.
* - [Axes.set_autoscalex_on](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_autoscalex_on.html)(b)
  - Establece si el eje _x_ se escala automáticamente al graficar o mediante `Axes.autoscale_view`.
* - [Axes.set_autoscaley_on](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_autoscaley_on.html)(b)
  - Establezce si el eje _y_ se escala automáticamente al graficar o mediante `Axes.autoscale_view`.
* - [Axes.set_xmargin](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xmargin.html)(m)
  - Establece el _padding_ de los límites de datos del eje _x_ antes del escalado automático.
* - [Axes.set_ymargin](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ymargin.html)(m)
  - Establece el _padding_ de los límites de datos del eje _y_ antes del escalado automático.
* - **Recuperar**
  -
* - [Axes.get_autoscale_on](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_autoscale_on.html)()
  - Retorna `True` si cada eje tiene escala automática, `False` de lo contrario.
* - [Axes.get_autoscalex_on](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_autoscalex_on.html)()
  - Indica si el eje _x_ tiene escala automática.
* - [Axes.get_autoscaley_on](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_autoscaley_on.html)()
  - Indica si el eje _y_ tiene escala automática.
```

<br/>

##### Compartir ejes

Métodos para compartir un eje entre diferentes gráficas o indicar que una gráfica tenga dos ejes diferentes en la misma dimensión.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [Axes.sharex](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.sharex.html)(other)
  - Comparte el eje _x_ con _other_.
* - [Axes.sharey](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.sharey.html)(other)
  - Comparte el eje _y_ con _other_.
* - [Axes.twinx](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.twinx.html)()
  - Crea un `Axes` gemelo con el cual comparte el eje _x_. Permite que en una misma gráfica, se grafiquen 2 series, con escalas del eje _y_ diferentes sin afectar la proporción de las curvas. Ver notas.
* - [Axes.twiny](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.twiny.html)()
  - Crea un `Axes` gemelo con el cual comparte el eje _y_. Permite que en una misma gráfica, se grafiquen 2 series, con escalas del eje _X_ diferentes sin afectar la proporción de las curvas. Ver notas
* - **Recuperar**
  -
* - [Axes.get_shared_x_axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_shared_x_axes.html)()
  - Retorna una _view_ inmutable en el _x-axes Grouper_ compartido.
* - [Axes.get_shared_y_axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_shared_y_axes.html)()
  - Retorna una _view_ inmutable en el _y-axes Grouper_ compartido.
```

Notas de `twinx()`

Se utiliza  de la siguiente forma:
```python
# Uso de twinx()
ax2=ax1.twinx()
```
-	_ax2_ tendrá el mismo eje _x_ que _ax1_. 
-	Posteriormente se puede usar _ax2_ para agregar una capa a la gráfica de _ax1_, pero _ax2_ tendrá su propio eje _y_, la forma como se declara `ax2.plot()` es igual, se deben de especificar ambos valores del eje _x_ y _y_. 
-	En ambos `Axes` _x_ debe tener los mismo valores.


<br/>

##### Escala

Métodos útiles para establecer o retornar la escala de los ejes de manera indivual.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - **Establecer**
  -
* - [Axes.set_xscale](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xscale.html)(value, **kwargs)
  - Establece la escala del eje _x_.
* - [Axes.set_yscale](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yscale.html)(value, **kwargs)
  - Establece la escala del eje _y_.
* - **Recuperar**
  -
* - [Axes.get_xscale](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_xscale.html)()
  - Retorna la escala del eje _x_ (como una cadena).
* - [Axes.get_yscale](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_yscale.html)()
  - Retorna la escala del eje _y_ (como una cadena).
```

<br/>

**Ejemplo**

En este ejemplo se ajustan las escalas en ambos ejes a una escalar logarítmica para que los datos se puedan visualizar de mejor manera.

```{code-cell} ipython3
# Importar dataset
planets=sns.load_dataset("planets")

# Crear gráfica
fig, ax=plt.subplots(figsize=(8, 6))
ax.scatter(planets['orbital_period'], planets['distance'], c=azul, alpha=0.3)

# Ajustar escalar en ambos ejes
ax.set_xscale('log')
ax.set_yscale('log')

# Imprimir la figura
plt.show()
```

<br/>

##### Límites y dirección

Métodos para establecer los límites de los ejes, es decir, el rango de valores en los ejes.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [Axes.invert_xaxis](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.invert_xaxis.html)()
  - Invierte el eje _x_.
* - [Axes.invert_yaxis](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.invert_yaxis.html)()
  - Invierte el eje _y_.
* - [Axes.update_datalim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.update_datalim.html)(xys, updatex=True, updatey=True)
  - Extiende el `dataLim` Bbox para incluir los puntos dados.
* - [Axes.xaxis_inverted](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.xaxis_inverted.html)()
  - Indica si el eje _x_ está orientado en la dirección "inversa".
* - [Axes.yaxis_inverted](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.yaxis_inverted.html)()
  - Indica si el eje _y_ está orientado en la dirección "inversa".
* - **Establecer**
  -
* - [Axes.set_xbound](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xbound.html)(lower=None, upper=None)
  - Establece los límites numéricos inferior y superior del eje _x_.
* - [Axes.set_xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html)(left=None, right=None, ...)
  - Establece los límites de vista del eje _x_.
* - [Axes.set_ybound](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ybound.html)(lower=None, upper=None)
  - Establece los límites numéricos inferior y superior del eje _y_.
* - [Axes.set_ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html)(bottom=None, top=None, ...)
  - Establece los límites de vista del eje _y_.
* - **Recuperar**
  -
* - [Axes.get_xbound](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_xbound.html)()
  - Retorna los límites inferior y superior del eje _x_, en orden creciente.
* - [Axes.get_xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_xlim.html)()
  - Retorna los límites de vista del eje _x_.
* - [Axes.get_ybound](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_ybound.html)()
  - Retorna los límites inferior y superior del eje _y_, en orden creciente.
* - [Axes.get_ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_ylim.html)()
  - Retorna los límites de vista del eje _y_.
```

<br/>

##### Proyección en otras escalas

Métodos para realizar transformaciones en la escala de los ejes.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [Axes.get_data_ratio](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_data_ratio.html)()
  - Retorna la relación de aspecto de los datos escalados.
* - [Axes.get_xaxis_text1_transform](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_xaxis_text1_transform.html)(pad_points)
  - .
* - [Axes.get_xaxis_text2_transform](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_xaxis_text2_transform.html)(pad_points)
  - .
* - [Axes.get_xaxis_transform](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_xaxis_transform.html)(which='grid')
  - Recupera la transformación utilizada para dibujar etiquetas, _ticks_ y líneas de cuadrícula del eje _x_.
* - [Axes.get_yaxis_text1_transform](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_yaxis_text1_transform.html)(pad_points)
  - .
* - [Axes.get_yaxis_text2_transform](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_yaxis_text2_transform.html)(pad_points)
  - .
* - [Axes.get_yaxis_transform](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_yaxis_transform.html)(which='grid')
  - Recupera la transformación utilizada para dibujar etiquetas, _ticks_ y líneas de cuadrícula del eje _y_.
* - [Axes.name](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.name.html)()
  - Retorna el nombre del _Axes_.
```

<br/>

##### Relación de aspecto

Métodos para establer la relación entre los ejes de la gráfica. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [Axes.apply_aspect](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.apply_aspect.html)(position=None)
  - Ajusta el `Axes` para una relación de aspecto de datos especificada.
* - **Establecer**
  -
* - [Axes.set_adjustable](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_adjustable.html)(adjustable, share=False)
  - Establece cómo el `Axes` se ajusta para lograr la relación de aspecto requerida.
* - [Axes.set_aspect](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_aspect.html)(aspect, adjustable=None, anchor=None, share=False)
  - Establece la relación de aspecto de la escala de los ejes, es decir, escala _y/x_.
* - [Axes.set_box_aspect](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_box_aspect.html)(aspect=None)
  - Establece la relación entre la altura y el ancho del `Axes`.
* - **Recuperar**
  -
* - [Axes.get_adjustable](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_adjustable.html)()
  - Indica si el `Axes` ajustará su dimensión física ('box') o sus límites de datos ('datalim') para lograr la relación de aspecto deseada.
* - [Axes.get_aspect](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_aspect.html)()
  - Retorna la relación de aspecto de la escala de los ejes.
* - [Axes.get_box_aspect](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_box_aspect.html)()
  - Retorna la relación entre la altura y el ancho del `Axes`.
```

<br/>

##### Ticks

Métodos útiles para retornar o establecer los _ticks_ del _axes_. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [Axes.locator_params](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.locator_params.html)(axis='both', tight=None, **kwargs)
  - Gestiona el comportamientos de los _icks_ principales.
* - [Axes.minorticks_off](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.minorticks_off.html)()
  - Elimina los _ticks_ menores del `Axes`.
* - [Axes.minorticks_on](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.minorticks_on.html)()
  - Muestra los _ticks_ menores en el `Axes`.
* - [Axes.tick_params](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html)(axis='both', **kwargs)
  - Modifica la apariencia de los _ticks_, las etiquetas de los _ticks_ y las líneas de cuadrícula.
* - [Axes.ticklabel_format](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.ticklabel_format.html)(*, axis='both', style='', scilimits=None, useOffset=None, useLocale=None, useMathText=None)
  - Configura el `ScalarFormatter` utilizado por defecto para `Axes` lineales.
* - [Axes.xaxis_date](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.xaxis_date.html)(tz=None)
  - Configura los _ticks_ y sus etiquetas en el eje para tratar los datos a lo largo del eje _x_ como fechas.
* - [Axes.yaxis_date](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.yaxis_date.html)(tz=None)
  - Configura los _ticks_ y sus etiquetas en el eje para tratar los datos a lo largo del eje _y_ como fechas.
* - **Establecer**
  -
* - [Axes.set_xticklabels](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticklabels.html)(minor=False, which=None)
  - Establece los _ticks_ del eje _x_. Está desaconsejado el uso de este método.
* - [Axes.set_yticklabels](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yticklabels.html)(minor=False, which=None)
  - Establece los _ticks_ del eje _y_. Está desaconsejado el uso de este método.
* - [Axes.set_xticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticks.html)(ticks, labels=None, ...)
  - Establece las ubicaciones de loss _ticks_ del eje _x_, opcionalmente, las etiquetas de los mismos.
* - [Axes.set_yticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yticks.html)(ticks, labels=None, ...)
  - Establece las ubicaciones de las _ticks_ del eje _y_, opcionalmente, las etiquetas de los mismos.
* - **Recuperar**
  -
* - [Axes.get_xgridlines](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_xgridlines.html)()
  - Retorna las líneas de cuadrícula del eje _x_ como un `list` de `Line2D`.
* - [Axes.get_xmajorticklabels](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_xmajorticklabels.html)()
  - Retorna las etiquetas de los _ticks_ principales del eje _x_, como `list` de `Text`.
* - [Axes.get_xminorticklabels](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_xminorticklabels.html)()
  - Retorna las etiquetas de los _ticks_ menores del eje _x_, como `list` de `Text`.
* - [Axes.get_xticklabels](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_xticklabels.html)(minor=False, which=None)
  - Recupera las etiquetas de los _ticks_ del eje _x_.
* - [Axes.get_xticklines](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_xticklines.html)(minor=False)
  - Retorna las líneas de _ticks_ del eje _x_ como `list` de `Line2D` .
* - [Axes.get_xticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_xticks.html)(*, minor=False)
  - Retorna las ubicaciones de los _ticks_ del eje _x_ en coordenadas de los datos.
* - [Axes.get_ygridlines](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_ygridlines.html)()
  - Retorna las líneas de la cuadrícula del eje _y_ como `list` de `Line2D` s.
* - [Axes.get_ymajorticklabels](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_ymajorticklabels.html)()
  - Retorna las etiquetas de los _ticks_ principales del eje _y_, como `list` de `Text`.
* - [Axes.get_yminorticklabels](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_yminorticklabels.html)()
  - Retorna las etiquetas de los _ticks_ menores del eje _y_, como `list` de `Text`.
* - [Axes.get_yticklabels](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_yticklabels.html)(minor=False, which=None)
  - Retorna las etiquetas de los _ticks_ del eje _y_.
* - [Axes.get_yticklines](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_yticklines.html)(minor=False)
  - Retorna las líneas de los _ticks_ del eje _y_ como `list` de `Line2D` .
* - [Axes.get_yticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_yticks.html)(*, minor=False)
  - Retorna las ubicaciones de los los _ticks_ del eje _y_ en coordenadas de los datos.
```

Patrones útiles:

```python
# modificar parámetros generales de los ticks
ax.tick_params('y', **kwargs)

# Girar etiquetas de los ticks del eje _x_
ax.bar(df.index, df['col'])
ax.set_xticklabels(df.index, rotation=90)
```

<br/>

**Ejemplo**:

En este ejemplo se modifican los _ticks_ del eje _y_. Por default, en esa gráfica, se muestran los _ticks_ del 2,000 al 5,000, con un paso de 1,000. Con esta nueva configuración se muestran desde 1,000 hasta 6,000 con un paso de 500.

```{code-cell} ipython3
# Crear figura y axes
fig, ax=plt.subplots(1, 1)

# Graficar datos
ax.plot(yearly_data['year'], 
        yearly_data['passengers'], 
        label='Passengers', 
        marker='o', 
        color=azul)

ax.set_yticks(list(range(1000, 6500, 500)))

# Show the plot
plt.show()
```

<br/>

##### Unidades

Métodos útiles para modificar las unidades de los ejes. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [Axes.convert_xunits](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.convert_xunits.html)(x)
  - Convierte _x_ usando el tipo de unidad del eje _x_.
* - [Axes.convert_yunits](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.convert_yunits.html)(y)
  - Convierte _y_ usando el tipo de unidad del eje _y_.
* - [Axes.have_units](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.have_units.html)()
  - Indica si las unidades están establecidas en cualquier eje.
```

<br/>

##### Visualización

Métodos para retornar o establecer ciertas características de la apariencia de la gráfica. 

:::{tip}
Para ocultar ejes ver también parámetro _option_ del método [Axes.axis()](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axis.html).
:::

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - **Establecer**
  -
* - [Axes.set_axis_off](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_axis_off.html)()
  - Oculta todos los componentes visuales de los ejes _x_ y _y_.
* - [Axes.set_axis_on](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_axis_on.html)()
  - Muestra todos los componentes visuales de los ejes _x_ y _y_.
* - [Axes.set_axisbelow](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_axisbelow.html)(b)
  - Establece si los _ticks_ de los ejes y las líneas de cuadrícula están por encima o por debajo de los _artists_.
* - [Axes.set_facecolor](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_facecolor.html)(color)
  - Establece el _facecolor_ del `Axes`.
* - [Axes.set_frame_on](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_frame_on.html)(b)
  - Establece si el _patch_ rectangular del `Axes` está dibujado.
* - **Recuperar**
  -
* - [Axes.get_axisbelow](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_axisbelow.html)()
  - Indica si los _tick_ de los ejes y las líneas de cuadrícula están por encima o por debajo de la mayoría de los _artists_.
* - [Axes.get_facecolor](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_facecolor.html)()
  - Recupera el _facecolor_ del `Axes`.
* - [Axes.get_frame_on](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_frame_on.html)()
  - Indica si el _patch_ rectangular del `Axes` está dibujado.
```

<br/>

---
#### Leyenda

Métodos para añadir leyendas a las gráficas o manipular las mismas.

:::{caution}
Para que una leyenda se coloque correctame se debió definir el parámetro _label_ en las llamadas a las gráficas.
:::

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [Axes.get_legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_legend.html)()
  - Retorna la instancia `Legend` o `None` si no está definida ninguna leyenda.
* - [Axes.get_legend_handles_labels](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_legend_handles_labels.html)(legend_handler_map=None)
  - Retorna los identificadores y etiquetas de la leyenda.
* - [Axes.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html)(*args, **kwargs)
  - Coloca una leyenda en el `Axes`.
```

<br/>

---
#### Posición

Métodos para establecer o retornar la posición del `Axes` y otros elementos.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - **Establecer**
  -
* - [Axes.set_anchor](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_anchor.html)(anchor, share=False)
  - Define la ubicación del _anchor_.
* - [Axes.set_axes_locator](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_axes_locator.html)(locator)
  - Establece el `Axes` _locator_.
* - [Axes.set_position](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_position.html)(pos, which='both')
  - Establece la posición del `Axes`.
* - [Axes.set_subplotspec](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_subplotspec.html)(subplotspec)
  - Establece el `SubplotSpec`.
* - **Recuperar**
  -
* - [Axes.get_anchor](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_anchor.html)()
  - Recupera la ubicación de _anchor_.
* - [Axes.get_axes_locator](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_axes_locator.html)()
  - Retorna el _axes\_locator_.
* - [Axes.get_position](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_position.html)(original=False)
  - Retorna la posición del `Axes` dentro de la figura como `Bbox`.
* - [Axes.get_subplotspec](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_subplotspec.html)()
  - Retorna el `SubplotSpec` asociado con el _subplot_, o `None`.
* - [Axes.reset_position](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.reset_position.html)()
  - Restablece la posición activa a la posición original.
```

<br/>

---
#### Títulos y etiquetas

Métodos para establecer o retornar títulos y etiquetas.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [Axes.label_outer](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.label_outer.html)(remove_inner_ticks=False)
  - Muestra solo sólo las etiquetas "externas" y las etiquetas de _ticks_.
* - **Establecer**
  -
* - [Axes.set_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html)(label, fontdict=None, loc=None, pad=None, ...)
  - Establece un título para el `Axes`.
* - [Axes.set_xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html)(xlabel, fontdict=None, labelpad=None, ...)
  - Establece la etiqueta para el eje x.
* - [Axes.set_ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html)(ylabel, fontdict=None, labelpad=None, ...)
  - Establece la etiqueta para el eje y.
* - **Recuperar**
  -
* - [Axes.get_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_title.html)(loc='center')
  - Retorna el título del `Axes`.
* - [Axes.get_xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_xlabel.html)()
  - Retorna la _xlabel_.
* - [Axes.get_ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_ylabel.html)()
  - Retorna la _ylabel_.
```

Patrones útiles:
```python
# Establecer etiqueta del eje x
ax.set_xlabel('x label')

# Establecer etiqueta del eje y
ax.set_ylabel('y label')

# Establecer título
ax.set_title('title')
```

<br/>

---
## Funciones útiles

A continuación se presentan algunas funciones útiles al trabajar con instancias de la clase `Axes`.

- `plt.gca( )`: Retorna el `Axes` actual., si no hay uno entonces crea uno.

