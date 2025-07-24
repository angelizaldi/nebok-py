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

# Pyplot

```{code-cell} ipython3
:tags: ["remove-input"]

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

azul = "#30adb9"
cafe = "#ba6a30"
cafe_claro = "#cf9975"
```

`matplotlib.pyplot` es un módulo que contiene una diversa cantidad de funciones útiles para crear gráficas en una interfaz basada en _Matlab_, aunque también contiene las funciones necesarias para trabajar en una interfaz orientada a objetos.

---
## Interfaz basada en Matlab

Para crear gráficas en un interfaz basada en _Matlab_ se utiliza las funciones del módulo `pyplot`, lo que permite llevar un control implícito de los objetos _ax_ y _figure_, es decir, no es necesario declararlos. Las figuras pueden tener un _axes_ o múltiples _axes_ como se verá a continuación.

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

### Figura con un solo _axes_

Para crear una figura con un único axes basta con llamar cualquiera de las {ref}`pyplot-funciones`. 

```python
# Llamar a alguna función de pyplot para crear una gráfica.
plt.plot() # Ejemplo con plt.plot()
# Llamar a alguna función de pyplot para personalizar gráficas.
plt.tile() # Ejemplo con plt.title()
...

# Imprimir la gráfica
plt.show()
```
**Notas**:
- Hacer llamadas de las funciones de `matplotlib.pyplot` para agregar {ref}`pyplot-funciones` o {ref}`pyplot-personalizacion`.
- Este estilo mantiene un seguimiento de los _fig_ y _ax_ actuales de manera implícita.
- Al finalizar para mostrar la gráfica usar `plt.show()`.

<br/>

**Ejemplo**:
En este ejemplo se utiliza directamente la función `plt.plot()` para crear una figura con un _axes_, además se hacen llamadas a las funciones `plt.xlabel()`, `plt.ylabel()`, `plt.title()` y `plt.legend()` para añadir elementos a la gráfica.

```{code-cell} ipython3
# Crear nueva figura (opcional)
plt.figure() 

# Graficar los datos
plt.plot(yearly_data['year'], 
         yearly_data['passengers'], 
         label='Passengers', 
         marker='o', 
         color=azul)

# Agregar elementos
plt.xlabel('Año')
plt.ylabel('Total de pasajeros')
plt.title('Tendencia de total de pasajeros')
plt.legend()

# Imprimir la figura
plt.show()
```

<br/>

### Figura con múltiples _axes_

Para crear una figura con múltiples axes, se usa la función `plt.subplot()`, en cada llamada se debe de indicar el número total de filas y columnas que tendrá la figura y el indice del _axes_ con el que se estará trabajando en cada llamada.

```python
# Opcionalmente llamar a la función plt.figure()
[plt.figure()]

# Llamar a la función plt.subplot()
plt.subplot(n, m, i1)
# Llamar a alguna función de pyplot para crear una gráfica.
plt.plot() # Ejemplo con plt.plot()
# Llamar a alguna función de pyplot para personalizar gráficas.
plt.tile() # Ejemplo con plt.title()

# Llamar a la función plt.subplot()
plt.subplot(n, m, i2)
# Llamar a alguna función de pyplot para crear una gráfica.
plt.plot() # Ejemplo con plt.plot()
# Llamar a alguna función de pyplot para personalizar gráficas.
plt.tile() # Ejemplo con plt.title()

# Hacer tantas llamadas a las funciones como sea necesario
...

# Imprimir la gráfica
plt.show()
```
**Notas**:
- Para trabajar con una gráfica en particular hacer una llamada a la función `plt.subplot()` indicando el índice y el número total de filas y columnas.
- Una vez se haya llamado a la función `plt.subplot()` indicando el índice, hacer llamadas de las funciones de `matplotlib.pyplot` para agregar {ref}`pyplot-funciones` o para {ref}`pyplot-personalizacion`.
- Este estilo mantiene un seguimiento de los _fig_ y _ax_ actuales de manera implícita.
- Al finalizar para mostrar la gráfica usar `plt.show()`.

<br/>

**Ejemplo**:
En este ejemplo se llama a la función `plt.subplot()` para cada _axes_ en la figura, en este caso se hacen dos llamadas.  

```{code-cell} ipython3
# Crear nueva figura (opcional)
plt.figure(figsize=(12, 5))

# Graficar datos de 1950
ax1=plt.subplot(1, 2, 1)
plt.bar(flights_1950['month'], flights_1950['passengers'], color=azul)
plt.title('Pasajeros en 1950')
plt.xlabel('Mes')
plt.ylabel('Número de Pasajeros')
plt.xticks(rotation=45)

# Graficar datos de 1960
plt.subplot(1, 2, 2, sharey=ax1)
plt.bar(flights_1960['month'], flights_1960['passengers'], color=cafe)
plt.title('Pasajeros en 1960')
plt.xlabel('Mes')
plt.xticks(rotation=45)

# Ajustar el layout
plt.tight_layout()

# Imprimir la figura
plt.show()
```

## Configuración

Funciones para establecer la configuración general de `Matplotlib`. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [rc](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.rc.html)(group, **kwargs)
  - Modifica la configuración por default de las gráficas. Ver {ref}`pyplot-config-rc-notes`.
* - [rc_context](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.rc_context.html)(rc=None, fname=None)
  - Retorna un administrador de contexto para cambiar temporalmente _rcParams_.
* - [rcdefaults](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.rcdefaults.html)()
  - Restaura el `rcParams` de estilos predeterminados de `Matplotlib`.
