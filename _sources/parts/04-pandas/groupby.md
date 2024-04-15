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

# GroupBy

Los objetos `SeriesGroupBy` y `DataFrameGroupBy` son unos objetos retornados al usar el método `.groupby()` ya sea con `DataFrame` o `Series`,  si solo se llama el método sin especificar ninguna función de _aggregate_, como tal no se calculará nada, salvo los datos intermedios de la llave de agrupación, es decir se determinarán las llaves y los datos de cada grupo.

El tipo retornado retornado por `.groupby()` dependerá de:
- Retorna `SeriesGroupBy`:
    - Si el método `.groupby()` se aplica a un `Series` o si se selecciona una columna en concreto después agrupar un `DataFrame`.
- Retorna `DataFrameGroupBy`:
    - Si el método `.groupby()` se aplica a un `DataFrame` o un subconjunto de columnas (al menos dos columnas).

```{code-cell} ipython3
# Importar libreria
import pandas as pd

# Create a DataFrame
df = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar'],
                   'B': [1, 2, 3, 4],
                   'C': [5, 6, 7, 8]})

# Agrupar por la columna 'A' en todo el dataframe
grouped_df = df.groupby('A')

# Agrupar por la columna 'A' en una columna en particular
grouped_series = df.groupby('A')['B']

print(type(grouped_df))

print(type(grouped_series ))	
```

Conceptualmente los objetos de tipo _GroupBy_ se pueden entender como un `DataFrame-like` donde las columnas tiene como índice las columnas del objeto original, el índice de las filas (que potencialmente puede ser un multi-índice) tendrá como etiquetas los _keys_ de los grupos y los elementos son `array-like` de una dimensión que son particiones del objeto original dada la columna y el _key_. Tener en cuenta que los elementos de cada `array-like` conservan los índices de fila del objeto original.

```{figure} ../images/groupby.png
:name: DataFrameGroupBy-image
:width: 700px
:align: center

Conceptualización de un objeto `DataFrameGroupBy`.
```

Al aplicar una función al objeto _GroupBy_ se aplica la función a cada `array-like` interno.

:::{warning}
La explicación anterior solo es para conceptualizar un objeto _GroupBy_ y no significa que en la práctica dicha estructura existe.
:::

Estos objetos tienen sus propios métodos, la mayoría son similares a los de `DataFrame` o `Series` pero algunos tienen un comportamiento ligeramente diferente.


```{note}
Para más información consultar la [documentación](https://pandas.pydata.org/docs/reference/groupby.html) de `pandas`.
```

```{tip}
Todos los métodos de `Series` y `DataFrame` se pueden usar con el objeto _GroupBy_.
```

<br/>

---
## Iteración sobre _GroupBy_

Los objetos de tipo _Groupby_ son iterables en un `for loop`, en esencia retorna un `tuple`, en el que el primer elemento es el nombre del grupo y el segundo es el grupo `Series` o `DataFrame`:
```python
# Iteración en un _GroupBy_
for name, group in df.groupby('key1'):
    # for body
```
- _name_, _group_ son nombre opcionales.
- `'key1'` es una columna categórica en _df_.

El caso de que se especifiquen dos o más keys entonces se retornará un `tuple` de _keys_:
```python
# Iteración en un _GroupBy_ con múltiples keys
for (k1, k2), group in X.groupby(['key1', 'key2']):
    # for body
```
- _name_, _group_ son nombre opcionales.
- `'key1'`, `'key2'` son columnas categóricas en _df_.

<br/>

---
## Convertir _GroupBy_ a `dict`

Un objeto de tipo _GroupBy_ se puede convertir a lista o a un diccionario, los _keys_ serán los valores únicos de las llaves con las que se se agrupó el `DataFrame` y los values será el `DataFrame`/`Series` con los datos de cada grupo:
```python
# Convertir "GroupBy" a dict
dict(list(df.groupby('key1')))
```
- `'key1'` es una columna categórica en _df_.

<br/>

---
## Selección de elementos

El objeto retornado por `.groupby()` se pueden entender como si fuera un `DataFrame-like`  entonces cualquier técnica de selección de columnas de esos objetos (seleccionar columnas para todos los grupos) funciona con _GroupBy_, por ejemplo: 

- Para acceder a una columna completa \- `SeriesGroupBy`:  <br> `grouped_object['col']`
- Para acceder a una columna completa \- `DataFrameGroupBy`:  <br> `grouped_object[['col']]`
- Para acceder a más de una columna completa \- `DataFrameGroupBy`: <br> `grouped_object[['col1', 'col2', ...]]`

