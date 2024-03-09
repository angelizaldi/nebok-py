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

# Listas

Corresponden al tipo de dato `list`. Las listas son secuencias. Algunas características de las listas, son:
- Sirven para almacenar múltiples valores de diferentes tipos en una sola variable. 
- Es mutable: Sus elementos se pueden modificar.
- Está indexado: Cada elemento está asociado con un índice y por lo tanto sus elementos están ordenados.
- Es un iterable: Se puede iterar por sus elementos y se puede usar la palabra reservada `in` para verificar memebresía.
- Un mismo valor puede existir múltiples veces en una lista.
- Se puede concatenar con otras listas.

Para más información visitar la [documentación](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range) de Python.

<br>

---
## Crear una lista
Existen dos métodos principales para crear una lista
**1**. Poner los elementos, separados por coma, dentro de corchetes `[]`:
```python
# Crear una lista
X = [x1, x2, ...]
```

**2**. Convertir una secuencia o un iterable a una lista con la función `list()`:
```python
# Convertir el iterable Y a una lista
X = list(Y)
```

```{note}
Otra forma de crear una lista es con {ref}`list-comp`.

```

```{warning}
Si `X` es una lista y sea crea otra lista `Y` usando `Y=X`, entonces modificaciones en `Y` también afectarán a `X` y vicerversa. Para que esto no suceda usar cualquiera de los siguientes opciones:
- `Y = list(X)`
- `Y = X[:]`
- `Y = X.copy()`

De esta manera modificaciones en `Y` no afectarán a `X` y viceversa.
```

<br>

---
##  Agregar/Concatenar elementos

Para agregar elementos a una lista existente se puede usar el operador `+`, que sirve para concatenar listas, los nuevos elementos se agregarán al final de la lista.
```python
# Si X y Y son listas, entonces W es la concatenacion de X y Y:
W = X + Y
```
- Si solo se quiere agregar un elemento que no es una lista encerrar entre corchetes o usar la función `list()` para convertirlo a lista y poder concatenarlo.

```{note}
Otras formas de agregar elementos usando métodos son:
- Para insertar algún elemento en un índice en específico sin remplazarlo (recorriendo el resto de los elementos a la derecha) usar el método `list.insert()`.
- Para insertar algún elemento al final de la lista usar el método `list.append()`.

Para más información revisar {ref}`Metodos-Agregar <list-metodos-agregar>`.
```

El operador `*` sirve para repetir `n` veces una lista y concatenarlas.
```python
# Si X es una lista y n un número entero
# entonces Y es X concatenado n veces
Y = X * n 
```

<br>

---
## Eliminar Elementos

Para eliminar un elemento específico o la lista completa usar la palabra reservada `del` y el elemento que se quiere eliminar:
```python
# Eliminar el elemento i de la lista X
del X[i]

# Eliminar la lista X
del X
```

```{note}
Otras formas de eliminar elementos con métodos son:
- Para remover un elemento específico usar el método `list.remove()`.
- Para remover un elemento de un índice en específico usar el método `list.pop()`.

Para más información revisar {ref}`Metodos-Eliminar <list-metodos-eliminar>`.
```

<br>

---
## Modificar Elementos

Para modificar un elemento en específico usar su índice y el operador de asignación:
```python
# Si X es una lista e i es un índice válido de X 
X[i] = val
```

Se pueden cambiar rangos completos con:
```python
# Modificar valores desde i hasta j-1
X[i:j] = [val1, val2, ...]
```
- La lista con los nuevos valores debe de tener `j-i` elementos.

<br>

---
## Verificar que un elemento exista en una lista

Para verificar si un elemento está dentro de una lista usar el operador de membresía `in`:
```python
# Si X es una lista
x in X
```
- Alternativamente se puede usar `not in`.

<br>

---
## Selección de elementos 

### Subsetting

