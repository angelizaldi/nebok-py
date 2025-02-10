# Anexos

En esta sección se presentan algunos temas para la personalización de las gráficas como podría ser modifcar las líneas, marcadores, colores, barras de colores, estilos, etc. en las visualizaciones.

<br/>

---
## Estilos

Para cambiar el estilo de una gráfica, como la gama de colores, las fuentes, entre otros elementos se puede usar la función `use()` del módulo `style`.
```python
# Modificar estilo de las gráficas
plt.style.use(style_name = 'default')

# Definir estilo de manera temporal
with plt.style.context('stylename'):
    # Definición de la gráfica

# Definir estilo de seaborn
import seaborn as sns
sns.set()
```
- _style\_name_ - `str`: Es el nombre del estilo. Algunos estilos disponibles son:
    - _classic_: Estilo clásico de `matplotlib`.
    - _ggplot_: Simula las gráficas creadas en _ggplot_ con _R_.
    - _default_: Es el default con lo que `matplotlib` grafica.
    - _seaborn-colorblind_: Usa colores amigables con personas daltónicas.
    - _grayscale_: Gráfica en escala de grises.
- Para enlistar todos los estilos disponibles usar: <br> `plt.style.available`
- Para utilizar el estilo de `seaborn` usar `sns.set()`, utilizar antes de definir cualquier gráfica.
- Para ver todos los estilos disponibles y visualizar cómo se ven, visitar la [documentación](https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html).
- Para cambiar el estilo de manera temporal en una gráfica en específico y no afectar toda la sesión utilizar la función `plt.style.context` y un administrador de contextos.

<br/>

---
(matplotlib-markers)=
## Markers

Para establecer el parámetro _marker_ se utiliza una cadena para indicar el tipo de marcados. Los más comunes son:
```{image} ../images/markers_table.png
:name: markers-table
:width: 400px
:align: center
```