Para seleccionar una fila concreta, que equivaldría a seleccionar un grupo para todas las columnas se puede usar el método `.get_group()` para `SeriesGroupBy` y `DataFrameGroupBy`.


**Ejemplos**:
```python
df = pd.DataFrame({'A': ['x', 'x', 'y', 'z', 'y'], 'B': [1, 1, 2, 3, 2], 'C': [1, 2, 3, 4, 5]})

df_grouped = df.groupby('A')

print(df_grouped['B'].get_group('y').mean())

print(df_grouped.get_group('y')[['B', 'C']].mean())
```
- No importa si primero se elige el grupo y después el conjunto de columnas o viceversa


Se pueden combinar ambas estrategias para seleccionar elementos específicos del objeto _GroupBy_ o subcojuntos del mismo.

<br/>

---
## Métodos

### `DataFrameGroupBy`

Métodos del objeto `DataFrameGroupBy`.


#### Cálculos

##### Aggregates

:::{note}
Estos métodos ignoran valores `NA`/`NaN`, a menos de que se indique lo contrario.
:::

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [DataFrameGroupBy.agg](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.DataFrameGroupBy.agg.html)([func, engine, ...])
  - Calcula _aggregates_ a los valores de cada grupo. Es posible específicar más una función de agregación e incluso se pueden aplicar diferentes _aggregates_ a diferentes columnas (con `dict`). Los _aggregates_ se pueden definir como `str` (`'min'`, `'mean'`, etc) o como `functions` (`max`, `np.mean`, etc.).
* - [DataFrameGroupBy.aggregate](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.DataFrameGroupBy.aggregate.html)([func, engine, ...])
  - Calcula _aggregates_ a los valores de cada grupo. Es posible específicar más una función de agregación e incluso se pueden aplicar diferentes _aggregates_ a diferentes grupos.
* - [DataFrameGroupBy.count](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.DataFrameGroupBy.count.html)()
  - Calcula el recuento de elementos en cada grupo.
* - [DataFrameGroupBy.prod](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.DataFrameGroupBy.prod.html)([numeric_only, min_count])
  - Calcula el producto de los valores en cada grupo.
* - [DataFrameGroupBy.size](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.DataFrameGroupBy.size.html)()
  - Calcula el tamaño de los grupos. Incluye valores nulos.
* - [DataFrameGroupBy.sum](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.DataFrameGroupBy.sum.html)([numeric_only, ...])
  - Calcula la suma de los valores en cada grupo.
```

:::{caution}
Para funciones como `.mean()`, `.std()`, etc. consultar los métodos de {ref}`groupby-dataframe-metodos-estadisticas`.
Para conteo de valores único revisar los métodos de {ref}`Valores únicos <groupby-dataframe-metodos-valores-unicos>`.
:::

<br/>

##### Booleanos

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [DataFrameGroupBy.all](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.DataFrameGroupBy.all.html)([skipna])
  - Retorna `True` si todos los valores del grupo son `True`, `False` en caso contrario, para cada grupo.
* - [DataFrameGroupBy.any](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.DataFrameGroupBy.any.html)([skipna])
  - Retorna `True` si al menos un valor en el grupo es `True`, `False` en caso contrario, para cada grupo.
```

<br/>

##### Cálculos acumulados, diferencias, cambios porcentuales y rank

:::{note}
Estos métodos ignoran valores `NA`/`NaN`, a menos de que se indique lo contrario.
:::

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [DataFrameGroupBy.cumcount](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.DataFrameGroupBy.cumcount.html)([ascending])
  - Enumera cada elemento en cada grupo desde 0 hasta la longitud de ese grupo. El objeto retornado es un `Series`/`DataFrame` con el índice del objeto original y los valores son las enumeraciones de los elementos con respecto a su grupo. 
* - [DataFrameGroupBy.cummax](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.DataFrameGroupBy.cummax.html)([axis, numeric_only])
  - Determina el valor máximo hasta ese elemento en cada grupo. El objeto retornado es un `Series`/`DataFrame` con el índice del objeto original y los valores son los valores máximos hasta ese elemento con respecto a su grupo. 
* - [DataFrameGroupBy.cummin](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.DataFrameGroupBy.cummin.html)([axis, numeric_only])
  - Determina el valor mínimo hasta ese elemento en cada grupo. El objeto retornado es un `Series`/`DataFrame` con el índice del objeto original y los valores son los valores mínimo hasta ese elemento con respecto a su grupo. 
