# Collections

Es un módulo que provee de "_containers_" especializados que expanden las funcionalidades de las listas, diccionacios, tuplas y sets. Es necesario importarlo.

```python
# Importar todo el módulo
import collections

# Importar una clase específica
from collections import class_name
```
- _class_name_ es el nombre de la clase que se desea importar.

```{warning}
- En esta sección solo se presentarán algunos tipos de datos de este módulo y de cada tipo solo se presentarán algunos métodos y atributos. Para una lista completa visitar la [página oficial](https://docs.python.org/3/library/collections.html) de Python.
- La información de esta sección está basada en la documentación de Python 3.11.
```

---
## Counter

Es una subclase de `dict` que permite conocer el número de veces que se repite un elemento en un objeto `iterable`.

**Counter**:

`collections.Counter()`: Retorna un objeto similar a un diccionario con cada elemento único de un iterable y el número de veces que aparece ese elemento en el iterable, ordenado de manera descendente.
```python
collections.Counter(X)
```

**Parámetros:**
- **`X`** \- `iterable`: Objeto.


**Retorna:**
- `Counter`.

Se puede  crear un counter desde cero:
```python
collections.Counter('key1'=val1, 'key2'=val2, ...)
```
- '_key1_', '_key2_', ... \- `str`: Son los nombres que tendrán las llaves.
- val1, val2, ... \- `int`: Son el número de veces que se repite ese elemento. Puede ser cero o incluso números negativos.

---
### Métodos

Los métodos de `dict` están disponibles para `Counter` a excepción de `.fromkeys()`, mientras que el método `.update()` tiene un comportamiento diferente. Los métodos exclusivos de `Counter` son:

```{list-table} Métodos de Counter
:header-rows: 1

* - Funciones
  - Descripción
  - Sintaxis
* - [elements](#elements)
  - Retorna los elementos del counter en la misma cantidad de veces que tiene en el counter.
  - `X.elements()`
* - [most_common](#most_common)
  - Devuelve los n elementos con más repeticiones.
  - `X.most_common([n])`
* - [total](#total)
  - Devuelve la suma de los conteos.
  - `X.total()`
```

```{attention}
Métodos no cubiertos en este sitio:
- `.subtract()`.
- `.update()`.
```

---
<a name='elements'></a>
**elements**:

`collections.Counter.elements()`: Retorna los elementos del counter en la misma cantidad de veces que tiene en el counter.
```python
X.elements()
```

**Parámetros:**
- **`X`** \- `Counter`: Es un objeto creado con `Counter()`.


**Retorna:**
- `list`.

<br><br>

---
<a name='most_common'></a>
**most_common**:

`collections.Counter.most_common()`: Devuelve los _n_ elementos con más repeticiones.
```python
X.most_common([n])
```

**Parámetros:**
- **`X`** \- `Counter`: Es un objeto creado con `Counter()`.
- **`n`** \- `int`: Número de elementos a mostar.
- Se puede encontrar los n elementos menos comunes con `X.most_common()[:-n-1:-1]`.


**Retorna:**
- `list` de `tuple`.

<br><br>

---
<a name='total'></a>
**total**:

`collections.Counter.total()`: Devuelve la suma de los conteos.
```python
X.total()
```

**Parámetros:**
- **`X`** \- `Counter`: Es un objeto creado con `Counter()`.


**Retorna:**
- `int`.

<br><br>

---
## Deque

Es similar `list` pero optimizado para eliminar y agregar elementos. 

**deque**:

`collections.deque()`: Retorna un objeto deque con los datos de iterable, si no se especifica, se inicializa un deque vacío.
```python
collections.deque(iterable=None, maxlen=None)
```

**Parámetros:**
- **`iterable`** \- `iterable`: Objeto sobre el cual se recuperarán los datos para inicializar el deque.
- **`maxlen`** \- `int`: Longitud máxima del deque, si no se especifica el deque puede crecer hasta una longitud arbitraria.


**Retorna:**
- `deque`.

---
### Atributos

**maxlen**:

`collections.deque.maxlen()`: Retorna la longitud máxima que puede tener el deque. Si no tiene longitud máxima retorna `None`.
```python
X.maxlen
```

**Parámetros:**
- **`X`** \- `deque`: Objeto.


**Retorna:**
- `int` o `None`.

<br><br>

---
### Métodos

#### Agregar elementos

```{list-table} Agregar elementos.
:header-rows: 1

* - Funciones
  - Descripción
  - Sintaxis
* - [append](#append)
  - Agrega un elemento al final de un deque, el elemento es un número, una cadena, una lista, etc.
  - `X.append(Y)`
* - [appendleft](#appendleft)
  - Agrega un elemento al incio de un deque, el elemento es un número, una cadena, una lista, etc.
  - `X.appendleft(Y)`
* - [extend](#extend)
  - Agrega elementos de un objeto iterable al final del deque.
  - `X.extend(Y)`
* - [extendleft](#extendleft)
  - Agrega elementos de un objeto iterable al incio del deque.
  - `X.extendleft(Y)`
* - [insert](#insert)
  - Inserta un elemento a un índice en específico, recorriendo el resto de los elementos a la derecha. Si el elemento provoca que se viole maxlen se arroja un IndexError.
  - `X.insert(i, Y)`
```