Para seleccionar elementos de una lista tener en cuenta las siguientes características:
- Se utilizan corchetes `[]` para acceder a los elementos, junto con el nombre de la lista y el índice del elemento: <br/>
`X[i]`
- Los índices comienza en cero (0), esto quiere decir que si quiere acceder al elemento `n`, se debe de usar `[n-1]`.
- Se puede utilizar índices negativos, para hacer subsetting de derecha a izquierda, comenzando por el último elemento. Por ejemplo, se puede acceder al último elemento con `[-1]`, al penúltimo elemento con `[-2]`, etc.
- Para listas dentro de otras listas, considerar que en esencia usar `X[i]` devolverá otra lista, entonces para acceder a los elementos de esa otra lista usar otro `[]`, esto es: <br/> `X[i][j]`
- Lo anterior se puede generalizar para cualquier número de listas anidadas.

Algunos patrones útiles:
- El primer elemento: <br> `X[0]`
- El elemento _n_: <br> `X[n-1]`
- El último elemento: <br> `X[-1]`

<br/>

### Slicing

Para seleccionar un rango de elementos consecutivos tener en cuenta las siguientes características:
- Se utiliza dos puntos, indicando los indices de inicio, fin y el paso: <br/> `X[i:j:k]`
- La selección por rango, tienen la característica que el primer elemento es inclusivo y el último es exclusivo, esto quiere decir que no se incluirá en el rango, si se usa el rango `[m:n]`, en realidad solo se accederá a `[m:n-1]`.

Algunos patrones útiles:
- Desde el índice `i` hasta el `j`, sin incluir el `j`: <br> `X[i:j]`
- Desde el inicio hasta el `j`, sin incluir el `j`: <br> `X[:j]`
- Desde la posición `i` hasta el final de la lista: <br>`X[i:]`
- Toda la lista: <br> `X[:]`
- Desde el índice `i` hasta el `j`, sin incluir el `j`, cada `k` elementos: <br> `X[i:j:k]`
- Toda la lista cada `k` elementos: <br> `X[::k]`
- Toda la lista al revés: <br> `X[::-1]`

<br>

---
## Unpack de listas

Se refiere a asignar a varias variables los elementos de un objeto iterable como `list`:
```
# X es una lista de longitud n
x1, x2, ... , xn  = X
```

Si el número de variables es menor que el número de elementos se puede usar un asterisco `*`, para indicar que en esa variable se almacenen el resto de los elementos:
```
# X es una lista
x1, x2, ... , *xi  = X
```
- En ese caso la varible `xi` almacenará todos lo valores restantes en la lista.
- El asterisco no tiene porque ir en la última variable, puede ir antes, en ese caso Python asignará el número de elementos que sea necesario, para que el resto de las variables tengan un elemento.

<br>

---
## Iteración

Para interar sobre todos los elementos de una lista se puede usar un `for loop`. Algunas opciones de iteración son:
```python
# Iterar sobre los elementos de la lista X:
for ele in X:
    # for body
        
# Iterar sobre los índices de la lista X:
for i in range(len(X)):
    # for body
    
# Iterar sobre los elementos y los índices de la lista X:
for i, ele in enumerate(X):
    # for body
```
- En todos los ejemplos anteriores `i` y `ele` son nombres opcionales.

<br>

---
(list-comp)=
## List comprehension

Son listas que se crean a partir procesos iterativos con la estructura `for`. Sintaxis:
```python
X = [expression for i in collection]
```
- _collection_ es cualquier `iterable`.
- _expression_ es cualquier expresión cuya evaluación retorne un objeto.

Lo anterior equivale a:
```python
X = []
for i in collection:
    X.append(expression)
```

Las _list comprehension_ también pueden tener condicionales, tanto en la parte de _expression_ como en la parte de _collection_, de manera que solo a cierto elementos se les aplique el código o de que dependiendo del resultado de la _expression_ se ponga un valor u otro. Sintaxis:

**En el iterable**: En este caso _expression_ solo se evalua si los elementos de _collection_ cumplen una condición.
```python
# list comprehension con condicional en collection
X = [expression for i in collection if condition]
```

**En la _expression_**: En este caso el elemento de `X` dependerá del resultado de _condition_.
```python
# list comprehension con condicional en expression
X = [expression_true if condition else expression_false for i in collection]
```
- Una _list comprehesion_ puede tener ambos tipos de condicionales al mismo tiempo.