* - [DataFrameGroupBy.cumprod](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.DataFrameGroupBy.cumprod.html)([axis])
  - Determina el producto acumulado hasta ese elemento en cada grupo. El objeto retornado es un `Series`/`DataFrame` con el índice del objeto original y los valores es el producto acumulado hasta ese elemento con respecto a su grupo. 
* - [DataFrameGroupBy.cumsum](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.DataFrameGroupBy.cumsum.html)([axis])
  - Determina la suma acumulada hasta ese elemento en cada grupo. El objeto retornado es un `Series`/`DataFrame` con el índice del objeto original y los valores es la suma acumulada hasta ese elemento con respecto a su grupo.
* - [DataFrameGroupBy.diff](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.DataFrameGroupBy.diff.html)([periods, axis])
  - Determina la diferencia de cada elemento con el antererior en cada grupo. El objeto retornado es un `Series`/`DataFrame` con el índice del objeto original y los valores son la diferencia hasta ese elemento con respecto a su grupo.
* - [DataFrameGroupBy.ngroup](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.DataFrameGroupBy.ngroup.html)([ascending])
  - Numera cada grupo desde 0 hasta el _número\_de\_grupos - 1_.
* - [DataFrameGroupBy.pct_change](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.DataFrameGroupBy.pct_change.html)([periods, ...])
  - Determina el cambio porcentual de cada elemento con el antererior en cada grupo. El objeto retornado es un `Series`/`DataFrame` con el índice del objeto original y los valores son el cambio porcentual hasta ese elemento con respecto a su grupo.
* - [DataFrameGroupBy.rank](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.DataFrameGroupBy.rank.html)([method, ascending, ...])
  - Determina el ranking de cada elemento en cada grupo. El objeto retornado es un `Series`/`DataFrame` con el índice del objeto original y los valores son el ranking de ese elemento con respecto a su grupo.
```

<br/>

(groupby-dataframe-metodos-estadisticas)=
##### Estadísticas

Métodos para cálculos estadísticos y _OHLC_.

:::{note}
Estos métodos ignoran valores `NA`/`NaN`, a menos de que se indique lo contrario.
:::

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [DataFrameGroupBy.corr](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.DataFrameGroupBy.corr.html)([method, min_periods, ...])
  - Calcula la correlación por pares de columnas de cada _key_.
* - [DataFrameGroupBy.corrwith](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.DataFrameGroupBy.corrwith.html)(other[, axis, ...])
  - Calcula la correlación por pares de columnas conn otro objeto.
* - [DataFrameGroupBy.cov](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.DataFrameGroupBy.cov.html)([min_periods, ddof, ...])
  - Calcula la covarianza por pares de columnas de cada _key_.
* - [DataFrameGroupBy.describe](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.DataFrameGroupBy.describe.html)([percentiles, ...])
  - Generar estadísticas descriptivas para cada grupo. Se recomienda usar solo si el objeto tiene pocas columnas y/o pocos _keys_.
* - [DataFrameGroupBy.mean](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.DataFrameGroupBy.mean.html)([numeric_only, ...])
  - Calcula la media de los grupos.
* - [DataFrameGroupBy.median](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.DataFrameGroupBy.median.html)([numeric_only])
  - Calcula la mediana de los grupos.
* - [DataFrameGroupBy.ohlc](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.DataFrameGroupBy.ohlc.html)()
  - Calcula los valores de apertura, máximo, mínimo y cierre para los elementos de cada grupo, excluyendo los valores faltantes. Retorna un `DataFrame` (potencialmente `MultiIndex`). Los valores se determinan por el orden del índice.
* - [DataFrameGroupBy.sample](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.DataFrameGroupBy.sample.html)([n, frac, replace, ...])
  - Devuelva una muestra aleatoria de elementos de cada grupo.
* - [DataFrameGroupBy.sem](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.DataFrameGroupBy.sem.html)([ddof, numeric_only])
  - Calcula el error estándar de la media de los grupos.
* - [DataFrameGroupBy.skew](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.DataFrameGroupBy.skew.html)([axis, skipna, ...])
  - Retorna el sesgo dentro de los grupos.
* - [DataFrameGroupBy.std](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.DataFrameGroupBy.std.html)([ddof, engine, ...])
  - Calcula la desviación estándar de los grupos.
* - [DataFrameGroupBy.var](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.DataFrameGroupBy.var.html)([ddof, engine, ...])
  - Calcula la varianza de los grupos.
```

<br/>

##### Estadísticos de orden

