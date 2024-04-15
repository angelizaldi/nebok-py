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

# Series

`Series` es una clase de `pandas` que representa un array unidimensional con etiquetas para identificar a cada elemento, todos los elementos del series deben de ser del mismo tipo. Los `Series` tiene dos tipos de índices:
- **índice implícito**: Es un índice númerico, que comienza desde cero, similiar a los índices de las secuencias.
- **índice explícito**: Es el objeto `Index` asociado, que puede tener etiquetas`int` o `str`.

<br/>

---
(pandas-series-creacion)=
## Creación de `Series`

La forma más sencilla de crear un objeto `Series` es con el constructor.

```{list-table}
:header-rows: 1

* - Constructor
  - Descripción
* - [pandas.Series](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series)(data, index, dtype, name, copy, ...)
  - Array unidimensional con etiquetas de eje.
```
**Notas**:
- _data_: Es un objeto que contiene los datos, se puede definir de diversas formas:
    - `array-like`, `iterable`: Un arreglo o una lista unidimensional con los datos.
    - `dict`: Un diccionario cuyos _keys_ serán los índices de los elementos y cuyos _values_ serán los elementos del `Series`.
    - `scalar`: Si se pasa un `scalar` y de define _index_, entonces todos los elementos serán el escalar con la misma longitud que _index_.
- _index_: Es un `array-like` o un objeto `Index` con los índices del `Series`. Normalmente debe ser de la misma longitud que _data_. En caso de que _data_ sea `dict`, _index_ se puede usar para generar el `Series` con solo determinados índices-elementos, excluyendo los que no definan en este parámetro.

**Ejemplo**
A continuación se crea un objeto `Series` cuyos valores son los cuadrados de los números del 1 al 5 y cuyo índice explícito son los nombres de los número del 0 al 4. Además el `Series` llevará por nombre _cuadrados_.

```{code-cell} ipython3
# Importar librería
import pandas as pd

# Crear Series
s = pd.Series(data=[i**2 for i in range(1, 6)], 
              index = ['uno', 'dos', 'tres', 'cuatro', 'cinco'], 
              name="cuadrados")

# Imprimir el objeto
print(s)
```

<br/>

---
## Selección de elementos

Existen diversos métodos para seleccionar elementos en un Series. Aquí se explicarán los más comunes. Todos los ejemplos de esta sección utilizará el `Series` definido en [la sección anterior](pandas-series-creacion):

### Notación con corchetes

Todas las estrategias para seleccionar elementos que aplican para `ndarray` de `numpy` funcionan también con `Series` la principal diferencia es que en el caso del `Series` se deben usar índices explícitos. **Importante**: El uso de los índices implícitos con esta notación está desaconsejado, para ello se recomienda usar el método `.iloc[]`.
    
- **Indexing**: Útil para seleccionar elementos específicos. Se utilizan corchetes `[]` para acceder a la fila, junto con el nombre del `Series` y el índice explícito del elemento
    - **Una fila específica** - `scalar`: Retorna el elemento en la etiqueta _'label'_: <br/> `X['label']`

<br/>

- **Slicing**: Útil para seleccionar _slices_ utilizando `start:stop:step`. Ambos extremos son inclusivos.
    - **Slices de filas** - `Series`: Retorna _slices_ de filas, entre las filas con etiquetas _'indi'_ y _'indj'_: <br/> `X.['indi':'indj']` <br/> `X['indi':'indj':step]`

<br/>

- **Fancy indexing**: Útil para seleccionar un conjunto de filas por medio de una secuencia los índices explícitos a seleccionar. Los índices se pueden poner en culquier orden e incluso se puedo poner más de una vez: <br/> `X[[labeli, labelj, ...]]` 
    - **Conjunto de filas** - `Series`: Retorna las filas en las etiquetas indicadas: <br/> `X.[['ind1', 'ind2', ...]]`

<br/>

- **Boolean masking**: Útil para seleccionar filas con base a _masks_. **Importante**: Asegurarse que el tamaño del _mask_ coincide con el tamaño del eje donde se va a aplicar.
    - **Mask en filas** - `Series`: Retorna los elementos que satisfacen el _mask_: <br/> `X.[row_mask, col_mask]`

:::{tip}
Se pueden usar los operadores {ref}`built-in-operadores-bitwise` para crear mask más complejos: <br/> `X[(mask1) & (mask2)] # Ejemplo con '&'`
- Notar que cada mask se pone entre paréntesis.
- **No usar** los operadores lógicos para conformar _masks_ más complicados.
:::

<br/>

**Ejemplos**: A continuación se ejemplifica la selección de elementos con las diversas estategias en notación con conchetes en un `Series`.

```{code-cell} ipython3
# Subsetting: Seleccionar 2 elemento ->
print(s['dos'], end="\n"*2)

# Slicing: Seleccionar elementos del 2 al 4 -> 4, 9, 16
print(s['dos':'cuatro'], end="\n"*2)

# Fancy indexing: Seleccionar elementos pares -> 4, 16
print(s[['dos', 'cuatro']], end="\n"*2)

# Boolean masking: Seleccionar elementos pares -> 4, 16
print(s[s%2==0])
```

<br/>

---
### Usando método `.loc[]`

El método `.loc[]` es útil para seleccionar elementos con base al **índice explícito**.

- **Indexing**: Útil para seleccionar elementos específicos.
	- **Elemento específico** - `scalar`: Retorna el elemento en la etiqueta _'ind'_: <br/> `X.loc['ind']`

- **Slicing**: Útil para seleccionar _slices_ utilizando `start:stop:step`. Ambos extremos son inclusivos.
    - **Slices de filas** - `Series`: Retorna _slices_ de filas, entre las filas con etiquetas _'indi'_ y _'indj'_: <br/> `X.loc['indi':'indj']` <br/> `X.loc['indi':'indj':step]`

- **Fancy indexing**: Útil para seleccionar un conjunto de filas específicas. Las etiquetas de fila se pueden poner en culquier orden e incluso se puedo poner más de una vez.
    - **Conjunto de filas** - `Series`: Retorna las filas en las etiquetas indicadas: <br/> `X.loc[['ind1', 'ind2', ...]]`

- **Boolean masking** - `Series`: Retorna las filas que satisfacen el _mask_. **Importante**: Asegurarse que el tamaño del _mask_ coincide con el tamaño del `Series`: <br/> `X.loc[mask]`

:::{tip}
Se pueden usar los operadores {ref}`built-in-operadores-bitwise` para crear mask más complejos: <br/> `X[(mask1) & (mask2)] # Ejemplo con '&'`
- Notar que cada mask se pone entre paréntesis.
- **No usar** los operadores lógicos para conformar _masks_ más complicados.
:::

<br/>

**Ejemplos**: A continuación se ejemplifica la selección de elementos con las diversas estategias con el método `.loc[]` en un `Series`.

```{code-cell} ipython3
# Subsetting: Seleccionar 2do elemento -> 4
print(s.loc['dos'], end="\n"*2)

# Slicing: Seleccionar elementos del 2 al 4 -> 4, 9, 16
print(s.loc['dos':'cuatro'], end="\n"*2)

# Fancy indexing: Seleccionar elementos 4 y 2 -> 16, 4
print(s.loc[['cuatro', 'dos']], end="\n"*2)

# Boolean masking: Seleccionar elementos pares -> 4, 16
print(s.loc[s%2==0], end="\n"*2)
```

<br/>

---
### Usando método `.iloc[]`

El método `.iloc[]` es útil para seleccionar elementos con base al **índice explícito**.

- **Indexing**: Útil para seleccionar elementos específicos.
	- **Elemento específico** - `scalar`: Retorna el elemento en índice _i_: <br/> `X.loc[i]`

<br/>

- **Slicing**: Útil para seleccionar _slices_ utilizando `start:stop:step`. En este caso no se incluye al elemento en el índice `stop`, es decir, es exclusivo.
    - **Slices de filas** - `Series`: Retorna _slices_ de filas, entre las filas con índices _start_ y _stop_: <br/> `X.loc[start:stop]` <br/> `X.loc[start:stop:step]`

<br/>

- **Fancy indexing**: Útil para seleccionar combinaciones de filas específicas. Los índices se pueden poner en culquier orden e incluso se puedo poner más de una vez.
    - **Combinación de filas** - `Series`: Retorna las filas en las etiquetas indicadas: <br/> `X.loc[[i, j, ...]]`

<br/>

- **Boolean masking**: No se puede hacer _boolean masking_ con este método.

<br/><br/>

---
## Verificar la existencia de un _label_

Para verificar si una etiqueta existe en un `Series` usar el operador de membresía `in`:
```python
# Si X es un Series
x in X
```
- La expresión anterior retornará un valor `bool`.
- Alternativamente se puede usar `not in`.

<br>

---
## Agregar elementos

Para agregar un elemento a un `Series` se puede simplmente crear una nueva etiqueta y asignarle un valor:
```python
# Agregar elemento
X['label'] = val
```

<br>

---
## Modificar elementos

Se pueden acceder a determinados elementos con cualquier método de selección de elementos y asignarle un nuevo valor.

:::{warning}
Al asignar elementos asegurarse que los tipos coincidan con el tipo del `Series` o al menos que sea posible forzar la conversión.
:::

```python
# Modificar elementos específicos
s.loc['ind'] = val	
s.iloc[i] = val

# Múltiples valores con mismo valor (ejemplo con slicing)
s.loc['indi':'indj'] = val

# Múltiples valores con diferentes valores (ejemplo con slicing)
df.loc['indi':'indj'] = [vali, ..., valj]
```
**Notas**:
- **Un elemento específico**: Seleccionar el elemento por cualquier estrategia de selección y asigarle un nuevo valor.
- **Múltiples elementos con un mismo valor**: Seleccionar los elementos por cualquier estrategia de selección y asignarles un `scalar`.
- **Múltiples elementos con valores diferentes**: Seleccionar los elementos por cualquier estrategia de selección y asignarles un `array-like` del mismo _shape_ que el objeto retornado por la selección.

