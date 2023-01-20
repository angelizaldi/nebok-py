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

# Funciones

Es un bloque de código que solo se ejecuta si es llamado. 
- Se puede pasar valores a la función, llamados parámetros. 
- Puede retornar valores u otras funciones.

```{note}
En Python las funciones se consideran un objeto.
```
---
## Crear una función:

La sintaxis para crear una función es la siguiente:
```python
def function_name(arg1=val1, arg2=val2, ...):
    """docstring"""
    expression
    return value
```
- _function_name_ es el nombre de la función.
- _"""docstring"""_ es opcional, pero se recomienda ponerlo, sirve para describir qué hace la función, describir los argumentos, describir el objeto retornado, describir los errores arrojados (si hay) y notas extras o ejemplos de uso (todo en ese orden).
- Definir los argumentos es opcional, el nombre de los argumentos (_keywords_) son los que se usarán dentro de la función y también se pueden usar al momento de llamar la función.
- Darle valores por default a los argumentos es opcional.
- Retornar un valor es opcional.
- También se puede declarar el tipo de dato de cada argumento y el tipo de dato del valor que retorna la función, usando dos puntos y el nombre del tipo de dato (`str`, `int`, etc.), para cada argumento y `->` para la función:
```python
def function_name(arg1=val1: dtype, ...) -> dtype:
    """docstring"""
    expression
    return value
```
- _dtype_ es el nombre del tipo de objeto.

```{warning} Es muy importante que se respete la indentación, esa es la forma como Python determina qué parte del código forma parte de cada bloque de la estructura. Los dos puntos indican el inicio de un bloque que debe de estar indentado.
```

Recomendaciones generales de funciones:
1. Se recomiendan que las funciones solo realicen una acción.
2. No usar objetos mutables como argumentos por default.

### Versión simplificada

Existe una versión simplificada de una sola línea, útil para funciones que solo retornan una expresión. La sintaxis es:
```python
def my_function(args): return expression
```

---
## Funciones Lambda

- Es una función anónima pequeña. 
- Puede tomar cualquier número de argumentos pero solo retornar una expresión.
- Se retorna la expresión evaluada.
- Se usan cuando se requiere una función anónima por un pequeño momento, por ejemplo, definir una función dentro de otra función.
```python
lambda args: expression
```
- _args_ son los parámetros, si son más de uno simplemente separar con coma.
- en _args_ también puedes poner `*args` y `**kwargs`.

La función se le puede asignar a una variable (ya no sería anónima), en ese caso la variable tomará el valor resultante en _expression_:
```python
X = lambda args: expression

# Se puede llamar a esta función de la siguiente manera:
X(args)

# Declarar la función así equivaldría a:
def X(args): return expression
```

---
## Docstrings

Estilo Numpy.
El formato general para una descripción siguiendo el estilo numpy es:

```
"""
Descripción de la función

Parameters:
arg_1: dtype de arg1, \[optional\]
    Descripción del argumento, se agrega _optional_ si es un argumento opcional.
arg_2: dtype de arg_2, \[optional\]
    Descripción del argumento, se agrega _optional_ si es un argumento opcional.
...

Returns:
dtype del tipo de objeto retornado
    descripción del objeto retornado
"""
```

```{tip} Para recuperar el docstring de una función usar cualquiera de los siguientes métodos:
- Usar el atributo `.__doc__` de la función.
- Usar la función `inspect.getdoc()` del módulo `inspect` (es necesario importarlo).
```

---
## Argumentos.

En Python al llamar o definir una función sus argumentos pueden ser definidos usando su nombre o su posición. Si no se utilizan los _keywords_ al llamar la función, el orden como se ingresen los argumentos debe de ser el mismo que en la forma como se definió la función. Si se utilizan los _keywords_ entonces se pueden poner en cualquier orden

Por ejemplo, si una función se definió como:
```python
def my_function(arg1, arg2, arg3):
    ...
```
Entonces definir los argumentos por posición, implica que:
```python
my_function(val1, val2, val3)
```
Equivale a:
```python
my_function(arg1=val1, arg2=val2, arg3=val3)
```

Los argumentos se pueden definir en un orden distinto si se usan los _keywords_:
```python
my_function(argi=vali, argj=valj, argk=valk)
```

Es posible hacer que los argumentos solo se puedan definir por keywords usando:
```python
def my_function(args, *, keyword_args, ...):
    ...
```
- En este caso todos los argumentos antes del `* `se pueden definir por _keyword_ o por posición, pero todos los argumentos después del `*` se deben definir por _keyword_.
- El asterístico se puede poner en cualquier parte, incluso al principio.

---
## Argumentos arbitrarios:

### Posicionales:

Si no se sabe cuántos argumentos posicionales serán necesarios pasar a la función, se puede usar `*args` al momento de definir la función, de esta forma la función recibe un `tuple` de argumentos y se accede a ellos de la misma manera como se accede a los tuples:
```python
def my_function(*args, keyword1=val1, ...):
```
- `args` es el nombre del parámetro, ese nombre se usará dentro de la función. Será un `tuple` dentro de la función.
- Los argumentos en el `tuple` deben de ser todos del mismo tipo de dato.
- Se pueden especificar además otros argumentos con nombres.
- Todos los argumentos posteriores a `*args` deben ser _keywords_.

```{warning} Si los argumento por _keyword_ no tienen valores por default, al llamar a la función se tiene que definir por keywords y no por posición, porque si no se indica el nombre se supondrá que forma parte de `*args`.
```