```

(pyplot-config-rc-notes)=
### Notas de _plt.rc_

:::{warning}
Se recomienda antes de modificar las configuraciones estándar, guardar una copia de la configuración: <br/> `config_default=plt.rcParams.copy()`, alternativamente se puede usar la función `plt.rcdefaults()`.

Para retornar a la configuración por default usar: <br> `plt.rcParams.update(Ipython_default)`
:::

[rc](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.rc.html): Modifica la configuración por default de las gráficas.

```python
# Sintaxis de llamada
plt.rc(group, **kwargs)
```
- **group** - `str`: Es el grupo para el _rc_. Por ejemplo 'figure', 'axes', 'grid', 'xtick', 'ytick', 'patch', 'lines', etc.
- **\*\*kwargs**: Son los parámetros de group, para ver todos los grupos y parámetros  (están en la forma de _group.param_nom_) revisar la [documentacion](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.RcParams)
- Una forma de definir los parámetros es usando un diccionario donde _key_ es el nombre del parámetro y _value_ es el valor de ese parámetro, posteriormente al llamar la función usar (donde _Y_ es `dict`): <br> `plt.rc(group, **Y)`
- Otra forma de definir los valores por default es sobreescribiendo los valores de los _keys_:  <br> `plt.rcParams['group.param']=value`

<br/>

---
## Figuras y _Axes_

A continuación se presentan las funciones relacionadas con la creación y manipulaciones de figuras y axes. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axes.html)(arg=None, **kwargs)
  - Añade un `Axes` a la figura actual y lo convierte en el `Axes` actual.
* - [cla](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.cla.html)()
  - Limpia los _Axes_ actuales.
* - [clf](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.clf.html)()
  - Limpia la figura actual.
* - [close](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.close.html)(fig=None)
  - Cierra una ventana de una figura.
* - [delaxes](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.delaxes.html)(ax=None)
  - Elimina un `Axes` (por defecto los _Axes_ actuales) de una figura.
* - [fignum_exists](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.fignum_exists.html)(num)
  - Indica si existe la figura con la identificación dada.
* - [figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html)(num=None, figsize=None, dpi=None, ...)
  - Crea una nueva figura o activa una figura existente.
* - [gca](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.gca.html)()
  - Retorna el `Axes` actual.
* - [gcf](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.gcf.html)()
  - Retorna la figura actual.
* - [get_figlabels](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.get_figlabels.html)()
  - Retorna un `list` de etiquetas de figuras existentes.
* - [get_fignums](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.get_fignums.html)()
  - Retorna un `list` de los identificadores numéricos de figuras existentes.
* - [sca](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.sca.html)(ax)
  - Establece el `Axes` actual a _ax_ y la `Figure` actual al padre de _ax_.
* - [subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html)(*args, **kwargs)
  - Añade un `Axes` a la figura actual o recupera un `Axes` existente.
* - [subplot2grid](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot2grid.html)(shape, loc, rowspan=1, colspan=1, fig=None, **kwargs)
  - Crea un _subplot_ en una ubicación específica dentro de un _grid_.
* - [subplot_mosaic](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot_mosaic.html)(mosaic, ...)
  - Crea un _layout_ de `Axes` basado en arte ASCII o listas anidadas.
* - [subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html)(nrows=1, ncols=1, ...)
  - Crea una figura y un `ndarray` de `Axes`.
* - [twinx](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.twinx.html)(ax=None)
  - Crea y devuelve un segundo eje que comparte el eje _x_.
* - [twiny](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.twiny.html)(ax=None)
  - Crea y devuelve un segundo eje que comparte el eje _y_.
```

<br/>

---
(pyplot-funciones)=
## Funciones de gráficas

### Básicas

Funciones útiles para crear gráficas básicas. 

#### Líneas y Marcadores

Estas gráficas están relaciones con gráficas de líneas, diagramas de dispersión, entre otras.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [errorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.errorbar.html)(x, y, yerr=None, xerr=None, fmt='', ...)
  - Grafica _x_ contra _y_ como línea o _markers_, junto con _errorbars_. Los errores se indican como escalar (el mismo para todas las observaciones), como 1D `ndarray` el error para cada observación o como 2D `ndarray` la parte positiva y negativa del error individualmente para cada observación.
* - [eventplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.eventplot.html)(positions, orientation='horizontal', ...)
  - Grafica líneas paralelas idénticas en las posiciones dadas.
* - [loglog](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.loglog.html)(*args, **kwargs)
  - Crea una gráfica con escala logarítmica en los ejes _x_ e _y_.
* - [plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html)(*args, scalex=True, scaley=True, data=None, **kwargs)
  - Grafica _y_ versus _x_ como líneas y/o marcadores.
* - [scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html)(x, y, s=None, c=None, marker=None, ...)
  - Realiza una gráfica de dispersión dando los valores de los ejes _x_ y _y_.
* - [semilogx](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.semilogx.html)(*args, **kwargs)
  - Crea un gráfico con escala logarítmica en el eje _x_.
* - [semilogy](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.semilogy.html)(*args, **kwargs)
  - Crea un gráfico con escala logarítmica en el eje _y_.
* - [stem](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.stem.html)(*args, linefmt=None, markerfmt=None, ...)
  - Crea un gráfica con rectas verticales para cada observación desde _base_ hasta _head_, y con un marcador en _head_.
* - [step](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.step.html)(x, y, *args, where='pre', data=None, **kwargs)
  - Crea una gráfica de _pasos_.
```

##### Notas de _plot_

[plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html): Realiza una gráfica dando los valores de los ejes _x_ y _y_, ya sean líneas o puntos.
```python
# Sintaxis de llamada
plt.plot([x], y, [fmt], *, data=None, **kwargs)
plt.plot([x], y, [fmt], [x2], y2, [fmt2], ..., **kwargs)
```
- **Parámetros:**
    - **x**, **y** - `array-like` o `label`: Coordenadas de los puntos horizontales y verticales, respectivamente. Si no se especifica _x_ será un rango de _0_ a `len(y) - 1`. Pueden ser etiquetas en caso de que se defina el argumento _data_.
    - **data** - `indexable object`: Objeto que se pueda aplicar `obj['label']` y retorne un 1D `array-like`, lo más común que sea un `DataFrame`.
    - **fmt** - `str`: Es una cadena de formato, para indicar cierto formato que debe de tener la gráfica especificamente, el tipo de linea, tipo de marker y el color de los mismos. Ver {ref}`matplotlib-fmt`.
    - **\*\*kwargs**: Propiedades de {ref}`matplotlib-line2d`.
    - Parámetros en la segunda forma de llamar la función:
        - **xi**, **yi** - `array-like` o `scalar`: Cordenadas de los puntos horizontales y verticales, respectivamente.
        - **fmti** - `str`: Es una cadena de formato, para indicar cierto formato que debe de tener la gráfica.
- **Retorna:**
    - `list` de [Line2D](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D).

:::{note}
Notar que también se pueden usar como argumentos propiedades de la clase {ref}`matplotlib-line2d`.
:::

**Ejemplo**:
En este ejemplo se utiliza directamente la función `plt.plot()` para crear una figura con un _axes_, además se hacen llamadas a las funciones `plt.xlabel()`, `plt.ylabel()`, `plt.title()` y `plt.legend()` para añadir elementos a la gráfica.

```{code-cell} ipython3
# Crear nueva figura (opcional)
plt.figure() 

