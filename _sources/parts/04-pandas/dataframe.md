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

Algunas características de los `DataFrame` son:
- Los `DataFrame` se podrían considerar como secuencias bidimensionales. Generalmente las columnas representan variables y las filas representan observaciones.
- Sirven para almacenar múltiples valores de diferentes tipos en un un solo objeto. El almacenamiento se hace de una manera similar a como se haría en una tabla, es decir, por filas y columnas. Cada columna es un `Series`.
- Es mutable: Sus elementos se pueden modificar.
- Está indexado: Cada elemento está asociado con un índice y por lo tanto sus elementos están ordenados. Además sus elementos también se pueden identificar por medio de una etiqueta.
- Es un iterable: Se puede iterar por sus elementos y se puede usar la palabra reservada `in` para verificar memebresía, pero la verificación se hará sobre el índice y no sobre los valores.
- Se puede apilar con otros `DataFrame`.

<br/>

---
(pandas-df-creacion)=
## Creación de _DataFrame_

La forma más sencilla de crear un objeto `DataFrame` es con el constructor.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [pandas.DataFrame](https://pandas.pydata.org/docs/reference/frame.html#constructor)([data, index, columns, dtype, copy])
  - Objeto bidimensional con columnas potencialmente heterogéneas para datos tabulares.
```
**Notas**:
- _data_: Es un objeto que contiene los datos, se puede definir de diversas formas:
    - `dict`: Los _keys_ serán las etiquetas de las columnas y los _values_ pueden ser `Series`, `array-like` o `list`, todos de la misma longitud, serán los valores de las filas en sus respectivas columnas. De esta forma se llena columna por columna.
    - `array-like`: Cada elemento interno será una fila, por lo que todos los elementos deben de tener la misma longitud. De esta forma se llena fila por fila. Si se difine el parámetro _columns_ debe tener la misma logitud que las listas internas y si se define el parámetro _index_ debe de tener la misma longitud que la lista externa.
    - `dict` de `dict`: Se interpreta como que los _outer keys_ son las etiquetas de las columnas y los _inner keys_ son las etiquetas de las filas y los _inner values_ son los valores del `DataFrame`.
    - `list` de `dict`: Los _keys_ serán las etiquetas de las columnas y los _values_ son los valores de una fila, cada `dict` represente una fila y por lo tanto los _keys_ de todos los diccionarios deben de ser los mismos, en caso de que haya _keys_ que no se comparten tendrán valores `NaN`.
- _index_: Es un `array-like` o un objeto `Index` con las etiquetas de las filas. Normalmente debe ser de la misma longitud que _data_. 
- _columns_: Es un `array-like` o un objeto `Index` con las etiquetas de las columnas.

:::{note}
Para otras opciones de construir `DataFrame` revisar los métodos de {ref}`pandas-df-metodos-contruccion`.
:::

<br/>

**Ejemplo**: A continuación se crea un objeto `DataFrame` que tiene la información de algunos estados de Estados Unidos, como su capital, población y área. Notar que los nombres de los estados son el índice explícito del `df`.

```{code-cell} ipython3
# Importar librería
import pandas as pd

# Crear diccionario con los datos
data={
    'Capital': ['Sacramento', 'Austin', 'Tallahassee', 'Albany'],
    'Population': [39.24, 29.5, 21.96, 20.2],
    'Area (km2)': [423970, 695662, 170451, 122283]
}

# Crer df, aquí se indica el 'index'
df=pd.DataFrame(data, index=['California', 'Texas', 'Florida', 'New York'])

# Imprimir el df
print(df)
```

<br/>

---
(pandas-df-seleccion-elementos)=
## Selección de elementos

Existen diversos métodos para seleccionar elementos en un `DataFrame`. Aquí se explicarán los más comunes. Todos los ejemplos de esta sección utilizará el `df` definido en [la sección anterior](pandas-df-creacion).


### Notación con corchetes

Al ser los `DataFrame` estructuras bidimensionales es posible seleccionar filas o columnas. Esto se puede hacer con los índices explícitos.

:::{caution}
El uso de los índices implícitos con esta notación está desaconsejado (excepto _slices_ sobre las filas), para ello se recomienda usar el método `.iloc[]`.
:::

- **Indexing**: Seleccionar columnas concretas usando las etiquetas de las columnas.
  - **Columnas completas**  - `Series`: Para seleccionar una columna y retornar `Series`, utilizar corchetes y el nombre de la columna. También se puede utilizar la notación punto `.`, en este caso la etiqueta no debe tener espacios, ni caracteres especiales, ni ser una palabra reservada: <br/> `X['label']` <br/> `X.label`

<br/>

- **Slicing**: Seleccionar _slices_ sobre las filas indicando su índice implícito.
  - **Filas completas**  - `DataFrame`: Retorna _slices_ de filas para todas las columnas: <br/> `X[start:stop:step]`

<br/>

- **Fancy indexing**: Seleccionar un conjunto de columnas con base a las etiquetas. 
  - **Columnas completas** - `DataFrame`: Para seleccionar una columna y retornar `DataFrame`, utilizar dobles corchetes y el nombre de la columna: <br/> `X[['label']]`
  - **Múltiples columnas** - `DataFrame`: Para seleccionar múltiples columnas y retornar `DataFrame`, utilizar dobles corchetes y los nombres de las columnas. Las etiquetas se pueden poner en cualquier orden e incluso se pueden repetir múltiples veces: <br/> `X[['label1', 'label2', ...]]`

<br/>

- **Boolean masking**: Selección de filas para todas las columnas, con base a una secuencia booleana denominada _mask_. 
    - **Mask en filas** - `Series`: Retorna los elementos que satisfacen el _mask_ en el eje cero. Normalmente el _mask_ se crea usando una columna del `DataFrame` y {ref}`Operadores de comparación <built-in-operadores-comparacion>`: <br/> `X[mask]`

:::{tip}
Se pueden usar los operadores {ref}`built-in-operadores-bitwise` para crear _mask_ más complejos: <br/> `X[(mask1) & (mask2)] # Ejemplo con '&'`
- Notar que cada _mask_ se pone entre paréntesis.
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

# Boolean masking: Seleccionar elementos que tenga una area mayor a 300,000
print(df[df['Area (km2)']>300000])
```

<br/>

---
### Usando método _.loc[]_

El método `.iloc[]` es útil para seleccionar elementos con base al **índice explícito**.

:::{attention}
En esta sección tener en cuenta las siguientes nomenclaturas:
- _'ind'_: Se refiere a una etiqueta del índice.
- _'col'_: Se refiere a una etiqueta de las columnas.
- `'indi':'indj'`: Se refiere a un _slice_, entre las etiquetas del índice 'indi' e 'indj'
- `'coli':'colj'`: Se refiere a un _slice_, entre las etiquetas de las columnas 'coli' y 'colj'
- `'ind1', 'ind2', ...`: Se refiere a varias etiquetas del índice.
- `'col1', 'col2', ...`: Se refiere a varias etiquetas de las columnas.
:::

- **Indexing**: Útil para seleccionar elementos específicos.
	- **Elemento específico** - `object`: Retorna el elemento en las etiquetas _'ind'_ y _'col'_: <br/>  `X.loc['ind', 'col']`
	
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
	- **Filas completas** - `Series`: Retorna la fila completa con la etiqueta _'ind'_ como `Series`: <br/> `X.loc['ind']` <br/> `X.loc['ind', :]` 
	- **Filas completas** - `DataFrame`: Retorna la fila completa con la etiqueta _'ind'_ como `DataFrame`: <br/> `X.loc[['ind']]` <br/> `X.loc[['ind'], :]` 
	- **Múltiples filas completas** - `DataFrame`: Retorna las filas completas con los índices indicados: <br/> `X.loc[['ind1', 'ind2', ...]]` <br/> `X.loc[['ind1', 'ind2', ...], :]` 
	- **Columna completa** - `Series`: Retorna la columna completa con la etiqueta _'col'_ como `Series`: <br/> `X.loc[:, 'col']`
	- **Columna completa** - `DataFrame`: Retorna la columna completa con la etiqueta _'col'_ como `DataFrame`: <br/> `X.loc[:, ['col']]`
	- **Múltiples columnas completas** - `DataFrame`: Retorna las columnas completas en los índices indicados: <br/> `X.loc[:, ['col1', 'col2', ...]]`
	- **Mask en filas** - `DataFrame`: Retorna las filas que satisfacen un _mask_. Asegurarse que el _mask_ esté conformado por valores booleanos y no por _1s_ y _0s_: <br/> `X.loc[row_mask, :]`
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
### Usando método _.iloc[]_

El método `.iloc[]` es útil para seleccionar elementos con base al **índice implícito**.

- **Indexing**: Útil para seleccionar elementos específicos:
	- **Elemento específico** - `object`: Retorna el elemento en índice _i_ y la columna _j_ como `scalar`, los índices empiezan en cero: <br/> `X.iloc[i, j]`

<br/>

- **Slicing**: Útil para seleccionar _slices_ tanto de filas como de columnas. Se separan los _slicers_ para las filas y las columnas con una coma.
	- **Slices de filas** - `DataFrame`: Retorna filas completas para todas las columnas: <br/> `X.iloc[start:stop:step]`<br/> `X.iloc[start:stop:step, :]` 
	- **Slices de columnas** - `DataFrame`: Retorna columnas completas para todas las filas: <br/> `X.iloc[:, start:stop:step]`
	- **Slices de filas y columnas** - `DataFrame`: Retorna _slices_ de filas y columnas específicas: <br/> `X.iloc[start:stop:step, start:stop:step]`

<br/>

- **Fancy indexing**: Útil para seleccionar combinaciones de filas y columnas específicas. Los índices se pueden poner en culquier orden e incluso se puedo poner más de una vez. Las filas y columnas se separan por coma.
	- **Combinación de filas y columnas** - `DataFrame`: Retorna las filas y columnas completas en los índices indicados: <br/> `X.iloc[[i1, i2, ...], [j1, j2, ...]`

<br/>

- **Combinación de estrategias**: Aquí se presentan algunas opciones de combinación de estrategias para las filas y columnas que permiten mayor versatibilidad para seleccionar elementos, particularmente columnas. **Importante**. Esta no es una lista extensiva, en general se puede aplicar cualquier estrategia para selección de elementos (excepto _masking_), de manera independiente tanto para las filas, como para las columnas.
	- **Filas completas**  - `Series`: Retorna la fila completa en el índice _i_ como `Series`, los índices empiezan en cero: <br/> `X.iloc[i]` <br/> `X.iloc[i, :]` 
	- **Filas completas**  - `DataFrame`: Retorna la fila completa en el índice _i_ como `DataFrame`, los índices empiezan en cero: <br/> `X.iloc[[i]]` <br/> `X.iloc[[i], :]`
	- **Múltiples filas completas** - `DataFrame`: Retorna las filas completa en los índices indicados: <br/> `X.iloc[[i1, i2, ...]]` <br/> `X.iloc[[i1, i2, ...], :]`
	- **Columna completa** - `Series`: Retorna la columna completa en el índice _j_ como `Series`: <br/> `X.iloc[: , j]`
	- **Columna completa** - `DataFrame`: Retorna la columna completa en el índice _j_ como `DataFrame`: <br/> `X.iloc[: , [j]]`
	- **Múltiples columnas completa**  - `DataFrame`: Retorna las columnas completas en los índices indicados: <br/> `X.iloc[: , [j1, j2, ...]]`
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
## Exploración básica

Para explorar el contenido de un `DataFrame` se puede hacer uso de varios métodos.
- `.describe()`: Genera estadísticas para cada una de las columnas.
- `.head(n=5)`: Imprime las primeras _n_ filas del `DataFrame`.
- `.info()`: Imprime información del `DataFrame` como número total de filas y columnas, nombre y tipo de cada una de las columnas, tipo de índice y rango del índice, resumen de los tipos de datos de las columnas.
- `.tail(n=5)`: Imprime las útlimas _n_ filas del `DataFrame`.

:::{note}
Existen varios atributos que retornan información relevante, para más información visitar {ref}`pd-dataframe-atributtes`.
:::

<br/><br/>

---
## Agregar columna

Para agregar una columna nueva simplemente asignar los valores a una etiqueta nueva.
```python
# Agregar nueva columna
X['label']=Y
```
- _X_ - `DataFrame`.
- _'label'_ será el nombre de la columna. 
- `Y` -  `Series`, `array-like`, `secuencia`: Asegurarse que el tamaño de este objeto coincida con el tamaño en el eje 0 del `DataFrame`
- **IMPORTANTE**: No se puede usar la notación `X.label=Y`.

<br/>

---
## Modificar valores

Se pueden acceder a determinados elementos con cualquier método de {ref}`pandas-df-seleccion-elementos` y asignarle un nuevo valor.

:::{warning}
Al asignar elementos asegurarse que los tipos coincidan con los tipos de las columnas donde se modificarán los valores o al menos que sea posible forzar la conversión.
:::

```python
# Modificar elementos específicos
df.loc['ind', 'col']=val	
df.iloc[i, j]=val

# Múltiples valores con mismo valor (ejemplo con slicing)
df.loc[:, ['col']]=val

# Múltiples valores con diferentes valores (ejemplo con slicing)
df.loc[:, ['col']]=[val1, val2, ...]
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
## Iteración

Para iterar sobre las columnas o filas usar las siguientes opciones:

```python
# Iteración por las etiquetas de las columnas
for col in df:
    # for body

# Iteración por las filas
for index, data in df.iterrows():
	# for body

# Iteración por las filas como namedtuple
for row in df.itertuples():
	# for body
```
- _col_ tendrá los _labels_ de las columnas de `DataFrame`.
- _index_ será el índice de la fila en la iteración.
- _data_ será un `Series`, que contendrá la información de todas las columnas para cada fila en la iteración, el índice de _data_ será el nombre de la columna de _df_. Se puede aplicar cualquier método de selección de elementos de `Series` en _data_.
- _row_ será un {ref}`modulos-collections-named-tuple`.

:::{note}
Para más opciones de iteración o más información revisar los métodos en la sección de {ref}`pd-df-metodos-seleccion-filtrado-iteracion`, particularmente los métodos:
- `.__iter__`: Retorna `iterator` de las etiquetas de las columnas del `DataFrame`.
- `.items`: Retorna un `iterable` de tuplas _(col_label, series)_.
- `.iterrows`: Retorna un `iterable` de tuplas _(ind_label, series)_.
- `.itertuples`: Retorna un `iterable` de `namedtuple` (sobre las filas) cuyos nombres serán las etiquetas de las columnas y más aparte del nombre _Index_ que hace referencia a la etiqueta del índice en la fila.
:::

<br/>

---
## Uniones y apilaciones

Para unir objetos de pandas, ya sea apilando los objetos o en una operación similar a un _join_ de SQL, revisar los siguientes funciones de `pandas` o métodos:
- `DataFrame.join()`: Permite unir columnas de objetos de `pandas` con base a valores de columnas o de los índices de una manera similar a un _join_ de SQL.
- `DataFrame.merge()`: Permite unir columnas de objetos de `pandas` con base a valores de columnas o de los índices de una manera similar a un _join_ de SQL. Permite más flexibilidad que `DataFrame.join()`.
- `pd.concat()`: Concatena objetos sobre un eje existe, resultando en un objeto con el mismo número de dimensiones que los objetos originales. Se puede indicar si el _index_ se debe de reiniciar o indicar a que objeto pertenecía cada fila.
- `pd.merge()`: Permite unir objetos de `pandas` con base a valores de columnas o de los índices de una manera similar a un _join_ de SQL.

:::{note}
Para más información visitar {ref}`Funciones de uniones y apilaciones <pandas-func-joins>` y {ref}`Métodos de unión <pandas-df-methods-joins>`.
:::



---
(pandas-df-pivot-unpivot)=
## Pivot y unpivot

En datos tabulares existen dos formatos principales:
1. **Long format**: También denominada _unpivot_, cada columna en la tabla representa una variable en los datos. Por lo tanto, los mismos valores se pueden repetir en múltiples filas y existe una o más columnas de valores. 
2. **Wide format**: También denominada _pivot_, distribuye los valores de una o mas variables categóricas a lo largo de las columnas, se establece un “índice” con los valores únicos de una columna categórica o las combinaciones únicas de dos más columnas categóricas y la columna de valores  pasa a ser los valores/cálculos de las mismas. Además es posible añadir totales para filas y columnas.


```{figure} ../images/wide-long-format.png
:name: wide-and-long-format
:width: 500px
:align: center

Visualización de _wide_ y _long format_.
```

Los objetos `DataFrame` tiene algunos métodos para cambiar de un formato a otro:
- `melt()`: Sirve para pasar de un _wide format_ a _long format_.
- `pivot()`: Permite pasar de _long format_ a _wide format_, no soporta _aggregates_ en los valores ni el calculo de subtotales y/o totales.
- `pivot_table()`: Permite pasar de _long format_ a _wide format_, soporta _aggregates_ en los valores y permite el calculo de totales.

:::{note}
Para más información de estos métodos visitar {ref}`Métodos de pivot y unpivot <pandas-df-methods-pivot-unpivot>`
:::

<br/>

**Ejemplos**:

```{code-cell} ipython3
# Definir DataFrame
long=pd.DataFrame({'col1': ['A', 'A', 'B', 'B', 'C', 'C'],
                    'col2': ['X', 'Y']*3,
                    'col3': [*range(1, 7)]})
print("DataFrame:", long, sep='\n', end='\n'*2)

# Pivot
pivot=long.pivot(columns='col2', index='col1', values='col3')
print("Pivot:", pivot, sep='\n', end='\n'*2)

# Unpivot
unpivot=pivot.reset_index().melt(id_vars='col1', var_name='col2', value_name='col3')
print("Unpivot:", unpivot, sep='\n', end='\n'*2)

# Pivot con totales
wide=long.pivot_table(values='col3', index='col1', columns='col2', aggfunc='sum', margins=True)
print("Pivot con totales:", wide, sep='\n')
```

<br/>

---
(pd-dataframe-atributtes)=
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
  - El índice (etiquetas de fila) del `DataFrame` como `Index` o una subclase del mismo. También se puede usar para establecer el índice asignándolo a un `list-like`.
* - [DataFrame.ndim](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.ndim.html)
  - Retorna un `int` que representa el número de ejes/dimensiones de la matriz.
* - [DataFrame.shape](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.shape.html)
  - Retorna un `tuple` que representa la dimensionalidad (número de elementos en cada eje) del `DataFrame`.
* - [DataFrame.size](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.size.html)
  - Retorna un `int` que representa el número total de elementos de este objeto.
* - [DataFrame.values](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.values.html)
  - Retorna una representación _ndarray_ de los valores del `DataFrame`.
```

<br/>


## Métodos

Atributos del objeto `DataFrame`.

(pandas-df-metodos-contruccion)=
### Construcción

Métodos para construir objetos `DataFrame` desde otros objetos.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [DataFrame.from_dict](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.from_dict.html)(data[, orient, dtype, ...])
  - Contruye un `DataFrame` desde un `dict` con valores `array-like` o `dict`.
* - [DataFrame.from_records](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.from_records.html)(data[, index, ...])
  - Contruye un `DataFrame` desde un array estructura, un `list` de `dict` o un `list` de `tuple`.
```

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

Patrones útiles:
```python
# Convertir una columna a float
df['num_col']=df['num_col'].astype('float')

# Convertir a categórica
cats=df['col'].unique()
df['col']=df['col'].astype('category', ordered=True, categories=cats)
```

<br/>

### IO y Serialización

Métodos para exportar el `DataFrame` en un formato específico o serializar el mismo. 

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

Patrones útiles:
```python
# Exportar a excel
df.to_excel(excel_writer='path/to/file.xls', sheet_name='sheet_name'[,startrow, startcol])

# Exportar a múltiples hojas
with pd.ExcelWriter('path/to/file.xlsx') as writer:
    df.to_excel(excel_writer=writer, sheet_name='sheet_name'[,startrow, startcol])
    df2.to_excel(excel_writer=writer, sheet_name='sheet_name2'[,startrow, startcol])
    ...
```

<br/>

### Cálculos y operadores

Métodos para realizar cálculos con el `DataFrame` o métodos equivalentes a operadores de Python. 

(pd-dataframe-methods-aggregates)=
#### Aggregates

Métodos para calcular _aggregates_, en esencia calculan un único número de resumen para algún eje del `DataFrame`. En esta categoría se enlistan todos los métodos que cumplen esa descripción, pero los mismos métodos se podrán encontrar en otras categorías.

:::{note}
Estos métodos ignoran valores `NA`/`NaN`, a menos de que se indique lo contrario.
:::

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [DataFrame.agg](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.agg.html)([func, axis])
  - Agrega usando una o más operaciones sobre el eje especificado.
* - [DataFrame.aggregate](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.aggregate.html)([func, axis])
  - Agrega usando una o más operaciones sobre el eje especificado.
* - [DataFrame.all](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.all.html)([axis, bool_only, skipna])
  - Retorna `True` si todos los valores son `True` sobre un eje.
* - [DataFrame.any](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.any.html)(*[, axis, bool_only, skipna])
  - Retorna `True` si hay al menos un valor `True` sobre un eje.
* - [DataFrame.corr](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.corr.html)([method, min_periods, ...])
  - Calcula la correlación por pares de columnas, excluyendo `NA`/valores nulos.
* - [DataFrame.corrwith](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.corrwith.html)(other[, axis, drop, ...])
  - Calcula la correlación por pares con otro objeto.
* - [DataFrame.count](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.count.html)([axis, numeric_only])
  - Retorna el conteo de los valores no nulos sobre el eje indicado.
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
* - [DataFrame.prod](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.prod.html)([axis, skipna, numeric_only, ...])
  - Retorna el producto de los valores sobre el eje indicado.
* - [DataFrame.product](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.product.html)([axis, skipna, ...])
  - Retorna el producto de los valores sobre el eje indicado.
* - [DataFrame.sample](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sample.html)([n, frac, replace, ...])
  - Retorna una muestra aleatoria de elementos de un eje del objeto.
* - [DataFrame.sem](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sem.html)([axis, skipna, ddof, numeric_only])
  - Retorna el error estándar de la media sobre el eje indicado.
* - [DataFrame.skew](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.skew.html)([axis, skipna, numeric_only])
  - Retorna el sesgo sobre el eje indicado.
* - [DataFrame.std](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.std.html)([axis, skipna, ddof, numeric_only])
  - Retorna la desviación estándar de la muestra sobre el eje indicado.
* - [DataFrame.sum](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sum.html)([axis, skipna, numeric_only, ...])
  - Retorna la suma de los valores sobre el eje indicado.
* - [DataFrame.var](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.var.html)([axis, skipna, ddof, numeric_only])
  - Retorna la varianza sobre el eje indicado.
```

##### Notas de _aggregate_

Aplica cálculos a los valores de un `DataFrame` sobre el eje indicado. Es lo mismo que `.agg()`.
```python
DataFrame.agg(func=None, axis=0)
```
- **Parámetros:**
    - **func** \- `function`, `str`, `list`, `dict`: La función de agregación.
        -  `function`: Una función.
            -  Las funciones de `numpy` se pueden usar, por ejemplo `np.mean`.
            - Se puede especificar una función personaliza o una _lambda function_, pero tener en cuenta que la función debe de recibir un `Series` y retornar un escalar.
        -  `str`: El nombre de una función de agregación. Los nombres válidos son: _'sum', 'prod', 'mean', 'median', 'min', 'max', 'std', 'var', 'sem', 'count', 'nunique', 'size', 'first', 'last', 'quantile', 'mad', 'skew', 'kurt'_.
        -  `list`: Si se quiere aplicar más de una función utilizar una lista de funciones o nombres de funciones.
        -  `dict`: Se puede especificar una función específica a cada columna con un diccionario, donde las _keys_ son las etiquetas de las columnas y los _value_ son las funciones de agregación, también se puede usar un `list` de funciones como _value_ si se desea aplicar más de una función.
    - **axis** \- {0 o 'index', 1 o 'columns'}: Eje sobre el cual realizar la operación.

Patrones útiles:
```python
# Calcular función personalizada
def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)
df['col_name'].agg(iqr)

# Calcular aggregate en mútiples columnas
df[['col1_name', 'col2_name', ...]].agg(iqr)

# Calcular mútiples aggregates en una columna
df['col_name'].agg([iqr, agg_func2, ...])

# Calcular múltiples aggregate en mútiples columnas
df[['col1_name', 'col2_name', ...]].agg([iqr, agg_func2, ...])

# Calcular aggregates diferentes por columna
df[['col1_name', 'col2_name', ...]].agg({'col1_name': iqr, 
                                         'col2_name': agg_func2,
                                         ...})
```

<br/>

#### Booleanos

Métodos para trabajar con `DataFrame` que contienen valores `bool`.

:::{note}
Estos métodos ignoran valores `NA`/`NaN`, a menos de que se indique lo contrario.
:::

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

Métodos para calcular productos o sumas acumuladas, también cálculo de diferencias y cambios porcentuales con desfases y rankings.

:::{note}
Estos métodos ignoran valores `NA`/`NaN`, a menos de que se indique lo contrario.
:::

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
  - Calcula los rangos de datos numéricos (1 a _n_) a lo largo del eje.
```

<br/>

#### Estadísticas

Métodos para el cálculo de estadísticas descriptivas, generar muestras aleatorias o calcular correlaciones y covarianzas entre dos variables.

:::{note}
Estos métodos ignoran valores `NA`/`NaN`, a menos de que se indique lo contrario.
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

Métodos útiles para trabajar con los valores numéricos ordenados, y algunos estadísticos destacados como mínimos, máximos, medianas y cuantiles.

:::{note}
Estos métodos ignoran valores `NA`/`NaN`, a menos de que se indique lo contrario.
:::

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
  - Retorna el cuantil dado de los valores sobre el eje indicado. _q_ es un valor entre cero y uno.
```

<br/>

#### Misceláneos

Otros métodos de naturaleza numérica.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [DataFrame.abs](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.abs.html)()
  - Retorna un `DataFrame` con el valor numérico absoluto de cada elemento.
```

<br/>

#### Operadores aritméticos y similares.

Métodos para realizar operaciones binarias con operadores aritméticos y sus equivalentes que tienen por sufijo una `r` útiles para intercambiar las posiciones del `DataFrame` y del argumento _other_. 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [DataFrame.add](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.add.html)(other[, axis, level, fill_value])
  - Retorna la suma del `DataFrame` y _other_, por elementos. Equivale a usar el operador `+`.
* - [DataFrame.div](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.div.html)(other[, axis, level, fill_value])
  - Retornar la división flotante del `DataFrame` y _other_, por elementos. Equivale a usar el operador `/`.
* - [DataFrame.dot](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dot.html)(other)
  - Calcula el producto escalar entre `DataFrame` y _other_.
* - [DataFrame.eval](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.eval.html)(expr, *[, inplace])
  - Evalua una cadena que describe operaciones en las columnas de un `DataFrame`.
* - [DataFrame.floordiv](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.floordiv.html)(other[, axis, level, ...])
  - Retornar la división entera del `DataFrame` y _other_, por elementos. Equivale a usar el operador `//`.
* - [DataFrame.mod](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.mod.html)(other[, axis, level, fill_value])
  - Retornar el módulo de la división del `DataFrame` y _other_, por elementos. Equivale a usar el operador `%`.
* - [DataFrame.mul](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.mul.html)(other[, axis, level, fill_value])
  - Retornar la multiplicación del `DataFrame` y _other_, por elementos. Equivale a usar el operador `*`.
* - [DataFrame.pow](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pow.html)(other[, axis, level, fill_value])
  - Retornar la potenciación del `DataFrame` y _other_, por elementos. Equivale a usar el operador `^`.
* - [DataFrame.radd](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.radd.html)(other[, axis, level, fill_value])
  - Retorna la suma del `DataFrame` y _other_, por elementos. Equivale a usar el operador `+`.
* - [DataFrame.rdiv](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rdiv.html)(other[, axis, level, fill_value])
  - Retornar la división flotante de _other_ y `DataFrame`, por elementos. Equivale a usar el operador `/`, siendo _other_ el numerador.
* - [DataFrame.rfloordiv](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rfloordiv.html)(other[, axis, level, ...])
  - Retornar la división entera de _other_ y `DataFrame`, por elementos. Equivale a usar el operador `//`, siendo _other_ el numerador.
* - [DataFrame.rmod](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rmod.html)(other[, axis, level, fill_value])
  - Retornar el módulo de la división de _other_ y `DataFrame`, por elementos. Equivale a usar el operador `%`, siendo _other_ el numerador.
* - [DataFrame.rmul](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rmul.html)(other[, axis, level, fill_value])
  - Retornar la multiplicación del `DataFrame` y _other_, por elementos. Equivale a usar el operador `*`.
* - [DataFrame.rpow](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rpow.html)(other[, axis, level, fill_value])
  - Retornar la potenciación de _other_ y `DataFrame`, por elementos. Equivale a usar el operador `^`, siendo _other_ la base.
* - [DataFrame.rsub](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rsub.html)(other[, axis, level, fill_value])
  - Retornar la resta de _other_ y `DataFrame`, por elementos. Equivale a usar el operador `-`, siendo _other_ el minuendo.
* - [DataFrame.rtruediv](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rtruediv.html)(other[, axis, level, ...])
  - Retornar la división flotante del _other_ y `DataFrame`, por elementos. Equivale a usar el operador `/`, siendo _other_ el numerador. Permite reemplazar valores nulos por algún valor en particular.
* - [DataFrame.sub](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sub.html)(other[, axis, level, fill_value])
  - Retornar la resta del `DataFrame` y _other_, por elementos. Equivale a usar el operador `-`.
* - [DataFrame.truediv](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.truediv.html)(other[, axis, level, ...])
  - Retornar la división flotante del `DataFrame` y _other_, por elementos. Equivale a usar el operador `/`. Permite reemplazar valores nulos por algún valor en particular.
```

<br/>

#### Operadores de comparación y membresía.

Métodos para comparar los elementos del `DataFrame` con otro objeto o verificar que los elementos del `DataFrame` satisfagan ciertas condiciones, como verificar que estén entre un rango o un conjunto de valores concretos. 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [DataFrame.eq](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.eq.html)(other[, axis, level])
  - Indica la igualdad del `DataFrame` y _other_, por elementos. Equivale a usar el operador `==`.
* - [DataFrame.equals](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.equals.html)(other)
  - Verifica si dos objetos contienen los mismos elementos.
* - [DataFrame.ge](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.ge.html)(other[, axis, level])
  - Indica si es mayor o igual el `DataFrame` y _other_, por elementos. Equivale a usar el operador `>=`.
* - [DataFrame.gt](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.gt.html)(other[, axis, level])
  - Indica si es mayor el `DataFrame` y _other_, por elementos. Equivale a usar el operador `>`.
* - [DataFrame.isin](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.isin.html)(values)
  - Retorna `DataFrame` booleano que indica si cada elemento del `DataFrame` está contenido en `values`.
* - [DataFrame.le](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.le.html)(other[, axis, level])
  - Indica si es menor o igual el `DataFrame` y _other_, por elementos. Equivale a usar el operador `<=`.
* - [DataFrame.lt](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.lt.html)(other[, axis, level])
  - Indica si es manor el `DataFrame` y _other_, por elementos. Equivale a usar el operador `<`.
* - [DataFrame.ne](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.ne.html)(other[, axis, level])
  - Indica si no son iguales el `DataFrame` y _other_, por elementos. Equivale a usar el operador `!=`.
```

<br/>

#### Series de tiempo

Métodos útiles para `DataFrame` que tienen un `Index` que representa una serie de tiempo (no necesariamente).

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [DataFrame.asfreq](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.asfreq.html)(freq[, method, how, ...])
  - Modifica la frecuencia de una serie de tiempo. El `DataFrame` debe de tener un índice `datetime-like`. Si se va a realizar un _aggregate_ con la nueva frecuencia se recomienda usar el método `DataFrame.resample()`.
* - [DataFrame.asof](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.asof.html)(where[, subset])
  - Retorna la/s última/s fila/s válida sin incluir `NaNs`s antes o en _where_, donde _where_ son etiquetas del índice.
* - [DataFrame.at_time](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.at_time.html)(time[, asof, axis])
  - Selecciona valores en un momento particular del día (por ejemplo, 9:30 a. m.).
* - [DataFrame.between_time](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.between_time.html)(start_time, end_time)
  - Selecciona valores entre horas particulares del día (por ejemplo, de 9:00 a 9:30 a. m.).
* - [DataFrame.resample](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.resample.html)(rule[, axis, closed, ...])
  - Modifica la frecuencia de una serie de tiempo, útil si se realizará un _aggregate_ con la nueva frecuencia. El objeto debe de tener un índice `datetime-like` o pasar valores `datetime-like` al argumento _on_ o _level_. **IMPORTANTE**: Este método retorna un objeto {doc}`./resampler`, que tiene otros métodos como `Resampler.asfreq()` o _aggregates_ como `Resampler.mean()`.
* - [DataFrame.shift](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.shift.html)([periods, freq, axis, ...])
  - Desplaza el índice según el número deseado de períodos con una frecuencia de tiempo opcional.
* - [DataFrame.to_period](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_period.html)([freq, axis, copy])
  - Convierte el índice del `DataFrame` de `DatetimeIndex` a `PeriodIndex`.
* - [DataFrame.to_timestamp](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_timestamp.html)([freq, how, axis, copy])
  - Convierte un índice `DatetimeIndex` al comienzo del período.
* - [DataFrame.tz_convert](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.tz_convert.html)(tz[, axis, level, copy])
  - Convierte un _axis_ compatible con _tz_ en la zona horaria objetivo.
* - [DataFrame.tz_localize](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.tz_localize.html)(tz[, axis, level, ...])
  - Localiza el índice _tz-naive_ a la zona horaria de destino.
```

<br/>

### Funciones ventana, agrupar, aplicar y mapeos

Diversos métodos de operaciones como cálculo por ventanas, cálculo de agrupamientos, aplicar funciones a algún eje del `DataFrame` y mapeos. 

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
  - Provee calculos en ventanas moviles de datos. Posteriormente se puede aplicar un {ref}`método <pandas-rolling-methods>` del objeto `Rolling` o `Window`.
* - [DataFrame.transform](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.transform.html)(func[, axis])
  - Aplica una función `func` en sí mismo, retornando un objeto con las mismas dimensiones que `self`.
```

Patrones útiles:
```python
# Mapear valores de columna categórica por otra
 mapping={'cat1':'new_cat1',
            'cat2':'new_cat2',
            ...}
 df['new_cat_col']=df['cat_col'].map(mapping)

# Cálculos sobre ventana móvil
df.rolling(window).method()

# Cálculos acumulados
df['col'].expanding().sum() # Equivale a df['col'].cumsum()
```

<br/>

---
### Gráficas

Métodos para gráficar. 

:::{note}
Para usar estps métodos es necesario importar a la sesión el módulo `matplotlib.pyplot as plt`.
:::

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [DataFrame.boxplot](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.boxplot.html)([column, by, ax, ...])
  - Crea un diagrama de caja a partir de `DataFrame` columnas.
* - [DataFrame.hist](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.hist.html)([column, by, grid, ...])
  - Crea un histograma de las columnas del DataFrame.
* - [DataFrame.plot](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.html)([x, y, kind, ax, ....])
  - Función general para crear gráficas con base a los datos del ´Series´.
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

:::{tip}
Para personalizar la gráfica se puede usar la {doc}`interfaz basada en Matalab <../05-matplotlib/pyplot>` de `matplotlib`.
:::

Patrones útiles:

```python
# Líneas
df.plot(x="col1", 
           y="col2",
           kind="line")

# Diagrama de dispersión
df.plot(x="col1", 
           y="col2",
           kind="scatter")

# Histograma
df["col"].hist(bins) # df["col"].plot(kind='hist')

# BoxPlot
s.plot(kind="box") # Un boxplot por columna

# Barras
df["col"].plot(kind="bar")

# Gráficas en un mismo axes (ejm hist)
df["col1"].hist(bins, alpha)
df["col2"].hist(bins, alpha)

# Graficar todas las columnas en subplots
df.plot(subplots=True) # line por default
```

#### Notas de _plot_

`DataFrame.plot()`: Crea gráficas con base a los datos de un `DataFrame` o `Series`. Por deafult creará una gráfica por cada columna, utilizará los nombres de las mismas para crear una leyenda, utilizará la escala de las mismas para el eje _y_ y el índice para el eje _x_.
```python
# Sintaxis de llamada
DataFrame.plot(x=None, y=None, kind='line', ax=None, subplots=False, layout=None, 
               figsize=None, use_index=True, title=None, legend=None, style=None, 
               xticks=None, yticks=None, xlim=None, ylim=None, xlabel=None, ylabel=None, 
               stacked=*, secondary_y=False, ax=None, alpha=None, sort_columns=False, 
               *args, **kwargs)
```
**Parámetros:**
- **x** \- `label` o `int`: Es el nombre o el índice de la columna que irá en el eje x. Aplica en _kind_ 2 y 3.
- **y** \- `label` o `int`: Es el nombre o el índice de la columna que irá en el eje y. Aplica en _kind_ 2 y 3.
- **kind** \- `str`: es el tipo de gráfico. Otra forma de declarar la gráfica es: `X.plot.kind(*args, **kwargs)`.
    - `'bar'`: Crea una gráfica de barras verticales.
    - `'barh'`: Crea una gráfica de barras horizontales.
    - `'line'`: Crea una gráfica línea. Default.
    - `'scatter'`: Crea una diagrama de dispersión entre 2 variables.
    - `'box'`: Crea un boxplot.
    - `'hist'`: Crea un histograma.
    - `'kde'`: Crea una estimación de la densidad de un Kernel.
    - `'density'`: Crea una estimación de la densidad de un Kernel.
    - `'area'`: Crea una gráfica de un área.
    - `'pie'`: Crea una gráfica de pastel.
    - `'hexbin'`: Crea una gráfica hexbin.
- **ax** \- `Axes`: El objeto _ax_ de la figura.
- **subplots** \- `bool`: Es para indicar que haga una subgráfica por cada columna, entonces hará cada gráfica en un recuadro diferente en lugar de hacerlo en el mismo. Checar argumentos _sharex_ y _sharey_, para compartir ejes entre gráficas si `subplots=True` y _layout_ para determinar cuántas filas y columnas de gráficas usar.
- **layout** \- `2-tuple` de `int`: Filas y columnas para el layout de las subgráficas.
- **figsize** \- `tuple` de `float`: Ancho y alto de la figura en pulgadas.
- **useindex** \- `bool`: Para indicar si usar el índice como el eje _x_.
- **title** \- `str` o `list`: Es el título que tendrá la gráfica. Si es una lista y `subplots=True` es para indicar los títulos de cada subgráfica.
- **legend** \- `bool` o {'reverse'}: Mostrar una leyenda.
- **style** \- `list` o `dict`: Tipo de línea de matplotlib por columna. Es similar al parámetro _fmt_.
- **xticks**, **yticks** \- `sequence`: Valores a usar en el eje _x_ y _y_ respectivamente.
- **xlim**, **ylim** \- `2-tuple` o `2-list`: Establece los límite de los ejes _x_ y _y_ respectivamente.
- **xlabel**, **ylabel** \- `label`: Etiqueta a usar en el eje _x_ y _y_ respectivamente. Por default en `xlabel` se usan el nombre del índice o el nombre de la columna del eje _x_. En `ylabel` no se pone etiqueta por default o el nombre del eje _y_ para gráficas planas.
- **stacked** \- `bool`: Es para indicar que se apilen las barras. Aplica en 'line', 'bar' y 'area'. Por default son `False`, `False` y `True` respectivamente.
- **bins** \- `int`: Es para especificar la cantidad de barras. Aplica en 'hist'.
- **secondary_y** \- `bool` o `secuencia`: Para indicar si debe incluir un eje _y_ secundario con otra escala. Si es `sequence` poner el/los `label` de la(s) columna(s) con los valores graficar con la otra escala.
- **ax** \- `Axes`: Para indicar en cual axes agregar en caso de un _grid_ de gráficas.
- **alpha** \- `float 0, 1`: Para indicart la transperiencia de las gráficas.
- **sort_columns** \- `bool`: En caso de que `subplots=True`, es para indicar que las columnas se ordenen de manera alfabética, en lugar de manter el orden que ya tienen.
- Otros argumentos útiles (todos opcionales), consultar `help()`:
    - `sharex=True if ax is None else False` - `bool`: Indica si compartir eje _x_ entre las subgráficas.
    - `sharey=False` - `bool`: Indica si compartir eje _y_ entre las subgráficas.
    - `grid=None` - `bool`: Para indicar si mostrar una malla de líneas en la gráfica.
    - `lgx=False` - `bool` o  {'sym'}: Escala log en _x_.
    - `lgy=False` - `bool` o  {'sym'}: ' Escala log en _y_.
    - `lglg=False` - `bool`  o  {'sym'}: Escala log en _x_ y _y_.
    - `rt=None` - `int: [0, 360]`: Rotación de los ticks.
    - `fntsize=None` - `int`: Tamaño de la fuente para los ticks.
    - `clrmap=None` - `str`, `Clrmap`: Colores de la gráfica.
    - `include_bl=False` - `bool`: Indica que los valores booleanos puedan ser graficados.
    - `yerr`, `xerr` - `DataFrame`, `Series`, `array-like`, `dict`,  `str`: Para agregar _error bars_.
**Retorna:**
- `Axes` o `ndarray` de `Axes`.

<br/>

---
### Información

Métodos que retorna información sobre el `DataFrame`. 

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - [DataFrame.info](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.info.html)([verbose, buf, max_cols, ...])
  - Devuelve información del `DataFrame` como dimensiones, tipo de datos de las columnas, nombre de las columnas, memoria usada, el tipo de dato del índice, valores non-null, etc.
* - [DataFrame.memory_usage](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.memory_usage.html)([index, deep])
  - Retorna el uso de memoria de cada columna en bytes.
```

<br/>

---
### Índice

Métodos para operaciones con el `Index`, los niveles y las etiquetas del mismo en un objeto `DataFrame`. 

:::{tip}
Revisar plantilas de uso básico más abajo.
:::

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
  - Intercambia los niveles _i_ y _j_ en un `MultiIndex`.
```

Manipulaciones básicas del índice:
```python
# Establecer una columna como índice
df.set_index("col", inplace=True)

# Establecer múltiples columnas como índice
df.set_index(["col1", "col2"], inplace=True)

# Convertir el índice en un columna (establece índice numérico)
df.reset_index(inplace=True)

# Eliminar índice (establece índice numérico)
df.reset_index(drop=True, inplace=True)

# Ordenar con base al índice
df.sort_index(inplace=True)
```
- Si no se usa `inplace=True` entonces se retorna un objeto nuevo.

<br/>

### Numéricas

Métodos útiles para `Series` con datos numéricos.

#### Redondear y truncar

Métodos para redondear o truncar valores numéricos.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [DataFrame.clip](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.clip.html)([lower, upper, axis, inplace])
  - Ajusta los valores para que estén en el intervalo _[lower, upper]_ en el eje indicado.
* - [DataFrame.round](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.round.html)([decimals])
  - Redondea cada valor en un `DataFrame` al número de decimales dado.
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
  - Asignar nuevas columnas a un `DataFrame`. Útil para crear columnas nuevas que sean resultados de operaciones con otras columnas o transformación de las mismas.
* - [DataFrame.combine](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.combine.html)(other, func[, fill_value, ...])
  - Realiza una combinación por columnas con otra `DataFrame` según una función _func_.
* - [DataFrame.combine_first](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.combine_first.html)(other)
  - Actualiza los elementos nulos con valor en la misma ubicación en _other_.
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
  - Reemplaza los valores _to_replace_ con _value_.
* - [DataFrame.set_flags](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.set_flags.html)(*[, copy, ...])
  - Retorna un nuevo objeto con indicadores actualizados.
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
### Métodos avanzados

A continuación se presentan algunos métodos avanzados para manipulación de `DataFrame`.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [DataFrame.query](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.query.html)(expr, *[, inplace])
  - Sirve para aplicar comparaciones booleanas con las columnas de un DataFrame.
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

#### Notas de _sort_values_

Ordena los valores de un `DataFrame` de acuerdo a los valores de una columna o más columnas de manera ascendente o descendente.
```python
DataFrame.sort_values(by, axis=0, level=None, ascending=True, inplace=False, na_position='last', key=None)
```
**Parámetros:**
- **by** \- `str` o `list` de `str`: Nombre de la columna o lista de las columnas para ordenar.
- **axis** \- {0 o 'index', 1 o 'columns'}: Eje sobre el cual realizar la operación.
- **ascending** \- `bool` o `list-like` de `bool`: Para indicar si ordenar de manera ascedente o descendente. Si son múltiples índices se usa una lista y se empata por posición con los elementos de _by_.
- **inplace** \- `bool`: Si es `False` retornará un objeto nuevo ordenado, si es `True` sobre el mismo `DataFrame` se ordenará.
- **na_position** \- {'first', 'last'}: Para indicar dónde ubicar los valores `NaN`.
- **key** \- `function`: Una función para aplicar sobre los valores antes de ordenarlos. Debe retornar el mismo _shape_ que _by_.

Patrones útiles:
```python
# Ordenar ascendente con base a una columna 
df.sort_values("col_name")

# Ordenar descendente con base a una columna 
df.sort_values("col_name", ascending=False)

# Ordenar con base a múltiples columnas
df.sort_values(["col1_name", "col2_name"], ascending=[True, False])
```
- Si en un ordamiento de múltiples columnas se harán todas de manera ascendente no es necesario especificar el parámetro _ascending_.

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

#### Notas de _melt_

[DataFrame.melt](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.melt.html): Sirve para modificar un _pivot table_ de _wide_ a _long format_ (_unpivot_), esto es, que algunas columnas se convertirán en observaciones de una sola columna dentro de la _large table_ y los valores pasarán a ser una columna de la misma.
```python
X.melt(id_vars=None, value_vars=None, var_name=None, value_name='value')
```
**Parámetros:**
- **id_vars** - `list`, `tuple` o `ndarray`: Indica cuáles columnas categóricas se utilizarán como índice.
- **value_vars** - `list`, `tuple` o `ndarray`: Indica cuáles columnas categóricas pasarán a ser valores en una sola columna en lugar de distintas columnas. Si no se específica utiliza todas las columnas que no se pusieron en _id_vars_.
- **var_name** - `str`: Indica cuál será el nombre de la columna que contendrá los valores que antes eran nombres de columnas.
- **value_name** - `str`: Indica cuál será el nombre de la columna que contendrá los valores.

#### Notas de _pivot_table_

[DataFrame.pivot_table](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pivot_table.html): Crea una tabla en formato _wide_, similar a la que se crearía con `.groupby()`, es decir, para cada valor único de una columna categórica calcula algo sobre los valores de una columna de valores. También se puede hacer lo mismo para las combinaciones únicas de los valores de dos o más columnas categóricas y se puede hacer más de un calculo sobre las columna de valores.
```python
DataFrame.pivot_table(values=None, index=None, columns=None, aggfunc='mean', fill_value=None, margins=False, margins_name='All')
```
**Parámetros:**
- **values** \- `str` o `list` de `str`: Columnas cuyos valores se utilizarán para realizar los cálculos.
- **index** \- `str` o `list` de `str`: Columnas cuyos valores se utilizarán para agrupar en las filas. También se puede usar una `array-like`/`series` del mismo tamaño que _df_, cuyos valores se utilizarán para agrupar. Los valores se empatarán por posición con los valores de _df_.
- **columns** \- `str` o `list` de `str`: Columnas cuyos valores se utilizarán para agrupar en las columnas. También se puede usar una `array-like`/`series` del mismo tamaño que X, cuyos valores se utilizarán para agrupar. Los valores se empatarán por posición con los valores de X.
- **aggfunc** \- `function`, `list` de `function` o `dict`: Función o funciones a aplicar.
    -  `function`: Una función.
        -  Las funciones de `numpy` se pueden usar, por ejemplo `np.mean`.
        - Se puede especificar una función personaliza o una _lambda function_, pero tener en cuenta que la función debe de recibir un `Series` y retornar un escalar.
    -  `str`: El nombre de una función de agregación. Los nombres válidos son: _'sum', 'prod', 'mean', 'median', 'min', 'max', 'std', 'var', 'sem', 'count', 'nunique', 'size', 'first', 'last', 'quantile', 'mad', 'skew', 'kurt'_.
    -  `list`: Si se quiere aplicar más de una función utilizar una lista de funciones o nombres de funciones.
    -  `dict`: Se puede especificar una función específica a cada columna con un diccionario, donde las _keys_ son las etiquetas de las columnas y los _value_ son las funciones de agregación, también se puede usar un `list` de funciones como _value_ si se desea aplicar más de una función. Las columnas aquí puestas tiene que ser equivalentes a las que se ponen en el parámetro _values_. El parámetro _values_ no se define si se específica un `dict`.
- **fill_value** \- `scalar`: Es para indicar cómo rellenar los `NaN`.
- **margins** \- `bool`: Es para agregar subotales y gran toteles.
- **margins_name** \- `str`: Es el nombre de la columna cuando `margins=True`.
- **dropna** \- `bool`: Para indicar que se omitan las columnas cuyos valores son todos `NaN`.

Patrones útiles:
```python
# Pivot en dos variables, rellenando valores pérdidos y calculando margins
df.pivot_table(values="num_col", 
               index="cat_col1", 
               columns="cat_col2", 
               fill_value=0, 
               margins=True)

# Una función de agregación
df.pivot_table(values="num_col", index="cat_col", aggfunc=func)

# Mútliples funciones de agregación
df.pivot_table(values="num_col", index="cat_col", aggfunc=[func, 'func_name'])
```

**Ejemplo**:

```{code-cell} ipython3
# Definir DataFrame
long=pd.DataFrame({'col1': ['A', 'A', 'B', 'B', 'C', 'C'],
                    'col2': ['X', 'Y']*3,
                    'col3': [*range(1, 7)]})
print("DataFrame:", long, sep='\n', end='\n'*2)

# Pivot con totales
wide=long.pivot_table(values='col3', index='col1', columns='col2', aggfunc='sum', margins=True)
print("Pivot con totales:", wide, sep='\n')
```
    
<br/>

---
(pd-df-metodos-seleccion-filtrado-iteracion)=
### Selección, filtrado e iteración de elementos

Métodos útiles para seleccionar elementos con base a etiquetas, índices o condiciones o para iterar en ellos. 

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
  - Retorna un `iterable` de tuplas _(col_label, Series)_.
* - [DataFrame.iterrows](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iterrows.html)()
  - Retorna un `iterable` de tuplas  _(ind_label, Series)_.
* - [DataFrame.itertuples](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.itertuples.html)([index, name])
  - Retorna un `iterable` de `namedtuple` (de las filas). Los nombres en el `namedtuple` serán los nombres de las columnas, más aparte el nombre _Index_ (literalmente) que hará referencia a la etiqueta del índice en esa fila.
* - [DataFrame.loc](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html)()
  - Accede a un valor o un conjunto de valores dadas las etiquetas del índice o un `array-like` booleano.
* - [DataFrame.pop](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pop.html)(item)
  - Elimina y retorna una columna dada su etiqueta de columna.
* - [DataFrame.query](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.query.html)(expr, *[, inplace])
  - Sirve para aplicar comparaciones booleanas con las columnas de un DataFrame.
* - [DataFrame.select_dtypes](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.select_dtypes.html)([include, exclude])
  - Retorna un subconjunto de las columnas del DataFrame según los tipos de columna.
* - [DataFrame.tail](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.tail.html)([n])
  - Retorna las últimas _n_ filas.
* - [DataFrame.take](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.take.html)(indices[, axis])
  - Retorna los elementos en los índices posicionales dados a lo largo de un eje. Los índices se pueden repetir. Es similar a hacer _fancy indexing_ con índices implícitos.
* - [DataFrame.truncate](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.truncate.html)([before, after, axis, copy])
  - Trunca un `DataFrame` antes y después de algún valor de índice.
* - [DataFrame.xs](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.xs.html)(key[, axis, level, drop_level])
  - Retorna una sección transversal del `DataFrame`. Particurlamente útil cuando el `DataFrame` tiene un `MultiIndex` en las filas o columnas y se quiere acceder a secciones enteras de un nivel o combinaciones de los niveles/subniveles.
```

#### Notas de _query_

[DataFrame.query](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.query.html): Sirve para aplicar comparaciones booleanas con las columnas de un `DataFrame`. Se puede interpretar como una expresión `WHERE` en un _query_ de SQL.
```python
DataFrame.query(expr, inplace=False)
```
**Parámetros:**
- **expr** - `str`: Es donde se ponen las condicionales.
    - Para utilizar una variable disponible en la sesión se debe de agregar un @ antes del nombre de la variable.
    - Los nombre de las columnas se ponen tal cual en la cadena, excepto si son nombres inválidos en Python (ejm. con espacios), en ese caso se pone el nombre entre ` ` (backticks), por ejemplo 'Area (cm)^2' sería <code>'\`Area (cm)^2`'</code>.
    - Se puede hacer uso de los operadores `and` y `or` para hacer las comparaciones más complejas. Si se va a usar condicionales de cadenas, las cadenas deben de ir entre comillas dobles `" "`.
    - Se usan los operadores de comparación ordinarios.
- **inplace** - `bool`: Si es `False` retornará un `DataFrame` modificado de acuerdo al _query_, si es `True` sobre el mismo `DataFrame` aplicará el _query_.

Patrones útiles:
```python
# Comparación numérica
df.query('col >= 100')

# Uso de operadores
df.query('col1 >= 100 and col2 < 140')

# Comparación de cadenas
df.query('col == "text"')

# Columna con nombre complejo
df.query('`Area (cm)^2`' < 10)
```

<br/>

---
### Uniones

Métodos útiles para unir el `DataFrame` con otros objetos de `pandas`. 

:::{caution}
No hay ningún método para apilar `DataFrames`, consultar {ref}`Funciones de uniones y apilaciones <pandas-func-joins>`.
:::

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

#### Notas de _merge_

[DataFrame.merge](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.merge.html#pandas.DataFrame.merge): Une `DataFrames` o `Series`, de una manera similar a un _join_ en _SQL_. El `DataFrame` resultante ignora el `Index`, a menos de que éste se haya usado para el hacer el _join_.
```python
# Sintaxis de llamada
df.merge(left, right, how='inner', on=None, left_on=None, right_on=None, left_index=False, right_index=False, suffixes=('_x', '_y'), validate=None)
```

**Parámetros:**
- **right** - `DataFrame` o `Series`: Objeto con el que se hará el _join_.
- **how** - {'left', 'right', 'outer', 'inner', 'cross'}: El tipo de _join_ que se realizará.
    - `inner`: Crea una tabla donde los _ids_ de ambas tablas coinciden.
    - `left`: Con base a los _id_ de la izquierda agrega los que también están en la derecha.
    - `right`: Con base a los _id_ de la derecha agrega los que también están a la izquierda.
    - `outer`: Retorna todos los records de las tablas, haciendo los _joins_ posibles.
    - `cross`: Equivale a hacer todas las combinaciones posibles de _ids_, sin importar si coinciden o no.
- **on** - `label` o `list` de `label`: La columna o nombre del `Index` sobre las cuales se hará el join. Debe de estar en _left_ y _right_.
- **left_on**, **right_on** - `label` o `list`: Las columnas o etiquetas del `Index` sobre las cuales se hará el _join_, una para la _left_ y otra para _right_.
- **left_index**, **right_index** - `bool`: Es para indicar que se use el `Index` de la tabla _left_ y _right_ respectivamente, para hacer el _join_.
- **suffixes** - `list-like` de `str`: Es para indicar el sujifo que se agregará a cada columna, dependiendo de a cuál tabla pertenece. Solo a aquellas que tienen el mismo nombre en ambas tablas.
- **validate** - `str`: Verifica que el tipo de join haya sido de un tipo específico, como 'ono_to_one' o '1:1', 'one_to_many' o '1:m', 'many_to_one' o 'm:1' y 'many_to_many' o 'm:m'.

```python
# Hacer inner join con base a columna/índice en común
df_merged=df.merge(other_df, on='col')

# Hacer inner join con base mútiples columnas/multiIndex
df_merged=df.merge(other_df, on=['col1', 'col2', ...])

# Hacer inner join con a lon índices
df_merged=df.merge(other_df, left_index=True, right_index=True)

# Hacer inner join con base a índices
df_merged=df.merge(other_df, left_on='indName', right_on='indName')

# Hacer múltiples inner joins en columna en común
df1.merge(df2, on='col').merge(df3, on='col').merge(df4, on='col')
```
- Para cualquier otro tipo de _join_ usar el parámetro _how_.

**Ejemplo**:

```{code-cell} ipython3
# Dataset 1: Employee information
employees=pd.DataFrame({
    'employee_id': [1, 2, 3, 4, 5],
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'department': ['HR', 'Engineering', 'Engineering', 'Marketing', 'HR']
})

print("Employees Dataset:", employees, sep='\n', end='\n'*2)

# Dataset 2: Employee salaries
salaries=pd.DataFrame({
    'employee_id': [3, 4, 5, 6],
    'salary': [70000, 80000, 60000, 75000],
    'bonus': [5000, 8000, 4000, 6000]
})

print("Salaries Dataset:", salaries, sep='\n', end='\n'*2)

# Inner join en columna en común
inner_merge=employees.merge(salaries, on='employee_id', how='inner')
print("Columna en común:", inner_merge, sep='\n', end='\n'*2)

# Inner join entre dos columnas
salaries_renamed=salaries.rename(columns={'employee_id': 'id'})
diff_key_merge=employees.merge(salaries_renamed, left_on='employee_id', right_on='id', how='inner')
print("Diferentes columnas:", diff_key_merge, sep='\n', end='\n'*2)

# Inner join con base al índice
employees_indexed=employees.set_index('employee_id')
salaries_indexed=salaries.set_index('employee_id')
merged_on_index=employees_indexed.merge(salaries_indexed, left_index=True, right_index=True, how='inner')
print("Índice:", merged_on_index, sep='\n')
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

#### Notas de _drop_duplicates_

Elimina los duplicados (filas duplicadas) de un `DataFrame`.
```python
DataFrame.drop_duplicated(subset=None, keep='first', inplace=False)
```
**Parámetros:**
- **subset** \- `column label` o `secuencia` de `labels`: Es para indicar en que columnas buscar los duplicados, es decir, solo se buscan duplicados en los valores de cada fila en esas columnas.
- **keep** \- {'first', 'last', `False`}: Es para indicar cuáles valores duplicados remover, puede ser:
  - `'first'`: Para todos menos la primer aparición.
  - `'last'`: Para todos menos la última aparición.
  - `False`: Para todos.
- **inplace** \- `bool`: Si es `False` retornará un objeto nuevo con el `DataFrame` con las filas duplicadas eliminadas, si es `True` sobre el mismo `DataFrame` eliminará las filas duplicadas.

**Ejemplo**
```python
# Eliminar duplicados en una columna
df.drop_duplicates("col_name")

# Eliminar duplicados con base a múltiples columnas
df.drop_duplicates(subset=["col1_name", "col2_name", ...])
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

Patrones útiles:
```python
# Detectar valores nulos por columnas
df.isna().any()

# Contar valores nulos por columnas
df.isna().sum()

# Porcentaje de valores nulos por columnas
df.isna().mean()
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
  - Retorna un `Series` que contiene la frecuencia de cada fila distinta en el `DataFrame`. Se puede elegir un subcojunto de columas para determinar las filas únicas. Es posible además retornar la proporción con el parámetro _normalize_ y ordenar el resultado con base al recuento.
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

