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

# Funciones built-in

En esta sección se presentan algunas funciones que forman parte de la librería estándar de Python y no es necesario importar ningún paquete o módulo. Las funciones están presentadas por categorías.

```{warning} Esta sección no incluye todas las funciones _built-in_ de Python, sino algunas de las más importantes. Para un listado completo de las funciones built-in de Python visitar la [documentación](https://docs.python.org/3/library/index.html) de Python.
```

---
## Cadenas

Funciones útiles para recuperar códigos Unicode o para recuperar representacios en cadenas de números.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [bin](https://docs.python.org/3/library/functions.html#bin)(x)
  - Convierte un número entero en una cadena binaria con el prefijo "0b".
* - [chr](https://docs.python.org/3/library/functions.html#chr)(i)
  - Devuelve la cadena que representa un carácter cuyo código Unicode es el entero _i_.
* - [hex](https://docs.python.org/3/library/functions.html#hex)(x)
  - Convierte un número entero en una cadena hexadecimal en minúsculas con el prefijo “0x”.
* - [format](https://docs.python.org/3/library/functions.html#format)(value, format_spec='')
  - Convierte _value_ en una representación "formateada", controlada por _format_spec_.
* - [oct](https://docs.python.org/3/library/functions.html#oct)(x)
  - Convierta un número entero en una cadena octal con el prefijo "0o".
* - [ord](https://docs.python.org/3/library/functions.html#ord)(c)
  - Dado un carácter Unicode, devuelve un número entero que representa el código Unicode de ese carácter

```

<br/>

## Archivos

Función para crear conexiones con achivos locales.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [open](https://docs.python.org/3/library/functions.html#open)(file, mode='r', buffering=- 1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
  - Abre un archivo y retorna un `file object` correspondiente. Si el archivo no se puede abrir, se genera un `OSError`. Ver {doc}`./io`.
```

<br/>

(func-iterables)=
## Iterables

Funciones útiles para objetos `iterable`.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [enumerate](https://docs.python.org/3/library/functions.html#enumerate)(iterable, start=0)
  - Crea un índice para cada elemento de un objeto iterable, por default comienza en cero.
* - [filter](https://docs.python.org/3/library/functions.html#filter)(function, iterable)
  - Retorna un `iterator` con los  elementos de _iterable_ para los cuales _function_ retorna `True`.
* - [iter](https://docs.python.org/3/library/functions.html#iter)(object)
  - Convierte un `iterable` en un `iterator`.
* - [len](https://docs.python.org/3/library/functions.html#len)(s)
  - Devuelve la longitud (el número de elementos) de un objeto. El argumento puede ser un secuencia (como una cadena, bytes, tupla, lista o rango) o una colección (como un diccionario, un `set` o `frozenset`).
* - [map](https://docs.python.org/3/library/functions.html#map)(function, iterable, *iterables)
  - Aplica una función a todos los elementos de un iterable. Retorna un `iterator`. En caso de que se pase más de un `iterable`, todos los `iterable` deben de ser del mismo tamaño.
* - [next](https://docs.python.org/3/library/functions.html#next)(iterator, default)
  - Recupera cada uno de los elementos de un `iterator`, uno a la vez. Si se proporcionó _default_, retorna ese valor cuando ya no haya elementos en el `iterator`, en caso contrario retornar `StopIteration`.
* - [reversed](https://docs.python.org/3/library/functions.html#reversed)(seq)
  - Retorna un `iterator` de _seq_ al inverso.
* - [sorted](https://docs.python.org/3/library/functions.html#sorted)(iterable, /, *, key=None, reverse=False)
  - Devuelve una nueva lista ordenada de los elementos en _iterable_.
* - [zip](https://docs.python.org/3/library/functions.html#zip)(*iterables, strict=False)
  - Combina dos (o más) objetos iterables, de manera que se crea un `tuple` con los elementos en posiciones correspondientes (`iterator` de `tuple`). El objeto con el tamaño menor determinará el tamaño del zip.
```

<br/>

### Uso de enumerate

A continuación se presentan algunas acciones comunes con objetos `enumerate` sobre el iterable _X_.

```python
# Crear un objeto enumerate
enumerate_obj = enumerate(X)

# Definir un for-loop con enumerate
for i, ele in enumerate(X):
    # for body

# Desempacar un enumerate. Retorna tuplas.
*enumerate(X)

# Convertir enumerate a una lista:
[*enumerate(X)] # equivalente a usar list(enumerate(X))

# Convertir enumerate a un tuple:
(*enumerate(X)) # equivalente a usar tuple(enumerate(X))
```
- `enumerate` crea tuplas de elementos en posiciones correspondientes entre el iterable y un rango numérico del mismo tamaño que `X`.
- _X_ es un `iterable`.

<br/>

---
### Uso de map

A continuación se presenta algunos ejemplos del uso de `map`.

```python
# Aplicar una función en cada elemento de un iterable X
map(fun, X)

# Aplicar una función en cada elemento de un iterable X con más de un argumento
map(fun, X, Y, ...)

# Desempacar un objeto map
*map(fun, X)
```
- _X, Y, ..._ son `iterable` del mismo tamaño cuyos elementos se usan como argumentos de la función _fun_, los elementos se empatan por posición.

---
### Uso de zip

A continuación se presentan algunas acciones comunes con objetos `zip` sobre los iterables _X_ y _Y_.

```python
# Crear un objeto zip
zip_obj = zip(X, Y)

# Recuperar los iterables originales
X, Y = zip(*zip_obj)

# Iterar en un objeto zip
for x, y in zip(X, Y):
    # for body

# Desempacar un objeto zip
*zip(X, Y)

# Convertir un objeto zip a una lista:
[*zip(X, Y)] # equivalente a usar list(zip(X, Y))

# Convertir un objeto zip a un tuple:
(*zip(X, Y)) # equivalente a usar tuple(zip(X, Y))
```
- `zip` crea tuplas de elementos en posiciones correspondientes.

<br/>

## Iterables booleanos

Funciones útiles para iterables con valores booleanos.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [all](https://docs.python.org/3/library/functions.html#all)(iterable)
  - Retorna `True` si todos los elementos de un objeto iterable son `True`.
* - [any](https://docs.python.org/3/library/functions.html#any)(iterable)
  - Retorna `True` si al menos un elemento de un objeto iterable es `True`.
```

<br/>

(func-iterables-numbericos)=
## Iterables numéricos

Funciones útiles para iterables numéricos.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [max](https://docs.python.org/3/library/functions.html#max)(iterable, *, key=None)
  - Devuélve el valor máximo de un iterable.
* - [min](https://docs.python.org/3/library/functions.html#min)(iterable, *, key=None)
  - Devuelve el valor mínimo en un iterable o el valor mínimo de dos o más argumentos.
* - [sum](https://docs.python.org/3/library/functions.html#sum)(iterable, /, start=0)
  - Suma los elementos de un objeto iterable.
```

<br/>

## Númericas

Funciones útiles para tipos numéricos. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [abs](https://docs.python.org/3/library/functions.html#abs)(x)
  - Devuelve el valor absoluto de un número.
* - [divmod](https://docs.python.org/3/library/functions.html#divmod)(a, b)
  - Devuélve un `tuple` con el cociente y residuo de la división de dos números.
* - [round](https://docs.python.org/3/library/functions.html#round)(number, ndigits=None)
  - Devuelve el número redondeado a la precisión indicada. Si se omite _ndigits_ o es `None`, devuelve el entero más cercano.
* - [pow](https://docs.python.org/3/library/functions.html#pow)(base, exp, mod=None)
  - Retorna _base_ a la potencia _exp_.
```

<br/>

(func-objetos-clases)=
## Objetos y Clases

Funciones útiles para instancias y clases. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [dir](https://docs.python.org/3/library/functions.html#dir)(object)
  - Sin argumentos, devuelve la lista de nombres en el ámbito local actual. Con argumentos, retorna una lista de atributos válidos para ese objeto.
* - [id](https://docs.python.org/3/library/functions.html#id)(object)
  - Retorna la identidad de un objeto, que es un identificador único durante una sesión. También sirve para identificar en dónde está almacenado en memoria el objeto.
* - [isinstance](https://docs.python.org/3/library/functions.html#isinstance)(object, classinfo)
  - Retorna `True` si el argumento _object_ es una instancia de _classinfo_.
* - [help](https://docs.python.org/3/library/functions.html#help)(request)
  - Invoca el sistema de ayuda integrado.
* - [super](https://docs.python.org/3/library/functions.html#super)(type, object_or_type=None)
  - Determina la siguiente clase en el _MRO_ de `type`. Útil para acceder a métodos heredados de otras clases que fueron sobreescritos.
```

<br/>

## Print/Input

Funciones para imprimir en consola o solicitar ingreso de información al usuario. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [input](https://docs.python.org/3/library/functions.html#input)(prompt)
  - La función lee una línea de la entrada, la convierte a una cadena y la retorna.
* - [print](https://docs.python.org/3/library/functions.html#print)(*objects, sep=' ', end='\n', file=None, flush=False)
  - Imprime en pantalla objetos, separados por _sep_.
```