# Graficar los datos
plt.plot(yearly_data['year'], 
         yearly_data['passengers'], 
         marker='o', 
         color=azul)

# Agregar etiquetas y título
plt.xlabel('Año')
plt.ylabel('Total de pasajeros')
plt.title('Tendencia de total de pasajeros')

# Imprimir la figura
plt.show()
```

<br/>

##### Notas de _scatter_

[scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html): Realiza una gráfica de dispersión dando los valores de los ejes X y Y.
```python
# Sintaxis de llamada
plt.scatter(x, y, s=None, c=None, *, marker=None, cmap=None, norm=None, vmin=None, 
            vmax=None, alpha=None, linewidths=None, edgecolors=None, colorizer=None, 
            plotnonfinite=False, data=None, **kwargs)
```
- **Parámetros:**
    - **x**, **y** - `array-like` o `float`: Cordenadas de los puntos horizontales y verticales, respectivamente.
    - **s** - `float` o `array-like`: Tamaño de los markers en puntos, al cuadrado.
    - **c** - `array-like`, `list` de `color` o `color`: Color de los markers.
        - `scalar` o `secuencia` de números: Esos números serán mapeados con _cmap_, dependiendo del valor se le asignará un color del mapa de color, los número se emparejarán por posición con los valores de _x_ y _y_, para determinar qué color usar en cada coordenada. Por lo tanto la longitud de la secuencia debe de ser igual que la de _x_ y _y_.
        - `secuencia` de `color`: Colores a usar para cada valor de _x_ y _y_, se empatan por posición y debe de tener la misma longitud que _x_ y _y_. Ver {ref}`matplotlib-color`.
        - `color`: Un solo color para usar en todos lo puntos. Ver {ref}`matplotlib-color`.
        - Se puede usar los valores de una variable categórica para que cada uno tenga un valor diferente. Ver {ref}`matplotlib-colormap`.
    - **marker** - `MarkeyStyle`: Revisar {ref}`matplotlib-markers`.
    - **cmap** - `str` o `ColorMap`: Mapa de color. Se usa solo si _c_ es un `array-like` de `float`. Ver {ref}`matplotlib-colormap`.
    - **alpha** - `float`: Para indicar la opacidad de la gráfica. Es un valor entre 0 y 1, donde 0 es completamente transparente y 1 es completamente opaco.
    - **linewidths** - `float` o `array-like`: Grosor del borde de los markers.
    - **edgecolors** - {'face', 'none', `None`}, `color` o `secuencia` de `color`: Color del borde de los markers. Si es 'face' será el mismo que el fondo del _marker_, si es 'none' no tendrá color o se puede especificar el color. Ver {ref}`matplotlib-color`.
    - **\*\*kwargs**: Propiedades de los objetos [PathCollection](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PatchCollection.set).
- **Retorna:**
    - [PathCollection](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PatchCollection).

:::{note}
Notar que también se pueden usar como argumentos propiedades de la clase [PathCollection](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PatchCollection.set).
:::

Patrones útiles:

```python
# Mapear colores a etiquetas de columna categórica (apply)
colors = {'cat1':'color1','cat2':'color2', ...}
df.plot.scatter(x=df['x'], y=df['y'], c=df['cat'].apply(lambda x: colors[x]))

# Mapear colores a etiquetas de columna categórica (map)
colors = {'cat1':'color1','cat2':'color2', ...}
plt.plot(x=df['x'], y=df['y'], c=df['cat'].map(colors))

# Mapear colores a etiquetas de columna categórica (as category)
plt.plot(x=df['x'], y=df['y'], c=df['cat'].astype("category").cat.codes)
```

**Ejemplo:**

En este ejemplo se utiliza la función `plt.scatter()` para crear un diagrama de dispersión entre _petal length_ vs _petal width_, usando el dataset _iris_.

```{code-cell} ipython3

# Importar el dataset iris
iris=sns.load_dataset("iris")

# Crear scatterplot: petal length vs petal width
plt.figure(figsize=(5, 4))
scatter=plt.scatter(iris["petal_length"], 
                      iris["petal_width"], 
                      c=iris["species"].astype("category").cat.codes, 
                      s=iris["sepal_length"] * 10, 
                      cmap="Dark2", 
                      alpha=0.7)

# Crear leyenda para "species"
species_labels=iris["species"].unique()
colors=scatter.cmap(np.linspace(0, 1, len(species_labels)))
handles=[plt.Line2D([0], [0], marker="o", color="w", markersize=10, markerfacecolor=colors[i]) for i in range(len(species_labels))]
plt.legend(handles, species_labels, title="Species", loc="upper left")

# Imprimir la figura
plt.tight_layout()
plt.show()
```

<br/>

#### Barras

Gráficas que involucran barras verticales y horizontales.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [bar](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar.html)(x, height, width=0.8, bottom=None, ...)
  - Crea una gráfica de barras.
* - [bar_label](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar_label.html)(container, labels=None, ...)
  - Genera etiquetas para una gráfica de barras.
* - [barh](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.barh.html)(y, width, height=0.8, left=None, ...)
  - Crea una gráfica de barras horizontales.
* - [broken_barh](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.broken_barh.html)(xranges, yrange, ...)
  - Grafica una secuencia horizontal de rectángulos.
```

##### Notas de _plt.bar_