:::{note}
Estos métodos ignoran valores `NA`/`NaN`, a menos de que se indique lo contrario.
:::

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [DataFrameGroupBy.idxmax](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.DataFrameGroupBy.idxmax.html)([axis, skipna, ...])
  - Retorna el índice del valor máximo sobre el eje solicitado por grupo.
* - [DataFrameGroupBy.idxmin](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.DataFrameGroupBy.idxmin.html)([axis, skipna, ...])
  - Retorna el índice del valor mínimo sobre el eje solicitado por grupo.
* - [DataFrameGroupBy.max](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.DataFrameGroupBy.max.html)([numeric_only, ...])
  - Calcular el máximo de valores de grupo.
* - [DataFrameGroupBy.min](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.DataFrameGroupBy.min.html)([numeric_only, ...])
  - Calcula el mínimo de valores del grupo.
* - [DataFrameGroupBy.quantile](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.DataFrameGroupBy.quantile.html)([q, ...])
  - Retorna valores de grupo en el cuantil dado, al estilo numpy.percentile.
```

<br/>

##### Series de tiempo

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [DataFrameGroupBy.resample](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.DataFrameGroupBy.resample.html)(rule, *args[, ...])
  - Modifica la frecuencia de una serie de tiempo por grupo, útil si se realizará un _aggregate_ con la nueva frecuencia. El objeto debe de tener un índice `datetime-like` o pasar valores `datetime-like` al argumento `on` o `level`. **IMPORTANTE**: Este método retorna un objeto `Resampler`, que tiene otros métodos como `Resampler.asfreq()` o _aggregates_ como `Resampler.mean()`.
* - [DataFrameGroupBy.shift](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.DataFrameGroupBy.shift.html)([periods, freq, ...])
  - Desplaza el índice según el número deseado de períodos con una frecuencia de tiempo opcional.
```

<br/>

#### Funciones rolling, aplicar, pipe, mapeos y transformaciones

Lorem ipsum dolor sit amet, consectetur adipiscing elit. 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [DataFrameGroupBy.apply](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.DataFrameGroupBy.apply.html)(func, *args[, ...])
  - Aplica la función `func` a cada grupo y combina los resultados. La función debe recibir un grupo y retornar el grupo modificado o un escalar.
* - [DataFrameGroupBy.pipe](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.DataFrameGroupBy.pipe.html)(func, *args, **kwargs)
  - Encadena un conjunto de funciones que deben de recibir y retornar (excepto la última) objetos de tipo _GroupBy_.
* - [DataFrameGroupBy.rolling](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.DataFrameGroupBy.rolling.html)(*args, **kwargs)
  - Provee calculos en ventanas moviles de datos por grupo. El objeto retornado es un `Series`/`DataFrame` con `MultiIndex` de los _keys_ de los grupos y los índices originales de los elementos aplicando la ventana a los elementos de cada grupo. 
* - [DataFrameGroupBy.transform](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.DataFrameGroupBy.transform.html)(func, *args[, ...])
  - Aplica la función `func` a cada grupo, pero manteniendo el _shape_ e índice del objeto original. Básicamente en el objeto original mapea a los valores el resultado de `func` de su respectivo grupo. La función debe de recibir un grupo y retornar el grupo transformado.
```

<br>

---
#### Gráficas

Gráficas. 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [DataFrameGroupBy.boxplot](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.DataFrameGroupBy.boxplot.html)([subplots, column, ...])
  - Crea diagramas de caja a partir de los datos de `DataFrameGroupBy`. Crea un _subplots_ por cada grupo y un diagrama por cada columna.
* - [DataFrameGroupBy.hist](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.DataFrameGroupBy.hist.html)([column, by, grid, ...])
  - Crea histogramas a partir de los datos de `DataFrameGroupBy`. Crea _subplots_ por cada grupo y diagrama por cada columna.
* - [DataFrameGroupBy.plot](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.DataFrameGroupBy.plot.html)()
  - Crea gráficas a partir de los datos de `DataFrameGroupBy`. Crea _subplots_ por cada grupo y diagrama por cada columna.
```

<br>

---
#### Selección, filtrado e iteración de elementos

Métodos para seleccionar elementos/filas concretas, filtrar los grupos o iterar sobre ellos. 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [DataFrameGroupBy.\_\_iter__](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.DataFrameGroupBy.__iter__.html)()
  - Iterador de grupo.
* - [DataFrameGroupBy.filter](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.DataFrameGroupBy.filter.html)(func[, dropna])
  - Filtra grupos que no cumplan cierto criterio (los valores con lo que `func` retorna `False`), la función recibe cada grupo.