Ejemplo:
<code> python
def product(*numbers, initial=1):
    total = initial
    for n in numbers:
        total *= n
    return total

#Llamando la función
product(4, 4)
product(4, 5, 2, initial=3)
</code>

---
### Keywords

Si no se sabe cuántos _keywords_ necesita la función se puede usar `**kwargs` al momento de definir la función. De esta manera se pasará un `dict` a la función con los keywords y sus respectivos valores, dentro de la función se accederá a ellos con el nombre haciendo subsetting del diccionario.
```python
def my_function(**kwargs):
    ...
```
- `kwargs` es el nombre del parámetro, se recomienda usar ese tal cual, ese nombre se usará dentro de la función. Será un diccionario dentro de la función.
- Al momento de llamar la función se tienen que pasar las _keywords_ y sus valores en pares `keyword=value`:
```python
my_function(keyword1=val1, ...)
```
- También es posible pasar directamente un diccionario y usar `**` paraa desempacar los `key-value`:
```python
my_function(dict**)
```

Ejemplo
```{code-cell} ipython3
def atributos(**attributes):
    """Returna una cadena con los pares key-value separados por coma."""
    return ", ".join(f"{param}: {value}" for param, value in attributes.items())

# Llamando por keywords
print(atributos(nombre="Juan", edad=20, sexo="Hombre"))

# Llamar con un diccionario.
items = {"nombre": "Juan", "edad": 20, "sexo": "Hombre"}
print(atributos(**items))
```

---
## Retornar valores:

Para que la función retorne un valor es necesario usar la palabra reservada return:
```python
def function_name(arg1, args2, ...):
    expression
    return value
```
- `return` es la última línea que se ejecutará en el código, una vez aparezca un `return` el resto de la función (en caso de que exista) ya no se ejecutará.
- Si se quiere retornar más de un valor se recomienda que estén dentro de un `tuple`. Recordar que para crear un tuple, basta con separar los elementos con coma, no es necesario usar los paréntesis o el constructor, es deicr `return a, b, c == return (a, b, c)`.
- También es posible retornar un `dic` en lugar de un`tuple`.
- Si una función no retorna ningún valor, implícitamente retornará `None`.
- Se puede retornar toda clase de objetos, incluyendo otras funciones. Si se retorna una función sin los paréntesis y se asigna a un objeto entonces ese objeto funcionará como la función que se retornó, ejemplo:
```{code-cell} ipython3
def print2(*args):
    return print(*args, sep="\n")

X = print2

# Ahora X funcionará como un print(sep="\n")
X("foo", "bar")
```

---
## Sentencia Pass:

Una función no puede estar vacía. Si por alguna razón se necesita que una función esté vacía, se tiene que usar la palabra reservada `pass`, para evitar un error.
```python
def my_function():
    pass
```

---
## Llamar a una función:

Para llamar a un función simplemente se usa su nombre y entre paréntesis los valores de los parámetros (en caso de que existan).
```python
function_name(val1, val2, ...)
```
- Si la función no tiene argumentos no poner nada dentro de los paréntesis.
- Se debe de pasar la misma cantidad de argumentos que aquellos que la función espera (argumentos obligatorios),  y en el mismo orden que en la manera como están definidos en la función en caso de que se no se usen los keywords, en caso contrario se pueden poner en un orden distinto.
```python
function_name(arg2=val2, arg1=val1, ...)
```

También se pueden asignar a otra variable, sin usar los paréntesis y posteriormente usar esta variable como si fuera la función original:
```python
X = function_name
X(arg1=val1, arg2=val2, ...)
```

También se pueden crear listas y diccionarios de funciones y llamarles por su índice o por su _key_, respectivamente:
```python
X = list(function1, function2, function3, ...)
X[i](arg1=val1, arg2=val2, ...)

Y = {'key1': function1, 'key2': function2, ...}
Y['keyi'](arg1=val1, arg2=val2, ...)
```

---
## Recursión
La recursión sucede cuando dentró de una función, la función se llama a sí misma. Se debe de tener cuidado de que la función termine en algún momento y de que no se consuma demasiada memoria para procesarla.
```python
def my_function(...):
    expression
        
    my_function(...)
        
    expression
```

```{caution} 
Por default el número máximo de recursiones es de 1000.
```

---
## Obtener código de una función.

Para obtener el código de una función es necesario importar el módulo `inspect`, posteriormente usar la función `getsource()`.
```python
import inspect
lines = inspect.getsource(function_name)
print(lines)
```
- Siendo _function_name_ el nombre de una función.

---
## Atributos
Atributos del objeto tipo `function`.

---
**__doc__**:

`function.__doc__()`: Retorna la documentación de una función (si tiene).
```python
X.__doc__
```

**Parámetros:**
- **`X`** \- `function`: Una función: 
- No se debe de poner los paréntesis en la función: 

**Retorna:**
-  `str`.

---
**__name__**:

`function.__name__()`: El nombre de la función.
```python
	X.__name__
```

**Parámetros:**
- **`X`** \- `function`: Una función: 
- No se debe de poner los paréntesis en la función: 

**Retorna:**
-  `str`.

---
**__defaults__**:

`function.__defaults__()`: Retorna los valores de los argumentos por default de la función.
```python
	X.__defaults__
```

**Parámetros:**
- **`X`** \- `function`: Una función: 
- No se debe de poner los paréntesis en la función: 

**Retorna:**
-  `str`.





