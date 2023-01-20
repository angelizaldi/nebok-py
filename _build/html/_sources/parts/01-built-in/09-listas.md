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

Correspnden al tipo de dato `list`. Las listas son secuencias. Algunas características de las listas, son:
- Sirven para almacenar múltiples valores de diferentes tipos en una sola variable. 
- Es mutable: Sus elementos se pueden modificar.
- Está indexado: Cada elemento está asociado con un índice y por lo tanto sus elementos están ordenados.
- Es un iterable: Se puede iterar por sus elementos y se puede usar la palabra reservada `in` para verificar memebresía.
- Un mismo valor puede existir múltiples veces en una lista.
- Se puede concatenar con otras listas

---
## Crear una lista:
Existen dos métodos principales para crear una lista
1. Poner los elementos, separados por coma, dentro de corchetes `[]`:
```python
X = [x1, x2, ...]
```
2. Poner los elementos, separados por coma, dentro del constructor `list()`:
```python
X = list(x1, x2, x3, ...)
```

Otra forma de crear una lista es con {ref}`list-comp`.

---
##  Agregrar/Concatenar elementos:

Para agregar elementos a una lista existente se puede usar el operador `+`, que sirve para concatenar, los nuevos elementos se agregarán al final de la primer lista.
```python
# Si X y Y son listas, entonces W es la concatenacion de X y Y:
W = X + Y
```
- Si solo se quiere agregar un elemento que no es una lista encerrar entre corchetes para convertirlo a lista y poder concatenarlo.

```{note}
Otras formas de agregar elementos usando los métodos son:
- Para insertar algún elemento en un índice en específico sin remplazarlo (recorriendo el resto de los elementos a la derecha) usar el método `list.insert`.
- Para insertar algún elemento al final de la lista usar el método `list.append`.
```

El operador `*` sirve para repetir `n` veces una lista y concatenarlas.
```python
# Si X es una lista y n un número entero, entonces Y es X concatenado n veces
Y = X * n 
```

---
## Eliminar Elementos:

Para eliminar un elemento específico o la lista completa usar la palabra reservada `del` y el elemento que se quiere eliminar:
```python
# Eliminar el elemento i de la lista X
del X[i]

# Eliminar la lista X
del X
```

```{note}
Otras formas de eliminar elementos con métodos son:
- Para remover un elemento específico usar el método `list.remove`.
- Para remover un elemento de un índice en específico usar el método `list.pop`.
```	

---
## Modificar Elementos:

Para modificar un elemento en específico usar su índice y el operador de asignación:
```python
# Si X es una lista e i es un índice válido de X 
X[i] = val
```

Se pueden cambiar rangos completos con:
```python
X[i:j] = [val1, val2, ...]
```

```{warning}
Si `X` es una lista y sea crea un objeto `Y` usando `Y=X`, entonces modificaciones en `Y` también afectarán a `X` y vicerversa. Para que esto no suceda usar cualquiera de los siguientes opciones:
- `Y = list(X)`
- `Y = X[:]`
- `Y = X.copy()`

De esta manera modificaciones en `Y` no afectarán a `X` y viceversa.
```

---
## Verificar que un elemento exista en una lista:
Para ver si un elemento está dentro de una lista X usar el operador de membresía `in`:
```python
# Si X es una lista
x in X
```

---
## Selección de elementos: 

### Subsetting:
Para seleccionar elementos de una lista tener en cuenta las siguientes características:
- Se utilizan corchetes `[]` para acceder a los elementos, junto con el nombre de la lista y el índice del elemento: <br/>
`X[i]`
- Los índices comienza en cero (0), esto quiere decir que si quiere acceder al elemento `i`, se debe de usar `[i-1]`.
- Se puede utilizar números negativos, de manera que se comience por el último elemento. Se puede acceder al último con `[-1]`, al penúltimo elemento `[-2]`, etc.
- Para listas dentro de otras listas, considerar que en esencia usar `X[i]` devolverá otra lista, entonces para acceder a los elementos de esa otra lista usar otro `[]`, esto es: <br/> `X[N1][N2]`
- Lo anterior se puede generalizar para cualquier número de listas anidadas.

---
### Slicing:
- Para seleccionar un rango de elementos consecutivos se utiliza dos puntos: <br/> `X[i:j]`
- La selección por rango, tienen la característica que el primer elemento es inclusivo y el último es exclusivo, esto quiere decir que no se incluirá en el rango, si se usa el rango `[i:j]`, en realidad solo se accederá a `[i:j-1]`.
- Desde el índice `i` hasta el `j`, sin incluir el `j`: <br> `X[i:j]`
- Desde el inicio hasta el `j`, sin incluir el `j`: <br> `X[:j]`
- Desde la posición `i` hasta el final de la cadena: <br>`X[i:]`
- Toda la lista: <br> `X[:]`
- Desde el índice `i` hasta el `j`, sin incluir el `j`, cada `k` elementos: <br> `X[i:j:k]`

Algunos patrones útiles:
- El primer elemento: <br> `X[0]`
- El último elemento: <br> `X[-1]`
- Toda la lista cada `k` elementos: <br> `X[::k]`
- Toda la lista al revés: <br> `X[::-1]`

---
## Unpack de listas:

Se refiere a asignar a varias variables los elementos de un objeto iterable como una `list`:
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
- El asterisco no tiene porque ir en la última variable, puede ir antes, en ese caso python asignará el número de elementos que sea necesario, para que el resto de las variables tengan un elemento.

---
## Iteración:

