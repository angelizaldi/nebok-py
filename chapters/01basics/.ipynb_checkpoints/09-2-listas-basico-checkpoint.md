# Listas

Algunas características de las listas, correspondientes al tipo de dato `list`, son:
- Sirven para almacenar múltiples valores de diferentes tipos en una sola variable. 
- Sus elementos están ordenados (indexados)
- Sus elementos se pueden modificar.
- Un mismo valor puede existir múltiples veces en una lista.

---
## Crear una lista:
Existen dos métodos principales para crear una lista
1.	Poner los elementos, separados por coma, dentro de corchetes `[]`:
```python
X = [x1, x2, …]
```
2.	Poner los elementos, separados por coma, dentro del constructor `list()`:
```python
X = list(x1, x2, x3, …)
```

---
##  Concatenar elementos:

Para agregar elementos a una lista existente se puede usar el operador `+`, que sirve para concatenar listas, los nuevos elementos se agregarán al final de la lista existente.
```python
X + [x1]
X + Y
```
donde
- X, Y son listas
- Si solo se quiere agregar un elemento encerrar entre corchetes para convertirlo a lista y poder concatenarlo.

```{note}
Otras formas de agregar elementos que serán cubiertas en los métodos:
- Para insertar algún elemento en un índice en específico sin remplazarlo (recorriendo el resto de los elementos a la derecha) usar el método `list.insert`.
- Para insertar algún elemento al final de la lista usar el método `list.append`.
```

---
## Eliminar Elementos:

Para eliminar un elemento específico o la lista completa usar la palabra reservada `del` y el elemento que se quiere eliminar:
```python
#Elimina el elemento i de la lista X
del X[i]

#Elimina la lista X
del X		
```

```{note}
Otras formas de eliminar elementos cubiertos en la sección de métodos:
- Para remover un elemento usar el método `list.remove`.
- Para remover un elemento de un índice en específico usar el método `list.pop`.
```	

---
## Modificar Elementos:

Para modificar un valor en específico usar su índice y el operador de asignación:
```python
X[i] = val
```

Se pueden cambiar rangos completos con:
```python
X[i:j] = [val1, val2, …]
```

```{warning}
Si se crea una lista y se asigna al objeto `X`, entonces `X` en realidad hace referencia a los elementos que se almacenan en memoria, si se asigna la lista a otro objeto `Y` con el operador de asignación `=`, entonces lo que se copia es la referencia, no los valores como tal, por lo tanto modificaciones en `Y` también afecta a `X` y vicerversa. Para que esto no suceda usar cualquiera de los siguientes opciones:
- `Y = list(X)`
- `Y = X[:]`
- `Y = X.copy()`

De esta manera modificaciones en `Y` no afectarán a `X`.
```

---
## Verificar que un elemento exista en una lista:
Para ver si un elemento está dentro de una lista X usar el operador de membresía `in`:
```python
x in X
```

---
## Selección de elementos: 

### Subsetting:
Para seleccionar elementos de una lista tener en cuenta las siguientes características:
- Se utilizan corchetes `[]` para acceder a los elementos, junto con el nombre de la lista y el índice del elemento: <br/>
`X[i]`
- Los índices comienza en cero (0), esto quiere decir que si quiere acceder al elemento `i`, se debe de usar `[i-1]`.
- Se puede utilizar números negativos, de manera que se comience por el último elemento. En una lista de tamaño `N`, se puede acceder al último con `[-1]`, al penúltimo elemento `[-2]`, etc.
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
- Desde el índice `i` hasta el `j`, sin incluir el `j`, cada `k` caracteres: <br> `X[i:j:k]`

Algunos patrones útiles:
- El primer elemento: <br> `X[0]`
- El último elemento: <br> `X[-1]`
- Toda la lista cada `k` elementos: <br> `X[::k]`
- Toda la lista al revés: <br> `X[::-1]`

---
## Unpack de listas:

Se refiere a asignar a varias variables los elementos de un objeto iterable como un `list`:
```
x1, x2, ... , xn  = X
```
- X \- `list`: Una lista de longitud `N`.

Si el número de variables es menor que el número de elementos se puede usar un asterisco `*`, para indicar que en esa variable se almacenen el resto de los elementos:
```
x1, x2, ... , *xi  = X
```
- X \- `list`: Una lista.
- En ese caso la varible `xi` almacenará todos lo valores restantes en la lista.
- El asterisco no tiene porque ir en la última variable, puede ir antes, en ese caso python asignará el número de elementos que sea necesario, para que el resto de las variables que vienen después tengan un elemento.
