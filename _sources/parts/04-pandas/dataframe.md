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

# DataFrame

`DataFrame` es una clase de `pandas` que podría interpretarse como un array bidimensional con etiquetas para identificar tanto a las filas como a las columnas, los elementos de cada columna deben de ser del mismo tipo, pero las columnas pueden ser de diferentes tipos. Los `DataFrame` tiene dos tipos de índices:
- **índice implícito**: Es un índice númerico, que comienza desde cero, similiar a los índices de las secuencias.
- **índice explícito**: Es el objeto `Index` asociado, que puede tener etiquetas `int` o `str`.

<br/>

---
(pandas-df-creacion)=
## Creación de `DataFrame`

La forma más sencilla de crear un objeto `DataFrame` es con el constructor.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [pandas.DataFrame](https://pandas.pydata.org/docs/reference/frame.html#constructor)([data, index, columns, dtype, copy])
  - Objeto bidimensional con columnas homogéneas para datos tabulares.
```
**Notas**:
- _data_: Es un objeto que contiene los datos, se puede definir de diversas formas:
    - Si es `dict` los _keys_ serán las etiquetas de las columnas y los _values_ pueden ser `Series`, `array-like` o `list`, todos de la misma longitud, serán los valores de las filas en sus respectivas columnas. De esta forma se llena columna por columna.
    - Si es un `list-like` anidado o un `array-like` 2D, cada elemento interno será una fila, por lo que todos los elementos deben de tener la misma longitud. De esta forma se llena fila por fila. Si se difine el parámetro _columns_ debe tener la misma logitud que las listas internas y si se define el parámetro _index_ debe de tener la misma longitud que la lista externa.
    - Si es un `dict` de `dict`, se interpreta como que los _outer keys_ son las etiquetas de las columnas y los _inner keys_ son las etiquetas de las filas y los _inner values_ son los valores del `DataFrame`.
    - Es posibles usar `list` de `dict`, donde los _keys_ serán las etiquetas de las columnas y los _values_ son los valores de una fila, cada `dict` represente una fila y por lo tanto los _keys_ de todos los diccionarios deben de ser los mismos, en caso de que haya _keys_ que no se comparten tendrán valores `NaN`.
- _index_: Es un `array-like` o un objeto `Index` con las etiquetas de las filas. Normalmente debe ser de la misma longitud que _data_. En caso de que _data_ sea `dict`, _index_ se puede usar para generar el `Series` con solo determinados índices-elementos, excluyendo los que no definan en este parámetro.    
- _columns_: Es un `array-like` o un objeto `Index` con las etiquetas de las columnas.

**Ejemplo**: A continuación se crea un objeto `DataFrame` que tiene la información de algunos estados de Estados Unidos, como su capital, población y área. Notar que los nombres de los estados son el índice explícito del `df`.

```{code-cell} ipython3
# Importar librería
import pandas as pd

# Crear diccionario con los datos
data = {
    'Capital': ['Sacramento', 'Austin', 'Tallahassee', 'Albany'],
    'Population': [39.24, 29.5, 21.96, 20.2],
    'Area (km2)': [423970, 695662, 170451, 122283]
}

# Crer df, aquí se indica el 'index'
df = pd.DataFrame(data, index = ['California', 'Texas', 'Florida', 'New York'])

# Imprimir el df
print(df)
```

<br/>

---
## Selección de elementos

Existen diversos métodos para seleccionar elementos en un `DataFrame`. Aquí se explicarán los más comunes. Todos los ejemplos de esta sección utilizará el `df` definido en [la sección anterior](pandas-df-creacion).


### Notación con corchetes

Al ser los `DataFrame` estructuras bidimensionales es posible seleccionar filas o columnas. Esto se puede hacer con los índices explícitos. <br/> **Importante**: El uso de los índices implícitos con esta notación está desaconsejado, para ello se recomienda usar el método `.iloc[]`.

- **Subsetting**: Seleccionar columnas concretas usando las etiquetas de las columnas.
  - **Columnas completas**  - `Series`: Para seleccionar una columna y retornar `Series`, utilizar corchetes y el nombre de la columna. También se puede utilizar la notación punto `.`, en este caso la etiqueta no debe tener espacios, ni caracteres especiales, ni ser una palabra reservada: <br/> `X['label']` <br/> `X.label`

<br/>

- **Fancy indexing**: Seleccionar un conjunto de columnas con base a las etiquetas. 
  - **Columnas completas** - `DataFrame`: Para seleccionar una columna y retornar `DataFrame`, utilizar dobles corchetes y el nombre de la columna: <br/> `X[['label']]`
  - **Múltiples columnas** - `DataFrame`: Para seleccionar múltiples columnas y retornar `DataFrame`, utilizar dobles corchetes y los nombres de las columnas. Las etiquetas se pueden poner en cualquier orden e incluso se pueden repetir múltiples veces: <br/> `X[['label1', 'label2', ...]]`

<br/>

- **Boolean masking**: Selección de filas para todas las columnas, con base a una _secuencia_ booleana de la misma longitud en el eje cero, denominada _mask_. Normalmente el _mask_ se crea usando una columna del `DataFrame` y {ref}`Operadores de comparación <built-in-operadores-comparacion>`: <br/> `X[mask]`

:::{tip}
Se pueden usar los operadores {ref}`built-in-operadores-bitwise` para crear mask más complejos: <br/> `X[(mask1) & (mask2)] # Ejemplo con '&'`
- Notar que cada mask se pone entre paréntesis.
- **No usar** los operadores lógicos para conformar _masks_ más complicados.
:::

<br/>

**Ejemplos**: A continuación se ejemplifica la selección de elementos con las diversas estategias en notación con conchetes en un `DataFrame`.

```{code-cell} ipython3
# Indexing: Seleccionar columna 'Population'
print(df['Population'], end="\n"*2)

# Fancy indexing: Seleccionar columna Population' y retornar DataFrame
print(df[['Population']], end="\n"*2)

# Fancy indexing: Seleccionar columnas 'Capital', 'Area (km2)' y 'Capital'
print(df[['Capital', 'Area (km2)', 'Capital']], end="\n"*2)

# Boolean masking: Seleccionar elementos pares
print(df[df['Area (km2)']>300000])
```

<br/>

---
### Usando método `.loc[]`

El método `.iloc[]` es útil para seleccionar elementos con base al **índice explícito**.

:::{attention}
En esta sección tener en cuenta las siguientes nomenclaturas:
- `'ind'`: Se refiere a una etiqueta del índice.
- `'col'`: Se refiere a una etiqueta de las columnas.
- `'indi':'indj'`: Se refiere a un _slice_, entre las etiquetas del índice 'indi' e 'indj'
- `'coli':'colj'`: Se refiere a un _slice_, entre las etiquetas de las columnas 'coli' y 'colj'
- `'ind1', 'ind2', ...`: Se refiere a varias etiquetas del índice.
- `'col1', 'col2', ...`: Se refiere a varias etiquetas de las columnas.
:::

- **Subsetting**: Útil para seleccionar elementos específicos.
	- **Elemento específico** - `scalar`: Retorna el elemento en las etiquetas _'ind'_ y _'col'_: <br/>  `X.loc['ind', 'col']`

<br/>

- **Slicing**: Útil para seleccionar _slices_ utilizando `start:stop:step`, tanto de filas como de columnas. Ambos extremos son inclusivos. Se separan los _slicers_ para las filas y las columnas con una coma.
	- **Slices de filas** - `DataFrame`: Retorna _slices_ de filas para todas las columnas: <br/> `X.loc['indi':'indj', :]` <br/> `X.loc['indi':'indj']`
	- **Slices de columnas** - `DataFrame`: Retorna _slices_ de columnas para todas las filas: <br/> `X.loc[:, 'coli':'colj']`
	- **Slices de filas y columnas** - `DataFrame`: Retorna _slices_ de filas y columnas específicas: <br/> `X.loc['indi':'indj', 'coli':'colj']`

<br/>

- **Fancy indexing**: Útil para seleccionar combinaciones de filas y columnas específicas. Los índices se pueden poner en cualquier orden e incluso se puedo poner más de una vez.
	- **Combinación de filas y columnas** - `DataFrame`: Retorna las filas y columnas en las etiquetas indicadas: <br/> `X.loc[['ind1', 'ind2', ...], ['col1', 'col2', ...]`

<br/>

- **Boolean masking**: Útil para seleccionar filas y/o columnas con base a _masks_. **Importante**: Asegurarse que el tamaño del _mask_ coincide con el tamaño del eje donde se va a aplicar.
	- **Mask en filas y columnas** - `DataFrame`: Retorna los elementos que satisfacen ambos _masks_: <br/> `X.loc[row_mask, col_mask]`

<br/>

- **Combinación de estrategias**: Aquí se presentan algunas opciones de combinación de estrategias para las filas y columnas que permiten mayor versatibilidad para seleccionar elementos. **Importante**: Esta no es una lista extensiva, en general se puede aplicar cualquier estrategia para selección de elementos de manera independiente tanto para las filas, como para las columnas.
	- **Filas completas** - `Series`: Retorna la fila completa con la etiqueta `'ind'` como `Series`: <br/> `X.loc['ind']` <br/> `X.loc['ind', :]` 
	- **Filas completas** - `DataFrame`: Retorna la fila completa con la etiqueta `'ind'` como `DataFrame`: <br/> `X.loc[['ind'], :]`, <br/> `X.loc[['ind']]`
	- **Múltiples filas completas** - `DataFrame`: Retorna las filas completas con los índices indicados: <br/> `X.loc[['ind1', 'ind2', ...]]` <br/> `X.loc[['ind1', 'ind2', ...], :]` 
	- **Columna completa** - `Series`: Retorna la columna completa con la etiqueta `'col'` como `Series`: <br/> `X.loc[:, 'col']`
	- **Columna completa** - `DataFrame`: Retorna la columna completa con la etiqueta `'col'` como `DataFrame`: <br/> `X.loc[:, ['col']]`
	- **Múltiples columnas completas** - `DataFrame`: Retorna las columnas completas en los índices indicados: <br/> `X.loc[:, ['col1', 'col2', ...]]`
	- **Mask en filas** - `DataFrame`: Retorna las filas que satisfacen un _mask. Asegurarse que el _mask_ esté conformado por valores booleanos y no por _1s_ y _0s_: <br/> `X.loc[row_mask, :]`
	- **Mask en columnas** - `DataFrame`: Retorna las columnas que satisfacen un _mask_. Asegurarse que el _mask_ esté conformado por valores booleanos y no por _1s_ y _0s_: <br/> `X.iloc[:, col_mask]`

<br/>

**Ejemplos**: A continuación se ejemplifica la selección de elementos con las diversas estategias con el método `.loc[]` en un `DataFrame`.

```{code-cell} ipython3
# Indexing: Elemento específico
print(df.loc['California', 'Population'], end="\n"*2)

# Slicing: Rango de filas
print(df.loc['California':'Texas', :], end="\n"*2)

# Boolean masking: Mask en ambos ejes
print(df.loc[df['Area (km2)']>300000, df.columns.isin(['Capital', 'Area (km2)'])], end="\n"*2)

# Combinación de estrategias: Boolean masking y fancy indexing
print(df.loc[df['Area (km2)']>300000, ['Capital', 'Population']])
```

<br/><br/>

---
### Usando método `.iloc[]`

El método `.iloc[]` es útil para seleccionar elementos con base al **índice implícito**:

- **Subsetting**: Útil para seleccionar elementos específicos:
	- **Elemento específico** - `scalar`: Retorna el elemento en índice _i_ y la columna _j_ como `scalar`, los índices empiezan en cero: <br/> `X.iloc[i, j]`

<br/>

- **Slicing**: Útil para seleccionar _slices_ tanto de filas como se columnas. Se separan los _slicers_ para las filas y las columnas con una coma.
	- **Slices de filas** - `DataFrame`: Retorna filas completas para todas las columnas: <br/> `X.iloc[start:stop:step]`<br/> `X.iloc[start:stop:step, :]` 
	- **Slices de columnas** - `DataFrame`: Retorna columnas completas para todas las filas: <br/> `X.iloc[:, start:stop:step]`
	- **Slices de filas y columnas** - `DataFrame`: Retorna _slices_ de filas y columnas específicas: <br/> `X.iloc[start:stop:step, start:stop:step]`

<br/>

- **Fancy indexing**: Útil para seleccionar combinaciones de filas y columnas específicas. Los índices se pueden poner en culquier orden e incluso se puedo poner más de una vez. Las filas y columnas se separan por coma.
	- **Combinación de filas y columnas** - `DataFrame`: Retorna las filas y columnas completas en los índices indicados: <br/> `X.iloc[[n1, n2, ...], [m1, m2, ...]`

<br/>

- **Combinación de estrategias**: Aquí se presentan algunas opciones de combinación de estrategias para las filas y columnas que permiten mayor versatibilidad para seleccionar elementos, particularmente columnas. **Importante**. Esta no es una lista extensiva, en general se puede aplicar cualquier estrategia para selección de elementos (excepto _masking_), de manera independiente tanto para las filas, como para las columnas.
	- **Filas completas**  - `Series`: Retorna la fila completa en el índice _i_ como `Series`, los índices empiezan en cero: <br/> `X.iloc[i, :]` <br/> `X.iloc[i]`
	- **Filas completas**  - `DataFrame`: Retorna la fila completa en el índice _i_ como `DataFrame`, los índices empiezan en cero: <br/> `X.iloc[[i]]` <br/> `X.iloc[[i], :]`
	- **Múltiples filas completas** - `DataFrame`: Retorna las filas completa en los índices indicados: <br/> `X.iloc[[n1, n2, ...]]` <br/> `X.iloc[[n1, n2, ...], :]`
	- **Columna completa** - `Series`: Retorna la columna completa en el índice _j_ como `Series`: <br/> `X.iloc[: , j]`
	- **Columna completa** - `DataFrame`: Retorna la columna completa en el índice _j_ como `DataFrame`: <br/> `X.iloc[: , [j]]`
	- **Múltiples columnas completa**  - `DataFrame`: Retorna las columnas completas en los índices indicados: <br/> `X.iloc[: , [m1, m2, ...]]`
	- **Mask en columnas** - `DataFrame`: Retorna las columnas especificadas por un _mask_ para una fila determinada. Asegurarse que el _mask_ esté conformado por valores booleanos y no por _1s_ y _0s_: <br/> `X.iloc[i, mask]`

<br/>

**Ejemplos**: A continuación se ejemplifica la selección de elementos con las diversas estategias con el método `.iloc[]` en un `DataFrame`.

```{code-cell} ipython3
# Indexing: Elemento específico
print(df.iloc[1, 1], end="\n"*2)

# Slicing
print(df.iloc[::2, ::-1], end="\n"*2)

# Fancy indexing
print(df.iloc[[0, 3, 1, 2], [0, 1, 0]], end="\n"*2)

# Combinación de estrategias: Fancy indexing y slicing
print(df.iloc[[1, 2, 0], ::2], end="\n"*2)
```

<br/><br/>

---
## Agregar columna

Para agregar una columna nueva simplemente asignar los valores a una etiqueta nueva.
```python
# Agregar nueva columna
X['label'] = Y
```
- _X_ - `DataFrame`.
- _'label'_ será el nombre de la columna. 
- `Y` -  `Series`, `array-like`, `secuencia`: Asegurarse que el tamaño de este objeto coincida con el tamaño en el eje 0 del `DataFrame`
- **IMPORTANTE**: No se puede usar la notación `X.label = Y`.

<br/>

---
## Modificar valores

Se pueden acceder a determinados elementos con cualquier método de selección de elementos y asignarle un nuevo valor.

:::{warning}
Al asignar elementos asegurarse que los tipos coincidan con los tipos de las columnas donde se modificarán los valores o al menos que sea posible forzar la conversión.
:::

```python
# Modificar elementos específicos
df.loc['ind', 'col'] = val	
df.iloc[i, j] = val

# Múltiples valores con mismo valor (ejemplo con slicing)
df.loc[:, ['col']] = val

# Múltiples valores con diferentes valores (ejemplo con slicing)
df.loc[:, ['col']] = [val1, val2, ...]
```
**Notas**:
- **Un elemento específico**: Seleccionar el elemento por cualquier estrategia de selección y asigarle un nuevo valor.
- **Múltiples con un mismo valor**: Seleccionar los elementos por cualquier estrategia de selección y asignarles un `scalar`.
- **Múltiples elementos con valores diferentes**: Seleccionar los elementos por cualquier estrategia de selección y asignarles un `array-like` del mismo _shape_ que el objeto retornado por la selección.

<br/>

---
## Eliminar una columna

Se puede usar la palabra reservada `del` para eliminar columnas completas:
```python
# Eliminar la columna 'label'	
del df['label']
```

<br/>

---
## Iteraración

### Sobre columnas

Para iterar sobre las columnas podría usarse la sintaxis:

```python
# Iteración por las etiquetas de las columnas
for col in df:
	# for body
```
- _col_ tendrá los _labels_ de las columnas de `DataFrame`.

<br/>

### Sobre las filas

Para iterar sobre las filas de un `DataFrame` utilizar el método `.iterrows()`:
```python
# Iteración por las filas
for index, data in df.iterrows():
	# for body
```
- _index_ será el índice de la fila en la iteración.
- _data_ será un `Series`, que contendrá la información de todas las columnas para cada fila en la iteración, el índice de _data_ será el nombre de la columna de _df_. Se puede aplicar cualquier método de selección de elementos de `Series` en _data_.

<br/>

---
## Uniones y apilaciones

Para unir objetos de pandas, ya sea apilando los objetos o en una operación similar a un _join_ de SQL, revisar los siguientes funciones de `pandas` o métodos:
- `DataFrame.join()`: Permite unir columnas de objetos de `pandas` con base a valores de columnas o de los índices de una manera similar a un _join_ de SQL.
- `DataFrame.merge()`: Permite unir columnas de objetos de `pandas` con base a valores de columnas o de los índices de una manera similar a un _join_ de SQL. Permite más flexibilidad que `DataFrame.join()`.
- `pd.concat()`: Concatena objetos sobre un eje existe, resultando en un objeto con el mismo número de dimensiones que los objetos originales. Se puede indicar si el _index_ se debe de reiniciar o indicar a que objeto pertenecía cada fila.
- `pd.merge()`: Permite unir bjetos de `pandas` con base a valores de columnas o de los índices de una manera similar a un _join_ de SQL.

:::{note}
Para más información vistar {ref}`Funciones de uniones y apilaciones <pandas-func-joins>` y {ref}`Métodos de unión <pandas-df-methods-joins>`.
:::

---
(pandas-df-pivot-unpivot)=
## Pivot y unpivot

En datos tabulares existen dos formatos principales:
1. **Long format**: También denominada _unpivot_, cada columna en la tabla representa una variable en los datos. Por lo tanto los mismos valores se pueden repetir en múltiples filas y existe una o más columnas de valores. 
2. **Wide format**: También denominada _pivot_, distribuye los valores de una o mas variables categóricas a lo largo de las columnas, se establece un “índice” con los valores únicos de una columna categórica o las combinaciones únicas de dos más columnas categóricas y la columna de valores  pasa a ser los valores/cálculos de las mismas. Además es posible añadir totales para filas y columnas.


```{figure} ../images/wide-long-format.png
:name: wide-and-long-format
:width: 500px
:align: center

Visualización de _wide_ y _long format_.
```

Los objetos `DataFrame` tiene algunos métodos para cambiar de un formato a otro. Para más información de estos métodos visitar {ref}`Métodos de pivot y unpivot <pandas-df-methods-pivot-unpivot>`:
- `melt()`: Sirve para pasar de un _wide format_ a _long format_.
- `pivot()`: Permite pasar de _long format_ a _wide format_, no soporta _aggregates_ en los valores ni el calculo de subtotales y/o totales.
- `pivot_table()`: Permite pasar de _long format_ a _wide format_, soporta _aggregates_ en los valores y permite el calculo de totales.

<br/>

**Ejemplos**:

```{code-cell} ipython3
# Definir DataFrame
long = pd.DataFrame({'col1': ['A', 'A', 'B', 'B', 'C', 'C'],
                    'col2': ['X', 'Y']*3,
                    'col3': [*range(1, 7)]})
print("DataFrame:", long, sep='\n', end='\n'*2)

# Pivot
pivot = long.pivot(columns='col2', index='col1', values='col3')
print("Pivot:", pivot, sep='\n', end='\n'*2)

# Unpivot
unpivot = pivot.reset_index().melt(id_vars='col1', var_name='col2', value_name='col3')
print("Unpivot:", unpivot, sep='\n', end='\n'*2)

# Pivot con totales
wide = long.pivot_table(values='col3', index='col1', columns='col2', aggfunc='sum', margins=True)
print("Pivot con totales:", wide, sep='\n')
```

<br/>

---
## Atributos

Atributos del objeto `DataFrame`. 

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - [DataFrame.axes](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.axes.html)
  - Retorna un `list` representando los ejes (objetos `Index` de cada eje) del `DataFrame`.
* - [DataFrame.columns](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.columns.html)
  - Las etiquetas de las columnas del `DataFrame` como `Index` o una subclase del mismo.
* - [DataFrame.dtypes](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dtypes.html)
  - Retorna los tipos de datos de cada columna en el `DataFrame` como `Series`.
* - [DataFrame.empty](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.empty.html)
  - Indica si el objeto está vacío.
* - [DataFrame.index](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.index.html)
  - El índice (etiquetas de fila) del `DataFrame` como `Index` o una subclase del mismo.
* - [DataFrame.info](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.info.html)([verbose, buf, max_cols, ...])
  - Devuelve información del `DataFrame` como dimensiones, tipo de datos de las columnas, nombre de las columnas, memoria usada, el tipo de dato del índice, valores non-null, etc.
* - [DataFrame.memory_usage](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.memory_usage.html)([index, deep])
  - Retorna el uso de memoria de cada columna en bytes.
* - [DataFrame.ndim](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.ndim.html)
  - Retorna un `int` que representa el número de ejes/dimensiones de la matriz.
* - [DataFrame.select_dtypes](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.select_dtypes.html)([include, exclude])
  - Retorna un subconjunto de las columnas del DataFrame según los tipos de columna.
* - [DataFrame.set_flags](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.set_flags.html)(*[, copy, ...])
  - Retorna un nuevo objeto con indicadores actualizados.
* - [DataFrame.shape](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.shape.html)
  - Retorna un `tuple` que representa la dimensionalidad (número de elementos en cada eje) del `DataFrame`.
* - [DataFrame.size](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.size.html)
  - Retorna un `int` que representa el número total de elementos de este objeto.
* - [DataFrame.values](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.values.html)
  - Retorna una representación _ndarray_ de los valores del `DataFrame`.
```

<br/>


## Métodos

### Conversión y copias

Métodos para convertir el objeto `DataFrame` a algún otro tipo o crear un copia. 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [DataFrame.astype](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.astype.html)(dtype[, copy, errors])
  - Convierte los datos a otro tipo de dato.
* - [DataFrame.convert_dtypes](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.convert_dtypes.html)([infer_objects, ...])
  - Convierte las columnas a los mejores tipos `dtype` posibles que admitan `pd.NA`.
* - [DataFrame.copy](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.copy.html)([deep])
  - Crea una copia del objeto.
* - [DataFrame.infer_objects](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.infer_objects.html)([copy])
  - Intenta inferir los mejores tipos de columnas del objeto.
* - [DataFrame.squeeze](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.squeeze.html)([axis])
  - Convierte ejes de 1 dimensión en un `scalar`.
* - [DataFrame.to_dict](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_dict.html)([orient, into, index])
  - Convierte el `DataFrame` a un diccionario.
```

<br/>

---
### IO y Serialización

Métodos para exportar el `DataFrame` en un formato específico o serializar el mismo. 


#### Entrada

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [DataFrame.from_dict](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.from_dict.html)(data[, orient, dtype, ...])
  - Contruye un `DataFrame` desde un `dict` con valores `array-like` o `dict`.
* - [DataFrame.from_records](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.from_records.html)(data[, index, ...])
  - Contruye un `DataFrame` desde un array estructura, un `list` de `dict` o un `list` de `tuple`.
```

#### Salida


```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [DataFrame.to_clipboard](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_clipboard.html)(*[, excel, sep])
  - Copia el objeto al portapapeles del sistema.
* - [DataFrame.to_csv](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html)([path_or_buf, sep, na_rep, ...])
  - Escribe el objeto en un archivo de valores separados por comas (csv).
* - [DataFrame.to_excel](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_excel.html)(excel_writer, *[, ...])
  - Escribe objeto en una hoja de Excel. **EJEMPLO**
* - [DataFrame.to_feather](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_feather.html)(path, **kwargs)
  - Escribe un `DataFrame` al formato binario _Feather_.
* - [DataFrame.to_hdf](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_hdf.html)(path_or_buf, *, key[, ...])
  - Escribe los datos contenidos en un archivo _HDF5_ usando _HDFStore_.
* - [DataFrame.to_html](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_html.html)([buf, columns, col_space, ...])
  - Retorna un `DataFrame` como una tabla HTML como `str`.
* - [DataFrame.to_json](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_json.html)([path_or_buf, orient, ...])
  - Convierte el objeto en una cadena _JSON_ como `str`.
* - [DataFrame.to_latex](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_latex.html)([buf, columns, header, ...])
  - Escribe el objeto como una tabla tabular de LaTeX como `str`.
* - [DataFrame.to_markdown](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_markdown.html)([buf, mode, index, ...])
  - Escribe el `DataFrame` en formato compatible con Markdown como `str`.
* - [DataFrame.to_orc](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_orc.html)([path, engine, index, ...])
  - Escribe un `DataFrame` al formato _ORC_.
* - [DataFrame.to_parquet](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_parquet.html)([path, engine, ...])
  - Escribe un `DataFrame` al formato _parquet_ binario.
* - [DataFrame.to_pickle](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_pickle.html)(path, *[, compression, ...])
  - Serializa el objeto en un _pickle_.
* - [DataFrame.to_records](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_records.html)([index, column_dtypes, ...])
  - Convierte `DataFrame` a un arreglo estructurado de _NumPy_.
* - [DataFrame.to_sql](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_sql.html)(name, con, *[, schema, ...])
  - Escribe los registros almacenados en un `DataFrame` a una base de datos SQL.
* - [DataFrame.to_stata](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_stata.html)(path, *[, convert_dates, ...])
  - Exporta el `DataFrame` a _Stata_.
* - [DataFrame.to_string](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_string.html)([buf, columns, ...])
  - Renderiza un `DataFrame` a una salida compatible con la consola.
* - [DataFrame.to_xarray](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_xarray.html)()
  - Retorna un objeto `xarray` del `DataFrame`.
```

<br/>

---
### Cálculos y operadores


#### Aggregates

:::{note}
Estos métodos ignoran valores `NA`/`NaN`.
:::

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [DataFrame.agg](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.agg.html)([func, axis])
  - Agrega usando una o más operaciones sobre el eje especificado.
* - [DataFrame.aggregate](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.aggregate.html)([func, axis])
  - Agrega usando una o más operaciones sobre el eje especificado.
* - [DataFrame.count](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.count.html)([axis, numeric_only])
  - Retorna el conteo de los valores no nulos sobre el eje indicado.
* - [DataFrame.prod](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.prod.html)([axis, skipna, numeric_only, ...])
  - Retorna el producto de los valores sobre el eje indicado.
* - [DataFrame.product](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.product.html)([axis, skipna, ...])
  - Retorna el producto de los valores sobre el eje indicado.
* - [DataFrame.sum](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sum.html)([axis, skipna, numeric_only, ...])
  - Retorna la suma de los valores sobre el eje indicado.
```

:::{caution}
Para funciones como `.mean()`, `.std()`, etc. consultar los métodos {ref}`Estadísticas <dataframe-metodos-estadisticas>`.
:::

<br/>

#### Booleanos

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [DataFrame.all](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.all.html)([axis, bool_only, skipna])
  - Retorna `True` si todos los valores son `True` sobre un eje.
* - [DataFrame.any](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.any.html)(*[, axis, bool_only, skipna])
  - Retorna `True` si hay al menos un valor `True` sobre un eje.
```

<br/>

#### Cálculos acumulados, diferencias, cambios porcentuales y rank

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [DataFrame.cummax](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.cummax.html)([axis, skipna])
  - Para cada elemento en el eje determina el valor máximo hasta ese elemento.
* - [DataFrame.cummin](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.cummin.html)([axis, skipna])
  - Para cada elemento en el eje determina el valor mínimo hasta ese elemento.
* - [DataFrame.cumprod](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.cumprod.html)([axis, skipna])
  - Para cada elemento en el eje determina el producto acumulado hasta ese elemento.
* - [DataFrame.cumsum](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.cumsum.html)([axis, skipna])
  - Para cada elemento en el eje determina la suma acumulada hasta ese elemento.
* - [DataFrame.diff](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.diff.html)([periods, axis])
  - Para cada elemento en un eje calcula la diferencia de elementos con cierto desfase `[i] - [i-1]`.
* - [DataFrame.pct_change](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pct_change.html)([periods, fill_method, ...])
  - Para cada fila calcula el cambio porcentual entre el elemento actual y el anterior.
* - [DataFrame.rank](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rank.html)([axis, method, numeric_only, ...])
  - Calcula los rangos de datos numéricos (1 a n) a lo largo del eje.
```

<br/>

#### Estadísticas

Métodos para el cálculo de estadísticas descriptivas, generar muestras aleatorias o calcular correlaciones y covarianzas entre dos variables.

:::{note}
Estos métodos ignoran valores `NA`.
:::

```{list-table}
:header-rows: 1
:name: dataframe-metodos-estadisticas

* - Método
  - Descripción
* - [DataFrame.corr](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.corr.html)([method, min_periods, ...])
  - Calcula la correlación por pares de columnas, excluyendo `NA`/valores nulos.
* - [DataFrame.corrwith](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.corrwith.html)(other[, axis, drop, ...])
  - Calcula la correlación por pares con otro objeto.
* - [DataFrame.cov](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.cov.html)([min_periods, ddof, numeric_only])
  - Calcula la covarianza por pares de columnas, excluyendo `NA`/valores nulos.
* - [DataFrame.describe](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html)([percentiles, include, ...])
  - Genera estadísticas descriptivas de los datos por columnas. 
* - [DataFrame.kurt](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.kurt.html)([axis, skipna, numeric_only])
  - Retorna curtosis sobre el eje solicitado.
* - [DataFrame.kurtosis](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.kurtosis.html)([axis, skipna, numeric_only])
  - Retorna curtosis sobre el eje solicitado.
* - [DataFrame.mean](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.mean.html)([axis, skipna, numeric_only])
  - Retorna la media de los valores sobre el eje indicado.
* - [DataFrame.median](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.median.html)([axis, skipna, numeric_only])
  - Retorna la mediana de los valores sobre el eje indicado.
* - [DataFrame.mode](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.mode.html)([axis, numeric_only, dropna])
  - Recupera la moda a lo largo del eje indicado.
* - [DataFrame.sample](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sample.html)([n, frac, replace, ...])
  - Retorna una muestra aleatoria de elementos de un eje del objeto.
* - [DataFrame.sem](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sem.html)([axis, skipna, ddof, numeric_only])
  - Retorna el error estándar de la media sobre el eje indicado.
* - [DataFrame.skew](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.skew.html)([axis, skipna, numeric_only])
  - Retorna el sesgo sobre el eje indicado.
* - [DataFrame.std](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.std.html)([axis, skipna, ddof, numeric_only])
  - Retorna la desviación estándar de la muestra sobre el eje indicado.
* - [DataFrame.var](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.var.html)([axis, skipna, ddof, numeric_only])
  - Retorna la varianza sobre el eje indicado.
```

<br/>

#### Estadísticos de orden

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [DataFrame.idxmax](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.idxmax.html)([axis, skipna, numeric_only])
  - Retorna la etiqueta del valor máximo sobre el eje indicado.
* - [DataFrame.idxmin](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.idxmin.html)([axis, skipna, numeric_only])
  - Retorna la etiqueta del valor mínimo sobre el eje indicado.
* - [DataFrame.nlargest](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.nlargest.html)(n, columns[, keep])
  - Retorna los _n_ elementos más grandes. por columnas en orden descendente.
* - [DataFrame.nsmallest](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.nsmallest.html)(n, columns[, keep])
  - Retorna los _n_ elementos más pequeños por columnas en orden ascendente.
* - [DataFrame.max](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.max.html)([axis, skipna, numeric_only])
  - Retorna el máximo de los valores sobre el eje indicado.
* - [DataFrame.min](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.min.html)([axis, skipna, numeric_only])
  - Retorna el mínimo de los valores sobre el eje indicado.
* - [DataFrame.quantile](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.quantile.html)([q, axis, numeric_only, ...])
  - Retorna el cuantil dado de los valores sobre el eje indicado. `q` es un valor entre cero y uno.
```

<br/>

#### Misceláneos

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [DataFrame.abs](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.abs.html)()
  - Retorna un `DataFrame` con el valor numérico absoluto de cada elemento.
```

<br/>

#### Operadores aritméticos y similares.

Métodos para realizar operaciones binarias con operadores aritméticos y sus equivalentes que tienen por sufijo una `r` útiles para intercambiar las posiciones del `DataFrame` y del argumento `other`. 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [DataFrame.add](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.add.html)(other[, axis, level, fill_value])
  - Retorna la suma del `DataFrame` y `other`, por elementos. Equivale a usar el operador `+`.
* - [DataFrame.div](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.div.html)(other[, axis, level, fill_value])
  - Retornar la división flotante del `DataFrame` y `other`, por elementos. Equivale a usar el operador `/`.
* - [DataFrame.dot](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dot.html)(other)
  - Calcula el producto escalar entre `DataFrame` y `other`.
* - [DataFrame.eval](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.eval.html)(expr, *[, inplace])
  - Evalua una cadena que describe operaciones en las columnas de un `DataFrame`.
* - [DataFrame.floordiv](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.floordiv.html)(other[, axis, level, ...])
  - Retornar la división entera del `DataFrame` y `other`, por elementos. Equivale a usar el operador `//`.
* - [DataFrame.mod](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.mod.html)(other[, axis, level, fill_value])
  - Retornar el módulo de la división del `DataFrame` y `other`, por elementos. Equivale a usar el operador `%`.
* - [DataFrame.mul](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.mul.html)(other[, axis, level, fill_value])
  - Retornar la multiplicación del `DataFrame` y `other`, por elementos. Equivale a usar el operador `*`.
* - [DataFrame.pow](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pow.html)(other[, axis, level, fill_value])
  - Retornar la potenciación del `DataFrame` y `other`, por elementos. Equivale a usar el operador `^`.
* - [DataFrame.radd](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.radd.html)(other[, axis, level, fill_value])
  - Retorna la suma del `DataFrame` y `other`, por elementos. Equivale a usar el operador `+`.
* - [DataFrame.rdiv](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rdiv.html)(other[, axis, level, fill_value])
  - Retornar la división flotante de `other` y `DataFrame`, por elementos. Equivale a usar el operador `/`, siendo `other` el numerador.
* - [DataFrame.rfloordiv](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rfloordiv.html)(other[, axis, level, ...])
  - Retornar la división entera de `other` y `DataFrame`, por elementos. Equivale a usar el operador `//`, siendo `other` el numerador.
* - [DataFrame.rmod](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rmod.html)(other[, axis, level, fill_value])
  - Retornar el módulo de la división de `other` y `DataFrame`, por elementos. Equivale a usar el operador `%`, siendo `other` el numerador.
* - [DataFrame.rmul](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rmul.html)(other[, axis, level, fill_value])
  - Retornar la multiplicación del `DataFrame` y `other`, por elementos. Equivale a usar el operador `*`.
* - [DataFrame.rpow](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rpow.html)(other[, axis, level, fill_value])
  - Retornar la potenciación de `other` y `DataFrame`, por elementos. Equivale a usar el operador `^`, siendo `other` la base.
* - [DataFrame.rsub](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rsub.html)(other[, axis, level, fill_value])
  - Retornar la resta de `other` y `DataFrame`, por elementos. Equivale a usar el operador `-`, siendo `other` el minuendo.
* - [DataFrame.rtruediv](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rtruediv.html)(other[, axis, level, ...])
  - Retornar la división flotante del `other` y `DataFrame`, por elementos. Equivale a usar el operador `/`, siendo `other` el numerador. Permite reemplazar valores nulos por algún valor en particular.
* - [DataFrame.sub](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sub.html)(other[, axis, level, fill_value])
  - Retornar la resta del `DataFrame` y `other`, por elementos. Equivale a usar el operador `-`.
* - [DataFrame.truediv](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.truediv.html)(other[, axis, level, ...])
  - Retornar la división flotante del `DataFrame` y `other`, por elementos. Equivale a usar el operador `/`. Permite reemplazar valores nulos por algún valor en particular.
```

<br/>

#### Operadores de comparación y membresía.

Lorem ipsum dolor sit amet, consectetur adipiscing elit. 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [DataFrame.eq](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.eq.html)(other[, axis, level])
  - Indica la igualdad del `DataFrame` y `other`, por elementos. Equivale a usar el operador `==`.
* - [DataFrame.equals](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.equals.html)(other)
  - Verifica si dos objetos contienen los mismos elementos.
* - [DataFrame.ge](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.ge.html)(other[, axis, level])
  - Indica si es mayor o igual el `DataFrame` y `other`, por elementos. Equivale a usar el operador `>=`.
* - [DataFrame.gt](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.gt.html)(other[, axis, level])
  - Indica si es mayor el `DataFrame` y `other`, por elementos. Equivale a usar el operador `>`.
* - [DataFrame.isin](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.isin.html)(values)
  - Retorna `DataFrame` booleano que indica si cada elemento del `DataFrame` está contenido en `values`.
* - [DataFrame.le](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.le.html)(other[, axis, level])
  - Indica si es menor o igual el `DataFrame` y `other`, por elementos. Equivale a usar el operador `<=`.
* - [DataFrame.lt](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.lt.html)(other[, axis, level])
  - Indica si es manor el `DataFrame` y `other`, por elementos. Equivale a usar el operador `<`.
* - [DataFrame.ne](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.ne.html)(other[, axis, level])
  - Indica si no son iguales el `DataFrame` y `other`, por elementos. Equivale a usar el operador `!=`.
```

#### Redondear y truncar

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [DataFrame.clip](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.clip.html)([lower, upper, axis, inplace])
  - Ajusta los valores para que estén en el intervalo `[lower, upper]` en el eje indicado.
* - [DataFrame.round](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.round.html)([decimals])
  - Redondea cada valor en un `DataFrame` al número de decimales dado.
```

<br/>

#### Series de tiempo

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [DataFrame.asfreq](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.asfreq.html)(freq[, method, how, ...])
  - Modifica la frecuencia de una serie de tiempo. El `DataFrame` debe de tener un índice `datetime-like`. Si se va a realizar un _aggregate_ con la nueva frecuencia se recomienda usar el método `Series.resample()`. **EJEMPLO**
* - [DataFrame.asof](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.asof.html)(where[, subset])
  - Retorna la/s última/s fila/s válida sin incluir `NaNs` antes o en `where`, donde `where` son etiquetas del índice.
* - [DataFrame.at_time](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.at_time.html)(time[, asof, axis])
  - Selecciona valores en un momento particular del día (por ejemplo, 9:30 a. m.).
* - [DataFrame.between_time](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.between_time.html)(start_time, end_time)
  - Selecciona valores entre horas particulares del día (por ejemplo, de 9:00 a 9:30 a. m.).
* - [DataFrame.resample](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.resample.html)(rule[, axis, closed, ...])
  - Modifica la frecuencia de una serie de tiempo, útil si se realizará un _aggregate_ con la nueva frecuencia. El objeto debe de tener un índice `datetime-like` o pasar valores `datetime-like` al argumento `on` o `level`. **IMPORTANTE**: Este método retorna un objeto `Resampler`, que tiene otros métodos como `Resampler.asfreq()` o _aggregates_ como `Resampler.mean()`.  **EJEMPLO**
* - [DataFrame.shift](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.shift.html)([periods, freq, axis, ...])
  - Desplaza el índice según el número deseado de períodos con una frecuencia de tiempo opcional. **EJEMPLO**
* - [DataFrame.to_period](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_period.html)([freq, axis, copy])
  - Convierte el índice del `DataFrame` de `DatetimeIndex` a `PeriodIndex`.
* - [DataFrame.to_timestamp](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_timestamp.html)([freq, how, axis, copy])
  - Convierte un índice `DatetimeIndex` al comienzo del período.
* - [DataFrame.tz_convert](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.tz_convert.html)(tz[, axis, level, copy])
  - Convierte un _axis_ compatible con `tz` en la zona horaria objetivo.
* - [DataFrame.tz_localize](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.tz_localize.html)(tz[, axis, level, ...])
  - Localiza el índice `tz-naive` a la zona horaria de destino.
```

<br/>

---
### Funciones ventana, agrupar, aplicar y mapeos

Lorem ipsum dolor sit amet, consectetur adipiscing elit. 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [DataFrame.agg](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.agg.html)([func, axis])
  - Agrega usando una o más operaciones sobre el eje especificado.
* - [DataFrame.aggregate](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.aggregate.html)([func, axis])
  - Agrega usando una o más operaciones sobre el eje especificado.
* - [DataFrame.apply](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.apply.html)(func[, axis, raw, ...])
  - Aplica una función lo largo de un eje del `DataFrame`.
* - [DataFrame.ewm](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.ewm.html)([com, span, halflife, alpha, ...])
  - Provee de cálculos ponderados exponencialmente (_EW_).
* - [DataFrame.expanding](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.expanding.html)([min_periods, axis, method])
  - A lo largo de un eje del `DataFrame` calcula un _aggregate_ hasta un elemento, para realizar el cálculo se debe aplicar un método del objeto `Expanding`. Funciona de manera similar a métodos de cálculos acumulados como `DataFrame.cumprod()`, `DataFrame.cumsum()`, etc.
* - [DataFrame.groupby](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html)([by, axis, level, ...])
  - Agrupa el `DataFrame` por un _mapper_ o los valores de un `Series`. Posteriorme se pueden aplicar métodos del objeto `GroupBy` a cada grupo.
* - [DataFrame.map](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.map.html)(func[, na_action])
  - Aplica una función a un `DataFrame` por elementos o mapea los valores con base a otro objeto.
* - [DataFrame.pipe](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pipe.html)(func, *args, **kwargs)
  - Encadena funciones que reciben `Series` o `DataFrame`.
* - [DataFrame.rolling](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rolling.html)(window[, min_periods, ...])
  - Provee calculos en ventanas moviles de datos. Posteriormente se puede aplicar un método del objeto `Rolling` o `Window`.
* - [DataFrame.transform](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.transform.html)(func[, axis])
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
* - [DataFrame.boxplot](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.boxplot.html)([column, by, ax, ...])
  - Crea un diagrama de caja a partir de `DataFrame` columnas.
* - [DataFrame.hist](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.hist.html)([column, by, grid, ...])
  - Crea un histograma de las columnas del DataFrame.
* - [DataFrame.plot](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.html)([x, y, kind, ax, ....])
  - Función general para crear gráficas con base a los datos del ´Series´. **EJEMPLO**
* - [DataFrame.plot.area](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.area.html)([x, y, stacked])
  - Gráfica de áreas apiladas.
* - [DataFrame.plot.bar](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.bar.html)([x, y])
  - Gráfica de barras verticales.
* - [DataFrame.plot.barh](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.barh.html)([x, y])
  - Gráfica de barras horizontales.
* - [DataFrame.plot.box](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.box.html)([by])
  - Gráfica de un diagrama de cajas de las columnas del `DataFrame`.
* - [DataFrame.plot.density](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.density.html)([bw_method, ind])
  - Genera un gráfico de estimación de densidad.
* - [DataFrame.plot.hexbin](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.hexbin.html)(x, y[, C, ...])
  - Genera un gráfico de agrupamiento hexagonal.
* - [DataFrame.plot.hist](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.hist.html)([by, bins])
  - Grafica un histograma de las columnas del `DataFrame`.
* - [DataFrame.plot.kde](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.kde.html)([bw_method, ind])
  - Genera un gráfico de estimación de densidad.
* - [DataFrame.plot.line](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.line.html)([x, y])
  - Gráfica de líneas.
* - [DataFrame.plot.pie](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.pie.html)(**kwargs)
  - Genera un diagrama circular.
* - [DataFrame.plot.scatter](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.scatter.html)(x, y[, s, c])
  - Crea un diagrama de dispersión.
```

<br/>

---
### Índice

Métodos para operaciones con el `Index`, los niveles y las etiquetas del mismo en un objeto `DataFrame`. 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [DataFrame.add_prefix](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.add_prefix.html)(prefix[, axis])
  - Agrega un prefijo a las etiquetas del `Index`.
* - [DataFrame.add_suffix](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.add_suffix.html)(suffix[, axis])
  - Agrega un sufijo a las etiquetas del `Index`.
* - [DataFrame.droplevel](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.droplevel.html)(level[, axis])
  - Elimina un nivel del `Index` de un `DataFrame`.
* - [DataFrame.align](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.align.html)(other[, join, axis, level, ...])
  - Alinea el índice de dos objetos en algún eje con el método de unión especificado. Este método sirve para igualar el índice de un objeto con base a otro, los índice nuevos por default tendrán `NA` como valores. 
* - [DataFrame.idxmax](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.idxmax.html)([axis, skipna, numeric_only])
  - Retorna la etiqueta del valor máximo sobre el eje indicado.
* - [DataFrame.idxmin](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.idxmin.html)([axis, skipna, numeric_only])
  - Retorna la etiqueta del valor mínimo sobre el eje indicado.
* - [DataFrame.first_valid_index](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.first_valid_index.html)()
  - Retorna el primer índice cuyo valor no sea `NA`, retorna `None` si no se encuentra ningún valor que no sea `NA`.
* - [DataFrame.last_valid_index](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.last_valid_index.html)()
  - Retorna el último índice cuyo valor no sea `NA`, retorna `None` si no se encuentra ningún valor que no sea `NA`.
* - [DataFrame.reindex](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.reindex.html)([labels, index, columns, ...])
  - Modifica el índice de un `DataFrame`.
* - [DataFrame.reindex_like](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.reindex_like.html)(other[, method, ...])
  - Modifica el índice de un `DataFrame` con base al índice de otro objeto.
* - [DataFrame.rename](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rename.html)([mapper, index, columns, ...])
  - Modifica el nombre o las etiquetas del índice o columnas del objeto.
* - [DataFrame.rename_axis](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rename_axis.html)([mapper, index, ...])
  - Reenombra el eje para el índice o las columnas.
* - [DataFrame.reorder_levels](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.reorder_levels.html)(order[, axis])
  - Reorganiza los niveles del índice usando el orden de entrada.
* - [DataFrame.reset_index](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.reset_index.html)([level, drop, ...])
  - Reestablece el `Index` del objeto (o un nivel), al índice numérico, empezando en cero.
* - [DataFrame.set_axis](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.set_axis.html)(labels, *[, axis, copy])
  - Asigna el índice deseado al eje dado.
* - [DataFrame.set_index](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.set_index.html)(keys, *[, drop, append, ...])
  - Establece una columna como `Index`.
* - [DataFrame.sort_index](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_index.html)(*[, axis, level, ...])
  - Ordena el `DataFrame` con base a las etiquetas del índice.
* - [DataFrame.swaplevel](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.swaplevel.html)([i, j, axis])
  - Intercambia los niveles `i` y `j` en un `MultiIndex`.
```

<br/>

---
### Manipulación

Métodos para realizar modificar en el `DataFrame` como modificar valores, eliminar valores, insertar valores, modificar el _shape_ (insertar o eliminar columnas/filas o convertir columnas a _index_), transponer, etc. 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [DataFrame.T](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.T.html)()
  - Transpone el `DataFrame`.
* - [DataFrame.assign](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.assign.html)(**kwargs)
  - Asignar nuevas columnas a un `DataFrame`. Útil para crear columnas nuevas que sean resultados de operaciones con otras columnas o transformación de las mismas. **PONER EJEMPLO**
* - [DataFrame.combine](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.combine.html)(other, func[, fill_value, ...])
  - Realiza una combinación por columnas con otra `DataFrame` según una función `func`.
* - [DataFrame.combine_first](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.combine_first.html)(other)
  - Actualiza los elementos nulos con valor en la misma ubicación en `other`.
* - [DataFrame.compare](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.compare.html)(other[, align_axis, ...])
  - Compara con otro `DataFrame` y muestra las diferencias.
* - [DataFrame.drop](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop.html)([labels, axis, index, ...])
  - Elimina las etiquetas especificadas de filas o columnas (elimina toda la columna/s o fila/s).
* - [DataFrame.explode](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.explode.html)(column[, ignore_index])
  - Transforma una columna de un `DataFrame` cuyos elementos son `list-like`, en un `DataFrame` donde cada elemento de los `list-like` se convierte en una fila en el `DataFrame`, las nuevas filas mantendrán el mismo índice que la lista original.
* - [DataFrame.insert](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.insert.html)(loc, column, value[, ...])
  - Inserta una columna en el `DataFrame` en el lugar especificado.
* - [DataFrame.mask](http://pandas.pydata.org/docs/reference/api/pandas.DataFrame.mask.html)(cond[, other, inplace, axis, level])
  - Reemplaza valores donde la condición es `True`.
* - [DataFrame.replace](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.replace.html)([to_replace, value, ...])
  - Reemplaza los valores `to_replace` con `value`.
* - [DataFrame.stack](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.stack.html)([level, dropna, sort, ...])
  - Convierte una o más columnas a índice. Retornando un objeto con un multi índice. Útil cuando se tiene más de un nivel en las columnas. Las columnas pasarán a ser el nivel más profundo (-1).
* - [DataFrame.transpose](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.transpose.html)(*args[, copy])
  - Transpone el índice y las columnas.
* - [DataFrame.update](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.update.html)(other[, join, overwrite, ...])
  - Actualiza _in-place_ utilizando valores que no sean `NA` de otro `DataFrame`. La actualización se hace con base a las coordenadas del índice y las columnas.
* - [DataFrame.unstack](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.unstack.html)([level, fill_value, sort])
  - Convierte uno o más niveles de índices a columnas. Los valores de estos pasarán a ser el nivel más profundos en las columnas. Si el índice no es multi-índice entonces retorna un `Series` en el que las columnas del `DataFrame` pasarán a ser el índice principal y el índice del `DataFrame` pasará a ser el índice interior.
* - [DataFrame.where](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.where.html)(cond[, other, inplace, ...])
  - Reemplaza valores donde la condición es `False`.
```

<br/>

---
### Ordenar

Métodos útiles para ordenar un `DataFrame`. 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [DataFrame.sort_index](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_index.html)(*[, axis, level, ...])
  - Ordena el `DataFrame` con base a las etiquetas del índice.
* - [DataFrame.sort_values](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_values.html)(by, *[, axis, ...])
  - Ordena por los valores a lo largo de cualquiera de los ejes.
```

<br/>

---
### Pivot y unpivot

Métodos para cambiar tablas tabulares entre formatos _wide_ y _long_.

```{list-table}
:header-rows: 1
:name: pandas-df-methods-pivot-unpivot

* - Método
  - Descripción
* - [DataFrame.melt](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.melt.html)([id_vars, value_vars, ...])
  - Sirve para modificar una _pivot table_  de _wide_ a _long format_ (_unpivot_), esto es, que algunas columnas se convertirán en observaciones de una sola columna dentro de la _large table_ y los valores pasarán a ser una columna de la misma.
* - [DataFrame.pivot](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pivot.html)(*, columns[, index, values])
  - Sirve para modificar una tabla de _long format_ a _wide format_ (_pivot_), basado en los valores de una columna. Esta función no soporta _aggregates_, para ello utilizar el método _.pivot_table()_.
* - [DataFrame.pivot_table](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pivot_table.html)([values, index, ...])
  - Crea una tabla en formato _wide_, similar a la que se crearía con _.groupby()_, es decir, para cada valor único de una columna categórica calcula algo sobre los valores de una columna de valores. También se puede hacer lo mismo para las combinaciones únicas de los valores de dos o más columnas categóricas y se puede hacer más de un calculo sobre las columna de valores. Es posible aplicar _aggregates_ específicos a funciones específicas con `dict`.
```

:::{tip}
Para ver cómo se utilizan estos métodos visitar {ref}`pandas-df-pivot-unpivot`.
:::

<br/>

---
### Selección, filtrado e iteración de elementos

Lorem ipsum dolor sit amet, consectetur adipiscing elit. 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [DataFrame.\_\_iter__](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.__iter__.html)()
  - Retorna un `iterator` de las etiquetas de las columnas.
* - [DataFrame.at](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.at.html)()
  - Accede a un valor único para un par de etiquetas de fila/columna. Similar a `DataFrame.loc[]`.
* - [DataFrame.filter](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.filter.html)([items, like, regex, axis])
  - Subconjunto de las filas o columnas del `DataFrame` según las etiquetas especificadas.
* - [DataFrame.get](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.get.html)(key[, default])
  - Accede a los elementos dada una etiqueta del índice/columnas, puede retornar tanto escalares como `Series` y `DataFrame`.
* - [DataFrame.head](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.head.html)([n])
  - Retorna las primeras _n_ filas.
* - [DataFrame.iat](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iat.html)()
  - Accede a un valor único para un par de fila/columna por posición de entero. Similar a `DataFrame.iloc[]`.
* - [DataFrame.iloc](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iloc.html)()
  - Accede a un valor o un conjunto de valores dadas las posiciones del índice o un `array-like` booleano.
* - [DataFrame.items](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.items.html)()
  - Retorna un `iterable` de tuplas `(col_label, Series)`.
* - [DataFrame.iterrows](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iterrows.html)()
  - Retorna un `iterable` de tuplas  `(ind_label, Series)`.
* - [DataFrame.itertuples](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.itertuples.html)([index, name])
  - Retorna un `iterable` de `namedtuple`. Los nombres del `tuple` serán `Index` y el nombre de cada una de las columnas y los valores serán el nombre del índice y los valores de esa fila en cada una de las columnas.
* - [DataFrame.loc](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html)()
  - Accede a un valor o un conjunto de valores dadas las etiquetas del índice o un `array-like` booleano.
* - [DataFrame.pop](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pop.html)(item)
  - Elimina y retorna una columna dada su etiqueta de columna.
* - [DataFrame.query](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.query.html)(expr, *[, inplace])
  - Sirve para aplicar comparaciones booleanas con las columnas de un DataFrame. **EJEMPLO**
* - [DataFrame.tail](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.tail.html)([n])
  - Retorna las últimas _n_ filas.
* - [DataFrame.take](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.take.html)(indices[, axis])
  - Retorna los elementos en los índices posicionales dados a lo largo de un eje. Los índices se pueden repetir. Es similar a hacer _fancy indexing_ con índices implícitos.
* - [DataFrame.truncate](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.truncate.html)([before, after, axis, copy])
  - Trunca un `DataFrame` antes y después de algún valor de índice.
* - [DataFrame.xs](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.xs.html)(key[, axis, level, drop_level])
  - Retorna una sección transversal del `DataFrame`. Particurlamente útil cuando el `DataFrame` tiene un `MultiIndex` en las filas o columnas y se quiere acceder a secciones enteras de un nivel o combinaciones de los niveles/subniveles.
```

<br/>

---
### Uniones

Métodos útiles para unir el `DataFrame` con otros objetos de `pandas`. 

```{list-table}
:header-rows: 1
:name: pandas-df-methods-joins

* - Método
  - Descripción
* - [DataFrame.join](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.join.html#pandas.DataFrame.join)(other[, on, how, lsuffix, ...])
  - Une columnas de `DataFrame`s de una manera similar a un _join_ de SQL, con base a valores de columnas o de los índices. Para más flexibilidad al definir el _join_ usar `DataFrame.merge()` o la función `pd.merge()`
* - [DataFrame.merge](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.merge.html#pandas.DataFrame.merge)(right[, how, on, left_on, ...])
  - Une columnas de `DataFrame`s de una manera similar a un _join_ de SQL, con base a valores de columnas o de los índices. Permite más flexibilidad que `DataFrame.join()`.
```

<br/>

---
### Valores duplicados

Métodos útiles para el manejo de valores duplicados. 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [DataFrame.drop_duplicates](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop_duplicates.html)([subset, keep, ...])
  - Retorna `DataFrame` con los valores duplicados eliminados.
* - [DataFrame.duplicated](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.duplicated.html)([subset, keep])
  - Retorna `Series` booleano que denota filas duplicadas.
```

<br/>

---
### Valores nulos

Métodos útiles para el manejo de valores nulos. 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [DataFrame.bfill](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.bfill.html)(*[, axis, inplace, limit, ...])
  - Reemplaza los valores `NA/NaN` utilizando la siguiente observación válida, en el eje indicado.
* - [DataFrame.dropna](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dropna.html)(*[, axis, how, thresh, ...])
  - Elimina las filas o columnas de un `DataFrame` con base a los `NA/NaN`. Por default elimina las filas que contengan al menos un valor `NA/NaN`. Se puede especificar el número mínimo de valores `NA` que debe haber con _how_ y _thresh_.
* - [DataFrame.ffill](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.ffill.html)(*[, axis, inplace, limit, ...])
  - Reemplaza los valores `NA/NaN` utilizando la última observación válida, en el eje indicado.
* - [DataFrame.fillna](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.fillna.html)([value, method, axis, ...])
  - Reemplaza los valores `NA/NaN` utilizando el método especificado, en el eje indicado.
* - [DataFrame.interpolate](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.interpolate.html)([method, axis, limit, ...])
  - Reemplaza los valores de `NaN` utilizando un método de interpolación, en el eje indicado.
* - [DataFrame.isna](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.isna.html)()
  - Indica los valores nulos.
* - [DataFrame.isnull](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.isnull.html)()
  - Indica los valores nulos. Similar a `DataFrame.isna()`.
* - [DataFrame.notna](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.notna.html)()
  - Indica los valores no nulos.
* - [DataFrame.notnull](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.notnull.html)()
  - Indica los valores no nulos. Similar a `DataFrame.notna()`.
```

<br/>

### Valores únicos

Métodos para obtener información sobre valores únicos en el `DataFrame`.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [DataFrame.nunique](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.nunique.html)([axis, dropna])
  - Retorna el número de elementos únicos en el eje especificado.
* - [DataFrame.value_counts](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.value_counts.html)([subset, normalize, ...])
  - Retorna un `Series` que contiene la frecuencia de cada fila distinta en el `DataFrame`. Se puede elegir un subcojunto de columas para determinar las filas únicas.
```

<br/>

---
## Accesor _sparse_

Si `DataFrame` es de tipo `sparse` existen métodos especiales usando el _accessor_ `sparse`. 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [DataFrame.sparse.density](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sparse.density.html)()
  - Relación entre puntos no dispersos y puntos de datos totales (densos).
* - [DataFrame.sparse.from_spmatrix](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sparse.from_spmatrix.html)(data[, ...])
  - Crea un nuevo `DataFrame` de un arreglo _sparse_ de `scipy`.
* - [DataFrame.sparse.to_coo](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sparse.to_coo.html)()
  - Devuelve el contenido del `DataFrame` como un arreglo _sparse_ de `scipy`.
* - [DataFrame.sparse.to_dense](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sparse.to_dense.html)()
  - Convierte un `DataFrame` con valores escasos a densos.
```

