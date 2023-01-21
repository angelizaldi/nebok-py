---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python
---

# Cadenas

El tipo de dato `str` almacenan una secuencia de caracteres encerrados entre comillas dobles o simples. `str` es considerado una secuencia. Sus principales características son:
- Es inmutable: No se puede modificar una vez creada.
- Está indexado: Se puede acceder a sus elementos por medio de un índice.
- Es un iterable: Se puede iterar por sus elementos y se puede utilizar la palabra reservada `in` para verificar membresía.
- Se puede hacer _subsetting_ y _slicing_ de sus caracteres.
- Se puede concatenar con otras cadenas.

---
## Crear una cadena

Para crear una variable de tipo de cadena usar comillas dobles o comillas simples para abrir y cerrar la cadena:
```python
# Formas de crear una cadena simple
x = "text"
x = 'text'
```

Para crear una cadena de mútiples líneas usar tres comillas dobles o tres comillas simples para abrir y cerrar la cadena:
```python
# Formas de crear una cadena de múltiples lineas
x = """
    text
    more text
    """
     
x = '''
    text
    more text
    '''
```
- Los saltos de línea (`\n`) se respetarán en la cadena.

---
### Unicode

Se utiliza para poder ingresar letras o símbolos especiales. Se utilizan los códigos unicode, que se pueden consultar en [códigos unicode](https://unicode-table.com/es/#basic-latin).

Para insertar códigos unicode se debe de poner el código dentro de una cadena con el prefijo `u` y el código se pone como <code>\u<i>code</i></code>, donde <code>\u<i>code</i></code> es el código de unicode. Ejemplo:

```{code-cell} ipython3
# Ingresando un espacio en blanco y el símbolo "!" con códigos unicode:
print(u"Hola\u0020mundo\u0021") 
```

---
### Raw strings

Son cadenas "crudas", que ignoran _caracteres ilegales_ como `\n` y los imprime tal cual. Para crear una cadena cruda se utiliza una `r` como prefijo de la cadena.

```{code-cell} ipython3
# Una cadena normal
print("text1\ttext2")

# Una cadena cruda
print(r"text1\ttext2")
```

Los caracteres ilegales son:
- `\'`: Comilla simple.
- `\"`: Comilla doble.
- `\n`: Salto de línea.
- `\t`: Tabulación.
- `\\`: Diagonal inversa.
- `\b`: Un espacio en blanco para atrás.
- `\xhh`: Valor hexadecimal.


---
## Concatenar y repetir cadenas:

Para concatenar cadenas se usa el operador `+`. Usar únicamente con objetos de tipo `str`:
```{code-cell} ipython3
# Definir las cadenas
x = "Hola"
y = "mundo!"

# Concatenar las cadenas
print(x + " " + y)
```

Para concatenar una misma cadena `n` veces usar el operador de multiplicación `*` con la cadena:
```{code-cell} ipython3
# Repetir "text " 5 veces 
print("text " * 5)
```

---
## Verificar membresía

Se puede verificar que una subcadena exista dentro de una cadena con los operadores `in` y `not in`, retornando un valor lógico.
```python
# Verificar que "sub" exista en "string"
sub in string

# Verificar que "sub" no exista en "string"
sub in string
```
- _sub_ \- `str`: Subcadena a buscar. Puede ser un patrón, palabras o frases.
- _string_ \- `str`: Cadena donde se buscará _sub_.

---
## Iteración

Las cadenas se pueden usar como el rango en un `for loop`, iterando caracter por caracter:
```python
for i in string:
    expression
```
- _string_ \- `str`: Cadena sobre la cual se iterará.

---
## Subsetting y slicing: 


### Subsetting:
Para seleccionar caracteres individuales de una cadena tener en cuenta las siguientes características:
- Se utilizan corchetes `[]` para acceder a los caracteres, junto con la cadena y el índice del elemento. 
- Los índices comienza en cero (0), esto quiere decir que si quiere acceder al caracter `n`, se debe de usar `[n-1]`. <br/>
- Se puede utilizar índices negativos, para hacer subsetting de derecha a izquierda, comenzando por el último caracter. Por ejemplo, se puede acceder al último caracter con `[-1]`, al penúltimo caracter elemento `[-2]`, etc.

Algunos patrones útiles:
- El primer caracter: <br> `X[0]`
- El caracter _n_: <br> `X[n-1]`
- El último caracter: <br> `X[-1]`

---
### Slicing:
Para seleccionar un rango de caracteres consecutivos tener en cuenta las siguientes características:
- Se utiliza dos puntos, indicando los indices de inicio, fin y el paso: <br/> `X[i:j:k]`
- La selección por rango, tienen la característica que el primer elemento es inclusivo y el último es exclusivo, esto quiere decir que no se incluirá en el rango, si se usa el rango `[i:j]`, en realidad solo se accederá a `[i:j-1]`.

Algunos patrones útiles:
- Desde el índice `i` hasta el `j`, sin incluir el `j`: <br> `X[i:j]`
- Desde el inicio hasta el `j`, sin incluir el `j`: <br> `X[:j]`
- Desde la posición `i` hasta el final de la cadena: <br>`X[i:]`
- Toda la cadena: <br> `X[:]`
- Desde el índice `i` hasta el `j`, sin incluir el `j`, cada `k` caracteres: <br> `X[i:j:k]`
- Toda la cadena cada `k` caracteres: <br> `X[::k]`
- Toda la cadena al revés: <br> `X[::-1]`

---
## Métodos de cadenas

En esta sección se enlistan los métodos del tipo `str` por categorias. 

Tener en cuenta que los métodos generalmente se aplican sobre un objeto de tipo `str`, por ejemplo, si `X` es `str`, entonces se utiliza <code>X.<i>method_name</i></code>. Sin embargo es posible usar la cadena como argumento de <code>str.<i>method_name</i></code>. Por ejemplo.

```{code-cell} ipython3
# Definir una cadena
X = "hola mundo"

# Usar el metodo sobre el objeto
print(X.upper())

# Equivale a:
print(str.upper(X))
```
- Tener en cuenta que en la segunda forma la cadena siempre debe de ser el primer argumento.


---
### Buscar subcadenas

Métodos para buscar subcadenas en una cadena.

```{list-table} Buscar
:header-rows: 1

* - Funciones
  - Descripción
* - [index](https://docs.python.org/3/library/stdtypes.html#str.index)(sub[, start[, end]])
  - Devuelve la primer posición de la cadena donde se encuentra una subcadena. Si no encuentra la subcadena devuelve `ValueError`.
* - [find](https://docs.python.org/3/library/stdtypes.html#str.find)(sub[, start[, end]])
  - Devuelve el primer índice en la cadena donde se encuentra la subcadena `sub`. Devuelve -1 si no se encuentra `sub`.
* - [rfind](https://docs.python.org/3/library/stdtypes.html#str.rfind)(sub[, start[, end]])
  - Devuelve el índice más grande en la cadena donde se encuentra la subcadena `sub`. Devuelve -1 si no se encuentra `sub`.
* - [rindex](https://docs.python.org/3/library/stdtypes.html#str.rindex)(sub[, start[, end]])
  - Devuelve el índice más grande en la cadena donde se encuentra la subcadena `sub`. Devuelve `ValueError` si no se encuentra `sub`.
```

---
### Formato de la cadena

Métodos para modificar el formato de una cadena.

```{list-table} Formato
:header-rows: 1

* - Funciones
  - Descripción
* - [zfill](https://docs.python.org/3/library/stdtypes.html#str.zfill)(width)
  - Retorna una cadena agregando ceros al principio de la cadena (si es necesario), para que tenga una longitud específica.
* - [ljust](https://docs.python.org/3/library/stdtypes.html#str.ljust)(width[, fillchar])
  - Justifica el texto a la izquierda, agregando caracteres al final de la cadena para que tenga una longitud determinada.
* - [rjust](https://docs.python.org/3/library/stdtypes.html#str.rjust)(width[, fillchar])
  - Justifica el texto a la derecha, agregando caracteres al principio de la cadena para que tenga una longitud determinada.
* - [title](https://docs.python.org/3/library/stdtypes.html#str.title)()
  - Devuelve una versión de título de la cadena donde las palabras comienzan con mayúscula y los caracteres restantes son minúsculas.
* - [upper](https://docs.python.org/3/library/stdtypes.html#str.upper)()
  - Convierte una cadena en mayúsculas.
* - [swapcase](https://docs.python.org/3/library/stdtypes.html#str.swapcase)()
  - Devuelve una copia de la cadena con caracteres en mayúsculas convertidos a minúsculas y viceversa.
* - [casefold](https://docs.python.org/3/library/stdtypes.html#str.casefold)()
  - Retorna una copia de la cadena con todos los caracteres en minúsculas.
* - [format](https://docs.python.org/3/library/stdtypes.html#str.format)(*args, **kwargs)
  - Realice una operación de formato de cadena.
* - [center](https://docs.python.org/3/library/stdtypes.html#str.center)(width[, fillchar])
  - Retorna una cadena agregando caracteres al princio y al final, para que tenga una longitud determinada y la cadena original esté al centro.
* - [format_map](https://docs.python.org/3/library/stdtypes.html#str.format_map)(mapping)
  - Similar a `str.format(**mapping)`, excepto que el mapeo es utilizado directamente y no copiado a un `dict`. Esto es útil si, por ejemplo, el mapeo es una subclase `dict`.
* - [lower](https://docs.python.org/3/library/stdtypes.html#str.lower)()
  - Devuelve una copia de la cadena con todos los caracteres en mayúsculas convertidos a minúsculas.
* - [capitalize](https://docs.python.org/3/library/stdtypes.html#str.capitalize)()
  - Devuelve una copia de la cadena con su primer carácter en mayúscula y el resto en minúsculas.
```

---
### Información de la cadena

Métodos para obtener información sobre la cadena.

```{list-table} Información
:header-rows: 1

* - Funciones
  - Descripción
* - [isdigit](https://docs.python.org/3/library/stdtypes.html#str.isdigit)()
  - Devuelve `True` si todos los caracteres de la cadena son dígitos y hay al menos un carácter, `False` en caso contrario.
* - [isprintable](https://docs.python.org/3/library/stdtypes.html#str.isprintable)()
  - Retorna `True` si todos los caracteres en la cadena son imprimibles o si es una cadena vacía, `False` en caso contrario.
* - [isspace](https://docs.python.org/3/library/stdtypes.html#str.isspace)()
  - Retorna `True` si solo hay espacios en blanco en la cadena y hay al menos un carácter, `False` en caso contrario.
* - [isupper](https://docs.python.org/3/library/stdtypes.html#str.isupper)()
  - Retorna `True` si todos los caracteres son mayúsculas y hay al menos un caracter alfabético en mayúsculas, `False` en caso contrario.
* - [count](https://docs.python.org/3/library/stdtypes.html#str.count)(sub[, start[, end]])
  - Devuelve el número de ocurrencias no superpuestas de la subcadena `sub` en el rango [`start`, `end`].
* - [istitle](https://docs.python.org/3/library/stdtypes.html#str.istitle)()
  - Retorna `True` si la cadena es una cadena con título y hay al menos una carácter.
* - [startswith](https://docs.python.org/3/library/stdtypes.html#str.startswith)(prefix[, start[, end]])
  - Devuelve `True` si la cadena comienza con el prefijo; de lo contrario, devuelve `False`.
* - [islower](https://docs.python.org/3/library/stdtypes.html#str.islower)()
  - Retorna `True` si todos los caracteres en la cadena están en minúsculas y hay al menos un carácter en minúsculas, de lo contrario retornar `False`.
* - [isdecimal](https://docs.python.org/3/library/stdtypes.html#str.isdecimal)()
  - Retorna `True` si todos los caracteres en la cadena son caracteres decimales y hay al menos un carácter, `False` de lo contrario.
* - [isidentifier](https://docs.python.org/3/library/stdtypes.html#str.isidentifier)()
  - Retorna `True` si la cadena es un identificador válido.
* - [endswith](https://docs.python.org/3/library/stdtypes.html#str.endswith)`(suffix[, start[, end]])`
  - Retorna `True` si la cadena termina con algún sufijo en específico.
* - [isalpha](https://docs.python.org/3/library/stdtypes.html#str.isalpha)()
  - Devuelve `True` si todos los caracteres de la cadena son alfabéticos y hay al menos un carácter, `False` en caso contrario.
* - [isascii](https://docs.python.org/3/library/stdtypes.html#str.isascii)()
  - Retorna `True` si la cadena está vacía o todos los caracteres de la cadena son ASCII, `False` en caso contrario.
* - [isalnum](https://docs.python.org/3/library/stdtypes.html#str.isalnum)()
  - Retorna `True` si todos los caracteres de la cadena son alfanuméricos.
* - [isnumeric](https://docs.python.org/3/library/stdtypes.html#str.isnumeric)()
  - Retorna `True` si todos los caracteres de la cadena son numéricos.
```

---
### Otros

Otros métodos para cadenas.

```{list-table} Otros
:header-rows: 1

* - Funciones
  - Descripción
* - [maketrans](https://docs.python.org/3/library/stdtypes.html#str.maketrans)(x[, y[, z]])
  - Este método estático devuelve una tabla de traducción utilizable para `str.translate()`.
* - [translate](https://docs.python.org/3/library/stdtypes.html#str.translate)(table)
  - Devuelve una copia de la cadena en la que se ha mapeado cada carácter de acuerdo al mapeo indicado en `str.maketrans()`.
* - [encode](https://docs.python.org/3/library/stdtypes.html#str.encode)(encoding='utf-8', errors='strict')
  - Devuelve la cadena codificada en bytes.
```

---
### Reemplazar y remover subcadenas.

Métodos para reemplazar o remover subcadenas dentro de una cadena.

```{list-table} Reemplazar
:header-rows: 1

* - Funciones
  - Descripción
* - [removeprefix](https://docs.python.org/3/library/stdtypes.html#str.removeprefix)(prefix, /)
  - Devuelve una copia de la cadena eliminando el prefijo `prefix` al inicio de la cadena, si existe.
* - [expandtabs](https://docs.python.org/3/library/stdtypes.html#str.expandtabs)`(tabsize=8)`
  - Devuelve una copia de la cadena donde todos los caracteres de tabulación se reemplazan por uno o más espacios.
* - [removesuffix](https://docs.python.org/3/library/stdtypes.html#str.removesuffix)(suffix, /)
  - Retorna una copia de la cadena eliminando el sufijo `suffix` al final de la cadena, si existe.
* - [replace](https://docs.python.org/3/library/stdtypes.html#str.replace)(old, new[, count])
  - Devuelve una copia de la cadena con todas las apariciones de la subcadena `old` reemplazada por `new`. Si se da el argumento opcional `count`, solo las primeras `count` ocurrencias son reemplazadas.
```

---
### Joins y splits

Métodos para separar cadenas o para crear cadenas desde iterables.

```{list-table} Separar y Unir
:header-rows: 1

* - Funciones
  - Descripción
* - [join](https://docs.python.org/3/library/stdtypes.html#str.join)(iterable)
  - Devuelve una cadena que es la concatenación de las cadenas en un iterable. Se generará un `TypeError` si hay valores que no sean cadenas en el iterable.
* - [split](https://docs.python.org/3/library/stdtypes.html#str.split)(sep=None, maxsplit=- 1)
  - Devuelve una lista de las palabras de la cadena, utilizando `sep` como cadena delimitadora. Si se da `maxsplit`, como máximo se realizan `maxsplit` divisiones. Por default se usan espacios en blanco como separador.
* - [rsplit](https://docs.python.org/3/library/stdtypes.html#str.rsplit)(sep=None, maxsplit=- 1)
  - Devuelve una lista de las palabras de la cadena, utilizando `sep` como cadena delimitadora. Si se da `maxsplit`, como máximo se realizan `maxsplit` divisiones. Por default se usan espacios en blanco como separador.
* - [splitlines](https://docs.python.org/3/library/stdtypes.html#str.splitlines)(keepends=False)
  - Devuelve una lista de las líneas de la cadena, separando por los saltos de línea.
* - [partition](https://docs.python.org/3/library/stdtypes.html#str.partition)(sep)
  - Divide la cadena en la primera aparición de `sep` y devuelva un `tuple` de 3 elementos que contiene la parte anterior al separador, el propio separador y la parte después del separador.
* - [rpartition](https://docs.python.org/3/library/stdtypes.html#str.rpartition)(sep)
  - Divide la cadena en la última aparición de `sep` y devuelva un `tuple` de 3 elementos que contiene la parte anterior al separador, el propio separador y la parte después del separador.
```

---
### Strip

Métodos para eliminar caracteres al inicio, final o ambos de una cadena.

```{list-table} Strip
:header-rows: 1

* - Funciones
  - Descripción
* - [strip](https://docs.python.org/3/library/stdtypes.html#str.strip)([chars])
  - Elimina los espacios en blanco o un conjunto de caracteres, al principio y final de una cadena.
* - [lstrip](https://docs.python.org/3/library/stdtypes.html#str.lstrip)([chars])
  - Elimina los espacios en blanco o un conjunto de caracteres en específico al principio de la cadena. Retorna una copia de la cadena.
* - [rstrip](https://docs.python.org/3/library/stdtypes.html#str.rstrip)([chars])
  - Elimina los espacios en blanco o un conjunto de caracteres en específico al final de la cadena.
```

---
## Formatos de cadenas.

En esta sección se explica el método `str.format()` y las "_f-strings_" que permiten darle un formato personalizado a las cadenas e incluir de manera dinámica variables en la cadena.

:::{warning} 
Existen otros métodos para hacer lo mismo como los `string.Template` o usando el operador `%`, pero no se cubrirán en esta página.
:::

---
### str.format

Es un método que sirve para imprimir valores de variables en algún formato en específico. Para ello en la cadena se deben especificar campos delimitados por corchetes `{}` donde irán los valores.

---
#### Uso

Existen tres formas principales de usar este método:

**1. índices**

- Dentro de la cadena se usa `{0}`, `{1}`, `{2}`, ..., que indican los índices de los argumentos de `str.format()`, donde 0 es el primer argumento, 1 el segundo, etc. 
- Un mismo índice `{i}` se puede poner múltiples veces, de manera que lo imprima más de una vez en una misma cadena. 
- Los índice comienzan en cero.
- Si no se indican los índices dentro de `{}` se empatan por posición los argumentos con los campos `{}`, pero el número de llaves debe ser igual al número de argumentos.

Ejemplo:
```{code-cell} ipython3
# Definir las variables
nombre = "Python"
version = 11

# Definir la plantilla
cadena = "Lenguaje: {0}\nVersión: {1}"

# Imprimir la cadena con los valores de las variables
print(cadena.format(nombre, version))
```

---
**2. nombres**

- En la cadena, los campos `{}` deben de tener nombres, los cuales se deben especificar en `str.format()` como un par  `name=val`.

Ejemplo:
```{code-cell} ipython3
# Definir las variables
nombre = "Python"
version = 11

# Definir la plantilla
cadena = "Lenguaje: {languaje}\nVersión: {version}"

# Imprimir la cadena con los valores de las variables
print(cadena.format(languaje=nombre, version=version))
```

---
**3. diccionario**

- El argumento de `str.format()` es un diccionario y en los campos `{}` se accede a los valores del diccionario recuperando el valor con los nombres de las llaves del diccionario. 
- Los nombres de las llaves dentro de la cadena no se deben de poner entre comillas.

Ejemplo:
```{code-cell} ipython3
# Definir el diccionario
my_dict = {"nombre": "Python", "version": 11}

# Definir la plantilla
cadena = "Lenguaje: {x[nombre]}\nVersión: {x[version]}"

# Imprimir la cadena con los valores del diccionario
print(cadena.format(x=my_dict))
```

---
### f-strings

Es una alternativa al método `str.format()`, está disponible en Python 3.6+. Requiere una sintaxis más sencilla y es más rápida, para ello se agrega el prefijo `f` a una cadena. Al igual que con el método `str.format()` se utilizan llaves `{}` para insertar los valores de las variables, pero en el caso de las f-string se ponen directamente las variables o expresiones.

**Sintaxis**:
```python
f"... {expression} ..."
```
- _expression_: Es un valor, un objeto o incluso funciones y/o métodos que retornen un objeto imprimible. El valor mostrado será el mismo que el del método `__str__()` o `__repr__()` de la clase del objeto.

Ejemplo:
```{code-cell} ipython3
# Definir las variables
nombre = "Python"
version = 11

# Imprimir la cadena con los valores de las variables
print(f"Lenguaje: {nombre}\nVersión: {version}")
```

Se puede realizar una conversión en los campos `{}`, algunas conversiones disponibles son:
- `!s`: Version en cadena.
- `!r`: Cadena en versión imprimible, es decir, entre comillas, (solo funciona si la expresión es `str`).
- `!a`: Como `!r` pero ignora los caracteres non-ASCII.

Ejemplo:
```{code-cell} ipython3
# Definir las variables
nombre = "Python"
version = 11

# Imprimir la cadena con los valores de las variables
print(f"Lenguaje: {nombre!r}\nVersión: {version!s}")
```

### Formatos

Para dar formatos en el método `str.format()` y en f-string, se utiliza dos puntos y el formato que se quiere dar dentro de las llaves `{}`:
```python
# f-string
f"... {expression:format}"

# método format
"... {expression:format} ...".format(...)
```
- <code><i> format </i></code>: Es el formato que se quiere dar.

Los formatos disponibles son:

```{list-table}
:header-rows: 1
:name: label-to-reference

* - Formato.
  - Resultado.
* - `{expression:<N}`
  - Alinear el texto a la izquierda, dejando _N_ espacios en blanco a la derecha.
* - `{expression:>N}`
  - Alinear el texto a la derecha, dejando _N_ espacios en blanco a la izquierda.
* - `{expression:^N}`
  - Alinear el texto al centro, dejando _N/2_ espacios en blanco a la der. e izq.
* - `{expression:+}`
  - Imprimir el signo del número, positivos y negativos.
* - `{expression:-}`
  - Imprimir el signo del número, solo el de los negativos.
* - `{expression:,}`
  - Separar con una coma los miles.
* - `{expression:.Ne}`
  - Imprimir el número en formato científico, con la e en minúscula, con _N_ decimales.
* - `{expression:.NE}`
  - Imprimir el número en formato científico, con la E en minúscula, con _N_ decimales.
* - `{expression:.Nf}`
  - Imprimir un número décimal, con _N_ decimales.
* - `{expression:.N%}`
  - Imprimir un número en formato de porcentaje, con _N_ décimales, el número tiene que ser >0 y <1.
* - `{expression:s}`
  - Dar formato como cadena.
* - `{expression:date-format}`
  - Imprimir una fecha, en un formato específico, utilizando los códigos de fechas, junto con otros caracteres. Por ejemplo `%Y-%m-%d`.
```
- _N_: Son números enteros, suelen ser opcionales.
- _expression_: Es la expresión, número, cadena, etc. a la que se le dará formato.

**Ejemplos***

```{code-cell} ipython3
# Definir la variable
x = 1897.9876

# Diversos formatos que se pueden aplicar a "x".
print(f"Sin formato: {x}")
print(f"Separar los miles: {x:,}")
print(f"Notación científica con 1 décimal: {x:.1e}")
print(f"Con tres décimales (redondea): {x:.3f}")
print(f"Combinación de separación de miles y 2 décimales: {x:,.2f}")
```