Para interar sobre todos los elementos de una lista se puede usar un `for loop`. Algunas opciones de iteración son:
```python
# Iterar sobre los elementos de la lista X:
for ele in X:
    expression
        
# Iterar sobre los índices de la lista X:
for i in range(len(X)):
    expression
    
# Iterar sobre los elementos y los índices de la lista X:
for i, ele in enumerate(X):
    expression
```
- En todos los ejemplos anteriores `i`y `ele` son nombres opcionales.

---
(list-comp)=
## List comprehension

Son listas que se crean a partir procesos iterativos con la estructura `for`. Sintaxis:
```python
X = [expression for i in collection]
```
donde:
- _collection_ es cualquier `iterable`
- _expression_ es cualquier expresión cuya evaluación retorne un objeto.

Lo anterior equivale a:
```python
X = []
for i in collection:
    X.append(expression)
```

Las list comprehension también pueden tener condicionales, tanto en la parte de _expression_ como en la parte de _collection_, de manera que solo a cierto elementos se les aplique el código o de que dependiendo del resultado de la _expression_ se ponga un valor u otro. Sintaxis:

En el iterable:
```python
X = [expression for i in collection if condition]
```

En la _expression_:
```python
X = [expression_true if condition else expression_false for i in collection]
```

Ejemplo:
```{code-cell} ipython3
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squared_even_numbers = [number**2 for number in numbers if number % 2 == 0]
print(squared_even_numbers)
```
* En el código anterior hubiera sido más eficiente utilizar la función `range()` para crear la secuencia de números.

## Métodos de listas:

Los métodos aquí explicados suponen que el método se aplica directamente sobre una lista, pero es posible usar la lista como argumento usando <code>list.<i>method_name</i>()</code>, por ejemplo, en lugar de usar `X.append(Y)` se puede usar:
```python
list.append(X, Y)
```
- `X` \- `list`.
- `Y` \- `object`.
- En ese caso el primer argumento debe de ser la lista.

---
### Agregar Elementos:

**append**:

`list.append()`: Agrega un elemento al final una lista “in-place”, el elemento es un número, una cadena, una lista, etc. también se puede utilizar el operador `+`.
```python
X.append(Y)
```

**Parámetros:**
- **`X`** \- `list`: Lista.
- **`Y`** \- `object`: Objeto a concatenar.

**Retorna:**
-  `none`.

---
**extend**:

`list.extend()`: Agrega elementos de un objeto iterable al final de la lista.
```python
X.extend(Y)
```

**Parámetros:**
- **`X`** \- `list`: Lista.
- **`Y`** \- `iterable`: Un iterable.

**Retorna:**
-  `none`.

---
**insert**:

`list.insert()`: Inserta un elementos a un índice en específico, recorriendo el resto de los elementos a la derecha.
```python
X.insert(i, Y)
```

**Parámetros:**
- **`X`** \- `list`: Lista.
- **`i`** \- `int`: Índice.
- **`Y`** \- `object`: Un número, una cadena, etc.

**Retorna:**
-  `none`.

---
### Eliminar Elementos

**pop**:

`list.pop()`: Remueve un elemento de una posición en específico, retorna ese elemento y recorre el resto de los elementos a la izquierda.
```python
X.pop([i = -1])
```

**Parámetros:**
- **`X`** \- `list`: Lista.
- **`i`** \- `int`: Es el índice. por default es el último elemento.

**Retorna:**
-  `object`.

---
**remove**:

`list.remove()`: Elimina la primer coincidencia de un elemento en la lista.
```python
X.remove(Y)
```

**Parámetros:**
- **`X`** \- `list`: Lista.
- **`Y`** \- `object`: Un número, una cadena, etc.

**Retorna:**
-  `none`.

---
### Información
**count**:

`list.count()`: Devuelve el número de veces que hay un elemento específico en la lista, el elemento es un número, una cadena, etc.
```python
X.count(Y)
```

**Parámetros:**
- **`X`** \- `list`: Lista.
- **`Y`** \- `object`: Un número, una cadena, etc.

**Retorna:**
-  `int`.

---
**index**:

`list.index()`: Devuelve el índice en el que se encuentra un elemento. retorna error si el valor no está en la lista.
```python
X.index(Y, [start = 0], [end = -1])
```

**Parámetros:**
- **`X`** \- `list`: Lista.
- **`Y`** \- `object`: Un número, una cadena, etc.
- **`start`** \- `int`: Indica desde cuál indice empezar a buscar.
- **`end`** \- `int`: Indica hasta cuál indice buscar.

**Retorna:**
-  `int`.

---
### Modificar

**reverse**:

`list.reverse()`: Modifica el orden de la lista de manera inversa “in-place”.
```python
X.reverse()
```

**Parámetros:**
- **`X`** \- `list`: Lista.

**Retorna:**
-  `none`.

---
**sort**:

`list.sort()`: Ordena los valores de la lista de manera alfabética o numérica. realiza la acción “in-place”.
```python
X.sort([reverse = False], [key = None])
```

**Parámetros:**
- **`X`** \- `list`: Lista.
- **`reverse`** \- `bool`: Es para indicar que sea de manera ascedente (`False`) o descendente (`True`).
- **`key`** \- `None`, `function`: Es una función para ordenar la lista con los resultados de aplicar esa función a cada uno de los elementos. solo se pone el nombre de la función, sin los paréntesis.

**Retorna:**
-  `none`.

```{note}
Si quieres asignar la lista ordenada a otra variable utilizar la función built-in `sorted()`.
```

---
### Otros

**clear**:

`list.clear()`: Remueve todos los elementos de la lista.
```python
X.clear()
```

**Parámetros:**
- **`X`** \- `list`: Lista.

**Retorna:**
-  `none`.

---
**copy**:

`list.copy()`: Crea una copia de la lista.
```python
X.copy()
```

**Parámetros:**
- **`X`** \- `list`: Lista.

**Retorna:**
-  `list`.

