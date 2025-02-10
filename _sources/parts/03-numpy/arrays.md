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


# Arrays

Los _arrays_ correspondientes al tipo `ndarray` son objetos que pueden almacenar distintos valores del mismo tipo de dato en _n_ dimensiones. El objeto `ndarray` permite hacer calculos vectorizados (elemento con elemento) de manera similar a los vectores en _R_. Algunas de sus características son:
- **Tipos de dato homogéneos**: Todos los elementos de un `ndarray` deben de ser del mismo tipo. Para ver los tipos de datos que se admiten revisar {ref}`numpy-tipos-datos`.
- **Es mutable**: Sus elementos se pueden modificar una vez creado.
- **Está indexado**: Cada elemento está asociado con un índice y por lo tanto sus elementos están ordenados.
- **Es un iterable**: Se puede iterar por sus elementos y se puede usar la palabra reservada `in` para verificar membresía.
- Los _arrays_ pueden tener varias dimensiones:
    - Cero (escalar): Es un _array_ con solo un elemento.
    - Uno (vector) : Es un _array_ con más de un elemento. Es recomendado interpretarlo como un vector horizontal
    - Dos (matriz): Es un _array_ bidimensional. Se podría considerar como un vector donde cada elemento es a su vez otro vector (vertical).
    - Tres o más (tensor): Son _arrays_ de tres o más dimensiones. En el caso de 3D, se podría interpretar como una matriz donde cada elemento es un vector que se extiende en la profundidad.

```{image} ../images/arrays-sizes.png
:name: arrays-types
:width: 500px
:align: center
```

:::{note}
Para conceptualizar _arrays_ de 4 dimensiones o más considerar:
- 4D: Un arreglo de 4 dimensiones es un vector horizontal donde cada elemento es un _array_ 3D.
- 5D: Un arreglo de 5 dimensiones es una matriz donde cada elemento es un _array_ 3D.
- 6D: Un arreglo de 6 dimensiones es un tensor 3D donde cada elemento es un _array_ 3D.
- 7D+: Aplicar la misma lógica anterior para conceptualizar _arrays_ de más dimensiones.
:::

<br/><br/>

---
## Creación de arrays

