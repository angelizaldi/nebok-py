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
- índice implícito: Es un índice númerico, que comienza desde cero, similiar a los índices de las secuencias.
- índice explícito: Es el objeto `Index` asociado, que puede tener etiquetas`int` o `str`.

<br>

---
(pandas-series-creacion=)
## Creación de Series

La forma más sencilla de crear un objeto `Series` es con el constructor:

```{list-table}
:header-rows: 1

* - Constructor
  - Descripción
* - [pandas.Series](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series)(data, index, dtype, name, copy, ...)
  - Array unidimensional con etiquetas de eje.
```

**Ejemplo**: A continuación se crea un objeto `Series` cuyos valores son los cuadrados de los números del 1 al 5 y cuyo índice explícito son los nombres de los número del 0 al 4. Además el `Series` llevará por nombre _cuadrados_.

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

---
## Selección de elementos

Existen diversos métodos para seleccionar elementos en un Series. Aquí se explicarán los más comunes. Todos los ejemplos de esta sección utilizará el `Series` definido en (la sección anterior)[pandas-series-creacion=]:


### Como `ndarray`

Todas las estrategias para seleccionar elementos que aplican para `ndarray` de `numpy` funcionan también con `Series` la principal diferencia es que en el caso del `Series` se puede usar tanto los índices implícitos, como los explícitos:

- **Índices implícitos**: 
    - **Subsetting**: Para seleccionar elementos en posiciones específicas.
        - Se utilizan corchetes `[]` para acceder a los elementos, junto con el nombre del `Series` y el índice del elemento. <br/> `X[i]`. 
        - Los índices comienzan en cero (0). 
        - Se puede utilizar índices negativos, para hacer subsetting desde el final al inicio. 
    - **Slicing**: Para seleccionar un rango de elementos consecutivos.
        - Se utiliza dos puntos, indicando los indices de inicio, fin y el paso. <br/> `X[i:j:k]`
        - La selección por rango, tienen la característica que el primer elemento es inclusivo y el último es exclusivo, esto quiere decir que no se incluirá en el rango, si se usa el rango `[m:n]`, en realidad solo se accederá a los índices `[m:n-1]`.
        - En `X[i:j]` Si se omite el índice `i` significa desde el inicio del array y si se omite el índice `j` significa hasta el final del array.
        - Es posible utilizar índices negativos.
    - **Fancy indexing**: Seleccionar elementos de un array en el que se indica por medio de una secuencia los índices ímplicitos a seleccionar. <br> `X[[i1, i2, ...]]` 
    
```{code-cell} ipython3
# Subsetting: Seleccionar 2do elemento -> 2
print(s[1], end="\n"*2)

# Slicing: Seleccionar elementos del 2 al 4 -> 4, 9, 16
print(s[1:4], end="\n"*2)

# Fancy indexing: Seleccionar elementos pares -> 4, 16
print(s[[1, 3]])
```
    
- **Índices explícitos**: 
    - **Subsetting**: Para seleccionar elementos en posiciones específicas.
        - Se utilizan corchetes `[]` para acceder a los elementos, junto con el nombre del `Series` y el índice explícito del elemento. <br/> `X[label]`. 
    - **Subsetting**: Para seleccionar un rango de elementos consecutivos.
        - Se utiliza dos puntos, indicando las etiquetas de inicio y fin. <br/> `X[label1:label2]`. En este caso ambas etiquetas son inclusivas.
    - **Fancy indexing**: Seleccionar elementos de un array en el que se indica por medio de una secuencia los índices explícitos a seleccionar. <br> `X[[labeli, labelj, ...]]` 
    
```{code-cell} ipython3
# Subsetting: Seleccionar 2 elemento ->
print(s['dos'], end="\n"*2)

# Slicing: Seleccionar elementos del 2 al 4 -> 4, 9, 16
print(s['dos':'cuatro'], end="\n"*2)

# Fancy indexing: Seleccionar elementos pares -> 4, 16
print(s[['dos', 'cuatro']])
```

- **Boolean masking**: Seleccionar elementos de un `Series` con base a una secuencia booleana del mismo tamaño, denominada _mask_. Los elementos que tengan posiciones correspondietes en el _mask_ con valores de `True` serán seleccionados, mientras los que tengan valores `False` no serán seleccionados. Normalmente el _mask_ se crea usando al mismo `Series` y [](built-in-operadores-comparacion). <br> `X[comparasión]` 

```{code-cell} ipython3
# Boolean masking: Seleccionar elementos pares
print(s[s%2==0])
```

Ejemplo:
```{code-cell} ipython3
# Subsetting: Seleccionar 2do elemento -> 2
print(s.iloc[1], end="\n"*2)

# Slicing: Seleccionar elementos del 2 al 4 -> 4, 9, 16
print(s.iloc[1:4], end="\n"*2)
```

<br>

---
### Usando método `.loc()`

El método `.loc()` es útil para seleccionar elementos con base al **índice explícito**.

