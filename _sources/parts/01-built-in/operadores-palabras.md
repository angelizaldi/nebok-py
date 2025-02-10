# Operadores y palabras reservadas

En esta sección se enlistan los operadores y palabras reservadas disponibles en Python.

## Aritméticos
Operadores para realizar operaciones aritméticas entre números.

|Nombre|Operador|Comentarios|
|:----------|:----------:|:------|
|Suma|`+`||
|Resta|`-`||
|Multiplicación|`*`||
|División|`/`||
|Exponenciación|`**`||
|Módulo|`%`|Retorna el residuo de una división|
|División parte entera|`//`|Rertorna el cociente de una división|


```{attention} 
El operador `+` también se usa para concatenar secuencias (`list`, `tuple` y `str`) y `*` se utiliza para repetir secuencias.
```

:::{attention}
En objetos tipo `set` algunos de estos operadores funcionan como operadores de conjuntos. Ver {ref}`set-operaciones-conjuntos`.
:::

:::{tip}
Para operaciones más complejas se recomienda utilizar paréntesis _( )_ para diferenciar de mejor manera cada operación.
:::

<br>

(built-in-operadores-asignacion)=
## Asignación

Operadores para asignación de valores.

|Nombre|Operador|
|:----------|:----------:|
|Asignación|`=`|
|Asignación recursivo aritmético|`+=`, `-=`, `*=`, `/=`, `**=`, `%=`, `//=`|
|Asignación recursivo lógico|`\|=`, `&=`|

<br>

(built-in-operadores-comparacion)=
## Comparación

Operadores para la comparación de valores.

|Nombre|Operador|
|:----------|:----------:|
|Igualdad|`==`|
|Diferencia|`!=`|
|Menor que|`<`|
|Mayor que|`>`|
|Menor o igual que|`<=`|
|Mayor o igual que|`>=`|

:::{note}
Las comparaciones entre cadenas (tipo `str`) se realizan comparaciones lexicográficas, en el orden alfabético y valores ASCII.
:::

:::{warning}
En objetos tipo `set` algunos de estos operadores funcionan como operadores de conjuntos. Ver {ref}`set-operaciones-conjuntos`.
:::

<br>

(built-in-operadores-bitwise)=
## Bitwise

Estos operadores operan a nivel de bits, trabajan sobre la representación binaria de los números. Recomendado utilizar únicamente con datos binarios. No se debe de confundir estos operadores con los {ref}`built-in-operadores-bool` que trabajan con valores `True` y `False`.

|Nombre|Operador|
|:----------|:----------:|
|Y|`&`|
|O|`\|`|
|NO|`~`|
|O excluyente (XOR)|`^`|
|Desplazamiento a la izquierda|`<<`|
|Desplazamiento a la derecha|`>>`|

**Ejemplo:**

:::{caution}
La tabla es para ejemplificar el resultado de utilizar los operadores con _1_ y _0_, pero los operadores funcionan con sus representaciones binarias, es decir _0b0001_ y _0b0000_ respectivamente. Además tener en cuenta que estos operadores no se limitan a trabajar solo con _0_ y _1_ sino con cualquier número (en su representación en sistema binario).
:::

|X|Y|X&Y|X\|Y|~X|X^Y|
|:---:|:---:|:---:|:---:|:---:|:---:|
|1|1|1|1|0|0|
|1|0|0|1|0|1|
|0|1|0|1|1|1|
|0|0|0|0|1|0|

:::{tip}
Para conocer la representación en binario de cualquier número usar la función `bin()`.
:::

:::{warning}
En objetos tipo `set` algunos de estos operadores funcionan como operadores de conjuntos. Ver {ref}`set-operaciones-conjuntos`.
:::

<br>

(built-in-operadores-bool)=
## Booleanos

Son los operadores para realizar operaciones entre valores booleanos.

|Nombre|Palabra|
|:----------|:----------:|
|Verdadero|`True`|
|Falso|`False`|
|Y|`and`|
|O|`or`|
|NO|`not`|

```{caution}
Se debe de respetar la primer letra en mayúscula en `False` y `True`
```

**Ejemplo:**

|X|Y|X and Y|X or Y|not X|
|:---:|:---:|:---:|:---:|:---:|
|`True`|`True`|`True`|`True`|`False`|
|`True`|`False`|`False`|`True`|`False`|
|`False`|`True`|`False`|`True`|`True`|
|`False`|`False`|`False`|`False`|`True`|

<br>

(built-in-operadores-identidad)=
## Identidad

Palabras reservadas para verificar que dos objetos sean los mismos (hagan referencia al mismo objeto). Retorna un objeto `bool`.

|Nombre|Palabra|
|:----------|:----------:|
|Es |`is`|
|No es|`not is`|

Un uso especial de este operador es para verificar que una variable o objeto sea un valor nulo:

