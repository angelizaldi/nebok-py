# Modulo char

`numpy.char` es un módulo que provee de funciones relacionadas con arrays de cadenas. Es posible importar solo el módulo o una función específica.

```python
# Importar el módulo
from numpy import char

# Importar una función específica
from numpy.char import function_name
```
- _function_name_ es el nombre de la función que se desea importar.
- Si se importa todo el módulo es necesario usar `char.function_name()` cada vez que se llame a una función el módulo.
- Si se usa `import numpy as np` y se desea usar una función del módulo `char`, entonces se debe usar `np.char.function_name()`.

:::{warning}
Para una lista completa visitar la [documentación](https://numpy.org/doc/stable/reference/routines.char.html#module-numpy.char) de `numpy`.
:::


---
## Buscar

Funciones para buscar subcadenas. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [char.find](https://numpy.org/doc/stable/reference/generated/numpy.char.find.html)(a, sub[, start, end])
  - Para cada elemento, devuelve el índice más bajo de la cadena donde se encuentra la subcadena `sub`.
* - [char.index](https://numpy.org/doc/stable/reference/generated/numpy.char.index.html)(a, sub[, start, end])
  - Como `find`, pero genera `ValueError` cuando no se encuentra la subcadena.
* - [char.rfind](https://numpy.org/doc/stable/reference/generated/numpy.char.rfind.html)(a, sub[, start, end])
  - Para cada elemento en `a`, devuelva el índice más alto en la cadena donde se encuentra la subcadena `sub`, de modo que `sub` esté contenido dentro de `[start, end]`.
* - [char.rindex](https://numpy.org/doc/stable/reference/generated/numpy.char.rindex.html)(a, sub[, start, end])
  - Como `rfind`, pero genera `ValueError` cuando no se encuentra la subcadena `sub`.
```

<br>

---
## Comparaciones

Funciones para realizar comparaciones entre arreglos. Estas funciones eliminan los espacios en blanco al inicio y al final de los elementos antes de realizar la comparación. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [char.equal](https://numpy.org/doc/stable/reference/generated/numpy.char.equal.html)(x1, x2)
  - Devuelve `(x1 == x2)` por elementos.
* - [char.greater](https://numpy.org/doc/stable/reference/generated/numpy.char.greater.html)(x1, x2)
  - Devuelve `(x1 > x2)` por elementos.
* - [char.greater_equal](https://numpy.org/doc/stable/reference/generated/numpy.char.greater_equal.html)(x1, x2)
  - Retorna `(x1 >= x2)` por elementos.
* - [char.less](https://numpy.org/doc/stable/reference/generated/numpy.char.less.html)(x1, x2)
  - Devuelve `(x1 < x2)` por elementos.
* - [char.less_equal](https://numpy.org/doc/stable/reference/generated/numpy.char.less_equal.html)(x1, x2)
  - Retorna `(x1 <= x2)` por elementos.
* - [char.not_equal](https://numpy.org/doc/stable/reference/generated/numpy.char.not_equal.html)(x1, x2)
  - Devuelve `(x1 != x2)` por elementos.
```

<br>

---
## Formato

Funciones que modifican el formato de los elementos. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [char.capitalize](https://numpy.org/doc/stable/reference/generated/numpy.char.capitalize.html)(a)
  - Devuelve una copia de `a` con solo el primer carácter de cada elemento en mayúscula.
* - [char.center](https://numpy.org/doc/stable/reference/generated/numpy.char.center.html)(a, width[, fillchar])
  - Devuelve una copia de `a` con sus elementos centrados en una cadena de largo `width`.
* - [char.ljust](https://numpy.org/doc/stable/reference/generated/numpy.char.ljust.html)(a, width[, fillchar])
  - Devuelve un arreglo con los elementos de `a` justificados a la izquierda en una cadena de longitud `width`.
* - [char.lower](https://numpy.org/doc/stable/reference/generated/numpy.char.lower.html)(a)
  - Devuelve un arreglo con los elementos convertidos a minúsculas.
* - [char.rjust](https://numpy.org/doc/stable/reference/generated/numpy.char.rjust.html)(a, width[, fillchar])
  - Devuelve un arreglo con los elementos de `a` justificados a la derecha en una cadena de longitud `width`.
* - [char.swapcase](https://numpy.org/doc/stable/reference/generated/numpy.char.swapcase.html)(a)
  - Devuelve por elementos una copia de la cadena con los caracteres en mayúsculas convertidos a minúsculas y viceversa.
* - [char.title](https://numpy.org/doc/stable/reference/generated/numpy.char.title.html)(a)
  - Devuelve por elementos una copia de la cadena con los caracteres convertidos a titulos, donde la primer letra de cada palabra se pone en mayúsculas y el resto en minúsculas.
* - [char.upper](https://numpy.org/doc/stable/reference/generated/numpy.char.upper.html)(a)
  - Devuelve un arreglo con los elementos convertidos a mayúsculas.
* - [char.zfill](https://numpy.org/doc/stable/reference/generated/numpy.char.zfill.html)(a, width)
  - Devuelve la cadena numérica rellena con ceros a la izquierda.
```

<br>

---
## Información

Funciones que retornan información sobre los elementos de los arrays. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [char.count](https://numpy.org/doc/stable/reference/generated/numpy.char.count.html)(a, sub[, start, end])
  - Devuelve un arreglo con el número de ocurrencias no superpuestas de la subcadena `sub` en el rango `[start, end]`.
* - [char.endswith](https://numpy.org/doc/stable/reference/generated/numpy.char.endswith.html)(a, suffix[, start, end])
  - Devuelve un arreglo booleano que es `True` donde el elemento de cada cadena en `a` termina con `suffix`, de lo contrario, es `False`.
* - [char.isalnum](https://numpy.org/doc/stable/reference/generated/numpy.char.isalnum.html)(a)
  - Devuelve `True` para cada elemento si todos los caracteres de la cadena son alfanuméricos y hay al menos un carácter; de lo contrario, devuelve `False`.
* - [char.isalpha](https://numpy.org/doc/stable/reference/generated/numpy.char.isalpha.html)(a)
  - Devuelve `True` para cada elemento si todos los caracteres de la cadena son alfabéticos y hay al menos un carácter; de lo contrario, devuelve `False`.
* - [char.isdecimal](https://numpy.org/doc/stable/reference/generated/numpy.char.isdecimal.html)(a)
  - Para cada elemento, devuelva `True` si solo hay caracteres decimales en el elemento.
* - [char.isdigit](https://numpy.org/doc/stable/reference/generated/numpy.char.isdigit.html)(a)
  - Devuelve `True` para cada elemento si todos los caracteres de la cadena son dígitos y hay al menos un carácter; de lo contrario, devuelve `False`.
* - [char.islower](https://numpy.org/doc/stable/reference/generated/numpy.char.islower.html)(a)
  - Devuelve `True` para cada elemento si todos los caracteres de la cadena están en minúsculas y hay al menos un carácter; de lo contrario, devuelve `False`.
* - [char.isnumeric](https://numpy.org/doc/stable/reference/generated/numpy.char.isnumeric.html)(a)
  - Para cada elemento, devuelva `True` si solo hay caracteres numéricos en el elemento.
* - [char.isspace](https://numpy.org/doc/stable/reference/generated/numpy.char.isspace.html)(a)
  - Devuelve `True` para cada elemento si solo hay caracteres de espacio en blanco en la cadena y hay al menos un carácter; de lo contrario, devuelve `False`.
* - [char.istitle](https://numpy.org/doc/stable/reference/generated/numpy.char.istitle.html)(a)
  - Devuelve `True` para cada elemento si el elemento es una cadena tipo título y hay al menos un carácter; de lo contrario, devuelve `False`.
* - [char.isupper](https://numpy.org/doc/stable/reference/generated/numpy.char.isupper.html)(a)
  - Devuelve `True` para cada elemento si todos los caracteres en la cadena están en mayúsculas y hay al menos un carácter; de lo contrario, devuelve `False`.
* - [char.startswith](https://numpy.org/doc/stable/reference/generated/numpy.char.startswith.html)(a, prefix[, start, end])
  - Devuelve un arreglo booleano que es `True` donde el elemento de cadena en `a` comienza con `prefix`; de lo contrario, es `False`.
* - [char.str_len](https://numpy.org/doc/stable/reference/generated/numpy.char.str_len.html)(a)
  - Devuelve `len(a)` por elementos.
```

<br>

---
## Operaciones

Funciones para realizar operaciones vectorizadas entre arrays de cadenas.. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [char.add](https://numpy.org/doc/stable/reference/generated/numpy.char.add.html)(x1, x2)
  - Devuelve la concatenación de cadenas por elementos para dos arreglos de `str` o unicode.
* - [char.multiply](https://numpy.org/doc/stable/reference/generated/numpy.char.multiply.html)(a, i)
  - Retorna `(a * i)`, es decir, la concatenación múltiple de cadenas, por elementos.
```

<br>

---
## Otros

Otras funciones. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [char.decode](https://numpy.org/doc/stable/reference/generated/numpy.char.decode.html)(a[, encoding, errors])
  - Llama `bytes.decode` por elementos.
* - [char.encode](https://numpy.org/doc/stable/reference/generated/numpy.char.encode.html)(a[, encoding, errors])
  - Llama `str.encode` por elementos.
* - [char.translate](https://numpy.org/doc/stable/reference/generated/numpy.char.translate.html)(a, table[, deletechars])
  - Para cada elemento en `a`, devuelve una copia de la cadena donde se eliminan todos los caracteres que aparecen en el argumento opcional `deletechars`, y los caracteres restantes se han mapeado a través de la tabla de traducción dada.
```

<br>

---
## Reemplazar

Funciones para reemplazar subcadenas por otras. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [char.expandtabs](https://numpy.org/doc/stable/reference/generated/numpy.char.expandtabs.html)(a[, tabsize])
  - Devuelve una copia de cada elemento de la cadena donde los caracteres de tabulación se reemplazan por uno o más espacios.
* - [char.replace](https://numpy.org/doc/stable/reference/generated/numpy.char.replace.html)(a, old, new[, count])
  - Para cada elemento en `a`, devuelva una copia de la cadena con todas las apariciones de la subcadena `old` reemplazada por `new`.
```

<br>

---
## Separar y concatenar

Funciones para hacer _splitting_ y concatenaciones. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [char.join](https://numpy.org/doc/stable/reference/generated/numpy.char.join.html)(sep, seq)
  - Devuelve una cadena que es la concatenación de las cadenas en la secuencia `seq`.
* - [char.partition](https://numpy.org/doc/stable/reference/generated/numpy.char.partition.html)(a, sep)
  - Divide cada elemento con base a `sep`.
* - [char.rpartition](https://numpy.org/doc/stable/reference/generated/numpy.char.rpartition.html)(a, sep)
  - Divide cada elemento con base a `sep` más a la derecha.
* - [char.rsplit](https://numpy.org/doc/stable/reference/generated/numpy.char.rsplit.html)(a[, sep, maxsplit])
  - Para cada elemento de `a`, devuelva una lista de las palabras de la cadena, utilizando `sep` como cadena delimitadora.
* - [char.split](https://numpy.org/doc/stable/reference/generated/numpy.char.split.html)(a[, sep, maxsplit])
  - Para cada elemento de `a`, devuelva una lista de las palabras de la cadena, utilizando `sep` como cadena delimitadora.
* - [char.splitlines](https://numpy.org/doc/stable/reference/generated/numpy.char.splitlines.html)(a[, keepends])
  - Para cada elemento de `a`, devuelva una lista de las líneas del elemento, rompiendo en los límites de línea.
```

<br>

---
## Strip

Funciones para eliminar caracteres al inicio, al final o ambos de los elementos de un arreglo. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [char.lstrip](https://numpy.org/doc/stable/reference/generated/numpy.char.lstrip.html)(a[, chars])
  - Para cada elemento en `a`, devuelva una copia con `chars` eliminados al inicio de la cadena.
* - [char.rstrip](https://numpy.org/doc/stable/reference/generated/numpy.char.rstrip.html)(a[, chars])
  - Para cada elemento en `a`, devuelva una copia con los caracteres finales eliminados.
* - [char.strip](https://numpy.org/doc/stable/reference/generated/numpy.char.strip.html)(a[, chars])
  - Para cada elemento en `a`, devuelva una copia con los caracteres iniciales y finales eliminados.
```

<br>