* - [DataFrameGroupBy.first](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.DataFrameGroupBy.first.html)([numeric_only, ...])
  - Determina el primer valor de cada columna dentro de cada grupo.
* - [DataFrameGroupBy.get_group](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.DataFrameGroupBy.get_group.html)(name[, obj])
  - Retorna `DataFrame` del grupo con el nombre proporcionado.
* - [DataFrameGroupBy.groups](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.DataFrameGroupBy.groups.html)()
  - Retorna un diccionario donde los _keys_ son el nombre del grupo y los valores es un `list-like` con las etiquetas de filas de los elementos del grupo `{nombre del grupo: etiquetas de grupo}`.
* - [DataFrameGroupBy.head](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.DataFrameGroupBy.head.html)([n])
  - Retorna las primeras _n_ filas de cada grupo.
* - [DataFrameGroupBy.indices](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.DataFrameGroupBy.indices.html)()
  - Retorna un diccionario donde los _keys_ son el nombre del grupo y los valores es un `list-like` con los índices de filas de los elementos del grupo `{nombre del grupo: etiquetas de grupo}`.
* - [DataFrameGroupBy.last](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.DataFrameGroupBy.last.html)([numeric_only, ...])
  - Determina el último valor de cada columna dentro de cada grupo.
* - [DataFrameGroupBy.nth](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.DataFrameGroupBy.nth.html)()
  - Retorna la enésima fila de cada grupo si _n_ es `int` , de lo contrario retorna un subconjunto de filas por cada grupo.
* - [DataFrameGroupBy.tail](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.DataFrameGroupBy.tail.html)([n])
  - Retorna las últimas _n_ filas de cada grupo.
* - [DataFrameGroupBy.take](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.DataFrameGroupBy.take.html)(indices[, axis])
  - Retorna los elementos en los índices posicionales dados en cada grupo.
```

<br/>


#### Valores nulos

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [DataFrameGroupBy.bfill](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.DataFrameGroupBy.bfill.html)([limit])
  - Reemplaza los valores `NA/NaN` utilizando la siguiente observación válida, en el eje indicado, en cada grupo.
* - [DataFrameGroupBy.ffill](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.DataFrameGroupBy.ffill.html)([limit])
  - Reemplaza los valores `NA/NaN` utilizando la última observación válida, en el eje indicado, en cada grupo.
```

<br/>

#### Valores únicos

```{list-table}
:header-rows: 1
:name: groupby-dataframe-metodos-valores-unicos

* - Método
  - Descripción
* - [DataFrameGroupBy.nunique](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.DataFrameGroupBy.nunique.html)([dropna])
  - Retorna `DataFrame` con recuentos de elementos únicos en cada grupo.
* - [DataFrameGroupBy.value_counts](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.DataFrameGroupBy.value_counts.html)([subset, ...])
  - Retorna el recuento de filas únicas para cada grupo. Se puede elegir un subcojunto de columas para determinar las filas únicas.
```

<br/><br/>

---
(pandas-seriesgroupby)=
### `SeriesGroupBy`

#### Cálculos

##### Aggregates

:::{note}
Estos métodos ignoran valores `NA`/`NaN`, a menos de que se indique lo contrario.
:::

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [SeriesGroupBy.agg](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.SeriesGroupBy.agg.html)([func, engine, engine_kwargs])
  - Calcula _aggregates_ a los valores de cada grupo. Es posibles específicar más una función de agregación e incluso se pueden aplicar diferentes _aggregates_ a diferentes grupos.**EJEMPLO**
* - [SeriesGroupBy.aggregate](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.SeriesGroupBy.aggregate.html)([func, engine, ...])
  - Calcula _aggregates_ a los valores de cada grupo. Es posibles específicar más una función de agregación e incluso se pueden aplicar diferentes _aggregates_ a diferentes grupos.
* - [SeriesGroupBy.count](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.SeriesGroupBy.count.html)()
  - Calcula el recuento de elementos en cada grupo.
* - [SeriesGroupBy.prod](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.SeriesGroupBy.prod.html)([numeric_only, min_count])
  - Calcula el producto de los valores en cada grupo.
* - [SeriesGroupBy.size](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.SeriesGroupBy.size.html)()
  - Calcula el tamaño de los grupos. Incluye valores nulos.
* - [SeriesGroupBy.sum](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.SeriesGroupBy.sum.html)([numeric_only, min_count, ...])
  - Calcula la suma de los valores en cada grupo.