[bar](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar.html): Crea una gráfica de barras.
```python
# Sintaxis de llamada
plt.bar(x, height, width=0.8, bottom=None, *, align='center', data=None, **kwargs)
```
**Parámetros:**
- **x** - `float` o `array-like`: Coordenadas del eje _x_, pueden ser las categorías a grafícar o solo una etiqueta.
- **height** - `float` o `array-like`: Valores que tienen la altura de las barras. Tiene que ser de la misma longitud que _x_.
- **width** - `float` o `array-like`: Ancho de las barras.
- **bottom** - `float` o `array-like`: Coordenas de _y_, de las bases de las barras. Útil en caso de que quieres apilar varios valores.
- **align** - {'center', 'edge'}: Alineación de las etiquetas de las barras en la coordenada _x_.
- **\*\*kwargs**: Propiedades de {ref}`matplotlib-rectangle`.
    - `tick_label` - `str` o `list` de `str`: Para modificar las etiquetas de las barras. Debe ser igual a la longitud de _x_.
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
plt.bar(df.index, df['col1'])
plt.bar(df.index, df['col2'], bottom=df['col1'])

# Barras de dos cantidades independientes
# Usar str con nombre de la categoría
plt.bar("Cat 1", df["col"].agg_func())
plt.bar("Cat 2", df2["col"].agg_func())

# Barras con barras de error (ejm std)
plt.bar("Cat 1", df["col"].agg_func(), yerr=df["col"].std())
plt.bar("Cat 2", df2["col"].agg_func(), yerr=df2["col"].std())
```

**Ejemplo:**

En este ejemplo se grafican barras apiladas, para el número de pasajeros en 1950 y 1960.

```{code-cell} ipython3

# Crear gráfica
plt.bar(flights_1950['month'], 
        flights_1950['passengers'], 
        color=azul, 
        label='1950')

# Crear gráfica apilada
plt.bar(flights_1950['month'], 
        flights_1960['passengers'], 
        bottom=flights_1950['passengers'], 
        color=cafe, 
        label='1960')

# Añadir leyenda
plt.legend()

# Imprimir gráfica
plt.show()
```

<br/>

(pyplot-funciones-areas-rectas)=
#### Rectas y áreas

Gráficas para generar áreas y líneas horizontales y verticales.

:::{warning}
Considerar lo siguiente:
- Las rectas aquí presentadas son múltiples rectas en un intervalo. Para graficar una única recta revisar funciones en {ref}`pyplot-funciones-spans`.
- Las áreas aquí presentadas son para rellenar áreas entre curvas o gráficas de áreas. Para generar _spans_ (rectángulos para resaltar zonas en gráficas) ver funciones en {ref}`pyplot-funciones-spans`.
:::

:::{note}
Los valores usados en estos métodos deben de coincidir con los valores del índice o de la columna que se use en el eje correspondiente. Por ejemplo, si uno de los ejes es de tipo fecha se debe de usar un valor que represente una fecha, por ejemplo `'2020-06-21'`.
:::

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [fill](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.fill.html)(*args, data=None, **kwargs)
  - Grafica polígonos rellenos.
* - [fill_between](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.fill_between.html)(x, y1, y2=0, where=None, interpolate=False, step=None, ...)
  - Rellena el área entre dos curvas horizontales ($y=f(x)$).
* - [fill_betweenx](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.fill_betweenx.html)(y, x1, x2=0, where=None, step=None, interpolate=False, ...)
  - Rellena el área entre dos curvas verticales ($x=g(y)$).
* - [hlines](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hlines.html)(y, xmin, xmax, colors=None, linestyles='solid', label='', ...)
  - Grafica líneas horizontales en cada _y_ desde _xmin_ hasta _xmax_.
* - [stackplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.stackplot.html)(x, *args, labels=(), colors=None, baseline='zero', data=None, **kwargs)
  - Crea una gráfica de áreas apiladas.
* - [vlines](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.vlines.html)(x, ymin, ymax, colors=None, linestyles='solid', label='', ...)
  - Grafica líneas verticales en cada _x_ desde _ymin_ hasta _ymax_.
```

<br/>

#### Circulares

Funciones para crear gráficas circulares.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [pie](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.pie.html)(x, , ...)
  - Grafica un gráfico circular.
* - [polar](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.polar.html)(*args, **kwargs)
  - Crea una gráfica polar.
```

<br/>

### Bins

Gráficas para datos en _bins_ como histogramas. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [hexbin](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hexbin.html)(x, y, ...)
  - Crea un gráfico de agrupación hexagonal 2D de los puntos _x_, _y_.
* - [hist](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html)(x, bins=None, range=None, density=False, weights=None, cumulative=False, ...)
  - Calcula y grafica un histograma.
* - [hist2d](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist2d.html)(x, y, bins=10, range=None, density=False, ...)
  - Crea un gráfico de histograma 2D.
* - [stairs](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.stairs.html)(values, edges=None, ...)
  - Grafica de escalera como una línea con bordes delimitadores o un gráfico relleno.
```

<br/>

#### Notas de _hist_

[hist](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html): Realiza un histograma.
```python
# Sintaxis de llamada
plt.hist(x, bins=None, *, range=None, density=False, weights=None, cumulative=False, 
         bottom=None, histtype='bar', align='mid', orientation='vertical', rwidth=None, 
         log=False, color=None, label=None, stacked=False, data=None, **kwargs)
```
**Parámetros:**
- **x** - `array-like` o `secuencia` de `array-like`: Datos de entrada. Si es una secuencia, los _arrays_ pueden ser de diferentes tamaños.
- **bins** - `int`, `secuencia` o `str`: Definir los _bins_ del histograma.
    - `int`: Número de _bins_ en el rango.
    - `secuencia`: Define los limites de cada _bin_. Es inclusivo.
    - `str`: El nombre de una estrategia para hacer los _bins_, las posibles opciones son 'auto', 'fd', 'doane', 'scott', 'stone', 'rice', 'sturges', o 'sqrt'.
- **range** - `tuple` o `None`: Rango de los bins. Ignorado si _bins_ es `sequence`. Por default es `(x.min(), x.max())`.
- **density** - `bool`: Para indicar que retorne la densidad de probabilidad (eje _y_ entre 0 y 1).
- **cumulative** - `bool`: Para indicar si realizar el histograma cumulativo. Si es -1 entonces la acumulación es al revés (empieza acumulado y se van restando los nuevos valores).
- **histtype** - {'bar', 'barstacked', 'step', 'stepfilled'}: Tipo de histograma.
- **align** - {'left', 'mid', 'right'}: Alineación de las barras.
- **orientation** - {'vertical', 'horizontal'}: Orientación de las barras.
- **stacked** - `bool`: Para indicar, en caso de múltiples datos, que las barras se apilen.
- **\*\*kwargs**: Propiedades de {ref}`matplotlib-patch`.