:::{note}
Para una lista completa vistar la [documentación](https://matplotlib.org/stable/api/markers_api.html#module-matplotlib.markers).
:::

<br/>

---
(matplotlib-lines)=
## Lines

El argumento _linestyle_ se puede de las siguientes maneras:

| Cadena | Nombre | Descripción |
| --- | --- | --- |
| `'-'` | 'solid' | Línea sólida |
| `'--'` | 'dashed' | Línea intermitente |
| `'-.'` | 'dashdot' | Línea de guiones y puntos |
| `':'` | 'dotted' | Línea de puntos |

Personalizables:

Se puede utilizar estilos personalizados con un `tuple` :
```python
# Linestyles personalizados
(offset, (on_off_seq))
```
- _offset_: Indica la posición relativa en relación con los datos en _x_ desde donde se debe de mostrar la línea. Este valor está en las mismas unidades que _x_, tal cual es el valor de _x_ donde debe iniciar la línea.
- _on\_off\_seq_: Es para indicar el patrón de la línea, se define por pares. El primer elemento es cuántos puntos consecutivos (sin espacios) tendrá el patrón, el segundo elemento es cuántos puntos vacíos dejar entre cada patrón de puntos (el definido en el primer elemento Ejemplos: <br> `(0, (1,1)) -> _ _ _ _ _ _ _ _` <br> `(0, (2,1)) -> __ __ __ __ __ __` <br/> Se puede poner más de un par, para un patrón más complejo: <br> `(0, (3, 3, 1, 3)) -> ___   _   ___   _   ___`
- **IMPORTANTE**: Los ejemplos de aquí son ilustrativos, se hicieron usando guión bajo, pero en realidad son puntos.
- Para más información visitar [la documentación](https://matplotlib.org/stable/gallery/lines_bars_and_markers/linestyles.html).

<br/>

---
(matplotlib-color)=
## Colores

El argumento `color` se puede definir de las siguientes maneras:

- **Tuple RGB o RGBA** - `tuple` de 3 o 4 elementos entre _[0, 1]_: Representando colores RGB o RGBA (_alpha=1_ es opaco), por ejemplo: `(0.1, 0.2, 0.3)`.
- **Cadena hexadécimal** (RGB o RGBA) - `str`: Código que represente un número en formato hexadécimal. Ejemplo: `'#0f0f0f'`.
    - Las cadenas se pueden consultar en [esta página](https://htmlcolorcodes.com/es/) en la parte de _Hex_ o _#_):
- **Cadena de escala de grises** - `str` de un número  entre _[0, 1]_: Representa la escala de gris, donde 1 es negro y 0 es blanco. Ejemplo `'0.5'`.
- **Color xkcd** - `str` con prefijo 'xkcd:' Son colores con nombres. Ejemplo `'xkcd:sky blue'`.
    - Las cadenas se pueden consultar en [esta página](https://xkcd.com/color/rgb/).
- **Colores con Nombre** -  `str`: Los nombres se pueden consultar en [esta página](https://htmlcolorcodes.com/es/).
- Colores X11 – str: Los colores se pueden consultar en [esta página](https://www.w3schools.com/colors/colors_x11.asp).
- **Carácter**:

| Caracter | Descripción |
| --- | --- |
| `'b'` | Azul |
| `'g'` | Verde |
| `'r'` | Rojo |
| `'c'` | Azul cielo |
| `'m'` | Morado |
| `'y'` | Amarillo |
| `'k'` | Negro |
| `'w'` | Blanco |

- **Paleta categórica 'T10'**:

| Caracter | Descripción |
| --- | --- |
| `'blue'` | Azul |
| `'green'` | Verde |
| `'red'` | Rojo |
| `'cyan'` | Azul cielo |
| `'purple'` | Morado |
| `'brown'` | Café |
| `'pink'` | Rosa |
| `'gray'` | Gris |
| `'orange'` | Naranja |
| `'olive'` | Olivo |

<br/>

---
(matplotlib-colormap)=
## ColorMap

Para poder aplicar un mapeo de color a una gráfica, ésta debe de tener el parámetro _cmap_ o _colormap_, simplemente se debe definir el parámetro con el nombre de una mapa de color válido. Además el argumento _color_ debe de tener un `array-like` de valores los cuales se mapearán a los valores de los datos por posición, para definir el color de cada dato.
Algunos colormaps válidos son:
- **Secuencia uniforme**.
    - 'viridis'
    - 'plasma'
    - 'inferno'
    - 'magma'
    - 'cividis'
- **Secuencial**:
    - 'Greys'
    - 'Purples'
    - 'Blues'
    - 'Oranges'
    - 'Reds'
    - 'Greens'
- **Divergentes** (divergen desde la mitad hacía dos colores distintos):
    - 'coolwarm'
    - 'seismic'
    - 'vanimo'
- **Cíclicos**:
    - 'twilight'
    - 'hsv'
- **Categóricos**:
    - 'Pastel1'
    - 'Paired'
    - 'Dark2'
    - 'Set1' 
- Existen una versión al revés de cada _colormap_, para ello solo agregar como sufijo _'r'_ al nombre, por ejemplo _'viridis_r'_.
- Para más estilos y visualización de las paletas visitar la [documentación](https://matplotlib.org/stable/gallery/color/colormap_reference.html).

![](https://matplotlib.org/stable/_images/sphx_glr_colormap_reference_001.png)

![](https://matplotlib.org/stable/_images/sphx_glr_colormap_reference_002.png)

![](https://matplotlib.org/stable/_images/sphx_glr_colormap_reference_003.png)

![](https://matplotlib.org/stable/_images/sphx_glr_colormap_reference_004.png)

![](https://matplotlib.org/stable/_images/sphx_glr_colormap_reference_005.png)

![](https://matplotlib.org/stable/_images/sphx_glr_colormap_reference_006.png)

![](https://matplotlib.org/stable/_images/sphx_glr_colormap_reference_007.png)

<br/>

### Color Map Personalizados

Es posible crear un _colormap_ personalizado con diccionarios. Es particularmente útil cuando se quiere establecer un color para cada valor de una variable categórica. Para ello en el diccionario usar como _keys_ cada uno de los valores de la variable categórica y como _values_ el color que tendrá ese valor, posteriormente al gráficar usar el argumento _c_ de la siguiente manera:
```python
# Definir diccionario
my_colormap = {'cat1': col1, 'cat2': col2, ...}

# Mapear colores a valores
plt.plot(df['x'], df['y'], c = df['var_cat'].map(my_colormap))
```
- 'var_cat' es el nombre de una variable categórica.
- _my\_colormap_ es el diccionario con los valores de la variable categórica como _keys_ y el color como _values_.
- Hacer esto es equivalente a usar el argumento _hue_ en `seaborn`.

<br/>

### Color Map Discretos

Por default los _colormap_ son continuos, para crear un _colormap_ discreto hacerlo de la siguiente manera:
```python

plt.scatter(I, cmap = plt.cm.get_cmap('cmap_name', N))
```
- _'cmap\_name'_: Es el nombre de un _colormap_ válido. 
- _N_ - `int`: Es el número de categorías discretas que se quieren poner en el _colormap_.

<br/>

---
(matplotlib-fmt)=
## Cadenas de Formato (fmt)

Una cadena de formato es una cadena para especificar el tipo de marker, tipo de linea y el color de los mismos en una gráfica. La sintaxis general es:
```python
# Cadena de formato
fmt = '[marker = 'o'][line='-'][color='b']'
```
- Cada una de las partes es opcional.
- Si se indica _line_, pero no _marker_, entonces, los datos serán líneas sin markers.
- Si se omite una parte entonces no se pondrá esa parte.
- Ejemplos de _fmt_: <br> `'b' # markers azules con forma por default ('o')` <br> `'or' # Círculos rojos` <br> `'-g' # Línea sólida verde` <br> `'--' # Línea intermitente con color por default (azul)` <br> `'^k:' # Markers de triángulos negros, conectados por una línea de puntos`

<br/>

### Marker

Los _markers_ admitidos en _fmt_ son:
| Caracter | Descripción |
| --- | --- |
| '.' | Punto |
| ',' | Pixel |
| 'o' | Círculo relleno |
| 'v' | Tríangulo invertido |
| '^' | Triángulo |
| '<' | Triángulo a la izquierda |
| '>' | Triángulo a la derecha |
| '1' | Tríangulo pequeño invertido |
| '2' | Triángulo pequeño |
| '3' | Triángulo pequeño a la izquierda |
| '4' | Triángulo pequeño a la derecha |
| '8' | Octágono |
| 's' | Cuadrado |
| 'p' | Pentágono |
| 'P' | Cruz rellena (+) |
| '*' | Estrella |
| 'h' | Hexágono |
| 'H' | Hexágono |
| '+' | plus marker |
| 'x' | Equis (X) |
| 'X' | Equis rellena |
| 'D' | Diamante relleno |
| 'd' | Diamante |
| '|' | Línea vertical |
| '_' | Línea horizontal |

- Para más información visitar la [documentación](https://matplotlib.org/stable/api/markers_api.html#module-matplotlib.markers).

<br/>

### Line

Los tipos de líneas admitidos en _fmt_ son:

| Caracter | Descripción |
| --- | --- |
| '-' | Línea sólida |
| '--' | Línea intermitente |
| '-.' | Línea de guiones y puntos |
| ':' | Línea de puntos |
- Para más información visitar [la documentación](https://matplotlib.org/stable/gallery/lines_bars_and_markers/linestyles.html).

<br/>

### Color

Los colores admitidos en _fmt_ son:

| Caracter | Descripción |
| --- | --- |
| 'b' | Azul |
| 'g' | Verde |
| 'r' | Rojo |
| 'c' | Azul cielo |
| 'm' | Morado |
| 'y' | Amarillo |
| 'k' | Negro |
| 'w' | Blanco |
