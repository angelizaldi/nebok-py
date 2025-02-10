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

# Seaborn

```{code-cell} ipython3
:tags: ["remove-input"]

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

azul="#30adb9"
cafe="#ba6a30"
cafe_claro="#cf9975"
```

Es una librería que se utiliza para realizar gráficas. Está construida sobre `matplotlib` por lo que muchas funciones de esa librería también funcionan con `seaborn`, incluso muchas funciones retornan objetos de la clase `matplotlib.Axes`. Es necesario importar la librería.

```python
# importar librería
import seaborn as sns
```
-	_sns_ es el nombre por convención.

```{attention}
Tener en cuenta lo siguiente al trabajar con la librería `seaborn`
- También es necesario que se importe  `matplotlib.pyplot`. <br> `import matplotlib.pyplot as plt`
- Para mostar las gráficas se tiene que usar `plt.tshow()`. Aunque esto no es necesario cuando se trabaja en {doc}`../08-otros/IPython`.
```

## Interfaces

En `seaborn` existen dos interfaces principales para creas gráficas:
- **Funciones de alto nivel**: Se utilizan funciones de `seaborn` para crear las gráficas, se recomienda esta interfaz si se quiere crear gráficas de manera rápida con menos opciones de personalización. Se divide a su vez en:
    - Funciones a nivel de figura: Las funciones a nivel de _figura_ gestionan un figura completa y permite crear gráficos con _subplots_, llaman a una función a nivel de eje a través del argumento _kind_ y retornan un objeto `FacetGrid`.
    - Funciones a nivel de eje: Las funciones a nivel de _ejes_ operan sobre un único eje, son más personalizables y retornan un objeto `matplotlib.Axes`, por lo que a estos objetos se les pueden aplicar todos los métodos de la clase {doc}`../05-matplotlib/axes`.
- **Interfaz de objetos**: Introducida en la versión 0.12, agrupa un colección de clases para transformar y graficar datos. Permite personalizar las graficas sin necesidad de utilizar `matplotlib`, aunque sigue siendo posible en caso de que se requiera. Se recomienda esta interfaz si se quiere un mayor control en la personalización de las gráficas.

Resumen de las interfaces de `seaborn`:

|Tipo de Función|Características|Cuándo usarla|
|---|---|---|
|A nivel de ejes|Simples, rápidas, fáciles de usar.|Análisis exploratorio rápido o gráficos sencillos.|
|A nivel de figura|Permiten manejar múltiples subplots y facetas.|Comparaciones entre grupos o análisis complejos en varias dimensiones.|
|Interfaz por objetos|Máxima personalización y flexibilidad.|Cuando se necesitan gráficos complejos, capas personalizadas o integración con `matplotlib`.|

:::{tip}
Una alternativa a crear gráficas con _subplots_ es usando la interfaz orienta a objetos de `matplotlib` y usar los parámetros _ax_ de las funciones a nivel de ejes de `seaborn`:

<code> 
fig, axes = plt.subplots(1, 2)

sns.axes_function(df['col']m ax=axes[0])
sns.axes_function(df['col2']m ax=axes[1])
</code>>
:::

Para los ejemplos de esta sección se utilizará el _dataset_ "flights" de la librería, además se agrupan los datos por año para las visualizaciones de un solo _axes_. Para las figuras con más de un _axes_ se crea un _dataset_ que contiene solo los datos de los años 1950 y 1960.

```{code-cell} ipython3
# Cargar el dataset
flights = sns.load_dataset("flights")

# Agrupar datos por año
yearly_data = flights.groupby('year')['passengers'].sum().reset_index()

# Filtrar datos para 1950 y 1960
sub_flights = flights[(flights['year'] == 1950) | (flights['year'] == 1960)]
```

### Funciones

Esta interfaz se divide a su vez en funciones a nivel de eje y funciones a nivel de figura.