- Para seleccionar un elemento:
    - Se utilizan corchetes `[]` para acceder a los elementos, junto con el nombre del `Series` y el índice explícito del elemento. <br/> `X.loc[label]`. 
- Para seleccionar rangos de elementos continuos:
    - Se utiliza dos puntos, indicando las etiquetas de inicio y fin. <br/> `X.loc[label1:label2]`. En este caso ambas etiquetas son inclusivas.

Ejemplo:
```{code-cell} ipython3
# Subsetting: Seleccionar 2 elemento ->
print(s.loc['dos'], end="\n"*2)

# Slicing: Seleccionar elementos del 2 al 4 -> 4, 9, 16
print(s.loc['dos':'cuatro'], end="\n"*2)
```

<br>

---
### Usando método `.iloc()`

El método `.iloc()` es útil para seleccionar elementos con base al **índice explícito**:

- Para seleccionar un elemento:
    - Se utilizan corchetes `[]` para acceder a los elementos, junto con el nombre del `Series` y el índice del elemento. <br/> `X.iloc[i]` 
    - Los índices comienzan en cero (0). 
    - Se puede utilizar índices negativos, para hacer subsetting desde el final al inicio. 
- Para seleccionar rangos de elementos continuos:
    - Se utiliza dos puntos, indicando los indices de inicio, fin y el paso. <br/> `X.iloc[i:j:k]`
    - La selección por rango, tienen la característica que el primer elemento es inclusivo y el último es exclusivo, esto quiere decir que no se incluirá en el rango, si se usa el rango `[m:n]`, en realidad solo se accederá a los índices `[m:n-1]`.
    - En `X[i:j]` Si se omite el índice `i` significa desde el inicio del array y si se omite el índice `j` significa hasta el final del array.
    - Es posible utilizar índices negativos.

<br><br>

---
## Agregar elementos

Para agregar un elemento a un `Series` se puede simplmente crear una nueva etiqueta y asignarle un valor:
```python
# Agregar 
X['label'] = val
```

<br><br>

---
## Métodos y atributos

A continuación se enlistan los links a la documentación oficial de `pandas` para consultar los métodos y atributos de `Series`.

- **Atributos:**
    - [Atributos](https://pandas.pydata.org/docs/reference/series.html#attributes)
- **Métodos:**
    - [Conversión](https://pandas.pydata.org/docs/reference/series.html#conversion)
    - [Iteración/Indexación](https://pandas.pydata.org/docs/reference/series.html#indexing-iteration)
    - [Operadores binarios](https://pandas.pydata.org/docs/reference/series.html#binary-operator-functions)
    - [Funciones de apply, aggregates, groupby y window](https://pandas.pydata.org/docs/reference/series.html#function-application-groupby-window)
    - [Cálculos y estadísticas descriptivas.](https://pandas.pydata.org/docs/reference/series.html#computations-descriptive-stats)
    - [Reindexación, selección y manipulación de etiquetas](https://pandas.pydata.org/docs/reference/series.html#reindexing-selection-label-manipulation)
    - [Datos perdidos](https://pandas.pydata.org/docs/reference/series.html#missing-data-handling)
    - [Reshaping y ordenar](https://pandas.pydata.org/docs/reference/series.html#reshaping-sorting)
    - [Comparar y combinar](https://pandas.pydata.org/docs/reference/series.html#combining-comparing-joining-merging)
    - [Series de tiempo](https://pandas.pydata.org/docs/reference/series.html#time-series-related)
    - [Gráficas](https://pandas.pydata.org/docs/reference/series.html#plotting)
    - [IO, conversión y serialización](https://pandas.pydata.org/docs/reference/series.html#serialization-io-conversion)
 
<br><br>

---  
## Accesors

Los _accesors_ permiten acceder a métodos adicionales para `Series` de algún tipo de dato concreto. Existen 4 tipos de _accesors_:


|Data Type| Accessor|
|---|---|
|`datetime`, `timedelta`,`period`| dt|
|`string` |str|
|`categorical`| cat|
|`sparse` | sparse |

Para conocer los métodos visitar los siguientes links:
- **dt**:
    - [Propiedades de datetime](https://pandas.pydata.org/docs/reference/series.html#datetime-properties)
    - [Métodos de datetime](https://pandas.pydata.org/docs/reference/series.html#datetime-methods)
    - [Propiedades de period](https://pandas.pydata.org/docs/reference/series.html#period-properties)
    - [Propiedades de timedelta](https://pandas.pydata.org/docs/reference/series.html#timedelta-properties)
    - [Métodos de timedelta](https://pandas.pydata.org/docs/reference/series.html#timedelta-methods)
- **str**:
    - [Cadenas](https://pandas.pydata.org/docs/reference/series.html#string-handling)
- **cat**:
    - [Categóricos](https://pandas.pydata.org/docs/reference/series.html#categorical-accessor)
- **sparse**
    - [Sparse](https://pandas.pydata.org/docs/reference/series.html#sparse-accessor)