```

:::{caution}
- Para funciones como `.mean()`, `.std()`, etc. consultar los métodos de {ref}`Estadísticas <groupby-series-metodos-estadisticas>`.
- Para conteo de valores únicos revisar los métodos de {ref}`Valores únicos <groupby-series-metodos-valores-unicos>`.
:::

<br/>

##### Booleanos

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [SeriesGroupBy.all](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.SeriesGroupBy.all.html)([skipna])
  - Retorna `True` si todos los valores del grupo son `True`, `False` en caso contrario, para cada grupo.
* - [SeriesGroupBy.any](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.SeriesGroupBy.any.html)([skipna])
  - Retorna `True` si al menos un valor en el grupo es `True`, `False` en caso contrario, para cada grupo.
```

<br/>

##### Cálculos acumulados, diferencias, cambios porcentuales y rank

:::{note}
Estos métodos ignoran valores `NA`/`NaN`, a menos de que se indique lo contrario.
:::

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [SeriesGroupBy.cumcount](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.SeriesGroupBy.cumcount.html)([ascending])
  - Enumera cada elemento en cada grupo desde 0 hasta la longitud de ese grupo. El objeto retornado es un `Series` con el índice del objeto original y los valores son las enumeraciones de los elementos con respecto a su grupo. 
* - [SeriesGroupBy.cummax](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.SeriesGroupBy.cummax.html)([axis, numeric_only])
  - Determina el valor máximo hasta ese elemento en cada grupo. El objeto retornado es un `Series` con el índice del objeto original y los valores son los valores máximos hasta ese elemento con respecto a su grupo. 
* - [SeriesGroupBy.cummin](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.SeriesGroupBy.cummin.html)([axis, numeric_only])
  - Determina el valor mínimo hasta ese elemento en cada grupo. El objeto retornado es un `Series` con el índice del objeto original y los valores son los valores mínimo hasta ese elemento con respecto a su grupo.
* - [SeriesGroupBy.cumprod](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.SeriesGroupBy.cumprod.html)([axis])
  - Determina el producto acumulado hasta ese elemento en cada grupo. El objeto retornado es un `Series` con el índice del objeto original y los valores es el producto acumulado hasta ese elemento con respecto a su grupo.
* - [SeriesGroupBy.cumsum](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.SeriesGroupBy.cumsum.html)([axis])
  - Determina la suma acumulada hasta ese elemento en cada grupo. El objeto retornado es un `Series` con el índice del objeto original y los valores es la suma acumulada hasta ese elemento con respecto a su grupo.
* - [SeriesGroupBy.diff](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.SeriesGroupBy.diff.html)([periods, axis])
  - Determina la diferencia de cada elemento con el antererior en cada grupo. El objeto retornado es un `Series` con el índice del objeto original y los valores son la diferencia hasta ese elemento con respecto a su grupo.
* - [SeriesGroupBy.ngroup](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.SeriesGroupBy.ngroup.html)([ascending])
  - Numera cada grupo desde 0 hasta el _número\_de\_grupos - 1_.
* - [SeriesGroupBy.pct_change](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.SeriesGroupBy.pct_change.html)([periods, ...])
  - Determina el cambio porcentual de cada elemento con el antererior en cada grupo. El objeto retornado es un `Series` con el índice del objeto original y los valores son el cambio porcentual hasta ese elemento con respecto a su grupo.
* - [SeriesGroupBy.rank](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.SeriesGroupBy.rank.html)([method, ascending, ...])
  - Determina el ranking de cada elemento en cada grupo. El objeto retornado es un `Series` con el índice del objeto original y los valores son el ranking de ese elemento con respecto a su grupo.
```

<br/>

##### Estadísticas

```{list-table}
:header-rows: 1
:name: groupby-series-metodos-estadisticas

* - Método
  - Descripción
* - [SeriesGroupBy.corr](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.SeriesGroupBy.corr.html)(other[, method, min_periods])
  - Calcula la correlación con otro `Series`, por grupo.
* - [SeriesGroupBy.cov](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.SeriesGroupBy.cov.html)(other[, min_periods, ddof])
  - Calcula la covarianza con otro `Series`, por grupo.
* - [SeriesGroupBy.describe](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.SeriesGroupBy.describe.html)([percentiles, ...])
  - Genera estadísticas descriptivas para cada grupo.
* - [SeriesGroupBy.mean](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.SeriesGroupBy.mean.html)([numeric_only, engine, ...])
  - Calcula la media de cada grupo..
* - [SeriesGroupBy.median](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.SeriesGroupBy.median.html)([numeric_only])
  - Calcula la mediana de cada grupo.
* - [SeriesGroupBy.nlargest](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.SeriesGroupBy.nlargest.html)([n, keep])
  - Retorna los _n_ elementos más grandes.
