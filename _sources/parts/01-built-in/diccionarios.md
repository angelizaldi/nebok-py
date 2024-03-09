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

# Diccionarios

Corresponde al tipo de dato `dict`. Algunas características de las diccionarios, son:
- Utilizan un formato `key-value` para almacenar valores.
- Es mutable: Se puede modificar una vez creado.
- Sus elementos no están ordenados, es decir, no se puede acceder a sus elementos por medio de índices.
- Es un iterable: Se puede iterar por sus elementos y se puede utilizar la palabra reservada `in` para verificar membresía de llaves.
- Se puede hacer _subsetting_.

Para más información visitar la [documentación](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict) de Python.

<br/>

---
## Crear un diccionario

Existen dos métodos principales para crear una diccionario:


**1.** Poner los elementos en un par `key: value`, separados por coma, dentro de llaves `{}`:
```python
# Crear un diccionario con llaves
X = {key1: value1, key2: value2, ...}
```

**2.** Usar la función `dict()`, para ello existen diversas formas de definir el diccionario:
```python
# Usando key=value dentro de dict()
X = dict(key1=value1, key2=value2, ...)

# Usando una lista de tuplas con pares (key, value)
X = dict([(key1, value1), (key2, value2), ...])
```
- Los _key_ de un diccionario deben de ser de un tipo inmutable, lo más común es usar cadenas, números o valores `bool` y además deben de ser únicas, es decir, no puede haber dos o más elementos con la misma llave.
- Los _value_ pueden ser cualquier tipo de objeto.


```{warning}
Al crear un diccionario el objeto `X` en realidad hace referencia a los elementos que se almacenan en memoria, si se asigna el diccionario a otro objeto `Y` con el operador de asignación, es decir `Y=X`, entonces lo que se copia es la referencia, no los valores como tal, entonces modificaciones en `Y` también afecta a `X` y vicerversa. Para que esto no suceda se puede usar:
- `Y = dict(X)`
- `Y = X.copy()`

De esta manera modificaciones en `Y` no afectarán a `X` y viceversa
```

Otra forma de crear un diccionario es con {ref}`dict-comp`.

<br/>

---
##  Agregrar elementos

Para agregar elementos a un diccionario simplemente poner entre corchetes el nombre de la nueva llave y con el operador de asignación darle un valor.
```python
# Si X es un diccionario
X['key'] = val
```

```{note}
Otra forma de agregar elementos con métodos es con:
- Agregar elementos desde otro objeto: `dict.update()`.

Revisar {ref}`Metodos agregar elementos <dict-metodos-agregar>`
```

<br/>

---
## Eliminar Elementos

Para eliminar un elemento específico o el diccionario completo usar la palabra reservada `del` y el elemento que se quiere eliminar:
```python
# Eliminar el par key-value del diccionario X
del X['key'] 

# Eliminar el diccionario X
del X
```

```{note}
Otras formas de eliminar elementos con métodos son:
- Para remover un elemento específico usar el método `dict.pop()`.
- Para remover y retornar un elemento de un índice en específico usar el método `dict.popitem()`.
- Para todos los elementos usar el método `dict.clear()`.

Revisar {ref}`Métodos eliminar elementos <dict-metodos-eliminar>`
```

<br/>

---
## Selección de elementos

Para acceder a los elementos de un diccionario se puede utilizar el nombre de la _key_, entre corchetes:
```python
# X es un diccionario
X['key']
```

```{note}
Otras formas de acceder a valores con métodos son:
- Acceder a un elemento con una llave en específico: `dict.get()`.
- Acceder a todos los valores: `dict.values()`
- Acceder a todas las llaves: `dict.keys()`
- Accedes a todos los pares `key-value`: `dict.items()`

Revisar {ref}`Metodos acceder a elementos <dict-metodos-acceder>`
```

<br/>

---
## Modificar Elementos

Para modificar el valor de una llave en específico usar el nombre de la llave y el operador de asignación:
```python
# Modificar el valor correspondiento a la llave 'key'
X['key'] = val
```

<br/>

---
## Verificar membresía

Para verificar si una llave existe en un diccionario usar el operador de membresía `in` junto con el nombre de la llave del elemento:
```python
# Verificar que 'key' exista en X.
"key" in X
```
- Alternativamente se puede usar `not in`.

<br/>

---
## Iteración