**Retorna:**
- **n** -`array` o `list` de `array`: Valores de los _bins_ (alturas de las barras).
- **bins** -`array`: Extremos de los bins.
- **patches** - `BarContainer`, `list` de `Polygon` o `list` de esos objetos: Contenedor de los artistas individuales usados para crear el histograma.


**Ejemplo:**
En este ejemplo se gráfica el histograma de la columna _total_bill_ del dataset _tips_.

```{code-cell} ipython3
# Importar el dataset
tips=sns.load_dataset("tips")

# Crear la figura
plt.figure(figsize=(14, 6))

# Graficar el histograma
plt.hist(tips['total_bill'], bins=20, color=azul, edgecolor='black', alpha=0.7)
plt.title('Histogram of Total Bill', fontsize=14)
plt.xlabel('Total Bill ($)', fontsize=12)
plt.ylabel('Frequency', fontsize=12)

# Imprimir la figura
plt.show()
```

<br/>

### Campos Vectoriales

Funciones para graficar campos vectoriales. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [barbs](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.barbs.html)(*args, data=None, **kwargs)
  - Grafica un campo 2D de púas.
* - [quiver](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.quiver.html)(*args, data=None, **kwargs)
  - Grafica un campo 2D de flechas.
* - [quiverkey](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.quiverkey.html)(Q, X, Y, U, label, **kwargs)
  - Agrega una clave a una gráfica _quiver_.
* - [streamplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.streamplot.html)(x, y, u, v, density=1, linewidth=None, color=None, cmap=None, ...)
  - Grafica líneas de corriente de un flujo vectorial.
```

<br/>

### Contornos

Funciones para gráficar de contornos. Útiles para representaciones 2D de de gráficas 3D.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [clabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.clabel.html)(CS, levels=None, **kwargs)
  - Etiqueta un una gráfica de contorno.
* - [contour](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.contour.html)(*args, data=None, **kwargs)
  - Grafica líneas de contorno.
* - [contourf](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.contourf.html)(*args, data=None, **kwargs)
  - Grafica contornos rellenos.
```

<br/>

### Espectral

Funciones útiles para diagramas espectrales, utilizados para analizar frecuencias y estructuras cíclicas.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [acorr](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.acorr.html)(x, ...)
  - Grafica la autocorrelación de _x_.
* - [angle_spectrum](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.angle_spectrum.html)(x, ...)
  - Grafica el espectro de ángulos.
* - [cohere](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.cohere.html)(x, y, ...)
  - Grafica la coherencia entre _x_ y _y_.
* - [csd](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.csd.html)(x, y, ...)
  - Grafica la densidad espectral cruzada.
* - [magnitude_spectrum](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.magnitude_spectrum.html)(x, ...)
  - Grafica el espectro de magnitudes.
* - [phase_spectrum](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.phase_spectrum.html)(x, ...)
  - Grafica el espectro de fases.
* - [psd](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.psd.html)(x, ...)
  - Grafica la densidad espectral de potencia.
* - [specgram](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.specgram.html)(x, ...)
  - Grafica un espectrograma.
* - [xcorr](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xcorr.html)(x, y, ...)
  - Grafica la correlación cruzada entre _x_ y _y_.
```

<br/>

### Estadísticas

Funciones útiles para gráficar visualizaciones estadísticas como _boxplots_, funciones acumuladas de probabilidad, entre otros. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [boxplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.boxplot.html)(x, ...)
  - Genera una gráfica de caja y bigotes. Retorna un diccionario que contiene las siguientes _keys_: _boxes_, _medians_, _whiskers_, _caps_, _fliers_, _means_.
* - [ecdf](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ecdf.html)(x, weights=None, ...)
  - Calcula y grafica la función de distribución acumulada de _x_.
* - [violinplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.violinplot.html)(dataset, ...)
  - Genera una gráfica de violín.
```

#### Notas de _plt.boxplot_

[boxplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.boxplot.html): Crea un boxplot por cada columna que se le pase.
```python
# Sintaxis de llamada
plt.boxplot(x, *, notch=None, sym=None, vert=None, orientation='vertical', whis=None, 
            positions=None, widths=None, patch_artist=None, bootstrap=None, 
            usermedians=None, conf_intervals=None, meanline=None, showmeans=None, 
            showcaps=None, showbox=None, showfliers=None, boxprops=None, tick_labels=None, 
            flierprops=None, medianprops=None, meanprops=None, capprops=None, 
            whiskerprops=None, manage_ticks=True, autorange=False, zorder=None, 
            capwidths=None, label=None, data=None)
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
_ = plt.boxplot(df['col'], patch_artist=True)
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
plt.figure(figsize=(8, 6))

# Graficar el histograma
_ = plt.boxplot(tips['total_bill'], patch_artist=True)

# Cambiar colores
for box in _['boxes']:
    box.set(facecolor=azul, edgecolor='black', linewidth=1)
for median in _['medians']:
    median.set(color=cafe, linewidth=2)

# Añadir título
plt.title('Boxplot of Total Bill', fontsize=14)

# Imprimir la figura
plt.show()
```

<br/>

### Arreglos 2D

Funciones para generar visualizaciones a partir de datos contenidos en arreglos. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [figimage](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figimage.html)(X, ...)
  - Agrega una imagen no remuestreada a la figura.
* - [imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html)(X, cmap=None, norm=None, ...)
  - Muestra un array como una imagen.
* - [matshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.matshow.html)(A, fignum=None, **kwargs)
  - Muestra un arreglo como matriz en una nueva figura.
* - [pcolor](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.pcolor.html)(*args, ...)
  - Crea una gráfica de pseudocolor con una cuadrícula rectangular no regular.
* - [pcolormesh](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.pcolormesh.html)(*args, ...)
  - Crea una gráfica de pseudocolor con una cuadrícula rectangular no regular.
* - [spy](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.spy.html)(Z, ...)
  - Traza el patrón de un arreglo 2D _sparse_.
