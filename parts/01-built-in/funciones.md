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
# Plantilla de una función
def function_name(param1=val1, param2=val2, ...):
    """docstring"""
    body
    return value
```
- _function_name_ es el nombre de la función.
- _"""docstring"""_ es opcional, pero se recomienda ponerlo, sirve para describir qué hace la función, describir los parámetros, describir el objeto retornado, describir los errores arrojados (si hay) y notas extras o ejemplos de uso. Consultar {ref}`docstrings`.
- _param1_, _param2_, etc. son los parámetros de la función. Definir los parámetros es opcional. El nombre de los parámetros (_keywords_) son los que se usarán dentro de la función y también se pueden usar al momento de llamar la función. Consultar {ref}`parametros`.
- _val1_, _val2_, etc. son los valores por default correspondientes a los parámetros _param1_, _param2_, etc. Darle valores por default a los parámetros es opcional.
- Retornar un valor es opcional. Consultar {ref}`retornar`.

También es posible declarar el tipo de dato de cada parámetro y el tipo de dato del valor que retorna la función, usando dos puntos y el nombre del tipo de dato (`str`, `int`, etc.), para cada parámetro y `->` para la función:
```python
# Plantilla definiendo los tipos de datos de los
# parámetros y el valor retornado
def function_name(param1=val1: dtype, ...) -> dtype:
    """docstring"""
    body
    return value
```
- _dtype_ es el nombre del tipo de objeto.

```{warning} Es muy importante que se respete la indentación, esa es la forma como Python determina qué parte del código forma parte de cada bloque de la estructura. Los dos puntos indican el inicio de un bloque que debe de estar indentado.
```

Recomendaciones generales de funciones:
1. Se recomiendan que las funciones solo realicen una acción.
2. No usar objetos mutables como parámetros por default.

### Versión simplificada

Existe una versión simplificada de una sola línea, útil para funciones que solo retornan una expresión. La sintaxis es:
```python
# Versión simple de una función
def my_function(params): return expression
```

---
## Funciones Lambda

Son funciones anónimas (no tiene nombre). Se suelen usar como argumento de funciones que reciben funciones como parámetros. Algunas caracterísicas de las funciones lambda son:
- Puede tomar cualquier número de parámetros pero solo retornar una expresión.
- Se retorna la expresión evaluada.

```python
# Función lambda
lambda params: expression
```
- _params_ son los parámetros, si son más de uno simplemente separar con coma.
- en _params_ también se puede usar `*args` y `**kwargs` (ver {ref}`params-arb`).

Se puede asignar la función a una variable (ya no sería anónima), en este caso la variable se podrá usar como la función:
```python
# Asignar a X una función lambda
X = lambda params: expression

# Se puede llamar a esta función de la siguiente manera:
X(params)