* - [SeriesGroupBy.nsmallest](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.SeriesGroupBy.nsmallest.html)([n, keep])
  - Retorna los _n_ elementos más pequeños.
* - [SeriesGroupBy.ohlc](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.SeriesGroupBy.ohlc.html)()
  - Calcula los valores de apertura, máximo, mínimo y cierre para los elementos de cada grupo, excluyendo los valores faltantes. Retorna un `DataFrame` (potencialmente `MultiIndex`). Los valores se determinan por el orden del índice.
* - [SeriesGroupBy.sample](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.SeriesGroupBy.sample.html)([n, frac, replace, ...])
  - Devuelva una muestra aleatoria de elementos de cada grupo.
* - [SeriesGroupBy.sem](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.SeriesGroupBy.sem.html)([ddof, numeric_only])
  - Calcula el error estándar de la media de cada grupo.
* - [SeriesGroupBy.skew](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.SeriesGroupBy.skew.html)([axis, skipna, numeric_only])
  - Retorna el sesgo dentro de cada grupo.
* - [SeriesGroupBy.std](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.SeriesGroupBy.std.html)([ddof, engine, ...])
  - Calcula la desviación estándar de cada grupo.
* - [SeriesGroupBy.var](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.SeriesGroupBy.var.html)([ddof, engine, ...])
  - Calcula la varianza de cada grupo.
```

<br/>

##### Estadísticos de orden

:::{note}
Estos métodos ignoran valores `NA`/`NaN`, a menos de que se indique lo contrario.
:::

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [SeriesGroupBy.idxmax](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.SeriesGroupBy.idxmax.html)([axis, skipna])
  - Retorna el índice del valor máximo por grupo.
* - [SeriesGroupBy.idxmin](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.SeriesGroupBy.idxmin.html)([axis, skipna])
  - Retorna el índice del valor mínimo por grupo.
* - [SeriesGroupBy.max](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.SeriesGroupBy.max.html)([numeric_only, min_count, ...])
  - Calcula el máximo de valores de grupo.
* - [SeriesGroupBy.min](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.SeriesGroupBy.min.html)([numeric_only, min_count, ...])
  - Calcula el mínimo de valores del grupo.
* - [SeriesGroupBy.quantile](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.SeriesGroupBy.quantile.html)([q, interpolation, ...])
  - Retorna valores de grupo en el cuantil dado.
```

<br/>

##### Series de tiempo

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [SeriesGroupBy.resample](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.SeriesGroupBy.resample.html)(rule, *args[, ...])
  - Modifica la frecuencia de una serie de tiempo por grupo, útil si se realizará un _aggregate_ con la nueva frecuencia. El objeto debe de tener un índice `datetime-like` o pasar valores `datetime-like` al argumento `on` o `level`. **IMPORTANTE**: Este método retorna un objeto `Resampler`, que tiene otros métodos como `Resampler.asfreq()` o _aggregates_ como `Resampler.mean()`.
* - [SeriesGroupBy.shift](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.SeriesGroupBy.shift.html)([periods, freq, axis, ...])
  - Desplaza el índice según el número deseado de períodos con una frecuencia de tiempo opcional.
```

<br/>

#### Funciones rolling, aplicar, pipe y mapeos

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [SeriesGroupBy.apply](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.SeriesGroupBy.apply.html)(func, *args, **kwargs)
  - Aplica la función `func` a cada grupo y combina los resultados.
* - [SeriesGroupBy.pipe](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.SeriesGroupBy.pipe.html)(func, *args, **kwargs)
  - Encadena un conjunto de funciones que deben de recibir y retornar (excepto la última) objetos de tipo _GroupBy_.
* - [SeriesGroupBy.rolling](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.SeriesGroupBy.rolling.html)(*args, **kwargs)
  - Provee calculos en ventanas moviles de datos por grupo. El objeto retornado es un `Series` con `MultiIndex` de los _keys_ de los grupos y los índices originales de los elementos aplicando la ventana a los elementos de cada grupo. 
* - [SeriesGroupBy.transform](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.SeriesGroupBy.transform.html)(func, *args[, ...])
  - Aplica la funcción `func` a cada grupo, pero manteniendo el _shape_ e índice del objeto orifinal. Básicamente en el objeto original mapea a los valores el resultado de `func` de su respectivo grupo.
```

<br/>

#### Gráficas