```

<br/>

(pyplot-funciones-spans)=
### Rectas y Áreas

Funciones para añadir rectas y áreas a gráficas.

:::{caution}
Para añadir _n_ rectas en un intervalo o agregar áreas entre curvas o áreas con formas más complejas (polígonos) revisar funciones de {ref}`pyplot-funciones-areas-rectas`.
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
* - [axhline](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axhline.html)(y=0, xmin=0, xmax=1, **kwargs)
  - Añade una línea horizontal a la gráfica.
* - [axhspan](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axhspan.html)(ymin, ymax, xmin=0, xmax=1, **kwargs)
  - Agrega un área (rectángulo horizontal) a la gráfica.
* - [axline](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axline.html)(xy1, xy2=None, ...)
  - Agrega una línea recta infinitamente larga.
* - [axvline](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axvline.html)(x=0, ymin=0, ymax=1, **kwargs)
  - Añade una línea vertical a la gráfica.
* - [axvspan](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axvspan.html)(xmin, xmax, ymin=0, ymax=1, **kwargs)
  - Agrega un tramo vertical (rectángulo) a la gráfica.
```

**Ejemplo**
En el siguiente ejemplo se añade una recta horizontal en y un área entre 1953 y 1954:

```{code-cell} ipython3
plt.figure() 

# Graficar los datos
plt.plot(yearly_data['year'], 
         yearly_data['passengers'], 
         marker='o', 
         color=azul)

# Añadir recta horizontal
plt.axhline(4500, color=cafe)

# Añadir área vertical
plt.axvspan(1953, 1954, color=cafe_claro, alpha=.3)

# Imprimir la figura
plt.show()
```

<br/>

### Texto y Anotaciones

Funciones útiles para añadir texto y otras anotaciones a las gráficas o a las figuras. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [annotate](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.annotate.html)(text, xy, ...)
  - Agrega un texto a una gráfica para resaltar algún punto. Es posible agregar una flecha que apunte hacia un punto en particular y se agrege un texto.
* - [arrow](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.arrow.html)(x, y, dx, dy, **kwargs)
  - Añade una flecha al `Axes`.
* - [figlegend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figlegend.html)(*args, **kwargs)
  - Coloca una leyenda en la **figura**.
* - [figtext](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figtext.html)(x, y, s, fontdict=None, **kwargs)
  - Añade texto a la **figura**.
* - [legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html)(*args, **kwargs)
  - Coloca una leyenda en el `Axes`.
* - [table](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.table.html)(cellText=None, ...)
  - Agrega una tabla a un `Axes`.
* - [text](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.text.html)(x, y, s, fontdict=None, **kwargs)
  - Agrega un texto al `Axes`.
```

<br/>

#### Notas de _annote_

[annotate](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.annotate.html): Agrega un texto a una gráfica para resaltar algún punto de la gráfica bajo una condición. Es posible agregar una flecha que apunte hacia un punto en particular y se agrege un texto.
```python
# Sintaxis de llamada
plt.annotate(text, xy, *args, xycoords='data', **kwargs)
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

En este ejemplo se añade el número de pasajeros exactos en el año 1954.

```{code-cell} ipython3
# Crear figura
plt.figure()

# Graficar los datos
plt.plot(yearly_data['year'], 
         yearly_data['passengers'], 
         label='Passengers', 
         marker='o', 
         color=azul)

# Añadir etiquetas y título
plt.xlabel('Año')
plt.ylabel('Total de pasajeros')
plt.title('Tendencia de total de pasajeros')

# Añadir texto en el punto 1954
plt.annotate("2,867", 
             xy=[1954, 2867], 
             xytext=[1954, 2000], 
             arrowprops={"arrowstyle":"->", "color":"gray"})

# Show the plot
plt.show()
```

<br/>

#### Notas de _text_

[text](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.text.html): Agrega texto a un `Axes` en las coordenadas de _x_ y _y_.
```python
# Sintaxis de llamada
plt.text(x, y, s, fontdict=None, **kwargs)
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
# Crear figura
plt.figure()

# Graficar los datos
plt.plot(yearly_data['year'], 
         yearly_data['passengers'], 
         marker='o', 
         color=azul)

# Añadir etiquetas y título
plt.xlabel('Año')
plt.ylabel('Total de pasajeros')
plt.title('Tendencia de total de pasajeros')

# Añadir texto en el punto 1954
plt.text(1954, 2650, "2867")

# Show the plot
plt.show()
```

<br/>

### Triangulos no Estructurados

Funciones para crear gráficas de mallas no estructuradas. Este tipo de mallas se compoenen de puntos espaciados de manera irregular conectados por elementos triangulares, una aplicación común es visualización de datos geoespaciales.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [tricontour](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tricontour.html)(*args, **kwargs)
  - Grafica líneas de contorno en una cuadrícula triangular no estructurada.
* - [tricontourf](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tricontourf.html)(*args, **kwargs)
  - Grafica regiones de contorno en una cuadrícula triangular no estructurada.
* - [tripcolor](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tripcolor.html)(*args, ...)
  - Crea una gráfica de pseudocolor de una cuadrícula triangular no estructurada.
* - [triplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.triplot.html)(*args, **kwargs)
  - Grafica una cuadrícula triangular no estructurada como líneas y/o marcadores.
```

<br/>

---
(pyplot-personalizacion)=
## Funciones de Personalización

Funciones para personalización de las gráficas. Las funciones aquí presentadas funcionan principalmente para los `Axes`. 

### Títulos y etiquetas

Funciones para establecer los títulos y etiquetas de figuras, _axes_ y ejes.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [suptitle](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.suptitle.html)(t, **kwargs)
  - Añade un subtítulo centrado a la **figura**. Es útil en figuras que tienen más de un gráfica.
* - [title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html)(label, fontdict=None, loc=None, pad=None, ...)
  - Establece un título para el `Axes`.
* - [xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html)(xlabel, fontdict=None, labelpad=None, ...)
  - Establece la etiqueta para el eje _x_.
* - [ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html)(ylabel, fontdict=None, labelpad=None, ...)
  - Establece la etiqueta para el eje _y_.
```

Patrones útiles:
```python
# Establecer título de la figura
plt.suptitle('Title')

# Establecer etiqueta del eje x
plt.xlabel('x label')

# Establecer etiqueta del eje y
plt.ylabel('y label')

# Establecer título
plt.title('title')
```

