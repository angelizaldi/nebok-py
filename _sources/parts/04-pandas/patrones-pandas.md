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

# Patrones útiles

En esta sección se presentan y explican algunos patrones útiles al trabajar con objetos de `pandas`.

---
## Data Cleaning

### Categorías inconsistentes

Para encontrar las filas que contiene cagorías incorrectas en una columna categórica, con base a un conjunto de categorías correctas utilzar el siguiente patrón:

```python
# Determinar categorías inconsistentes
inconsistent_categories = set(df['cat_col']).difference(categories)

# Imprimir filas con categorías inconsistentes
inconsistent_rows = df['cat_col'].isin(inconsistent_categories) 
display(df[inconsistent_rows])

# Opcionalmente, eliminar filas inconsistentes
df_consistent = df[~inconsistent_rows]
```
- _categories_ debe ser un `array-like` con las categorías correctas únicas.

<br/>

### Categorización de una variable

Si se desea convertir una columna numérica en una variable categórica con base a rangos continuos de los valores. Existen dos opciones:

`pandas.qcut()` - `Categorical`, `series` o `ndarray`: Divide una columna en _q_ categorías, basado en cuantiles. Produce una variable categórica para indicar a cuál cuantil pertenece. Garantiza _bins_ del mismo tamaño.

```python
# Opción 1: qcut()
df['cat_column'] = pd.qcut(df['numeric_col'], q, labels=None, retbins=False)
```
- **`q`** \- `int` o `list-like` de `float: [0, 1]`:
    - Si es entero es el número de cuantiles.
    - Si es una lista, los los extremos de cada categoría. Por ejemplo para cuartiles sería `[0, .25, .5, .75, 1]`.
- **`labels`** \- `array`, `False`, `None`: Los nombres de las categorías.
    - `array`: Tiene que tener la misma longitud que los bins/cuantiles resultantes (_q_ o `len(q)`).
    - `False`: Retorna valores enteros que indican el cuantil al que pertenecen.
    - `None`: Retorna los bins (rangos de cada cuantil).
- **`retbins`** \- `bool`: Para retornar el bin (rango del cuantil) y la etiqueta juntos.

<br/>

`pandas.cut()` - `Categorical`, `series` o `ndarray`: Crea categorías de acuerdo a qué rango pertenece un valor. Las categorías estarán jerarquizadas. No garantiza que cada _bin_ tenga el mismo número de _data points_.

```python
# Opción 2: cut()
bins = [0,200000,500000,np.inf]
df['cat_column'] = pd.cut(df['numeric_col'], bins, right = True, labels = None, retbins = False, include_lowest = False, precision = 3)
```
- **`bins`** \- `int`, `sequence` de `scalar`: Criterio para crear las categorías.
    - `int`: Define el número de categorías del mismo anchos, en _df_.
    - `sequence`: Definine los extremos de cada _bin_. Por ejemplo `[0, 10, 20]`, crearía rangos de _(0,10)_ y _(10, 20)_`.
- **`right`** \- `bool`: Indica si el extremo superior sea incluído o no.
- **`labels`** \- `array-like`, `False`, `None`: Los nombres de las categorías.
    - `array`: Tiene que tener la misma longitud que los bins resultantes (_bins_ o `len(bins)-1`).
    - `False`: Retorna valores enteros que indican el _bin_ al que pertenecen.
    - `None`: Retorna los _bins_ (rangos de cada cuantil).
    - IMPORTANTE: Si `labels=None`, como quiera se puede acceder a los rangos de cada _bin_ con `df.code` y la numeráción (como si `labels=False`) con `df.categories`
- **`retbins`** \- `bool`: Para indicar que se retorne el _bin_ (rango del cuantil) y la etiqueta juntos.
- **`include_lowest`** \- `bool`: Para indicar si incluir el extremo inferior.
- **`precision`** \- `int`: Número de décimales a usar en los rangos de los bines cuando _bins_ es `int`.

### Mapeo de categorias

Si se tiene una columna categórica y se quiere renombrarlas o colapsarlas a otras categorías se puede hacer uso de los métodos `.replace()` o `.map()`:

```python
# Crear diccionario con el mapeo
mapping = {'cat1':'new_cat1', 'cat2':'new_cat2', ...}

# Aplicar mapeo
devices['new_cat_col'] = df['cat_col'].replace(mapping)

# Lo anterior equivale a
devices['new_cat_col'] = df['cat_col'].map(mapping)
```
- Ambos métodos funcionan igual solo cuando se proporciona un diccionario.

<br/>

---
## Fechas y tiempos

## Establecer o modificar una zona horaria:

En un `Series` que sea de tipo `datetime64` es posible establecer o modifcar la zona horaria, ya que manteniendo la misma información o ajustándola a la nueva zona horaria:
- Para mantener usar el método `tz_localize()` del _accesor_ `dt`.
- Para modificar usar el método `tz_convert()` del _accesor_ `dt`.

```python
# Establecer una zona horaria sin modificar la hora
Series.dt.tz_localize(tz).