<br/>

## Uniones y apilaciones

Para unir objetos de pandas, ya sea apilando los objetos o en una operación similar a un _join_ de SQL, revisar los siguientes funciones de `pandas`:
- `pd.concat()`: Concatena objetos sobre un eje existe, resultando en un objeto con el mismo número de dimensiones que los objetos originales. Se puede indicar si el _index_ se debe de reiniciar o indicar a que objeto pertenecía cada fila.
- `pd.merge()`: Permite unir objetos de `pandas` con base a valores de columnas o de los índices de una manera similar a un _join_ de SQL.

:::{note}
Para más información vistar {ref}`Funciones de uniones y apilaciones <pandas-func-joins>`.
:::

<br/>

---
## Atributos

Atributos del objeto `Series`. 

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - [Series.T](http://pandas.pydata.org/docs/reference/api/pandas.Series.T.html)
  - Retorna la transpuesta, que por definición es `self`.
* - [Series.array](http://pandas.pydata.org/docs/reference/api/pandas.Series.array.html)
  - Retorna el `Series` como array.
* - [Series.dtype](http://pandas.pydata.org/docs/reference/api/pandas.Series.dtype.html)
  - Retorna el `dtype` de los datos subyacentes.
* - [Series.empty](http://pandas.pydata.org/docs/reference/api/pandas.Series.empty.html)
  - Indica si el `Series` está vacío.
* - [Series.hasnans](http://pandas.pydata.org/docs/reference/api/pandas.Series.hasnans.html)
  - Retorna `True` si hay algún `NaN`.
* - [Series.index](http://pandas.pydata.org/docs/reference/api/pandas.Series.index.html)
  - Retorna el índice (etiquetas de eje) del `Series` como `pd.Index` o una subclase del mismo.
* - [Series.memory_usage](http://pandas.pydata.org/docs/reference/api/pandas.Series.memory_usage.html)([index, deep])
  - Retorna el uso de memoria del `Series`.
* - [Series.name](http://pandas.pydata.org/docs/reference/api/pandas.Series.name.html)
  - Retorna el nombre del `Series`.
* - [Series.nbytes](http://pandas.pydata.org/docs/reference/api/pandas.Series.nbytes.html)
  - Retorna el número de bytes de los datos subyacentes.
* - [Series.ndim](http://pandas.pydata.org/docs/reference/api/pandas.Series.ndim.html)
  - Número de dimensiones de los datos subyacentes, por definición 1.
* - [Series.shape](http://pandas.pydata.org/docs/reference/api/pandas.Series.shape.html)
  - Retorna un `tuple` con el _shape_ de los datos subyacentes.
* - [Series.size](http://pandas.pydata.org/docs/reference/api/pandas.Series.size.html)
  - Retorna el número de elementos de los datos subyacentes.
* - [Series.values](http://pandas.pydata.org/docs/reference/api/pandas.Series.values.html)
  - Retorna los elementos del `Series` como `ndarray`.
```

<br/>


## Métodos

### Conversión y copias

Métodos para convertir el objeto `Series` a algún otro tipo. 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [Series.astype](http://pandas.pydata.org/docs/reference/api/pandas.Series.astype.html)(dtype[, copy, errors])
  - Convierte los datos a otro tipo de datos.
* - [Series.convert_dtypes](http://pandas.pydata.org/docs/reference/api/pandas.Series.convert_dtypes.html)([infer_objects, ...])
  - Convierte los valores al mejor tipo `dtype` posible que admitan `pd.NA`.
* - [Series.copy](http://pandas.pydata.org/docs/reference/api/pandas.Series.copy.html)([deep])
  - Crea una copia del `Series`.
* - [Series.infer_objects](http://pandas.pydata.org/docs/reference/api/pandas.Series.infer_objects.html)([copy])
  - Intenta inferir el tipo `dtype` de los valores.
* - [Series.factorize](http://pandas.pydata.org/docs/reference/api/pandas.Series.factorize.html)([sort, use_na_sentinel])
  - Codifica los valores como un tipo enumerado o una variable categórica.
* - [Series.squeeze](http://pandas.pydata.org/docs/reference/api/pandas.Series.squeeze.html)([axis])
  - Convierte un `Series` con un solo elemento en un escalar de Python.
* - [Series.to_list](http://pandas.pydata.org/docs/reference/api/pandas.Series.to_list.html)()
  - Retorna un `list` de los valores.
* - [Series.to_numpy](http://pandas.pydata.org/docs/reference/api/pandas.Series.to_numpy.html)([dtype, copy, na_value])
  - Retorna un `ndarray` de los valores.
* - [Series.to_period](http://pandas.pydata.org/docs/reference/api/pandas.Series.to_period.html)([freq, copy])
  - Convierte el `Series` de `DatetimeIndex` a `PeriodIndex`.
* - [Series.to_timestamp](http://pandas.pydata.org/docs/reference/api/pandas.Series.to_timestamp.html)([freq, how, copy])
  - Convierte el índice de un `Series` de `PeriodIndex` a `DateTimeIndex`, cada periodo lo convierte al inicio del periodo.
* - [Series.unstack](http://pandas.pydata.org/docs/reference/api/pandas.Series.unstack.html)([level, fill_value, sort])
  - Convierte un `Series` con `MultiIndex` en `DataFrame`.
```

<br/>

### IO y Serialización

Métodos para exportar el `Series` en un formato específico o serializar el mismo.


```{list-table}
:header-rows: 1

* - [Series.to_clipboard](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_clipboard.html)(*[, excel, sep])
  - Copia el objeto al portapapeles del sistema.
* - [Series.to_csv](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_csv.html)([path_or_buf, sep, na_rep, ...])
  - Escribe el objeto en un archivo de valores separados por comas (csv).
* - [Series.to_dict](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_dict.html)(*[, into])
  - Convierte `Series` a `dict` de forma similar a: `{label: value}`.
* - [Series.to_excel](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_excel.html)(excel_writer, *[, ...])
  - Escribe el objeto en una hoja de Excel.
* - [Series.to_frame](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_frame.html)([name])
  - Convierte `Series` a `DataFrame`.
* - [Series.to_hdf](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_hdf.html)(path_or_buf, *, key[, mode, ...])
  - Escribe los datos contenidos en un archivo _HDF5_ usando _HDFStore_.
* - [Series.to_json](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_json.html)([path_or_buf, orient, ...])
  - Escribe el objeto en una cadena _JSON_.
* - [Series.to_latex](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_latex.html)([buf, columns, header, ...])
  - Escribe el objeto en una tabla tabular de LaTeX.
* - [Series.to_markdown](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_markdown.html)([buf, mode, index, ...])
  - Escribe el `Series` en formato compatible con Markdown.
* - [Series.to_pickle](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_pickle.html)(path, *[, compression, ...])
  - Serializa el objeto en un _pickle_.
* - [Series.to_sql](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_sql.html)(name, con, *[, schema, ...])
  - Escribe los registros almacenados en un `Series` a una base de datos _SQL_.
* - [Series.to_string](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_string.html)([buf, na_rep, ...])
  - Escribe el objeto en una cadena.
* - [Series.to_xarray](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_xarray.html)()
  - Retorna un objeto _xarray_ del objeto pandas.
```

<br/>

---
### Cálculos y operadores

Métodos para realizar cálculos con el `Series` o métodos equivalentes a operadores de Python. 


#### Aggregates

```{list-table}
:header-rows: 1
:name: pandas-series-methods-cumm

* - Método
  - Descripción
* - [Series.agg](http://pandas.pydata.org/docs/reference/api/pandas.Series.agg.html)([func, axis])
  - Calcula _aggregates_ usando una o más operaciones.
* - [Series.aggregate](http://pandas.pydata.org/docs/reference/api/pandas.Series.aggregate.html)([func, axis])
  - Calcula _aggregates_ usando una o más operaciones.
* - [Series.prod](http://pandas.pydata.org/docs/reference/api/pandas.Series.prod.html)([axis, skipna, numeric_only, ...])
  - Retorna el producto de los valores.
* - [Series.product](http://pandas.pydata.org/docs/reference/api/pandas.Series.product.html)([axis, skipna, numeric_only, ...])
  - Retorna el producto de los valores.
* - [Series.sum](http://pandas.pydata.org/docs/reference/api/pandas.Series.sum.html)([axis, skipna, numeric_only, ...])
  - Retorna la suma de los valores.
```

:::{caution}
Para funciones como `.mean()`, `.std()`, etc. consultar los métodos {ref}`Estadísticas <series-metodos-estadisticas>`.
:::

<br/>

#### Booleanos


```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [Series.all](http://pandas.pydata.org/docs/reference/api/pandas.Series.all.html)([axis, bool_only, skipna])
  - Retorna `True` si todos los valores son `True` en el  `Series`.
* - [Series.any](http://pandas.pydata.org/docs/reference/api/pandas.Series.any.html)(*[, axis, bool_only, skipna])
  - Retorna `True` si hay al menos un valor `True` en el  `Series`.
```

<br/>

#### Cálculos acumulados, diferencias, cambios porcentuales y rank


```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [Series.cummax](http://pandas.pydata.org/docs/reference/api/pandas.Series.cummax.html)([axis, skipna])
  - Para cada fila calcula el valor máximo hasta esa fila.
* - [Series.cummin](http://pandas.pydata.org/docs/reference/api/pandas.Series.cummin.html)([axis, skipna])
  - Para cada fila calcula el valor mínimo hasta esa fila.
* - [Series.cumprod](http://pandas.pydata.org/docs/reference/api/pandas.Series.cumprod.html)([axis, skipna])
  - Para cada fila calcula el producto hasta esa fila.
* - [Series.cumsum](http://pandas.pydata.org/docs/reference/api/pandas.Series.cumsum.html)([axis, skipna])
  - Para cada fila calcula la suma hasta esa fila.
* - [Series.diff](http://pandas.pydata.org/docs/reference/api/pandas.Series.diff.html)([periods])
  - Para cada fila calcula la diferencia entre el elemento actual y el anterior (`[i] - [i-1]`). Se puede definir el desfase con el parámetro _periods_.
* - [Series.pct_change](http://pandas.pydata.org/docs/reference/api/pandas.Series.pct_change.html)([periods, fill_method, ...])
  - Para cada fila calcula el cambio porcentual entre el elemento actual y el anterior (`[i] - [i-1]`). Se puede definir el desfase con el parámetro _periods_.
* - [Series.rank](http://pandas.pydata.org/docs/reference/api/pandas.Series.rank.html)([axis, method, numeric_only, ...])
  - Calcula el _rank_ (1 a _n_) a lo largo del eje.
```

<br/>

#### Conteo


```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [Series.count](http://pandas.pydata.org/docs/reference/api/pandas.Series.count.html)()
  - Retorna el número de observaciones no nulas en el `Series`.
* - [Series.value_counts](http://pandas.pydata.org/docs/reference/api/pandas.Series.value_counts.html)([normalize, sort, ...])
  - Retorna un `Series` que contiene recuentos de los valores únicos.
```

<br/>

#### Estadísticas

Métodos para el cálculo de estadísticas descriptivas, generar muestras aleatorias o calcular correlaciones y covarianzas entre dos variables.

:::{note}
Estos métodos ignoran valores `NA`.
:::

```{list-table}
:header-rows: 1
:name: series-metodos-estadisticas

* - Método
  - Descripción
* - [Series.corr](http://pandas.pydata.org/docs/reference/api/pandas.Series.corr.html)(other[, method, min_periods])
  - Calcula la correlación con `other`, excluye los valores perdidos.
* - [Series.cov](http://pandas.pydata.org/docs/reference/api/pandas.Series.cov.html)(other[, min_periods, ddof])
  - Calcula la covarianza con `other`, excluye los valores perdidos.
* - [Series.describe](http://pandas.pydata.org/docs/reference/api/pandas.Series.describe.html)([percentiles, include, exclude])
  - Genera estadísticas descriptivas de los datos. 
* - [Series.kurt](http://pandas.pydata.org/docs/reference/api/pandas.Series.kurt.html)([axis, skipna, numeric_only])
  - Retorna la curtosis de los datos.
* - [Series.kurtosis](http://pandas.pydata.org/docs/reference/api/pandas.Series.kurtosis.html)([axis, skipna, numeric_only])
  - Retorna la curtosis de los datos.
* - [Series.mean](http://pandas.pydata.org/docs/reference/api/pandas.Series.mean.html)([axis, skipna, numeric_only])
  - Retorna la media aritmética de los valores.
* - [Series.median](http://pandas.pydata.org/docs/reference/api/pandas.Series.median.html)([axis, skipna, numeric_only])
  - Retorna la mediana de los valores.
* - [Series.mode](http://pandas.pydata.org/docs/reference/api/pandas.Series.mode.html)([dropna])
  - Retorna la moda de los valores.
* - [Series.sample](http://pandas.pydata.org/docs/reference/api/pandas.Series.sample.html)([n, frac, replace, weights, ...])
  - Retorna una muestra aleatoria de elementos del objeto.
* - [Series.sem](http://pandas.pydata.org/docs/reference/api/pandas.Series.sem.html)([axis, skipna, ddof, numeric_only])
  - Retorna el error estándar de la media de los valores.
* - [Series.skew](http://pandas.pydata.org/docs/reference/api/pandas.Series.skew.html)([axis, skipna, numeric_only])
  - Retorna el sesgo de los valores.
* - [Series.std](http://pandas.pydata.org/docs/reference/api/pandas.Series.std.html)([axis, skipna, ddof, numeric_only])
  - Retorna la desviación estándar de la muestra de los valores.
* - [Series.var](http://pandas.pydata.org/docs/reference/api/pandas.Series.var.html)([axis, skipna, ddof, numeric_only])
  - Retorna la varianza de los valores.
```

<br/>

#### Estadísticos de orden

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [Series.argmax](http://pandas.pydata.org/docs/reference/api/pandas.Series.argmax.html)([axis, skipna])
  - Retorna la posición `int` del valor máximo en el objeto.
* - [Series.argmin](http://pandas.pydata.org/docs/reference/api/pandas.Series.argmin.html)([axis, skipna])
  - Retorna la posición `int` del valor mínimo en el objeto.
* - [Series.max](http://pandas.pydata.org/docs/reference/api/pandas.Series.max.html)([axis, skipna, numeric_only])
  - Retorna el máximo de los valores sobre el eje solicitado.
* - [Series.min](http://pandas.pydata.org/docs/reference/api/pandas.Series.min.html)([axis, skipna, numeric_only])
  - Retorna el mínimo de los valores.
* - [Series.nlargest](http://pandas.pydata.org/docs/reference/api/pandas.Series.nlargest.html)([n, keep])
  - Retorna los _n_ elementos más grandes.
* - [Series.nsmallest](http://pandas.pydata.org/docs/reference/api/pandas.Series.nsmallest.html)([n, keep])
  - Retorna los _n_ elementos más pequeños.
* - [Series.quantile](http://pandas.pydata.org/docs/reference/api/pandas.Series.quantile.html)([q, interpolation])
  - Retorna el cuantil dado de los valores. `q` es un valor entre cero y uno.
```

<br/>

#### Misceláneos

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [Series.abs](http://pandas.pydata.org/docs/reference/api/pandas.Series.abs.html)()
  - Retorna el valor numérico absoluto de cada elemento.
```

<br/>

#### Operadores aritméticos y similares.

Métodos para realizar operaciones binarias con operadores aritméticos y sus equivalentes que tienen por sufijo una `r`, que estos últimos son útiles para intercambiar las posiciones del `Series` y del argumento `other`. 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [Series.add](http://pandas.pydata.org/docs/reference/api/pandas.Series.add.html)(other[, level, fill_value, axis])
  - Retorna la suma del `Series` y `other`, por elementos. Equivale a usar el operador `+`.
* - [Series.div](http://pandas.pydata.org/docs/reference/api/pandas.Series.div.html)(other[, level, fill_value, axis])
  - Retornar la división flotante del `Series` y `other`, por elementos. Equivale a usar el operador `/`.
* - [Series.dot](http://pandas.pydata.org/docs/reference/api/pandas.Series.dot.html)(other)
  - Calcula el producto escalar entre `Series` y `other`.
* - [Series.floordiv](http://pandas.pydata.org/docs/reference/api/pandas.Series.floordiv.html)(other[, level, fill_value, axis])
  - Retornar la división entera del `Series` y `other`, por elementos. Equivale a usar el operador `//`.
* - [Series.mod](http://pandas.pydata.org/docs/reference/api/pandas.Series.mod.html)(other[, level, fill_value, axis])
  - Retornar el módulo de la división del `Series` y `other`, por elementos. Equivale a usar el operador `%`.
* - [Series.mul](http://pandas.pydata.org/docs/reference/api/pandas.Series.mul.html)(other[, level, fill_value, axis])
  - Retornar la multiplicación del `Series` y `other`, por elementos. Equivale a usar el operador `*`.
* - [Series.pow](http://pandas.pydata.org/docs/reference/api/pandas.Series.pow.html)(other[, level, fill_value, axis])
  - Retornar la potenciación del `Series` y `other`, por elementos. Equivale a usar el operador `^`.
* - [Series.radd](http://pandas.pydata.org/docs/reference/api/pandas.Series.radd.html)(other[, level, fill_value, axis])
  - Retorna la suma del `Series` y `other`, por elementos. Equivale a usar el operador `+`.
* - [Series.rdiv](http://pandas.pydata.org/docs/reference/api/pandas.Series.rdiv.html)(other[, level, fill_value, axis])
  - Retornar la división flotante de `other` y `Series`, por elementos. Equivale a usar el operador `/`, siendo `other` el numerador.
* - [Series.rfloordiv](http://pandas.pydata.org/docs/reference/api/pandas.Series.rfloordiv.html)(other[, level, fill_value, ...])
  - Retornar la división entera de `other` y `Series`, por elementos. Equivale a usar el operador `//`, siendo `other` el numerador.
* - [Series.rmod](http://pandas.pydata.org/docs/reference/api/pandas.Series.rmod.html)(other[, level, fill_value, axis])
  - Retornar el módulo de la división de `other` y `Series`, por elementos. Equivale a usar el operador `%`, siendo `other` el numerador.
* - [Series.rmul](http://pandas.pydata.org/docs/reference/api/pandas.Series.rmul.html)(other[, level, fill_value, axis])
  - Retornar la multiplicación del `Series` y `other`, por elementos. Equivale a usar el operador `*`.
* - [Series.rpow](http://pandas.pydata.org/docs/reference/api/pandas.Series.rpow.html)(other[, level, fill_value, axis])
  - Retornar la potenciación de `other` y `Series`, por elementos. Equivale a usar el operador `^`, siendo `other` la base.
* - [Series.rsub](http://pandas.pydata.org/docs/reference/api/pandas.Series.rsub.html)(other[, level, fill_value, axis])
  - Retornar la resta de `other` y `Series`, por elementos. Equivale a usar el operador `-`, siendo `other` el minuendo.
* - [Series.rtruediv](http://pandas.pydata.org/docs/reference/api/pandas.Series.rtruediv.html)(other[, level, fill_value, axis])
  - Retornar la división flotante del `other` y `Series`, por elementos. Equivale a usar el operador `/`, siendo `other` el numerador. Permite reemplazar valores perdidos por algún valor en particular.
* - [Series.sub](http://pandas.pydata.org/docs/reference/api/pandas.Series.sub.html)(other[, level, fill_value, axis])
  - Retornar la resta del `Series` y `other`, por elementos. Equivale a usar el operador `-`.
* - [Series.truediv](http://pandas.pydata.org/docs/reference/api/pandas.Series.truediv.html)(other[, level, fill_value, axis])
  - Retornar la división flotante del `Series` y `other`, por elementos. Equivale a usar el operador `/`. Permite reemplazar valores perdidos por algún valor en particular.
```

<br/>

#### Operadores de comparación y membresía.

Métodos para comparar los elementos del `Series` con otro objeto o verificar que los elementos del `Series` satisfagan ciertas condiciones, como verificar que estén entre un rango o un conjunto de valores concretos. 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [Series.between](http://pandas.pydata.org/docs/reference/api/pandas.Series.between.html)(left, right[, inclusive])
  - Retorna `Series` booleano que indica si `left` <= `Series` <= `right`, por elementos.
* - [Series.eq](http://pandas.pydata.org/docs/reference/api/pandas.Series.eq.html)(other[, level, fill_value, axis])
  - Indica la igualdad del `Series` y `other`, por elementos. Equivale a usar el operador `==`.
* - [Series.equals](http://pandas.pydata.org/docs/reference/api/pandas.Series.equals.html)(other)
  - Verifica si dos objetos contienen los mismos elementos.
* - [Series.ge](http://pandas.pydata.org/docs/reference/api/pandas.Series.ge.html)(other[, level, fill_value, axis])
  - Indica si es mayor o igual el `Series` y `other`, por elementos. Equivale a usar el operador `>=`.
* - [Series.gt](http://pandas.pydata.org/docs/reference/api/pandas.Series.gt.html)(other[, level, fill_value, axis])
  - Indica si es mayor el `Series` y `other`, por elementos. Equivale a usar el operador `>`.
* - [Series.isin](http://pandas.pydata.org/docs/reference/api/pandas.Series.isin.html)(values)
  - Retorna `Series` booleano que indica si `Series in values`, por elementos.
* - [Series.le](http://pandas.pydata.org/docs/reference/api/pandas.Series.le.html)(other[, level, fill_value, axis])
  - Indica si es menor o igual el `Series` y `other`, por elementos. Equivale a usar el operador `<=`.
* - [Series.lt](http://pandas.pydata.org/docs/reference/api/pandas.Series.lt.html)(other[, level, fill_value, axis])
  - Indica si es menor el `Series` y `other`, por elementos. Equivale a usar el operador `<`.
* - [Series.ne](http://pandas.pydata.org/docs/reference/api/pandas.Series.ne.html)(other[, level, fill_value, axis])
  - Indica si no son iguales el `Series` y `other`, por elementos. Equivale a usar el operador `!=`.
```

<br/>

#### Series de tiempo

Métodos útiles para `Series` que tienen un `Index` que representa una serie de tiempo.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [Series.asfreq](http://pandas.pydata.org/docs/reference/api/pandas.Series.asfreq.html)(freq[, method, how, ...])
  - Modifica la frecuencia de una serie de tiempo. El `Series` debe de tener un índice `datetime-like`. Si se va a realizar un _aggregate_ con la nueva frecuencia se recomienda usar el método `Series.resample()`.
* - [Series.asof](http://pandas.pydata.org/docs/reference/api/pandas.Series.asof.html)(where[, subset])
  - Retorna la/s última/s fila/s válida sin incluir `NaNs` antes o en `where`, donde `where` son etiquetas del índice.
* - [Series.at_time](http://pandas.pydata.org/docs/reference/api/pandas.Series.at_time.html)(time[, asof, axis])
  - Selecciona valores en un momento particular del día (por ejemplo, 9:30 a. m.).
* - [Series.autocorr](http://pandas.pydata.org/docs/reference/api/pandas.Series.autocorr.html)([lag])
  - Calcula la autocorrelación de los datos con `lag` desfases.
* - [Series.between_time](http://pandas.pydata.org/docs/reference/api/pandas.Series.between_time.html)(start_time, end_time[, ...])
  - Selecciona valores entre horas particulares del día (por ejemplo, de 9:00 a 9:30 a. m.).
* - [Series.resample](http://pandas.pydata.org/docs/reference/api/pandas.Series.resample.html)(rule[, axis, closed, label, ...])
  - Modifica la frecuencia de una serie de tiempo, útil si se realizará un _aggregate_ con la nueva frecuencia. El objeto debe de tener un índice `datetime-like` o pasar valores `datetime-like` al argumento `on` o `level`. **IMPORTANTE**: Este método retorna un objeto `Resampler`, que tiene otros métodos como `Resampler.asfreq()` o _aggregates_ como `Resampler.mean()`. 
* - [Series.shift](http://pandas.pydata.org/docs/reference/api/pandas.Series.shift.html)([periods, freq, axis, ...])
  - Desplaza el índice según el número deseado de períodos con una frecuencia de tiempo opcional.
* - [Series.tz_convert](http://pandas.pydata.org/docs/reference/api/pandas.Series.tz_convert.html)(tz[, axis, level, copy])
  - Convierte un _axis_ compatible con `tz` en la zona horaria objetivo.
* - [Series.tz_localize](http://pandas.pydata.org/docs/reference/api/pandas.Series.tz_localize.html)(tz[, axis, level, copy, ...])
  - Localiza el índice `tz-naive` a la zona horaria de destino.
```

<br/>

---
### Funciones ventana, agrupar, aplicar y mapeos

Diversos métodos de operaciones comúnes con `Series`. 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [Series.apply](http://pandas.pydata.org/docs/reference/api/pandas.Series.apply.html)(func[, convert_dtype, args, by_row])
  - Aplica una función a cada valor del `Series`.
* - [Series.ewm](http://pandas.pydata.org/docs/reference/api/pandas.Series.ewm.html)([com, span, halflife, alpha, ...])
  - Provee de cálculos ponderados exponencialmente (_EW_).
* - [Series.expanding](http://pandas.pydata.org/docs/reference/api/pandas.Series.expanding.html)([min_periods, axis, method])
  - Para cada fila en el `Series` calcula un _aggregate_ hasta esa fila, para realizar el cálculo se debe aplicar un {ref}`método <pandas-expanding-methods>` del objeto `Expanding`. Funciona de manera similar a {ref}`métodos de cálculos acumulados <pandas-series-methods-cumm>` como `Series.cumprod()`, `Series.cumsum()`, etc.
* - [Series.groupby](http://pandas.pydata.org/docs/reference/api/pandas.Series.groupby.html)([by, axis, level, as_index, ...])
  - Agrupa por los valores del `Series`. Posteriorme se pueden aplicar {ref}`métodos <pandas-seriesgroupby>` del objeto `SeriesGroupBy` a cada grupo.
* - [Series.map](http://pandas.pydata.org/docs/reference/api/pandas.Series.map.html)(arg[, na_action])
  - Aplica una función a cada valor del `Series` o mapea los valores con base a otro objeto.
* - [Series.pipe](http://pandas.pydata.org/docs/reference/api/pandas.Series.pipe.html)(func, *args, **kwargs)
  - Encadena funciones que reciben `Series` o `DataFrame`.
* - [Series.rolling](http://pandas.pydata.org/docs/reference/api/pandas.Series.rolling.html)(window[, min_periods, ...])
  - Provee calculos en ventanas moviles de datos. Posteriormente se puede aplicar un {ref}`método <pandas-rolling-methods>` del objeto `Rolling` o `Window`. 
* - [Series.transform](http://pandas.pydata.org/docs/reference/api/pandas.Series.transform.html)(func[, axis])
  - Aplica una función `func` en sí mismo, retornando un objeto con las mismas dimensiones que `self`.
```

<br/>

---
### Gráficas

Métodos para gráficar. 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [Series.hist](https://pandas.pydata.org/docs/reference/api/pandas.Series.hist.html)([by, ax, grid, xlabelsize, ...])
  - Grafica el histograma de la serie de entrada usando `matplotlib`.
* - [Series.plot](https://pandas.pydata.org/docs/reference/api/pandas.Series.plot.html)([kind, ax, figsize, ....])
  - Función general para crear gráficas con base a los datos del `Series`.
* - [Series.plot.area](https://pandas.pydata.org/docs/reference/api/pandas.Series.plot.area.html)([x, y, stacked])
  - Gráfica de áreas apiladas.
* - [Series.plot.bar](https://pandas.pydata.org/docs/reference/api/pandas.Series.plot.bar.html)([x, y])
  - Gráfica de barras verticales.
* - [Series.plot.barh](https://pandas.pydata.org/docs/reference/api/pandas.Series.plot.barh.html)([x, y])
  - Gráfica de barras horizontales.
* - [Series.plot.box](https://pandas.pydata.org/docs/reference/api/pandas.Series.plot.box.html)([by])
  - Gráfica de un diagrama de cajas.
* - [Series.plot.density](https://pandas.pydata.org/docs/reference/api/pandas.Series.plot.density.html)([bw_method, ind])
  - Genera un gráfico de estimación de densidad.
* - [Series.plot.hist](https://pandas.pydata.org/docs/reference/api/pandas.Series.plot.hist.html)([by, bins])
  - Grafica un histograma de los datos del `Series`.
* - [Series.plot.kde](https://pandas.pydata.org/docs/reference/api/pandas.Series.plot.kde.html)([bw_method, ind])
  - Genera un gráfico de estimación de densidad.
* - [Series.plot.line](https://pandas.pydata.org/docs/reference/api/pandas.Series.plot.line.html)([x, y])
  - Gráfica de líneas
* - [Series.plot.pie](https://pandas.pydata.org/docs/reference/api/pandas.Series.plot.pie.html)(**kwargs)
  - Genera un diagrama circular.
```

<br/>

---
### Índice

Métodos para operaciones con el `Index`, los niveles y las etiquetas del mismo en un objeto `Series`. 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [Series.add_prefix](http://pandas.pydata.org/docs/reference/api/pandas.Series.add_prefix.html)(prefix[, axis])
  - Agrega un prefijo a las etiquetas del `Index`.
* - [Series.add_suffix](http://pandas.pydata.org/docs/reference/api/pandas.Series.add_suffix.html)(suffix[, axis])
  - Agrega un sufijo a las etiquetas del `Index`.
* - [Series.align](http://pandas.pydata.org/docs/reference/api/pandas.Series.align.html)(other[, join, axis, level, ...])
  - Alinea el índice de dos objetos con el método de unión especificado. Este método sirve para igualar el índice de un objeto con base a otro, los índice nuevos por default tendrán `NA`. 
* - [Series.droplevel](http://pandas.pydata.org/docs/reference/api/pandas.Series.droplevel.html)(level[, axis])
  - Elimina un nivel del `Index` de un `Series`.
* - [Series.first_valid_index](http://pandas.pydata.org/docs/reference/api/pandas.Series.first_valid_index.html)()
  - Retorna el primer índice cuyo valor no sea `NA`, retorna `None` si no se encuentra ningún valor que no sea `NA`.
* - [Series.idxmax](http://pandas.pydata.org/docs/reference/api/pandas.Series.idxmax.html)([axis, skipna])
  - Retorna la etiqueta de fila del valor máximo.
* - [Series.idxmin](http://pandas.pydata.org/docs/reference/api/pandas.Series.idxmin.html)([axis, skipna])
  - Retorna la etiqueta de fila del valor mínimo.
* - [Series.last_valid_index](http://pandas.pydata.org/docs/reference/api/pandas.Series.last_valid_index.html)()
  - Retorna el último índice cuyo valor no sea `NA`, retorna `None` si no se encuentra ningún valor que no sea `NA`.
* - [Series.reindex](http://pandas.pydata.org/docs/reference/api/pandas.Series.reindex.html)([index, axis, method, copy, ...])
  - Modifica el índice de un `Series`.
* - [Series.reindex_like](http://pandas.pydata.org/docs/reference/api/pandas.Series.reindex_like.html)(other[, method, copy, ...])
  - Modifica el índice de un `Series` con base al índice de otro objeto.
* - [Series.rename](http://pandas.pydata.org/docs/reference/api/pandas.Series.rename.html)([index, axis, copy, inplace, ...])
  - Modifica el nombre o las etiquetas del índice del objeto.
* - [Series.rename_axis](http://pandas.pydata.org/docs/reference/api/pandas.Series.rename_axis.html)([mapper, index, axis, ...])
  - Renombra el índice del objeto.
* - [Series.reorder_levels](http://pandas.pydata.org/docs/reference/api/pandas.Series.reorder_levels.html)(order)
  - Reorganiza los niveles del índice usando el orden de entrada.
* - [Series.reset_index](http://pandas.pydata.org/docs/reference/api/pandas.Series.reset_index.html)([level, drop, name, ...])
  - Reestablece el `Index` del objeto, al índice numérico, empezando en cero.
* - [Series.set_axis](http://pandas.pydata.org/docs/reference/api/pandas.Series.set_axis.html)(labels, *[, axis, copy])
  - Asigna el índice deseado al eje dado.
* - [Series.swaplevel](http://pandas.pydata.org/docs/reference/api/pandas.Series.swaplevel.html)([i, j, copy])
  - Intercambia los niveles `i` y `j` en un `MultiIndex`.
```

<br/>

---
### Manipulación

Métodos para manipulación de los elementos en el `Series` como eliminar valores, reemplazar valores, repetir elementos, manipulación del _shape_, etc. 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [Series.case_when](http://pandas.pydata.org/docs/reference/api/pandas.Series.case_when.html)(caselist)
  - Reemplaza valores donde las condiciones sean `True`.
* - [Series.compare](http://pandas.pydata.org/docs/reference/api/pandas.Series.compare.html)(other[, align_axis, ...])
  - Realiza una comparación con otro `Series` y muestra las diferencias.
* - [Series.combine](http://pandas.pydata.org/docs/reference/api/pandas.Series.combine.html)(other, func[, fill_value])
  - Combina el `Series` con otro o un escalar según una función `func`.
* - [Series.combine_first](http://pandas.pydata.org/docs/reference/api/pandas.Series.combine_first.html)(other)
  - Actualiza los elementos nulos con valor en la misma ubicación en `other`.
* - [Series.drop](http://pandas.pydata.org/docs/reference/api/pandas.Series.drop.html)([labels, axis, index, columns, ...])
  - Retorna `Series` con las etiquetas de índice especificadas eliminadas.
* - [Series.mask](http://pandas.pydata.org/docs/reference/api/pandas.Series.mask.html)(cond[, other, inplace, axis, level])
  - Reemplaza valores donde la condición es `True`.
* - [Series.repeat](http://pandas.pydata.org/docs/reference/api/pandas.Series.repeat.html)(repeats[, axis])
  - Repite elementos de un `Series`.
* - [Series.replace](http://pandas.pydata.org/docs/reference/api/pandas.Series.replace.html)([to_replace, value, inplace, ...])
  - Reemplaza los valores `to_replace` con `value`.
* - [Series.unstack](http://pandas.pydata.org/docs/reference/api/pandas.Series.unstack.html)([level, fill_value, sort])
  - Convierte un `Series` con `MultiIndex` en `DataFrame`.
* - [Series.update](http://pandas.pydata.org/docs/reference/api/pandas.Series.update.html)(other)
  - Modifica el `Series` "_in-place_" usando valores de otros `Series`. Se alinean con base al `Index`.
* - [Series.where](http://pandas.pydata.org/docs/reference/api/pandas.Series.where.html)(cond[, other, inplace, axis, level])
  - Reemplaza valores donde la condición es `False`.
```

<br/>

---
### Numéricas

#### Redondear y truncar

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [Series.clip](http://pandas.pydata.org/docs/reference/api/pandas.Series.clip.html)([lower, upper, axis, inplace])
  - Ajusta los valores para que estén en el intervalo `[lower, upper]`.
* - [Series.round](http://pandas.pydata.org/docs/reference/api/pandas.Series.round.html)([decimals])
  - Redondea cada valor en un `Series` al número de decimales dado.
```

<br/>

#### Información

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [Series.is_monotonic_decreasing](http://pandas.pydata.org/docs/reference/api/pandas.Series.is_monotonic_decreasing.html)()
  - Retorna booleano si los valores del objeto disminuyen monótonamente.
* - [Series.is_monotonic_increasing](http://pandas.pydata.org/docs/reference/api/pandas.Series.is_monotonic_increasing.html)()
  - Retorna booleano si los valores del objeto aumentan monótonamente.
```

<br/>

---
### Ordenar

Métodos útiles para ordenar un `Series`. 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [Series.argsort](http://pandas.pydata.org/docs/reference/api/pandas.Series.argsort.html)([axis, kind, order, stable])
  - Retorna los índices enteros que ordenarían el `Series`.
* - [Series.explode](http://pandas.pydata.org/docs/reference/api/pandas.Series.explode.html)([ignore_index])
  - Transforma un `Series` cuyos elementos son `list-like`, en un `Series` donde cada elemento de los `list-like` se convierte en una fila en el `Series`, las nuevas filas mantendrán el mismo índice que la lista original.
* - [Series.searchsorted](http://pandas.pydata.org/docs/reference/api/pandas.Series.searchsorted.html)(value[, side, sorter])
  - Determina los índices donde se deben insertar elementos para mantener el orden.
* - [Series.sort_index](http://pandas.pydata.org/docs/reference/api/pandas.Series.sort_index.html)(*[, axis, level, ...])
  - Ordena el `Series` con base a las etiquetas del índice.
* - [Series.sort_values](http://pandas.pydata.org/docs/reference/api/pandas.Series.sort_values.html)(*[, axis, ascending, ...])
  - Ordena el `Series` por los valores del mismo.
```

<br/>

---
### Selección, filtrado e iteración de elementos

Métodos útiles para seleccionar elementos con base a etiquetas, índices o condiciones o para iterar en ellos. 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [Series.\_\_iter__](http://pandas.pydata.org/docs/reference/api/pandas.Series.__iter__.html)()
  - Retorna un `iterator` de los valores.
* - [Series.at](http://pandas.pydata.org/docs/reference/api/pandas.Series.at.html)()
  - Accede a un valor único dada una etiqueta del índice. Similar a `Series.loc[]`.
* - [Series.filter](http://pandas.pydata.org/docs/reference/api/pandas.Series.filter.html)([items, like, regex, axis])
  - Retorna un subconjunto de las filas según las etiquetas de índice especificadas.
* - [Series.get](http://pandas.pydata.org/docs/reference/api/pandas.Series.get.html)(key[, default])
  - Accede a un valor único dada una etiqueta del índice. Similar a `Series.loc[]`.
* - [Series.head](http://pandas.pydata.org/docs/reference/api/pandas.Series.head.html)([n])
  - Retorna las primeras _n_ filas.
* - [Series.iat](http://pandas.pydata.org/docs/reference/api/pandas.Series.iat.html)()
  - Accede a un valor único dada una posición del índice. Similar a `Series.iloc[]`.
* - [Series.iloc](http://pandas.pydata.org/docs/reference/api/pandas.Series.loc.html)()
  - Accede a un valor o un conjunto de valores dadas las posiciones del índice o un `array-like` booleano.
* - [Series.item](http://pandas.pydata.org/docs/reference/api/pandas.Series.item.html)()
  - Retorna el primer elemento de los datos subyacentes como un escalar de Python.
* - [Series.items](http://pandas.pydata.org/docs/reference/api/pandas.Series.items.html)()
  - Retorna un `iterable` de tuplas `(index, value)`.
* - [Series.keys](http://pandas.pydata.org/docs/reference/api/pandas.Series.keys.html)()
  - Alias ​​para `Index`.
* - [Series.loc](http://pandas.pydata.org/docs/reference/api/pandas.Series.loc.html)()
  - Accede a un valor o un conjunto de valores dadas las etiquetas del índice o un `array-like` booleano.
* - [Series.pop](http://pandas.pydata.org/docs/reference/api/pandas.Series.pop.html)(item)
  - Elimina y retorna un elemento dada su etiqueta.
* - [Series.tail](http://pandas.pydata.org/docs/reference/api/pandas.Series.tail.html)([n])
  - Retorna las últimas _n_ filas.
* - [Series.take](http://pandas.pydata.org/docs/reference/api/pandas.Series.take.html)(indices[, axis])
  - Retorna los elementos en los índices posicionales dados a lo largo de un eje. Los índices se pueden repetir. Es similar a hacer _fancy indexing_ con índices implícitos.
* - [Series.truncate](http://pandas.pydata.org/docs/reference/api/pandas.Series.truncate.html)([before, after, axis, copy])
  - Trunca un `Series` antes y después de algún valor de índice.
* - [Series.xs](http://pandas.pydata.org/docs/reference/api/pandas.Series.xs.html)(key[, axis, level, drop_level])
  - Retorna la sección transversal del `Series`. Particurlamente útil cuando el `Series` tiene un `MultiIndex` y se quiere acceder a secciones enteras de un nivel o combinaciones de los niveles/subniveles.
```

<br/>

---
### Valores duplicados

Métodos útiles para el manejo de valores duplicados. 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [Series.drop_duplicates](http://pandas.pydata.org/docs/reference/api/pandas.Series.drop_duplicates.html)(*[, keep, inplace, ...])
  - Retorna `Series` con valores duplicados eliminados.
* - [Series.duplicated](http://pandas.pydata.org/docs/reference/api/pandas.Series.duplicated.html)([keep])
  - Indica si los valores del `Series` 
```

<br/>

---
### Valores perdidos

Métodos útiles para el manejo de valores perdidos. 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [Series.bfill](http://pandas.pydata.org/docs/reference/api/pandas.Series.bfill.html)(*[, axis, inplace, limit, ...])
  - Reemplaza los valores `NA/NaN` utilizando la siguiente observación válida.
* - [Series.dropna](http://pandas.pydata.org/docs/reference/api/pandas.Series.dropna.html)(*[, axis, inplace, how, ...])
  - Retorna un nuevo `Series` con los valores perdidos eliminados.
* - [Series.ffill](http://pandas.pydata.org/docs/reference/api/pandas.Series.ffill.html)(*[, axis, inplace, limit, ...])
  - Reemplaza los valores `NA/NaN` utilizando la última observación válida.
* - [Series.fillna](http://pandas.pydata.org/docs/reference/api/pandas.Series.fillna.html)([value, method, axis, ...])
  - Reemplaza los valores `NA/NaN` utilizando el método especificado.
* - [Series.interpolate](http://pandas.pydata.org/docs/reference/api/pandas.Series.interpolate.html)([method, axis, limit, ...])
  - Reemplaza los valores de `NaN` utilizando un método de interpolación.
* - [Series.isna](http://pandas.pydata.org/docs/reference/api/pandas.Series.isna.html)()
  - Indica para cada fila si el valor está perdido.
* - [Series.isnull](http://pandas.pydata.org/docs/reference/api/pandas.Series.isnull.html)()
  - Indica para cada fila si el valor está perdido. Similar a `Series.isna`.
* - [Series.notna](http://pandas.pydata.org/docs/reference/api/pandas.Series.notna.html)()
  - Indica para cada fila si el valor no está perdido.
* - [Series.notnull](http://pandas.pydata.org/docs/reference/api/pandas.Series.notnull.html)()
  - Indica para cada fila si el valor no está perdido. Similar a `Series.notna`.
```

<br/>

### Valores únicos

Métodos para obtener información sobre valores únicos en el `Series`.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [Series.is_unique](http://pandas.pydata.org/docs/reference/api/pandas.Series.is_unique.html)()
  - Indica si los valores del objeto son únicos.
* - [Series.nunique](http://pandas.pydata.org/docs/reference/api/pandas.Series.nunique.html)([dropna])
  - Retorna el número de elementos únicos en el objeto.
* - [Series.unique](http://pandas.pydata.org/docs/reference/api/pandas.Series.unique.html)()
  - Retorna los valores únicos del `Series`.
* - [Series.value_counts](http://pandas.pydata.org/docs/reference/api/pandas.Series.value_counts.html)([normalize, sort, ...])
  - Retorna un `Series` que contiene recuentos de los valores únicos.
```

<br/>


---  
## Accesors

Los _accesors_ permiten acceder a métodos adicionales para `Series` de algún tipo de dato concreto. Existen 4 tipos de _accesors_:


|Data Type| Accessor|
|---|---|
|`datetime`, `timedelta`, `period`| dt|
|`str` |str|
|`categorical`| cat|
|`sparse` | sparse |


### Accesor Categórico

Este _accesor_ es para `Series` de tipo `categorical`. 

#### Atributos


```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - [Series.cat.categories](http://pandas.pydata.org/docs/reference/api/pandas.Series.cat.categories.html)
  - Retorna las categorías únicas.
* - [Series.cat.codes](http://pandas.pydata.org/docs/reference/api/pandas.Series.cat.codes.html)
  - Retorna el índice asociado a cada categoría de cada observación en el objeto.
* - [Series.cat.ordered](http://pandas.pydata.org/docs/reference/api/pandas.Series.cat.ordered.html)
  - Indica si las categorías del objeto tienen un orden. Esta propiedad se puede manipular con los métodos `.cat.as_ordered` y `.cat.as_unordered`.
```

#### Métodos

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [Series.cat.add_categories](http://pandas.pydata.org/docs/reference/api/pandas.Series.cat.add_categories.html)(*args, **kwargs)
  - Añade nuevas categorías.
* - [Series.cat.as_ordered](http://pandas.pydata.org/docs/reference/api/pandas.Series.cat.as_ordered.html)(*args, **kwargs)
  - Establece que las categorías están ordendas, esto no significa que efectivamente las categorías estén ordenadas de alguna forma en particular.
* - [Series.cat.as_unordered](http://pandas.pydata.org/docs/reference/api/pandas.Series.cat.as_unordered.html)(*args, **kwargs)
  - Establece que las categorías están desordendas, esto no significa que efectivamente las categorías estén desordenadas.
* - [Series.cat.remove_categories](http://pandas.pydata.org/docs/reference/api/pandas.Series.cat.remove_categories.html)(*args, **kwargs)
  - Elimina las categorías especificadas.
* - [Series.cat.remove_unused_categories](http://pandas.pydata.org/docs/reference/api/pandas.Series.cat.remove_unused_categories.html)(*args, ...)
  - Elimina las categorías que no se utilizan.
* - [Series.cat.rename_categories](http://pandas.pydata.org/docs/reference/api/pandas.Series.cat.rename_categories.html)(*args, **kwargs)
  - Reenombra determinadas categorías.
* - [Series.cat.reorder_categories](http://pandas.pydata.org/docs/reference/api/pandas.Series.cat.reorder_categories.html)(*args, **kwargs)
  - Reordena las categorías como se especifica en _new\_categories_.
* - [Series.cat.set_categories](http://pandas.pydata.org/docs/reference/api/pandas.Series.cat.set_categories.html)(*args, **kwargs)
  - Establece las categorías en las nuevas categorías especificadas.
```

<br/>

---
### Accesor de _sparse_

Este _accesor_ es para `Series` de tipo `sparse`.

#### Atributos

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - [Series.sparse.density](http://pandas.pydata.org/docs/reference/api/pandas.Series.sparse.density.html)()
  - El porcentaje de puntos no-`fill_value`, como decimal.
* - [Series.sparse.fill_value](http://pandas.pydata.org/docs/reference/api/pandas.Series.sparse.fill_value.html)()
  - Los elementos de los datos que son `fill_value` no se almacenan.
* - [Series.sparse.npoints](http://pandas.pydata.org/docs/reference/api/pandas.Series.sparse.npoints.html)()
  - El número de puntos no-`fill_value`.
* - [Series.sparse.sp_values](http://pandas.pydata.org/docs/reference/api/pandas.Series.sparse.sp_values.html)()
  - Un `ndarray` que contiene los valores no-`fill_value`.
```

#### Métodos

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [Series.sparse.from_coo](http://pandas.pydata.org/docs/reference/api/pandas.Series.sparse.from_coo.html)(A[, dense_index])
  - Crea un `Series` con valores _sparse_ desde `scipy.sparse.coo_matrix()`.
* - [Series.sparse.to_coo](http://pandas.pydata.org/docs/reference/api/pandas.Series.sparse.to_coo.html)([row_levels, ...])
  - Crea un `scipy.sparse.coo_matrixU a partir de un `Series` con `MultiIndex`.
```

<br/>

---
### Accesor de `str`

Este _accesor_ es para `Series` de tipo `str`.

:::{tip}
La gran mayoría de métodos de esta función también funcionan con objetos `Index` de tipo `str`.
:::

:::{tip}
Algunos de estos métodos también funcionan incluso si los elementos del `Series` no son `str`, pero sí son de algún tipo `sequence`.
:::

#### Subsetting y Slicing

Es posible hacer _subsetting_ y _slicing_ de manera vectorizada (se aplicará el _subsetting_ o _slicing_ a cada valor del `Series`), para ello simplemente utilizar corchetes, junto con el nombre del objeto y `.str`:
```python
# Subsetting.
X.str[i]
	
# Slicing.
X.str[start:stop:step]
```
- `X` `Series` de `str` o `sequence`.

:::{tip}
Equivalentemente se pueden usar los métodos `Series.str.get()` y `Series.str.slice()` para obtener los mismos resultados.
:::

:::{warning}
No es posible usar las estrategias de _fancy indexing_ ni _boolean masking_.
:::

<br/>

#### Buscar subcadenas

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [Series.str.find](http://pandas.pydata.org/docs/reference/api/pandas.Series.str.find.html)(sub[, start, end])
  - Devuelve la primer posición en cada cadena donde se encuentra una subcadena, si no encuentra la subcadena retorna `-1`.
* - [Series.str.index](http://pandas.pydata.org/docs/reference/api/pandas.Series.str.index.html)(sub[, start, end])
  - Devuelve la primer posición en cada cadena donde se encuentra una subcadena. Si no encuentra la subcadena devuelve `ValueError`.
* - [Series.str.rfind](http://pandas.pydata.org/docs/reference/api/pandas.Series.str.rfind.html)(sub[, start, end])
  - Devuelve la última posición en cada cadena donde se encuentra una subcadena, si no encuentra la subcadena retorna `-1`.
* - [Series.str.rindex](http://pandas.pydata.org/docs/reference/api/pandas.Series.str.rindex.html)(sub[, start, end])
  - Devuelve la última posición en cada cadena donde se encuentra una subcadena. Si no encuentra la subcadena devuelve `ValueError`.
```

<br/>

#### Concatenación y separaciones

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [Series.str.cat](http://pandas.pydata.org/docs/reference/api/pandas.Series.str.cat.html)([others, sep, na_rep, join])
  - Concatena cadenas en el objeto con otras cadenas con el separador dado.
* - [Series.str.join](http://pandas.pydata.org/docs/reference/api/pandas.Series.str.join.html)(sep)
  - Concatena `sequence` en el objeto con el delimitador indicado.
* - [Series.str.partition](http://pandas.pydata.org/docs/reference/api/pandas.Series.str.partition.html)([sep, expand])
  - Divide la cadena en tres partes en la primera aparición de `sep`.
* - [Series.str.repeat](http://pandas.pydata.org/docs/reference/api/pandas.Series.str.repeat.html)(repeats)
  - Duplica cada cadena en el objeto un número determinado de veces.
* - [Series.str.rpartition](http://pandas.pydata.org/docs/reference/api/pandas.Series.str.rpartition.html)([sep, expand])
  - Divida la cadena en tres partes en la última aparición de `sep`.
* - [Series.str.rsplit](http://pandas.pydata.org/docs/reference/api/pandas.Series.str.rsplit.html)([pat, n, expand])
  - Retorna una lista de subcadenas de cada elemento del objeto de acuero al delimitador dado, patrón o expresión regular.
* - [Series.str.split](http://pandas.pydata.org/docs/reference/api/pandas.Series.str.split.html)([pat, n, expand, regex])
  - Retorna una lista de subcadenas de cada elemento del objeto de acuero al delimitador dado, patrón o expresión regular.
```

<br/>

#### Formatos y modificaciones

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [Series.str.capitalize](http://pandas.pydata.org/docs/reference/api/pandas.Series.str.capitalize.html)()
  - Convierte las cadenas en el objeto en mayúsculas.
* - [Series.str.casefold](http://pandas.pydata.org/docs/reference/api/pandas.Series.str.casefold.html)()
  - Convierte las cadenas en el objeto en minúsculas de manera más estricta que `str.lower()`.
* - [Series.str.lower](http://pandas.pydata.org/docs/reference/api/pandas.Series.str.lower.html)()
  - Convierte las cadenas en el objeto en minúsculas.
* - [Series.str.normalize](http://pandas.pydata.org/docs/reference/api/pandas.Series.str.normalize.html)(form)
  - Retorna la forma normal Unicode para las cadenas en el objeto.
* - [Series.str.swapcase](http://pandas.pydata.org/docs/reference/api/pandas.Series.str.swapcase.html)()
  - Convierte las cadenas en el objeto intercambiando las mayúsculas y las minúsculas.
* - [Series.str.title](http://pandas.pydata.org/docs/reference/api/pandas.Series.str.title.html)()
  - Convierte las cadenas en el objeto a formato de título, es decir, la primer letras de cada palabra en mayúsculas y el resto en minúsculas.
* - [Series.str.upper](http://pandas.pydata.org/docs/reference/api/pandas.Series.str.upper.html)()
  - Convierte las cadenas en el objeto a mayúsculas.
```

<br/>

#### Información

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [Series.str.count](http://pandas.pydata.org/docs/reference/api/pandas.Series.str.count.html)(pat[, flags])
  - Cuenta las apariciones de un patrón o expresión regular `pat` en cada cadena del objeto.
* - [Series.str.endswith](http://pandas.pydata.org/docs/reference/api/pandas.Series.str.endswith.html)(pat[, na])
  - Verifica si el final de cada elemento de cadena coincide con un patrón.
* - [Series.str.isalnum](http://pandas.pydata.org/docs/reference/api/pandas.Series.str.isalnum.html)()
  - Verifica si todos los caracteres de cada cadena son alfanuméricos.
* - [Series.str.isalpha](http://pandas.pydata.org/docs/reference/api/pandas.Series.str.isalpha.html)()
  - Verifica si todos los caracteres de cada cadena son alfabéticos.
* - [Series.str.isdecimal](http://pandas.pydata.org/docs/reference/api/pandas.Series.str.isdecimal.html)()
  - Verifica si todos los caracteres de cada cadena son decimales.
* - [Series.str.isdigit](http://pandas.pydata.org/docs/reference/api/pandas.Series.str.isdigit.html)()
  - Verifica si todos los caracteres de cada cadena son dígitos.
* - [Series.str.islower](http://pandas.pydata.org/docs/reference/api/pandas.Series.str.islower.html)()
  - Verifica si todos los caracteres de cada cadena están en minúsculas.
* - [Series.str.isnumeric](http://pandas.pydata.org/docs/reference/api/pandas.Series.str.isnumeric.html)()
  - Verifica si todos los caracteres de cada cadena son numéricos.
* - [Series.str.isspace](http://pandas.pydata.org/docs/reference/api/pandas.Series.str.isspace.html)()
  - Verifica si todos los caracteres de cada cadena son espacios en blanco.
* - [Series.str.istitle](http://pandas.pydata.org/docs/reference/api/pandas.Series.str.istitle.html)()
  - Verifica si todos los caracteres de cada cadena son mayúsculas y minúsculas.
* - [Series.str.isupper](http://pandas.pydata.org/docs/reference/api/pandas.Series.str.isupper.html)()
  - Verifica si todos los caracteres de cada cadena están en mayúsculas.
* - [Series.str.len](http://pandas.pydata.org/docs/reference/api/pandas.Series.str.len.html)()
  - Determina la longitud de cada elemento en el objeto.
* - [Series.str.startswith](http://pandas.pydata.org/docs/reference/api/pandas.Series.str.startswith.html)(pat[, na])
  - Pruebe si el inicio de cada elemento de cadena coincide con un patrón.
```

<br/>

#### Otros y dummies

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [Series.str.decode](http://pandas.pydata.org/docs/reference/api/pandas.Series.str.decode.html)(encoding[, errors])
  - Decodifica la cadena de caracteres en el objeto usando la codificación indicada.
* - [Series.str.encode](http://pandas.pydata.org/docs/reference/api/pandas.Series.str.encode.html)(encoding[, errors])
  - Codifica la cadena de caracteres en el objeto usando la codificación indicada.
* - [Series.str.get_dummies](http://pandas.pydata.org/docs/reference/api/pandas.Series.str.get_dummies.html)([sep])
  - Retorna un `DataFrame` de variables _dummies_ (convierte variables categóricas en columnas que indican si cada fila contiene esa categoría).
```

<br/>

#### Reemplazar y eliminar subcadenas

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [Series.str.removeprefix](http://pandas.pydata.org/docs/reference/api/pandas.Series.str.removeprefix.html)(prefix)
  - Elimina un prefijo en las cadenas del objeto.
* - [Series.str.removesuffix](http://pandas.pydata.org/docs/reference/api/pandas.Series.str.removesuffix.html)(suffix)
  - Elimina un sufijo en las cadenas del objeto.
* - [Series.str.replace](http://pandas.pydata.org/docs/reference/api/pandas.Series.str.replace.html)(pat, repl[, n, case, ...])
  - Reemplaza cada aparición de `pat` en el objeto con otra subcadena.
* - [Series.str.slice_replace](http://pandas.pydata.org/docs/reference/api/pandas.Series.str.slice_replace.html)([start, stop, repl])
  - Reemplaza un segmento posicional de una cadena con otro valor.
* - [Series.str.translate](http://pandas.pydata.org/docs/reference/api/pandas.Series.str.translate.html)(table)
  - Asigna todos los caracteres de la cadena a través de la tabla de mapeo proporcionada.
```

<br/>

#### Regular expressions

Métodos que pueden utilizar expresiones regulares con argumentos.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [Series.str.contains](http://pandas.pydata.org/docs/reference/api/pandas.Series.str.contains.html)(pat[, case, flags, na, ...])
  - verifica si el patrón o la expresión regular están contenidos dentro de las cadenas del objeto.
* - [Series.str.count](http://pandas.pydata.org/docs/reference/api/pandas.Series.str.count.html)(pat[, flags])
  - Cuenta las apariciones de un patrón o la expresión regular `pat` en cada cadena del objeto.
* - [Series.str.extract](http://pandas.pydata.org/docs/reference/api/pandas.Series.str.extract.html)(pat[, flags, expand])
  - Extrae grupos de captura en la expresión regular `pat` como columnas en un `DataFrame`.
* - [Series.str.extractall](http://pandas.pydata.org/docs/reference/api/pandas.Series.str.extractall.html)(pat[, flags])
  - Extrae los grupos de captura en la expresión regular `pat` como columnas en `DataFrame`.
* - [Series.str.findall](http://pandas.pydata.org/docs/reference/api/pandas.Series.str.findall.html)(pat[, flags])
  - Determina todas las apariciones de patrones o expresiones regulares en el objeto.
* - [Series.str.fullmatch](http://pandas.pydata.org/docs/reference/api/pandas.Series.str.fullmatch.html)(pat[, case, flags, na])
  - Determine si cada cadena coincide completamente con una expresión regular.
* - [Series.str.match](http://pandas.pydata.org/docs/reference/api/pandas.Series.str.match.html)(pat[, case, flags, na])
  - Determine si cada cadena comienza con una coincidencia de una expresión regular.
* - [Series.str.rsplit](http://pandas.pydata.org/docs/reference/api/pandas.Series.str.rsplit.html)([pat, n, expand])
  - Retorna una lista de subcadenas de cada elemento del objeto de acuero al delimitador dado, patrón o expresión regular.
* - [Series.str.split](http://pandas.pydata.org/docs/reference/api/pandas.Series.str.split.html)([pat, n, expand, regex])
  - Retorna una lista de subcadenas de cada elemento del objeto de acuero al delimitador dado, patrón o expresión regular.
```

<br/>

### Selección

Métodos para seleccionar elementos en índices específicos o _slices_ de elementos en la secuencia.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [Series.str.get](http://pandas.pydata.org/docs/reference/api/pandas.Series.str.get.html)(i)
  - Extre el elemento de cada componente en la posición especificada o con la clave especificada. Equivale a usar `Series.str[i]`.
* - [Series.str.slice](http://pandas.pydata.org/docs/reference/api/pandas.Series.str.slice.html)([start, stop, step])
  - Corta subcadenas de cada elemento en el objeto. Equivale a usar `Series.str[start:stop:step]`.
```

<br/>

#### Strips y pads

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [Series.str.center](http://pandas.pydata.org/docs/reference/api/pandas.Series.str.center.html)(width[, fillchar])
  - Convierte las cadenas agregando caracteres al princio y al final, para que tengan una longitud determinada y las cadenas originales estén al centro.
* - [Series.str.ljust](http://pandas.pydata.org/docs/reference/api/pandas.Series.str.ljust.html)(width[, fillchar])
  - Convierte las cadenas agregando algún caracter al lado derecho de las cadenas para que tengan una longitud determinada.
* - [Series.str.lstrip](http://pandas.pydata.org/docs/reference/api/pandas.Series.str.lstrip.html)([to_strip])
  - Elimina los personajes principales.
* - [Series.str.pad](http://pandas.pydata.org/docs/reference/api/pandas.Series.str.pad.html)(width[, side, fillchar])
  - Rellena las cadenas en el objeto hasta el ancho indicado con un caracter indicado, se puede indicar en qué lado añadir los caracteres.
* - [Series.str.rjust](http://pandas.pydata.org/docs/reference/api/pandas.Series.str.rjust.html)(width[, fillchar])
  - Convierte las cadenas agregando algún caracter al lado izquierdo de las cadenas para que tengan una longitud determinada.
* - [Series.str.strip](http://pandas.pydata.org/docs/reference/api/pandas.Series.str.strip.html)([to_strip])
  - Elimina los caracteres iniciales y finales.
* - [Series.str.wrap](http://pandas.pydata.org/docs/reference/api/pandas.Series.str.wrap.html)(width, **kwargs)
  - Convierte las cadenas en el objeto agregando caracteres al princio y al final, para que tengan una longitud determinada y las cadenas originales estén al centro
* - [Series.str.zfill](http://pandas.pydata.org/docs/reference/api/pandas.Series.str.zfill.html)(width)
  - Convierte las cadenas en el objeto anteponiendo caracteres '0', para que tengan una longitud determinada.
```

<br/>

### Accesor de fechas y tiempo

#### Atributos de `datetime`

A continuación se enlistan algunas propiedades de `Series` de tipo `datetime64`. Para retornar partes específicas de las fechas, usar:

```python
# Recuperar un atributo
X.dt.part
```
- X `Series` de `datetime64`.
- _part_: Es cualquiera de los siguientes:
    - `date`: Retorna la parte de la fecha, sin tiempo.
    - `time`: Retorna la parte del tiempo, sin la fecha.
    - `year` \- `int`: Retorna el año.
    - `month` \- `int`: Retorna el mes.
    - `day` \- `int`: Retorna el día.
    - `hour` \- `int`: Retorna la hora.
    - `minute` \- `int`: Retorna los minutos.
    - `second` \- `int`: Retorna los segundos.
    - `microsecond` \- `int`: Retorna los milisegundos.
    - `nanosecond` \- `int`: Retorna los nanosegundos.
    - `second` \- `int`: Retorna los segundos.
    - `dayofweek`  \- `int`: Retorna el día de la semana, donde lunes es cero y domingo es 6. Lo mismo que usar `day_of_week` o `weekday`.
    - `dayofyear`  \- `int`: Retorna el día del año. Lo mismo que usar `day_of_year`.   
    - `daysinmonth`  \- `int`: Retorna cuántos días hay en ese mes. Lo mismo que `days_in_month`.
    - `quarter`  \- `int`: Retorna el trimestre.
    - `is_leap_year` \- `bool`: Indica si el año bisiesto.
    - `is_month_start` \- `bool`: Indica si el día el comienzo de un mes.
    - `is_month_end` \- `bool`: Indica si el día el final de un mes.
    - `is_year_start` \- `bool`: Indica si el día el comienzo de un año.
    - `is_year_end` \- `bool`: Indica si el día el final de un año.
    - Para una lista completa visitar la [documentación de pandas](https://pandas.pydata.org/docs/reference/series.html#datetime-properties).

<br/>

---
#### Métodos de `datetime`

Métodos para `Series` de tipo `datetime64`.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [Series.dt.ceil](http://pandas.pydata.org/docs/reference/api/pandas.Series.dt.ceil.html)(*args, **kwargs)
  - "Redondea" los datos hacía arriba a la frecuencia especificada.
* - [Series.dt.day_name](http://pandas.pydata.org/docs/reference/api/pandas.Series.dt.day_name.html)(*args, **kwargs)
  - Retorna los nombres de los días con la configuración regional especificada.
* - [Series.dt.floor](http://pandas.pydata.org/docs/reference/api/pandas.Series.dt.floor.html)(*args, **kwargs)
  - "Redondea" los datos hacía arriba a la frecuencia especificada.
* - [Series.dt.isocalendar](http://pandas.pydata.org/docs/reference/api/pandas.Series.dt.isocalendar.html)()
  - Determina el año, semana y día según la norma _ISO 8601_.
* - [Series.dt.month_name](http://pandas.pydata.org/docs/reference/api/pandas.Series.dt.month_name.html)(*args, **kwargs)
  - Retorna los nombres de los meses con la configuración regional especificada.
* - [Series.dt.normalize](http://pandas.pydata.org/docs/reference/api/pandas.Series.dt.normalize.html)(*args, **kwargs)
  - Convierte las horas a medianoche.
* - [Series.dt.round](http://pandas.pydata.org/docs/reference/api/pandas.Series.dt.round.html)(*args, **kwargs)
  - "Redondea" los datos a la frecuencia especificada.
* - [Series.dt.strftime](http://pandas.pydata.org/docs/reference/api/pandas.Series.dt.strftime.html)(*args, **kwargs)
  - Convierte a `Index` utilizando el formato de fecha especificado.
* - [Series.dt.to_period](http://pandas.pydata.org/docs/reference/api/pandas.Series.dt.to_period.html)(*args, **kwargs)
  - Convierte a `PeriodArray`/`PeriodIndex` en una frecuencia particular.
* - [Series.dt.tz_convert](http://pandas.pydata.org/docs/reference/api/pandas.Series.dt.tz_convert.html)(*args, **kwargs)
  - Convierta un arreglo/índice de fecha y hora compatible con _tz_ de una zona horaria a otra.
* - [Series.dt.tz_localize](http://pandas.pydata.org/docs/reference/api/pandas.Series.dt.tz_localize.html)(*args, **kwargs)
  - Convierte un arreglo/índice de fecha y hora con _tz-naive_ en un arreglo/índice de fecha y hora compatible con _tz_.
```

<br/>

#### Atributos de `period`

Atributos para `Series` de tipo `period`.

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - [Series.dt.end_time](http://pandas.pydata.org/docs/reference/api/pandas.Series.dt.end_time.html)
  - Recupera el _Timestamp_ del final del período.
* - [Series.dt.start_time](http://pandas.pydata.org/docs/reference/api/pandas.Series.dt.start_time.html)
  - Recupera el _Timestamp_ del inicio del período.
```

<br/>

#### Atributos de `TimeDelta`

Atributos para `Series` de tipo `period`.

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - [Series.dt.components](http://pandas.pydata.org/docs/reference/api/pandas.Series.dt.components.html)
  - Retorna un `Dataframe` de los componentes de `TimeDelta`.
* - [Series.dt.days](http://pandas.pydata.org/docs/reference/api/pandas.Series.dt.days.html)
  - Número de días para cada elemento.
* - [Series.dt.microseconds](http://pandas.pydata.org/docs/reference/api/pandas.Series.dt.microseconds.html)
  - Número de microsegundos (>= 0 y menor de 1 segundo) para cada elemento.
* - [Series.dt.nanoseconds](http://pandas.pydata.org/docs/reference/api/pandas.Series.dt.nanoseconds.html)
  - Número de nanosegundos (>= 0 y menos de 1 microsegundo) para cada elemento.
* - [Series.dt.seconds](http://pandas.pydata.org/docs/reference/api/pandas.Series.dt.seconds.html)
  - Número de segundos (>= 0 y menos de 1 día) para cada elemento.
```

<br/>

#### Métodos de `TimeDelta`

Métodos para `Series` de tipo `period`. 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [Series.dt.to_pytimedelta](http://pandas.pydata.org/docs/reference/api/pandas.Series.dt.to_pytimedelta.html)()
  - Devuelve un arreglo de objetos nativos `datetime.timedelta`.
* - [Series.dt.total_seconds](http://pandas.pydata.org/docs/reference/api/pandas.Series.dt.total_seconds.html)(*args, **kwargs)
  - Retorna la duración total de cada elemento expresada en segundos.
```