<br/>

### Leyenda

Funciones para añadir leyendas a las gráficas.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [figlegend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figlegend.html)(*args, **kwargs)
  - Coloca una leyenda en la **figura**.
* - [legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html)(*args, **kwargs)
  - Coloca una leyenda en el `Axes`. Si no se pone ningún argumento, se infieren los argumentos, el nombre que se mostrará en la leyenda será el que se le puso a cada gráfica con el parámetro _label_. Si una gráfica no tiene _label_ no se mostrará en la leyenda.
```

<br/>

#### Notas de _legend_

[legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html): Añade una leyenda a un `Axes`. Si no se pone ningún argumento, se infieren los argumentos, por las gráficas presenten en el `Axes`, el nombre que se mostrará en la leyenda será al que se le puso a cada gráfica con el argumento label. Si una gráfica no tiene label no se mostrará en la leyenda.
```python
# Sinxis de llamada
plt.legend(labels=None, loc='best', ncol=1, labelcolor=None, fontsize=None, 
           facecolor='white', edgecolor 'black', title=None, title_fontsize=None)
```

**Parámetros:**
- **labels** - `list` de `str`: Nombres a mostrar en la leyenda, debe ser de la misma longitud que el número de gráficas y en el mismo orden que `Axes`.
- **loc** - `str`, `int` o `2-tuple` de `float`: Posición de la leyenda en la gráfica. Si es `str` o `int` ver más abajo la tabla de posibles valores. Si es `tuple` es la posición en el eje _x_ y _y_, es un valor entre 0 y 1.
- **ncol** - `int`: Número de columnas en la leyenda.
- **labelcolor** - `str` o `list` de `str`: Color de las etiquetas en la leyenda.
- **fontsize** - {'xx-small', 'x-small', 'small', 'medium', 'large', 'x-large', 'xx-large'}: Tamaño de la fuente de la leyenda.
- **facecolor** 'inherit' o - `color`: Color del fondo de la leyenda.
- **edgecolor** 'inherit' o - `color`: Color del borde de la leyenda.
- **title** - `str` o `None`: Título de la leyenda.
- **title_fontsize** - {'xx-small', 'x-small', 'small', 'medium', 'large', 'x-large', 'xx-large'}: Tamaño del título de la leyenda.

**Retorna:**
- `Legend`.

Posibles valores del parámetro _loc_, como cadena o como entero:

| loc \<str/> | loc \<int> |
| --- | --- |
| `'best'` | 0 |
| `'upper right'` | 1 |
| `'upper left'` | 2 |
| `'lower left'` | 3 |
| `'lower right'` | 4 |
| `'right'` | 5 |
| `'center left'` | 6 |
| `'center right'` | 7 |
| `'lower center'` | 8 |
| `'upper center'` | 9 |
| `'center'` | 10 |

<br/>

### Grids

Funciones para establecer o configurar el _grid_ (líneas de cruadrículas) en las gráficas.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [grid](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.grid.html)(visible=None, which='major', axis='both', **kwargs)
  - Configuración de las líneas de la cuadrícula.
* - [rgrids](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.rgrids.html)(radii=None, labels=None, angle=None, fmt=None, **kwargs)
  - Recupera o establece las líneas de cuadrícula radiales en el gráfico polar actual.
* - [thetagrids](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.thetagrids.html)(angles=None, labels=None, fmt=None, **kwargs)
  - Recupera o establece las líneas de cuadrícula _theta_ en la gráfica polar actual.
```

<br/>

### Ejes

En esta sección se enlistan las funciones relacionadas con los ejes de los objetos `Axes`.

#### Funciones generales

Funciones para manipular los ejes en general.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [axis](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axis.html)(arg=None, /, ...)
  - Método de conveniencia _get_ o _set_ de algunas propiedades del eje.
* - [box](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.box.html)(on=None)
  - Activa o desactiva el cuadro de ejes en los ejes actuales.
```

#### Escala

Funciones para establecer la escala de los ejes.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [autoscale](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.autoscale.html)(enable=True, axis='both', tight=None)
  - Escala automáticamente la vista del eje a los datos.
* - [xscale](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xscale.html)(value, **kwargs)
  - Establece la escala del eje _x_.
* - [yscale](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.yscale.html)(value, **kwargs)
  - Establece la escala del eje _y_.
```

<br/>

**Ejemplo**

En este ejemplo se ajustan las escalas en ambos ejes a una escalar logarítmica para que los datos se puedan visualizar de mejor manera.

```{code-cell} ipython3
# Importar dataset
planets=sns.load_dataset("planets")

# Crear gráfica
plt.figure(figsize=(8, 6))
plt.scatter(planets['orbital_period'], planets['distance'], color=azul, alpha=0.3)

# Ajustar escalar en ambos ejes
plt.xscale('log')
plt.yscale('log')

# Imprimir la figura
plt.show()
```

<br/>

#### Límites

Funciones para establecer los límites de los ejes, es decir, el rango de valores en los ejes.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlim.html)(*args, **kwargs)
  - Recupera o establece los límites _x_ de los ejes actuales.
* - [ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylim.html)(*args, **kwargs)
  - Recupera o establece los límites _y_ de los ejes actuales.
```

:::{tip}
Otras formas de establecer los límites: <br/> `plt.axis([xmin, xmax, ymin, ymax], *args)` <br/> `gca().set(xlim=(xmin, xmax), ylim=(ymin, ymax))`
:::

<br/>

#### Ticks

Funciones para configurar los _ticks_ en los ejes. Los _ticks_ son los valores en los ejes, ya sean numéricos o categóricos. Se puede configurar sus ubicaciones, sus valores, la cantidad, etc.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [locator_params](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.locator_params.html)(axis='both', tight=None, **kwargs)
  - Controla el comportamiento de los localizadores de _major ticks_.
* - [minorticks_off](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.minorticks_off.html)()
  - Remueve los _minor ticks_ del `Axes`.
* - [minorticks_on](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.minorticks_on.html)()
  - Muestra los _minor ticks_ del `Axes`.
* - [tick_params](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tick_params.html)(axis='both', **kwargs)
  - Modifica la apariencia de los _ticks_, sus etiquetas y las líneas de cuadrícula.
* - [ticklabel_format](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ticklabel_format.html)(axis='both', style='', ...)
  - Configura el `ScalarFormatter` utilizado por defecto para `Axes` lineales.
* - [xticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xticks.html)(ticks=None, labels=None, ...)
  - Recupera o establece las ubicaciones y las etiquetas de los _ticks_ del eje _x_.
* - [yticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.yticks.html)(ticks=None, labels=None, ...)
  - Recupera o establece las ubicaciones y las etiquetas de los _ticks_ del eje _y_.
```

