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

En esta sección se presentan algunas funciones que ya vienen incluídas y no es necesario importar ningún paquete o módulo. Las funciones están presentadas por categorías.

```{warning} Esta sección no incluye todas las funciones built-in de python, sino algunas de las más importantes. Para un listado completo de las funciones built-in de python visitar la [pagina oficial de Python](https://docs.python.org/3/library/index.html).
```

---
## Cadenas

Funciones útiles para recuperar códigos Unicode o para recuperar representacios de cadenas de números.

```{list-table} cadenas
:header-rows: 1

* - Funciones
  - Descripción
* - [chr](https://docs.python.org/3/library/functions.html#chr)(i)
  - Devuelve la cadena que representa un carácter cuyo código Unicode es el entero `i`.
* - [hex](https://docs.python.org/3/library/functions.html#hex)(x)
  - Convierta un número entero en una cadena hexadecimal en minúsculas con el prefijo “0x”.
* - [oct](https://docs.python.org/3/library/functions.html#oct)(x)
  - Convierta un número entero en una cadena octal con el prefijo "0o".
* - [ord](https://docs.python.org/3/library/functions.html#ord)(c)
  - Dado un carácter Unicode, devuelve un número entero que representa el código Unicode de ese carácter.
* - [format](https://docs.python.org/3/library/functions.html#format)(value, format_spec='')
  - Convierte `value` en una representación "formateada", controlada por `format_spec`.
* - [bin](https://docs.python.org/3/library/functions.html#bin)(x)
  - Convierta un número entero en una cadena binaria con el prefijo "0b".
```

---
## Archivos

Función para crear conexiones con achivos locales.

```{list-table} files
:header-rows: 1

* - Funciones
  - Descripción
* - [open](https://docs.python.org/3/library/functions.html#open)(file, mode='r', buffering=- 1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
  - Abre un archivo y retorna un `file object` correspondiente. Si el archivo no se puede abrir, se genera un `OSError`.
```

---
## Iterables

Funciones útiles para iterables.

```{list-table} iter
:header-rows: 1

* - Funciones
  - Descripción
* - [sorted](https://docs.python.org/3/library/functions.html#sorted)(iterable, /, *, key=None, reverse=False)
  - Devuelve una nueva lista ordenada de los elementos en `iterable`.
* - [enumerate](https://docs.python.org/3/library/functions.html#enumerate)(iterable, start=0)
  - Crea un índice para cada elemento de un objeto iterable, por default comienza en cero.
* - [filter](https://docs.python.org/3/library/functions.html#filter)(function, iterable)
  - Retorna un `iterator` con los  elementos de `iterable` para los cuales `function` retorna `True`.
* - [len](https://docs.python.org/3/library/functions.html#len)(s)
  - Devuelve la longitud (el número de elementos) de un objeto. El argumento puede ser un secuencia (como una cadena, bytes, tupla, lista o rango) o una colección (como un diccionario, un `set` o `frozenset`).
* - [map](https://docs.python.org/3/library/functions.html#map)(function, iterable, *iterables)
  - Aplica una función a todos los elementos de un iterable. Retorna un `iterator`.
* - [reversed](https://docs.python.org/3/library/functions.html#reversed)(seq)
  - Retorna un `iterator` de `seq` al inverso.
* - [zip](https://docs.python.org/3/library/functions.html#zip)(*iterables, strict=False)
  - Combina dos (o más) objetos iterables, de manera que se crea un `tuple` con los elementos en posiciones correspondientes. El objeto con el tamaño menor determinará el tamaño del zip.
* - [iter](https://docs.python.org/3/library/functions.html#iter)(object)
  - Convierte un `iterable` en un `iterator`.
* - [next](https://docs.python.org/3/library/functions.html#next)(iterator, default)
  - Recupera cada uno de los elementos de un `iterator`, uno a la vez. Si se proporcionó `default`, retorna ese valor cuando ya no haya elementos en el `iterator`, en caso contrario retornar `StopIteration`.
```

### Uso de enumerate

A continuación se presentan algunas acciones comunes con objetos `enumerate` sobre el iterable `X`.