```python
# Verificar que variable sea un valor nulo
x is None

# Verificar que variable no sea un valor nulo
x not is None
```

:::{warning}
No se debe de usar el operador de igual (`==`) para verificar que una valor sea un valor nulo.
:::

<br>

(built-in-operadores-membresia)=
## Membresía

Palabras reservadas para verificar que un elemento esté dentro de una secuencia. Retornan un objeto `bool`.

|Nombre|Palabra|
|:----------|:----------:|
|En |`in`|
|No en|`not in`|

<br>

## Operadores * y **

En esta parte se explica el uso de `*` y `**` para desempacar secuencias y diccionarios como argumentos de funciones. Para información más completa sobre estos operadores visitar [este artículo](https://treyhunner.com/2018/10/asterisks-in-python-what-they-are-and-how-to-use-them/) de Trey Hunner.

Si se usa `*` como prefijo de una `secuencia` al llamar una función equivale a poner los elementos de la secuencia como argumentos de la función. Por ejemplo:
```python
# Definir la secuencia
x = ['a','b','c']

# Desempacar la secuencia usando "*"
print(*x) # Equivale a: print('a', 'b', 'c')
```

Si se usa `**` como prefijo de un `dict` al llamar una función equivale a poner los `key=value` del diccionario como argumentos con nombre de la función. Por ejemplo:
```python
# Definir el diccionario
x = {'key1': 'value1', 'key2': 'value2'}

# Desempacar el diccionario
function(**x) # Equivale a: function(key1=value1, key2=value2)
```

```{caution}
Notar que los _keys_ del diccionario serán los nombres de los parámetros en la función.
```

### Otros usos:

Otros usos del operador `*` incluye:
- Al usar `*` al definir los parámetros de una función implica que todos los parámetros definidos después de `*` se deben de definir por _keyword_. Ver {ref}`func-parametros`.

<br>

---
(keywords)=
## Palabras reservadas

Son palabras que tienen un significado especial para python.

|Palabra|Significado|
|:----------|:----------|
|`as`|Crear un alias|
|`assert`|Verifica si una expresión booleana es verdadera o falsa. Si es falsa devuelve un error. Si es verdadera, no retorna nada. Revisar [](keyword-assert)|
|`async`|Definir una función asincrónica|
|`await`|En funciones asincrónicas para retornar el control al bucle de eventos|
|`break`|Salir de un cíclo|
|`class`|Definir una clase|
|`continue`|Continuar a la siguiente iteración de un cíclo|
|`def`|Definir una función|
|`del`|Eliminar un objeto|
|`from`|Impotar partes específicas de un módulo|
|`global`|Declarar una variable en el scope global|
|`import`|Importar un módulo|
|`lambda`|Crear una función lambda|
|`nonlocal`|Declarar una variable de manera no local|
|`pass`|Una setencia que no hace nada|
|`raise`|Arrojar una excepción|
|`return`|Retornar una valor en una función|
|`with`|Administrador de contextos|
|`yield`|Terminar una función. Retorna un generator|

:::{caution}
En la lista anterior no se incluyeron las siguientes _keywords_:
- Operadores lógicos: `and`, `or`, y `not`.
- Operadores de membresía e indentidad: `is` y `in`.
- Valores booleanos: `True` y `False`.
- Otras constantes: `None`.
- Estructuras lógicas: `if`, `else` y `elif`.
- Estructuras cíclicas: `for` y `while`.
- Estructura para manejo de error: `try`, `except`, `finally`.
:::

<br>

(keyword-assert)=
### Assert

Verifica si una condición es `True` o `False`. Si es `False` retorna un error de tipo `AssertionError`. Si es `True`, no retorna nada, es decir, retorna `None`.

Cuando se utiliza `assert`, se puede agregar un mensaje en caso de que la condición sea `False`:
```python
assert expression, message
```
- `expression`: Cualquier expresión que retorne `bool`. 
- `message` \- `str`: Cualquier mensaje que se quiera retornar en caso de que `expression` sea `False`.

<br>

---
## Jerarquía de operadores

A continuación se presenta la jerarquía de operadores, es decir, los operadores que se ejecutarán primero en el código. Esta tabla está basada en la [esta tabla](https://www.programiz.com/python-programming/precedence-associativity) de programiz.com.

|Jerarquía|Operadores|
|:----------:|:----------:|
|1|`()`|
|2|`**`|
|3|`~x`, `+x`, `-x`|	
|4|`*`, `/`, `//`, `%`|
|5|`+`, `-`|
|6|`&`|	
|7|`^`|	
|8|`\|`|	
|9|`==`, `!=`, `>`, `>=`, `<`, `<=`, `is`, `is not`, `in`, `not in`|
|10|`not`|
|11|`and`|
|12|`or`|