# Establecer una zona horaria modificando la hora
Series.dt.tz_convert(tz).
```
- _tz_ - `str`, `pytz.timezone`, `dateutil.tz.tzfile`, `datetime.tzinfo` or `None`: Zona horaria. Ver {ref}`datetime-zonas-horarias`. Si se usa `None` se elimina la zona horaria que tenía.
- Estos métodos son similares a los métodos `datetime.replace` y `datetime.astimezone` del módulo `datetime`.


---
## Series de tiempo

(cookbook-resampling)=
### Cambiar frecuencia de una Serie de Tiempo (resampling)

Una serie de tiempo normalmente tendrá un índice de tipo `datetime-like`. Existen dos opciones principales para cambiar la frecuencia.

**Importante**: Para los ejemplos de esta sección se utilizará el siguiente `Series`:

```{code-cell} ipython3
# Importar librerias
import pandas as pd
from numpy.random import default_rng

# Crear índice
ind = pd.date_range('01/01/2024', '31/01/2024', freq = '2D')

# Generar datos
rng = default_rng()
data = rng.normal(100, 8, len(ind))

# Crear e imprimir el Series
s = pd.Series(data, index=ind)
print(s)
```
- Notar que la serie tiene una frecuencia de 2 días.

#### Upsampling

Se refiere a pasar de una unidad más grande a unidades más pequeñas, como de meses a días. Implica que se generarán valores perdidos _NA_. Los cuales se pueden rellenar o interpolar, por default se dejan los valores vacíos. Existen tres estrategias para hacer _upsampling_:
1. Utilizar el método [.asfreq()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.asfreq.html).
2. Utilizar el método [.resample()](http://pandas.pydata.org/docs/reference/api/pandas.DataFrame.resample.html#pandas.DataFrame.resample). 
3. También se puede usar `.reindex()` pasando un índice con la nueva frecuencia y para rellenar valores perdidos es se pueden usar los métodos para valores nulos de `Series` o `DataFrame`.

La plantilla básica para usar cualquiera de las primeras dos estrategias son:
```python
# Con .asfreq()
X.asfreq(freq)
# Rellenar valores NA
X.asfreq(freq, method, fill_value) #Solo se pone uno de los dos

# Con .resample()
X.resample(freq).asfreq(fill_value) # si no se indica fillvalue se mantendrán los NA.
# Rellenar valores NA
X.resample(freq).fillna() #Ejemplo con filla(), existen más métodos
```
- Para rellenar valores dependerá de la estrategia que se haya utilizado:
    1. `asfreq()`: Se utiliza los argumentos _method_ o _fill\_value_.
    2. `resample()`: Utilizar los {ref}`métodos <pandas-resampler-methods-upsamplig>`, como por ejemplo `asfreq()`, `fillna()`, `interpolate()`, etc. 

<br/>

**Ejemplo**: A continuación veremos como aplicar _upsampling_ pasando de una frecuencia de cada dos días a diario:

```{code-cell} ipython3
# Upsampling con .asfreq
s_u1 = s.asfreq('1D', method='pad')
print(s_u1, end='\n'*2)

# Upsampling con .resample().interpolate()
s_u2 = s.resample('1D').interpolate()
print(s_u2, end='\n'*2)
```
- Recordar que si se usa `.resample` existen más {ref}`métodos <pandas-resampler-methods-upsamplig>` para rellenar los valores perdidos, por ejemplo, también se pudo haber usado `X.resample('1D').asfreq(100)` para rellenar los _NaN_ con 100.

#### Downsampling

Se refiere a pasar de una unidad más pequeña  a una más grande, como de días a meses, en este caso será necesario hacer _aggregates_. Se utiliza el método [.resample()](http://pandas.pydata.org/docs/reference/api/pandas.DataFrame.resample.html#pandas.DataFrame.resample). Es similar a un _groupby_, posteriormente se debe usar un método de _aggregate_ como `.first()`, `.last()`, etc. o `.agg()` para el caso de más de una función:
```python
# Downsampling con un aggregate
X.resample(freq).mean() # Ejemplo con .mean().

# Downsampling con múltiples aggregates
X.resample(freq).agg(['func1', 'func2'])  #Ejemplo de dos aggregates
```
- También es posible usar el método `.asfreq(freq)` pero en este caso no se hará un _aggregate_, sino que se seleccionaran las observaciones de acuerdo a la frecuencia indicada.

<br/>

**Ejemplo**: A continuación veremos como aplicar _downsampling_ pasando de una frecuencia de cada dos días a cada 7 días (1 semana):

```{code-cell} ipython3
# Upsampling con .resample().mean()
s.resample('1W').mean()
```
- El resultado hubiera sido el mismo si se hubiera usado como _offset_ la cadena `'7D'`.
- Recordar que existen más {ref}`métodos <pandas-resampler-methods-aggregate>` para calcular el _aggregate_, o que incluso se pueden calcular más de un {ref}`aggregate <pandas-resampler-methods-apply>` al mismo tiempo.

<br/>

### Shifting

Se pueden desfasar los valores en una serie de tiempo con el método [.shift()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.shift.html) el cual se debe indicar cuántos periodos desfasar, los cuales pueden ser positivos o negativos, y adicionalmente se pueden indicar una frecuencia en particular, en caso de que se indique una frecuencia, los datos originales se preservan y se desfasa la serie de tiempo. Ejemplos:

```{code-cell} ipython3
# shift simple
print(s.shift(3).head(), end='\n'*2)

# shift indicando una frecuencia
s.shift(3, freq='D').head()
```
