# Métodos

## Acceder a contenido

Métodos para acceder a los valores de las llaves, valores o ambos.

---
**get**:

`dict.get()`: Retorna el valor de una llave especifica.
```python
X.get(key, [value = None])
```

**Parámetros:**
- **`X`** \- `dict`: Diccionario.
- **`key`** \- `object`: Es el nombre de la llave.
- **`value`** \- `object`, `None`: Es un valor que se regresará si la llave no existe.

**Retorna:**
-  `object`.

---
**items**:

`dict.items()`: Retorna una lista que contiene un `tuple` para cada par llave-valor.
```python
X.items()
```

**Parámetros:**
- **`X`** \- `dict`: Diccionario.
- No tiene argumentos.

**Retorna:**
-  `list` de `tuple`.


---
**keys**:

`dict.keys()`: Retorna una lista que contiene todas las llaves del diccionario.
```python
X.keys()
```

**Parámetros:**
- **`X`** \- `dict`: Diccionario.
- No tiene argumentos.

**Retorna:**
-  `list`.

---
**values**:

`dict.values()`: Retorna una lista con los valores del diccionario.
```python
X.values()
```

**Parámetros:**
- **`X`** \- `dict`: Diccionario.
- No tiene argumentos.

**Retorna:**
-  `list`.


---
**setdefault**:

`dict.setdefault()`: Retorna el valor de una llave especificada, si la llave no existe, inserta la llave con el valor especificado _in-place_.
```python
X.setdefault(key, [value=None])
```

**Parámetros:**
- **`X`** \- `dict`: Diccionario.
- **`key`** \- `object`: Es el nombre de la llave.
- **`value`** \- `object`: Es el valor que tendrá la llave si la llave no existe.

**Retorna:**
-  `object`, `None`.

## Agregar elementos

Métodos para agregar elementos a un diccionario existente.

---
**update**:

`dict.update()`: Actualiza el diccionario con las llaves y valores especificados _in-place_. También se puede utilizar para actualizar el valor de una llave.
```python
X.update(iterable)
```

**Parámetros:**
- **`X`** \- `dict`: Diccionario.
- **`iterable`** \- `dict` o `iterable`: Un objeto con pares llaves-valor que se insertarán al diccionario.

**Retorna:**
-  `None`.

## Eliminar elementos

Métodos para eliminar elementos.

---
**clear**:

`dict.clear()`: Remueve todos los elementos del diccionario _in-place_.
```python
X.clear()
```

**Parámetros:**
- **`X`** \- `dict`: Diccionario.
- No tiene argumentos.

**Retorna:**
-  `None`.

---
**pop**:

`dict.pop()`: Remueve un elemento de una llave en específico y retorna el valor.
```python
X.pop(key, [default])
```

**Parámetros:**
- **`X`** \- `dict`: Diccionario.
- **`key`** \- `object`: Es el nombre de la llave.
- **`default`** \- `object`: Es un valor a retornar si la llave no existe. Si no se especifica este argumento y la llave no existe entonces se producirá un error.

**Retorna:**
-  `object`.

---
**popitem**:

`dict.popitem()`: Remueve y retorna el último par llave-valor del diccionario (python 3.7+).
```python
X.popitem()
```

**Parámetros:**
- **`X`** \- `dict`: Diccionario.
- No tiene argumentos.

**Retorna:**
-  `tuple`.

## Otros

Otros métodos del tipo `dict`.

---
**copy**:

`dict.copy()`: Crea una copia del diccionario.
```python
X.copy()
```

**Parámetros:**
- **`X`** \- `dict`: Diccionario.

**Retorna:**
-  `dict`.

---
**fromkeys**:

`dict.fromkeys()`: Crea un diccionario con las llaves y valores especificados.
```python
dict.fromkeys(keys, [values=None])
```

**Parámetros:**
- **`keys`** \- `iterable`: Objeto.
- **`values`** \- `None`, `object`: Es un valor default para todos los elementos.

**Retorna:**
-  `dict`.