<br/>

**Ejemplo**:

En este ejemplo se modifican los _ticks_ del eje _y_. Por default, en esa gráfica, se muestran los _ticks_ del 2,000 al 5,000, con un paso de 1,000. Con esta nueva configuración se muestran desde 1,000 hasta 6,000 con un paso de 500.

```{code-cell} ipython3
# Crear figura
plt.figure()

# Graficar los datos
plt.plot(yearly_data['year'], 
         yearly_data['passengers'], 
         marker='o', 
         color=azul)

# Añadir etiquetas y título
plt.xlabel('Año')
plt.ylabel('Total de pasajeros')
plt.title('Tendencia de total de pasajeros')

plt.yticks(list(range(1000, 6500, 500)))

# Show the plot
plt.show()
```

<br/>

---
### Layout

Funciones para configurar el _layout_ de las gráficas. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [margins](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.margins.html)(*margins, x=None, y=None, tight=True)
  - Establece o retorna los márgenes de escala automática.
* - [subplot_tool](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot_tool.html)(targetfig=None)
  - Inicializa una ventana de herramientas de _subplot_ para una figura.
* - [subplots_adjust](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots_adjust.html)(left=None, bottom=None, right=None, top=None, wspace=None, hspace=None)
  - Ajusta los parámetros del _layout_ para _subplots_.
* - [tight_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html)(*, pad=1.08, h_pad=None, w_pad=None, rect=None)
  - Ajusta el espacio entre y alrededor de los _subplots_.
```

<br/>

---
### Colormapping

Funciones para recuperar o establecer propiedades relacionadas con el mapeo de colores de los datos en la gráfica.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [clim](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.clim.html)(vmin=None, vmax=None)
  - Establece los límites de color de la imagen actual.
* - [colorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.colorbar.html)(mappable=None, cax=None, ax=None, **kwargs)
  - Agrega una barra de colores a un gráfico.
* - [gci](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.gci.html)()
  - Recupera el _colorable artist_ actual.
* - [get_cmap](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.get_cmap.html)(name=None, lut=None)
  - Recupera una instancia de `colormap`, con valores predeterminados de _rc_ si el _name_ es `None`.
* - [imread](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imread.html)(fname, format=None)
  - Lee una imagen de un archivo como un arreglo.
* - [imsave](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imsave.html)(fname, arr, **kwargs)
  - Asigna colores y guarda un arreglo como una imagen localmente.
* - [sci](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.sci.html)(im)
  - Establece la imagen actual.
* - [set_cmap](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.set_cmap.html)(cmap)
  - Establece el _colormap_ predeterminado y lo aplica a la imagen actual.
```

<br/>

---
## Otros

Otras funciones. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [connect](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.connect.html)(s, func)
  - Vincula la función _func_ a el evento _s_.
* - [disconnect](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.disconnect.html)(cid)
  - Desconecta el _callback_ con id _cid_.
* - [findobj](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.findobj.html)(o=None, match=None, include_self=True)
  - Encuentra objetos _artist_.
* - [get](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.get.html)(obj, *args, **kwargs)
  - Retorna el valor de una propiedad de un `Artist` o imprime todas las propiedades.
* - [get_current_fig_manager](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.get_current_fig_manager.html)()
  - Retorna el administrador de figuras de la figura actual.
* - [getp](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.getp.html)(obj, *args, **kwargs)
  - Retorna el valor de una propiedad de un `Artist` o imprime todas las propiedades.
* - [ginput](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ginput.html)(n=1, timeout=30, show_clicks=True, mouse_add=MouseButton.LEFT, mouse_pop=MouseButton.RIGHT, mouse_stop=MouseButton.MIDDLE)
  - Llamada de "bloqueo" para interactuar con una figura.
* - [new_figure_manager](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.new_figure_manager.html)(num, *args, **kwargs)
  - Crea una nueva instancia de administrador de figuras.
* - [set_loglevel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.set_loglevel.html)(*args, **kwargs)
  - Configure los niveles de _logging_ de Matplotlib.
* - [setp](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.setp.html)(obj, *args, **kwargs)
  - Establece una o más propiedades en un `Artist` , o `list` valores permitidos.
* - [waitforbuttonpress](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.waitforbuttonpress.html)(timeout=-1)
  - Llamada de "bloqueo" para interactuar con la figura.
* - [xkcd](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xkcd.html)(scale=1, length=100, randomness=2)
  - Activa el modo de dibujo _sketch-style xkcd_.
```

<br/>

---
## Producción

Funciones para configurar la visualización de las gráficas.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [draw](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.draw.html)()
  - Vuelve a dibujar la figura actual.
* - [draw_if_interactive](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.draw_if_interactive.html)()
  - Vuelve a dibujar la figura actual si está en modo interactivo.
* - [install_repl_displayhook](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.install_repl_displayhook.html)()
  - Se conecta al _hook_ de visualización del shell actual.
* - [ioff](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ioff.html)()
  - Desactiva el modo interactivo.
* - [ion](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ion.html)()
  - Habilita el modo interactivo.
* - [isinteractive](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.isinteractive.html)()
  - Indica si los gráficos se actualizan después de cada comando de graficado. 
* - [pause](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.pause.html)(interval)
  - Ejecuta el cíclo de eventos de la GUI durante por intervalos de segundos.
* - [savefig](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html)(*args, **kwargs)
  - Almacena la figura actual localmente.
* - [show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html)(*, block=None)
  - Imprime todas las figuras abiertas.
* - [switch_backend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.switch_backend.html)(newbackend)
  - Establece el _backend_ de pyplot.
* - [uninstall_repl_displayhook](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.uninstall_repl_displayhook.html)()
  - Se deconecta del _hook_ de visualización del _shell_ actual.
```

