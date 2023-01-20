# Sets

Corresponde al tipo `set`. Son objetos iterables para almacener múltiples elementos en una sola variable. Algunas características del tipo de dato` set` son:
- Se pueden almacenar diferentes tipos de datos en un `set`.
- Los elementos no están ordenados, por lo tanto no se puede acceder a ellos por medio de índices.
- No permite valores duplicados.
- Es mutable: Se pueden modificar una vez creado el `set`. 

---
## Creación

Existen dos métodos principales para crear una sets:

1. Poner los elementos, separados por coma, dentro de llaves `{}`:
```python
X = {x1, x2, ..., xn}
```
2. Convertir un`iterable` es un ser con el constructor `set()`:
```python
# Si Y es un iterable
X = set(Y)
```
> Recordar que los elementos deben de ser únicos.

Otra forma de crear un `set` es con ref`{set-comp}`.

---
## Selección de elementos

No se puede extraer los elementos de un set. La única forma para acceder a los elementos de un set es en un `for loop` o conviertiendo el `set` en `list`:

---
##  Agregar y eliminar elementos:

Para agregar y eliminar elementos de un `set` usar los siguientes métodos:
- Agregar:
  - Agregar un elemento al set usar el método `set.add`.
  - Concatenar sets usar el método `set.update`.

- Eliminar:
  - Eliminar todos los elementos usar el método `set.clear`.
  - Eliminar un elemento específico usar el método `set.discard`. 
  - Eliminar y retornar un elemento específico usar el método `set.pop`.
  - Eliminar un elemento específico y retornar error si no existe usar el método `set.remove`.
 
```{note}
Para más información de esos métodos consultar la sección de métodos de sets.
```

Para eliminar todo el `set` se puede usar la palabra reservada `del`:
```python
# Si X es un set
del X
```

---
## Iteración en sets:
Para interar sobre todos los elementos de una `set` se puede usar un `for loop`. 
```python
# Iterar sobre los elementos de la lista X:
for ele in X:
    ...
```

```{caution} Como los sets no están indexados el orden en el que aparecen los elementos puede diferir de una iteración a otra.
```

---
label(set-comp)=
## Set comprehension

Son sets que se crean a partir procesos iterativos con la estructura `for`. Sintaxis:
```python
X = {expression for i in collection}
```
donde:
- _collection_ es cualquier `iterable`
- _expression_ es cualquier expresión cuya evaluación retorne un objeto.

Lo anterior equivale a:
```python
X = []
for i in collection:
    X.add(expression)
```

Los sets comprehension también pueden tener condicionales, tanto en la parte de _expression_ como en la parte de _collection_, de manera que solo a cierto elementos se les aplique el código o de que dependiendo del resultado de _expression_ se ponga un valor u otro. Sintaxis:

En el iterable:
```python
X = {expression for i in collection if condition}
```

En la _expression_:
```python
X = {val_true if condition else val_false for i in collection}
```

---
## Métodos de sets.

Aquí se enlistas todos los métodos del tipo `set`.

---
### Agregar elementos
Métodos para agregar elementos a un set. Revisar también el método `str.update` en {ref}`subsection:op-conjuntos`.

---
**add**:

`set.add()`: Agrega un elemento a un `set`.
```python
X.add(Y)
```

**Parámetros:**
- **`X`** \- `set`: Un objeto de tipo set.
- **`Y`** \- `object`: Un número, una cadena, etc.

**Retorna:**
-  `None`.

---
### Eliminar Elementos
Métodos para eliminar elementos de un set.

---
**clear**:

`set.clear()`: Remueve todos los elementos del `set` in-place.
```python
X.clear()
```

**Parámetros:**
- **`X`** \- `set`: Un objeto de tipo set.

**Retorna:**
-  `None`.

----
**discard**:

`set.discard()`: Elimina un elemento determinado in-place. No retorna un error si el elemento no existe en el `set`.
```python
X.discard(Y)
```

**Parámetros:**
- **`X`** \- `set`: Un objeto de tipo set.
- **`Y`** \- `object`: Un número, una cadena, etc.

**Retorna:**
-  `None`.

---
**pop**:

`set.pop()`: Elimina y retorna el ultimo elemento de un `set`.
```python
X.pop()
```

**Parámetros:**
- **`X`** \- `set`: Un objeto de tipo set.

**Retorna:**
-  `object`.

---
**remove**:

`set.remove()`: Elimina un elemento determinado in-place. Retorna un error si el elemento no existe en el `set`
```python
X.remove(Y)
```

**Parámetros:**
- **`X`** \- `set`: Un objeto de tipo set.
- **`Y`** \- `object`: Un número, una cadena, etc.

**Retorna:**
-  `None`.

---
### Información
Métodos que retornan información sobre la interacción de dos conjuntos.

---
**isdisjoint**:

`set.isdisjoint()`: Retorna `True` si los elementos de `X` y `Y` son todos diferentes. `False` si al menos hay un elementos en común entre ambos sets.
```python
X.isdisjoint(Y)
```

**Parámetros:**
- **`X`** \- `set`: Un objeto de tipo `set`
- **`Y`** \- `iterable`: Cualquier objeto que sea iterable.

**Retorna:**
-  `bool`.

---
**issubset**:

`set.issubset()`: Retorna `True` si todos los elementos de `X` están en `Y`, `False` en caso contrario. Se debe satisfacer que `len(x) < len(y)`.
```python
X.issubset(Y)
```

