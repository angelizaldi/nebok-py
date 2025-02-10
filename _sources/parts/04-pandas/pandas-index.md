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

# Pandas

`pandas` es una librería que se utiliza principalmente para analizar, limpiar, explorar y manipular datos tabulares. Sus principales clases son `DataFrame`, `Series` e `Index` pero tiene una variedad de clases más.

Para utilizar `pandas` es necesario instalarlo. Desde la terminal usar:
```
# Con pip
pip install pandas

# Con conda
conda install pandas
```

Una vez instalado se debe de importar
```python
# Importar pandas a la sesión
import pandas as pd
```
- `pd` es el alias por convención.
- En el sitio se utilizará `pd` para hacer referencia a `pandas`.

Para conocer la versión de `pandas` instalada usar:
```python
# Verificar la versión de pandas
pd.__version__ 
```

</br>

En pandas existen tres objetos que son con los que se estará trabajando principalmente:
- {doc}`./index`: Es un array inmutable que puede ser de cualquier tipo de dato, pero todos los elementos del mismo tipo, funje el papel de identificar por medio de etiquetas cada fila o columna. Puede ser visto como un `set` ordenado o un multi set ordenado, aunque `Index` puede tener valores repetidos.
- {doc}`./series`: Es un `ndarray` unidimensional (un vector columna) que puede ser de cualquier tipo de dato, pero todos los elementos del mismo tipo. Además las filas tienen un `Index` para identificar a cada fila.
- {doc}`./dataframe`: Aunque se podría considerar a un `DataFrame` como un `ndarray` bidimensional, como una matriz que tiene filas y columnas, en términos generales es un `ndarray` multidimensional, pero para efectos prácticos se considerará como una matriz. Las columnas pueden ser de diferentes tipos entre sí, pero los elementos de cada columna deben de ser todos del mismo tipo. Tanto las filas como las columna tiene etiquetas que identifican los elementos mediante objetos `Index`.

Las tres clases anteriores funcionan de manera similar a como funcionan los arrays de `numpy`, por ejemplo, las operaciones entre estos objetos están vectorizadas y muchas funciones de `numpy` también se pueden usar con estas clases.

</br>

---
## Tipos de datos

La mayoría de {ref}`numpy-tipos-datos` disponibles en `numpy` se pueden usar en `pandas`, estos a su vez extienden los tipos _built-in_ de escalares disponibles en Python, los cuales se pueden resumir brevemente como:

- `Integer` (_int64_): Números enteros.
- `Float` (_float64_): Números décimales.
- `Object` (_object_): Útil para almacenar cualquier tipo de dato, incluyendo cadenas `str`.
- `Datetime` (_datetime64_): Fechas y tiempo.
- `Boolean` (_bool_): Valores lógicos (`True` y `False`).

`pandas` introduce además otros escalares y _arrays_ algunos de los cuales se revisan con más detalle en {doc}`Escalares y Arrays <escalares-arrays>`.

