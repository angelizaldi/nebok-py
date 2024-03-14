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

# Collections

Es un módulo que provee de "_containers_" especializados que expanden las funcionalidades de las listas, diccionarios, tuplas y sets. Es necesario importarlo.

```python
# Importar todo el módulo
import collections

# Importar una clase específica
from collections import class_name
```
- _class_name_ es el nombre de la clase que se desea importar.

<br>

A continuación se presenta una lista completa de los contenedores especializados de este módulo.

| Contenedor | Descripción |
| :---: | :---------- |
|[namedtuple](https://docs.python.org/3/library/collections.html#namedtuple-factory-function-for-tuples-with-named-fields) | Función de fábrica para crear subclases de tuplas con elementos con nombres. |
|[deque](https://docs.python.org/3/library/collections.html#deque-objects) | Contenedor similar a `list` con inserciones y eliminaciones rápidas en ambos extremos. |
|[ChainMap](https://docs.python.org/3/library/collections.html#chainmap-objects) | Clase similar a un diccionario para crear una vista única de varios mapeos. |
|[Counter](https://docs.python.org/3/library/collections.html#counter-objects) | Subclase de diccionario para contar objetos _hashable_. |
|[OrderedDict](https://docs.python.org/3/library/collections.html#ordereddict-objects) | Subclase de diccionario que respeta el orden en que se agregaron las entradas. |
|[defaultdict](https://docs.python.org/3/library/collections.html#defaultdict-objects) | Subclase de diccionario con valores por default para valores perdidos. |
|[UserDict](https://docs.python.org/3/library/collections.html#userdict-objects) | Envoltorio alrededor de objetos `dict` para facilitar la subclasificación de diccionarios. |
|[UserList](https://docs.python.org/3/library/collections.html#userlist-objects) | Envoltorio alrededor de objetos `list` para facilitar la subclasificación de listas. |
|[UserString](https://docs.python.org/3/library/collections.html#userstring-objects) | Envoltorio alrededor de objetos `str` para facilitar la subclasificación de cadenas. |

```{warning}
En esta sección solo se presentarán algunas clases de este módulo y de cada clase solo se presentarán algunos métodos y atributos. Para más información presionar en el nombre de cada contenedor lo cual lleva a la documentación oficial de Python.
```

<br/>

---
## Counter

Es una subclase de `dict` que permite conocer el número de veces que se repite un elemento en un objeto `iterable`.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [Counter](https://docs.python.org/3/library/collections.html#collections.Counter)([iterable-or-mapping])
  - Un `Counter` es una subclase de `dict` para contar objetos _hashable_. Es una colección donde los elementos se almacenan como claves de diccionario y sus recuentos se almacenan como valores de diccionario.
```

<br/>

### Crear un `Counter`

Para crear un objeto `Counter` se usa el constructor `collections.Counter()`, existen dos formas de crear el `Counter`

**1.** Desde un `iterable`: Se pasa como argumento un objeto iterable. En este caso se retornará el `Counter` con el número de veces que aparece cada elemento en el iterable.
```python
# Importar el módulo
import collections

# Si Y es un iterable
X = collections.Counter(Y)
```

**2.** Desde un _mapping_: Se pasa como argumento un diccionario o pares `key=value` separados por coma. En este caso se indica directamente el recuento (`value`) de cada elemento `key` en el `Counter`.
```python
# Importar el módulo
import collections

# Crear un counter con key=value
collections.Counter('key1'=val1, 'key2'=val2, ...)
```
- '_key1_', '_key2_', ... \- `str`: Son los nombres que tendrán las llaves.
- val1, val2, ... \- `int`: Son los recuentos de los elemento. Puede ser cero o incluso números negativos.

:::{tip}
Si se tienen dos objetos `Counter` con _keys_ en común se pueden sumar sus respectivos recuentos con el operador `+`.
:::

<br/>

---
### Métodos

Los métodos de `dict` están disponibles para `Counter` a excepción de `dict.fromkeys()`, mientras que el método `.update()` tiene un comportamiento diferente. Los métodos exclusivos de `Counter` son:

```{list-table}
:header-rows: 1

* - Funciones
  - Descripción
* - [elements](https://docs.python.org/3/library/collections.html#collections.Counter.elements)()
  - Retorna un `iterator` con los elementos del `Counter` repitiendo cada uno tantas veces como su contador.
* - [most_common](https://docs.python.org/3/library/collections.html#collections.Counter.most_common)([n])
  - Devuelve una lista de los `n` elementos más comunes y sus recuentos de la más comunes a los menos. Si se omite `n` o es `None`, `most_common()` devuelve todos los elementos del contador.
* - [subtract](https://docs.python.org/3/library/collections.html#collections.Counter.subtract)([iterable-or-mapping])
  - Los elementos se sustraen de un iterable o de otro mapeo (o contador). Como `dict.update()` pero resta cuentas en su lugar de reemplazarlos.
* - [total](https://docs.python.org/3/library/collections.html#collections.Counter.total)()
  - Devuelve la suma de los recuentos.
* - [update](https://docs.python.org/3/library/collections.html#collections.Counter.update)([iterable-or-mapping])
  - Los elementos se cuentan desde un iterable o se agregan desde otro mapeo (o contador). Como `dict.update()` pero agrega cuentas en lugar de reemplazarlos.
```

<br/>

### Ejemplo de uso

A continuación se presenta un ejemplo en el que se crea un objeto `Counter` desde una lista y se imprime el elemento que más se repite

```{code-cell} python3
# importar la clase Counter 
from collections import Counter

# Definir una lista
words = ["apple", "banana", "apple", "orange", "banana", "orange", "banana"]

# Crear el objeto Counter a partir de la lista
word_count = Counter(words)

# Imprimir word_count
print(word_count, end="\n"*2)

# Imprimir solo el elemento con mas repeticiones
print(f"Elemento más común: {word_count.most_common(1)}")
```

<br/>

---
## Deque

Es un objeto similar a `list` pero optimizado para eliminar y agregar elementos. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [deque](https://docs.python.org/3/library/collections.html#collections.deque)([iterable[, maxlen]])
  - Devuelve un nuevo objeto `deque` inicializado de izquierda a derecha (usando `append()`) con datos de `iterable`. Si no se especifica iterable, el `deque` estará vacío.
```

<br/>

### Crear un `deque`

Para crear un objeto `deque` se debe pasar como argumento un objeto iterable al constructor `collections.deque(iterable, maxlen)`.

```python
# Importar el módulo
import collections

# Crear un deque desde el iterable Y
X = collections.deque(Y)
```
- Y \- `iterable`: Un objeto iterable. Si no se especifica, se inicializa un deque vacío.
- Se puede además especificar el parámetro `maxlen` que representa la longitud máxima que puede tener el `deque`, si no se especifica, entonces el `deque` puede crecer hasta una longitud arbitraria.

<br/>

---
### Atributos

Atributos de instancia de la clase `deque`.

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - [maxlen](https://docs.python.org/3/library/collections.html#collections.deque.maxlen)()
  - Retorna la longitud máxima que puede tener el `deque`. Si no tiene longitud máxima retorna `None`.
```

<br/>

### Métodos

Métodos de instancia de la clase `deque`.


#### Agregar elementos

Métodos para agregar elementos.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [append](https://docs.python.org/3/library/collections.html#collections.deque.append)(x)
  - Agrega un elemento `x` al final del `deque`.
* - [appendleft](https://docs.python.org/3/library/collections.html#collections.deque.appendleft)(x)
  - Agrega un elemento `x` al incio de un `deque`.
* - [extend](https://docs.python.org/3/library/collections.html#collections.deque.extend)(iterable)
  - Agrega elementos de un objeto iterable al final del `deque`.
* - [extendleft](https://docs.python.org/3/library/collections.html#collections.deque.extendleft)(iterable)
  - Agrega elementos de un objeto iterable al incio del `deque`.
* - [insert](https://docs.python.org/3/library/collections.html#collections.deque.insert)(i, x)
  - Inserta un elemento a un índice en específico, recorriendo el resto de los elementos a la derecha. Si el elemento provoca que se viole `maxlen` se arroja un `IndexError`.
```

<br/>

#### Eliminar elementos

Métodos para eliminar elementos.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [clear](https://docs.python.org/3/library/collections.html#collections.deque.clear)()
  - Elimina todos los elementos del `deque`.
* - [pop](https://docs.python.org/3/library/collections.html#collections.deque.pop)()
  - Remueve y retorna el último elemento. Si el `deque` no tiene elementos genera un `IndexError`. 
* - [popleft](https://docs.python.org/3/library/collections.html#collections.deque.popleft)()
  - Remueve y retorna el primer elemento del `deque`. Si no hay elementos presentes se genera un `IndexError`.
* - [remove](https://docs.python.org/3/library/collections.html#collections.deque.remove)(value)
  - Elimina la primer coincidencia de un elemento en la lista. Si no se encuentra el elemento se retorna un error `ValueError`.
```

<br/>

#### Información

Métodos que retornan información sobre el objeto `deque`. 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [count](https://docs.python.org/3/library/collections.html#collections.deque.count)(x)
  - Devuelve el número de veces que hay un elemento específico `x` en el `deque`.
* - [index](https://docs.python.org/3/library/collections.html#collections.deque.index)(x[, start[, stop]])
  - Devuelve el índice en el que se encuentra el elemento `x`. Retorna `ValueError` si el elemento no se encuentra.
```

<br/>

#### Modificar

Métodos para modificar el `deque`.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [reverse](https://docs.python.org/3/library/collections.html#collections.deque.reverse)()
  - Modifica el orden del `deque` de manera inversa in-place.
* - [rotate](https://docs.python.org/3/library/collections.html#collections.deque.rotate)(n=1)
  - Desplaza los elementos a la derecha o izquierda `n` posiciones.
```

<br/>

#### Copiar

Métodos para crear una copia del objeto.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [copy](https://docs.python.org/3/library/collections.html#collections.deque.copy)()
  - Retorna una copia superficial del `deque`.
```

<br/>

---
## Default dict

Es una subclase de `dict`, es como un diccionario que permite que si se trata de acceder a una _key_ que no existe, en lugar de arrojar un error, crea esa _key_ como un tipo de dato específico. El valor que tendrá esa _key_ dependerá del tipo de dato especificado.

Los métodos y la funcionalidad de `defaultdict` es la misma que la de `dict`, a excepción de lo anteriormente explicado.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [defaultdict](https://docs.python.org/3/library/collections.html#collections.defaultdict)(default_factory=None, /[, ...])
  - Crea un diccionario con valores por default de determinado tipo de dato, lo que permite que si se trata de acceder a un key que no existe, en lugar de arrojar un error, se crea ese elemento con el valor por default del tipo de dato.
```

<br/>

---
### Crear un `defaultdict`

Para crear un `defaultdict` se puede usar la función `collections.defaultdict()` cuyo argumento es un tipo de dato.

```python
# Importar el módulo
import collections

# Crear un defaultdict de "dtype"
collections.dafaultdict(dtype)
```
- **`dtype`** \- `dtype`: Es el nombre del tipo que tendrá el valor por default, por ejemplo `str`, `list`, `int`, etc. El valor que tendrá esa key será el mismo que el retornado por el constructor de `dtype`, por ejemplo, si `dtype=int` entonces el valor de la _key_ será `int()` que es el número 0. 

<br>

**Ejemplo**: En el siguiente ejemplo se usa la clase `defaultdict` para contar el número de veces que aparece cada letra en la palabra "mississippi". Básicamente la forma como funciona es que si se trata de acceder a una letra que todavía no está en el `defaultdict` entonces creará una llave nueva con el valor de 0 (porque es de tipo `int`) y le suma uno. Pero si ya existe la llave entonces simplemente le suma uno al valor de la llave.

```{code-cell} python3
# Importar la clase
from collections import defaultdict

# Definir una cadena
s = 'mississippi'

# Definir un defaultdict de tipo int
d = defaultdict(int)

# Crear keys con base a "s"
for k in s:
    d[k] += 1
    
# Imprimir d
print(d)
```

<br/>

---
## Named tuple

`namedtuple` es como un `tuple` pero sus elementos tienen nombre, lo que permite que se pueda acceder a los elementos por el nombre.


```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [namedtuple](https://docs.python.org/3/library/collections.html#collections.namedtuple)(typename, field_names, *, rename=False, defaults=None, module=None)
  - Devuelve una nueva subclase de `tuple` denominada `typename`. La nueva subclase se usa para crear objetos similares a `tuple` que tienen campos accesibles mediante nombres, además de ser indexables e iterables.
```

### Crear un `namedtuple`

Para crear un `namedtuple` se puede usar la función `collections.namedtuple()`. Esta función recibe como argumento una cadena que será el nombre del `tuple` y una cadena o lista de cadenas que serán los nombres de cada uno de los elementos.

```python
# Importar el módulo
import collections

# Crear un namedtuple
X = collections.namedtuple(typename, field_names)
```
- **`typename`** \- `str`: Es el nombre que tendrá el `tuple`.
- **`field_names`** \- `list` de `str` o `str`: Es el nombre que tendrá cada elemento
    - Si es una lista, cada nombre está separado por coma. 
    - Si es cadena, los nombres de separan por coma o espacios: `"name1, name2, ..."` o `"name1 name2 ..."`.


Posteriormente para llenar el `namedtuple` se usa:
```python
X(name1=val1, name2=val2, ...)
```
- _name1_, _name2_, ...: Son los nombre de los elementos que se pusieron en `field_names` en la función `collections.namedtuple()`. 
- _val1_, _val2_ \- `object`: Son los valores que tendrán esos campos. Se pueden poner los valores por nombre o por posición.


Para acceder a los elementos del `namedtuple` se puede usar:
```python
# Acceder al elemento i con su nombre con notación "."
X.name

# Acceder al elemento i con su nombre con notación "[]"
X["name"]

# Acceder al elemento i con su índice
X[i]
```
- _name_ es un nombre válido de `X`.