# Declarar la función así equivaldría a:
def X(params): return expression
```

---
(docstrings)=
## Docstrings

Los docstrings son una cadena al inicio de una función que incluye información sobre la función. Entre la información que suele incluir incluir es:
- Describir qué hace la función.
- Describir los parámetros.
- Describir el objeto retornado.
- Describir los errores arrojados.
- Notas.
- Ejemplos de uso.

### Estilo Numpy

El formato general para una descripción siguiendo el estilo numpy es:

```
"""
Descripción de la función

Parameters:
arg_1: dtype de param1, \[optional\]
    Descripción del parámetro, se agrega _optional_ si es un parámetro opcional.
arg_2: dtype de param2, \[optional\]
    Descripción del parámetro, se agrega _optional_ si es un parámetro opcional.
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
(parametros)=
## Parámetros

En Python al llamar una función sus parámetros pueden ser definidos usando su nombre (_keyword_) o su posición. Si no se utilizan los _keywords_ al llamar la función, el orden como se ingresen los parámetros debe de ser el mismo que en la forma como se definió la función. Si se utilizan los _keywords_ entonces se pueden poner en cualquier orden.

Por ejemplo:
```python
# Si una función se definió como:
def my_function(param1, param2, param3):
    body

# Definir los argumentos por posición, implica que:
my_function(val1, val2, val3)

# Equivale a:
my_function(param1=val1, param2=val2, param3=val3)
```

Los parámetros se pueden definir en un orden distinto si se usan los _keywords_:
```python
# Llamar a un función por keywords
my_function(param3=val3, param1=val1, param2=val2)
```

Es posible hacer que los parámetros solo se puedan definir por keywords usando un `*`:
```python
# Todos los parametros despues de * deben ser keywords
def my_function(params, *, keyword_params, ...):
    ...
```
- En este caso todos los parámetros antes del `* `se pueden definir por _keyword_ o por posición, pero todos los parámetros después del `*` se deben definir por _keyword_.
- El `*` se puede poner en cualquier parte, incluso al principio.

---
(params-arb)=
### Parámetros arbitrarios

#### Posicionales

Si no se sabe cuántos parámetros posicionales serán necesarios pasar a la función, se puede usar `*args` al momento de definir la función, de esta forma la función recibe un `tuple` de parámetros y se accede a ellos de la misma manera como se accede a los tuples:
```python
def my_function(*args, keyword1=val1, ...):
```
- `args` es un nombre arbitario del parámetro, ese nombre se usará dentro de la función. Será un `tuple` dentro de la función.
- Cada argumento se separa con una coma y deben de ser todos del mismo tipo de dato.
- Se pueden especificar además otros parámetros con nombres.
- Todos los parámetros posteriores a `*args` deben ser _keywords_.

:::{warning} Si los parámetro por _keyword_ no tienen valores por default, al llamar a la función se tiene que definir por keywords y no por posición, porque si no se indica el nombre se supondrá que forma parte de `*args`.
:::

<br>

**Ejemplo**: A continuación se define una función que recibe un número arbitrario de números y un valor inicial y calcula la multiplicación del valor inicial y todos los números recibidos.
```python
# Definir la función
def producto(*numeros, inicial=1):
    total = inicial
    for n in numeros:
        total *= n
    return total

# Llamando la función
print(producto(4, 4))

# Llamando la función indicando el paramtro por keyword
producto(4, 5, 2, inicial=3)
```
- En el ejemplo anterior si no se indicará `inicial=3` y solo se pusiera el 3, entonces el 3 formaría parte de `*numeros`.

---
#### Keywords

Si no se sabe cuántos _keywords_ necesita la función se puede usar `**kwargs` al momento de definir la función. De esta manera se pasará un `dict` a la función con los keywords y sus respectivos valores, dentro de la función se accederá a ellos con el nombre haciendo subsetting del diccionario.

```python
def my_function(**kwargs):
    ...
```
- `kwargs` es un nombre arbitrario del parámetro, se recomienda usar ese tal cual, ese nombre se usará dentro de la función. Será un diccionario dentro de la función.
- Al momento de llamar la función se tienen que pasar las _keywords_ y sus valores en pares `keyword=value`.
```python
# AL llamar una función con **kwargs usar keyword=value
my_function(keyword1=val1, ...)

# Si X es dict se puede usar ** paraa desempacar los `key-value`
# Definir un diccionario
X = {"keyword1": val1, ...}

# Desempacar los keyword-value en la función
my_function(**X) # Equivale a my_function(keyword1=val1, ...)
```

<br>

**Ejemplo**: A continuación se define una función que recibe una cantidad arbitraria de `key-value` y concatena los resultados, separados por coma y un espacio.
```{code-cell} ipython3
# Definir la función
def atributos(**attributes):
    """Returna una cadena con los pares key-value separados por coma."""
    return ", ".join(f"{param}: {value}" for param, value in attributes.items())

# Llamando la función por keyword=value
print(atributos(nombre="Juan", edad=20, sexo="Hombre"))

# Llamar con un diccionario.
items = {"nombre": "Juan", "edad": 20, "sexo": "Hombre"}
print(atributos(**items))
```

---
(retornar)=
## Retornar valores

Para que la función retorne un valor es necesario usar la palabra reservada `return`:
```python
def function_name(param1, param2, ...):
    body
    return value
```
- `return` es la última línea que se ejecutará en el código, una vez aparezca un `return` el resto de la función (en caso de que exista) ya no se ejecutará.
- Si se quiere retornar más de un valor se recomienda que estén dentro de un `tuple`. Recordar que para crear un tuple, basta con separar los elementos con coma, no es necesario usar los paréntesis, es decir, `return a, b, c == return (a, b, c)`.
- También es posible retornar un `dict` en lugar de un `tuple`.
- Si una función no retorna ningún valor, implícitamente retornará `None`.
- Se puede retornar toda clase de objetos, incluyendo otras funciones. Si se retorna una función y se asigna a un objeto entonces ese objeto funcionará como la función que se retornó, ejemplo:
```{code-cell} ipython3
# Definir una función que retorna print con sep="\n"
def print2(*args):
    return print(*args, sep="\n")

# Asignar la función a X
X = print2

# Ahora X funcionará como un print(*args, sep="\n")
X("foo", "bar")
```

---
## Sentencia Pass

Una función no puede estar vacía. Si por alguna razón se necesita que una función esté vacía, se tiene que usar la palabra reservada `pass`, para evitar un error.
```python
def my_function():
    pass
```

---
## Llamar a una función

Para llamar a un función simplemente se usa su nombre y entre paréntesis los valores de los parámetros (en caso de que existan).
```python
# Llamar a la función "function_name"
function_name(val1, val2, ...)
```
- Si la función no tiene parámetros no poner nada dentro de los paréntesis.
- Se debe de pasar la misma cantidad de parámetros que aquellos que la función espera (parámetros obligatorios),  y en el mismo orden que en la manera como están definidos en la función en caso de que se no se usen los keywords, en caso contrario se pueden poner en un orden distinto.
```python
# Llamar a una funcion por keywords
function_name(param2=val2, param1=val1, ...)
```

También se pueden asignar a otra variable, sin usar los paréntesis y posteriormente usar esta variable como si fuera la función original:
```python
# Asignar una función a una variable
X = function_name

# Usar la variable como función
X(param1=val1, param2=val2, ...)
```

También se pueden crear listas y diccionarios de funciones y llamarles por su índice o por su _key_, respectivamente:
```python
# Definir una lista de funciones
X = list(function1, function2, function3, ...)
# Llamar a una función por su índices
X[i](param1=val1, param2=val2, ...)

# Definir un diccionario de funciones
Y = {'key1': function1, 'key2': function2, ...}
# Llamar a una función por su key
Y['keyi'](param1=val1, param2=val2, ...)
```

---
## Scopes

En Python, las variables se pueden clasificar en tres categorías: variables locales, variables no locales y variables globales.

- **Variables locales**: Son aquellas que se definen dentro de una función o método y solo están disponibles dentro de ese ambiente (_scope_). Una vez que la función o método ha terminado de ejecutarse, estas variables ya no están disponibles.
- **Variables no locales**: Son aquellas que se definen en el ámbito de una función o método, pero se refieren a una variable con el mismo nombre definida en el ambiente no local de esa función o método. La palabra reservada `nonlocal` se utiliza para acceder a estas variables, generalmente dentro de funciones anidadas.
- **Variables globales**: Son aquellas que se definen en el ambiente principal del script o módulo y son accesibles desde cualquier punto del script o módulo. La palabra reservada `global` se utiliza para acceder a estas variables dentro de una función o método.

**Ejemplo**:
```{code-cell} ipython3
# Una variable global
x = 15 

# Definir una función
def outer_function():
    # Una variable local
    y = 5
    # Una variable no local
    x = 5 
    # Definir una función interna
    def inner_function():
        # Acceder a la variable no local x
        nonlocal x 
        # Modifical la variable no local x
        x += y 
        print("inner:", x)
    inner_function()
    print("outer:", x)

outer_function()
print("global:", x)
```
- En este ejemplo `x = 15` es una variable global porque está definida en el ambiente global.
- `y = 5` es una variable local porque está definida dentro de una función y no se refiere a una variable con el mismo nombre en el ambiente global.
- `x = 5` es una variable no local porque está definida dentro de una función, pero se refiere a una variable con el mismo nombre en el ambiente global.
- Al usar `nonlocal x` dentro de `inner_function`, entonces `x` valdrá 5, porque se está accediendo a la variable no local `x = 5`. Por lo que básicamente ahora la variable `x` tanto en `inner_function` como en `outer_function` son la misma variable.
- Como `inner_function()` modifica el valor de la variable `nonlocal x` entonces ahora la variable no local `x` vale 10, en lugar de 5. El valor de la variable global no cambia porque no se accedió a ella y por lo tanto no se modificó.
- Notar que si en lugar de usar `nonlocal x` se usará `global x` dentro de `inner_function`, entonces `x` valdría 15 en `inner_function` y en el ambien global, pero no en `outerfunction`, porque se estaría accediendo a la variable global `x = 15` y después de la modificación tanto "inner x" como "global x" valdrían 20, pero "outer x" seguiría valiendo 5.


---
## Recursión

La recursión sucede cuando dentró de una función, la función se llama a sí misma. Se debe de tener cuidado de que la función termine en algún momento y de que no se consuma demasiada memoria para procesarla.
```python
def my_function(...):
    body
        
    my_function(...)
        
    body
```

```{caution} 
Por default el número máximo de recursiones es de 1000.
```

**Ejemplo**: A continuación se define una función recursiva que calcula el factorial de un número entero, la función se llama a si misma siempre que $n>1$.
```{code-cell} ipython3
# Definir una función recursiva
def factorial(n):
    # Caso base: si n es igual a 0 o 1, el factorial es 1
    if n == 0 or n == 1:
        return 1
    # Caso recursivo: se llama a la función factorial con n-1 
    # y se multiplica el resultado por n
    else:
        return n * factorial(n-1)

# Probar la función
print(factorial(5))
```

---
## Obtener código de una función

Para obtener el código de una función es necesario importar el módulo `inspect`, posteriormente usar la función `getsource()`.
```python
# Importar módulo
import inspect

# Recuperar el código fuente
lines = inspect.getsource(function_name)

# Imprimir el código fuente
print(lines)
```
- Siendo _function_name_ el nombre de una función.

---
## Atributos

Las funciones son objetos de tipo `function`, por lo tanto tienen algunos atributos. A continuación se presentan algunos atributos del tipo `function`. Para más información visitar la [documentación](https://docs.python.org/3/library/inspect.html?highlight=__defaults__#types-and-members) de Python.

| Atributo    | Descripción |
| :---: | :--- |
| `__doc__` | Retorna el docstring de la función. |
| `__name__` | Retorn el nombre con el cual esta función fue definida. |
| `__defaults__` | `tuple` de cualquier valor predeterminado para los parámetros posicionales o _keywords_. |
| `__kwdefaults__` | Mapeo de cualquier valor predeterminado para los parámetros _keywords_. |
| `__module__` | Nombre del módulo en el cual esta función fue definida. |