#### Eliminar elementos

```{list-table} Eliminar elementos.
:header-rows: 1

* - Funciones
  - Descripción
  - Sintaxis
* - [pop](#pop)
  - Remueve y retorna el último elemento.
  - `X.pop()`
* - [popleft](#popleft)
  - Remueve y retorna el primer elemento.
  - `X.popleft()`
* - [remove](#remove)
  - Elimina la primer coincidencia de un elemento en la lista. Si no se encuentra el elemento se retorna un error `ValueError`.
  - `X.remove(Y)`
```

#### Información

```{list-table} Información.
:header-rows: 1

* - Funciones
  - Descripción
  - Sintaxis
* - [count](#count)
  - Devuelve el número de veces que hay un elemento específico en el deque, el elemento es un número, una cadena, etc.
  - `X.count(Y)`
* - [index](#index)
  - Devuelve el índice en el que se encuentra un elemento. Retorna `IndexError` si el valor no está en la lista.
  - `X.index(Y, [start = 0], [end = -1])`
```

#### Modificar

```{list-table} Modificar
:header-rows: 1

* - Funciones
  - Descripción
  - Sintaxis
* - [reverse](#reverse)
  - Modifica el orden del deque de manera inversa in-place.
  - `X.reverse()`
* - [rotate](#rotate)
  - Desplaza los elementos a la derecha o izquierda n posiciones.
  - `X.rotate(n=1)`
```

#### Otros

```{list-table} Otros métodos.
:header-rows: 1

* - Funciones
  - Descripción
  - Sintaxis
* - [clear](#clear)
  - Remueve todos los elementos del deque.
  - `X.clear()`
* - [copy](#copy)
  - Crea una copia del deque.
  - `X.copy()`
```

#### Listado de métodos

---
<a name='append'></a>
**append**:

`collections.deque.append()`: Agrega un elemento al final de un deque, el elemento es un número, una cadena, una lista, etc.
```python
X.append(Y)
```

**Parámetros:**
- **`X`** \- `deque`: Objeto.
- **`Y`** \- `object`: Elemento a agregar.


**Retorna:**
- `None`.

<br><br>

---
<a name='appendleft'></a>
**appendleft**:

`collections.deque.appendleft()`: Agrega un elemento al incio de un deque, el elemento es un número, una cadena, una lista, etc.
```python
X.appendleft(Y)
```

**Parámetros:**
- **`X`** \- `deque`: Objeto.
- **`Y`** \- `object`: Elemento a agregar.


**Retorna:**
- `None`.

<br><br>

---
<a name='extend'></a>
**extend**:

`collections.deque.extend()`: Agrega elementos de un objeto iterable al final del deque.
```python
X.extend(Y)
```

**Parámetros:**
- **`X`** \- `deque`: Objeto.
- **`Y`** \- `iterable`: Objeto cuyos elementos se agregarán al `deque`.


**Retorna:**
- `None`.

<br><br>

---
<a name='extendleft'></a>
**extendleft**:

`collections.deque.extendleft()`: Agrega elementos de un objeto iterable al incio del deque.
```python
X.extendleft(Y)
```

**Parámetros:**
- **`X`** \- `deque`: Objeto.
- **`Y`** \- `iterable`: Objeto cuyos elementos se agregarán al `deque`.


**Retorna:**
- `None`.

<br><br>

---
<a name='insert'></a>
**insert**:

`collections.deque.insert()`: Inserta un elemento a un índice en específico, recorriendo el resto de los elementos a la derecha. Si el elemento provoca que se viole maxlen se arroja un IndexError.
```python
X.insert(i, Y)
```

**Parámetros:**
- **`X`** \- `deque`: Objeto.
- **`i`** \- `int`: Es el índice.
- **`Y`** \- `object`: Un número, una cadena, etc.


**Retorna:**
- `None`.

<br><br>

---
<a name='pop'></a>
**pop**:

`collections.deque.pop()`: Remueve y retorna el último elemento.
```python
X.pop()
```

**Parámetros:**
- **`X`** \- `deque`: Objeto.


**Retorna:**
- `object` o `IndexError`.

<br><br>

---
<a name='popleft'></a>
**popleft**:

`collections.deque.popleft()`: Remueve y retorna el primer elemento.
```python
X.popleft()
```

**Parámetros:**
- **`X`** \- `deque`: Objeto.


**Retorna:**
- `object` o `IndexError`.

<br><br>

---
<a name='remove'></a>
**remove**:

`collections.deque.remove()`: Elimina la primer coincidencia de un elemento en la lista. Si no se encuentra el elemento se retorna un error `ValueError`.
```python
X.remove(Y)
```