**Parámetros:**
- **`X`** \- `set`: Un objeto de tipo `set`
- **`Y`** \- `iterable`: Cualquier objeto que sea iterable.

**Retorna:**
-  `bool`.
**issuperset**:

`set.issuperset()`: Retorna `True` si todos los elementos de `Y` están en `X`, `False` en caso contrario. Se debe satisfacer que `len(x)  > len(y)`.
```python
X.issuperset(Y)
```

**Parámetros:**
- **`X`** \- `set`: Un objeto de tipo `set`
- **`Y`** \- `iterable`: Cualquier objeto que sea iterable.

**Retorna:**
-  `bool`.

---
### Operaciones entre conjuntos

Métodos para las operaciones entre dos o más conjuntos (sets) que retornan un objeto nuevo con el resultado.

---
**difference**:

`set.difference()`: Retorna los elementos que solo están en el `set` `X` pero no en el `set` `Y`.
```python
X.difference(Y, ...)
```

**Parámetros:**
- **`X`** \- `set`: Un objeto de tipo set.
- **`Y`** \- `iterable`: Cualquier otro objeto iterable. Puede ser más de un iterable, separados por coma

**Notas:**
- Equivale a la expresión de python `X - Y`
- Equivale a la operación entre conjuntos $X - X \cap Y$

**Retorna:**
-  `set`.

---
**intersection**:

`set.intersection()`: Retorn los elementos en común de dos sets `X` y `Y`.
```python
X.intersection(Y, ...)
```

**Parámetros:**
- **`X`** \- `set`: Un objeto de tipo set.
- **`Y`** \- `iterable`: Cualquier otro objeto iterable. Puede ser más de un iterable, separados por coma

**Notas:**
- Equivale a la expresión de python `X & Y`.
- Equivale a la operación entre conjuntos $X \cap Y$

**Retorna:**
-  `set`.

---
**symmetric_difference**:

`set.symmetric_difference()`: Retorna los elementos de dos sets `X` y `Y`, excepto aquellos que tienen en común. 
```python
X.symmetric_difference(Y)
```

**Parámetros:**
- **`X`** \- `set`: Un objeto de tipo set.
- **`Y`** \- `iterable`: Cualquier otro objeto iterable.

**Notas:**
- Equivale a la expresión de python `X ^ Y`.
- Equivale a la operación entre conjuntos $X \cup Y - X \cap Y$

**Retorna:**
-  `set`.

---
**update**:

`set.union()`: Retorna todos los elementos de dos sets `X` y `Y`, eliminando duplicados.
```python
X.union(Y)
```

**Parámetros:**
- **`X`** \- `set`: Un objeto de tipo set.
- **`Y`** \- `iterable`: Cualquier otro objeto iterable.

**Notas:**
- Equivale a la expresión de python `X | Y`.
- Equivale a la operación entre conjuntos $X \cup Y$

**Retorna:**
-  `None`.

---
(subsection:op-conjuntos)=
### Operaciones entre conjuntos in-place

Métodos para las operaciones entre dos o más conjuntos (sets), que actualizan los valores de uno de ellos en lugar de retornar un objeto con el resultado.

---
**difference_update**:

`set.difference_update()`: Actualiza el `set` `X` con los elementos que solo están en el `set` `X` pero no en el `set` `Y`.
```python
X.difference_update(Y, ...)
```

**Parámetros:**
- **`X`** \- `set`: Un objeto de tipo set.
- **`Y`** \- `iterable`: Cualquier otro objeto iterable. Puede ser más de un iterable, separados por coma

**Notas:**
- Equivale a la expresión de python `X -= Y`
- Equivale a la operación entre conjuntos $X = X - X \cap X$

**Retorna:**
-  `None`.

---
**intersection_update**:

`set.intersection_update()`: Actualiza el `set` `X`, para que solo incluya los elementos en común de dos sets `X` y `Y`.
```python
X.intersection_update(Y, ...)
```

**Parámetros:**
- **`X`** \- `set`: Un objeto de tipo set.
- **`Y`** \- `iterable`: Cualquier otro objeto iterable. Puede ser más de un iterable, separados por coma

**Notas:**
- Equivale a la expresión de python `X &= Y`.
- Equivale a la operación entre conjuntos $X = X \cap Y$

**Retorna:**
-  `None`.

---
**symmetric_difference_update**:

`set.symmetric_difference_update()`: Actualiza el `set` `X` con los elementos de dos sets`X` y `Y`, excepto aquellos que tienen en común. equivale a `X ^= Y`.
```python
X.symmetric_difference(Y)
```

**Parámetros:**
- **`X`** \- `set`: Un objeto de tipo set.
- **`Y`** \- `iterable`: Cualquier otro objeto iterable.

**Notas:**
- Equivale a la expresión de python `X ^= Y`.
- Equivale a la operación entre conjuntos $X = X \cup Y - X \cap Y$

**Retorna:**
-  `None`.

---
**update**:

`set.update()`: Actualiza un `set` `X` con los elementos de`X`, solo aquellos que no están en ambos sets. 
```python
X.update(Y)
```

**Parámetros:**
- **`X`** \- `set`: Un objeto de tipo set: X `set`. un objeto de tipo `set`
- **`Y`** \- `set`: Un objeto de tipo set: Y `set`. un objeto de tipo `set`

**Notas:**
- Equivale a la expresión de python `X |= Y`.
- Equivale a la operación entre conjuntos $X = X \cup Y$

**Retorna:**
-  `None`.