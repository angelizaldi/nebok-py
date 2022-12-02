# Métodos de sets
Aquí se enlistas todos los métodos del tipo `set`.

---
## Agregar elementos
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
## Eliminar Elementos
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
## Información
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
## Operaciones entre conjuntos

Métodos para las operaciones entre dos o más conjuntos (sets) que retornan un objeto nuevo con el resultado.

---
**difference**:

`set.difference()`: Retorna los elementos que solo están en el `set` `X` pero no en el `set` `Y`.
```python
X.difference(Y, […])
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
X.intersection(Y, […])
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
## Operaciones entre conjuntos in-place

Métodos para las operaciones entre dos o más conjuntos (sets), que actualizan los valores de uno de ellos en lugar de retornar un objeto con el resultado.

---
**difference_update**:

`set.difference_update()`: Actualiza el `set` `X` con los elementos que solo están en el `set` `X` pero no en el `set` `Y`.
```python
X.difference_update(Y, […])
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
X.intersection_update(Y, […])
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