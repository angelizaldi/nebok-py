# Excepciones

Una excepción es un evento que ocurre durante la ejecución de un programa y que interrumpe la ejecución del programa. Las excepciones indican que se generó un error que se puede manejar, en comparación con errores que no se pueden manejar como los errores de sintaxis (`SyntaxError`) o de identación (`IndentationError`).

Cuando ocurre una excepción, Python genera un objeto de excepción que contiene información sobre el error. Si no se maneja correctamente, el programa se detiene y se muestra un _traceback_.

Se puede probar que algún bloque del código tenga excepción, en caso de que así sea evitar que se detanga la ejecución del programa y realizar alguna acción en específico. Para ello se usan las palabras reservadas `try` y `except`.
```python
# Plantilla de try except
try:
    # try body
except [exception_type] [as my_exception_name]:
    # except body
```
- Se prueba _try body_, en caso de que suceda algún error, entonces se procederá a ejecutar _except body_, si no sucede ningún error, entonces _except body_ no se ejecutará.
- _error_type_: Es para específicar que hacer en caso de un error en específico, se pone tal cual el nombre del error. Para ver los tipos de errores revisar {ref}`excepciones-excepciones`. También se pueden poner excepciones personalizadas. Es posible poner más de un tipo de error dentro de un `tuple`.
- Es posible indicar que el error se retorne como un objeto renombrándolo con la palabra reservada `as` para poder utilizar ese objeto, como imprimir su tipo.

:::{note}
Al usar `print()` con una instancia de alguna excepción se imprimirá un representación en cadena del mensaje de error.
:::


Se pueden anidar varios `except`, para ello es necesario especificar qué hacer en cada tipo de error.
```python
# Definir un try
try:
    # try body
# Definir un except para un error en específico
except error_type_1 [as my_exception_name]:
    # error type 1 body
# Se pueden definir múltiples excepts para varios tipos de errores
...
# Definir un except general para el resto de los errores
except:
    # any other error body
```
- En este caso solo se ejecutará _error type 1 body_ si ocurre un error de tipo _error_type_1_.
- Se puede especificar un bloque como el anterior múltiples veces para diferentes errores.
- Se puede indicar un bloque general para todos lo demás errores.

<br/>

---
## Sentencias Else y Finally

Existen otras sentencias que se pueden usar junto con `try` y `except`:

- `Else`: Se usa para definir un bloque de código que se ejecute en caso de que **no** ocurra un error (además del que se está probando con `try`).
```python
# Uso de else
try:
    expression
except:
    expression_error
else:
    expression_else
```
<br>

- `Finally`: Se ejecuta un bloque del código independientemente de si ocurrió un error o no, es decir siempre se ejecutará este bloque de código.
```python
# Uso de finally
try:
    expression
except:
    expression_error
finally:
    expression_finally
```

<br/>

---
## Arrojar un error

Se puede arrojar un error (_exception_) en caso de que se cumpla alguna condición, para ello se utiliza `raise` y `Exception()`. Tener en cuenta que al arrojar un error se detiene la ejecución del programa y se lanza un mensaje, a menos de que se maneje con `try` y `except`.
```python
# Plantilla general
if condition:
    raise Exception(message)
```
- _message_ \- `str`: Dentro de `Exception` se puede poner algún mensaje.
- En lugar de `Exception()` se puede poner algún error en específico, por ejemplo:
```python
# Arrojar ValueError
if condition:
    raise ValueError(message)
```
- Para ver los tipos de errores revisar {ref}`excepciones-excepciones`. También se pueden poner errores personalizados creados con clases, ver {ref}`excepciones`.

<br>

### Assert

La palabra reservada `assert` es una alternativa para arrojar una excepción, `assert` verifica si una condición es `True` o `False`. Si es `False` retorna un error de tipo `AssertionError`. Si es `True`, no retorna nada, es decir, retorna `None`.

Cuando se utiliza `assert`, se puede agregar un mensaje en caso de que la condición sea `False`:
```python
assert expression, message
```
- `expression`: Cualquier expresión que retorne `bool`. 
- `message` \- `str`: Cualquier mensaje que se quiera retornar en caso de que `expression` sea `False`.

:::{warning}
Se recomienda usar `assert` durante la etapa de desarrollo y no durante producción.
:::

<br>

---
(excepciones)=
## Crear una excepción personalizada

Es posible crear una excepción personaliza. Para ello se debe de crear una clase cuya clase padre sea `Exception`, aunque se podría usar otras excepciones como clase padre. 

Las excepciones personalizadas son útiles para personalizar el nombre de la excepción y de esta forma ser más explícitos respecto al error ocurrido cuando se muestre el _traceback_.

```python
# Definir clase
MyException(Exception):
    pass
```
- Lo más común es que la clase esté vacía.
- También es posible definir un constructor con el método `__init__()` para definir un mensaje (una propiedad heredada de `Exception`):
```
def __init__(self, message):
    self.message = message
```
- No estrictamente la clase padre tiene que ser `Exception`, puede ser cualquiera de sus subclases.

<br>

---
(excepciones-excepciones)=
## Lista de excepciones

Algunas excepciones _built-in_ en Python son:

:::{caution}
Todas las excepciones en Python se derivan de la clase `BaseException`. Para más información de esta clase como sus métodos y atributos visitar la [documentación](https://docs.python.org/3/library/exceptions.html#BaseException) de Python.
:::

:::{caution}
Tener en cuenta que algunas excepciones tienen atributos/métodos únicos para esa excepción en particular. Revisar cada excepción en la [documentación](https://docs.python.org/3/library/exceptions.html#concrete-exceptions) para más detalles.
:::

```{list-table}
:header-rows: 1

* - Excepción
  - Descripción
* - `ArithmeticError`
  - Cuando ocurre un error en cálculos numéricos.
* - `AtributeError`
  - Cuando ocurre un error en cálculos numéricos.
* - `FloatingPointError`
  - Cuando ocurre un error en cálculos de números flotantes.
* - `IndentationError`
  - Cuando la identación no es correcta.
* - `IndexError`
  - Cuando el índice de una secuencia no existe.
* - `KeyError`
  - Cuando una llave no existe en un diccionario.
* - `NameError`
  - Cuando una variable no existe.
* - `OverflowError`
  - Cuando el resultado de un cálculo numérico es muy grande.
* - `ReferenceError`
  - Cuando una referencia débil de un objeto no existe.
* - `StopIteration`
  - Cuando el método `next()` de un iterator ya no tiene más valores.
* - `SyntaxError`
  - Cuando ocurre un error de sintaxis.
* - `TabError`
  - Cuando la identación consiste de tabulaciones o espacios.
* - `TypeError`
  - Cuando dos tipo de datos distintos son combinados.
* - `ValueError`
  - Cuando existe un valor incorrecto en un tipo de dato especificado.
* - `ZeroDivisionError`
  - Cuando el denominador de una división es cero.
```
- Para una lista jerarquizada completa visitar [la página oficial](https://docs.python.org/3/library/exceptions.html#exception-hierarchy) de Python.