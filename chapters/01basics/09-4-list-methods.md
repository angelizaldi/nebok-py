# Métodos de listas:

Los métodos aquí explicados suponen que el método se aplica directamente sobre una lista, pero es posible usar la lista como argumento usando <code>list.<i>method_name</i>()</code>, por ejemplo, en lugar de usar `X.append(Y)` se puede usar:
```python
list.append(X, Y)
```
- `X` \- `list`.
- `Y` \- `object`.
- En ese caso el primer argumento debe de ser la lista.

---
## Agregar Elementos:

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
## Eliminar Elementos

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
## Información
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
## Modificar

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
# Otros

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