**Ejemplo**: Encontrar los elementos al cuadrado de una lista numérica, solo si el número es par.
```{code-cell} ipython3
# Definir una lista
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Definir la list comprehesion 
pares_cuadrados = [numero**2 for numero in numeros if numero % 2 == 0]

# Imprimir la lista
print(pares_cuadrados)
```
* En el código anterior hubiera sido más eficiente utilizar la función `range()` para crear la secuencia de números, es decir, `numeros = range(11)`.

<br>

---
## Métodos de listas

En esta sección se enlistan los métodos del tipo `list` por categorias. 

Tener en cuenta que los métodos generalmente se aplican sobre un objeto de tipo `list`, por ejemplo, si `X` es `list`, entonces se utiliza <code>X.<i>method_name</i></code>. Sin embargo es posible usar la lista como argumento de <code>list.<i>method_name</i></code>. Por ejemplo.

```{code-cell} ipython3
# Definir una lista
X = ["a", "a", "b", "c"]

# Usar el metodo sobre el objeto
print(X.count("a"))

# Equivale a:
print(list.count(X, "a"))
```
- Tener en cuenta que en la segunda forma la lista siempre debe de ser el primer argumento.


### Agregar elementos

Métodos para agregar elementos a una lista.

```{list-table}
:header-rows: 1
:name: list-metodos-agregar

* - Método
  - Descripción
* - [append](https://docs.python.org/3/library/stdtypes.html#mutable-sequence-types)(x)
  - Agrega un elemento al final de una lista "_in-place_". También se puede utilizar el operador `+`.
* - [extend](https://docs.python.org/3/library/stdtypes.html#mutable-sequence-types)(t)
  - Extiende una lista con el contenido de un iterable "_in-place_".
* - [insert](https://docs.python.org/3/library/stdtypes.html#mutable-sequence-types)(i, x)
  - Inserta `x` en una lista en el índice dado por `i`, recorriendo el resto de los elementos a la derecha.
```

<br/>

### Copiar

Métodos para copiar una lista.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [copy](https://docs.python.org/3/library/stdtypes.html#mutable-sequence-types)()
  - Crea una copia superficial de la lista.
```

<br/>

### Eliminar elementos

Métodos para eliminar elementos de una lista.

```{list-table}
:header-rows: 1
:name: list-metodos-eliminar

* - Método
  - Descripción
* - [clear](https://docs.python.org/3/library/stdtypes.html#mutable-sequence-types)()
  - Remueve todos los elementos de la lista.
* - [pop](https://docs.python.org/3/library/stdtypes.html#mutable-sequence-types)(i)
  - Remueve un elemento de una posición en específico, retorna ese elemento y recorre el resto de los elementos a la izquierda.
* - [remove](https://docs.python.org/3/library/stdtypes.html#mutable-sequence-types)(x)
  - Elimina la primer coincidencia de un elemento en la lista "_in-place_".
```

<br/>

### Información de la lista

Métodos para obtener información sobre una lista.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [count](https://docs.python.org/3/library/stdtypes.html#common-sequence-operations)(x)
  - Retorna el número total de ocurrencias de `x` en la lista.
* - [index](https://docs.python.org/3/library/stdtypes.html#common-sequence-operations)(x[, i[, j]])
  - Indice de la primera aparición de `x` en la lista (en o después índice `i` y antes del índice `j`). Retorna `ValueError` si `x` no está en la lista. 
```

<br/>

### Ordenar

Métodos para ordenar una lista.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [reverse](https://docs.python.org/3/library/stdtypes.html#mutable-sequence-types)()
  - Modifica el orden de la lista de manera inversa "_in-place_".
* - [sort](https://docs.python.org/3/library/stdtypes.html#list.sort)(*, key=None, reverse=False)
  - Ordena los valores de la lista de manera alfabética o numérica. Realiza la acción "_in-place_".
```

<br/>

---
## Funciones útiles para listas

Algunas funciones built-in útiles para listas son:
- `max()`: Encontrar el valor máximo de la lista.
- `min()`: Encontrar el valor minimo de la lista.
- `len()`: Encontrar la longitud (número de elementos) de la lista.