Existen diversas formas de crear _arrays_. 
1. {ref}`seq-to-array`, usando la función `np.array()`.
2. {doc}`Funciones <creacion-arrays>` de `numpy` para crear `ndarray`.
3. {ref}`concatenacion`.
4. Importar datos desde un sitio externo o desde un archivo local con {doc}`Funciones <lectura-escritura>` de `numpy`. 
5. Creación de matrices a partir de bytes sin procesar mediante el uso de cadenas o búferes. [Más información](https://numpy.org/doc/stable/user/basics.creation.html#creating-arrays-from-raw-bytes-through-the-use-of-strings-or-buffers)
6. Otras funciones de otras librerias para crear arrays.  [Más información](https://numpy.org/doc/stable/user/basics.creation.html#use-of-special-library-functions-e-g-scipy-pandas-and-opencv).

:::{note}
Para más información sobre creación de _arrays_ visitar la [Guía de usuario](https://numpy.org/doc/stable/user/basics.creation.html#array-creation) de `numpy`.
:::

<br/>

(seq-to-array)=
### Convertir secuencia a array

Cualquier objeto de Python que sea una secuencia se puede convertir a un objeto `np.ndarray` con la función `numpy.array()`:

```python
# Importar librería
import numpy as np

# Convertir X a ndarray
a = np.array(X)
```
- _X_ \- `sequence`: Cualquier objeto de Python que sea una secuencia (`list`, `tuple`, `str` o `range`). 

:::{tip}
Para ver cómo indicar el tipo de dato del _array_ al crearlo revisar {ref}`numpy-tipo-datos-array`.
:::

<br/>

Al convertir una secuencia anidada tener en cuenta las siguientes consideraciones. Se utilizará `list` como ejemplo.

- Una lista simple se convertirá en un _array_ 1D.
- Una lista anidada de dos niveles será un _array_ 2D. Tener en cuenta lo siguiente:
    - Cada lista interna representa una fila. Por ejemplo, en la imagen hay dos listas internas (corchetes cafés <span style="color: #ba6a30">■</span>), y por lo tanto el _array_ tendrá dos filas.
    - Los elementos de las listas internas representan los elementos de las columnas de su respectiva fila. En la imagen, cada lista tiene 2 elementos, por lo tanto cada fila tendrá dos columnas.

<br/>

```{image} ../images/2d-anidado.png
:name: nested-2d-list
:width: 400px
:align: center
```

<br/>

- Una lista anidada de 3 niveles será un _array_ 3D. Tener en cuenta lo siguiente.
    - Las listas de color café <span style="color: #ba6a30">■</span> representan "rebanadas" del cubo, como hay dos listas de este tipo, entonces hay dos rebanadas.
    - Las listas de color verde <span style="color: #98BA30">■</span> representan las filas. En cada rebanada hay dos listas de este tipo, por lo tanto cada rebanada tiene filas columnas.
    - Los elementos de listas de color verde <span style="color: #98BA30">■</span> representan las columnas. En la imagen, cada lista de color verde <span style="color: #98BA30">■</span> tiene 2 elementos, por lo tanto cada fila tendrá dos columnas.

```{image} ../images/3d-anidado.png
:name: nested-3d-list
:width: 400px
:align: center
```

<br/><br/>

---
## Vectorización

La principal ventaja de los arreglos de `numpy` frente a otras estructuras estándar de Python como las listas, es que los objetos `ndarray` permiten realizar operaciones vectorizadas, como operaciones aritméticas y de comparación entre arreglos con escales y con otros arreglos. Algunos ejemplos son:

```{code-cell} ipython3
# Importar librería
import numpy as np

# Definir el array
X = np.array(range(1, 6))

# Multiplicacion escalar por array
Y = 2 * X
print(f"Multiplicación escalar: {Y}", end='\n'*2)

# Suma entre dos arreglos
print(f"Suma vectorizada: {X+Y}", end='\n'*2)

# Comparación entre arreglo y escalar
print(f"Comparación: {X%2 == 0}") 
```
- Es posible operar entre escalares y arreglos o entre arreglos y otros arreglos, incluso de diferentes tamaños, con la mayoría de los {doc}`operadores <../01-built-in/operadores-palabras>`.
- Las operaciones entre arreglos de diferentes tamaños es posible (aunque con limitaciones) gracias al {ref}`numpy-arrays-broadcasting`.

<br/><br/>

---
## Copias y views

Al manipular o realizar determinadas acciones con _arrays_ es posible que se retorna una copia o una _view_ del mismo.
- Una copia de un _array_ retorna un objeto nuevo con la misma información que el original, de manera que modificaciones en el nuevo objeto (la copia), no afectan al objeto con el que se hizo la copia (el original). 
- Una _view_ comparte los mismos datos con el objeto original, por que lo que modificaciones en el _view_, sí afectan al objeto  original, sin embargo es posible modificar el _shape_ o el tipo de dato (`dtype`) en el _view_ sin modificar los mismos en el objeto original. En esencia únicamente comparten los mismos datos, pero pueden diferir en otros atributos.

Se pueden crear copias y _views_ de los objetos `ndarray` con los métodos `.copy()` y `.view()`

```python
# Definir un array
X = np.array(range(1, 10)).reshape((3, 3))

# Crear una copia de X
Y = X.copy()

# Crear una view de X
Z = X.view()
```
- Revisar el _warning_ para ver otras opciones de crear una copia de un objeto `ndarray`.

:::{note}
Aunque una _view_ comparte los datos con el objeto original se consideran dos objetos diferentes e independientes. Incluso cada uno tiene su propio _id_, pero los datos subyacentes comparten la misma memoria.
:::

```{warning}
Si _X_ es un `ndarray` y sea crea otro arreglo _W_ usando `W = X`, entonces _W_ es una referencia a _X_, es decir _W_ es el mismo objeto _X_ pero con otro nombre, por lo que modificaciones en _W_ también afectarán a _X_ y viceversa. Notar que _W_ **no** es una _view_ de _X_, en esencia son el mismo objeto. Para que esto no suceda usar cualquiera de los siguientes opciones para crear una copia de _X_:
- `W = X.copy()`
- `W = X[:]`
- `W = np.array(X)`
- `np.copyto(W, X)`

De esta manera modificaciones en _W_ no afectarán a _X_ y viceversa. No se debe usar `W = X.view()` por en este caso modificaciones en uno sí modificarán el otro objeto.
``` 

Para verificar si un objeto es una _view_ utilizar el atributo `ndarray.base`.
```python
# Verificar si X es una view
X.base
```
- Si _X_ es una view entonces se retornará el objeto al que _X_ hace referencia, en caso contrario, se retornará `None`, es decir, no se retornará nada.

<br/>

Algunas operaciones comunes que retornan _views_ son:
- {ref}`numpy-arrays-slicing`.
- {ref}`numpy-arrays-masking`.
- {ref}`numpy-arrays-indexing`.
- {ref}`numpy-arrays-reshaping`.
- El atributo `ndarray.T`, es decir, transponer el _array_.

```{warning}
Si _x_ es una lista y sea crea otra lista _y_ usando `Y = X`, entonces modificaciones en _y_ también afectarán a _x_ y viceversa. Para que esto no suceda usar cualquiera de los siguientes opciones:
- `Y = list(X)`
- `Y = X[:]`
- `Y = X.copy()`

De esta manera modificaciones en _y_ no afectarán a _x_ y viceversa.
``` 

<br/>

---

(numpy-arrays-seleccion)=
## Selección de elementos

Existen diversos métodos para seleccionar elementos de un _array_.

<br/>

```{image} ../images/axis-3D.png
:name: axis-3D
:width: 300px
:align: center
```

<br/>

Para identificar los índices de los elementos de un _array_ tomar como referencia la imagen para _arrays_ 1D, 2D y 3D, las flechas indican la dirección en que los índices van aumentando en su respectivo eje. Como regla general, dimensiones extras se convierten en el eje 0, de tal forma que tenemos:
- **1D**: (axis 0).
- **2D**: (axis 0, axis 1).
- **3D**: (axis 0, axis 1, axis 2).
- **4D**: (axis 0, axis 1, axis 2, axis 3).
- Generalizar para dimensiones superiores.

<br/>

---
(numpy-arrays-indexing)=
### Indexing

_Indexing_ se refiere a seleccionar elementos en índices específicos.

```{image} ../images/index-arrays.png
:name: arrays-indexing
:width: 500px
:align: center
```

<br/>

Al seleccionar elementos por índices tomar en cuenta las siguientes características.

- Se utilizan corchetes `[]` para acceder a los elementos, junto con el nombre del _array_ y el índice del elemento: <br/> `X[i]`
- Los índices comienzan en cero (0), esto quiere decir que si quiere acceder al elemento en la posición _n_, se debe de usar el índice `[n-1]`.
- Se puede utilizar índices negativos, para hacer indexing desde el final al inicio. Por ejemplo, se puede acceder al último elemento con `[-1]`, al penúltimo elemento con `[-2]`, etc.
- Para _arrays_ de dos dimensiones o más separar los índices de cada dimensión con coma, donde el primer elemento corresponde a la dimensión 1 (axis 0), el segundo a la dimensión 2 (axis 1), etc. <br/> `X[i, j, k, ...]`
- Se puede omitir el índice de la última dimensión, para seleccionar todos los elementos en esa última dimensión, por ejemplo, si _X_ es 2D entonces `X[k]` o `X[k,]` selecciona toda la fila en el índice _k_.

Algunos patrones útiles en 1D:
- El primer elemento: <br/> `X[0]`
- El elemento _n_: <br/> `X[n-1]`
- El último elemento: <br/> `X[-1]`

<br/>

**Ejemplo 1D**

```{code-cell} ipython3
# Importar librería
import numpy as np

# Definir el array
X = np.array(["a", "b", "c", "d", "e"])

# Seleccionar primer elemento, i.e, el índice 0 -> "a"
print(f"Elemento 1: {X[0]}", end='\n'*2)

# Seleccionar el elemento 3, i.e, el índice 2 -> "c"
print(f"Elemento 3: {X[2]}", end='\n'*2)

# Seleccionar último elemento -> "e"
print(f"Último elemento: {X[-1]}") 
```

<br/>

Algunos patrones útiles en 2D:
- Elemento en la fila _i_ y la columna _j_: <br/> `X[i-1, j-1]`
- Toda la fila _i_: <br/> `X[i-1]` <br/> `X[i-1,]`

**Ejemplo 2D**

```{code-cell} ipython3
# Importar librería
import numpy as np

# Definir el array
X = np.array([["a", "b"],
              ["c", "d"]])

# Seleccionar fila 1 y columna 2 -> "b"
print(f"Fila 1, columna 2: {X[0, 1]}", end='\n'*2)

# Seleccionar toda la fila 2 -> ["c", "d"]
print(f"Fila 2: {X[1,]}")
```

:::{note}
Es posible combinar _indexing_ con otras estrategías para seleccionar elementos como _boolean masking_, _fancy indexing_ o _slicing_ para diferentes dimensiones del arreglo. Por ejemplo, para seleccionar la columna _j_ completa se puede combinar _indexing_ y _slicing_ de la siguiente manera: <br/> `X[:,j-1]`
:::

<br/>

---
(numpy-arrays-slicing)=
### Slicing

_Slicing_ se refiere a seleccionar rangos de elementos contiguos en índices específicos.

Para seleccionar un rango de elementos consecutivos tener en cuenta las siguientes características:
- Se utiliza dos puntos, indicando los indices de inicio, fin y el paso: <br/> `X[start:stop:step]`
- La selección por rango, tienen la característica que el primer elemento (_start_) es inclusivo y el último (_stop_) es exclusivo, esto quiere decir que no se incluirá en el rango, si se usa el rango `[m:n]`, en realidad solo se accederá a los índices `[m:n-1]`.
- En `X[i:j]`:
    - Si se omite el índice _i_ significa desde el inicio del _array_.
    - Si se omite el índice _j_ significa hasta el final del _array_.
    - Si se omiten ambos significa todo el _array_. 
- También es posible utilizar índices negativos.
- Para _arrays_ de dos o más dimensiones, separar con coma el slice de cada dimensión: <br/> `X[start:stop:step, start:stop:step, ...]`.

:::{warning}
Si _X_ es `ndarray` y sea crea otro _array_ _Y_ usando `Y=X[i:j]`, entonces _Y_ será una _view_ de _X_ y modificaciones en _Y_ también afectarán a _X_ y vicerversa. Para que esto no suceda usar:
- `Y = X[i:j].copy()`

De esta manera modificaciones en _Y_ no afectarán a _X_ y viceversa.
:::

:::{Note}
Al seleccionar filas o columnas completas de un _array_ 2D la forma como se haga la selección modificará el _shape_ del objeto retornado. 

Por ejemplo, si _X_ es un _array_ con _shape_ _(3, 3)_ y se desea seleccionar toda la segunda fila, existen diversas formas de hacerlo:
- `X[1]` o `X[1,]` retornan un _array_ de _shape_ (3,), es decir, un _array_ 1D.
- `X[1, :]` retorna un _array_ de _shape_ (3,), es decir, un _array_ 1D.
- `X[1:2, :]` retorna un _array_ de _shape_ (1, 3), es decir, un _array_ 2D.

Por lo tanto si se desea retornar un _array_ 2D en lugar de 1D, se debe usar _slices_ en ambas dimensiones, en caso contrario se retornará un _array_ 1D.
:::

Algunos patrones útiles en **1D**:
- Desde el índice _i_ hasta el _j_, sin incluir el _j_: <br/> `X[i:j]`
- Desde el inicio hasta el _j_, sin incluir el _j_: <br/> `X[:j]`
- Desde la posición _i_ hasta el final: <br/>`X[i:]`
- Todo el _array_: <br/> `X[:]`
- Desde el índice _i_ hasta el _j_, sin incluir el _j_, cada _k_ elementos: <br/> `X[i:j:k]`
- Todo el _array_ cada _k_ elementos: <br/> `X[::k]`
- Todo el _array_ al revés: <br/> `X[::-1]`

```{image} ../images/patrones-1D.png
:name: patrones-1D
:width: 500px
:align: center
```
<br/>

Algunos patrones útiles en **2D**:
- Primeras _n_ filas y primeras _m_ columnas: <br/> `X[:n, :m]`
- Seleccionar la columna en el índice _j_, para todas las filas: <br/> `X[:, j]`
- Seleccionar todas las columnas excepto la última, para todas las filas: <br/> `X[:, :-1]`
- Seleccionar la última columna, para todas las filas: <br/> `X[:, -1]`
- Seleccionar la fila en el índice _i_, para todas las columnas: <br/> `X[i, :]`
- Seleccionar las primeras _k_ filas de todas las columnas: <br/> `X[:k, :]`
- Seleccionar todas las filas después de la fila _k_ de todas las columnas: <br/> `X[k:, :]`

```{image} ../images/patrones-2D.png
:name: patrones-2D
:width: 400px
:align: center
```

<br/>

Algunos patrones útiles en **3D**:
- Seleccionar toda una fila, para todas las columnas, de una "rebanada" específica: <br/> `X[k, i, :]`
- Seleccionar toda una columna, para todas las filas, de una "rebanada" específica: <br/> `X[k, :, j]`
- Seleccionar un elemento para una fila y una columna específica de todas las "rebanadas": <br/> `X[:, i, j]`
- Seleccionar todas las filas y todas las columnas de una "rebanada" específica: <br/> `X[k, :, :]`

```{image} ../images/patrones-3D.png
:name: patrones-3D
:width: 400px
:align: center
```

:::{tip}
Para arreglos multidimensionales de 4D o más es de utilidad utilizar la literal `...` o la constante `Ellipsis` para indicar que se expandan a tantos _slicings_ (`:`) como sean necesarios para completar las dimensiones que faltan. Por ejemplo, si se tiene un array 4D con _shape_ _(blocks, depth, rows, columns)_, entonces:
- `X[..., j]` equivale a `X[:, :, :, j]`
- `X[b, ..., j]` equivale a `X[b, :, :, j]`
- `X[b, ...]` equivale a `X[b, :, :, :]`

Para más información del uso de la _ellipsis_ para _slicing_ visitar {ref}`const-ellipsis-slicing`.
:::

:::{note}
Es posible combinar _slicing_ con otras estrategías para seleccionar elementos como _boolean masking_, _fancy indexing_ o _indexing_ para diferentes dimensiones del arreglo.
:::

<br/>

---
(numpy-arrays-masking)=
### Boolean masking

_Boolean masking_ se refiere a seleccionar elementos de un _array_ con base a otro _array_ booleano del mismo tamaño, denominado _mask_. Los elementos que tengan posiciones correspondietes en el _mask_ con valores de `True` serán seleccionados, mientras los que tengan valores `False` no serán seleccionados. 

:::{note}
El _array_ retornado al seleccionar elementos por _boolean masking_ siempre será de una dimensión.
:::

:::{warning}
El _array_ retornado al seleccionar elementos por _boolean masking_ será un _view_ del _array_ original.
:::

Se pueden crear masks usando comparaciones vectorizadas con el _array_. Para comparaciones más complejas se pueden usar los [operadores bitwise](https://nebok-py.com/parts/01-built-in/anexos-operadores-palabras.html#bitwise). También es posible crear listas para hacer el mask, por ejemplo, usando [list comprehession](https://nebok-py.com/parts/01-built-in/listas.html#list-comprehension).

```python
# Boolean masking simple
X[mask]

# Boolean masking usando &
X[(mask1) & (mask2)]

# Boolean masking usando |
X[(mask1) | (mask2)]
```
- _mask_ es un `array-like` boolenado de las mismas dimensiones que _X_. Usualmente se construye utilizando al mismo vector _X_ y [operadores de comparación](https://nebok-py.com/parts/01-built-in/anexos-operadores-palabras.html#comparacion), [identidad](https://nebok-py.com/parts/01-built-in/anexos-operadores-palabras.html#identidad) o [membresía](https://nebok-py.com/parts/01-built-in/anexos-operadores-palabras.html#membresia), o en general, cualquier expresión que resulte en un _array_ booleano del mismo tamaño que _X_. 
- Notar que si se tienen 2 o más condiciones, cada condición se debe poner entre `()`.

:::{warning}
No utilizar los operadores lógicos `and`, `or` o `not` para hacer combinar los _masks_.
:::

<br/>

**Ejemplo**: A continuación se muestra dos ejemplos sencillos de cómo crear _boolean masks_.

```{code-cell} ipython3
# Definir el array
X = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

# Mask simple
print(f"Elementos menores que 5: {X[X<5]}")

# Mask usando &
print(f"Número pares mayores a 5: {X[(X%2 == 0) & (X>5)]}")
```

:::{note}
Es posible combinar _boolean masking_ con otras estrategías para seleccionar elementos como _slicing_, _fancy indexing_ o _indexing_ para diferentes dimensiones del arreglo.
:::

<br/>

---
(numpy-arrays-fancy-indexing)=
### Fancy Indexing

_Fancy indexing_ es una estrategia para seleccionar elementos de un _array_ en el que se indica por medio de un `array-like` los índices a seleccionar, de tal forma que se seleccionan los elementos que están en los índices del _array-like_. 

:::{note}
El _array_ retornado al seleccionar elementos por _fancy indexing_ usualmente será de una dimensión si se utiliza un `list-like`. Si se desea que el _array_ retornado tenga un _shape_ determinido se puede usar un `ndarray` con un determinado _shape_ como se verá más adelante.
:::

:::{warning}
El _array_ retornado al seleccionar elementos por _fancy indexing_ será un _view_ del _array_ original.
:::

**Ejemplo**

```{code-cell} ipython3
# Definir el array
X = np.array(["a", "e", "i", "o", "u"])

# Una lista con los índices a seleccionar
ind = [2, 0, 4, 0]

# Aplicar la lista -> ["i", "a", "u", "a"]
print(X[ind])
```
- Los índices en _ind_ pueden estar en cualquier orden, incluso se puede repetir más de una vez un mismo índice.

Se puede usar un `np.ndarray` que tenga un _shape_ específico y el _array_ devuelto tendrá ese mismo _shape_. Esto solo funciona si el objeto que se usa para hacer _fancy indexing_ es `np.ndarray`.

```{code-cell} ipython3
# Definir el array
X = np.array(["a", "e", "i", "o", "u"])

# Un array con los índices a seleccionar
ind = np.array([[2, 0], [4, 0]])

# Aplicar el array -> [["i", "a"], ["u", "a"]]
print(X[ind])
```

En **dos dimensiones** tener en cuenta lo siguiente:
- Si se pasa un _array_ 1D entonces se hará _fance indexing_ solo de las filas. Retornando un _array_ 2D.
- Se puede pasar una lista/_array_ con los índices de las filas y otra/o con los índices de las columnas por separado, los elementos se empatan por posición. Lo mismo se puede generalizar para _arrays_ de más dimensiones.

```{code-cell} ipython3
# Definir el array
X = np. array([[0, 1, 2, 3],
               [4, 5, 6, 7],
               [8, 9, 10, 11]])
           
# Definir arrays para indexar  
row = np.array([0, 1, 2])
col = np.array([2, 1, 3])

# Aplicar los índices a seleccionar -> array([ 2,  5, 11])
print(X[row, col])
```

:::{note}
Es posible combinar _fancy indexing_ con otras estrategías para seleccionar elementos como _slicing_, _boolena masking_ o _indexing_ para diferentes dimensiones del arreglo.
:::

<br/>

---
## Modificar elementos

Para modificar elementos de un _array_ se puede utilizar cualquier estrategia de {ref}`numpy-arrays-seleccion` y asignar nuevos valores:

```python
# Modificar un elemento, ejemplo con indexing
myarray[i] = val

# Modificar múltiples elementos con el mismo valor, ejemplo con slicing
myarray[i:j] = val

# Modificar múltiples elementos con valores diferentes, ejemplo con slicing
myarray[i:j] = [val_i, ..., val_j] 
```
- Si se van a asignar múltiples valores diferentes tener en cuenta lo siguiente:
    - El objeto que asigne debe ser de tipo `array-like`.
    - Se deben asignar el mismo número de elementos que los que se están seleccionando.
    - Es técnicamente posible asignar múltiples valores por medio de _boolean masking_, pero no es recomendado ya que es necesario saber con anticipación cúantos elementos serán seleccionados.
- **Importante**: Se puede usar cualquier operador de {ref}`built-in-operadores-asignacion`, no solo `=`, por ejemplo: <br/> `myarray[i:j] += val # Ejemplo con += y fancy indexing`

<br/>

---
(numpy-arrays-reshaping)=
## Reshaping


Se refiere a modificar el _shape_ de un _array_, ya sea modificando el número de dimensiones o modificando el número de elementos en cada dimensión. Existen dos formas principales para realizar esta acción, con el método `.reshape()` o con `np.newaxis` los cuales se revisan más adelante. También es posible utilizar el atributo `.shape`

```{admonition} Info
El _shape_ de un _array_ indica el número de elementos que hay en cada dimensión del arreglo, se suele representar como un `tuple`, donde el primer elemento es el número de elementos en el eje 0, el segundo el número de elementos en el eje 1, etc. <br/> _(n, m, p, ...)_
```

:::{tip}
Para más opciones de hacer _reshape_ de un _array_ consultar los métodos {ref}`manipulacion-shape` y las funciones {doc}`manipulacion-arrays`.
:::

Para revisar el _shape_ actual de un _array_ usar el atributo `ndarray.shape`

```python
# Ver el shape del array X
X.shape
```
- Este atributo retorna un `tuple` con el número de elementos en cada dimensión.
- Es atributo también se puede utilizar para modificar el _shape_ del arreglo, simplemente se debe de asignar a un `tuple` con las dimensiones deseadas, cuidando que sea _shape_ válido.

:::{note}
La diferencias entre los _arrays_ con _shape_ _(n,)_ y los _arrays_ con _shape_ _(n, 1)_ o _(1, n)_, son las siguientes:
- Los arreglos con _shape_ _(n,)_ son arreglos 1D. Son una secuencia de elementos ordenados.
- Los arreglos con _shape_ _(n, 1)_ son arreglos 2D. Se podrían interpretar como una columna de una matriz.
- Los arreglos con _shape_ _(1, n)_ son arreglos 2D. Se podrían interpretar como una fila de una matriz.

```{image} ../images/1d-vs-2d.png
:name: 1d-vs-2d
:width: 300px
:align: center
```
:::

<br/>

(reshape)=
### Método _reshape_

El método `ndarray.reshape()` se usa para modificar el _shape_ de un _array_.
```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [reshape](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.reshape.html)(shape[, order])
  - Devuelve un arreglo que contiene los mismos datos con un nuevo _shape_.
```
- _shape_ - `tuple`: Indica la cantidad de elementos en cada dimensión que se desea que tenga el _array_.
    - Si el _array_ tiene _k_ elementos, entonces la multiplicación del número de elementos en cada una de las nuevas dimensiones debe ser igual a _k_.
- _order_ - {'C', 'F', 'A'}: Indica el orden de cómo leer los elementos del _array_. 

:::{warning}
El método `ndarray.reshape()` retorna _views_ en lugar de copias en la mayoría de los casos.
:::

**Algunos reshapes cómunes**:

:::{attention}
Todos los ejemplos de esta sección muestran reshapes con `order=C`. Existe otra forma en la que se ordenan los elementos al hacer el reshape que corresponde al orden _F_. Tomar como referencia las imágenes para conceptualizar como se transforman los _arrays_ de un _shape_ a otro.
:::

**Cualquier dimensión a 1D**: Si se quiere modificar un _array_ de cualquier dimensión a 1D usar:

```python
# Convertir X a 1D
X.reshape(-1)
```
- En lugar de usar -1, se podría poner el número de elementos total _k_ que tiene _X_.

:::{tip}
Existen métodos para convertir cualquier dimensión a 1D:
- `ndarray.flatten()`: Retorna una copia del _array_ en 1D.
- `ndarray.ravel()`: Retorna una _view_ del _array_ en 1D.

Para más información consultar {ref}`manipulacion-shape`.
:::

<br/>

**1D a 2D**: Si se quiere cambiar el _shape_ de un _array_ de 1D a 2D usar:

```python
# Convertir a vector columna
X.reshape((-1, 1)) # Equivale a X.reshape((k, 1))

# Convertir a vector fila
X.reshape((1, -1)) # Equivale a X.reshape((1, k))

# Convertir a matriz (m, n)
X.reshape((m, n))
```
- _k_ es el número de elementos en el _array_ _X_.
- Es importante considerar que $m*n=k$, es decir, la multiplicación del número de filas $m$ por el números de columnas $n$ debe ser igual al número de elementos $k$.

```{image} ../images/1D-a-2D.png
:name: 1D-a-2D
:width: 300px
:align: center
```

<br/>

**1D a 3D**: Si se quiere cambiar el _shape_ de un _array_ de 1D a 3D usar:

```python
# Convertir a una fila de un "cubo"
X.reshape((-1, 1, 1)) # Equivale a X.reshape((k, 1, 1))

# Convertir a una columna de un "cubo"
X.reshape((1, -1, 1)) # Equivale a X.reshape((1, k, 1))

# Convertir a una fila en la profundidad de un "cubo"
X.reshape((1, 1, -1)) # Equivale a X.reshape((1, 1, k))

# Convertir a tensor 3D
X.reshape((m, n, p))
```
- _k_ es el número de elementos en el _array_ _X_.
- Es importante considerar que $m*n*p=k$, es decir, la multiplicación del número de filas $m$ por el números de columnas $n$ por la profundidad $p$ debe ser igual al número de elementos $k$.
- Usar la siguiente imagen como referencia, para identificar cómo se construye un _array_ 3D a partir de un _array_ 1D.

```{image} ../images/1D-a-3D.png
:name: 1D-a-3D
:width: 400px
:align: center
```

<br/>

**2D a 3D**: Si se quiere cambiar el _shape_ de un _array_ de 2D a 3D usar:
```python
# Convertir matriz a tensor
X.reshape((m, n, 1))

# Convertir matriz a tensor en dimensiones específicas
X.reshape((m, n, p))
```

```{image} ../images/2D-a-3D.png
:name: 2D-a-3D
:width: 400px
:align: center
```

<br/>

---
### Usando np.newaxis

Se puede utilizar `np.newaxis` para modificar el _shape_ de un _array_, para ello se pone `np.newaxis` en la dimensión que se quiere agregar entre corchetes, como si se hiciera _slicing_. Esta forma de modificar el _shape_ de una _array_ es útil cuando se desea modificar el número de dimensiones, pero no agregar elementos en esas nuevas dimensiones.

```{image} ../images/2D-a-3D-2.png
:name: 2D-a-3D-2
:width: 400px
:align: center
```

:::{note}
Usar `np.newaxis` equivale a usar un "1" en el método `ndarray.reshape()`.
:::

**1D a 2D**: Si se quiere cambiar el _shape_ de un _array_ de 1D a 2D usar:

```python
# Convertir a vector columna
X[:, np.newaxis] # Equivale a X.reshape((-1, 1))

# Convertir a vector fila
X[np.newaxis, :] # Equivale a X.reshape((1, -1))
```

**2D a 3D**: Si se quiere cambiar el _shape_ de un _array_ de 2D a 3D usar:
```python
# Convertir matriz (m, n) a tensor 3D
X[:, :, np.newaxis] # Equivale a X.reshape((m, n, 1))
```

<br/><br/>

---
(numpy-arrays-broadcasting)=
## Broadcasting

Se refiere al ajuste que se hace en las dimensiones y/o el número de elementos de un _array_ cuando se hacen operaciones vectorizadas entre _arrays_ de distintas dimensiones y/o número de elementos en una misma dimensión. El _array_ de menor dimensión se ajustará al de mayor dimensión. Existen algunas reglas para que se pueda hacer el broadcasting:

:::{note}
Como tal estos cambios en el _shape_ de los _arrays_ no ocurren en la práctica, pero es útil para conceptualizar cómo se realizan las operaciones vectorizadas.
:::

- **Número de dimensiones**: Si dos _arrays_ difieren en el número de dimensiones, a aquel con menos dimensiones, se le aumentará el número de dimensiones, desde la izquierda, hasta que coincida con el número de dimensiones del otro _array_. Por ejemplo, si se quiere hacer una operación entre un _array_ 1D _(k,)_ y uno 3D _(k, m, n)_, entonces, el 1D se convertirá en _(1, 1, k)_ para que concidan en el número de dimensiones.

```{image} ../images/broadcasting-1.png
:name: broadcasting-1
:width: 400px
:align: center
```

<br/>

- **Número de elementos**: Para cada dimensión en ambos _arrays_, si el número de elementos difieren en esa dimensión y al menos uno de los _arrays_ tiene un único elemento en esa dimensión, entonces ese elemento se duplica a lo largo de esa dimensión para que coincida con el número de elementos del otro _array_. Por ejemplo, si se tienen dos _arrays_ con _shape (k, m, n)_ y _(1, 1, n)_, los _arrays_ coinciden en el número de elementos solo en el eje 3, y el segundo _array_ solo tiene un elemento en el eje _1_ y _2_, por lo que esos elementos se duplicarán a lo largo de esa dimensión para que concidan con _k_ y _m_ respectivamente, de tal forma que se convierta en _(k, m, n)_.

```{image} ../images/broadcasting-2.png
:name: broadcasting-2
:width: 400px
:align: center
```

<br/>

- Si los _arrays_ en alguna dimensión no coinciden en el número de elementos y ninguno de los _arrays_ tiene un único elemento en esa dimensión, entonces no se podrá realizar la operación entre esos _arrays_ y se arrojará un error. Por ejemplo, los _arrays_ con _shape (3, 2)_ y _(2, 3)_ arrojarán un error si se trata de realizar operaciones vectorizadas con ellos.

<br/>

Como resumen, veamos el siguiente ejemplo:

```{code-cell} ipython3
# Definir el array 1
X = np. array([[1, 1, 1],
               [2, 2, 2]])
               
# Definir el array 2
Y = np. array([1, 2, 3])
           
# Multiplicar ambos arrays
print(X*Y)
```

Lo cual se puede representar como:

```{image} ../images/broadcasting-ejm-1.png
:name: broadcasting-ejm-1
:width: 500px
:align: center
```

<br/>

Tener en cuenta que:
1. Lo primero que se hace es hacer que ambos _arrays_ tengan el mismo número de dimensiones, es decir, se convierte _(3,)_ a _(1, 3)_.
2. Posteriormente, como los _arrays_ difieren en el número de elementos en el eje 0, entonces se duplican los elementos a lo largo de ese eje para pasar de _(1, 3)_ a _(2, 3)_. 

De esta forma ya se puede hacer una multiplicación _element-wise_ entre ambos _arrays_.

```{image} ../images/broadcasting-ejm-2.png
:name: broadcasting-ejm-2
:width: 500px
:align: center
```

<br/><br/>

---
(concatenacion)=
## Concatenación y apilación de arrays

Existen dos técnicas principales para unir _arrays_, concatenación y apilación:

:::{note}
Para más información sobre las funciones de concatenación y apilación en esta sección visitar {ref}`numpy-func-manipulacion-concat-stack`.
:::

**Concatenación**: 

- Se utiliza la función `np.concatenate()`.
- En concatenación los _arrays_ se unen en **ejes existentes**. Es decir, preservan el número de dimensiones.
- En 1D solo se puede concatenar sobre el eje 0, en 2D sobre los eje 0 y 1, en 3D sobre los ejes 0, 1 y 2, etc.
- Los _arrays_ deben de tener el mismo número de elementos en los ejes, excepto en el eje sobre el cual se concatenarán.
- Consultar las imágenes {ref}`join-arrays-1D` y {ref}`join-arrays-2D` de referencia. 


**Apilación (_stack_)**: 

- Se utiliza la función `np.stack()`.
- En _stack_ los _arrays_ se unen en un **eje nuevo**. Es decir, el resultado siempre tendrá una dimensión extra.
- Apilar _arrays_ 1D resulta en _arrays_ 2D, apilar _arrays_ 2D resulta en _arrays_ 3D, etc.
- Los _arrays_ deben de tener el mismo _shape_.
- Consultar las imágenes {ref}`join-arrays-1D` y {ref}`join-arrays-2D` de referencia. 

<br/>

**Otros funciones para concatenar y unir**:

**En 1D**:

<br/>

```{figure} ../images/join-arrays-1D.png
:name: join-arrays-1D
:width: 500px
:align: center

Concatenación y apilación en 1D
```

<br/>

- `np.vstack()` y `np.row_stack()`: 
    - Son igual que `np.stack(axis=0)`. Equivale también a `np.concatenate(axis=0)` después de convertir los _array_ de (k,) a (1, k). 
    - Los _arrays_ deben de tener el mismo número de elementos. 
    - El resultado es un _array_ 2D.
- `np.hstack()`: 
    - Equivale a `np.concatenate(axis=0)`. 
    - Los _arrays_ pueden tener cualquier longitud. 
    - El resultado es un _array_ 1D.
- `np.column_stack()`: 
    - Equivale a `np.stack(axis=1)` o a `np.concatenate(axis=1)` después de convertir los _array_ de (k,) a (k, 1). 
    - Básicamente convierte _arrays_ 1D como columnas de un _array_ 2D. 
    - Los _arrays_ deben de tener el mismo número de elementos. 
    - El resultado es un _array_ 2D.
- `np.dstack()`: 
    - Equivale a `np.stack(axis=2)`, después de convertir los _array_ de (k,) a (1, k). 
    - Los _arrays_ deben de tener el mismo número de elementos. 
    - El resultado es un _array_ 3D. 

<br/>

**En 2D**:

<br/>

```{figure} ../images/join-arrays-2D.png
:name: join-arrays-2D
:width: 500px
:align: center

Concatenación y apilación en 2D
```

<br/>

- `np.vstack()` y `np.row_stack()`: 
    - Son igual que `np.concatenate(axis=0)`. 
    - Siempre concatenan en el eje 0. 
    - Los _arrays_ deben de tener el mismo número de elementos en los ejes, excepto en el eje 0. 
    - El resultado es un _array_ 2D.
- `np.hstack()` y `np.column_stack()`: 
    - Son igual que `np.concatenate(axis=1)`. 
    - Siempre concatenan en el eje 1. 
    - Los _arrays_ deben de tener el mismo número de elementos en los ejes, excepto en el eje 1. 
    - El resultado es un _array_ 2D.
- `np.dstack()`: 
    - Es igual que `np.stack(axis=2)`. 
    - Los _arrays_ deben de tener el mismo _shape_.
    - El resultado es un _array_ 3D.



<br/><br/>

---
## Separar arrays (split)

Para realizar la operación contraria a concatenar se pueden utilizar las siguientes funciones.

- `np.split(ary, indices_or_sections, axis=0)`: Divide un _array_ en índices específicos o en _N_ partes iguales y retorna una lista con cada uno de los _arrays_ resultantes del _split_.
    - Si el _array_ es de dos o más dimensiones se pueden indicar sobre cuál eje aplicar el _split_. Por default es sobre el eje 0.
    - Existen funciones con el eje por default como:
        - `np.vsplit()`: Equivale a `np.split(axis=0)`.
        - `np.hsplit()`: Equivale a `np.split(axis=1)`.
        - `np.dsplit()`: Equivale a `np.split(axis=2)`.

:::{note}
Para más información de estas funciones consultar {doc}`manipulacion-arrays` en la sección de _Splitting_.
:::

<br/>

**Ejemplos en 1D**:

```{code-cell} ipython3
# Definir el array
X = np.arange(9)

# Split de un array 1D en partes iguales
print(np.split(X, 3), end='\n'*2)

# Split de un array 1D en índices específicos
X = np.arange(9)
print(np.split(X, [2, 7]))
```

<br/>

**Ejemplos en 2D**:

Split en las filas (eje 0):

```{code-cell} ipython3
# Definir el array
X = np.arange(1, 16).reshape(5, 3)
print(X, end='\n'*2)

# Split de las filas en partes iguales
print(np.vsplit(X, 5), end='\n'*2) # Equivale a np.split(X, 5)

# Split de las filas en índices específicos
print(np.vsplit(X, [2, 3])) # Equivale a np.split(X, [2, 3])
```
- `np.vsplit(X, [2, 3])` retorna tres _arrays_, uno con la fila 1 y 2 (`[:2]`), otro con la fila 3 (`[2:3]`), y otro con la fila 4 y 5 (`[3:]`).


Split en las columnas (eje 1):

```{code-cell} ipython3
# Definir el array
X = np.arange(1, 16).reshape(3, 5)
print(X, end='\n'*2)

# Split de las columnas en partes iguales
print(np.hsplit(X, 5), end='\n'*2) # Equivale a np.split(X, 5, axis=1)

# Split de las columnas en índices específicos
print(np.hsplit(X, [2, 3])) # Equivale a np.split(X, [2, 3], axis=1)
```
- `np.hsplit(X, [2, 3])` retorna tres _arrays_, uno con la columna 1 y 2, otro con la columna 3, y otro con la columna 4 y 5.

<br/>

**Ejemplos en 3D**:

Split en el eje 0 (dimensión 1 - rebanadas):

```{code-cell} ipython3
# Definir el array
X = np.arange(1, 13).reshape(2, 2, 3)
print(X, end='\n'*2)

# Split sobre la dimensión 3 en partes iguales
print(np.vsplit(X, 2), end='\n'*2) # Equivale a np.split(X, 2, axis=0)
```

<br/>

Split en el eje 2 (dimensión 3 - columnas):

```{code-cell} ipython3
# Definir el array
X = np.arange(1, 13).reshape(2, 2, 3)
print(X, end='\n'*2)

# Split sobre la dimensión 3 en partes iguales
print(np.dsplit(X, 3), end='\n'*2) # Equivale a np.split(X, 3, axis=2)

# Split sobre la dimensión 3 en índices específicos
print(np.dsplit(X, [1])) # Equivale a np.split(X, [1], axis=2)
```



<br/><br/>

---
(iteracion)=
## Iterar en un array

Para iterar sobre un _array_ se pueden utilizar algunas funciones específicas para este fin o se puede iterar directamente en el _array_.


**Usando funciones**:

Para iterar sobre un `ndarray`, independientemente de la dimensión, utilizar la función `np.nditer()`:
```python
# Iterar sobre el array X
for value in np.nditer(X, order):
    # for body
```
- `order` \- {‘C’, ‘F’, ‘A’, ‘K’}: Es para indicar el orden de iteración. Los valores más comúnes son _C_ y _F_.
    - _K_: Respeta el orden en el que el _array_ se almacena en memoria, lo más común es que sea `'C'` (por filas). Para más información sobre los órdenes consultar [este artículo](https://en.wikipedia.org/wiki/Row-_and_column-major_order).
    - _C_:
        - En 2D itera elemento por elemento, fila por fila.
        - En 3D tomar como referencia la imagen para ver como se extraen matrices, las cuales posteriormente se iterarán por cada elemento, fila por fila.
    - _F_: 
        - En 2D itera elemento por elemento, columna por columna. Equivale a usar <br/> `np.nditer(a.T, order='C')`.
        - En 3D tomar como referencia la imagen para ver como se extraen matrices, las cuales posteriormente se iterarán por cada elemento, columna por columna.
        
```{figure} ../images/3D-nditer.png
:name: 3D-nditer
:width: 400px
:align: center

Funcionamiento de `np.nditer()` en 3D.
```

<br/>

También se puede usar `np.ndenumerate()` para que se retorne también el índice del elemento:
```python
# Iterar sobre el array X
for i, value in np.ndenumerate(X):
    # for body
```

:::{note}
Para más opciones de iteración consultar {doc}`indices` en la sección de _Iteración_.
:::

<br/>

**Directamente**

:::{note}
Al iterar por _arrays_ usando `for loop` por default `numpy` lo hará por filas, es decir `order='C'`.
:::

Se puede iterar directamente sobre un _array_ en un `for loop`. La manera como se haga la iteración dependerá de la dimensión del _array_.

**1D**: Para iterar por cada elemento.
```python
# Si X es un array 1D
for i in X: # i será un escalar.
    # for body
```

<br/>

**2D**: Iterar por cada fila.
```python
# Iterar por filas
for row in X: # row será un vector 1D.
    # for body

# Iterar por cada elemento de cada fila
for row in X: # row será un array 1D.
    for i in row: # i será un escalar.
        # for body
```

<br/>

**3D**: Iterar por cada elemento, de cada matriz.
```python
# Iterar por cada matriz
for matrix in X: # matrix será un array 2D.
    # for body

# Iterar por cada fila de cada matriz
for matrix in X: # matrix será un array 2D.
    for row in matrix: # row será un array 1D.
        # for body

# Iterar por cada elemento de cada fila de cada matriz
for matrix in X: # matrix será un array 2D.
    for row in matrix: # row será un array 1D.
        for i in row: # i será un escalar.
            # for body
```

Tener en cuenta que las matrices _matrix_ a las que se refiere en la iteración en 3D se conforman de la siguiente manera:

```{image} ../images/iteracion-3D.png
:name: iteracion-3D
:width: 400px
:align: center
```

<br/>

---
## Ordenar array

Para ordenar un _array_ usar los siguientes métodos y funciones:

- `np.sort()`: Retorna una versión ordenada de un _array_. Es posible indicar que se ordene un eje en específico.
- `ndarray.sort()`: Este método ordena un _array_ _in-place_.
- `np.argsort()`: Retorna los índices de los elementos ordenados.
- `np.partition()`: Retorna una copia de un _array_ en la que los primeros _k_ elementos serás los _k_ elementos más pequeños, y el resto los más grandes. Es posible indicar que se haga la partición en un eje en específico.

:::{note}
Para más información consultar los métodos {ref}`seleccion-manipulacion` y las funciones {doc}`buscar-contar-ordenar-unicos` en la sección _Ordenar_.
:::

<br/>

---
## Elementos únicos

Para determinar los elementos únicos de una _array_ usar:

- `np.unique()`: Retorna una copia de un _array_ con los elementos únicos ordenados. Se puede retornar el recuento de cada elemento si se indica `return_counts=True`.

:::{note}
Para más información consultar las funciones {doc}`buscar-contar-ordenar-unicos` en la sección _Valores únicos_.
:::

<br/>

---
## Atributos

A continuación se enlistan los atrbutos de los objetos `np.ndarray`.

### Información

Atributos que retornan información sobre el _array_. 

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - [base](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.base.html)
  - Retorna el objeto en el que el _array_ almacena sus datos (en caso de que sea una view). Retorna `None` si el objeto posee los datos.
* - [dtype](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.dtype.html)
  - Tipo de dato de los elementos del arreglo.
* - [ndim](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.ndim.html)
  - Número de dimensiones del arreglo.
* - [shape](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.shape.html)
  - Retorna un `tuple` con las dimensiones del arreglo.
* - [size](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.size.html)
  - Número de elementos en el arreglo.
```

<br/>

### Otros-atributos

Otros atributos de los objetos `ndarray`. 

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - [T](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.T.html)
  - Retorna una view de la transpuesta del arreglo.
* - [flat](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.flat.html)
  - Retorna un `iterator` 1D del arreglo.
* - [imag](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.imag.html)
  - La parte imaginaria del arreglo.
* - [real](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.real.html)
  - La parte real del arreglo.
```

<br/><br/>

## Métodos

A continuación se enlistan los métodos de la clase `np.ndarray`.

### Conversión y salida

Métodos para convertir _arrays_ a otros tipos o para exportar el _array_ a un archivo. 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [astype](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.astype.html)(dtype[, order, casting, ...])
  - Retorna una copia del arreglo, convertida en un tipo especifico.
* - [copy](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.copy.html)([order])
  - Devuelve una copia del arreglo.
* - [dump](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.dump.html)(file)
  - Almacena un `pickle` del arreglo al archivo especificado.
* - [fill](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.fill.html)(value)
  - Rellena el arreglo con un valor escalar.
* - [item](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.item.html)(*args)
  - Copia un elemento del arreglo en un escalar estándar de Python y lo retorna.
* - [itemset](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.itemset.html)(*args)
  - Inserta un elemento en un arreglo.
* - [tofile](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.tofile.html)(fid[, sep, format])
  - Exporta un arreglo en un archivo de texto o binario (default).
* - [tolist](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.tolist.html)()
  - Devuelve el arreglo como una lista anidada.
* - [view](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.view.html)([dtype][, type])
  - Devuelve una _view_ del arreglo con los mismos datos.
```

<br/>

---
### Cálculos

Métodos para hacer cálculos sobre el _array_. 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [all](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.all.html)([axis, out, keepdims, where])
  - Devuelve `True` si todos los elementos se evalúan como `True`.
* - [any](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.any.html)([axis, out, keepdims, where])
  - Devuelve `True` si al menos uno de los elementos del arreglo se evalúa como `True`.
* - [argmax](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.argmax.html)([axis, out, keepdims])
  - Devuelve los índices de los valores máximos a lo largo del eje dado.
* - [argmin](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.argmin.html)([axis, out, keepdims])
  - Devuelve los índices de los valores mínimos a lo largo del eje dado.
* - [clip](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.clip.html)([min, max, out])
  - Devuelve un arreglo cuyos valores están limitados a _[min, max]_.
* - [conj](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.conj.html)()
  - Complejo conjugado de todos los elementos.
* - [cumprod](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.cumprod.html)([axis, dtype, out])
  - Devuelve el producto acumulado de los elementos a lo largo del eje dado.
* - [cumsum](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.cumsum.html)([axis, dtype, out])
  - Devuelve la suma acumulada de los elementos a lo largo del eje dado.
* - [max](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.max.html)([axis, out, keepdims, initial, ...])
  - Devuelve el valor máximo a lo largo de un eje dado.
* - [mean](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.mean.html)([axis, dtype, out, keepdims, where])
  - Devuelve el promedio de los elementos del arreglo a lo largo del eje dado.
* - [min](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.min.html)([axis, out, keepdims, initial, ...])
  - Devuelve el valor mínimo a lo largo de un eje dado.
* - [prod](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.prod.html)([axis, dtype, out, keepdims, ...])
  - Devuelve el producto de los elementos del arreglo sobre el eje dado.
* - [ptp](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.ptp.html)([axis, out, keepdims])
  - Devuelve el rango (máximo - mínimo) a lo largo de un eje dado.
* - [round](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.round.html)([decimals, out])
  - Devuelve el arreglo con cada elemento redondeado al número dado de decimales.
* - [std](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.std.html)([axis, dtype, out, ddof, ...])
  - Devuelve la desviación estándar de los elementos del arreglo a lo largo del eje dado.
* - [sum](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.sum.html)([axis, dtype, out, keepdims, ...])
  - Devuelve la suma de los elementos del arreglo sobre el eje dado.
* - [trace](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.trace.html)([offset, axis1, axis2, dtype, out])
  - Devuelve la suma a lo largo de la diagonal del arreglo.
* - [var](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.var.html)([axis, dtype, out, ddof, ...])
  - Devuelve la varianza de los elementos del arreglo, a lo largo del eje dado.
```

<br/>

---
(manipulacion-shape)=
### Manipulación del shape

Métodos para manipular el _shape_ o los ejes del _array_. 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [flatten](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.flatten.html)([order])
  - Devuelve una copia del arreglo colapsada en una dimensión.
* - [ravel](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.ravel.html)([order])
  - Devuelve un arreglo aplanado.
* - [reshape](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.reshape.html)(shape[, order])
  - Devuelve un arreglo que contiene los mismos datos con un nuevo shape.
* - [resize](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.resize.html)(new_shape[, refcheck])
  - Modifica el _shape_ y el tamaño del arreglo in-place.
* - [squeeze](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.squeeze.html)([axis])
  - Elimina los ejes de longitud uno del arreglo.
* - [swapaxes](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.swapaxes.html)(axis1, axis2)
  - Devuelve una _view_ del arreglo con _axis1_ y _axis2_ intercambiados.
* - [transpose](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.transpose.html)(*axes)
  - Devuelve una _view_ del arreglo con los ejes transpuestos.
```

<br/>

---
(seleccion-manipulacion)=
### Selección y manipulación de elementos

Métodos para manipulación y selección de elementos, incluyendo ordenar. 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [argpartition](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.argpartition.html)(kth[, axis, kind, order])
  - Devuelve los índices que dividirán el arreglo.
* - [argsort](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.argsort.html)([axis, kind, order])
  - Devuelve los índices que ordenarían este arreglo.
* - [choose](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.choose.html)(choices[, out, mode])
  - Construye un _array_ desde un arreglo de índices y un conjunto de arreglos desde los cuales se eligirán los elementos.
* - [compress](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.compress.html)(condition[, axis, out])
  - Devuelve las porciones seleccionadas del arreglo a lo largo del eje dado.
* - [diagonal](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.diagonal.html)([offset, axis1, axis2])
  - Devuelve las diagonales del arreglo especificadas.
* - [nonzero](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.nonzero.html)()
  - Devuelve los índices de los elementos que no son cero.
* - [partition](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.partition.html)(kth[, axis, kind, order])
  - Reorganiza los elementos del arreglo de tal manera que el valor del elemento en la k-ésima posición está en la posición en la que estaría en un arreglo ordenado.
* - [put](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.put.html)(indices, values[, mode])
  - Establece `a.flat[n] = values[n]` para todos los _n_ en _indices_.
* - [repeat](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.repeat.html)(repeats[, axis])
  - Repite elementos de un arreglo.
* - [searchsorted](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.searchsorted.html)(v[, side, sorter])
  - Determina los índices donde los elementos de `v` deben insertarse en el arreglo para mantener el orden.
* - [sort](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.sort.html)([axis, kind, order])
  - Ordena un arreglo in-place.
* - [take](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.take.html)(indices[, axis, out, mode])
  - Retorna un arreglo con los elementos indicados en _indices_.
```

