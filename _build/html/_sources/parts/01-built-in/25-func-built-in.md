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

```{warning} Esta sección no incluye todas las funciones built-in de python, sino algunas de las más importantes. Para un listado completo de las funciones built-in de python 3.9 visitar la [pagina oficial de Python](https://docs.python.org/3.9/library/functions.html).
```

---
## Conversiones numéricas

Funciones para convertir objetos a números o valores bool.

```{list-table} Conversiones numéricas
:header-rows: 1

* - Funciones
  - Descripción
  - Sintaxis
* - [bool](#bool)
  - Convierte una variable a un valor lógico. Retorna `True` con casi todos los objetos excepto con: `None`, `False`, `0`, `""`, `()`, `[]`, `{}`.
  - bool(X)
* - [complex](#complex)
  - Convierte una variable a número complejo:
  - complex(N1, [N2 = 0])
* - [float](#float)
  - Convierte un número o una cadena a un número flotante.
  - float(N)
* - [int](#int)
  - Convierte un número o una cadena a un número entero.
  - int(N, [base = 10])
```

---
## Conversiones de cadenas

Funciones para convertir valores numéricos a cadenas o caracteres a códigos unicode y viceversa.

```{list-table} Conversiones de cadenas
:header-rows: 1

* - Funciones
  - Descripción
  - Sintaxis
* - [chr](#chr)
  - Retorna el caracter correspondiente a un código de Unicode.
  - chr(N)
* - [ord](#ord)
  - Retorna el código Unicode correspondiente a un caracter.
  - ord(char)
* - [str](#str)
  - Convierte un objeto a una cadena.
  - str(X)
* - [bin](#bin)
  - Convierte un entero a una cadena binaria.
  - bin(integer)
* - [hex](#hex)
  - Convierte un entero a una cadena hexadecimal.
  - hex(integer)
* - [oct](#oct)
  - Convierte un entero a una cadena octal.
  - oct(integer)
```

---
## Conversiones a secuencias

Funciones para convertir objetos a secuencias.

```{list-table} Conversiones a secuencias
:header-rows: 1

* - Funciones
  - Descripción
  - Sintaxis
* - [list](#list)
  - Convierte un objeto a una lista.
  - list(X)
* - [set](#set)
  - Crea o convierte un objeto a un `set`
  - set(X)
* - [tuple](#tuple)
  - Convierte un objeto a un `tuple`
  - tuple(X)
```

---
## Conversiones a mappings

Función para crear diccionarios o convertir iterables a un diccionario.

```{list-table} Conversiones a mappings
:header-rows: 1

* - Funciones
  - Descripción
  - Sintaxis
* - [dict](#dict)
  - Crea o convierte un objeto a diccionario.
  - dict(X)
```

---
## Funciones para números

Funciones para objetos de tipos numéricos.

```{list-table} Funciones para números
:header-rows: 1

* - Funciones
  - Descripción
  - Sintaxis
* - [abs](#abs)
  - Devuelve el valor absoluto de un número en específico.
  - abs(N)
* - [divmod](#divmod)
  - Devuélve un `tuple` con el cociente y residuo de la división de dos números.
  - divmod(N1, N2)
* - [pow](#pow)
  - Devuelve un número elevado a otro número.
  - pow(N1, N2)
* - [round](#round)
  - Redondea un número.
  - round(N1, [N2 = 0])
```

---
## Iterables booleanos

Funciones útiles para iterables de tipo `bool`.

```{list-table} Iterables booleanos
:header-rows: 1

* - Funciones
  - Descripción
  - Sintaxis
* - [all](#all)
  - Retorna `True` si todos los elementos de un objeto iterable son `True`
  - all(X)
* - [any](#any)
  - Retorna `True` si al menos un elemento de un objeto iterable es `True`
  - any(X)
```

---
## Iterables numéricos

Funciones útiles para iterables de tipo numérico.

