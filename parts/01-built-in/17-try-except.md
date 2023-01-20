# Exceptions

Se puede probar que algún bloque del código tenga un error, en caso de que así sea realizar alguna acción en específico. Para ello se usan las palabras reservadas `Try` y `Except`. Es útil para evitar que el programa se detenga en caso de que surja un error.
```python
try:
    expression
except [error_type] [as err]:
    expression_error
```
- Se prueba `_expression_`, en caso de que suceda algun error, entonces se procederá a ejecutar `_expression_error_`, si no sucede ningún error, entonces `_expression_error_` no se ejecutará.
- `_error_type_`: Es para específicar que hacer en caso de un error en específico, se pone el nombre tal cual el nombre del error. Para ver los tipos de errores checar la sección de Exceptions, también se pueden poner excepciones personalizadas. Es posible poner más de un tipo de error dentro de un `tuple`.
- Es posible indicar que el error se retorne como un objeto para poder utilizar ese objeto como imprimir su tipo.


Se pueden anidar varios except, para ello es necesario especificar qué hacer en cada tipo de error.
```python
try:
    expression
except error_type_1:
    expression_error_type_1
    ...
except:
    expression_error
```
- En este caso solo se ejecutará `_expression_error_type_1_` si ocurre un error de tipo `_error_type_1_`.
- Se puede especificar un bloque como el anterior múltiples veces para diferentes errores.
- Se puede indicar un bloque general para todos lo demás errores.

## Sentencias Else y Finally:

Existen otras sentencias que se pueden usar junto con try y except:
- `Else`: Se usa para definir un bloque de código que se ejecute en caso de que **no** ocurra un error (además del que se está probando con `try`).
```python
try:
    expression
except:
    expression_error
else:
    expression_else
```

- `Finally`: Se ejecuta un bloque del código independientemente de si ocurrió un error o no, es decir siempre se ejecutará este bloque de código.
```python
try:
    expression
except:
    expression_error
finally:
    expression_finally
```

## Arrojar un error:

Se puede arrojar un error en caso de que se cumpla alguna condición, para ello se utiliza `raise` y `Exception()`. Tener en cuentea que al arrojar un error se detiene la ejecución del programa y se lanza un mensaje.
```python
if condition:
    raise Exception(message)
```
- `_message_` \- `str`: Dentro de `Exception` se puede poner algún mensaje.
- En lugar de `Exception()` se puede poner algún error en específico, por ejemplo:
```python
if condition:
	raise ValueError(message)
```
- Para ver los tipos de errores checar la seccion de Exceptions. También se pueden poner error personalizados creados con clases.

## Lista de excepciones

Algunas excepciones built-in en python son:

```{list-table}
:header-rows: 1
:name: label-to-reference

* - Excepción.
  - Descripción.
* - `ArithmeticError`.
  - Cuando ocurre un error en cálculos numéricos.
* - `FloatingPointError`.
  - Cuando ocurre un error en cálculos de números flotantes.
* - `IndentationError`.
  - Cuando la identación no es correcta.
* - `IndexError`.
  - Cuando el índice de una secuencia no existe.
* - `KeyError`.
  - Cuando una llave no existe en un diccionario.
* - `NameError`.
  - Cuando una variable no existe.
* - `OverflowError`.
  - Cuando el resultado de un cálculo numérico es muy grande.
* - `ReferenceError`.
  - Cuando una referencia débil de un objeto no existe.
* - `StopIteration`.
  - Cuando el método `next()` de un iterator ya no tiene más valores.
* - `SyntaxError`.
  - Cuando ocurre un error de sintaxis.
* - `TabError`.
  - Cuando la identación consiste de tabulaciones o espacios.
* - `SystemError`.
  - Cuando ocurre un error en el Sistema.
* - `TypeError`.
  - Cuando dos tipo de datos distintos son combinados.
* - `ValueError`.
  - Cuando existe un valor incorrecto en un tipo de dato especificado.
* - `ZeroDivisionError`.
  - Cuando el denominador de una división es cero.
```
- Para una lista completa visitar [la página oficial](https://docs.python.org/3.10/library/exceptions.html#exception-hierarchy) de Python.