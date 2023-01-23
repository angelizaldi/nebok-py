# If ... Else.

Se utiliza usando las palabras reservada `if` y `else`:
```python
# Plantilla básica de un if else
if condition:
    expression_true
else:
    expression_false
```
- _condition_ es una expresión que retorne `True` o `False`. Es posible poner un objeto y por default se evaluará ese objeto con la función `bool()`.
- Si _condition_ es `True` entonces se ejecutará _expression_true_, si es `False`, se ejecutará _expression_false_.
- No estrictamente necesita un `else`, se puede poner solo el `if`. En ese caso solo se ejecutará el código si se cumple la condición.

```{warning} Es muy importante que se respete la indentación, esa es la forma como Python determina qué parte del código forma parte de cada bloque de la estructura. Los dos puntos indican el inicio de un bloque que debe de estar indentado.
```

Se pueden verificar varias condiciones con la palabra reservada `elif`:
```python
# Platila básica de un if elif else
if condition_1:
    expression_1
elif condition_2:
    expression_2
else:
    expression_3
```
- Se pueden poner tantos `elif` como sean necesarios.

---
## Versión simplificada:

También conocida como "_ternary operators_" o "_conditional expressions_", son una forma de escribir una estructura `if else` en una sola línea. Es útil cuando se quiere evaluar una expresión, existen dos versiones principales:
```python
# Version 1:
if condition: expression_true

# Version 2:
expression_true if condition else expression_false
```
- Es posible anidar otros `if` o `if else`.

Existe otra versionas con tuples y diccionarios:
```python
# Tuple
(expression_false, expression_true)[condition]

# Diccionario
{True: expression_false, False: expression_true}[condition]
```
- En la versión de tupla, basicamente es un `tuple` con dos elementos y se hace _subsetting_, con base a una comparación lógica, de manera que si es falsa se elija el elemento con índice cero y si es cierta, se elige el elemento con índice uno. Lo mismo se podría hacer con una lista.
- En diccionario, es similar, pero en lugar de hacer subsetting por índice, lo hace por el nombre de la _key_.

---
## Operadores logicos.

Se puede utilizar los operadores `and`, `or` y `not` en las condiciones de las estructuras `if else`:
- `and`: Se usa para verificar que dos o más condiciones sean `True`. Si al menos una es `False` entonces toda la expresión será `False`.
- `or`: Se usa para verificar que al menos una condición sea `True`. Para que la expresión retorne `False`, todas las condiciones tienen que ser `False`.
- `not`: Se usa para invertir el resultado de la expresión, de manera que convierte `True` en `False` y viceversa.

---
## Pass
Las estructuras `if else` no pueden estar vacías, pero por si alguna razón se necesita una estructura `if ... else` vacía se puede usar la sentencia `pass` para evitar errores:
```python
# Una estructura if vacía
if condicion:
    pass
```