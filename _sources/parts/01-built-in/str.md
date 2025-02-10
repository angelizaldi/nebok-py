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

# str

El tipo de dato `str` almacenan una secuencia de caracteres. Se definen encerrando los caracteres entre comillas dobles o simples. Sus principales características son:
- `str` es considerado una secuencia.
- Es inmutable: No se puede modificar una vez creada.
- Está indexado: Se puede acceder a sus elementos por medio de un índice, por lo tanto sus elementos están ordenados.
- Es un iterable: Se puede iterar por sus elementos y se puede utilizar la palabra reservada `in` para verificar membresía.
- Se puede hacer _subsetting_ y _slicing_ de sus caracteres.
- Se puede concatenar con otras cadenas.

:::{note}
Para más información visitar la [documentación](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str) de Python.
:::

<br>

---
## Crear una cadena

Para crear una variable de tipo de cadena usar comillas dobles o comillas simples para abrir y cerrar la cadena:
```python
# Formas de crear una cadena simple
X = "text"
X = 'text'
```

Para crear una cadena de mútiples líneas usar tres comillas dobles o tres comillas simples para abrir y cerrar la cadena:
```python
# Formas de crear una cadena de múltiples lineas
X = """
    text
    more text
    """
     
X = '''
    text
    more text
    '''
```
- Los saltos de línea (`\n`) se respetarán en la cadena.

También se puede crear la representación en cadena de otro objeto con la función `str()`:
```python
# X es la representación en cadena de Y
X = str(Y)
```

<br>

---
(str-secuencias-escape)=
## Secuencias de Escape