```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [SeriesGroupBy.hist](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.SeriesGroupBy.hist.html)([by, ax, grid, ...])
  - Crea diagramas de caja a partir de los datos de `SeriesGroupBy`. Crea un _subplot_ por cada grupo.
* - [SeriesGroupBy.plot](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.SeriesGroupBy.plot.html)()
  - Crea gráficas a partir de los datos de `SeriesGroupBy`. Crea un _subplots_ por cada grupo.
```

#### Información


```{list-table}
:header-rows: 1

* - [SeriesGroupBy.is_monotonic_decreasing](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.SeriesGroupBy.is_monotonic_decreasing.html)()
  - Indica si los valores de cada grupo están disminuyendo monótonamente.
* - [SeriesGroupBy.is_monotonic_increasing](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.SeriesGroupBy.is_monotonic_increasing.html)()
  - Indica si los valores de cada grupo aumentan monótonamente.
```

<br/>

#### Selección, filtrado e iteración de elementos

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [SeriesGroupBy.\_\_iter__](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.SeriesGroupBy.__iter__.html)()
  - Iterador de grupo.
* - [SeriesGroupBy.filter](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.SeriesGroupBy.filter.html)(func[, dropna])
  - Filtra grupos que no cumplan cierto criterio (los valores con lo que `func` retorna `False`), la función recibe cada grupo.
* - [SeriesGroupBy.first](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.SeriesGroupBy.first.html)([numeric_only, ...])
  - Determina el primer valor dentro de cada grupo.
* - [SeriesGroupBy.get_group](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.SeriesGroupBy.get_group.html)(name[, obj])
  - Retorna `Series` del grupo con el nombre proporcionado.
* - [SeriesGroupBy.groups](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.SeriesGroupBy.groups.html)()
  - Retorna un diccionario donde los _keys_ son el nombre del grupo y los valores es un `list-like` con las etiquetas de filas de los elementos del grupo `{nombre del grupo: etiquetas de grupo}`.
* - [SeriesGroupBy.head](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.SeriesGroupBy.head.html)([n])
  - Retorna las primeras _n_ filas de cada grupo.
* - [SeriesGroupBy.indices](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.SeriesGroupBy.indices.html)()
  - Retorna un diccionario donde los _keys_ son el nombre del grupo y los valores es un `list-like` con los índices de filas de los elementos del grupo `{nombre del grupo: etiquetas de grupo}`.
* - [SeriesGroupBy.last](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.SeriesGroupBy.last.html)([numeric_only, ...])
  - Determina el último valor de cada columna dentro de cada grupo.
* - [SeriesGroupBy.nth](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.SeriesGroupBy.nth.html)()
  - Retorna la enésima fila de cada grupo si _n_ es `int` , de lo contrario retorna un subconjunto de filas por cada grupo.
* - [SeriesGroupBy.tail](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.SeriesGroupBy.tail.html)([n])
  - Retorna las últimas _n_ filas de cada grupo.
* - [SeriesGroupBy.take](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.SeriesGroupBy.take.html)(indices[, axis])
  - Retorna los elementos en los índices posicionales dados en cada grupo.
```

<br/>

#### Valores nulos

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [SeriesGroupBy.bfill](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.SeriesGroupBy.bfill.html)([limit])
  - Reemplaza los valores `NA/NaN` utilizando la siguiente observación válida, en cada grupo.
* - [SeriesGroupBy.ffill](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.SeriesGroupBy.ffill.html)([limit])
  - Reemplaza los valores `NA/NaN` utilizando la última observación válida, en cada grupo.
```

<br/>

#### Valores únicos

```{list-table}
:header-rows: 1
:name: groupby-series-metodos-valores-unicos

* - Método
  - Descripción
* - [SeriesGroupBy.nunique](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.SeriesGroupBy.nunique.html)([dropna])
  - Retorna el número de elementos únicos en cada grupo.
* - [SeriesGroupBy.unique](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.SeriesGroupBy.unique.html)()
  - Retorna `Series` con los elementos únicos en cada grupo.
* - [SeriesGroupBy.value_counts](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.SeriesGroupBy.value_counts.html)([normalize, ...])
  - Retorna el recuento de valores para cada grupo.
```

<br>

---
## Funciones últiles

Lorem ipsum dolor sit amet, consectetur adipiscing elit. 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [Grouper](https://pandas.pydata.org/docs/reference/api/pandas.Grouper.html)(*args, **kwargs)
  - Un Grouper permite al usuario especificar una instrucción groupby para un objeto.
* - [NamedAgg](https://pandas.pydata.org/docs/reference/api/pandas.NamedAgg.html)(column, aggfunc)
  - Ayudante para la agregación específica de columnas con control sobre los nombres de las columnas de salida.
```
