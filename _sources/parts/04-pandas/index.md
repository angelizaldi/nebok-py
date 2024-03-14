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

Los objetos `Index` son un array inmutable, funje el papel de identificar por medio de etiquetas las filas y columnas. Pueden ser vistos como un `set` ordenado o un multi set ordenado, aunque `index` puede tener valores repetidos.

En esta sección se presentará principalmente la clase `Index`, pero no es el único tipo de índice que existe, entre otros índices disponibles están:
- [RangeIndex](https://pandas.pydata.org/docs/reference/indexing.html#numeric-index): Índice numérico.
- [CategoricalIndex](https://pandas.pydata.org/docs/reference/indexing.html#categoricalindex): Índice categórico.
- [IntervalIndex](https://pandas.pydata.org/docs/reference/indexing.html#intervalindex): Índice por intervalos.
- [MultiIndex](https://pandas.pydata.org/docs/reference/indexing.html#multiindex): Índice multinivel o jerarquíco.
- [DatetimeIndex](https://pandas.pydata.org/docs/reference/indexing.html#datetimeindex): Índice de `datetime64`.
- [TimedeltaIndex](https://pandas.pydata.org/docs/reference/indexing.html#timedeltaindex): Índice de `timedelta64`.
- [PeriodIndex](https://pandas.pydata.org/docs/reference/indexing.html#periodindex): Índice de periodos de tiempo.

<br><br>

## Tipo de índices

Los objetos `DataFrame` y `Series` tienes dos tipos de índices:
- índice implícito: Es un índice númerico, que comienza desde cero, similiar a los índices de las secuencias.
- índice explícito: Es el objeto `Index` asociado, que puede tener etiquetas`int` o `str`.

<br><br>

---
## Operaciones entre objetos

Al realizar operaciones entre clases de `pandas` tener en cuenta las siguientes características:
- Si la operación es unitaria (nada más se necesita un operando, como elevar al cuadrado) entonces el output mantendrá el índice del objeto original. 
- Si la operación es binaria (se necesitan dos operandos, como sumar dos números), entonces se alinearán los índices explícitos. Esto quiere decir que si los objetos no tienen algún índice en común, el restultado sí contendrá esos índices, pero tendrán `NaN` como valor. En el caso de `DataFrame` se alinean tantos los índices de las filas, como los índices de las columnas.
- Si la operación es entre un `DataFrame` y un `Series`, la operación se hará entre los elementos con el mismo índice explícito y de acuerdo a lo siguiente:
    - **Nivel columnas**: Si se quiere que sea a nivel de columnas, es decir, los elementos del `Series` con cada columna del `DataFrame`, se debe de usar el argumento `axis=1` (default), en este caso la cantidad de filas en el `DataFrame` debe ser igual a la cantidad de elementos en el `Series` y el `Index` del `Series` se alineará con el `Index` de las columnas del `DataFrame`. 
    - **Nivel filas**: Si se quiere que sea a nivel de filas, es decir, los elementos del `Series` con cada fila del `DataFrame`, se debe de usar el argumento `axis=0`, en este caso, la cantidad de filas en el `DataFrame` debe de ser igual a la cantidad de elementos en el `Series` y el `Index` del `Series` se alineará con el `Index` de las filas del `DataFrame`. .

<br>

```{figure} ../images/operaciones-binarias-pandas.png
:name: operacion-binaria-filas
:width: 500px
:align: center

Operaciones binarias.
```

```{attention}
Recordar que la operación únicamente se realizará entre los índices coincidentes.
```

**Ejemplo:**
En este ejemplo se puede observar una operación a nivel columnas (comportamiento por default), el índices del `Series` se alinea con las columnas del `DataFrame`, de tal forma que a toda la columna `a` del `df` se le suma 2 y a toda las columna `b` se le suma 4. Además se puede observar que los índices que no están en los dos objetos también aparecen en el resultado pero con `NaN`.

```{code-cell} ipython3
# Importar libreria
import pandas as pd

# Definir series
x = pd.Series([2, 4, 5], index=['a', 'b', 'c'])

# Definir df
df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})

# Realizar operación a nivel de columnas
df.add(x)
```

<br><br>

---
## Clase Index



### Creación de Index.

La forma más sencilla de crear un índex es con el constructor:

```{list-table}
:header-rows: 1

* - Constructor
  - Descripción
* - [Index](https://pandas.pydata.org/docs/reference/api/pandas.Index.html#pandas.Index)(data=None, dtype=None, copy=False, name=None, tupleize_cols=True)
  - Immutable sequence used for indexing and alignment.
```

Ejemplo:

```{code-cell} ipython3
# Importar librería
import pandas as pd

# Crear objeto ind
ind = pd.Index(["a", "b", "c"])

# Imprimir contenido de ind
print(ind)
```

<br>

---
### Selección de elementos

Para seleccionar elementos se pueden usar las mismas estrategias que la selección de elementos de arrays unidimensionales de numpy:
- Subsetting.
- Slicing.
- Boolean masking.
- Fancy indexing.

Adicionalmente se pueden seleccionar elementos por [Métodos de selección](https://pandas.pydata.org/docs/reference/indexing.html#selecting).

Ejemplo:
```{code-cell} ipython3
# Crear objeto ind
ind = pd.Index(["a", "e", "i", "o", "u"])

# Seleccionar haciendo subsetting -> "i"
print(f"Subsetting: {ind[2]}", end = "\n"*2)  

# Seleccionar haciendo slicing -> ["a", "i", "u"]
print(f"Slicing: {ind[::2]}", end = "\n"*2)  

# Seleccionar haciendo boolean masking -> ["i", "o"]
print(f"Boolean masking: {ind[ind.isin(['i', 'o'])]}", end = "\n"*2)  

# Seleccionar haciendo fancy indexing -> ["o", "a", "u"]
print(f"Fancy indexing: {ind[[3, 0, 4]]}", end = "\n"*2)
```

<br>

---
### Operaciones de conjuntos

Se pueden realizar operaciones de conjunto entre objetos `Index` con [Metodos de operaciones de conjunto](https://pandas.pydata.org/docs/reference/indexing.html#combining-joining-set-operations).

Ejemplo:
```{code-cell} ipython3
# Crear ind1
ind1 = pd.Index(["a", "e", "i", "o", "u"])

# Crear ind2
ind2 = pd.Index(["a", "b", "c", "d", "e"])

# Calcular la intersección -> ['a', 'e']
print(ind1.intersection(ind2))
```

```{warning} 
No se pueden usar los operadores {ref}`operadores:bitwise` para realizar operaciones de conjuntos entre objetos `Index`.
```


<br>

---
### Atributos y métodos

Para conocer los atributos y métodos de clase `Index`, visitar los siguientes links:

- **Atributos**:
    - [Propiedades](https://pandas.pydata.org/docs/reference/indexing.html#properties).
- **Métodos**:
    - [Modificación y cálculos.](https://pandas.pydata.org/docs/reference/indexing.html#modifying-and-computations).
    - [Compatibilidad con multiíndice](https://pandas.pydata.org/docs/reference/indexing.html#compatibility-with-multiindex).
    - [Valores perdidos](https://pandas.pydata.org/docs/reference/indexing.html#missing-values).
    - [Conversión](https://pandas.pydata.org/docs/reference/indexing.html#conversion).
    - [Ordenar](https://pandas.pydata.org/docs/reference/indexing.html#sorting).
    - [Operaciones específicas de tiempo](https://pandas.pydata.org/docs/reference/indexing.html#time-specific-operations).
    - [Combinación/Operaciones de unión/Operaciones de conjuntos](https://pandas.pydata.org./docs/reference/indexing.html#combining-joining-set-operations).
    - [Seleccionar](https://pandas.pydata.org/docs/reference/indexing.html#selecting).


<br><br>

---
## Multiindex

La clase multiindex es una subclase de `Index`, es un multi set ordenado, que permite tener índices jearquizados por niveles. Esta clase es una alternativa para crear objetos de más de dos dimensiones.

### Creación de un multiindex

Existen diversas formas de crear un multiindex o de crear un objetos de pandas con un índice multiindex, a continuación se enlistan algunas de ellas:

**Constructores multiindex**: La clase `Multiindex` tiene varios [constructores](https://pandas.pydata.org/docs/reference/indexing.html#multiindex-constructors) para crear un muiltiíndice a partir de secuencias anidadas, productos cartesianos o DataFrames.

Ejemplo:
```{code-cell} ipython3
# Crear multiindex desde un secuencia anidada
arrays = [[1, 1, 2, 2], ['red', 'blue', 'red', 'blue']]

multind1 = pd.MultiIndex.from_arrays(arrays, names=('number', 'color'))
print(f"Multiíndice desde secuencias: {multind1}", end="\n*"*2)

# Crear multiindex desde un producto cartesiano
numbers = [0, 1, 2]

colors = ['green', 'purple']

multind2 = pd.MultiIndex.from_product([numbers, colors], names=['number', 'color'])
print(f"Multiíndice desde producto cartesiano: {multind2}")
```
- En el caso de la secuencias anidadas, cada secuencia interior debe de ser del mismo tamaño, el número de secuencias interiores determina el número de niveles en el multiíndice y los índices se emparentan de una manera similar a como funciona la función `zip()`.
- En el caso del producto cartesiano se proporciona una secuencia anidada cuyas sencuencias interiores pueden diferir en longitud, el número de secuencias interiores determina el número de niveles en el multiíndice.

```{note}
Los multiíndices creados por los constructores se pueden usar como valor de los argumentos `index` y `columns` al momento de crear un objeto de `pandas` o al cambiar el índice de un objeto existente con el método `.reindex()`.
```

<br>

**Con el constructor Index y secuencias anidadas**: Otra alternativa para crear multiíndices es pasando directamente al constructor `Index()` alguna secuencia anidada. Cada secuencia interior debe de ser del mismo tamaño, el número de secuencias interiores determina el número de niveles en el multiíndice y los índices se empatan de una manera similar a como funciona la función `zip()`.
```{code-cell} ipython3
# Crear multiindex desde un secuencia anidada
nested_sequence = [[1, 1, 2, 2], ['red', 'blue', 'red', 'blue']]

multind1 = pd.Index(nested_sequence)
print(f"Multiíndice desde secuencias: {multind1}")
```

<br><br>
