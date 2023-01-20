# Diccionarios

Correspnden al tipo de dato `list`. Las listas son un `iterable`. Algunas características de las diccionarios, son:
- Utilizan un formato `key-value` para almacenar valores.
- Es mutable: Se puede modificar una vez creado.
- Sus elementos no están ordenados.
- Es un iterable: Se puede iterar por sus elementos y se puede utilizar la palabra reservada `in` para verificar membresía de llaves.
- Se puede hacer _subsetting_.

---
## Crear un diccionario:
Existen dos métodos principales para crear una diccionario
1. Poner los elementos en un par `key: value`, separados por coma, dentro de llaves `{}`:
```python
X = {key1: value1, key2: value2, ...}
```
2. Poner los elementos en un par `key=value`, separados por coma, dentro del constructor `dict()`:
```python
X = dict(key1=value1, key2=value2, ...)
```
- En ambos casos las _key_ deben de ser de un tipo inmutable, lo más común es usar cadenas, números o valor `bool` y además deben de ser únicas, es decir, no puede haber dos o más elementos con la misma llave.
- Los _value_ pueden ser cualquier tipo de objeto.


Otra forma de crear un diccionario es con {doc}`12-3--comprehession.md`.

---
##  Agregrar elementos:

Para agregar elementos a un diccionario simplemente poner entre corchetes el nombre de la nueva llave y con el operador de asignación darle un valor.
```python
# Si X es un diccionario:
X['key'] = val
```

```{note}
Otras formas de agregar elementos usando métodos:
- Para agregar algún elemento al diccionario usar el método `dict.append`.
```

---
## Eliminar Elementos:

Para eliminar un elemento específico o el diccionario completo usar la palabra reservada `del` y el elemento que se quiere eliminar:
```python
# Eliminar el par key-value que corresponde a la llave 'key' del diccionario X
del X['key'] 

# Eliminar el diccionario X
del X
```

```{note}
Otras formas de eliminar elementos con métodos son:
- Para remover un elemento específico usar el método `dict.pop`.
- Para remover un elemento de un índice en específico usar el método `dict.popitem`.
- Para remover un elemento de un índice en específico usar el método `dict.clear`.
```

---
## Modificar Elementos:

Para modificar el valor de una llave en específico usar el nombre de la llave y el operador de asignación:
```python
# Modifcar el valor correspondiento a la llave `key`
X['key'] = val
```

```{note}
Otra forma de modificar valores con método es:
- Modificar el valor de una llave en específico `dict.update`.
```

```{warning}
Al crear un diccionario el objeto `X` en realidad hace referencia a los elementos que se almacenan en memoria, si se asigna el diccionario a otro objeto `Y` con el operador de asignación, entonces lo que se copia es la referencia, no los valores como tal, entonces modificaciones en `Y` también afecta a `X` y vicerversa. Para que esto no suceda se puede usar:
- Y = dict(X)
- Y = X.copy()

De esta manera modificaciones en `Y` no afectarán a `X` y viceversa
```

---
## Verificar membresía:
Para ver si un elemento está dentro de un diccionario usar el operador de membresía `in` junto con el nombre de la llave del elemento:
```python
# Verificar que 'key' exista en X.
"key" in X
```

---
## Selección de elementos: 

Para acceder a los elementos de un diccionario se puede utilizar el nombre de la _key_, entre corchetes:
```python
# X es un diccionario
X['key']
```

```{note}
Otras formas de acceder a valores con métodos sin:
- Acceder a un elemento con una llave en específico: `dict.get`.
- Acceder a los los valores: `dict.values`
- Acceder a todas las llaves: `dict.keys`
- Accedes a todos los pares `key-value`: `dict.items`
```

---
## Iteración:
Para interar sobre todos los elementos de un diccionario se puede usar un `for loop`. Algunas opciones de iteración son:
```python
# Iterar sobre las llaves del diccionario X:
# Opción 1:
for key in X:
    expression
   
# Opción 2:
for key in X.keys():
    expression
        
# Iterar sobre los valoes del diccionario X:
for value in X.values():
    expression
    
# Iterar sobre los pares key-value del diccionario X:
for key, value in X.items():
    expression
```
- En todos los ejemplos anteriores `key` y `value` son nombres opcionales.
- Notar que se se itera directamente en un diccionario por default se iterará sobre las llaves.
