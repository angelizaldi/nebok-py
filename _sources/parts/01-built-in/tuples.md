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

# Tuples

Corresponde al tipo de dato `tuple`. Los tuples son una secuencia. Algunas caractacterísticas son:
- Sirven para almacenar múltiples valores de diferentes tipos en una sola variable. 
- Está indexado: Cada elemento está asociado con un índice y por lo tanto sus elementos están ordenados.
- Es inmutable: No se puede modificar una vez creado el `tuple`.
- Un mismo valor puede existir múltiples veces en la tupla.
- Es un iterable: Se puede iterar por sus elementos y se puede usar la palabra reservada `in` para verificar memebresía.
- Se puede concatenar con otras tuplas.

Para más información visitar la [documentación](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range) de Python.

<br>

---
## Crear un tuple

Para crear un `tuple` existen distintas formas:
1. Poner los elementos, separados por coma directamente
2. Poner los elementos, separados por coma de paréntesis `()`.
3. Utilizar la función `tuple()` para convertir un iterable a un `tuple`.
```python
# Las siguientes expresiones son equivalentes
X = x1, x2, ...
X = (x1, x2, ...)

# Convertir a tuple el iterable Y
X = tuple(Y)
```
- Los elementos pueden ser otros tuples.

```{warning} Si se quiere crear un tuple de solo un elemento usando paréntesis, se tienen que poner una coma ‘,’ después del elemento, es decir, <code> X = (x,) </code>
```

<br>

---
##  Concatenar y multiplicar:

El operador `+` sirve para concatenar tuplas, los elementos se agrega al final `tuple`.
```python
# Si X y Y son tuples, entonces W es la concatenacion de X y Y:
W = X + Y
```

El operador `*` sirve para repetir `n` veces un `tuple` y concatenarlos.
```python
# Si X es un tuple y n un número entero
# entonces Y es X concatenado n veces
Y = X * n 
```

<br>

---
## Verificar que un elemento exista en un tuple:
Para verificar si un elemento está dentro de un `tuple` usar el operador de membresía `in`:
```python
# Si X es una tupla
x in X
```
- Alternativamente se puede usar `not in`.

<br>

---
## Selección de elementos: 

### Subsetting:
Para seleccionar elementos de una tupla tener en cuenta las siguientes características:
- Se utilizan corchetes `[]` para acceder a los elementos, junto con el nombre de la tupla y el índice del elemento: <br/>
`X[i]`
- Los índices comienza en cero (0), esto quiere decir que si quiere acceder al elemento `n`, se debe de usar `[n-1]`.
- Se puede utilizar índices negativos, para hacer subsetting de derecha a izquierda, comenzando por el último elemento. Por ejemplo, se puede acceder al último elemento con `[-1]`, al penúltimo elemento con `[-2]`, etc.
- Para tuplas dentro de otras tuplas, considerar que en esencia usar `X[i]` devolverá otra tupla, entonces, para acceder a los elementos de esa otra tupla usar otro `[]`, esto es: <br/> `X[n1][n2]`
- Lo anterior se puede generalizar para cualquier número de tuplas anidadas.

Algunos patrones útiles:
- El primer elemento: <br> `X[0]`
- El elemento _n_: <br> `X[n-1]`
- El último elemento: <br> `X[-1]`

### Slicing:
Para seleccionar un rango de elementos consecutivos tener en cuenta las siguientes características:
- Se utiliza dos puntos, indicando los indices de inicio, fin y el paso: <br/> `X[i:j:k]`
- La selección por rango, tienen la característica que el primer elemento es inclusivo y el último es exclusivo, esto quiere decir que no se incluirá en el rango, si se usa el rango `[m:n]`, en realidad solo se accederá a `[m:n-1]`.

Algunos patrones útiles:
- Desde el índice `i` hasta el `j`, sin incluir el `j`: <br> `X[i:j]`
- Desde el inicio hasta el `j`, sin incluir el `j`: <br> `X[:j]`
- Desde la posición `i` hasta el final de la tupla: <br>`X[i:]`
- Toda la tupla: <br> `X[:]`
- Desde el índice `i` hasta el `j`, sin incluir el `j`, cada `k` elementos: <br> `X[i:j:k]`
- Toda la tupla cada `k` elementos: <br> `X[::k]`
- Toda la tupla al revés: <br> `X[::-1]`

<br>

##  Modificar tuples:
Los tuples no se pueden modificar una vez creados. Un truco para modificar una tupla es convertir la tupla en una lista y después volverla a convertir en una tupla:
```python
# Un tuple
X = (...)

# Convertir a lista
Y = list(X)

# modificar
expression

# Convertir a tuple de vuelta
X = tuple(Y)
```

Para eliminar todo el tuple se puede usar la palabra reservada `del`:
```python
# Si X es un tuple
del X
```

<br>

---
## Unpack de tuples:

Se refiere a asignar a varias variables los elementos de un objeto iterable como un `tuple`:
```python
# Si X es una tupla de longitud n:
x1, x2, ... , xn  = X
```

Si el número de variables es menor que el número de elementos se puede usar un asterisco `*`, para indicar que en esa variable se almacenen el resto de los elementos:
```python
# Si X es una tupla:
x1, x2, ... , *xi  = X
```
- En ese caso la varible `xi` almacenará todos lo valores restantes en la tupla.
- El asterisco no tiene porque ir en la última variable, puede ir antes, en ese caso python asignará el número de elementos que sea necesario, para que el resto de las variables que vienen después tengan un elemento.

<br>

---
## Iteración:

Para iterar sobre todos los elementos de un `tuple` se puede usar un `for loop`. Algunas opciones de iteración son:
```python
# Iterar sobre los elementos del tuple X:
for ele in X:
    ...
        
# Iterar sobre los índices del tuple X:
for i in range(len(X)):
    ...
    
# Iterar sobre los elementos y los índices del tuple X:
for i, ele in enumerate(X):
    ...
```
- En todos los ejemplos anteriores `i` y `ele` son nombres opcionales.

<br>

---
## Métodos de tuple

En esta sección se enlistan los métodos del tipo `list`. 

Tener en cuenta que los métodos generalmente se aplican sobre un objeto de tipo `tuple`, por ejemplo, si `X` es `tuple`, entonces se utiliza <code>X.<i>method_name</i></code>. Sin embargo es posible usar la tupla como argumento de <code>tuple.<i>method_name</i></code>. Por ejemplo.

```{code-cell} ipython3
# Definir una tupla
X = ("a", "a", "b", "c")

# Usar el metodo sobre el objeto
print(X.count("a"))

# Equivale a:
print(tuple.count(X, "a"))
```
- Tener en cuenta que en la segunda forma la tupla siempre debe de ser el primer argumento.

---
### Informacion sobre el tuple

Métodos para recuperar información sobre el `tuple`.

```{list-table} Informacion
:header-rows: 1

* - Funciones
  - Descripción
* - [count](https://docs.python.org/3/library/stdtypes.html#common-sequence-operations)(x)
  - Devuelve el número de veces que hay un elemento `x` en el `tuple`.
* - [index](https://docs.python.org/3/library/stdtypes.html#common-sequence-operations)(x[, i[, j]])
  - Devuelve el índice en el que se encuentra un elemento `x`.
```

<br>

---
## Funciones útiles para listas

Algunas funciones built-in útiles para tuplas son:
- `max()`: Encontrar el valor máximo del `tuple`.
- `min()`: Encontrar el valor minimo del `tuple`.
- `len()`: Encontrar la longitud (número de elementos) del `tuple`.

