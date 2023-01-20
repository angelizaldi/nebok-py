# Cadenas

El tipo de dato `str` almacenan una secuencia de caracteres encerrados entre comillas dobles o simples. `str` es considerado una secuencia. Sus principales características son:
- Es inmutable: No se puede modificar una vez creada.
- Está indexado: Sus elementos están ordenados.
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
print(u"Hello\u0020World\u0021") 
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
- `\’`: Comilla simple.
- `\”`: Comilla doble.
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
x = "Hello"
y = "World!"

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

Se puede verificar que un patrón esté dentro de una cadena con los operadores `in` y `not in`, retornando un valor lógico.
```python
# Verificar que "pattern" exista en "string"
pattern in string

# Verificar que "pattern" no exista en "string"
pattern in string
```
- _pattern_ \- `str`: Patrón a buscar. Puede ser partes de palabras, palabras enteras o frases.
- _string_ \- `str`: Cadena donde se buscará _pattern_.

---
## Iteración

Las cadenas son una secuencia, esto permite que se puede usar una cadena como el rango en un `for loop`, iterando caracter por caracter:
```python
for i in string:
    expression
```
- _string_ \- `str`: Cadena sobre la cual se iterará.

---
## Subsetting y slicing: 


### Subsetting:
Para seleccionar caracteres de una cadena tener en cuenta las siguientes características:
- Se utilizan corchetes `[]` para acceder a los caracteres, junto con la caden y el índice del elemento: <br/>
`X[i]`
- Los índices comienza en cero (0), esto quiere decir que si quiere acceder al caracter `i`, se debe de usar `[i-1]`.
- Se puede utilizar números negativos, de manera que se comience por el último caracter. Se puede acceder al último con `[-1]`, al penúltimo elemento `[-2]`, etc.

---
### Slicing:
- Para seleccionar un rango de caracteres consecutivos se utiliza dos puntos: <br/> `X[i:j]`
- La selección por rango, tienen la característica que el primer elemento es inclusivo y el último es exclusivo, esto quiere decir que no se incluirá en el rango, si se usa el rango `[i:j]`, en realidad solo se accederá a `[i:j-1]`.
- Desde el índice `i` hasta el `j`, sin incluir el `j`: <br> `X[i:j]`
- Desde el inicio hasta el `j`, sin incluir el `j`: <br> `X[:j]`
- Desde la posición `i` hasta el final de la cadena: <br>`X[i:]`
- Toda la cadena: <br> `X[:]`
- Desde el índice `i` hasta el `j`, sin incluir el `j`, cada `k` caracteres: <br> `X[i:j:k]`

Algunos patrones útiles:
- El primer caracter: <br> `X[0]`
- El último caracter: <br> `X[-1]`
- Toda la cadena cada `k` caracteres: <br> `X[::k]`
- Toda la cadena al revés: <br> `X[::-1]`

---
## Formatos de cadenas.

En esta sección se explica el método `str.format()` y las "f-strings" que permiten darle un formato personalizado a las cadenas e incluir de manera dinámica variables en la cadena.

:::{warning} 
Existen otros métodos para hacer lo mismo como los `string.Template` o usando el operador `%`, pero no se cubrirán en esta página.
:::

---
### str.format

Es un método que sirve para imprimir valores de variables en algún formato en específico. Para ello en la cadena se deben especificar campos delimitados por corchetes `{}` donde irán los valores.

---
#### Uso

Existen tres formas principales de usar este método:

**índices**

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
**nombres**

- En la cadena, los campos `{}` deben de tener nombres, los cuales se deben especificar en `str.format()` como un par  `name=val`.

Ejemplo:
```{code-cell} ipython3
# Definir las variables
nombre = "Python"
version = 11

# Definir la platilla
cadena = "Lenguaje: {languaje}\nVersión: {version}"

# Imprimir la cadena con los valores de las variables
print(cadena.format(languaje=nombre, version=version))
```

---
**diccionario**

- El argumento de `str.format()` es un diccionario y en los campos `{}` se accede a los valores del diccionario recuperando el valor con los nombres de las llaves del diccionario. 
- Los nombres de las llaves dentro de la cadena no se deben de poner entre comillas.

Ejemplo:
```{code-cell} ipython3
# Definir el diccionario
my_dict = {"nombre": "Python", "version": 11}

# Definir la platilla
cadena = "Lenguaje: {x[nombre]}\nVersión: {x[version]}"

# Imprimir la cadena con los valores del diccionario
print(cadena.format(x=my_dict))
```

---
### f-strings

Es una alternativa al método `str.format()`, está disponible en Python 3.6+. Requiere una sintaxis más sencilla y es más rápida, para ello se agrega el prefijo `f` a una cadena. Al igual que con el método `str.format()` se utilizan llaves `{}` para insertar los valores de las variables, pero el en caso de la f-string se ponen directamente las variables o expresiones.

**Sintaxis**:
```python
f"text ... {expression} ..."
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

Se puede relaizar una conversión en la cadena, algunas conversiones disponibles son:
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
f"text ... {expression:format}"
"text ... {expression:format} ...".format(...)
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

Ejemplos_
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