| Tipo de Dato | Escalar | _Array_ | Alias en cadena |
| --- | --- | --- | --- |
| Datetime | {ref}`pandas-scalars-timestamp` | [pd.arrays.DatetimeArray](https://pandas.pydata.org/docs/reference/api/pandas.arrays.DatetimeArray.html#pandas.arrays.DatetimeArray) | `'datetime64[ns, <tz>]'` |
| Timedelta | {ref}`pandas-scalars-timedelta` | [pd.arrays.TimedeltaArray](https://pandas.pydata.org/docs/reference/api/pandas.arrays.TimedeltaArray.html) | `'timedelta64[<freq>]'` |
| Period | {ref}`pandas-scalars-period` | [pd.arrays.PeriodArray](https://pandas.pydata.org/docs/reference/api/pandas.arrays.PeriodArray.html#pandas.arrays.PeriodArray) | `'period[<freq>]'` |
| Interval | {ref}`pandas-scalars-interval` | [pd.arrays.IntervalArray](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntervalArray.html#pandas.arrays.IntervalArray) | `'interval'`, `'Interval'`, `'Interval[<numpy_dtype>]'`, `'Interval[datetime64[ns, <tz>``'`, `'Interval[timedelta64[<freq>``'` |
| Categorical | (none) | [pd.Categorical](https://pandas.pydata.org/docs/reference/arrays.html#categoricals) | `'category'` | 
| String | `str` | [pd.arrays.StringArray](https://pandas.pydata.org/docs/reference/arrays.html#strings) | `'string'` |
| Nullable Integer | (none) | [pd.arrays.IntegerArray](https://pandas.pydata.org/docs/reference/arrays.html##nullable-integer) | `'Int8'`, `'Int16'`, `'Int32'`, `'Int64'`, `'UInt8'`, `'UInt16'`, `'UInt32'`, `'UInt64'` |
| Nullable Float  | (none) | [pd.arrays.FloatingArray](https://pandas.pydata.org/docs/reference/arrays.html#nullable-float) | `'Float32'`, `'Float64'` |
| Nullable Boolean  | `bool` | [pd.arrays.BooleanArray](https://pandas.pydata.org/docs/reference/arrays.html#nullable-boolean) | `'boolean'` |
| Sparse | (none) | [pd.arrays.SparseArray](https://pandas.pydata.org/docs/reference/arrays.html#sparse) | `'Sparse'`, `'Sparse[int`'`, `'Sparse[float`'` |

:::{note}
Para más información visitar la [documentación](https://pandas.pydata.org/docs/reference/arrays.html#objects) de `pandas`.
:::

### Valores pérdidos en _pandas_

En las principales clases de `pandas` existen restricciones con respecto a los tipos de datos de los elementos, por ejemplo, en `Series` e `Index` todos los elementos deben de ser del mismo tipo, mientras que en `DataFrame` todos los elementos de cada columna deben de ser del mismo tipo. Tomando en cuenta lo anterior para que los objetos de `pandas` puedan tener valores pérdidos, es necesario realizar algunas conversiones en los tipos de datos. Los principales valores considerados como valores perdidos son:
1. `None`: Es un objeto _built-in_ de Python que representa un valor pérdido.
2. `NaN`: Es un valor `float` que representa un valor numérico pérdido. 

Por lo tanto para que los objetos de `pandas` puedan contener valores perdidos, respetando las restricciones de tipos de datos, es necesario que éstos se conviertan a tipo `object` o `float`, siguiendo la siguientes reglas:
1. Los objetos de tipo `object` pueden contener `None` o `np.nan`.
2. En los objetos de tipo `float` se convierten los `None` a `np.nan`.
3. Los objetos de tipo `int` se covierten a `float` en caso de que haya valores `np.nan` o `None`.
4. Los objetos de tipo `bool` se convierten a `object` en caso de que haya valores `np.nan` o `None`.

:::{note}
En `pandas` existen _arrays_ que permiten valores perdidos como _nullable integer_, _nullable float_, _nullable boolean_, así como otros de tipo fecha  y tiempo como _datetimes_ y _timedeltas_, estos valores pérdidos se representarán por los objetos `pd.NA` y `pd.NaT`.
:::

<br>

---
## Operaciones entre objetos 

Al realizar operaciones con las clases de `pandas` tener en cuenta las siguientes características.

### Operaciones unitarias

Si la operación es unitaria, es decir, que utiliza un solo objeto, como elevar al cuadrado, entonces el objeto resultante tendrá el mismo `Index` que el objeto original:

```{code-cell} ipython3
# Importar librería
import pandas as pd

# Crear Series
s = pd.Series(data=[i**2 for i in range(1, 6)], 
              index = ['uno', 'dos', 'tres', 'cuatro', 'cinco'], 
              name="cuadrados")

# Imprimir el objeto
print(s**2)
```

<br>

### Operaciones binarias

Si la operación es binaria, es decir, utiliza dos objetos, entonces el objeto resultante tendrá como `Index` la **unión** de los índices de ambos objetos, pero únicamente tendrán valores la **intersección** de ambos objetos, mientras que el resto tendrán `NaN`. En caso de que los objetos sean ambos `DataFrame` la unión de índices se hace tanto para las filas como para las columnas.

```{code-cell} ipython3
# Crear otro Series
o = pd.Series(data = [1, 3, 5, 7, 9], 
              index = ['uno', 'tres', 'cinco', 'siete', 'nueve'], 
              name = "impares")

# Imprimir el objeto
print(s+o)
```
- **Importante**: Notar que el índice se ordena de manera ascendente. Lo mismo ocurriría con las columnas en `DataFrame`s.

:::{tip}
En caso de que la operación se realice con una función o método, es posible que se pueda utilizar el parámetro _fill_ para indicar algún valor para rellenar los valores `NaN`.
:::

<br>

### Operaciones entre `Series` y `DataFrame`

Si la operación es entre un `DataFrame` y un `Series`, la operación se hará entre los elementos con el mismo índice explícito, y se realizará _broadcasting_ del `Series` de acuerdo a lo siguiente:
- **Nivel columnas**: Si se quiere que sea a nivel de columnas, es decir, los elementos del `Series` a lo largo de las columnas del `DataFrame`, se debe de usar el argumento `axis=1` (default).
    - El `Series` se convertirá en un _vector fila_ y se "duplicará" a lo largo de las filas del `DataFrame`, para posteriormente hacer la operación _element wise_.
    - El `Index` del `Series` se alineará con el `Index` de las columnas del `DataFrame`. 
- **Nivel filas**: Si se quiere que sea a nivel de filas, es decir, los elementos del `Series` a lo largo de las filas del `DataFrame`, se debe de usar el argumento `axis=0`.
    - El `Series` se convertirá en un _vector columna_ y se "duplicará" a lo largo de las columnas del `DataFrame`, para posteriormente hacer la operación _element wise_. 
    - El `Index` del `Series` se alineará con el `Index` de las filas del `DataFrame`. .

<br>

```{figure} ../images/operaciones-binarias-pandas.png
:name: operaciones-binarias
:width: 500px
:align: center

Operaciones binarias entre `Series` y `DataFrame`.
```

```{attention}
Recordar que la operación únicamente se realizará entre los índices coincidentes.
```

**Ejemplo:**
En este ejemplo se puede observar una operación a nivel columnas (en el eje 1, comportamiento por default), el índice del `Series` se alinea con las columnas del `DataFrame`, de tal forma que a toda la columna _a_ del `df` se le suma 2 y a toda las columna _b_ se le suma 4. Además se puede observar que los índices que no están en los dos objetos (en este caso _c_) también aparecen en el resultado pero con `NaN`.

```{code-cell} ipython3
# Importar libreria
import pandas as pd

# Definir series
x = pd.Series([2, 4, 5], index=['a', 'b', 'c'])

# Definir df
df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})

# Realizar operación a nivel de columnas
print(df.add(x))
```

<br>

---
## Parámetro _axis_

En las funciones y/o métodos que tienen el parámetro _axis_ significa que la función/método se puede aplicar únicamente en un eje determinado, dando como resultado un objeto de una dimensión menor con respecto al número de dimensiones del objeto original. Tomar como referencia la imagen para conceptualizar cómo se aplica la función dependiendo del eje indicado en un `DataFrame`.

```{image} ../images/2d-func-axis.png
:name: axis-2D-func
:width: 300px
:align: center
```
Independientemente del eje indicado el objeto retornado en la mayoría de los casos será un `Series` o un escalar.
- `axis=0` o `'index'`: En este caso se aplica la función a cada colummna a lo largo del índice.
- `axis=1` o `'columns'`: En este caso se aplica la función a cada fila a lo largo de las columnas.

## Tabla de contenido


```{tableofcontents}
````