# Listas

Correspnden al tipo de dato `list`. Las listas son secuencias. Algunas características de las listas, son:
- Sirven para almacenar múltiples valores de diferentes tipos en una sola variable. 
- Es mutable: Sus elementos se pueden modificar.
- Está indexado: Cada elemento está asociado con un índice.
- Es un iterable: Se puede iterar por sus elementos y se puede usar la palabra reservada `in` para verificar memebresía.
- Un mismo valor puede existir múltiples veces en una lista.
- Se puede concatenar con otras listas

---
## Crear una lista:
Existen dos métodos principales para crear una lista
1. Poner los elementos, separados por coma, dentro de corchetes `[]`:
```python
X = [x1, x2, …]
```
2. Poner los elementos, separados por coma, dentro del constructor `list()`:
```python
X = list(x1, x2, x3, …)
```

Otra forma de crear una lista es con {doc}`09-3-list-comprehessions.md`.

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
Si se crea una lista y se asigna al objeto `X`, entonces `X` en realidad hace referencia a los elementos que se almacenan en memoria, si se asigna la lista a otro objeto `Y` con el operador de asignación `=`, entonces lo que se copia es la referencia, no los valores como tal, por lo tanto modificaciones en `Y` también afectan a `X` y vicerversa. Para que esto no suceda usar cualquiera de los siguientes opciones:
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