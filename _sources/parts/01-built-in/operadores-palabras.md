# Operadores y palabras reservadas.

## Aritméticos:
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

<br>

---
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

<br>

---
## Asignación
Operaciones para asignación de valores.

|Nombre|Operador|
|:----------|:----------:|
|Asignación|`=`|
|Asignación recursivo aritmético|`+=`, `-=`, `*=`, `/=`, `**=`, `%=`, `//=`|
|Asignación recursivo lógico|`\|=`, `&=`|

<br>

---
(operadores:bitwise)=
## Bitwise
|Nombre|Operador|
|:----------|:----------:|
|Y|`&`|
|O|`\|`|
|NO|`~`|
|O excluyente (XOR)|`^`|

Existen otros como `<<` y `>>`.

**Ejemplo**

|X|Y|X&Y|X\|Y|~X|X^Y|
|:---:|:---:|:---:|:---:|:---:|:---:|
|1|1|1|1|0|0|
|1|0|0|1|0|1|
|0|1|0|1|1|1|
|0|0|0|0|1|0|

<br>

---
## Bool

Palabras reservadas para trabajar con valores booleanos y manipulaciones entre ellos.
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

<br>

---
## Identidad

Palabras reservadas para verificar que dos objetos sean los mismos (hagan referencia al mismo objeto). Retorna un objeto `bool`.

|Nombre|Palabra|
|:----------|:----------:|
|Es |`is`|
|No es|`not is`|

<br>

---
## Membresía

Palabras reservadas para verificar que un elemento esté dentro de una secuencia. Retorna un objeto `bool`.

|Nombre|Palabra|
|:----------|:----------:|
|En |`in`|
|No en|`not in`|

<br>

---
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

<br>

---
## Palabras reservadas

Son palabras que tienen un significado especial para python.

|Palabra|Significado|
|:----------|:----------|
|`as`|Crear un alias|
|`assert`|Verifica si una expresión booleana es verdadera o falsa. Si es falsa devuelve un error. Si es verdadera, no retorna nada. Revisar [](uso-assert)|
|`break`|Salir de un cíclo|
|`continue`|Continuar a la siguiente iteración de un cíclo|
|`def`|Definir una función|
|`global`|Declarar una variable en el scope global|
|`del`|Eliminar un objeto|
|`from`|Impotar partes específicas de un módulo|
|`import`|Importar un módulo|
|`lambda`|Crear una función lambda|
|`None`|Representa una ausencia de valor o un valor nulo|
|`nonlocal`|Declarar una variable de manera no local|
|`pass`|Una setencia que no hace nada|
|`return`|Retornar una valor en una función|
|`with`|Administrador de contextos|
|`yield`|Terminar una función. Retorna un generator|

<br>

---
(uso-assert)=
### Uso de assert

Verifica si una expresión booleana es `True` o `False`. Si es `False` retorna un error de tipo `AssertionError`. Si es `True`, no retorna nada, es decir, retorna `None`.

Cuando se utiliza `assert`, se puede agregar un mensaje en caso de que haya un error:
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