Para iterar sobre los elementos de un diccionario se puede usar un `for loop`. Algunas opciones de iteración son:
```python
# Iterar sobre las llaves del diccionario X:
# Opción 1:
for key in X:
    # for body
   
# Opción 2:
for key in X.keys():
    # for body
        
# Iterar sobre los valores del diccionario X:
for value in X.values():
    # for body
    
# Iterar sobre los pares key-value del diccionario X:
for key, value in X.items():
    # for body
```
- En todos los ejemplos anteriores `key` y `value` son nombres opcionales.
- Notar que si se itera directamente en un diccionario por default se iterará sobre las llaves.

<br/>

---
(dict-comp)=
## Dict comprehesions

Son diccionarios que se crean a partir procesos iterativos con la estructura `for loop`. Sintaxis.
```python
X = {key_expression : value_expression for i in collection}
```

Los diccionarios pueden tener condicionales, en la parte de _collection_, de manera que solo a ciertos elementos se les aplique el código. Sintaxis de las condicionales:
```python
# dict comprehension con condicional en collection
X = {key_expression : value_expression for i in collection if condition]
```

<br/>

---
## Métodos

En esta sección se enlistan los métodos del tipo `dict` por categorias. 

Tener en cuenta que los métodos generalmente se aplican sobre un objeto de tipo `dict`, por ejemplo, si `X` es `dict`, entonces se utiliza <code>X.<i>method_name</i></code>. Sin embargo es posible usar el diccionario como argumento de <code>dict.<i>method_name</i></code>. Por ejemplo.

```{code-cell} ipython3
# Definir el diccionario
X = {"a": 1, "b": 2, "c": 3}

# Usar el metodo sobre el objeto
print(X.keys())

# Equivale a:
print(dict.keys(X))
```
- Tener en cuenta que en la segunda forma el diccionario siempre debe de ser el primer argumento.

<br/>

### Acceder a elementos

Métodos para recuperar las llaves, los valores o ambos de un diccionario.

```{list-table}
:header-rows: 1
:name: dict-metodos-acceder

* - Método
  - Descripción
* - [get](https://docs.python.org/3/library/stdtypes.html#dict.get)(key[, default])
  - Devuelve el valor de la llave si la llave está en el diccionario, de lo contrario, el valor predeterminado. Si no se proporciona el valor predeterminado, el valor predeterminado es `None`, de modo que este método nunca retorn `KeyError`.
* - [items](https://docs.python.org/3/library/stdtypes.html#dict.items)()
  - Devuelve una `view` de los elementos del diccionario (clave, valor).
* - [keys](https://docs.python.org/3/library/stdtypes.html#dict.keys)()
  - Devuelve una `view` de las llaves del diccionario.
* - [values](https://docs.python.org/3/library/stdtypes.html#dict.values)()
  - Devuelve una `view` de los valores del diccionario.
```

<br/>

---
### Agregar elementos

Métodos para agregar elementos a un diccionario.

```{list-table}
:header-rows: 1
:name: dict-metodos-agregar

* - Método
  - Descripción
* - [update](https://docs.python.org/3/library/stdtypes.html#dict.update)([other])
  - Actualiza el diccionario con los pares llave/valor de `other`, sobrescribiendo llaves existentes. Realiza la operación in-place.
```

<br/>

---
### Eliminar elementos

Métodos para eliminar elementos de un diccionario.

```{list-table}
:header-rows: 1
:name: dict-metodos-eliminar

* - Método
  - Descripción
* - [clear](https://docs.python.org/3/library/stdtypes.html#dict.clear)()
  - Remueve todos los elementos del diccionario.
* - [pop](https://docs.python.org/3/library/stdtypes.html#dict.pop)(key[, default])
  - Si la llave está en el diccionario, elimina la llave y retorna su valor, de lo contrario, retorna `default`. Si no se proporciona el valor `default` y la llave no está en el diccionario, se genera un `KeyError`.
* - [popitem](https://docs.python.org/3/library/stdtypes.html#dict.popitem)()
  - Elimina y devuelve un par (clave, valor) del diccionario. Los pares se devuelven en orden _LIFO_.
```

<br/>

---
### Otros

Otros métodos de diccionarios.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [copy](https://docs.python.org/3/library/stdtypes.html#dict.copy)()
  - Devuelve una copia superficial del diccionario.
* - [fromkeys](https://docs.python.org/3/library/stdtypes.html#dict.fromkeys)(iterable[, value])
  - Crea un nuevo diccionario con llaves del `iterable` y los valores se establecen como `value`.
* - [setdefault](https://docs.python.org/3/library/stdtypes.html#dict.setdefault)(key[, default])
  - Retorna el valor de una llave especificada, si la llave no existe, inserta la llave con el valor especificado.
```

<br/>

---
## Funciones útiles para diccionarios

Algunas funciones built-in útiles para dicionarios son:
- `len()`: Encontrar la longitud (número de elementos) del diccionario.