![](https://seaborn.pydata.org/_images/function_overview_8_0.png)

#### Funciones a nivel de figura (subplots).

En esta interfaz se usan las funciones `sns.catplot()`, `sns.relplot()` y `sns.displot()` que retornan una instancia de la clase `FacetGrid`, así como `sns.pairplot()` y `sns.jointplot()`, que retornan `JointGrid` y `PairGrid`, respectivamente. El tipo de gráfica se especifica con el parámetro _kind_, para gráficas con _subplots_ se debe de especificar los parámetros _col_ y/o _row_.

```python
# Importar módulos
import seaborn as sns
import matplotlib.pyplot as plt

# Utilizar función
sns.figure_function(data, x, y, [kind, col, row])

# Imprimir figura
plt.show()
```
**Notas**
- _data_ - `DataFrame`, `Series`, `dict`, `ndarray`: Son los datos que se van a graficar.
- _x_, _y_ - `array-like`, `str`: Especifican los datos del eje _x_ y _y_ respectivamente:
    - `array-like`: En caso de que no se haya especificado _data_, se puede proveer de un arreglo con los datos para cada eje.
    - `str`: En caso de _data_ sea `DataFrame` o `dict`, es la etiqueta de los datos que se van a graficar en cada eje.  

**Ejemplo - un axes**: 

En este ejemplo únicamente se especifica el parámetro _kind_ para indicar el tipo de gráfica en el eje.

```{code-cell} ipython3
# Utilizar función
sns.relplot(yearly_data, x='year', y='passengers', kind="line", color=azul)

# Imprimir figura
plt.show()
```


**Ejemplo - mútiples axes**: 

En este ejemplo se utiliza el parámetro _col_ para crear una figura con múltiples ejes.

```{code-cell} ipython3
# Utilizar función
sns.catplot(sub_flights, x='month', y='passengers', kind='bar', col='year', color=azul)

# Imprimir figura
plt.show()
```

#### Funciones a nivel de ejes

En esta interfaz se usan las funciones de `seaborn` para especificar el tipo de gráfica. Retornando un objeto `Axes` de `matplotlib`.

```python
# Importar módulos
import seaborn as sns
import matplotlib.pyplot as plt

# Utilizar función
sns.axes_function(data, x, y, [hue])

# Imprimir figura
plt.show()
```
**Notas**
- _data_ - `DataFrame`, `Series`, `dict`, `ndarray`: Son los datos que se van a graficar.
- _x_, _y_, _hue_ - `array-like`, `str`: Especifican los datos del eje _x_ y _y_ respectivamente:
    - `array-like`: En caso de que no se haya especificado _data_, se puede proveer de un arreglo con los datos para cada eje.
    - `str`: En caso de _data_ sea `DataFrame` o `dict`, es la etiqueta de los datos que se van a graficar en cada eje.
- _hue_ - `array-like`, `str`: Es una variable categórica que especifica cómo segmentar los datos por los valores únicos de esta variable. Identifica para valor con un color diferente y añade una leyenda.

**Ejemplo**:

```{code-cell} ipython3
# Utilizar función
sns.lineplot(yearly_data, x='year', y='passengers', color=azul)

# Imprimir figura
plt.show()
```

### Interfaz de objetos

En esta interfaz se usan clases del módulo `seaborn.objects`, se inicializa una gráfica con la clase `Plot` y se añaden capaz para especificar el tipo de gráficas y personalización.

**Ejemplo un eje**:

```{code-cell} ipython3
# Importar interfaz
import seaborn.objects as so

# Crear gráfica
plot = (
    so.Plot(yearly_data, x='year', y='passengers')
    .add(so.Line(color=azul))
    .add(so.Dot(color=azul))
    .label(x='Año', y='Total de Pasajeros', title='Tendencia de total de pasajeros')
)

# Mostrar gráfica
plot.show()
```

**Ejemplo múltiples ejes**:

```{code-cell} ipython3
# Importar interfaz
import seaborn.objects as so

# Crear gráfica
plot = (
    so.Plot(sub_flights, x='month', y='passengers')
    .add(so.Bar(color=azul))
    .facet(col='year')
    .layout(size=(10, 6))
)

# Mostrar gráfica
plot.show()
```

### Tamaños

Las funciones a nivel de _ejes_ se pueden crear en un _Axes_ especificado, con el argumento _ax_, si no se especifica, se creará un _axes_ nuevo en una nueva figura. Para definir un tamaño especifico de la gráfica tener en cuenta:
- A nivel de _ejes_ utilizar las funciones de `matplotlib` para definir el tamaño de la figura (como `plt.subplots()` y/o el argumento _figsize_).
- A nivel de figura utilizar los argumentos _heigh_ y _aspect_.
- Con la interfaz basada en objeros usar el método _.layout_ y el parámetro _size_: `g.layout(size=(width, height))`