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

# Index

Los objetos `Index` son un conjunto de de objetos que pueden utilizarse para identificar los elementos de los objetos `Series` y `DataFrame` por medio de etiquetas. Estos objetos pueden ser de varios tipos y con diversas características.

En esta sección se presentará el objeto `Index` y algunas de sus subclases, las subclases que no se explicarán en esta sección son las siguientes:
- [RangeIndex](https://pandas.pydata.org/docs/reference/api/pandas.RangeIndex.html#pandas.RangeIndex): Índice numérico monotono. Es similar al índice implícito por default.
- [CategoricalIndex](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.html#pandas-categoricalindex): Índice categórico.
- [IntervalIndex](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.html#pandas-intervalindex): Índice por intervalos.

<br/>

---
(index-index)=
## Index

Los objetos `Index` son un array inmutable, funje el papel de identificar por medio de etiquetas las filas y/o columnas. Pueden ser vistos como un `set` ordenado (cada elemento se identifica por un índice) o un multi-set ordenado, aunque `Index` puede tener valores repetidos. Algunas características de las listas, son:
- Es inmutable: Sus elementos no se pueden modificar una vez creado el objeto.
- Está indexado: Cada elemento está asociado con un índice y por lo tanto sus elementos están ordenados.
- Es un iterable: Se puede iterar por sus elementos y se puede usar la palabra reservada `in` para verificar memebresía.
- Permite valores duplicados.
- Sus elementos pueden ser de diferentes tipos, pero es recomendado que todos sean del mismo tipo.
- Es _hashable_, lo que quiere decir que se puede utilizar como _key_ en un diccionario.
- Soporta {ref}`index-index-operaciones` de manera similar a los `set`.

<br/>

### Creación de Index.

La forma más sencilla de crear un `Index` es con el constructor:

```{list-table}
:header-rows: 1

* - Constructor
  - Descripción
* - [Index](https://pandas.pydata.org/docs/reference/api/pandas.Index.html#pandas.Index)(data=None, dtype=None, copy=False, name=None, tupleize_cols=True)
  - Secuencia inmutable para selección de elementos y alineación con con otros objetos.
```
- _data_ - `array-like`, `iterable`: Un arreglo o una lista unidimensional con los datos.

**Ejemplo**:

```{code-cell} ipython3
# Importar librería
import pandas as pd

# Crear objeto ind
ind = pd.Index(["a", "b", "c"])

# Imprimir contenido de ind
print(ind)
```

<br/>

---
(index-index-seleccion)=
### Selección de elementos

Para seleccionar elementos se pueden usar las mismas estrategias que la {ref}`selección de elementos <numpy-arrays-seleccion>` de arrays unidimensionales de `numpy`:
- {ref}`numpy-arrays-indexing`.
- {ref}`numpy-arrays-slicing`.
- {ref}`numpy-arrays-masking`.
- {ref}`numpy-arrays-fancy-indexing`.

**Ejemplos**: A continuación se verán algunos ejemplos utilizando las distintas estrategias enlistadas anteriormente.

```{code-cell} ipython3
# Crear objeto ind
ind = pd.Index(["a", "e", "i", "o", "u"])

# Seleccionar haciendo Indexing -> "i"
print(f"Indexing: {ind[2]}", end = "\n"*2)  

# Seleccionar haciendo slicing -> ["a", "i", "u"]
print(f"Slicing: {ind[::2]}", end = "\n"*2)  

# Seleccionar haciendo boolean masking -> ["i", "o"]
print(f"Boolean masking: {ind[ind.isin(['i', 'o'])]}", end = "\n"*2)  

# Seleccionar haciendo fancy indexing -> ["o", "a", "u"]
print(f"Fancy indexing: {ind[[3, 0, 4]]}", end = "\n"*2)
```

<br/>

---
(index-index-operaciones)=
### Operaciones de conjuntos

Los objetos `Index` son similares a un `set`, por lo tanto se pueden realizar operaciones de conjuntos entre objetos `Index` con métodos de {ref}`Operaciones de conjuntos <index-index-metodos-conjuntos>`.

- **Unión**: Para determinar la unión de dos `Index` se usa el método `.union`: <br/> `X.union(Y)`
- **Intersección**: Para determinar la intersección (elementos en común) de dos `Index` se usa el método `.intersection`: <br/> `X.intersection(Y)`
- **Diferencia**: Para determinar la diferencia de dos `Index` (elementos en _X_ pero no en _Y_) se usa el método `.difference(Y)`: <br/> `X.difference(Y)`
- **Diferencia simétrica**: Para determinar la diferencia simétrica de dos `Index` (elementos en _X_ o _Y_, pero no en ambos) se usa el método `.symmetric_difference(Y)`: <br/> `X.symmetric_difference(Y)`

:::{warning}
No se pueden usar los operadores _bitwise_ `|`, `&`, `-`, etc. para realizar operaciones de conjuntos entre objetos `Index`.
:::

**Ejemplos**: A continuación se verán unos ejemplos del uso de los métodos para realizar operaciones de conjuntos entre objetos de tipo `Index`.

```{code-cell} ipython3
# Crear ind1
ind1 = pd.Index(["a", "e", "i", "o", "u"])

# Crear ind2
ind2 = pd.Index(["a", "b", "c", "d", "e"])

# Calcular la unión -> ["a", "b", "c", "d", "e", "i", "o", "u"]
print("Union: ", ind1.union(ind2))

# Calcular la intersección -> ['a', 'e']
print("Intesección: ", ind1.intersection(ind2))

# Calcular la diferencia -> ["i", "o", "u"]
print("Diferencia: ", ind1.difference(ind2))
```

<br/>

---
### Atributos de _Index_

En esta sección se enlistan los atributos del objeto `Index`.

#### Atributos generales

Atributos generales del objeto `Index`.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [Index.dtype](http://pandas.pydata.org/docs/reference/api/pandas.Index.dtype.html)
  - Retorna el `dtype` de los datos subyacentes.
* - [Index.name](http://pandas.pydata.org/docs/reference/api/pandas.Index.name.html)
  - Retorna el nombre del objeto `Index` o `MultiIndex`. También se puede usar para modificar el nombre.
* - [Index.names](http://pandas.pydata.org/docs/reference/api/pandas.Index.names.html)
  - Retorna los nombres de los niveles de un índice. También se puede usar para modificar o agregar nombres a los niveles de un índice.
* - [Index.ndim](http://pandas.pydata.org/docs/reference/api/pandas.Index.ndim.html)
  - Número de dimensiones de los datos subyacentes, por definición 1.
* - [Index.shape](http://pandas.pydata.org/docs/reference/api/pandas.Index.shape.html)
  - Retorna un `tuple` del _shape_ de los datos subyacentes.
* - [Index.size](http://pandas.pydata.org/docs/reference/api/pandas.Index.size.html)
  - Retorna el número total de elementos de los datos subyacentes.
* - [Index.T](http://pandas.pydata.org/docs/reference/api/pandas.Index.t.html)
  - Retorna la transpuesta, que por definición es _self_.
* - [Index.values](http://pandas.pydata.org/docs/reference/api/pandas.Index.values.html)
  - Devuelve un arreglo con los valores del `Index`.
```

<br/>

#### Información

Atributos que indican si el `Index` cumple determinadas características.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [Index.empty](http://pandas.pydata.org/docs/reference/api/pandas.Index.empty.html)
  - Indica si el índice está vacío.
* - [Index.has_duplicates](http://pandas.pydata.org/docs/reference/api/pandas.Index.has_duplicates.html)
  - Verifica si el `Index` tiene valores duplicados.
* - [Index.hasnans](http://pandas.pydata.org/docs/reference/api/pandas.Index.hasnans.html)
  - Retorna `True` si hay algun valor `NaN`.
* - [Index.is_monotonic_decreasing](http://pandas.pydata.org/docs/reference/api/pandas.Index.is_monotonic_decreasing.html)
  - Retorna `bool` indicando si los valores son iguales o decrecientes.
* - [Index.is_monotonic_increasing](http://pandas.pydata.org/docs/reference/api/pandas.Index.is_monotonic_increasing.html)
  - Retorna `bool` indicando si los valores son iguales o crecientes.
* - [Index.is_unique](http://pandas.pydata.org/docs/reference/api/pandas.Index.is_unique.html)
  - Indica si el índice tiene solo valores únicos.
```

<br/>

---
### Métodos de _Index_

En esta sección se enlistan los métodos del objeto `Index` por categorías.

#### Cálculos y operadores

##### Comparaciones

Métodos para comparar objetos `Index`.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [Index.equals](http://pandas.pydata.org/docs/reference/api/pandas.Index.equals.html)(other)
  - Determina si dos objetos `Index` objeto son iguales.
* - [Index.identical](http://pandas.pydata.org/docs/reference/api/pandas.Index.identical.html)(other)
  - Similar a `Index.equals()`, pero verifica que los atributos y tipos de objetos también sean iguales.
```

<br/>

##### Membresía

Métodos para verificar que los elementos del objeto `Index` estén dentro de un conjunto de valores.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [Index.isin](http://pandas.pydata.org/docs/reference/api/pandas.Index.isin.html)(values[, level])
  - Devuelve un arreglo booleano que indica si los valores del índice están en _values_.
```

<br/>

##### Mínimos y máximos

Métodos para determinar elementos máximos y mínimos en el objeto `Index`.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [Index.argmax](http://pandas.pydata.org/docs/reference/api/pandas.Index.argmax.html)([axis, skipna])
  - Retorna la posición `int` del valor máximo en el `Index`.
* - [Index.argmin](http://pandas.pydata.org/docs/reference/api/pandas.Index.argmin.html)([axis, skipna])
  - Retorna la posición `int` del valor mínimo en el `Index`.
* - [Index.max](http://pandas.pydata.org/docs/reference/api/pandas.Index.max.html)([axis, skipna])
  - Retorna el valor máximo de `Index`.
* - [Index.min](http://pandas.pydata.org/docs/reference/api/pandas.Index.min.html)([axis, skipna])
  - Retorna el valor mínimo de `Index`.
```

<br/>

(index-index-metodos-conjuntos)=
##### Operaciones de conjuntos

Métodos para realizar operaciones de conjuntos entre objetos `Index`. 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [Index.difference](http://pandas.pydata.org/docs/reference/api/pandas.Index.difference.html)(other[, sort])
  - Retorna un nuevo `Index` con los elementos del índice que no están en _other_.
* - [Index.intersection](http://pandas.pydata.org/docs/reference/api/pandas.Index.intersection.html)(other[, sort])
  - Retorna la intersección de dos objetos `Index`, es decir, los elementos en común.
* - [Index.symmetric_difference](http://pandas.pydata.org/docs/reference/api/pandas.Index.symmetric_difference.html)(other[, ...])
  - Calcula la diferencia simétrica de dos objetos `Index`, es decir, los elementos que están en alguno de los objetos, pero no en ambos.
* - [Index.union](http://pandas.pydata.org/docs/reference/api/pandas.Index.union.html)(other[, sort])
  - Retorna la unión de dos objetos `Index`, es decir, un índice nuevo con todos los elementos de ambos objetos.
```

<br/>

##### Operadores booleanos

Métodos para trabajar con objetos `Index` boolenos.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [Index.all](http://pandas.pydata.org/docs/reference/api/pandas.Index.all.html)(*args, **kwargs)
  - Retorna `True` si todos los elementos son `True`.
* - [Index.any](http://pandas.pydata.org/docs/reference/api/pandas.Index.any.html)(*args, **kwargs)
  - Retorna `True` si al menos un elemento es `True`.
```

<br/>

#### Compatibilidad Con MultiIndex

Métodos compatibles con objetos `Index` anidados, es decir, que tienen más de una nivel similar a los objetos `MultiIndex`. 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [Index.droplevel](http://pandas.pydata.org/docs/reference/api/pandas.Index.droplevel.html)([level])
  - Elimina un nivel de un índice multinivel.
* - [Index.set_names](http://pandas.pydata.org/docs/reference/api/pandas.Index.set_names.html)(names, *[, level, inplace])
  - Establece el nombre de un objeto `Index` o los nombres de los niveles de un objeto `MultiIndex`.
```

<br/>

#### Conversión, transformaciones y _views_

Métodos para convertir el objeto `Index` a otro tipo o convertir sus valores a otro tipo. 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [Index.astype](http://pandas.pydata.org/docs/reference/api/pandas.Index.astype.html)(dtype[, copy])
  - Crea un `Index` con los valores convertidos al tipo de dato _dtype_.
* - [Index.copy](http://pandas.pydata.org/docs/reference/api/pandas.Index.copy.html)([name, deep])
  - Crea una copia del objeto.
* - [Index.ravel](http://pandas.pydata.org/docs/reference/api/pandas.Index.ravel.html)([order])
  - Retorna una _view_ del índice.
* - [Index.to_frame](http://pandas.pydata.org/docs/reference/api/pandas.Index.to_frame.html)([index, name])
  - Convierte el `Index` a un `DataFrame` con una columna que contiene los valores del índice.
* - [Index.to_list](http://pandas.pydata.org/docs/reference/api/pandas.Index.to_list.html)()
  - Retorna un `list` de los valores.
* - [Index.to_series](http://pandas.pydata.org/docs/reference/api/pandas.Index.to_series.html)([index, name])
  - Convierte el `Index` a `Series`
```

<br/>

#### Modificaciones

Métodos para realizar modificaciones en el objeto `Index` como eliminar elementos, modificar elementos, renombrar, categorizar, mapear, etc.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [Index.delete](http://pandas.pydata.org/docs/reference/api/pandas.Index.delete.html)(loc)
  - Retorna un nuevo `Index` con los elementos en las posiciones indicadas eliminados.
* - [Index.drop](http://pandas.pydata.org/docs/reference/api/pandas.Index.drop.html)(labels[, errors])
  - Retorna un nuevo `Index` con los elementos con las etiquetas indicadas eliminados.
* - [Index.factorize](http://pandas.pydata.org/docs/reference/api/pandas.Index.factorize.html)([sort, use_na_sentinel])
  - Codifica el objeto como un tipo enumerado o una variable categórica. Básicamente a cada elemento único le asigna un valor numérico: `['b', 'b', 'a', 'c', 'b'] -> [0, 0, 1, 2, 0]`
* - [Index.insert](http://pandas.pydata.org/docs/reference/api/pandas.Index.insert.html)(loc, item)
  - Retorna el `Index` con un nuevo elemento insertado en la ubicación indicada.
* - [Index.map](http://pandas.pydata.org/docs/reference/api/pandas.Index.map.html)(mapper[, na_action])
  - Mapea valores de acuerdo una correspondencia de entrada, es decir, asigna valores dependiendo de los valores de entrada con base a una función u otro objeto.
* - [Index.reindex](http://pandas.pydata.org/docs/reference/api/pandas.Index.reindex.html)(target[, method, level, ...])
  - Crea un nuevo objeto `Index` con base a otro seleccionando únicamente algunos elementos determinados. Retorna también un `ndarray` con los índices de los elementos elegidos.
* - [Index.rename](http://pandas.pydata.org/docs/reference/api/pandas.Index.rename.html)(name, *[, inplace])
  - Modifica el nombre de un objeto `Index` o `MultiIndex`.
* - [Index.repeat](http://pandas.pydata.org/docs/reference/api/pandas.Index.repeat.html)(repeats[, axis])
  - Repite elementos de un objeto `Index`.
* - [Index.putmask](http://pandas.pydata.org/docs/reference/api/pandas.Index.putmask.html)(mask, value)
  - Retorna un nuevo `Index` modificando los valores de acuerdo a un array booleano, aquellos cuyos valores sea `True` se modificarán. _value_ puede ser otro índice.
* - [Index.where](http://pandas.pydata.org/docs/reference/api/pandas.Index.where.html)(cond[, other])
  - Reemplaza valores donde la condición es `False`.
```

<br/>

#### Operaciones de tiempo

Métodos útiles para índices de tipo `datetime-like`. 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [Index.shift](http://pandas.pydata.org/docs/reference/api/pandas.Index.shift.html)([periods, freq])
  - Modifica el índice según el número deseado de incrementos de frecuencia de tiempo.
```

<br/>

#### Selección de elementos

Métodos para seleccionar elementos en el objeto `Index`. 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [Index.asof](http://pandas.pydata.org/docs/reference/api/pandas.Index.asof.html)(label)
  - Retorna una etiqueta determinada en el índice o, si no está presente, la inmediata anterior.
* - [Index.asof_locs](http://pandas.pydata.org/docs/reference/api/pandas.Index.asof_locs.html)(where, mask)
  - Retorna las posiciones (índices) de unas etiquetas determinadas en el índice.
* - [Index.get_indexer](http://pandas.pydata.org/docs/reference/api/pandas.Index.get_indexer.html)(target[, method, limit, ...])
  - Retorna un _indexador_ dado el índice actual y un nuevo índice. El _indexador_ es un arreglo que indica las posiciones de los valores en un nuevo índice _target_ dadas las posiciones actuales de los mismos valores en el índice actual. Si un valor en _target_ no existe en el índice actual se le asigna la posición -1.
* - [Index.get_indexer_for](http://pandas.pydata.org/docs/reference/api/pandas.Index.get_indexer_for.html)(target)
  - Garantiza el retorno de un _indexador_ incluso cuando los valores en el índice actual no son únicos. El _indexador_ es un arreglo que indica las posiciones de los valores en un nuevo índice _target_ dadas las posiciones actuales de los mismos valores en el índice actual. Para un valor no único dado retorna todas las posiciones en el índice actual.
* - [Index.get_indexer_non_unique](http://pandas.pydata.org/docs/reference/api/pandas.Index.get_indexer_non_unique.html)(target)
  - Retorna un _indexador_ incluso cuando los valores en el índice actual no son únicos. El _indexador_ es un arreglo que indica las posiciones de los valores en un nuevo índice _target_ dadas las posiciones actuales de los mismos valores en el índice actual. Para un valor no único dado retorna todas las posiciones en el índice actual.
* - [Index.get_level_values](http://pandas.pydata.org/docs/reference/api/pandas.Index.get_level_values.html)(level)
  - Retorna un `Index` de valores para el nivel solicitado.
* - [Index.get_loc](http://pandas.pydata.org/docs/reference/api/pandas.Index.get_loc.html)(key)
  - Recupera la posición, el segmento o la máscara booleana para la etiqueta solicitada.
* - [Index.get_slice_bound](http://pandas.pydata.org/docs/reference/api/pandas.Index.get_slice_bound.html)(label, side)
  - Calcula el límite del segmento que corresponde a la etiqueta dada.
* - [Index.item](http://pandas.pydata.org/docs/reference/api/pandas.Index.item.html)()
  - Retorna el primer elemento de los datos subyacentes como un escalar de Python.
* - [Index.slice_indexer](http://pandas.pydata.org/docs/reference/api/pandas.Index.slice_indexer.html)([start, end, step])
  - Retorna un _slice_ con las posiciones de los parámetros _start_, _end_ y _stop_ en el `Index`, el cual debe de ser único y estar ordenado. Retorna `slice`.
* - [Index.slice_locs](http://pandas.pydata.org/docs/reference/api/pandas.Index.slice_locs.html)([start, end, step])
  - Retorna un `tuple` con las posiciones de los parámetros _start_, _end_ y _stop_ en el `Index`, el cual debe de ser único y estar ordenado. Retorna `slice`.
* - [Index.where](http://pandas.pydata.org/docs/reference/api/pandas.Index.where.html)(cond[, other])
  - Reemplaza valores donde la condición es `False`.
```

<br/>

#### Ordenar

Métodos para ordenar el `Index`.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [Index.argsort](http://pandas.pydata.org/docs/reference/api/pandas.Index.argsort.html)(*args, **kwargs)
  - Retorna los índices enteros que ordenarían el índice.
* - [Index.searchsorted](http://pandas.pydata.org/docs/reference/api/pandas.Index.searchsorted.html)(value[, side, sorter])
  - Determina los índices donde se deben insertar elementos para mantener el orden, bajo el supuesto de que el `Index` está ordenado. En caso de múltiples valores, los índices se determinan solo con respecto al `Index` original.
* - [Index.sort_values](http://pandas.pydata.org/docs/reference/api/pandas.Index.sort_values.html)(*[, return_indexer, ...])
  - Retorna una copia ordenada del índice.
```

<br/>

#### Uniones y combinaciones

Métodos para unir y combinar objetos `Index`. 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [Index.append](http://pandas.pydata.org/docs/reference/api/pandas.Index.append.html)(other)
  - Retorna un nuevo `Index` que es la concatenación de un índice con otro.
* - [Index.join](http://pandas.pydata.org/docs/reference/api/pandas.Index.join.html)(other, *[, how, level, ...])
  - Retorna un nuevo `Index` que es el resultado de aplicar un _join_ con base a dos índices. Solo retorna los índices que satisfacen el tipo de unión.
```

<br/>

#### Valores duplicados

Métodos para trabajar con valores duplicados en el `Index`.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [Index.drop_duplicates](http://pandas.pydata.org/docs/reference/api/pandas.Index.drop_duplicates.html)(*[, keep])
  - Retorna el `Index` con los valores duplicados eliminados.
* - [Index.duplicated](http://pandas.pydata.org/docs/reference/api/pandas.Index.duplicated.html)([keep])
  - Retorna un array booleano indicado para cada valor si está duplicado (`True`) o no (`False`).
```

<br/>

#### Valores pérdidos

Métodos para trabajar con valores perdidos `NA`/`NaN` en el `Index`.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [Index.dropna](http://pandas.pydata.org/docs/reference/api/pandas.Index.dropna.html)([how])
  - Retorna el `Index` sin valores `NA`/`NaN`.
* - [Index.fillna](http://pandas.pydata.org/docs/reference/api/pandas.Index.fillna.html)([value, downcast])
  - Reemplaza los valores `NA`/`NaN` con un valor especificado.
* - [Index.isna](http://pandas.pydata.org/docs/reference/api/pandas.Index.isna.html)()
  - Retorna un array boolenado indicando para cada elemento si es `NA`/`NaN`.
* - [Index.notna](http://pandas.pydata.org/docs/reference/api/pandas.Index.notna.html)()
  - Retorna un array boolenado indicando para cada elemento si no es `NA`/`NaN`.
```

<br/>

#### Valores únicos

Métodos para trabajar con valores únicos en el `Index`.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [Index.nunique](http://pandas.pydata.org/docs/reference/api/pandas.Index.nunique.html)([dropna])
  - Retorna el número de elementos únicos en el objeto.
* - [Index.unique](http://pandas.pydata.org/docs/reference/api/pandas.Index.unique.html)([level])
  - Retorna los valores únicos en el índice.
* - [Index.value_counts](http://pandas.pydata.org/docs/reference/api/pandas.Index.value_counts.html)([normalize, sort, ...])
  - Retorna un `Series` que contiene recuentos de valores únicos.
```

<br/><br/>

---
## MultiIndex

La clase `MultiIndex` es una subclase de `Index`, es un multiset ordenado, que permite tener índices jearquizados por niveles. Esta clase es una alternativa para crear objetos de más de dos dimensiones. Algunas características de las listas, son:
- Es inmutable: Sus elementos no se pueden modificar una vez creado el objeto.
- Está indexado: Cada elemento está asociado con un índice y por lo tanto sus elementos están ordenados.
- Es un iterable: Se puede iterar por sus elementos y se puede usar la palabra reservada `in` para verificar memebresía.
- Permite valores duplicados.

<br/>

### Creación de un _MultiIndex_

La clase `MultiIndex` tiene varios {ref}`index-multiindex-metodos-constructores` para crear un multi-índice a partir de secuencias anidadas, productos cartesianos, objetos `DataFrame`, entre otros.

**Ejemplos**: En este ejemplo se revisar el uso de los constructores `pd.MultiIndex.from_arrays()` y `pd.MultiIndex.from_product()`.
```{code-cell} ipython3
# Crear MultiIndex desde un secuencia anidada
arrays = [[1, 1, 2, 2], ['red', 'blue', 'red', 'blue']]

multind1 = pd.MultiIndex.from_arrays(arrays, names=('number', 'color'))
print(f"Multiíndice desde secuencias:\n{multind1}", end="\n"*2)

# Crear MultiIndex desde un producto cartesiano
numbers = [0, 1, 2]

colors = ['green', 'purple']

multind2 = pd.MultiIndex.from_product([numbers, colors], names=['number', 'color'])
print(f"Multiíndice desde producto cartesiano:\n{multind2}")
```
- En el caso de `.from_arrays()`, se proporciona un `array-like` anidado, cada `array-like` interior debe de ser del mismo tamaño. El número de secuencias interiores determina el número de niveles en el multi-índice y los elementos se empatan por posición.
- En el caso de `.from_product()` se proporciona un `array-like` anidado cuyos `array-like` interiores pueden diferir en longitud. El número de secuencias interiores determina el número de niveles en el multi-índice y los elementos serán el producto cartesiano de los `array-like` interiores.

```{note}
Los multi-índice creados con los constructores se pueden usar como argumentos de los parámetros `index` y `columns` al momento de crear un objeto de `pandas` o al cambiar el índice de un objeto existente con el método `.reindex()`.
```

<br/>

#### Objetos con _MultiIndex_

Otra alternativa para crear un multi-índice directamente en un objeto como en `Series` o `DataFrame` es definiendo el parámetro utilizando alguna de las siguientes estategias:
- Pasando al parámetro `index` alguna secuencia anidada. Cada secuencia interior debe de ser del mismo tamaño y tener el mismo número de filas que el objeto. El número de secuencias interiores determina el número de niveles en el multiíndice y los elementos se empatan por posición. Básicamente funciona igual que `pd.MultiIndex.from_arrays()`.
- Al momento de crear un objeto, en el parámetros `data` usar como argumento un `dict` con _keys_ que sean `tuple`, todos los _tuple_ deben de tener el mismo número de elementos y cada elemento de cada <tuple> será un nivel en el índice.
- Se pueden convertir columnas actuales de un `DataFrame` en un multi-índice con el método `.set_index()`.

**Ejemplos**: En los siguientes ejemplos se revisan las estrategias de secuencias anidadas y de diccionarios con _keys_ de `tuple`:
```{code-cell} ipython3
# Crear multiindex desde un secuencia anidada
nested_sequence = [[1, 1, 2, 2], ['red', 'blue', 'red', 'blue']]

# Inicializar objeto
s1 = pd.Series([10, 11, 12, 13], index=nested_sequence)
print(f"Multiíndice desde secuencias:\n{s1}", end="\n"*2)

# Definir diccioanrio
data = {
    ('A', 'X'): 1,
    ('A', 'Y'): 2,
    ('B', 'X'): 3,
    ('B', 'Y'): 4
}

# Inicializar objeto
s2 = pd.Series(data)
print(f"Multiíndice desde dict de tuples:\n{s2}")
```

:::{caution}
Notar que con el método anterior el objeto retornado es de tipo `Index` y no `MultiIndex`.
:::

<br/>

---
### Seleccion elementos de _MultiIndex_

:::{warning}
En esta sección se explica cómo seleccionar elementos en objetos con índices de tipo `MultiIndex`. Los métodos aquí explicados **no** se aplican directamente sobre objetos `MultiIndex`. Para seleccionar elementos directamente en un objeto `MultiIndex` ver {ref}`index-index-seleccion`, pero en esencia se pueden aplicar las mismas estrategias para seleccionar elementos que en un `ndarray` unidimensional y cuyos elementos son objetos de tipo `tuple`.
:::

#### _Series_

Selección de elementos en un `Series` con `MultiIndex`.

- **Indexing**: Selección de elementos específicos o niveles completos.
    - **Elementos específicos**: Para seleccionar elementos específicos se puede separar las etiquetas de cada nivel con comas o usar un `tuple` con las etiquetas de cada nivel, aplica lo mismo con el método `.loc()`. <br/> `X['label1', 'label2', ...]` <br/> `X[('label1', 'label2', ...)]` <br/> `X.loc['label1', 'label2', ...]` <br/> `X.loc[('label1', 'label2', ...)]`
    - **Niveles completos superiores**: Se puede seleccionar una etiqueta de un nivel superior o una serie de etiquetas en niveles superiores y mostrar todos los elementos en los niveles inferiores, simplemente indicar la etiqueta o las etiquetas, respetando la jerarquía de los niveles, se puede usar corchetes o el método `.loc()`: <br/> `X['label1'] # Primer nivel` <br/> `X[('label1', 'label2')] # Segundo nivel` <br/> `...`
- **Slicing**: Para seleccionar _slices_ de los elementos, indicando el inicio, fin y paso (`start:stop:step`). Al usar las etiquetas de los elementos, entonces ambos extremos del _slice_ son inclusivos. **Importante**: Los elementos del índice deben estar ordenados para que funcione correctamente.
    - **Slicing en niveles superiores**: Se puede aplicar slicing en todos los niveles o solo algunos superiores y mostrar todos los elementos en los niveles inferiores. Se puede usar corchetes o el método `.loc()`, no usar `tuple`: <br/> `X['label1i':'label1:j', 'label2i':'label2j', ...]`
    - **Omitir niveles**: Se pueden omitir niveles (mostrar todas las etiquetas en ese nivel) usando `:`: <br/> `X[:, 'label2i':'label2j'] # Todo primer nivel y slice en segundo nivel` <br/> `...`
    - **Niveles inferiores completos**: Se puede combinar _slicing_ y _Indexing_ para seleccionar todas las etiquetas en niveles inferiores, independientemente de los niveles superiores: <br/> `X[:, 'label2'] # Todas los label2` <br/> `X[:, :, 'label3'] # Todas los label3` <br/> `...`
- **Fancy indexing**: Seleccionar un conjunto de elementos en posiciones específicas. Se usa una lista en cada nivel con los _labels_ a seleccionar en cualquier orden e incluso se pueden repetir. Se puede definir como `tuple` o separado por comas y con corchetes o con el método `.loc()`. <br/> `X[['label1i', 'label1j', ...], ['label2i', 'label2j', ...], ...]` <br/> `X[(['label1i', 'label1j', ...], ['label2i', 'label2j', ...], ...)]` <br/> `X[[('label1i', 'label1j', ...), ('label2i', 'label2j', ...), ...]]` <br/> `X.loc[(['label1i', 'label1j', ...], ['label2i', 'label2j', ...], ...)]`
- **Boolean masking**: En _boolean masking_ es indiferente si el índice es un multi-índice. Se debe usar un _array booleano_ del mismo tamaño que el `Series`.

:::{tip}
Se pueden combinar distintas estrategias de selección para diferentes niveles.
:::

**Ejemplos**
```{code-cell} ipython3
# Crear Series con multi-índice
s = pd.Series([*'abcdef'], index = multind2)

# Imprimir objeto:
print(f"Series:\n{s}", end='\n'*2)

# Indexing: Elemento específico
print("Elemento específico:", s[(0, 'purple')], sep='\n', end='\n'*2)

# Indexing: Elemento de nivel superior
print("Elemento de nivel superior:", s[1], sep='\n', end='\n'*2)

# Slicing: Nivel superior
print("Slicing:", s.loc[1:], sep='\n', end='\n'*2)

# Fancy indexing
print("Fancy indexing:", s.loc[([0, 2], ['purple'])], sep='\n', end='\n'*2)

# Combinación de estrategias
print("Todos los green:", s[:, 'green'], sep='\n')
```

#### _DataFrame_

Selección de elementos en un `DataFrame` con `MultiIndex`. En esta sección se estará usando el método `.loc()`. 
- **Indexing**: Se puede específicar los niveles en orden, opcionalmente omitiendo niveles más profundos y mostrando todos los niveles restantes. Se puede aplicar tanto en el índice, columnas o ambos: <br/> `X.loc[(ind1, ind2, ...), (col1, col2, ...)] # Ambos ejes` <br/> `X.loc[(ind1, ind2, ...), :] # Solo filas` <br/> `X.loc[:, (col1, col2, ...)] # Solo columnas`
- **Slicing**: Se puede aplicar _slicing_ para seleccionar _slices_ de los datos, indicando el inicio, fin y paso (`start:stop:step`). Se usa un `tuple` para `start`, `stop` y `step`, los elementos son _labels_ de los niveles en orden, opcionalmente se pueden omitir niveles más profundo y mostrar todos los niveles restantes. Se puede aplicar tanto en el índice, columnas o ambos. **Importante**: Los elementos del índice deben estar ordenados para que funcione correctamente. <br/> `X.loc[(ind1_i, ind2_i, ...):(ind1_j, ind2_j, ...), (col1_i, col2_i, ...):(col1_j, col2_j, ...)] # Ambos ejes` <br/> `X.loc[(ind1_i, ind2_i, ...):(ind1_j, ind2_j, ...), :] # Solo filas` <br/> `X.loc[:, (col1_i, col2_i, ...):(col1_j, col2_j, ...)] # Solo columnas`
- **Fancy indexing**: Se puede aplicar _fancy indexing_ para seleccionar un conjunto de elementos en posiciones específicas. Se usa una lista para cada nivel indicando los _labels_ a seleccionar en cualquier orden e incluso se pueden repetir. Los niveles se especifican en orden, opcionalmente omitiendo niveles más profundo y mostrando todos los niveles restantes. Se puede aplicar tanto en el índice, columnas o ambos. <br/> `X.loc[([ind1_i, ind1_j, ...], [ind2_i, ind2_j, ...], ...), ([col1_i, col1_j, ...], [col2_i, col2_j, ...], ...)] # Ambos ejes` <br/> `X.loc[([ind1_i, ind1_j, ...], [ind2_i, ind2_j, ...], ...), :] # Solo filas` <br/> `X.loc[:, ([col1_i, col1_j, ...], [col2_i, col2_j, ...], ...)] # Solo columnas`
- **Boolean masking**: En _boolean masking_ es indiferente si el índice o las columnas son multi-índice. Se debe usar un _array booleano_ del mismo tamaño que el número de elementos en el índice o las columnas, según sea el caso.
- **Niveles internos**: Para seleccionar valores específicos de niveles internos para todos los niveles superiores es necesario usar `pd.IndexSlice`. Se puede aplicar tanto en el índice, columnas o ambos. <br/> `X.loc[pd.IndexSlice[:, ..., ind], pd.IndexSlice[:, ..., col]] # Ambos ejes` <br/> `X.loc[pd.IndexSlice[:, ..., ind], :] # Solo filas` <br/> `X.loc[:, pd.IndexSlice[:, ..., col]] # Solo columnas`


:::{tip}
Se pueden combinar distintas estrategias de selección para diferentes niveles y para diferentes ejes.
:::

**Ejemplos**:

```{code-cell} ipython3
# Definir los datos
data = [[1, 2, 3, 4],
   [4, 5, 6, 7],
   [7, 8, 9, 10],
   [10, 11, 12, 13],
   [14, 15, 16, 17],
   [18, 19, 20, 21]]

# Crear índices de filas y columnas
index = pd.MultiIndex.from_tuples([('row1', 'a'), ('row1', 'b'), ('row2', 'c'), ('row2', 'd'), ('row3', 'e'), ('row3', 'f')], names=['Level_1', 'Level_2'])
columns = pd.MultiIndex.from_tuples([('Group_A', 'X'), ('Group_A', 'Y'), ('Group_B', 'X'), ('Group_B', 'Y')], names=['Group', 'Variable'])

# Crear DataFrame
df_mul = pd.DataFrame(data, index=index, columns=columns)
print(df_mul, sep='\n', end='\n'*2)

# Indexing: Elemento específico
print("Elemento específico:", df_mul.loc[('row2', 'd'), ('Group_B', 'X')], sep='\n', end='\n'*2)

# Slicing
print("Slicing:", df_mul.loc[('row1'):('row2'), :], sep='\n', end='\n'*2)

# Fancy indexing
print("Fancy indexing:", df_mul.loc[(['row1', 'row3']), (['Group_A'])], sep='\n', end='\n'*2)

# Niveles internos
print("Todas las X:", df_mul.loc[:, pd.IndexSlice[:, 'X']], sep='\n')
```

<br/>

---
### Renombrar niveles

Para asignar o renombrar los niveles de un objeto con `MultiIndex` se puede hacer uso del atributo `.names` y asignarlo a un `list-like` con la misma cantidad que el número de niveles en el objeto.

```python
# Asignar nombres
obj.names = ['level_name1', 'level_name2', ...]
```
- También se pueden asignar los nombres con el parámetro _names_ de cualquier constructor del multi-índice.

<br/>

---
### Conversiones entre objetos con _MultiIndex_

A continuación se presentará de manera breve algunos métodos para realizar conversiones entre objetos con un `MultiIndex`:
- **Convertir niveles del índice a niveles de columnas**: Para pasar niveles del índice de las filas a niveles de las columnas usar los métodos [Series.unstack()](http://pandas.pydata.org/docs/reference/api/pandas.Series.unstack.html) o [DataFrame.unstack()](http://pandas.pydata.org/docs/reference/api/pandas.DataFrame.unstack.html).
- **Convertir niveles de columnas a niveles de filas**: Para convertir un nivel o varios niveles de las columnas de un `DataFrame` a niveles de las filas usar el método [DataFrame.stack()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.stack.html).
- **Convertir niveles del índice en columnas**: Uno o varios niveles se pueden convertir en columnas con el método [Series.reset_index()](http://pandas.pydata.org/docs/reference/api/pandas.Series.reset_index.html) o [DataFrame.reset_index()](http://pandas.pydata.org/docs/reference/api/pandas.DataFrame.reset_index.html).
- **Convertir columnas en niveles del índice**: Una o varias columnas se pueden convertir en niveles del índice de las filas con el método [DataFrame.set_index()](http://pandas.pydata.org/docs/reference/api/pandas.DataFrame.set_index.html).

---
### Atributos de _MultiIndex_

Atributos de los objetos `MultiIndex`. 

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción

* - [MultiIndex.dtypes](http://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.dtypes.html)
  - Retorna los tipos de datos como `Series` del objeto `MultiIndex`.
* - [MultiIndex.levels](http://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.levels.html)
  - niveles del `MultiIndex`.
* - [MultiIndex.levshape](http://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.levshape.html)
  - Retorna un `tuple` con la longitud de cada nivel.
* - [MultiIndex.names](http://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.names.html)
  - Nombres de niveles del `MultiIndex`.
* - [MultiIndex.nlevels](http://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.nlevels.html)
  - Número de niveles en el `MultiIndex`.
```

<br/>

---
### Métodos de _MultiIndex_

Métodos de la clase `MultiIndex`.

(index-multiindex-metodos-constructores)=
#### Constructores

Métodos para crear objetos `MultiIndex` desde otros objetos. Estos métodos se aplican directamente sobre la clase `MultiIndex` y no sobre sus instancias. 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [MultiIndex.from_arrays](http://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.from_arrays.html)(arrays[, sortorder, ...])
  - Convierte arreglos a `MultiIndex`.
* - [MultiIndex.from_frame](http://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.from_frame.html)(df[, sortorder, names])
  - Crea una `MultiIndex` a partir de un `DataFrame`.
* - [MultiIndex.from_product](http://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.from_product.html)(iterables[, ...])
  - Crea una `MultiIndex` del producto cartesiano de múltiples iterables.
* - [MultiIndex.from_tuples](http://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.from_tuples.html)(tuples[, sortorder, ...])
  - Convierte `list` de `tuple` a `MultiIndex`.
```

<br/>

#### Convertir

Métodos para convertir objetos `MultiIndex` a otro tipo de objeto. 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [MultiIndex.to_flat_index](http://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.to_flat_index.html)()
  - Convierte un `MultiIndex` a un `Index` de tuplas que contienen los valores de los niveles.
* - [MultiIndex.to_frame](http://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.to_frame.html)([index, name, ...])
  - Crea un `DataFrame` con los niveles del `MultiIndex` como columnas.
```

#### Modificar

Métodos que permiten modificar un `MultiIndex` como agregar niveles, eliminar niveles, reordenar niveles, etc. 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [MultiIndex.append](http://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.append.html)(other)
  - Concatena una colección de elementos `Index`.
* - [MultiIndex.copy](http://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.copy.html)([names, deep, name])
  - Crea una copia del objeto.
* - [MultiIndex.drop](http://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.drop.html)(codes[, level, errors])
  - Retorna un nuevo `pandas.MultiIndex` eliminando determinados códigos.
* - [MultiIndex.droplevel](http://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.droplevel.html)([level])
  - Elimina un nivel determinado del `MultiIndex`.
* - [MultiIndex.remove_unused_levels](http://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.remove_unused_levels.html)()
  - Crea un nuevo `MultiIndex` eliminando los niveles no utilizados.
* - [MultiIndex.reorder_levels](http://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.reorder_levels.html)(order)
  - Reordena los niveles usando el orden de entrada.
* - [MultiIndex.set_codes](http://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.set_codes.html)(codes, *[, level, ...])
  - Establece nuevos códigos en `MultiIndex`.
* - [MultiIndex.set_levels](http://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.set_levels.html)(levels, *[, level, ...])
  - Establecer nuevos niveles en `MultiIndex`.
* - [MultiIndex.sortlevel](http://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.sortlevel.html)([level, ascending, ...])
  - Ordena el `MultiIndex` en el nivel indicado.
* - [MultiIndex.swaplevel](http://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.swaplevel.html)([i, j])
  - Intercambia el nivel _i_ con el nivel _j_.
* - [MultiIndex.truncate](http://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.truncate.html)([before, after])
  - Trunca el índice entre dos etiquetas/tuplas, retorna un nuevo `MultiIndex`.
```

<br/>

#### Selección

Métodos para seleccionar y recuperar ubicaciones de determinados elementos en el objeto `MultiIndex`. 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [MultiIndex.get_indexer](http://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.get_indexer.html)(target[, method, ...])
  - Retorna un _indexador_ dado el índice actual y un nuevo índice. El _indexador_ es un arreglo que indica las posiciones de los valores en un nuevo índice _target_ dadas las posiciones actuales de los mismos valores en el índice actual. Si un valor en _target_ no existe en el índice actual se le asigna la posición -1.
* - [MultiIndex.get_level_values](http://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.get_level_values.html)(level)
  - Retorna un vector con los valores de etiqueta para el nivel solicitado.
* - [MultiIndex.get_loc](http://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.get_loc.html)(key)
  - Recupera la ubicación para una etiqueta o un `tuple` de etiquetas.
* - [MultiIndex.get_loc_level](http://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.get_loc_level.html)(key[, level, ...])
  - Recupera la ubicación y el índice para las etiquetas/niveles solicitados.
* - [MultiIndex.get_locs](http://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.get_locs.html)(seq)
  - Recupera la ubicación de una secuencia de etiquetas.
```

<br/>

---
## DateTimeIndex

La clase `DateTimeIndex` es una subclase de `Index` de tipo `datetime64` que representan fechas y tiempos. Para crear un objeto `Series` o `DataFrame` con un índice de fecha primero se debe de crear un objeto `DateTimeIndex`, posteriormente asignar ese objeto al parámetro _index_. Algunas características de las listas, son:
- Es inmutable: Sus elementos no se pueden modificar una vez creado el objeto.
- Está indexado: Cada elemento está asociado con un índice y por lo tanto sus elementos están ordenados.
- Es un iterable: Se puede iterar por sus elementos y se puede usar la palabra reservada `in` para verificar memebresía.
- Permite valores duplicados.

<br/>

### Creación

Para crear un `DateTimeIndex` existen principalmente tres métodos:

**1. Con el constructor**.

Usar el constructor con un `array-like` 1D de `str` u objetos `datetime-like`.

```{list-table}
:header-rows: 1

* - Constructor
  - Descripción
* - [DatetimeIndex](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.html)([data, freq, tz, normalize, ...])
  - Arreglo inmutable de datos `datetime64`.
```

**Ejemplo**:
```{code-cell} ipython3
# Crear DateTimeIndex con el constructor
dtidx = pd.DatetimeIndex(['2020-01-01', '2021-01-01', '2022-01-01', '2023-01-01'])

# Imprimir objeto
print(f"DatetimeIndex:\n{dtidx}")
```

<br/>

**2.  Con la función** `pd.date_range()`.

La función [pd.date_range()](https://pandas.pydata.org/docs/reference/api/pandas.date_range.html#pandas.date_range) retorna un `DateTimeIndex`, se debe indicar la fechas-tiempo de inicio y fin (`str` o `datetime-like`) y opcionalmente el número de periodos y frecuencia.

**Ejemplo**:
```{code-cell} ipython3
# Crear DateTimeIndex con la función pd.date_range()
dtidx = pd.date_range('2020-01-01', '2024-01-01', freq='YE')

# Imprimir objeto
print(f"DatetimeIndex:\n{dtidx}")
```
- Para ver la manera de definir el parámetro _freq_ revisar {ref}`pd-anexos-offsets`.

:::{warning}
Notar que para replicar el `DateTimeIndex` retornado por el ejemplo con el constructor, fue necesario especificar el parámetro `freq='YS'`, esto es así porque por default `pd.date_range()` tiene `freq='D'` que significa con una frecuencia por día.
:::

<br/>

**3 Con la función** `pd.to_datetime()`

Si se provee de un `list-like` de `str`, {ref}`pd.TimeStamp <pandas-scalars-timestamp>` u objetos `datetime-like` entonces la función [pd.to_datetime()](https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html#pandas.to_datetime) retorna `DateTimeIndex`.

**Ejemplo**:
```{code-cell} ipython3
# Definir lista
dates = ['2020-01-01', '2021-01-01', '2022-01-01', '2023-01-01']

# Crear DatetimeIndex con pd.to_datetime()
dtidx = pd.to_datetime(dates)

# Imprimir objeto
print(f"DatetimeIndex:\n{dtidx}")
```

<br/>

---
### Seleccion elementos de _DateTimeIndex_

:::{warning}
En esta sección se explica cómo seleccionar elementos en objetos con índices de tipo `DatetimeIndex`. Los métodos aquí explicados **no** se aplican directamente sobre objetos `DatetimeIndex`. Para seleccionar elementos directamente en un objeto `DatetimeIndex` ver {ref}`index-index-seleccion`, pero en esencia se pueden aplicar las mismas estrategias para seleccionar elementos que en un `ndarray`.
:::

Al especificar la fecha y tiempo se puede hacer de diversas formas:
- Se pueden usar cadenas que representen fechas-tiempo. Es recomendado usar cadenas que respeten ISO 8601 `YYYY-MM-DD HH:MM:SS`, pero es posible ponerlo en otros formatos como `MM/DD/YYYY HH:MM:SS`, `YYYYMMDD HH:MM:SS`, etc.
- Se pueden usar objetos de tipo `datetime.datetime`.
- Se pueden usar objetos de tipo `pd.TimeStamp`.

:::{warning}
No se puede usar cadenas con el formato `DD/MM/YYYY` porque se va a interpretar como `MM/DD/YYYY`.
:::

#### Con corchetes

:::{caution}
Para esta sección tener en cuenta lo siguiente:
- Todos los ejemplos presentados en esta sección se harán suponiendo que se aplican a un `Series` con `DateTimeIndex`. No es posible seleccionar elementos (filas) en un `DataFrame` con este método, en un `DataFrame` usar el método `.iloc[]`.
- Los ejemplos aquí presentados se harán con cadenas ISO 8601 _'YYYY-MM-DD'_, pero como se comentó anteriormente se pueden usar otros formatos, incluir el tiempo también o usar instancias de otras clases.
:::

Estrategias de selección de elementos:
- **Indexing**: Seleccionar elementos con una fecha específica o unidades específicas
    - Fechas indicando todas las unidades, las coincidencias serán exactas: <br/> `X['YYYY-MM-DD']` <br/> `X[datetime(yyyy, mm, dd)]` <br/> `X[pd.Timestamp(year = yyyy, month = mm, day = dd)]`
    - Fechas indicando solo algunas unidades parciales, entonces se seleccionarán todos los registros que satisfagan esas unidades: <br/> `X['YYYY'] # Con base al año` <br/> `X['YYYY-MM'] # Con base al año y mes`
- **Slicing**:
    - Rangos considerando todas las unidades y que muestren todos las fechas que estén dentro de ese rango, ambos extremos son inclusivos: <br/> `X['YYYY-MM-DD':'YYYY-MM-DD']`
    - Rangos de solo algunas unidades parciles, que muestren todos las fechas que estén dentro de ese rango, ambos extremos son inclusivos: <br/> `X['YYYY':'YYYY'] # Rangos con base al año` <br/> `X['YYYY-MM':'YYYY-MM'] # Rangos con base al año y mes`
    - **Importante**: Se puede omitir el _start_ o _end_ para indicar desde el inicio y hasta el final respectivamente, la parte que sí se indique es inclusiva: <br/> `X[:'YYYY'] # Desde el inicio` <br/> `X['YYYY':] # Hasta el final`
- **Fancy indexing**:
    - Múltiples fechas específicas indicando todas las unidades: <br/> `X[['YYYY-MM-DD', 'YYYY-MM-DD', ...]]`
    - Múltiples fechas indicando solo algunas unidades parciales: <br/> `X[['YYYY', 'YYYY', ...]] # Elementos con base a múltiples años` <br/> `X[['YYYY-MM', 'YYYY-MM', ...]] # Elementos con base a múltiples años y meses`

#### Con el método .loc[]

:::{caution}
Para esta sección tener en cuenta lo siguiente:
- Todos los ejemplos presentados en esta sección se harán suponiendo que se aplican a un `DataFrame` con `DateTimeIndex` y que las columnas se seleccionan por indexing, pero se puede seleccionar las columnas con cualquier otra estrategia válida. En caso de que se aplique en un `Series` simplemente omitir la parte de las columnas.
- Los ejemplos aquí presentados se harán con cadenas ISO 8601 `'YYYY-MM-DD'`, pero como se comentó anteriormente se pueden usar otros formatos, incluir el tiempo también o usar instancias de otras clases.
:::

Estrategias de selcción de elementos con el método `.loc[]`:
- **Indexing**: Seleccionar elementos con una fecha específica o unidades específicas
    - Fechas indicando todas las unidades, las coincidencias serán exactas: <br/> `X.loc['YYYY-MM-DD', col]` <br/> `X.loc[datetime(yyyy, mm, dd), col]` <br/> `X.loc[pd.Timestamp(year = yyyy, month = mm, day = dd), col]`
    - Fechas indicando solo algunas unidades parciales, entonces se seleccionarán todos los registros que satisfagan esas unidades: <br/> `X.loc['YYYY', col] # Con base al año` <br/> `X.loc['YYYY-MM', col] # Con base al año y mes`
- **Slicing**:
    - Rangos considerando todas las unidades y que muestren todos las fechas que estén dentro de ese rango, ambos extremos son inclusivos: <br/> `X.loc['YYYY-MM-DD':'YYYY-MM-DD', col]`
    - Rangos de solo algunas unidades parciales, que muestren todos las fechas que estén dentro de ese rango, ambos extremos son inclusivos: <br/> `X.loc['YYYY':'YYYY', col] # Rangos con base al año` <br/> `X.loc['YYYY-MM':'YYYY-MM', col] # Rangos con base al año y mes`
    - **Importante**: Se puede omitir el _start_ o _end_ para indicar desde el inicio y hasta el final respectivamente, la parte que sí se indique es inclusiva: <br/> `X.loc[:'YYYY', col] # Desde el inicio` <br/> `X.loc['YYYY':, col] # Hasta el final`
- **Fancy indexing**:
    - Múltiples fechas específicas indicando todas las unidades: <br/> `X.loc[['YYYY-MM-DD', 'YYYY-MM-DD', ...], col]`
    - Múltiples fechas indicando solo algunas unidades parciales: <br/> `X.loc[['YYYY', 'YYYY', ...], col] # Elementos con base a múltiples años` <br/> `Xloc[['YYYY-MM', 'YYYY-MM', ...], col] # Elementos con base a múltiples años y meses`

<br/>

---
### Atributos de _DatetimeIndex_

Atributos para recuperar partes individuales del `DateTimeIndex`.

:::{caution}
Los atributos retornarnan _arrays_.
:::

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - `DatetimeIndex.date`
  - Retorna objetos `datetime.date` que representan la fecha. 
* - `DatetimeIndex.day`
  - Día del mes.
* - `DatetimeIndex.day_name`
  - Retorna el nombre del día con la configuración regional especificada.
* - `DatetimeIndex.day_of_week`
  - El día de la semana, donde lunes=0 y domingo=6.
* - `DatetimeIndex.day_of_year`
  - El día ordinal del año.
* - `DatetimeIndex.dayofweek`
  - El día de la semana, donde lunes=0, domingo=6.
* - `DatetimeIndex.dayofyear`
  - El día ordinal del año.
* - `DatetimeIndex.freq`
  - Frecuencia del índice.
* - `DatetimeIndex.freqstr`.
  - Retorna la frecuencia como cadena, o `None` si no tiene.
* - `DatetimeIndex.hour`
  - La Hora.
* - `DatetimeIndex.inferred_freq`
  - Intenta devolver una cadena que representa una frecuencia generada por `infer_freq`.
* - `DatetimeIndex.is_leap_year`
  - Indica si la fecha pertenece a un año bisiesto.
* - `DatetimeIndex.is_month_end`
  - Indica si la fecha es el último día del mes.
* - `DatetimeIndex.is_month_start`
  - Indica si la fecha es el primer día del mes.
* - `DatetimeIndex.is_quarter_end`
  - Indicador de si la fecha es el último día del trimestre.
* - `DatetimeIndex.is_quarter_start`
  - Indicador de si la fecha es el primer día del trimestre.
* - `DatetimeIndex.is_year_end`
  - Indica si la fecha es el último día del año.
* - `DatetimeIndex.is_year_start`
  - Indica si la fecha es el primer día de un año.
* - `DatetimeIndex.microsecond`
  - Los microsegundos.
* - `DatetimeIndex.minute`
  - Los minutos.
* - `DatetimeIndex.month`
  - El mes, donde enero=1, diciembre=12.
* - `DatetimeIndex.month_name`
  - Retorna los nombres de los meses con la configuración regional especificada.
* - `DatetimeIndex.nanosecond`
  - Los nanosegundos.
* - `DatetimeIndex.quarter`
  - El trimestre.
* - `DatetimeIndex.second`
  - Los segundos.
* - `DatetimeIndex.time`
  - Retorna objetos `datetime.time` que representa el tiempo.
* - `DatetimeIndex.timetz`
  - Retorna objetos `datetime.time` que representa el tiempo con zona horaria.
* - `DatetimeIndex.tz`
  - Retorna la zona horaria.
* - `DatetimeIndex.weekday`
  - El día de la semana, donde lunes=0, domingo=6.
* - `DatetimeIndex.year`: 
  - El año.
```
- Para más información visitar la [documentación](https://pandas.pydata.org/docs/reference/indexing.html#time-date-components) de `pandas`.

<br/>

---
### Métodos de _DatetimeIndex_

#### Conversión 

Métodos para modificar el _dtype_ o el tipo de objeto del índice.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [DatetimeIndex.as_unit](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.as_unit.html)(*args, **kwargs)
  - Convierte a un `dtype` con la resolución unitaria dada.
* - [DatetimeIndex.to_frame](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.to_frame.html)([index, name])
  - Retorna un `DataFrame` con una columna que contiene el `Index`.
* - [DatetimeIndex.to_period](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.to_period.html)(*args, **kwargs)
  - Convierte el objeto a `PeriodArray`/`PeriodIndex` con una frecuencia particular.
* - [DatetimeIndex.to_pydatetime](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.to_pydatetime.html)(*args, **kwargs)
  - Retorna un `ndarray` de objetos `datetime.datetime`.
* - [DatetimeIndex.to_series](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.to_series.html)([index, name])
  - Crea un `Series` con el `Index` y valores iguales a el `Index`.
```

<br/>

#### Métodos estadísticos

Métodos útiles para calcular estadísticas del índice.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [DatetimeIndex.mean](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.mean.html)(*[, skipna, axis])
  - Retorna el valor medio del índice.
* - [DatetimeIndex.std](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.std.html)(*args, **kwargs)
  - Retorna la desviación estándar del índice.
```

<br/>

#### Operaciones específicas de tiempo

Métodos para trabajar con los valores de fechas y tiempo.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [DatetimeIndex.ceil](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.ceil.html)(*args, **kwargs)
  - Redondea hacía arriba los datos a la frecuencia especificada.
* - [DatetimeIndex.floor](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.floor.html)(*args, **kwargs)
  - Redondea hacía abajolos datos a la frecuencia especificada.
* - [DatetimeIndex.normalize](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.normalize.html)(*args, **kwargs)
  - Convierte las horas a medianoche.
* - [DatetimeIndex.round](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.round.html)(*args, **kwargs)
  - Redondea los datos a la frecuencia especificada.
* - [DatetimeIndex.snap](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.snap.html)([freq])
  - Ajusta las marcas de tiempo a la frecuencia más cercana.
* - [DatetimeIndex.strftime](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.strftime.html)(date_format)
  - Convierte a `Index` utilizando el formato de fecha especificado.
* - [DatetimeIndex.tz_convert](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.tz_convert.html)(tz)
  - Convierte los valores de una zona horaria a otra.
* - [DatetimeIndex.tz_localize](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.tz_localize.html)(tz[, ambiguous, ...])
  - Establece la zona hoararia, sin modificar la hora.
```

<br/>

#### Selección

Métodos últiles para seleccionar elementos que cumplan determinadas características.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [DatetimeIndex.indexer_at_time](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.indexer_at_time.html)(time[, asof])
  - Retorna valores dado en un momento particular.
* - [DatetimeIndex.indexer_between_time](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.indexer_between_time.html)(...[, ...])
  - Retorna valores dados entre momentos particulares del día.
```

<br/>

---
## TimeDeltaIndex

La clase `TimeDeltaIndex` es una subclase de `Index` de tipo `timedelta64` que representan diferencias de fechas y/o tiempos (duraciones).

<br/>

### Creación

Para crear un `TimeDeltaIndex` existen principalmente tres métodos:

**1. Con el constructor**.

Usar el constructor con un `array-like` 1D de `str`, `datetime.timedelta` o {ref}`pd.Timedelta <pandas-scalars-timedelta>`.

```{list-table}
:header-rows: 1

* - Constructor
  - Descripción
* - [TimeDeltaIndex](https://pandas.pydata.org/docs/reference/api/pandas.TimedeltaIndex.html)([data, freq, tz, normalize, ...])
  - Arreglo inmutable de datos `timedelta64`.
```

**Ejemplo**:
```{code-cell} ipython3
# Crear TimeDeltaIndex con el constructor
tdidx = pd.TimedeltaIndex(['0 days', '1 days', '2 days', '3 days', '4 days'])

# Imprimir objeto
print(f"TimedeltaIndex:\n{tdidx}")
```

**2. Con la función** `pd.to_timedelta()`

Si se provee de un `list-like` de `str`, `datetime.timedelta` o `pd.TimeDelta` entonces la función [pd.to_timedelta()](https://pandas.pydata.org/docs/reference/api/pandas.to_timedelta.html#pandas.to_timedelta) retorna `TimeDeltaIndex`.

**Ejemplo**:
```{code-cell} ipython3
# Crear TimeDeltaIndex con la función to_timedelta()
tdidx = pd.to_timedelta(['0 days', '1 days', '2 days', '3 days', '4 days'])

# Imprimir objeto
print(f"TimedeltaIndex:\n{tdidx}")
```

<br/>

**3.  Con la función** `pd.timedelta_range()`.

La función [pd.timedelta_range()](https://pandas.pydata.org/docs/reference/api/pandas.timedelta_range.html#pandas.timedelta_range) retorna un `TimeDeltaIndex`, se debe indicar las duraciones de inicio y fin (`str` o `datetime-like`) y/u opcionalmente el número de periodos y frecuencia.

**Ejemplo**:
```{code-cell} ipython3
# Crear DateTimeIndex con la función timedelta_range()
tdidx = pd.timedelta_range(start='1 day', end='2 days', freq='6h')

# Imprimir objeto
print(f"TimeDeltaIndex:\n{tdidx}")
```

<br/>

### Selección de elementos de _TimeDeltaIndex_

:::{warning}
En esta sección se explica cómo seleccionar elementos en objetos con índices de tipo `TimeDeltaIndex`. Los métodos aquí explicados **no** se aplican directamente sobre objetos `TimeDeltaIndex`. Para seleccionar elementos directamente en un objeto `TimeDeltaIndex` ver {ref}`index-index-seleccion`, pero en esencia se pueden aplicar las mismas estrategias para seleccionar elementos que en un `ndarray`.
:::

Al especificar el _timedelta_ se puede hacer principalmente de tres formas:
- Se pueden usar cadenas que representen _timedeltas_. 
- Se pueden usar objetos de tipo `datetime.timedelta`.
- Se pueden usar objetos de tipo {ref}`pd.Timedelta <pandas-scalars-timedelta>`.

:::{caution}
Para esta sección tener en cuenta lo siguiente:
- Los ejemplos aquí presentados se harán con cadenas.
- Los ejemplos aquí presentados se harán con el método `.loc[]`, tambien se pueden usar corchetes y funcionaría de manera muy similar que con `.loc[]`. También se podría usar el método `.iloc[]` y usando los índices implícitos.
- Todos los ejemplos presentados en esta sección se harán suponiendo que se aplican a un `DataFrame` con `TimeDeltaIndex` y que las columnas se seleccionan por _indexing_, pero se puede seleccionar las columnas con cualquier otra estrategia válida. En caso de que se aplique en un `Series` simplemente omitir la parte de las columnas.
:::
- **Indexing**: Seleccionar elementos con _timedelta_ específico <br/> `X.loc['timedelta', col]` <br/> `X.loc[datetime.timedelta(days, seconds, ...), col]` <br/> `X.loc[pd.TimeDelta(timedelta), col]`
- **Slicing**: _Slices_ de elementos indicando inicion, fin y paso (`start:stop:step`), al usar los _labels_ se incluyen ambos extremos (inclusivo): <br/> `X.loc['timdeltai':'timedeltaj', col]`
- **Fancy indexing**:
    - Múltiples _timedeltas_ específicos: <br/> `X.loc[['timedelta1', 'timedelta2', ...], col]`

### Atributos de _TimeDeltaIndex_

Atributos para recuperar partes individuales del `TimeDeltaIndex`.

:::{caution}
Los atributos retornarnan _arrays_.
:::

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - `TimedeltaIndex.components`
  - Retorna un `DataFrame` con los componentes individuales como columnas de los `Timedeltas`.
* - `TimedeltaIndex.days`
  - Número de días para cada elemento.
* - `TimedeltaIndex.inferred_freq`
  - Intenta devolver una cadena que representa una frecuencia generada por `infer_freq`.
* - `TimedeltaIndex.microseconds`
  - Número de microsegundos (>= 0 y menor de 1 segundo) para cada elemento.
* - `TimedeltaIndex.nanoseconds`
  - Número de nanosegundos (>= 0 y menor de 1 microsegundo) para cada elemento.
* - `TimedeltaIndex.seconds`
  - Número de segundos (>= 0 y menor de 1 día) para cada elemento.
```
- Para más información visitar la [documentación](https://pandas.pydata.org/docs/reference/indexing.html#components) de `pandas`.

<br/>

---
### Métodos de _TimeDeltaIndex_

Métodos de la clase `TimeDeltaIndex`

#### Conversión 

Métodos para modificar el _dtype_ o el tipo de objeto del índice.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [TimedeltaIndex.as_unit](https://pandas.pydata.org/docs/reference/api/pandas.TimedeltaIndex.as_unit.html)(unit)
  - Convierte a un `dtype` con la resolución unitaria dada.
* - [TimedeltaIndex.ceil](https://pandas.pydata.org/docs/reference/api/pandas.TimedeltaIndex.ceil.html)(*args, **kwargs)
  - Redondea hacia arriba los datos a la frecuencia especificada.
* - [TimedeltaIndex.floor](https://pandas.pydata.org/docs/reference/api/pandas.TimedeltaIndex.floor.html)(*args, **kwargs)
  - Redondea hacia abajo los datos a la frecuencia especificada.
* - [TimedeltaIndex.round](https://pandas.pydata.org/docs/reference/api/pandas.TimedeltaIndex.round.html)(*args, **kwargs)
  - Redondea los datos a la frecuencia especificada.
* - [TimedeltaIndex.to_frame](https://pandas.pydata.org/docs/reference/api/pandas.TimedeltaIndex.to_frame.html)([index, name])
  - Crea un `DataFrame` con una columna que contiene el `Index`.
* - [TimedeltaIndex.to_pytimedelta](https://pandas.pydata.org/docs/reference/api/pandas.TimedeltaIndex.to_pytimedelta.html)(*args, **kwargs)
  - Retorna un `ndarray` de objetos `datetime.timedelta`.
* - [TimedeltaIndex.to_series](https://pandas.pydata.org/docs/reference/api/pandas.TimedeltaIndex.to_series.html)([index, name])
  - Crea un `Series` con índice y valores iguales a el `Index`.
```

<br/>

---
#### Métodos estadísticos

Métodos para trabajar con los valores de las duraciones.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [TimedeltaIndex.mean](https://pandas.pydata.org/docs/reference/api/pandas.TimedeltaIndex.mean.html)(*[, skipna, axis])
  - Retorna el valor medio del índice.
```

<br/>

---
## PeriodIndex

La clase `PeriodIndex` es una subclase de `Index` que representa un arreglo inmutable de valores ordinales que representan periodos de tiempo regulares.

<br/>

### Creación

**1. Con el constructor**

Usar el constructor con un `array-like` 1D de `int`, `str` u objetos {ref}`pd.Period <pandas-scalars-period>`.

```{list-table}
:header-rows: 1

* - Constructor
  - Descripción
* - [PeriodIndex](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.html)([data, ordinal, freq, dtype, ...])
  - Arreglo inmutable de valores ordinales que representan peridos de tiempo regulares.
```

**Ejemplo**:

```{code-cell} ipython3
# Crear PeriodIndex con el constructor
pidx = pd.PeriodIndex(['2023-01', '2023-02', '2023-03'], freq='M')

# Imprimir objeto
print(f"PeriodIndex:\n{pidx}")
```

<br/>

**2. Con métodos de pd.PeriodIndex**

La clase `pd.PeriodIndex` tiene algunos métodos que permiten construir `PeriodIndex` de distintas formas. Consultar los {ref}`Métodos <pandas-index-periodindex-methods>`, particularmente `pd.PeriodIndex.from_fields()` y `pd.PeriodIndex.from_ordinals()`. Tener en cuenta que los métodos se usan directamente sobre la clase `pd.PeriodIndex` y no sobre sus instancias.

**Ejemplo**:

```{code-cell} ipython3
# Crear PeriodIndex desde el método .from_fields()
pidx = pd.PeriodIndex.from_fields(year=[2023]*3, month=[1, 2, 3], freq='M')

# Imprimir objeto
print(f"PeriodIndex:\n{pidx}")
```

<br/>

**3. Con la función** `pd.period_range()`:

La función [pd.period_range()](https://pandas.pydata.org/docs/reference/api/pandas.period_range.html)` retorna un `PeriodIndex`, se debe indicar el periodo inicial y final, y opcionalmente el número de periodos y/o frecuencia.

**Ejemplo**:

```{code-cell} ipython3
# Crear PeriodIndex con la función pd.period_range()
pidx = pd.period_range(start='2023-01', end='2023-03', freq='M')

# Imprimir objeto
print(f"PeriodIndex:\n{pidx}")
```

<br/>

**4. Con la función** `pd.to_datetime()`:

La función [pd.to_datetime()](https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html) se puede aprovechar para crear un `DateTimeIndex` y posteriormente convertilos a `PeriodIndex` con el método `DateTimeIndex.to_period()`, en el cual se debe especificar la frecuencia.

```{code-cell} ipython3
# Crear PeriodIndex con la función pd.to_datetime()
dtidx = pd.to_datetime(['2023-01', '2023-02', '2023-03'])
pidx = dtidx.to_period('M')

# Imprimir objeto
print(f"PeriodIndex:\n{pidx}")
```

<br/>

### Selección de elementos de _PeriodIndex_

:::{warning}
En esta sección se explica cómo seleccionar elementos en objetos con índices de tipo `PeriodIndex`. Los métodos aquí explicados **no** se aplican directamente sobre objetos `PeriodIndex`. Para seleccionar elementos directamente en un objeto `PeriodIndex` ver {ref}`index-index-seleccion`, pero en esencia se pueden aplicar las mismas estrategias para seleccionar elementos que en un `ndarray`.
:::

Al especificar el _period_ se puede hacer principalmente de dos formas:
- Se pueden usar cadenas que representen _periods_. 
- Se pueden usar objetos de tipo `datetime.datetime`.
- Se pueden usar objetos de tipo {ref}`pd.TimeStamp <pandas-scalars-timestamp>`.

:::{caution}
Para esta sección tener en cuenta lo siguiente:
- Los ejemplos aquí presentados se harán con cadenas.
- Los ejemplos aquí presentados se harán con el método `.loc[]`, tambien se pueden usar corchetes y funcionaría de manera muy similar que con `.loc[]`. También se podría usar el método `.iloc[]` y usando los índices implícitos.
- Todos los ejemplos presentados en esta sección se harán suponiendo que se aplican a un `DataFrame` con `PeriodIndex` y que las columnas se seleccionan por _indexing_, pero se puede seleccionar las columnas con cualquier otra estrategia válida. En caso de que se aplique en un `Series` simplemente omitir la parte de las columnas.
:::
- **Indexing**: Seleccionar elementos con _period_ específico <br/> `X.loc['YYYY-MM-DD', col]` <br/> `X.loc[datetime.datetime(year, month, day, ...), col]` <br/> `X.loc[pd.TimeStamp(yyyy, mm, dd), col]`
- **Slicing**: _Slices_ de elementos indicando inicion, fin y paso (`start:stop:step`), al usar los _labels_ se incluyen ambos extremos (inclusivo): <br/> `X.loc['YYYY-MM-DD':'YYYY-MM-DD', col]`
- **Fancy indexing**:
    - Múltiples _timedeltas_ específicos: <br/> `X.loc[['YYYY-MM-DD', 'YYYY-MM-DD', ...], col]`

<br/>

### Atributos de _PeriodIndex_

Atributos para recuperar partes individuales del `DateTimeIndex`.

:::{caution}
Los atributos retornarnan _arrays_.
:::

```{list-table}
:header-rows: 1
:name: pandas-index-periodindex-attributes

* - Método
  - Descripción
* - `PeriodIndex.day`
  - Los días del período.
* - `PeriodIndex.day_of_week`
  - El día de la semana con lunes=0, domingo=6.
* - `PeriodIndex.day_of_year`
  - El día ordinal del año.
* - `PeriodIndex.dayofweek`
  - El día de la semana con lunes=0, domingo=6.
* - `PeriodIndex.dayofyear`
  - El día ordinal del año.
* - `PeriodIndex.days_in_month`
  - El número de días del mes.
* - `PeriodIndex.daysinmonth`
  - El número de días del mes.
* - `PeriodIndex.end_time`
  - Recupera la marca de tiempo del final del período.
* - `PeriodIndex.freq`
  - .
* - `PeriodIndex.freqstr`
  - Retorna el objeto de frecuencia como una cadena si es `set` , de lo contrario `None`.
* - `PeriodIndex.hour`
  - La hora del período.
* - `PeriodIndex.is_leap_year`
  - Lógico indicar si la fecha pertenece a un año bisiesto.
* - `PeriodIndex.minute`
  - El minuto del periodo.
* - `PeriodIndex.month`
  - El mes como enero=1, diciembre=12.
* - `PeriodIndex.quarter`
  - El cuarto de la fecha.
* - `PeriodIndex.qyear`
  - .
* - `PeriodIndex.second`
  - El segundo del periodo.
* - `PeriodIndex.start_time`
  - Recupera la marca de tiempo del inicio del período.
* - `PeriodIndex.week`
  - El ordinal de semana del año.
* - `PeriodIndex.weekday`
  - El día de la semana con lunes=0, domingo=6.
* - `PeriodIndex.weekofyear`
  - El ordinal de semana del año.
* - `PeriodIndex.year`
  - El año del período.
```
- Para más información visitar la [documentación](https://pandas.pydata.org/docs/reference/indexing.html#id7) de `pandas`.
 
<br/>

---
### Métodos de _PeriodIndex_

Métodos de objeto `PeriodIndex`. Tener en cuenta que `.from_ordinals()` y `.from_fields()` son métodos de clase y no de instancia.

```{list-table}
:header-rows: 1
:name: pandas-index-periodindex-methods

* - Método
  - Descripción
* - [PeriodIndex.asfreq](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.asfreq.html)([freq, how])
  - Convierte el `PeriodArray` a la frecuencia especificada.
* - [PeriodIndex.from_fields](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.from_fields.html)(*[, year, quarter, ...])
  - Crea un `PeriodIndex` indicando las partes de cada _period_, se debe de proveer un `array-like` por cada campo, todos del mismo tamaño. Para conformar el _period_ los elementos se empatarán por posición.
* - [PeriodIndex.from_ordinals](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.from_ordinals.html)(ordinals, *, freq)
  - Crea un `PeriodIndex` indicando los ordinales del _period_ como `array-like` e indicando la frecuencia.
* - [PeriodIndex.strftime](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.strftime.html)(*args, **kwargs)
  - Convierte a `Index` indicando el formato de fecha especificado.
* - [PeriodIndex.to_timestamp](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.to_timestamp.html)([freq, how])
  - Convierte el objeto a `DatetimeArray`/`DatetimeIndex`.
```