**Parámetros:**
- **`X`** \- `deque`: Objeto.
- **`Y`** \- `object`: Un número, una cadena, etc.


**Retorna:**
- `None` o `ValueError`.

<br><br>

---
<a name='count'></a>
**count**:

`collections.deque.count()`: Devuelve el número de veces que hay un elemento específico en el deque, el elemento es un número, una cadena, etc.
```python
X.count(Y)
```

**Parámetros:**
- **`X`** \- `deque`: Objeto.
- **`Y`** \- `object`: Un número, una cadena, etc.


**Retorna:**
- `int`.

<br><br>

---
<a name='index'></a>
**index**:

`collections.deque.index()`: Devuelve el índice en el que se encuentra un elemento. Retorna `IndexError` si el valor no está en la lista.
```python
X.index(Y, [start = 0], [end = -1])
```

**Parámetros:**
- **`X`** \- `deque`: Objeto.
- **`Y`** \- `object`: Un número, una cadena, etc.
- **`start`**, **`end`** \- `int`: Indican desde cuál indice empezar a buscar y hasta cuál.


**Retorna:**
- `int` o `IndexError`.

<br><br>

---
<a name='reverse'></a>
**reverse**:

`collections.deque.reverse()`: Modifica el orden del deque de manera inversa in-place.
```python
X.reverse()
```

**Parámetros:**
- **`X`** \- `deque`: Objeto.


**Retorna:**
- `None`.

<br><br>

---
<a name='rotate'></a>
**rotate**:

`collections.deque.rotate()`: Desplaza los elementos a la derecha o izquierda n posiciones.
```python
X.rotate(n=1)
```

**Parámetros:**
- **`X`** \- `deque`: Objeto.
- **`n`** \- `int`: Número entero, si es positivo desplazará a la derecha, si es negativo desplazará a la izquierda.


**Retorna:**
- `None`.

<br><br>

---
<a name='clear'></a>
**clear**:

`collections.deque.clear()`: Remueve todos los elementos del deque.
```python
X.clear()
```

**Parámetros:**
- **`X`** \- `deque`: Objeto.


**Retorna:**
- `None`.

<br><br>

---
<a name='copy'></a>
**copy**:

`collections.deque.copy()`: Crea una copia del deque.
```python
X.copy()
```

**Parámetros:**
- **`X`** \- `deque`: Objeto.


**Retorna:**
- `list`.

<br><br>

## Default dict

Es una subclase de `dict`, es como un diccionario que permite que si se trata de acceder a un key que no existe, en lugar de arrojar un error, crea esa _key_ como un tipo de dato específico. 

**defaultdict**:

`collections.defaultdict()`: Crea un diccionario 
```python
collections.dafaultdict(type)
```

**Parámetros:**
- **`type`** \- `type`: Es el nombre del tipo que tendrá el valor por default, por ejemplo `str`, `list`, `int`, etc. El primer valor que tendrá esa key será el mismo que el retornado por el constructor del tipo, por ejemplo, si `type=int` entonces el primer valor de la _key_ será `int()` que es el número 0. 


**Retorna:**
- `defaultdict`.

<br><br>

Los métodos y la funcionalidad de `defaultdict` es la misma que la de {doc}`../01-built-in/12-diccionarios.md`, a excepción de lo anteriormente explicado.

## Named tuple

`namedtuple` es como un `tuple` pero sus elementos tienen nombre, lo que permite que se pueda acceder a los elementos por el nombre.


**namedtuple**:

`collections.namedtuple()`: Retorna una subclase de `tuple`. Esta clase permite crear `namedtuples`, pero no retorna un `nametuple`.
```python
collections.namedtuple(typename, field_names, *, rename=False, defaults=None, module=None)
```

**Parámetros:**
- **`typename`** \- `str`: Es el nombre que tendrá el `tuple`.
- **`field_names`** \- `list` de `str` o `str`: Es el nombre que tendrá cada elemento
    - Si es una lista, cada nombre está separado por coma. 
    - Si es cadena, los nombres de separan por coma o especios: `"name1, name2, ..."` o `"name1, name2, ..."`.

**Retorna:**
- `typename`.


Posteriormente para llenar el `namedtuple` se usa:
```python
X(name1=val1, name2=val2, ...)
```
- _X_ \- `typename`: Es un objeto creado con `collections.namedtuple()`.
- _name1_, _name2_, ...: Son los nombre de los elementos que se pusieron en `field_names` en la función `collections.namedtuple()`. Se pueden poner los valores por nombre o por posición.
- _val1_, _val2_ \- `object`: Son los valores que tendrán esos campos.


Para acceder a los elementos del `namedtuple` se puede usar:
```python
# Acceder al elemento i con su nombre con notación .
X.name

# Acceder al elemento i con su nombre con notación []
X["name"]

# Acceder al elemento i con su índice
X[i]
```