Son la combinación de algunos caracteres especiales, que comienzan por la barra invertida (`\`), que tienen un significado particular dentro de una cadena en Python. Las secuencias de escape son:
- `\'`: Comilla simple.
- `\"`: Comilla doble.
- `\b`: Retroceso.
- `\n`: Salto de línea.
- `\r`: Retorno de carro.
- `\t`: Tabulación.
- `\uXXXX`: Carácter unicode, donde _XXXX_ es el código _unicode_ (ver {ref}`str-unicode`).
- `\\`: Diagonal inversa.
- `\b`: Un espacio en blanco para atrás.
- `\xhh`: Valor hexadecimal, donde _hh_ es el valor hexadecimal.

```{code-cell} ipython3
# Secuencia \n
print("text1\ntext2")
```

<br>

(str-unicode)=
### Unicode

Se utiliza para poder ingresar letras o símbolos especiales. Se utilizan los códigos unicode, que se pueden consultar en [códigos unicode](https://unicode-table.com/es/#basic-latin).

Para insertar códigos unicode se debe de poner el código dentro de una cadena con el prefijo `u` y el código se pone como <code>\u<i>code</i></code>, donde <code>\u<i>code</i></code> es el código de unicode. Ejemplo:

```{code-cell} ipython3
# Ingresando un espacio en blanco y el símbolo "!" con códigos unicode:
print(u"Hola\u0020mundo\u0021") 
```

<br>

(str-raw)=
### Raw strings

Son cadenas "crudas", que ignoran las _secuencias de escape_ como `\n` y los imprime tal cual. Para crear una cadena cruda se utiliza una `r` como prefijo de la cadena.

```{code-cell} ipython3
# Una cadena normal
print("text1\ttext2")

# Una cadena cruda
print(r"text1\ttext2")
```
- Ver {ref}`str-secuencias-escape`

<br>

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

Para concatenar una misma cadena _n_ (`int`) veces usar el operador de multiplicación `*` con la cadena:
```{code-cell} ipython3
# Repetir "text " 5 veces 
print("text " * 5)
```
- Es importante que _n_ sea `int`, ya que si es `float` ocurrirá un error `TypeError`.

<br>

---
## Verificar membresía

Se puede verificar que una subcadena exista dentro de una cadena con los operadores `in` y `not in`, retornando un valor `bool`.
```python
# Verificar que "sub" exista en "string"
sub in string

# Verificar que "sub" no exista en "string"
sub not in string
```
- _sub_ \- `str`: Subcadena a buscar. Puede ser un patrón, palabras o frases.
- _string_ \- `str`: Cadena donde se buscará _sub_.

:::{note}
Si en lugar de verificar la existencia de subcadenas se desea obtener más sobre esas subcadenas revisar los {ref}`Métodos de búsqueda <str-metodos-buscar>`.
:::

<br>

---
## Iteración

Las cadenas se pueden usar como el rango en un `for loop`, iterando caracter por caracter:
```python
for i in string:
    # for body
```
- _string_ \- `str`: Cadena sobre la cual se iterará.

<br/>

---
## Subsetting y slicing: 

### Subsetting:
Para seleccionar caracteres individuales de una cadena tener en cuenta las siguientes características:
- Se utilizan corchetes `[]` para acceder a los caracteres, junto con la cadena y el índice del elemento. <br/> `X[i]`
- Los índices comienza en cero (0), esto quiere decir que si quiere acceder al caracter `n`, se debe de usar `[n-1]`. <br/>
- Se puede utilizar índices negativos, para hacer subsetting de derecha a izquierda, comenzando por el último caracter. Por ejemplo, se puede acceder al último caracter con `[-1]`, al penúltimo caracter elemento `[-2]`, etc.

Algunos patrones útiles:
- El primer caracter: <br> `X[0]`
- El caracter _n_: <br> `X[n-1]`
- El último caracter: <br> `X[-1]`

**Ejemplos**

```{code-cell} ipython3
# Definir la cadena
x = "Hola mundo!"

# Acceder al cuarto caracter
print(x[3])

# Acceder al penúltimo caracter
print(x[-2])
```

<br/>

### Slicing:
Para seleccionar un rango de caracteres consecutivos tener en cuenta las siguientes características:
- Se utiliza dos puntos, indicando los indices de inicio, fin y el paso: <br/> `X[i:j:k]`
- La selección por rango, tienen la característica que el primer elemento es inclusivo y el último es exclusivo, esto quiere decir que no se incluirá en el rango, si se usa el rango `[i:j]`, en realidad solo se accederá a `[i:j-1]`.

Algunos patrones útiles:
- Desde el índice _i_ hasta el _j_, sin incluir el _j_: <br> `X[i:j]`
- Desde el inicio hasta el _j_, sin incluir el _j_: <br> `X[:j]`
- Desde la posición _i_ hasta el final de la cadena: <br>`X[i:]`
- Toda la cadena: <br> `X[:]`
- Desde el índice _i_ hasta el _j_, sin incluir el _j_, cada `k` caracteres: <br> `X[i:j:k]`
- Toda la cadena cada `k` caracteres: <br> `X[::k]`
- Toda la cadena al revés: <br> `X[::-1]`

**Ejemplos**

```{code-cell} ipython3
# Definir la cadena
x = "Hola mundo!"

# Acceder la primer palabra
print(x[:4])

# Acceder a la segunda palabra
print(x[5:])

# La palabra al revés
print(x[::-1])
```

<br>

## Métodos de cadenas

En esta sección se enlistan los métodos del tipo `str` por categorias. 

Tener en cuenta que los métodos generalmente se aplican sobre un objeto de tipo `str`, por ejemplo, si _x_ es `str`, entonces se utiliza <code>X.<i>method_name</i></code>. Sin embargo es posible usar la cadena como argumento de <code>str.<i>method_name</i></code>. Por ejemplo:

```{code-cell} ipython3
# Definir una cadena
x = "Hola mundo!"

# Usar el metodo sobre el objeto
print(x.upper())

# Equivale a:
print(str.upper(x))
```
- Tener en cuenta que en la segunda forma la cadena siempre debe de ser el primer argumento.
- Lo anterior también se hubiera conseguido con las siguientes variantes con nombres: <br> `result=re.search(r"(?P<letters>\w+) (\d+) (?P=letters)", X)`

<br>

(str-metodos-buscar)=
### Buscar subcadenas

Métodos para buscar subcadenas en una cadena.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [index](https://docs.python.org/3/library/stdtypes.html#str.index)(sub[, start[, end]])
  - Devuelve la primer posición de la cadena donde se encuentra una subcadena. Si no encuentra la subcadena devuelve `ValueError`.
* - [find](https://docs.python.org/3/library/stdtypes.html#str.find)(sub[, start[, end]])
  - Devuelve el primer índice en la cadena donde se encuentra la subcadena _sub_. Devuelve -1 si no se encuentra _sub_.
* - [rfind](https://docs.python.org/3/library/stdtypes.html#str.rfind)(sub[, start[, end]])
  - Devuelve el índice más grande en la cadena donde se encuentra la subcadena _sub_. Devuelve -1 si no se encuentra _sub_.
* - [rindex](https://docs.python.org/3/library/stdtypes.html#str.rindex)(sub[, start[, end]])
  - Devuelve el índice más grande en la cadena donde se encuentra la subcadena _sub_. Devuelve `ValueError` si no se encuentra _sub_.
```

<br>

### Concatenaciones y splits

Métodos para separar cadenas o para crear cadenas desde iterables.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [join](https://docs.python.org/3/library/stdtypes.html#str.join)(iterable)
  - Devuelve una cadena que es la concatenación de las cadenas en un iterable. Se generará un `TypeError` si hay valores que no sean cadenas en el iterable.
* - [partition](https://docs.python.org/3/library/stdtypes.html#str.partition)(sep)
  - Divide la cadena en la primera aparición de _sep_ y devuelva un `tuple` de 3 elementos que contiene la parte anterior al separador, el propio separador y la parte después del separador.
* - [rpartition](https://docs.python.org/3/library/stdtypes.html#str.rpartition)(sep)
  - Divide la cadena en la última aparición de _sep_ y devuelva un `tuple` de 3 elementos que contiene la parte anterior al separador, el propio separador y la parte después del separador.
* - [rsplit](https://docs.python.org/3/library/stdtypes.html#str.rsplit)(sep=None, maxsplit=- 1)
  - Devuelve una lista de las palabras de la cadena, utilizando _sep_ como cadena delimitadora. Si se da _maxsplit_, como máximo se realizan _maxsplit_ divisiones. Por default se usan espacios en blanco como separador.
* - [split](https://docs.python.org/3/library/stdtypes.html#str.split)(sep=None, maxsplit=- 1)
  - Devuelve una lista de subcadenas de la cadena, utilizando _sep_ como cadena delimitadora. Si se da _maxsplit_, como máximo se realizan _maxsplit_ divisiones. Por default se usan espacios en blanco como separador.
* - [splitlines](https://docs.python.org/3/library/stdtypes.html#str.splitlines)(keepends=False)
  - Devuelve una lista de las líneas de la cadena, separando por los saltos de línea. Equivale a `str.split(sep='\n')`.
```

<br>

### Formatos y modificaciones

Métodos para modificar el formato de una cadena.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [capitalize](https://docs.python.org/3/library/stdtypes.html#str.capitalize)()
  - Devuelve una copia de la cadena con su primer carácter en mayúscula y el resto en minúsculas.
* - [casefold](https://docs.python.org/3/library/stdtypes.html#str.casefold)()
  - Devuelve una copia de la cadena en minúsculas de manera más estricta que `str.lower()`.
* - [format](https://docs.python.org/3/library/stdtypes.html#str.format)(*args, **kwargs)
  - Realiza una operación de formato de cadena. Para más información revisar {ref}`str-formatos-format`.
* - [format_map](https://docs.python.org/3/library/stdtypes.html#str.format_map)(mapping)
  - Similar a `str.format(**mapping)`, excepto que el mapeo es utilizado directamente y no copiado a un `dict`. Esto es útil si, por ejemplo, el mapeo es una subclase `dict`.
* - [lower](https://docs.python.org/3/library/stdtypes.html#str.lower)()
  - Devuelve una copia de la cadena con todos los caracteres en mayúsculas convertidos a minúsculas.
* - [swapcase](https://docs.python.org/3/library/stdtypes.html#str.swapcase)()
  - Devuelve una copia de la cadena con caracteres en mayúsculas convertidos a minúsculas y viceversa.
* - [title](https://docs.python.org/3/library/stdtypes.html#str.title)()
  - Devuelve una versión de título de la cadena donde las palabras comienzan con mayúscula y los caracteres restantes son minúsculas.
* - [upper](https://docs.python.org/3/library/stdtypes.html#str.upper)()
  - Convierte una cadena en mayúsculas.
```

<br>

### Información

Métodos que retornan información sobre la cadena.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [count](https://docs.python.org/3/library/stdtypes.html#str.count)(sub[, start[, end]])
  - Devuelve el número de ocurrencias no superpuestas de la subcadena _sub_ en el rango _[start, end]_.
* - [endswith](https://docs.python.org/3/library/stdtypes.html#str.endswith)(suffix[, start[, end]])
  - Retorna `True` si la cadena termina con algún sufijo en específico.
* - [isalnum](https://docs.python.org/3/library/stdtypes.html#str.isalnum)()
  - Retorna `True` si todos los caracteres de la cadena son alfanuméricos.
* - [isalpha](https://docs.python.org/3/library/stdtypes.html#str.isalpha)()
  - Devuelve `True` si todos los caracteres de la cadena son alfabéticos y hay al menos un carácter, `False` en caso contrario.
* - [isascii](https://docs.python.org/3/library/stdtypes.html#str.isascii)()
  - Retorna `True` si la cadena está vacía o todos los caracteres de la cadena son ASCII, `False` en caso contrario.
* - [isdecimal](https://docs.python.org/3/library/stdtypes.html#str.isdecimal)()
  - Retorna `True` si todos los caracteres en la cadena son caracteres.
* - [isdigit](https://docs.python.org/3/library/stdtypes.html#str.isdigit)()
  - Devuelve `True` si todos los caracteres de la cadena son dígitos y hay al menos un carácter, `False` en caso contrario.
* - [isidentifier](https://docs.python.org/3/library/stdtypes.html#str.isidentifier)()
  - Retorna `True` si la cadena es un identificador válido.
* - [islower](https://docs.python.org/3/library/stdtypes.html#str.islower)()
  - Retorna `True` si todos los caracteres en la cadena están en minúsculas y hay al menos un carácter en minúsculas, de lo contrario retornar `False`.
decimales y hay al menos un carácter, `False` de lo contrario.
* - [isnumeric](https://docs.python.org/3/library/stdtypes.html#str.isnumeric)()
  - Retorna `True` si todos los caracteres de la cadena son numéricos.
* - [isprintable](https://docs.python.org/3/library/stdtypes.html#str.isprintable)()
  - Retorna `True` si todos los caracteres en la cadena son imprimibles o si es una cadena vacía, `False` en caso contrario.
* - [isspace](https://docs.python.org/3/library/stdtypes.html#str.isspace)()
  - Retorna `True` si solo hay espacios en blanco en la cadena y hay al menos un carácter, `False` en caso contrario.
* - [istitle](https://docs.python.org/3/library/stdtypes.html#str.istitle)()
  - Retorna `True` si la cadena es una cadena con título y hay al menos una carácter.
* - [isupper](https://docs.python.org/3/library/stdtypes.html#str.isupper)()
  - Retorna `True` si todos los caracteres son mayúsculas y hay al menos un caracter alfabético en mayúsculas, `False` en caso contrario.
* - [startswith](https://docs.python.org/3/library/stdtypes.html#str.startswith)(prefix[, start[, end]])
  - Devuelve `True` si la cadena comienza con el prefijo; de lo contrario, devuelve `False`.
```

<br>

### Otros

Otros métodos para cadenas.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [encode](https://docs.python.org/3/library/stdtypes.html#str.encode)(encoding='utf-8', errors='strict')
  - Devuelve la cadena codificada en bytes.
* - [maketrans](https://docs.python.org/3/library/stdtypes.html#str.maketrans)(x[, y[, z]])
  - Este método estático devuelve una tabla de traducción utilizable para `str.translate()`.
* - [translate](https://docs.python.org/3/library/stdtypes.html#str.translate)(table)
  - Devuelve una copia de la cadena en la que se ha mapeado cada carácter de acuerdo al mapeo indicado en `str.maketrans()`.
```

<br>

### Reemplazar y eliminar subcadenas

Métodos para reemplazar o remover subcadenas dentro de una cadena.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [expandtabs](https://docs.python.org/3/library/stdtypes.html#str.expandtabs)(tabsize=8)
  - Devuelve una copia de la cadena donde todos los caracteres de tabulación se reemplazan por uno o más espacios.
* - [removeprefix](https://docs.python.org/3/library/stdtypes.html#str.removeprefix)(prefix, /)
  - Devuelve una copia de la cadena eliminando el prefijo _prefix_ al inicio de la cadena, si existe.
* - [removesuffix](https://docs.python.org/3/library/stdtypes.html#str.removesuffix)(suffix, /)
  - Retorna una copia de la cadena eliminando el sufijo _suffix_ al final de la cadena, si existe.
* - [replace](https://docs.python.org/3/library/stdtypes.html#str.replace)(old, new[, count])
  - Devuelve una copia de la cadena con todas las apariciones de la subcadena _old_ reemplazada por _new_. Si se da el argumento opcional _count_, solo las primeras _count_ ocurrencias son reemplazadas.
```

<br>

### Strip y pads

Métodos para agregar o eliminar caracteres al inicio, final o ambos de una cadena.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [center](https://docs.python.org/3/library/stdtypes.html#str.center)(width[, fillchar])
  - Retorna una cadena agregando caracteres al princio y al final, para que tenga una longitud determinada y la cadena original esté al centro.
* - [ljust](https://docs.python.org/3/library/stdtypes.html#str.ljust)(width[, fillchar])
  - Justifica el texto a la izquierda, agregando caracteres al final de la cadena para que tenga una longitud determinada.
* - [lstrip](https://docs.python.org/3/library/stdtypes.html#str.lstrip)([chars])
  - Elimina los espacios en blanco o un conjunto de caracteres en específico al principio de la cadena. Retorna una copia de la cadena.
* - [rjust](https://docs.python.org/3/library/stdtypes.html#str.rjust)(width[, fillchar])
  - Justifica el texto a la derecha, agregando caracteres al principio de la cadena para que tenga una longitud determinada.
* - [rstrip](https://docs.python.org/3/library/stdtypes.html#str.rstrip)([chars])
  - Elimina los espacios en blanco o un conjunto de caracteres en específico al final de la cadena.
* - [strip](https://docs.python.org/3/library/stdtypes.html#str.strip)([chars])
  - Elimina los espacios en blanco o un conjunto de caracteres, al principio y final de una cadena.
* - [zfill](https://docs.python.org/3/library/stdtypes.html#str.zfill)(width)
  - Retorna una cadena agregando ceros al principio de la cadena (si es necesario), para que tenga una longitud específica.
```

<br>

---
(str-formatos)=
## Formatos de cadenas.

En esta sección se explica el método `str.format()` y las "_f-strings_" que permiten darle un formato personalizado a las cadenas e incluir de manera dinámica variables en la cadena.

:::{warning} 
Existen otros métodos para hacer lo mismo como los `string.Template` o usando el operador `%`, pero no se cubrirán en este sitio.
:::

<br/>

(str-formatos-format)=
### str.format

El método `str.format` sirve para valores en textos predefinidos, opcionalmente en algún formato en específico. Para ello en la cadena se deben especificar campos delimitados por corchetes `{}` donde irán los valores.

Existen tres formas principales de usar este método:

#### 1. Índices

Dentro de la cadena se usa _{0}, {1}, {2}, ..._, que indican los índices de los argumentos de `str.format()`, donde 0 es el primer argumento, 1 el segundo, etc. 
- Un mismo índice `{i}` se puede poner múltiples veces, de manera que se inserte el mismo valor más de una vez en una misma cadena. 
- Los índice comienzan en cero.
- Si no se indican los índices dentro de `{}` se empatan por posición los argumentos con los campos `{}`, pero el número de `{}` debe ser igual al número de argumentos.

**Ejemplo**:

```{code-cell} ipython3
# Definir las variables
nombre = "Python"
version = 11

# Definir la plantilla
cadena = "Lenguaje: {0}\nVersión: {1}"

# Imprimir la cadena con los valores de las variables
print(cadena.format(nombre, version))
```
- En lugar de variables se pueden ingresar las valores directamente: <br/> `pprint(cadena.format("Python", 11))`

<br/>

#### 2. Llaves

En la cadena, los campos `{}` pueden de tener nombres de llaves, las cuales se deben especificar en `str.format()` como un par  `name=val`.

**Ejemplo**:

```{code-cell} ipython3
# Definir las variables
nombre = "Python"
version = 11

# Definir la plantilla
cadena = "Lenguaje: {name}\nVersión: {version}"

# Imprimir la cadena con los valores de las variables
print(cadena.format(name=nombre, version=version))
```
- En lugar de variables se pueden ingresar las valores directamente: <br/> `print(cadena.format(name="Python", version=11))`

<br/>

#### 3. Diccionario

El argumento de `str.format()` puede ser un diccionario y en los campos `{}` se accede a los valores del diccionario recuperando el valor con los nombres de las llaves del diccionario. 
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
f"text {expression} more text"
```
- _expression_: Es un valor, un objeto o incluso funciones y/o métodos que retornen un objeto imprimible. El valor mostrado será el mismo que el del método `__str__()` o `__repr__()` de la clase del objeto.

<br/>

**Ejemplo**:

```{code-cell} ipython3
# Definir las variables
nombre = "Python"
version = 11

# Imprimir la cadena con los valores de las variables
print(f"Lenguaje: {nombre}\nVersión: {version}")
```
- En lugar de variables se pueden ingresar las valores directamente: <br/> `print(f"Lenguaje: {'Python'}\nVersión: {1}")`
    - Notar que si se usaron comillas dobles afuera, entonces se deben de usar comillas simples adentro y viceversa.

<br/>

Se puede realizar una conversión en los campos `{}`, algunas conversiones disponibles son:
- `!s`: Version en cadena.
- `!r`: Cadena en versión imprimible, es decir, entre comillas, (solo funciona si la expresión es `str`).
- `!a`: Como `!r` pero ignora los caracteres non-ASCII.

<br/>

Ejemplo:
```{code-cell} ipython3
# Definir las variables
nombre = "Python"
version = 11

# Imprimir la cadena con los valores de las variables
print(f"Lenguaje: {nombre!r}\nVersión: {version!s}")
```

<br/>

---
### Formatos

Para dar formatos en el método `str.format()` y en las f-string, se utiliza dos puntos y el formato que se quiere dar dentro de las llaves `{}`:
```python
# f-string
f"text {expression:format} more text"

# método format
"text {expression:format} more text".format(...)
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
  - Imprimir una fecha, en un formato específico, utilizando los {ref}`Códigos de fechas <date-codes>`, junto con otros caracteres. Por ejemplo `%Y-%m-%d`.
```
- _N_: Son números enteros, suelen ser opcionales.
- _expression_: Es la expresión, número, cadena, etc. a la que se le dará formato o en el caso de que se use el método `str.format()` es el índice o llave que se le dará formato. <br/> `f"P-value: {.05:.2%}"` <br/> `"P-value: {0:.2%}".format(0.05)` <br/> `"P-value: {p_value:.2%}".format(p_value=0.05)`

<br/>

**Ejemplos**:

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