```{list-table} Iterables numéricos
:header-rows: 1

* - Funciones
  - Descripción
  - Sintaxis
* - [max](#max)
  - Devuélve el valor máximo de un iterable.
  - max(X, [key = None])
* - [min](#min)
  - Devuélve el valor mínimo de un iterable.
  - min(X, [key = None])
* - [sum](#sum)
  - Suma los elementos de un objeto iterable.
  - sum(X, [start = 0])
```

---
## Iterables

Funciones para crear o interactual con iterables.

```{list-table} Iterables
:header-rows: 1

* - Funciones
  - Descripción
  - Sintaxis
* - [enumerate](#enumerate)
  - Crea un índice para cada elemento de un objeto iterable, por default comienza en cero.
  - enumerate(X, [start = 0])
* - [filter](#filter)
  - Filtra secuencias, removiendo elementos que no satisfacen determinados criterios.
  - filter(función, X)
* - [len](#len)
  - Devuelve el número de elementos que tiene un iterable.
  - len(X)
* - [map](#map)
  - Aplica una función a todos los elementos de un iterable.
  - map(funcion, X)
* - [range](#range)
  - Genera una secuencia de números enteros. Se pueden crear secuencias decrecientes, con el `step` negativo y con `start ` end`.
  - range(start=0, end, step = 1)