```python
# Crear un objeto enumerate
enumerate_obj = zip(X, Y)

# Crear un for con enumerate
for i, ele in enumerate(X):
    body

# Desempacar un enumerate. Retorna tuplas.
*enumerate(X)

# Convertir enumerate a una lista:
[*enumerate(X)]

# Convertir enumerate a un tuple:
(*enumerate(X))
```
- `enumerate` crea tuplas de elementos en posiciones correspondientes entre el iterable y un rango numérico del mismo tamaño que `X`.
- `X` es un `iterable`.

### Uso de zip

A continuación se presentan algunas acciones comunes con objetos `enumerate` sobre los iterables `X` y `Y`.

```python
# Crear un objeto zip
zip_obj = zip(X, Y)

# Recuperar los iterables originales
X, Y = zip(*zip_obj)

# Iterar en un objeto zip
for x, y in zip(X, Y):
    body

# Desempacar un objeto zip
*zip(X, Y)

# Convertir un objeto zip a una lista:
[*zip(X, Y)]

# Convertir un objeto zip a un tuple:
(*zip(X, Y))
```
- `zip` crea tuplas de elementos en posiciones correspondientes.

---
## Iterables booleanos

Funciones útiles para iterables con valores booleanos.

```{list-table} iter-bool
:header-rows: 1

* - Funciones
  - Descripción
* - [all](https://docs.python.org/3/library/functions.html#all)(iterable)
  - Retorna `True` si todos los elementos de un objeto iterable son `True`.
* - [any](https://docs.python.org/3/library/functions.html#any)(iterable)
  - Retorna `True` si al menos un elemento de un objeto iterable es `True`.
```

---
## Iterables numéricos

Funciones útiles para iterables numéricos.

```{list-table} iter-num
:header-rows: 1

* - Funciones
  - Descripción
* - [min](https://docs.python.org/3/library/functions.html#min)(iterable, *, key=None)
  - Devuelve el valor mínimo en un iterable o el valor mínimo de dos o más argumentos.
* - [sum](https://docs.python.org/3/library/functions.html#sum)(iterable, /, start=0)
  - Suma los elementos de un objeto iterable.
* - [max](https://docs.python.org/3/library/functions.html#max)(iterable, *, key=None)
  - Devuélve el valor máximo de un iterable.
```

---
## Númericas

Funciones útiles para tipos numéricos. 

```{list-table} numeros
:header-rows: 1

* - Funciones
  - Descripción
* - [pow](https://docs.python.org/3/library/functions.html#pow)(base, exp, mod=None)
  - Regrese `base` a la potencia `exp`.
* - [round](https://docs.python.org/3/library/functions.html#round)(number, ndigits=None)
  - Devuelve el número redondeado a la precisión indicada. Si se omite `ndigits` o es `None`, devuelve el entero más cercano.
* - [divmod](https://docs.python.org/3/library/functions.html#divmod)(a, b)
  - Devuélve un `tuple` con el cociente y residuo de la división de dos números.
* - [abs](https://docs.python.org/3/library/functions.html#abs)(x)
  - Devuelve el valor absoluto de un número.
```

---
## Instancias y Clases

Funciones útiles para instancias y clases. 

```{list-table} obj-clases
:header-rows: 1

* - Funciones
  - Descripción
* - [isinstance](https://docs.python.org/3/library/functions.html#isinstance)(object, classinfo)
  - Retorna `True` si el argumento `object` es una instancia de `classinfo`.
* - [dir](https://docs.python.org/3/library/functions.html#dir)(object)
  - Sin argumentos, devuelve la lista de nombres en el ámbito local actual. Con un argumento, retorna una lista de atributos válidos para ese objeto.
* - [id](https://docs.python.org/3/library/functions.html#id)(object)
  - Retorna la identidad de un objeto, que es un identificador único durante una sesión. También sirve para identificar en dónde está almacenado en memoria el objeto.
* - [help](https://docs.python.org/3/library/functions.html#help)(request)
  - Invoca el sistema de ayuda integrado.
```

---
## Print/Input

Funciones para imprimir en consola o solicitrar ingreso de información al usuario. 

```{list-table} print/input
:header-rows: 1

* - Funciones
  - Descripción
* - [input](https://docs.python.org/3/library/functions.html#input)(prompt)
  - La función lee una línea de la entrada, la convierte a una cadena y la retorna.
* - [print](https://docs.python.org/3/library/functions.html#print)(*objects, sep=' ', end='\n', file=None, flush=False)
  - Imprime en pantalla objetos, separados por `sep` y seguidos por `end`.
```

