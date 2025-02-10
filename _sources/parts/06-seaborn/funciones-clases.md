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

# Funciones y Clases

```{code-cell} ipython3
:tags: ["remove-input"]

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

azul="#30adb9"
cafe="#ba6a30"
cafe_claro="#cf9975"
```

En esta sección se resumen las funciones y clases relacionadas con la interface por funciones.

---
## Categóricas

Funciones para graficar variables categóricas, incluyendo gráficas de barras, _boxplots_, gráfica de puntos, gráfica de recuentos, gráficas de violines y de panales, etc. Existe la gráfica a nivel de figura y varias a nivel de ejes.

**Figure level**

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [catplot](https://seaborn.pydata.org/generated/seaborn.catplot.html)(data=None, ...)
  - Interfaz a nivel de figura para crear gráficos categóricos en un `FacetGrid`.
```
**Parámetros:**
- **x**, **y** - ` array-like ` o `str`: Pueden ser vectores o etiquetas en _data_, que especifican los valores en los ejes _x_ y _y_ respectivamente. Una de ellas debe de ser una variable categórica. Dependiendo de en cuál eje se haya puesta la variable categórica la gráfica será horizontal o vertical.
- **data** - `DataFrame`, `ndarray`, `mapping` o `secuencia`: Estructura de datos de entrada.
- **kind** - `str`: Para especificar el tipo de gráfica:.
    - Dispersión: 'strip', 'swarm'.
    - Distribución: 'boxplot', 'violinplot', 'boxenplot'.
    - Estimación: 'pointplot', 'barplot', 'countplot'.
- **hue** - ` array-like ` o `str`: Pueden ser vectores o etiquetas en _data_, es una variable categórica que es mapeada para determinar el color de los elementos de la gráfica.
- **hue_order** - `array-like` de `str`: Para indicar el orden de las categorías del argumento _hue_. Deben de ser los valores únicos ordenadas en orden que prefieras de _hue_.
- **row**, **col** - ` array-like ` o `str`: Pueden ser vectores o etiquetas en _data_, es una variable categórica para crear _subplots_ de acuerdo a los valores de ésta. Si se usan ambos se creará una matriz.
- **col_wrap** - `int`: Para indicar un número máximo de columnas de gráficas a realizar, si se supera se crearán filas. Es incompatible con el argumento row.
- **estimator** - `callable`: Una función que de entrada reciba un `vector` y retorne un `scalar`. Pueden ser métodos de `DataFRame` como _mean_, _median_, etc.
- **ci** - `float`: Tamaño del intervalo de confianza al agregar un estimator.
- **order** - `list` de `str`: Para modificar el orden de las categorías. Debe ser una lista con las categorías únicas ordenas en el orden deseado.
- **col_order**, **row_order** - `array-like` de `str`: Los elementos de la columna/fila para indicar cómo ordenar cada uno de los valores.
- **height** - `scalar`: Altura de cada facet en pulgadas.
- **aspect** - `scalar`: Radio entre la altura y ancho de cada facet en pulgadas.
- **orient** - {'v', 'h'}: Orientación de la gráfica.
- **color** - `color`: Color de todos los elementos.
- **palette** - `string`, `list`, `dict` o `matplotlib.colors.Colormap`: Métodos para escoger la paleta de colores, cuando se mapea con base a hue.
- **legend** - `bool`: Para indicar si mostrar una leyenda.

Patrones útiles.

```python
# Uso de función a nivel de figura
sns.catplot(x, y, [data], [kind], [col], [row])

# Modificar orden de las categorías
category_order=['cat1', 'cat2', ...]
sns.catplot(x, y, [data], [kind], [col], [row], order=category_order)
```

<br/>

**Axes level**

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [barplot](https://seaborn.pydata.org/generated/seaborn.barplot.html)(data=None, ...)
  - Realiza una gráfica de barras, sumariza los datos con un _aggregate_ (media por default) y añade _error bars_ con un intevarlo de confianza del 95%, de acuerdo a los valores de una variable categórica.
* - [boxenplot](https://seaborn.pydata.org/generated/seaborn.boxenplot.html)(data=None, ...)
  - Grafica un diagrama de caja mejorado para conjuntos de datos más grandes y permite visualizar de mejor manera la distribución de los datos.
* - [boxplot](https://seaborn.pydata.org/generated/seaborn.boxplot.html)(data=None, ...)
  - Grafica un boxplot, para mostrar la distribución de acuerdo a los valores de una variable categórica.
* - [countplot](https://seaborn.pydata.org/generated/seaborn.countplot.html)(data=None, ...)
  - Genera una gráfica de barras, donde la altura de la barra será el número de veces que se repite cada categoría en toda la columna, de acuerdo a los valores de una variable categórica.
* - [pointplot](https://seaborn.pydata.org/generated/seaborn.pointplot.html)(data=None, ...)
  - Grafica estimaciones puntuales y errores usando líneas con marcadores por categorías.
* - [stripplot](https://seaborn.pydata.org/generated/seaborn.stripplot.html)(data=None, ...)
  - Grafica una diagrama de dispersión donde una de las variables es categórica, utilizando _jitter_ para reducir marcas superpuestas.
* - [swarmplot](https://seaborn.pydata.org/generated/seaborn.swarmplot.html)(data=None, ...)
  - Grafica un diagrama de dispersión donde una de las variables es categórica. Es similar a `sns.stipplot()`, la diferencia es que distribuye los puntos a lo largo del eje categórico de manera de éstos no se sobreencimen y permite una mejor visualización de la distribución de los valores.
* - [violinplot](https://seaborn.pydata.org/generated/seaborn.violinplot.html)(data=None, ...)
  - Grafica una combinación entre un boxplot y una estimación de la densidad del kernel.
```
**Parámetros comunes**:
- **x**, **y** - ` array-like ` o `str`: Pueden ser vectores o etiquetas en data, que especifican los valores en los ejes _x_ y _y_ respectivamente. Una de ellas debe de ser una variable categórica. Dependiendo de en cuál eje se haya puesta la variable categórica la gráfica será horizontal o vertical. Algunas gráficas aceptan solo uno de los dos y otras los dos.
- **data** - `DataFrame`, `ndarray`, `mapping` o `secuencia`: Estructura de datos de entrada.
- **hue** - ` array-like ` o `str`: Pueden ser vectores o etiquetas en _data_. Es una variable categórica que es mapeada para determinar el color de los elementos de la gráfica, estableciendo la leyenda de la gráfica.
- **order** - `list` de `str`: Para modificar el orden de las categorías. . Deben de ser los valores únicos ordenados en orden que se prefiera
- **hue_order** - `array-like` de `str`: Para indicar el orden de las categorías del argumento _hue_. Deben de ser los valores únicos ordenados en orden que se prefiera de _hue_.
- **orient** - {'v', 'h'}: Orientación de la gráfica.
- **color** - `color`: Color de todos los elementos.

Patrones útiles.

```python
# Uso de función a nivel de ejes
sns.function_name([x], [y], [data])

# Modificar orden de las categorías
category_order=['cat1', 'cat2', ...]
sns.function_name([x], [y], [data], order=category_order)
```

### Ejemplo de _bar_

[barplot](https://seaborn.pydata.org/generated/seaborn.barplot.html): Realiza una gráfica de barras, sumariza los datos con un _aggregate_ (media por default) y añade _error bars_ con un intevarlo de confianza del 95%, de acuerdo a los valores de una variable categórica.

:::{tip}
Para cambiar la orientación de las barras intercambiar los argumentos _x_ y _y_.
:::

Patrones comunes:
```python
# Modificar el estimador (por default media)
sns.barplot(x='x', y='y', data=data, estimator=median)

# Modificar intervalos de confianza
sns.barplot(x='x', y='y', data=data, estimator=('ci', 95))
```
Notas:
- _estimator_ - `pandas method` o `callable`: Una función que de entrada reciba un `array-like` y retorne un `scalar`. Puede ser un método de _data_ como _mean_, _median_, etc.
- _errorbar_ - `str`, `tuple`, `callable` o `None`: Tipo de barras de errores.
    - `str` - {'ci', 'pi', 'se', or 'sd'}: Nombre del método.
    - `tuple`: Tupla de dos elementos con el nombre del método y el nivel del parámetro, por ejemplo `('ci', 95)`, es un intervalo de confianza del 95%.
    - `callable`: Función que recibe un `array-like` y retorna un tuple `(min, max)` con el intervalo.
    - `None`: Para ocultar las barras de errores. 

En este ejemplo de gráfica la media de _bill_length_mm_ para cada _species_.

```{code-cell} ipython3
# Importar el dataset iris
penguins=sns.load_dataset("penguins")

# Definir graficar
sns.barplot(x="species", y='bill_length_mm', data=penguins, color=azul)
# Equivale a: sns.catplot(x="species", y='bill_length_mm', data=penguins, kind="bar")

# Imprimir gráfica
plt.show()
```

### Ejemplo de _box_

[boxenplot](https://seaborn.pydata.org/generated/seaborn.boxenplot.html): Grafica un boxplot, para mostrar la distribución de acuerdo a los valores de una variable categórica.

:::{tip}
Para cambiar la orientación de las barras intercambiar los argumentos _x_ y _y_.
:::

Patrones útiles:
```python
# Omitir datos atíplicos
sns.boxplot(x='x', y='y', data=data, sym="")

# Modificar orden las categorías
category_order=['cat1', 'cat2', ...]
sns.function_name(x='x', y='y', data=data, order=category_order)

# Modificar los "bigotes"
sns.boxplot(x='x', y='y', data=data, whis=[q1, q2])
```
Notas:
- _whis_ - `float` o `list`: Proporción del _IQR_, para indicar el rango máximo de los bigotes del boxplot, por default es `1.5*IQR`. Los puntos fuera de este rango serán considerados outliers. Si se quieren incluir todos los datos usar np.inf o `[0, 100]`. Se puede indificar percentiles específicos con una lista de dos elementos, por ejemplo `[5, 95]`, mostraría hasta los percentiles 5 y 95.

En este ejemplo de grafica la distribucipon de _total_bill_ para cada _day_.

```{code-cell} ipython3
# Importar el dataset tips
tips=sns.load_dataset("tips")

# Definir graficar
sns.boxplot(x="day", y='total_bill', data=tips, color=azul)
# Equivale a: sns.catplot(x="day", y='total_bill', data=tips, kind="box")

# Imprimir gráfica
plt.show()
```

### Ejemplo de _countplot_

[countplot](https://seaborn.pydata.org/generated/seaborn.countplot.html): Genera una gráfica de barras, donde la altura de la barra será el número de veces que se repite cada categoría en toda la columna, de acuerdo a los valores de una variable categórica.

:::{tip}
Para cambiar la orientación de las barras utilizar el argumento _y_ en lugar de _x_, o viceversa.
:::

:::{caution}
Solo se debe de especificar uno de los parámetros _x_ o _y_, no ambos.
:::

En este ejemplo de grafica la cantidad de observaciones para cada _species_.

```{code-cell} ipython3
# Importar el dataset iris
penguins=sns.load_dataset("penguins")

# Definir graficar
sns.countplot(x="species", data=penguins, color=azul)
# Equivale a: sns.catplot(x="species", data=penguins, kind="count")

# Imprimir gráfica
plt.show()
```

### Ejemplo de _swarmplot_

[swarmplot](https://seaborn.pydata.org/generated/seaborn.swarmplot.html): Grafica un diagrama de dispersión donde una de las variables es categórica. Es similar a `sns.stipplot()`, la diferencia es que distribuye los puntos a lo largo del eje categórico de manera de éstos no se sobreencimen y permite una mejor visualización de la distribución de los valores.

En este ejemplo de gráfica la distribución de _total_bill_ para cada _day_.

```{code-cell} ipython3
# Definir grafica
sns.swarmplot(x="day", y='total_bill', data=tips, color=azul)
# Equivale a: sns.catplot(x="day", y='total_bill', data=tips, kind="swarm")

# Imprimir gráfica
plt.show()
```

<br/>

---
## Distribución

Funciones útiles para visualizar la distribución de los datos. Existe la gráfica a nivel de figura y varias a nivel de ejes.

**Figure level**

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [displot](https://seaborn.pydata.org/generated/seaborn.displot.html)(data=None, ...)
  - Interfaz a nivel de figura para generar gráficos de distribución en un `FacetGrid`.
```
**Parámetros:**
- **x**, **y** - ` array-like ` o `str`: Pueden ser vectores o etiquetas en _data_, que especifican los valores en los ejes _x_ y _y_ respectivamente.
- **data** - `DataFrame`, `ndarray`, `mapping` o `secuencia`: Estructura de datos de entrada.
- **kind** - {'hist', 'kde', 'ecdf'}: Para especificar el tipo de gráfica:.
    - 'hist': Histograma.
    - 'kde': Kernel density.
    - 'ecdf': Empirical cumulative distribution function.
- **hue** - ` array-like ` o `str`: Pueden ser vectores o etiquetas en _data_. Es una variable categórica que es mapeada para determinar el color de los elementos de la gráfica.
- **row**, **col** - ` array-like ` o `str`: Pueden ser vectores o etiquetas en _data_, es una variable categórica para crear _subplots_ de acuerdo a los valores de ésta. Si se usan ambos se creará una matriz.
- **col_wrap** - `int`: Para indicar un número máximo de columnas de gráficas a realizar, si se supera se crearán filas cuando se usa _col_. Es incompatible con el parámetro _row_.
- **col_order**, **row_order** - `array-like` de `str`: Los elementos de la _col_ o _row_ para indicar cómo ordenar cada uno de los valores, se utilizan solo los valores únicos de esos argumentos.
- **rug** - `bool`: Para indicar que para cada observación se muestren ticks marginales.
- **rug_kws** - `dict`: Para manipular la apariencia del rug.
- **palette** - `strin`, `list`, `dict` o `matplotlib.colors.Colormap`: Métodos para escoger la paleta de colores, cuando se mapea con base a _hue_.
- **hue_order** - `array-like` de `str`: Para indicar el orden de las categorías del argumento _hue_. Deben de ser los valores únicos ordenadas en orden que prefieras de hue.
- **legend** - {'auto', 'brief', 'full', False}: Para indicar cómo mostrar una leyenda.
- **height** - `scalar`: Altura de cada _facet_ en pulgadas.
- **aspect** - `scalar`: Radio entre la altura y ancho de cada _facet_ en pulgadas.
- **color** - `color`: Color de todos los elementos.
- **\*\*kwargs**: Argumentos adicionales de `histplot()`, `kdeplot()` y `ecdfplot()`.

:::{tip}
Para crear dos tipos de gráficas en el mismo _facet_, por ejemplo un histograma y un _kde_ se puede usar los argumentos: _kde_ y _rug_.
:::

<br/>

**Axes level**

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [ecdfplot](https://seaborn.pydata.org/generated/seaborn.ecdfplot.html)(data=None, ...)
  - Grafica la función de distribución acumulada empirica.
* - [histplot](https://seaborn.pydata.org/generated/seaborn.histplot.html)(data=None, ...)
  - Grafica histogramas univariados o bivariados, para visualizar la distribución de _datasets_.
* - [kdeplot](https://seaborn.pydata.org/generated/seaborn.kdeplot.html)(data=None, ...)
  - Grafica distribuciones univariadas o bivariadas, usando la estimación de la densidad del kernel.
* - [rugplot](https://seaborn.pydata.org/generated/seaborn.rugplot.html)(data=None, ...)
  - Grafica distribuciones marginales por medio de _ticks_ a lo largo de los ejes _x_ y _y_.
```
**Parámetros comunes**:
- **x**, **y** - ` array-like ` o `str`: Pueden ser vectores o etiquetas en data, que especifican los valores en los ejes _x_ y _y_ respectivamente. Una de ellas debe de ser una variable categórica. Dependiendo de en cuál eje se haya puesta la variable categórica la gráfica será horizontal o vertical. Algunas gráficas aceptan solo uno de los dos y otras los dos.
- **data** - `DataFrame`, `ndarray`, `mapping` o `secuencia`: Estructura de datos de entrada.
- **hue** - ` array-like ` o `str`: Pueden ser vectores o etiquetas en _data_. Es una variable categórica que es mapeada para determinar el color de los elementos de la gráfica, estableciendo la leyenda de la gráfica.
- **hue_order** - `array-like` de `str`: Para indicar el orden de las categorías del argumento _hue_. Deben de ser los valores únicos ordenados en orden que se prefiera de _hue_.

### Ejemplo de _histplot_

[histplot](https://seaborn.pydata.org/generated/seaborn.histplot.html): Grafica histogramas univariados o bivariados, para mostrar la distribución de datasets.

Patrones útiles:
```python
# Agregar kde
sns.histplot(x='col', data=data, kde=True)
```

En este ejemplo se gráfica la distribución de _total_bill_.

```{code-cell} ipython3
# Definir grafica
sns.histplot(x='total_bill', data=tips, bins=20, color=azul)
# Equivale a: sns.displot(x="total_bill", data=tips, kind="hist", bins=20, color=azul)

# Imprimir gráfica
plt.show()
```
- El valor por default es `kind="hist"`, por lo que no es necesario especificarlo.

### Ejemplo de _kdeplot_

[kdeplot](https://seaborn.pydata.org/generated/seaborn.kdeplot.html): Grafica distribuciones univariadas o bivariadas, usando la estimación de la densidad del kernel.

Patrones útiles:
```python
# Agregar rug
sns.kdeplot(x='col', data=data, rug=True)

# Con relleno
sns.kdeplot(x='col', data=data, fill=True)
```

En este ejemplo se gráfica la distribución de _total_bill_.

```{code-cell} ipython3
# Definir grafica
sns.kdeplot(x='total_bill', data=tips, color=azul)
# Equivale a: sns.displot(x="total_bill", data=tips, kind="kde", color=azul)

# Imprimir gráfica
plt.show()
```

<br/>

---
## Matriz

Funciones para crear gráficas matriciales como mapas de calor.


```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [clustermap](https://seaborn.pydata.org/generated/seaborn.clustermap.html)(data, ...)
  - Grafica datos rectangulares, como una matriz, que muestra datos jerarquicamente agrupados (grupos de datos similares los pone juntos, es como un _heatmap_ ordenado por grupos similares) y la magnitud en colores.
* - [heatmap](https://seaborn.pydata.org/generated/seaborn.heatmap.html)(data, ...)
  - Grafica datos rectangulares como una matriz que muestra la magnitud como colores.
```

### Ejemplo de _heatmap_

[heatmap](https://seaborn.pydata.org/generated/seaborn.heatmap.html): Grafica datos rectangulares como una matriz que muestra la magnitud como colores.

:::{tip}
Es común que para graficar mapas de calor se usen las siguientes funciones:
- `pd.crosstab()`: Calcula un _aggregate_ de los valores de la combinación de dos variables categóricas.
- `pd.corr()`: Calcula la correlación en pares de variables cuantitativas.
:::

Patrones útiles

```python
# Añadir valor en cada celda
sns.heatmap(data, annot=True)

# Cambiar paleta y valor 0
sns.heatmap(data, cmap='cmap', center=float)

# Desactivar barra de color
sns.heatmap(data, cbar=False)

# Modificar valores mínimo y máximo de la barra de color
sns.heatmap(data, vmin=float, vmax=float)
```

En este ejemplo se calcula el mapa de calor de la correlación de las variables numéricas del dataset _penguins_.

```{code-cell} ipython3
# Crear mapa de calor
sns.heatmap(penguins.corr(numeric_only=True), cmap='BrBG', center=0)

# Imprimir gráfica
plt.show()
```

<br/>

---
## Regresión

Funciones útiles para análisis de regresión.

**Figure level**

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [lmplot](https://seaborn.pydata.org/generated/seaborn.lmplot.html)(data, ...)
  - Interfaz a nivel de figura para generar gráficos de datos y ajustar del modelo de regresión en un `FacetGrid`.
```
**Parámetros:**
- **x**, **y** - ` array-like ` o `str`: Pueden ser vectores o etiquetas en _data_, que especifican los valores en los ejes _x_ y _y_ respectivamente. Una de ellas debe de ser una variable categórica. Dependiendo de en cuál eje se haya puesta la variable categórica la gráfica será horizontal o vertical.
- **data** - `DataFrame`, `ndarray`, `mapping` o `secuencia`: Estructura de datos de entrada.
- **kind** - `str`: Para especificar el tipo de gráfica:.
    - Dispersión: 'strip', 'swarm'.
    - Distribución: 'boxplot', 'violinplot', 'boxenplot'.
    - Estimación: 'pointplot', 'barplot', 'countplot'.
- **hue** - ` array-like ` o `str`: Pueden ser vectores o etiquetas en _data_, es una variable categórica que es mapeada para determinar el color de los elementos de la gráfica.
- **hue_order** - `array-like` de `str`: Para indicar el orden de las categorías del argumento _hue_. Deben de ser los valores únicos ordenadas en orden que prefieras de _hue_.
- **row**, **col** - ` array-like ` o `str`: Pueden ser vectores o etiquetas en _data_, es una variable categórica para crear _subplots_ de acuerdo a los valores de ésta. Si se usan ambos se creará una matriz.
- **col_wrap** - `int`: Para indicar un número máximo de columnas de gráficas a realizar, si se supera se crearán filas. Es incompatible con el argumento row.
- **x_estimator** - `callable`: Una función que de entrada reciba un `vector` y retorne un `scalar`. Pueden ser métodos de `DataFRame` como _mean_, _median_, etc.
- **ci** - `float`: Tamaño del intervalo de confianza al agregar un estimator.
- **order** - `list` de `str`: Para modificar el orden de las categorías. Debe ser una lista con las categorías únicas ordenas en el orden deseado.
- **col_order**, **row_order** - `array-like` de `str`: Los elementos de la columna/fila para indicar cómo ordenar cada uno de los valores.
- **height** - `scalar`: Altura de cada facet en pulgadas.
- **aspect** - `scalar`: Radio entre la altura y ancho de cada facet en pulgadas.
- **orient** - {'v', 'h'}: Orientación de la gráfica.
- **color** - `color`: Color de todos los elementos.
- **palette** - `string`, `list`, `dict` o `matplotlib.colors.Colormap`: Métodos para escoger la paleta de colores, cuando se mapea con base a hue.
- **legend** - `bool`: Para indicar si mostrar una leyenda.

**Axes level**

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [regplot](https://seaborn.pydata.org/generated/seaborn.regplot.html)(data=None, ...)
  - Gráfica datos (diagrama de dispersión) y ajusta un modelo de regresión.
* - [residplot](https://seaborn.pydata.org/generated/seaborn.residplot.html)(data=None, ...)
  - Grafica los residules de un modelo de regresión.
```

### Ejemplo de _regplot_

[regplot](https://seaborn.pydata.org/generated/seaborn.regplot.html): Gráfica datos (diagrama de dispersión) y ajusta un modelo de regresión.


Patrones útiles:
```python
# Modificar estilo de marker
sns.regplot(x="x", y="y", data=data, marker='sym')

# Ajustar polinomio de otro grado
sns.regplot(x="x", y="y", data=data, order=int)

# Jitter sobre el eje x
sns.regplot(x="x", y="y", data=data, x_jitter=float)

# Jitter sobre el eje y
sns.regplot(x="x", y="y", data=data, y_jitter=float)

# Estimador sobre eje x
sns.regplot(x="x", y="y", data=data, x_estimator=np.mean)
```
- **`marker`** - `marker code` `: Tipo de marker en la gráfica.
- **`order`** - `int`: Para indicar el orden de regresión, para regresiones polinómicas.
- **`x_jitter`**, **`y_jitter`**, - `int`: Añade ruido a los valores _x_ y _y_ respectivamente. Útil para visualizar mejor puntos que se sobreenciman mucho.
- **`x_estimator`** - `callable`: Función que reciba un `vector` y retorne un `scalar`. Aplica esta función a cada valor único de _x_ y grafica la estimación resultante. Es útil cuando _x_ son valores categóricos ordenados.
- **`x_bins`** - `int` o `vector`: Agrupa la variable _x_ en _bins_ discretos, estima la tendencia central y un intervalo de confianza por cada _bin_.



En este ejemplo se gráfica el diagrama de dispersión y la regresión lineal de _bill_length_mm_ vs _bill_depth_mm_ del dataset _penguins_. 

```{code-cell} ipython3
# Definir grafica
sns.regplot(x="bill_length_mm", y="bill_depth_mm", data=penguins, color=azul)
# Equivale a: sns.lmplot(x="bill_length_mm", y="bill_depth_mm", data=penguins, color=azul)

# Imprimir gráfica
plt.show()
```

<br/>

---
## Relacionales

Funciones útiles para visualizar la relación entre dos variales.

**Figure level**

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [relplot](https://seaborn.pydata.org/generated/seaborn.relplot.html)(data=None, ...)
  - Interfaz a nivel de figura para generar gráficos relacionales en un `FacetGrid`.
```
**Parámetros comunes:**
- **x**, **y** - ` array-like ` o `str`: Pueden ser vectores o etiquetas en _data_, que especifican los valores en los ejes _x_ y _y_ respectivamente.
- **data** - `DataFrame`, `ndarray`, `mapping` o `secuencia`: Estructura de datos de entrada.
- **kind** - `str`: Para especificar el tipo de gráfica.
    - 'scatter': Diagrama de dispersión.
    - 'line': Gráfico de líneas.
- **hue** - ` array-like ` o `str`: Pueden ser vectores o etiquetas en _data_. Es una variable categórica que es mapeada para determinar el color de los elementos de la gráfica.
- **size** - `vector` o `str`: Un vector o una etiqueta en _data_, para realizar los puntos de diferente tamaño de acuerdo a los valores de esta variable.
- **style** - `vector` o `str`: Un vector o una etiqueta en _data_, para realizar los puntos de diferente estilo de acuerdo a los valores de esta variable.
- **row**, **col** - ` array-like ` o `str`: Pueden ser vectores o etiquetas en _data_, es una variable categórica para crear _subplots_ de acuerdo a los valores de ésta. Si se usan ambos se creará una matriz.
- **col_wrap** - `int`: Para indicar un número máximo de columnas de gráficas a realizar, si se supera se crearán filas cuando se usa _col_. Es incompatible con el parámetro _row_.
- **col_order**, **row_order** - `array-like` de `str`: Los elementos de la _col_ o _row_ para indicar cómo ordenar cada uno de los valores, se utilizan solo los valores únicos de esos argumentos.
- **palette** - `strin`, `list`, `dict` o `matplotlib.colors.Colormap`: Métodos para escoger la paleta de colores, cuando se mapea con base a _hue_.
- **hue_order** - `array-like` de `str`: Para indicar el orden de las categorías del argumento _hue_. Deben de ser los valores únicos ordenadas en orden que prefieras de hue.
- **legend** - {'auto', 'brief', 'full', False}: Para indicar cómo mostrar una leyenda.
- **height** - `scalar`: Altura de cada _facet_ en pulgadas.
- **aspect** - `scalar`: Radio entre la altura y ancho de cada _facet_ en pulgadas.

Patrones útiles:
```python
# Gráfico de líneas con markers
sns.relplot(x="x", y="y", data=data, [kind], markers=True)

# Subplots en las columnas
sns.relplot(x="x", y="y", data=data, [kind], col='col')

# Subplots en las filas
sns.relplot(x="x", y="y", data=data, [kind], row='row')

# Modificar orden de las categorías de los subplots (ejm col)
category_order=['cat1', 'cat2', ...]
sns.relplot(x="x", y="y", data=data, [kind], col_order=category_order)
```

<br/>

**Axes level**

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [lineplot](https://seaborn.pydata.org/generated/seaborn.lineplot.html)(data=None, ...)
  - Realiza una gráfica de líneas.
* - [scatterplot](https://seaborn.pydata.org/generated/seaborn.scatterplot.html)(data=None, ...)
  - Grafica un diagrama de dispersión.
```
**Parámetros comunes:**
- **x**, **y** - ` array-like ` o `str`: Pueden ser vectores o etiquetas en _data_, que especifican los valores en los ejes _x_ y _y_ respectivamente.
- **data** - `DataFrame`, `ndarray`, `dict` o `secuencia`: Estructura de datos de entrada.
- **hue** - ` array-like ` o `str`: Pueden ser vectores o etiquetas en _data_. Es una variable categórica que es mapeada para determinar el color de los elementos de la gráfica, estableciendo la leyenda de la gráfica.
- **size** - `vector` o `str`: Un vector o un etiqueta en _data_, para realizar los puntos de diferente tamaño de acuerdo a los valores de esta variable.
- **style** - `vector` o `str`: Un vector o un etiqueta en data, para realizar los trazos de diferente estilo de acuerdo a los valores de esta variable.
- **palette** - `str`, `list`, `dict` o `matplotlib.colors.Colormap`: Métodos para escoger la paleta de colores, cuando se mapea con base a hue.
    - `str`: Nombre de una paleta de colores.
    - `list`: Una lista con un color por cada valor único de la variable definida en _hue_.
    - `dict`: Un diccionario con _keys_ como los valores únicos de la varaible definida en _hue_ y como _values_ un color.
- **hue_order** - `array-like` de `str`: Para indicar el orden de las categorías del argumento _hue_. Deben de ser los valores únicos ordenadas en el orden que se prefiera de _hue_.
- **alpha** - `float`: Opacidad de los trazos.

### Ejemplo de _scatter_

[scatterplot](https://seaborn.pydata.org/generated/seaborn.scatterplot.html): Grafica un diagrama de dispersión.

Patrones útiles:

```python
# Gráfico con leyenda
sns.scatterplot(x="x", y="y", data=data, hue='hue')

# Modificar estilo de markers con base a variable categórica
sns.scatterplot(x="x", y="y", data=data, style='style')

# Modificar estilo de marker
sns.scatterplot(x="x", y="y", data=data, marker='+')

# Modificar transparencia de marker
sns.scatterplot(x="x", y="y", data=data, alpha=alpha)

# Modificar tamaño de markers con base a variable categórica
sns.scatterplot(x="x", y="y", data=data, size='size')
```

En este ejemplo se crea un diagrama de dispersión entre _bill_length_mm_ y _bill_depth_mm_, además se crea una leyenda por _sex_ y se modifica el estilo del marcador por _species_.

```{code-cell} ipython3
# Crear gráfica
sns.scatterplot(x="bill_length_mm", 
                y="bill_depth_mm", 
                data=penguins,
                hue='sex',
                style='species',
                palette={'Male': azul, 'Female': cafe})
                
# Equivale a:            
# sns.relplot(x="bill_length_mm", y="bill_depth_mm", data=penguins, hue='sex', style='species', kind="scatter")

# Imprimir gráfica
plt.show()
```

### Ejemplo de _line_

[lineplot](https://seaborn.pydata.org/generated/seaborn.lineplot.html): Realiza una gráfica de líneas.

Patrones útiles:

```python
# Gráfico de líneas con markers
sns.lineplot(x="x", y="y", data=data, markers=True)

# Gráfico con leyenda
sns.lineplot(x="x", y="y", data=data, hue='hue')

# Modificar estilo de trazos con base a variable categórica
sns.lineplot(x="x", y="y", data=data, style='style')

# Modificar transparencia de trazos
sns.lineplot(x="x", y="y", data=data, alpha=alpha)

# Desactivar estilo de líneas
sns.lineplot(x="x", y="y", data=data, dashes=False)

# Modificar estimador
sns.lineplot(x="x", y="y", data=data, estimator=median)

# Modificar intervalo de confianza**
sns.lineplot(x="x", y="y", data=data, errorbars=('ci', 95))
```
Notas:
- _dashes_ - `bool`, `list`, `dict`: Para indicar cómo dibujar las líneas de las gráficas.
    - `bool`: Para indicar que se use lo estilos por default o que no se usen líneas.
    - `list`: Una lista de los tipo de línea.
    - `dict`: Para mapear un estilo a cada gráfica.
- _markers_ - `bool`, `list`, `dict`: Para indicar cómo dibujar los markers de las gráficas.
    - `bool`: Para indicar que se use lo estilos por default o que no se usen markers.
    - `list`: Una lista de los tipo de markers.
    - `dict`: Para mapear un estilo a cada gráfica.
- _estimator_ - `pandas method` o `callable`: Una función que de entrada reciba un `array-like` y retorne un `scalar`. Puede ser el nombre de un método de _data_ como _mean_, _median_, etc.
- _errorbar_ - `str`, `tuple`, `callable` o `None`: Tipo de barras de errores.
    - `str` - {'ci', 'pi', 'se', or 'sd'}: Nombre del método.
    - `tuple`: Tupla de dos elementos con el nombre del método y el nivel del parámetro, por ejemplo `('ci', 95)`, es un intervalo de confianza del 95%.
    - `callble`: Función que recibe un `array-like` y retorna un tuple `(min, max)` con el intervalo.
    - `None`: Para ocultar las barras de errores.

En este ejemplo se grafica el _tip_ para los días, con la leyenda por _smoker_.

```{code-cell} ipython3
# Crear el gráfico de líneas
sns.lineplot(x="day", y="tip", hue="smoker", data=tips,
                palette={'Yes': azul, 'No': cafe})
# Equivale a: sns.relplot(tips, x='day', y='tip', hue="smoker", kind="line", errorbar=None)

# Imprimir gráfica
plt.show()
```

 

<br/>

---
## Personalización

Para personalizar gráficas en `seaborn` dependerá del tipo retornado por la función:
- Funciones a nivel de figura: Para ver cómo personalizar las clases retornadas por funciones a nivel de figura revisar los métodos de la clase en cuestión. Tener en cuenta que todas las clases de `seaborn` heredan métodos de la clase `Figure` de `matplotlib`, por lo que los métodos de esta clase también se pueden usar para personalizar gráficas en `seaborn`.
- Funciones a nivel de eje: Las funciones a nivel eje retornar instancias de la clase `Axes` de `matplotlib`, por lo que se pueden usar sus {ref}`métodos de personalización <axes-methods-customization>` para personalizar estas gráficas.

```python
# Ejemplo de customización a nivel de ejes:
fig, ax = plt.subplots()
sns.axes_function(df['col'], ax=ax)
ax.set(xlabel="x label", ylabel="y label", title="Title")
```
- Nivel de ejes:
    - En este ejemplo se uso la interfaz orienta a objetos para crear el objetos _ax_. También se podría asignar la función a una _dummy variable_ y usar los métodos de `Axes` en esa variable: `_ = sns.axes_function(df['col'])` <br/> `_.set(xlabel="x label", ylabel="y label", title="Title")`
    - En este ejemplo se uso el método `Axes.set()`, pero se podría usar cualquier otro método.

Las siguientes funciones se pueden utilizar para realizar ciertas acciones a las gráficas:

Otras funciones útiles para manipulación de las gráficas, relacionadas con eliminar los ejes y reubicar la leyenda a otra posición. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [despine](https://seaborn.pydata.org/generated/seaborn.despine.html)(fig=None, ax=None, top=True, right=True, left=False, bottom=False, offset=None, trim=False)
  - Remueve los ejes (_spines_) de una gráfica (el cuadrado que rodea la gráfica), por default remueve el superior y el derecho.
* - [move_legend](https://seaborn.pydata.org/generated/seaborn.move_legend.html)(obj, loc, **kwargs)
  - Recrea la leyenda de una gráfica en una nueva ubicación.
```

---
## Paletas de Colores

Funciones útiles para retornar o manipular la paleta de colores de las gráficas.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [blend_palette](https://seaborn.pydata.org/generated/seaborn.blend_palette.html)(colors, n_colors=6, as_cmap=False, input='rgb')
  - Crea una paleta que difumina entre los elementos de un `list` de colores.
* - [color_palette](https://seaborn.pydata.org/generated/seaborn.color_palette.html)(palette=None, n_colors=None, desat=None, as_cmap=False)
  - Retorna un `list` de colores o _colormap_ continuos que definen una paleta. Si no se indica _palette_ se usa la paleta actual.
* - [crayon_palette](https://seaborn.pydata.org/generated/seaborn.crayon_palette.html)(colors)
  - Crea una paleta con nombres de colores de crayones Crayola.
* - [cubehelix_palette](https://seaborn.pydata.org/generated/seaborn.cubehelix_palette.html)(n_colors=6, start=0, rot=0.4, gamma=1.0, hue=0.8, light=0.85, dark=0.15, reverse=False, as_cmap=False)
  - Crea una paleta secuencial a partir del sistema _cubehelix_.
* - [dark_palette](https://seaborn.pydata.org/generated/seaborn.dark_palette.html)(color, n_colors=6, reverse=False, as_cmap=False, input='rgb')
  - Crea una paleta secuencial que difumina de oscuro a `color`.
* - [diverging_palette](https://seaborn.pydata.org/generated/seaborn.diverging_palette.html)(h_neg, h_pos, s=75, l=50, sep=1, n=6, center='light', as_cmap=False)
  - Crea una paleta divergente entre dos colores _HUSL_.
* - [hls_palette](https://seaborn.pydata.org/generated/seaborn.hls_palette.html)(n_colors=6, h=0.01, l=0.6, s=0.65, as_cmap=False)
  - Retorna tonos (h) con luminosidad (l) y saturación (s) constantes en el sistema HLS.
* - [husl_palette](https://seaborn.pydata.org/generated/seaborn.husl_palette.html)(n_colors=6, h=0.01, s=0.9, l=0.65, as_cmap=False)
  - Retorna tonos (h) con luminosidad (l) y saturación (s) constantes en el sistema _HUSL_.
* - [light_palette](https://seaborn.pydata.org/generated/seaborn.light_palette.html)(color, n_colors=6, reverse=False, as_cmap=False, input='rgb')
  - Crea una paleta secuencial que difumina de claro a `color`.
* - [mpl_palette](https://seaborn.pydata.org/generated/seaborn.mpl_palette.html)(name, n_colors=6, as_cmap=False)
  - Retorna una paleta o _colormap_ del registro de `matplotlib`.
* - [set_palette](https://seaborn.pydata.org/generated/seaborn.set_palette.html)(palette, n_colors=None, desat=None, color_codes=False)
  - Establece el ciclo de color `matplotlib` usando una paleta de `seaborn`.
* - [xkcd_palette](https://seaborn.pydata.org/generated/seaborn.xkcd_palette.html)(colors)
  - Crea una paleta con nombres de colores de tipo _xkcd_.
```

### Notas de _set_palette_

[set_palette](https://seaborn.pydata.org/generated/seaborn.set_palette.html): Establece la gama de colores de las gráficas. Se utiliza antes de la gráfica.

```python
# Establecer un estilo
set_palette(palette, n_colors=None, desat=None, color_codes=False)
```
**Parámetros:**
- **palette**: Define la paleta de colores. Puede ser:
    - Nombre de una paleta de `seaborn`: {'deep', 'muted', 'bright', 'pastel', 'dark', 'colorblind'}. Cada paleta tiene 10 colores, existen sus variantes con 6 colores si se añade un 6 al final del nombre, por ejemplo _'deep6'_.
    - Nombre de un _colormap_ de `matplotlib`. Ver {ref}`matplotlib-colormap`.
    - Un `sequence` de colores en cualquier formato que `matplotlib` acepte. Ver {ref}`matplotlib-color`.
    - {'hls', 'huls'}.
    - ‘ch:\<cubehelix arguments>’.
    - ‘light:\<color>’, ‘dark:\<color>’, ‘blend:\<color>,\<color>’.
- **n_colors** - `int`: Número de colores en la paleta.
- **desat** - `float`: Proporción para desaturar cada color.

Paleta de colores de `seaborn`:

```{code-cell} ipython3
# Imprimir cada paleta de colores
for p in sns.palettes.SEABORN_PALETTES:
    sns.set_palette(p)
    sns.palplot(sns.color_palette())
    plt.title(p)
    plt.show()
```

<br/>

---
## Widgets

Funciones útiles para inicializar widgets interactivos. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [choose_colorbrewer_palette](https://seaborn.pydata.org/generated/seaborn.choose_colorbrewer_palette.html)(data_type, as_cmap=False)
  - Selecciona una paleta del ColorBrewer `set`.
* - [choose_cubehelix_palette](https://seaborn.pydata.org/generated/seaborn.choose_cubehelix_palette.html)(as_cmap=False)
  - Inicie un widget interactivo para crear una paleta _cubehelix_ secuencial.
* - [choose_dark_palette](https://seaborn.pydata.org/generated/seaborn.choose_dark_palette.html)(input='husl', as_cmap=False)
  - Inicie un widget interactivo para crear una paleta secuencial oscura.
* - [choose_diverging_palette](https://seaborn.pydata.org/generated/seaborn.choose_diverging_palette.html)(as_cmap=False)
  - Inicie un widget interactivo para elegir una paleta de colores divergente.
* - [choose_light_palette](https://seaborn.pydata.org/generated/seaborn.choose_light_palette.html)(input='husl', as_cmap=False)
  - Inicie un widget interactivo para crear una paleta de colores secuencial _light_.
```

<br/>

---
## Temas

Funciones para modificar el estilo de las gráficas como colores, escalas, establecer elementos personalizables, etc. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [axes_style](https://seaborn.pydata.org/generated/seaborn.axes_style.html)(style=None, rc=None)
  - Recupera los parámetros que controlan el estilo general de los gráficos.
* - [plotting_context](https://seaborn.pydata.org/generated/seaborn.plotting_context.html)(context=None, font_scale=1, rc=None)
  - Recupera los parámetros que controlan la escala de los elementos de la gráfica.
* - [reset_defaults](https://seaborn.pydata.org/generated/seaborn.reset_defaults.html)()
  - Restaurs todos los parámetros _RC_ a la configuración predeterminada.
* - [reset_orig](https://seaborn.pydata.org/generated/seaborn.reset_orig.html)()
  - Restaurz todos los parámetros _RC_ a la configuración original (respeta el _RC_ personalizado).
* - [set](https://seaborn.pydata.org/generated/seaborn.set.html)(*args, **kwargs)
  - Alias ​​para `set_theme()`.
* - [set_color_codes](https://seaborn.pydata.org/generated/seaborn.set_color_codes.html)(palette='deep')
  - Modifica la forma en que se interpretan los _shorthands_ de color de `matplotlib`.
* - [set_context](https://seaborn.pydata.org/generated/seaborn.set_context.html)(context=None, font_scale=1, rc=None)
  - Establece los parámetros que controlan la escala de los elementos de la gráfica. Sirve para modificar el tamaño y grosor de las etiquetas, las líneas y otros elementos.
* - [set_style](https://seaborn.pydata.org/generated/seaborn.set_style.html)(style=None, rc=None)
  - Establece los parámetros que controlan el estilo general de los gráficos, como agregar una rendija, o los colores del fondo. Se pone antes de realizar cualquier gráfica.
* - [set_theme](https://seaborn.pydata.org/generated/seaborn.set_theme.html)(context='notebook', style='darkgrid', palette='deep', font='sans-serif', font_scale=1, color_codes=True, rc=None)
  - Establece múltiples parámetros del tema en un paso. Afecta también las gráficas de `matplotlib ` y `pandas`. Existe una alias llamado `sns.set()`, pero es preferible usar `set_theme()`. Es equivalente a usar `set_context()`, `set_style()` y `set_palette()`, entre otras caracterísitcas en una sola función.
```

### Notas de _set_context_

[set_context](https://seaborn.pydata.org/generated/seaborn.set_context.html): Establece los parámetros que controlan la escala de los elementos de la gráfica. Sirve para modificar el tamaño y grosor de las etiquetas, las líneas y otros elementos.

```python
# Establecer un contexto
set_context(context=None, font_scale=1, rc=None)
```

**Parámetros:**
- **context** - `dict`, `None` o {'paper', 'notebook', 'talk', 'poster'}: Diccionario de parámetos o algún contexto preestablecido.
    - De menor a mayor: 'paper', 'notebook', 'talk' (útil en presentaciones), 'poster'.
- **font_scale** - `float`: Factor para escalar el tamaño de manera independiente, usando como base el estilo 'notebook'.
- **rc** - `dict`: Mapeo de parámetros a modificar los valores en el estilo actual. Para conocer los parámetros y sus valores, del estilo actual, utilizar: `sns.axes_style`


### Notas de _set_style_

```python
# Establecer un estilo
sns.set_style(style=None, rc=None)
```
- _style_ - `dict` o {'darkgrid', 'whitegrid', 'dark', 'white', 'ticks'}: Estilo preconfigurado.
- _rc_ - `dict`: : Mapeo de parámetros a modificar los valores en el estilo actual. Para conocer los parámetros y sus valores, del estilo actual, utilizar: `sns.axes_style`

```{code-cell} ipython3
# Crear gráfica para cada tipo de estilo
for style in ['white','dark','whitegrid','darkgrid','ticks']:
    sns.set_style(style)
    _ = sns.histplot(tips['total_bill'])
    _.set_title(style)
    plt.show()
```

<br/>

---
## Utilidades

Otras funciones útiles para manipulación de las gráficas. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [desaturate](https://seaborn.pydata.org/generated/seaborn.desaturate.html)(color, prop)
  - Disminuye el canal de saturación de un color en un porcentaje dado.
* - [despine](https://seaborn.pydata.org/generated/seaborn.despine.html)(fig=None, ax=None, top=True, right=True, left=False, bottom=False, offset=None, trim=False)
  - Remueve los ejes (_spines_) de una gráfica (el cuadrado que rodea la gráfica), por default remueve el superior y el derecho.
* - [get_data_home](https://seaborn.pydata.org/generated/seaborn.get_data_home.html)(data_home=None)
  - Retorna la ruta al directorio caché, por ejemplo, _datasts_.
* - [get_dataset_names](https://seaborn.pydata.org/generated/seaborn.get_dataset_names.html)()
  - Retorna el nombre de todos los _datasets_ disponibles en el repositorio de `seaborn`.
* - [load_dataset](https://seaborn.pydata.org/generated/seaborn.load_dataset.html)(name, cache=True, data_home=None, **kws)
  - Carga a la sesion un dataset del repositiorio de datasets de `seaborn`.
* - [move_legend](https://seaborn.pydata.org/generated/seaborn.move_legend.html)(obj, loc, **kwargs)
  - Recrea la leyenda de una gráfica en una nueva ubicación.
* - [saturate](https://seaborn.pydata.org/generated/seaborn.saturate.html)(color)
  - Retorna un color completamente saturado con el mismo _hue_ (tono).
* - [set_hls_values](https://seaborn.pydata.org/generated/seaborn.set_hls_values.html)(color, h=None, l=None, s=None)
  - Manipula de forma independiente los canales _h_ (tono), _l_ (brillo) o _s_ (saturación) de un color.
```

<br/>

---
## Clases

En esta sección se presentan algunas clases relacionadas con hacer gráficas múltiples en una sola figura. Existen tres clases con tales fines:
- `FacetGrid`: Permite crear gráficas múltiples para cada valor de una variable categórica.
- `JointGrid`: Permite crear gráficas múltiples para la variables bivariadas, al mismo tiempo que se grafican sus marginales.
- `PairGrid`: Permite crear gráficas múltiples para la combinación de dos variables categegóricas.

---
### FacetGrid

Se utiliza para crear una malla de gráficas, cada una mostrando un subcojunto de los datos con base a los valores de una o más variables categóricas. Algunas de sus características son:
- Permite utilizar 4 tipos de gráficas diferentes.
- Permite establecer la variables categóricas tanto en las columnas, como en las filas.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [FacetGrid](https://seaborn.pydata.org/generated/seaborn.FacetGrid.html)(data, ...)
  - Crea la cuadricula para múltiples gráficas de relaciones condicionales (usar los valores de variables categóricas para separar por filas y columnas). Esta función no crea las gráficas como tal, solo prepara la cuadricula, para agregar las gráficas es necesario usar los métodos `FacetGrid.map()` y `FacetGrid.map_DataFrame()`.
```
**Parámetros**
- **`data`** - `DataFrame`: Estructura de datos de entrada.
- **`row`**, **`col`** - `str`: Etiquetas en _data_, es una variable categórica para crear subplots de acuerdo a los valores de ésta. Si se usan ambos se creará una matriz.
- **`hue`** - `str`: Etiquetas en _data_, es una variable categórica que es mapeada para determinar el color de los elementos de la gráfica.
- **`col_wrap`** - `int`: Para indicar un número máximo de columnas de gráficas a realizar, si se supera se crearán filas. Es incompatible con el parámetro _row_.
- **`height`** - `scalar`: Altura de cada _facet_ en pulgadas.
- **`aspect`** - `scalar`: Proporción entre la altura y ancho de cada _facet_ en pulgadas.
- **`palette`** - `str`, `list`, `dict`: Métodos para escoger la paleta de colores, cuando se mapea con base a _hue_.
- **`hue_order`** - `list` de `str`: Para indicar el orden de las categorías del argumento _hue_. Deben de ser los valores únicos ordenadas en orden que prefieras de _hue_.
- **`col_order`**, **`row_order`** - `list` de `str`: Los elementos de la columna/fila para indicar cómo ordenar cada uno de los valores.

**Patrones útiles**

:::{caution}
Algunos patrones aquí prensentados utilizan métodos de objetos de `matplotlib`.
:::

```python
# Asignar gráfica a una variable
g=sns.relplot()

# Cambiar título de la figura
g.fig.suptitle("New Title", y=1.03)

# Cambiar títulos de los _subplots_ (ejm cols)
g.set_titles("Template {col_name}")

# Cambiar etiquetas de los ejes
g.set(xlabel="New X Label", ylabel="New Y Label")
```

#### Uso

Para usar esta clase es necesario indicar los datos y las variables categóricas sobre las cuales de creara el _grid_ en las columnas y/o filas con _col_ y _row_ respectivaemente. Posteriormente se debe usar el método `FacetGrid.map()` para añadir las gráficas, se debe indicar la función y pasar los argumentos de la misma.

```python
# Preparar FacetGrid
g = sns.FacetGrid(data, col="col", row='row')

# Aplicar gráficas
g.map(sns.axes_plot, **kwargs)
```
- _**kwargs_ son argumentos de _axes_function_.

**Ejemplo**

```python
# Importar dataset
exercise = sns.load_dataset("exercise")

# Preparar FacetGrid
g = sns.FacetGrid(exercise, col="kind", row='diet')

# Aplicar gráficas
g.map(sns.histplot, 'pulse', color=azul)
```

<br/>

#### Atributos

Atributos de `FacetGrid`.

```{list-table}
:header-rows: 1

* - Atributos
  - Descripción
* - `FacetGrid.ax`
  - El objeto `matplotlib.axes.Axes` cuando no se asignan variables de _faceting_.
* - `FacetGrid.axes`
  - Una matriz de los objetos `matplotlib.axes.Axes` en la cuadricula.
* - `FacetGrid.axes_dict`
  - Un diccionario de los nombres de _facets_ con su correspondiente `matplotlib.axes.Axes`.
* - [FacetGrid.facet_data](https://seaborn.pydata.org/generated/seaborn.FacetGrid.facet_data.html)
  - _Generator_ de nombres y subconjuntos de datos para cada _facet_.
* - `FacetGrid.figure`
  - El objeto `matplotlib.figure.Figure` subyacente de la cuadrícula.
* - `FacetGrid.legend`
  - El objeto `matplotlib.legend.Legend`, si está presente.
```

<br/>

#### Métodos

Métodos de `FacetGrid`.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [FacetGrid.\_\_init__](https://seaborn.pydata.org/generated/seaborn.FacetGrid.__init__.html)(data,  *[,  row,  col,  hue,  col_wrap,  ...])
  - Inicializa la figura `matplotlib` y el objeto `FacetGrid`.
* - [FacetGrid.add_legend](https://seaborn.pydata.org/generated/seaborn.FacetGrid.add_legend.html)([legend_data,  title,  ...])
  - Añade una leyenda, posiblemente colocándola fuera de los ejes y cambiando el tamaño de la figura.
* - [FacetGrid.apply](https://seaborn.pydata.org/generated/seaborn.FacetGrid.apply.html)(func,  *args,  **kwargs)
  - Pasa la cuadrícula a una función proporcionada por el usuario y retorna _self_.
* - [FacetGrid.despine](https://seaborn.pydata.org/generated/seaborn.FacetGrid.despine.html)(**kwargs)
  - Remueve los _spines_ de los ejes de las _facets_.
* - [FacetGrid.facet_axis](https://seaborn.pydata.org/generated/seaborn.FacetGrid.facet_axis.html)(row_i,  col_j[,  modify_state])
  - Activa el eje identificado por los índices y lo retorna. 
* - [FacetGrid.map](https://seaborn.pydata.org/generated/seaborn.FacetGrid.map.html)(func,  *args,  **kwargs)
  - Aplica una función de trazado al subconjunto de datos de cada _facet_.
* - [FacetGrid.map_dataframe](https://seaborn.pydata.org/generated/seaborn.FacetGrid.map_dataframe.html)(func,  *args,  **kwargs)
  - Similar a  `FacetGrid.map` pero pasa _args_ como cadenas e inserta datos en _kwargs_.
* - [FacetGrid.pipe](https://seaborn.pydata.org/generated/seaborn.FacetGrid.pipe.html)(func,  *args,  **kwargs)
  - Pasa la cuadrícula a una función proporcionada por el usuario y devuelve su valor.
* - [FacetGrid.refline](https://seaborn.pydata.org/generated/seaborn.FacetGrid.refline.html)(*[,  x,  y,  color,  linestyle])
  - Agrega una(s) línea(s) de referencia a cada _facet_.
* - [FacetGrid.savefig](https://seaborn.pydata.org/generated/seaborn.FacetGrid.savefig.html)(*args,  **kwargs)
  - Almacena una imagen de la gráfica.
* - [FacetGrid.set](https://seaborn.pydata.org/generated/seaborn.FacetGrid.set.html)(**kwargs)
  - Establece atributos en cada _subplot_ `Axes`.
* - [FacetGrid.set_axis_labels](https://seaborn.pydata.org/generated/seaborn.FacetGrid.set_axis_labels.html)([x_var,  y_var,  clear_inner])
  - Establece etiquetas de los ejes en la columna izquierda y en la fila inferior de la cuadrícula.
* - [FacetGrid.set_titles](https://seaborn.pydata.org/generated/seaborn.FacetGrid.set_titles.html)([template,  row_template,  ...])
  - Dibuja títulos encima de cada _facet_ o en los márgenes de la cuadrícula.
* - [FacetGrid.set_xlabels](https://seaborn.pydata.org/generated/seaborn.FacetGrid.set_xlabels.html)([label,  clear_inner])
  - Establece las etiquetas en el eje _x_, en la fila inferior de la cuadrícula.
* - [FacetGrid.set_xticklabels](https://seaborn.pydata.org/generated/seaborn.FacetGrid.set_xticklabels.html)([labels,  step])
  - Establece las etiquetas de los _ticks_ del eje _x_ de la cuadrícula.
* - [FacetGrid.set_ylabels](https://seaborn.pydata.org/generated/seaborn.FacetGrid.set_ylabels.html)([label,  clear_inner])
  - Establece las etiquetas en el eje _y_, en la columna izquierda de la cuadrícula.
* - [FacetGrid.set_yticklabels](https://seaborn.pydata.org/generated/seaborn.FacetGrid.set_yticklabels.html)(labels=None, **kwargs)
  - Establece las etiquetas de los _ticks_ del eje _y_ en la columna izquierda de la cuadrícula
* - [FacetGrid.tick_params](https://seaborn.pydata.org/generated/seaborn.FacetGrid.tick_params.html)(axis='both', **kwargs)
  - Modifica los _ticks_, las etiquetas de los _ticks_ y las líneas de cuadrícula.
* - [FacetGrid.tight_layout](https://seaborn.pydata.org/generated/seaborn.FacetGrid.tight_layout.html)(*args,  **kwargs)
  - Llama a `fig.tight_layout`, que excluye la leyenda.
```

<br/>

---
### JointGrid

Gráficos conjuntos (relación bivariada + distribuciones marginales).

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [JointGrid](https://seaborn.pydata.org/generated/seaborn.JointGrid.html)(data=None, ...)
  - Crea la cuadrícula para generar un gráfico bivariado con gráficos univariados marginales. Esta función no crea las gráficas como tal, solo prepara la cuadricula para agregar las gráficas es necesario usar los métodos `JointGrid.plot()`, `JointGrid.plot_joint()` o `JointGrid.plot_marginals()`.
* - [jointplot](https://seaborn.pydata.org/generated/seaborn.jointplot.html)(data=None, ...)
  - Grafica la distribución bivariada y las marginales. El tipo de la gráfica bivariada se puede especificar, las marginales serán histogramas o _kde_, dependiendo de los argumentos.
```

#### Uso

Para usar esta clase es necesario indicar los datos y las variables. Posteriormente se deben usar los métodos `JointGrid.plot()`, `JointGrid.plot_joint()` o `JointGrid.plot_marginals()` para añadir las gráficas.

```python
# Preparar JointGrid 
g = sns.JointGrid(data, x='col', y='col')
# Aplicar gráficas
g.plot(sns.axes_function_join, sns.axes_function_marginal)

# Preparar JointGrid 
g = sns.JointGrid(data, x='col', y='col')
# Aplicar gráfica a la diagonal
g.plot_joint(sns.axes_function_join, **kwargs)
# Aplicar gráfica fuera de la diagonal
g.plot_marginals(sns.axes_function_marginal, **kwargs)
```
- _**kwargs_ son argumentos de _axes_function_.

**Ejemplo**

```python
# Preparar JointGrid
g = sns.JointGrid(data=iris, x="sepal_length", y="petal_length")

# Aplicar gráfica a la diagonal
g.plot_joint(sns.scatterplot, color=cafe)

# Aplicar gráfica fuera de la diagonal
g.plot_marginals(sns.histplot, kde=False, color=azul)
```

<br/>

#### Atributos

Atributos de la clase `JointGrid`.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [figure](https://seaborn.pydata.org/generated/)()
  - Retorna el objeto `matplotlib.figure.Figure` subyacente de la cuadrícula.
```


#### Métodos

Métodos de la clase `JointGrid`.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [__init__](https://seaborn.pydata.org/generated/seaborn.JointGrid.__init__.html)([data,  x,  y,  hue,  height,  ratio,  ...])
  - ConfigurA la cuadrícula de _subplots_ y almacena los datos internamente para facilitar el graficado.
* - [apply](https://seaborn.pydata.org/generated/seaborn.JointGrid.apply.html)(func,  *args,  **kwargs)
  - Pasa la cuadrícula a una función proporcionada por el usuario y retorna _self_.
* - [pipe](https://seaborn.pydata.org/generated/seaborn.JointGrid.pipe.html)(func,  *args,  **kwargs)
  - Pasa la cuadrícula a una función proporcionada por el usuario y devuelve su valor.
* - [plot](https://seaborn.pydata.org/generated/seaborn.JointGrid.plot.html)(joint_func,  marginal_func,  **kwargs)
  - Genera la gráfica pasando funciones para los `Axes` _joint_ y marginal.
* - [plot_joint](https://seaborn.pydata.org/generated/seaborn.JointGrid.plot_joint.html)(func,  **kwargs)
  - Grafica un gráfico bivariado en los `Axes` _joint_ de la cuadrícula.
* - [plot_marginals](https://seaborn.pydata.org/generated/seaborn.JointGrid.plot_marginals.html)(func,  **kwargs)
  - Genera los gráficos univariados en cada eje marginal.
* - [refline](https://seaborn.pydata.org/generated/seaborn.JointGrid.refline.html)(*[,  x,  y,  joint,  marginal,  color,  ...])
  - Agrega una(s) línea(s) de referencia a cada _facet_.
* - [savefig](https://seaborn.pydata.org/generated/seaborn.JointGrid.savefig.html)(*args,  **kwargs)
  - Almacena una imagen de la gráfica.
* - [set](https://seaborn.pydata.org/generated/seaborn.JointGrid.set.html)(**kwargs)
  - Establece atributos en cada _subplot_ `Axes`.
* - [set_axis_labels](https://seaborn.pydata.org/generated/seaborn.JointGrid.set_axis_labels.html)([xlabel,  ylabel])
  - Establece etiquetas de los ejes en la columna izquierda y en la fila inferior de la cuadrícula.
```

<br/>

---
### PairGrid

Matrices de gráficos bivariados entre todas las combinaciones de variables numéricas.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [PairGrid](https://seaborn.pydata.org/generated/seaborn.PairGrid.html)(data, ...)
  - Crea la cuadricula para múltiples gráficas de relaciones en pares. Esta función no crea las gráficas como tal, solo prepara la cuadricula, para agregar las gráficas es necesario usar los métodos `PairGrid.map()`, `PairGrid.map_diag()` y `PairGrid.map_offdiag()`.
* - [pairplot](https://seaborn.pydata.org/generated/seaborn.pairplot.html)(data, ...)
  - Grafica relaciones en pares de variables de un _dataset_, generando una matriz de gráficas. Se puede especificar tanto el tipo de gráfica de la relación de cada par, como las de la diagonal de la matriz.
```

#### Uso

Para usar esta clase es necesario indicar los datos y las variables categóricas sobre las cuales de creara el _grid_ en las columnas y filas con _vars_. Posteriormente se deben usar los métodos `PairGrid.map()`, `PairGrid.map_diag()` o `PairGrid.map_offdiag()` para añadir las gráficas.

```python
# Preparar PairGrid 
g = sns.FacetGrid(data, vars=['row', 'col'])
# Aplicar misma gráfica a todas las celdas
g.map(sns.axes_function, **kwargs)

# Preparar PairGrid
g = sns.FacetGrid(data, vars=['row', 'col'])
# Aplicar gráfica a la diagonal
g.map_diag(sns.axes_function, **kwargs)
# Aplicar gráfica fuera de la diagonal
g.map_offdiag(sns.axes_function, **kwargs)
```
- _**kwargs_ son argumentos de _axes_function_.

**Ejemplo**

```python
# Importar dataset
iris = sns.load_dataset("iris")

# Preparar PairGrid 
g = sns.PairGrid(iris)

# Aplicar gráfica a la diagonal
g.map_diag(sns.kdeplot, color=cafe)

# Aplicar gráfica fuera de la diagonal
g.map_offdiag(sns.scatterplot, color=azul)
```

<br/>

#### Atributos

Atributos de la clase `PairGrid`.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [PairGrid.figure](https://seaborn.pydata.org/generated/)
  - Retorna el objeto `matplotlib.figure.Figure` subyacente de la cuadrícula.
* - [PairGrid.legend](https://seaborn.pydata.org/generated/)
  - El objeto `matplotlib.legend.Legend`, si está presente.
```

<br/>

#### Métodos

Métodos de la clase `PairGrid`.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [PairGrid.__init__](https://seaborn.pydata.org/generated/seaborn.PairGrid.__init__.html)(data,  *[,  hue,  vars,  x_vars,  ...])
  - Inicializa la figura `matplotlib` y el objeto `PairGrid`.
* - [PairGrid.add_legend](https://seaborn.pydata.org/generated/seaborn.PairGrid.add_legend.html)([legend_data,  title,  ...])
  - Añade una leyenda, posiblemente colocándola fuera de los ejes y cambiando el tamaño de la figura.
* - [PairGrid.apply](https://seaborn.pydata.org/generated/seaborn.PairGrid.apply.html)(func,  *args,  **kwargs)
  - Pasa la cuadrícula a una función proporcionada por el usuario y retorna _self_.
* - [PairGrid.map](https://seaborn.pydata.org/generated/seaborn.PairGrid.map.html)(func,  **kwargs)
  - Grafica con la misma función en cada _subplot_.
* - [PairGrid.map_diag](https://seaborn.pydata.org/generated/seaborn.PairGrid.map_diag.html)(func,  **kwargs)
  - Gráfica con una función univariada en cada _subplot_ diagonal.
* - [PairGrid.map_lower](https://seaborn.pydata.org/generated/seaborn.PairGrid.map_lower.html)(func,  **kwargs)
  - Gráfica con una función bivariada en los _subplots_ diagonales inferiores.
* - [PairGrid.map_offdiag](https://seaborn.pydata.org/generated/seaborn.PairGrid.map_offdiag.html)(func,  **kwargs)
  - Gráfica con una función bivariada en los _subplots_ fuera de la diagonal.
* - [PairGrid.map_upper](https://seaborn.pydata.org/generated/seaborn.PairGrid.map_upper.html)(func,  **kwargs)
  - Gráfica con una función bivariada en los _subplots_ diagonales superiores.
* - [PairGrid.pipe](https://seaborn.pydata.org/generated/seaborn.PairGrid.pipe.html)(func,  *args,  **kwargs)
  - Pasa la cuadrícula a una función proporcionada por el usuario y devuelve su valor.
* - [PairGrid.savefig](https://seaborn.pydata.org/generated/seaborn.PairGrid.savefig.html)(*args,  **kwargs)
  - Almacena una imagen de la gráfica.
* - [PairGrid.set](https://seaborn.pydata.org/generated/seaborn.PairGrid.set.html)(**kwargs)
  - Establece atributos en cada _subplot_ `Axes`.
* - [PairGrid.tick_params](https://seaborn.pydata.org/generated/seaborn.PairGrid.tick_params.html)([axis])
  - Modifica los _ticks_, las etiquetas de los _ticks_ y las líneas de cuadrícula.
* - [PairGrid.tight_layout](https://seaborn.pydata.org/generated/seaborn.PairGrid.tight_layout.html)(*args,  **kwargs)
  - Llama a `fig.tight_layout`, que excluye la leyenda.
```