* - [reversed](#reversed)
  - Retorna un iterable al reverso.
  - reversed(X)
* - [slice](#slice)
  - Sirve para hacer slice en un iterable.
  - Y = slice(start, end, [step = 1])
* - [sorted](#sorted)
  - Ordena los elementos de un iterable, los datos pueden ser numéricos o cadenas, pero solo de un tipo.
  - sorted(X, [key = None], [reverse = False])
* - [zip](#zip)
  - Combina dos (o más) objetos iterables, de manera que la posición de cada objeto se une con el otro creando un. El objeto con el tamaño menor determinará el tamaño del zip.
  - zip(X, Y, ...)
```

---
## Objetos y Clases

Funciones útiles para objetos, instancias y clases.

```{list-table} Objetos y Clases
:header-rows: 1

* - Funciones
  - Descripción
  - Sintaxis
* - [dir](#dir)
  - Retorna los atributos y método de un objeto. Si no se pone argumento entonces retorna los objetos en el _scope_ local.
  - id(object)
* - [id](#id)
  - Retorna la identidad de un objeto, que es un identificador único durante una sesión. También sirve para identificar en dónde está almacenado en memoria el objeto.
  - id(object)
* - [isinstance](#isinstance)
  - Verifica que un objeto sea de una clase, incluyendo sus clases padres.
  - isinstance(X, type)
* - [issubclass](#issubclass)
  - Retorna `True` si class es una clase hija de `subclass`. Una clase se considera subclase de sí misma.
  - issubclass(class, classinfo)
* - [super](#super)
  - super( ) `object` Retorna la clase padre de una clase hija, se utiliza para sobreescribir métodos.
  - super()
* - [type](#type)
  - type( ) `type` Devuelve el tipo de variable que es un objeto.
  - type(X)
```


## Listado de funciones.

---
***Conversiones numéricas**

Funciones para convertir objetos a números o valores bool.

---
<a name='bool'></a>
**bool**:

`bool()`: Convierte una variable a un valor lógico. Retorna `True` con casi todos los objetos excepto con: `None`, `False`, `0`, `""`, `()`, `[]`, `{}`.
```python
bool(X)
```

**Parámetros:**
- **`X`** \- `object`: Objeto a convertir.

**Retorna:**
-  `bool`.

<br><br>

---
<a name='complex'></a>
**complex**:

`complex()`: Convierte una variable a número complejo:
```python
complex(N1, [N2 = 0])
```

**Parámetros:**
- **`N1`** \- `float`, `int`: Es un número que será la parte real y `N2` `float` es un número que será la parte imaginaria. También puede convertir una cadena a un número imaginario, para ello poner la cadena de la siguiente manera `N1+N2j`.

**Retorna:**
-  `complex`.

<br><br>

---
<a name='float'></a>
**float**:

`float()`: Convierte un número o una cadena a un número flotante.
```python
float(N)
```

**Parámetros:**
- **`N`** \- `int`, `str`: Podría ser una cadena con el valor.

**Retorna:**
-  `float`.

<br><br>

---
<a name='int'></a>
**int**:

`int()`: Convierte un número o una cadena a un número entero.
```python
int(N, [base = 10])
```

**Parámetros:**
- **`N`** \- `float`, `str`, `long`: Si es un número decimal, lo truncará, pero también podría ser una cadena con el valor.

**Retorna:**
-  `int`.

<br><br>

---
**Conversiones de cadenas**

Funciones para convertir valores numéricos a cadenas o caracteres a códigos unicode y viceversa.

---
<a name='chr'></a>
**chr**:

`chr()`: Retorna el caracter correspondiente a un código de Unicode.
```python
chr(N)
```

**Parámetros:**
- **`N`** \- `int`: Número entero que representa el código de Unicode.

**Retorna:**
-  `str`.

<br><br>

---
<a name='ord'></a>
**ord**:

`ord()`: Retorna el código Unicode correspondiente a un caracter.
```python
ord(char)
```

**Parámetros:**
- **`char`** \- `str`: caracter.

**Retorna:**
-  `int`.

<br><br>

---
<a name='str'></a>
**str**:

`str()`: Convierte un objeto a una cadena.
```python
str(X)
```

**Parámetros:**
- **`X`** \- `object`: Lo más común es que sea un número.

**Retorna:**
-  `str`.

<br><br>

---
<a name='bin'></a>
**bin**:

`bin()`: Convierte un entero a una cadena binaria.
```python
bin(integer)
```

**Parámetros:**
- **`integer`** \- `str`: Número entero.

**Retorna:**
-  `str`.

<br><br>

---
<a name='hex'></a>
**hex**:

`hex()`: Convierte un entero a una cadena hexadecimal.
```python
hex(integer)
```

**Parámetros:**
- **`integer`** \- `str`: Número entero.

**Retorna:**
-  `str`.

<br><br>

---
<a name='oct'></a>
**oct**:

`oct()`: Convierte un entero a una cadena octal.
```python
oct(integer)
```

**Parámetros:**
- **`integer`** \- `str`: Número entero.

**Retorna:**
-  `str`.

<br><br>

---
**Conversiones a secuencias**

Funciones para convertir objetos a secuencias.

---
<a name='list'></a>
**list**:

`list()`: Convierte un objeto a una lista.
```python
list(X)
```

**Parámetros:**
- **`X`** \- `iterable`. Objeto: • X `iterable`. Objeto.

**Retorna:**
-  `list`.

<br><br>

---
<a name='set'></a>
**set**:

`set()`: Crea o convierte un objeto a un `set`
```python
set(X)
```

**Parámetros:**
- **`X`** \- `iterable`: Objeto.

**Retorna:**
-  `set`.

<br><br>

---
<a name='tuple'></a>
**tuple**:

`tuple()`: Convierte un objeto a un `tuple`
```python
tuple(X)
```

**Parámetros:**
- **`X`** \- `iterable`: Objeto.

**Retorna:**
-  `tuple`.

<br><br>

---
**Conversiones a mappings**

Función para crear diccionarios o convertir iterables a un diccionario.

---
<a name='dict'></a>
**dict**:

`dict()`: Crea o convierte un objeto a diccionario.
```python
dict(X)
```

**Parámetros:**
- **`X`** \- `iterable`: Sus elementos deben de ser pares, donde el primer elemento será el key y el segundo el valor, por ejemplo, una lista donde cada elemento es otra lista con 2 elementos o una lista de tuples de 2 elementos cada uno, etc.

**Retorna:**
-  `dict`.

```{note}
Tambien se pueden pasar los argumentos de la siguiente forma `dict(key1 = val1, key2 = val2, ...)`. Las _key_ no necesitas ir entre comillas, pero los _value_ sí en caso de que se trate de objetos `str`.
```

<br><br>

---
**Funciones para números**

Funciones para objetos de tipos numéricos.

---
<a name='abs'></a>
**abs**:

`abs()`: Devuelve el valor absoluto de un número en específico.
```python
abs(N)
```

**Parámetros:**
- **`N`** \- `int`, `float`: Número.

**Retorna:**
-  `int`, `float`.

<br><br>

---
<a name='divmod'></a>
**divmod**:

`divmod()`: Devuélve un `tuple` con el cociente y residuo de la división de dos números.
```python
divmod(N1, N2)
```

**Parámetros:**
- **`N1,`** \- N2 `int`, `float`: Representa el dividendo, es decir, el numerador.
- **`N2`** \- `int`, `float`: Representa el dividendo, es decir, el denominador

**Retorna:**
-  `tuple`.

<br><br>

---
<a name='pow'></a>
**pow**:

`pow()`: Devuelve un número elevado a otro número.
```python
pow(N1, N2)
```

**Parámetros:**
- **`N1`** \- `int`, `float`: Base
- **`N1`** \- `int`, `float`: Exponente

**Retorna:**
-  `int`, `float`.

<br><br>

---
<a name='round'></a>
**round**:

`round()`: Redondea un número.
```python
round(N1, [N2 = 0])
```

**Parámetros:**
- **`N1`** \- `int`, `float`: Es el número que se va a redondear
- **`N2`** \- `int`: Es el número de decimales que se desea tener.

**Retorna:**
-  `float`.

<br><br>

---
**Iterables booleanos**

Funciones útiles para iterables de tipo `bool`.

---
<a name='all'></a>
**all**:

`all()`: Retorna `True` si todos los elementos de un objeto iterable son `True`
```python
all(X)
```

**Parámetros:**
- **`X`** \- `iterable`: Objeto.

**Retorna:**
-  `bool`.

<br><br>

---
<a name='any'></a>
**any**:

`any()`: Retorna `True` si al menos un elemento de un objeto iterable es `True`
```python
any(X)
```

**Parámetros:**
- **`X`** \- `iterable`: Objeto.

**Retorna:**
-  `bool`.

<br><br>

---
**Iterables numéricos**

Funciones útiles para iterables de tipo numérico.

---
<a name='max'></a>
**max**:

`max()`: Devuélve el valor máximo de un iterable.
```python
max(X, [key = None])
```

**Parámetros:**
- **`X`** \- `iterable`: Iterable numérico.
- **`key`**  \- `function`: Es el nombre de una función para ordenar los elementos de `X`.

**Retorna:**
-  `int`, `float`, `str`.

<br><br>

---
<a name='min'></a>
**min**:

`min()`: Devuélve el valor mínimo de un iterable.
```python
min(X, [key = None])
```

**Parámetros:**
- **`X`** \- `iterable`: Iterable numérico.
- **`key`**  \- `function`: Es el nombre de una función para ordenar los elementos de `X`.

**Retorna:**
-  `int`, `float`, `str`.

<br><br>

---
<a name='sum'></a>
**sum**:

`sum()`: Suma los elementos de un objeto iterable.
```python
sum(X, [start = 0])
```

**Parámetros:**
- **`X`** \- `iterable`: Iterable numérico.
- **`start`** \- `int`, `float`: Es para indicar que la suma empiece en un valor.

**Retorna:**
-  `int`, `float`.

<br><br>

---
**Iterables**

Funciones para crear o interactual con iterables.

---
<a name='enumerate'></a>
**enumerate**:

`enumerate()`: Crea un índice para cada elemento de un objeto iterable, por default comienza en cero.
```python
enumerate(X, [start = 0])
```

**Parámetros:**
- **`X`** \- `iterable`, `iterator`: Objeto.
- **`start`** \- `int`: Es para indicar desde que índice empezar.

**Retorna:**
-  `enumerate`.

```{note}
Si X es `enumerate` 
- Para convertir a `list` usar `list(X)` o `[*X]`.
- Para convertir a `tuple` usar `tuple(X)` o `(*X)`.
```

<br><br>

---
<a name='filter'></a>
**filter**:

`filter()`: Filtra secuencias, removiendo elementos que no satisfacen determinados criterios.
```python
filter(función, X)
```

**Parámetros:**
- **`función`** \- `function`: Función que debe de devolver valores `True `o `False`.
- **`X`** \- `iterable`: Objeto

**Retorna:**
-  `iterable`.

<br><br>

---
<a name='len'></a>
**len**:

`len()`: Devuelve el número de elementos que tiene un iterable.
```python
len(X)
```

**Parámetros:**
- **`X`** \- `iterable`: Objeto.

**Retorna:**
-  `int`.

<br><br>

---
<a name='map'></a>
**map**:

`map()`: Aplica una función a todos los elementos de un iterable.
```python
map(funcion, X)
```

**Parámetros:**
- **`función`** \- `function`: Nombre de la función. Si es una función lambda, debe de estar definida de tal forma que toma como argumento un elemento del iterable, o sea, un `scalar`.
- **`X`** \- `iterable`: Objeto

**Retorna:**
-  `list`.

<br><br>

---
<a name='range'></a>
**range**:

`range()`: Genera una secuencia de números enteros. Se pueden crear secuencias decrecientes, con el `step` negativo y con `start>end`.
```python
range(start=0, end, step = 1)
```

**Parámetros:**
- **`start`** \- `int`: Indica desde que número comenzar la secuencia
- **`end`** \- `int`: Indica hasta que número hacer la secuencia, sin incluir este número.
- **`step`** \- `int`: Indica el paso en la secuencia.

**Retorna:**
-  `range`.

<br><br>

---
<a name='reversed'></a>
**reversed**:

`reversed()`: Retorna un iterable al reverso.
```python
reversed(X)
```

**Parámetros:**
- **`X`** \- `iterable`: Objeto

**Retorna:**
-  `iterable`.

<br><br>

---
<a name='slice'></a>
**slice**:

`slice()`: Sirve para hacer slice en un iterable. Equivale a usar `X[start:end:step]`.
```python
Y = slice(start, end, [step = 1])
```

**Parámetros:**
- **`start`** \- `int`: Indica desde que índice comenzar el slice.
- **`end`** \- `int`: Indica hasta que índice hacer el slice, sin incluir este número.
    - \-1 equivale hasta el final sin incluir el último elemento.
    - `None` equivale hasta el final, incluyendo el último elemento.
- **`step`** \- `int`: Indica el paso del slice.

```{note}
Los parámetros `start`, `end` y `step` pueden ser valores positivos o negativos.
```

**Retorna:**
-  `slice`.

**Ejemplo:**

```{code-cell} python3
# Crear un objeto iterable
x = list("aeiou")

# Slice para seleccionar indices pares (elementos impares)
int_pares = slice(0, None, 2)

# Hacer el slice
print(x[int_pares])
```

<br><br>

---
<a name='sorted'></a>
**sorted**:

`sorted()`: Ordena los elementos de un iterable, los datos pueden ser numéricos o cadenas, pero solo de un tipo.
```python
sorted(X, [key = None], [reverse = False])
```

**Parámetros:**
- **`X`** \- `iterable`: • X `iterable`.
- **`key`** \- `function`: Nombre de un función para ordenarlos con base a los resultados de aplicar esa función a cada elemento.
- **`reverse`** \- `bool`: Es para indicar que se ordene de manera descendente.

**Retorna:**
-  `iterable`.

<br><br>

---
<a name='zip'></a>
**zip**:

`zip()`: Combina dos (o más) objetos iterables, de manera que la posición de cada objeto se une con el otro creando un. El objeto con el tamaño menor determinará el tamaño del zip.
```python
zip(X, Y, ...)
```

**Parámetros:**
- **`X`** \- `iterable`. Objetos. Pueden ser más de dos: • X `iterable`. Objetos. Pueden ser más de dos.

**Retorna:**
-  `zip`.

```{note}
Para hacer _unzip_ (retornar los objetos originales) usar: `X, Y, ... = zip(*objetoZip)`

```

<br><br>

---
**Objetos y Clases**

Funciones útiles para objetos, instancias y clases.

---
<a name='dir'></a>
**dir**:

`dir()`: Retorna los atributos y método de un objeto. Si no se pone argumento entonces retorna los objetos en el _scope_ local. Más información sobre esta función se puede encontrar en {doc}`01-ayuda.md`.

```python
id(object)
```

**Parámetros:**
- **`object`** \- `object`: Objeto.

**Retorna:**
-  `list`.

<br><br>

---
<a name='id'></a>
**id**:

`id()`: Retorna la identidad de un objeto, que es un identificador único durante una sesión. También sirve para identificar en dónde está almacenado en memoria el objeto.
```python
id(object)
```

**Parámetros:**
- **`object`** \- `object`: Objeto.

**Retorna:**
-  `int`.

<br><br>

---
<a name='isinstance'></a>
**isinstance**:

`isinstance()`: Verifica que un objeto sea de una clase, incluyendo sus clases padres.
```python
isinstance(X, type)
```

**Parámetros:**
- **`X`** \- `object`: • X `object`.
- **`type`** \- `class`, `type`, `tuple de class o type`: Nombre de la clase, incluyendo tipos de datos.

**Retorna:**
-  `bool`.

<br><br>

---
<a name='issubclass'></a>
**issubclass**:

`issubclass()`: Retorna `True` si class es una clase hija de `subclass`. Una clase se considera subclase de sí misma.
```python
issubclass(class, classinfo)
```

**Parámetros:**
- **`class`** \- `Class`: Nombre de la clase hija.
- **`classinfo`** \- `Class`. Nombre de la clase padre: • classinfo `Class`. Nombre de la clase padre.

**Retorna:**
-  `bool`.

<br><br>

---
<a name='super'></a>
**super**:

`super()`: Retorna la clase padre de una clase hija, se utiliza para sobreescribir métodos. Se usa dentro de las definiciones de las clases hijas.
```python
super()
```

**Parámetros:**
- **`X`** \- `object`: Objeto.

**Retorna:**
-  `object`.

```{note}
La forma de usarlo es `super().method_name(args)` donde _method_name_ es un método de la clase padre inmeditamente superior.
```

**Ejemplo:**

En el siguiente ejemplo la clase hija sobreesribe el método `__init__()` para convertir una cadena en una lista.
```{code-cell} python3
# Clase padre
class Cadena:
    def __init__(self, txt):
        self.message = txt

    def imprimir(self):
        print(self.message)

# Clase hija
class Lista(Cadena):
    def __init__(self, txt):
        txt = txt.split()
        # Lo siquiente equivale a: Cadena.__init__(self, txt)
        super().__init__(txt)

# Crear objetos
x = Cadena("Hello, and welcome!")
y = Lista("Hello, and welcome!")

# Imprimir objetos
print(x.imprimir())
print(y.imprimir())
```

<br><br>

---
<a name='type'></a>
**type**:

`type()`: Devuelve el tipo de variable que es un objeto.
```python
type(X)
```

**Parámetros:**
- **`X`** \- `object`: Objeto.

**Retorna:**
-  `type`.