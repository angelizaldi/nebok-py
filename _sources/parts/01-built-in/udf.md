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

# Funciones (UDF)

Las funciones definidas por el usuario o _UDF_, por sus siglas en inglés, son un bloque de código que se ejecuta solo si es llamado, para fines prácticos en esta sección simplemente se le llamarán funciones. Algunas características de las funciones son:
- Son objetos.
- Se puede pasar valores a la función, llamados argumentos, incluidas otras funciones. 
- Puede retornar otros objetos, incluidas otras funciones.
- Se pueden asignar a variables

```{note}
En Python las funciones se consideran un objeto.
```

<br/>

---
## Crear una función

La sintaxis para crear una función es la siguiente:
```python
# Plantilla básica de una función
def function_name(param1=val1, param2=val2, [...]):
    """docstring"""
    # function body
    [return expression]



# Plantilla definiendo los tipos de datos de los
# parámetros y el valor retornado
def function_name(param1=val1: dtype, [...]) -> dtype:
    """docstring"""
    # function body
    [return expression]
```
- _function_name_ es el nombre de la función. Algunas indicaciones y recomendaciones al definir el nombre son:
    - Solo debe de contener caracteres alfanuméricos (a-z, A-Z, 0-9) y guiones bajos (_).
    - No puede iniciar por un digito.
    - Es sensible a mayúsculas y minúsculas.
    - No debe de contener _keywords_.
    - Se recomienda que solo contenga minúsculas y separar cada palabra por guión bajo.
- _"""docstring"""_ es opcional, pero se recomienda ponerlo, sirve para describir qué hace la función, describir los parámetros, describir el objeto retornado, describir los errores arrojados (si hay) y notas extras o ejemplos de uso (en ese orden). Consultar {ref}`func-docstrings`.
- _param1_, _param2_, etc. son los parámetros de la función. Asignar valores por default a los parámetros es opcional, el nombre de los parámetros (_keywords_) son los que se usarán dentro de la función y también se pueden usar al momento de llamar la función. Consultar {ref}`func-parametros`.
- _val1_, _val2_, etc. son los valores por default correspondientes a los parámetros _param1_, _param2_, etc. Darle valores por default a los parámetros es opcional. Es altamente recomendado que los valores por default sean de tipos inmutables.
- Retornar un valor es opcional. Consultar {ref}`func-retornar`.
- También es posible declarar el tipo de dato de cada parámetro y el tipo de dato del valor que retorna la función, usando dos puntos `:` y el tipo de dato (`str`, `int`, etc.), para cada parámetro y `->` para la función.
    - _dtype_ es el nombre del tipo de objeto.

```{caution}
Para ver como definir una _función generator_ revisar {doc}`./generators`.
```

Recomendaciones generales de funciones:
1. Se recomiendan que las funciones solo realicen una acción.
2. No usar objetos mutables como parámetros por default.

```{warning} Es muy importante que se respete la indentación, esa es la forma como Python determina qué parte del código forma parte de cada bloque de la estructura. Los dos puntos indican el inicio de un bloque que debe de estar indentado.
```

<br/>

### Versión simplificada

Existe una versión simplificada de una sola línea, útil para funciones que solo retornan una expresión. La sintaxis es:
```python
# Versión simple de una función
def my_function(params): return expression
```

<br/>

---
## Funciones Lambda

Son funciones anónimas (no tienen nombre). Se suelen usar como argumento de funciones que reciben funciones como argumento. Algunas caracterísicas de las funciones lambda son:
- Puede tomar cualquier número de parámetros pero solo retornar una expresión.
- Se retorna la expresión evaluada.

```python
# Función lambda
lambda params: expression
```
- _params_ son los parámetros, si son más de uno simplemente separar con coma.
- en _params_ también se puede usar `*args` y `**kwargs` (ver {ref}`func-params-arb`).

Se puede asignar la función a una variable (ya no sería anónima), en este caso la variable se podrá usar como la función:
```python
# Asignar a X una función lambda
X = lambda params: expression

# Se puede llamar a esta función de la siguiente manera:
X(args)

# Declarar la función así equivaldría a:
def X(params): return expression
```

<br/>

---
(func-docstrings)=
## Docstrings

Los _docstrings_ son una cadena al inicio de una función que incluye información sobre la función. Entre la información que suele contener incluye:
- Describir qué hace la función.
- Describir los parámetros.
- Describir el objeto retornado.
- Describir los errores arrojados.
- Notas.
- Ejemplos de uso.

Los _docstrings_ se colocan en la línea inmediata posterior al encabezado de la función y se ponen entre triples comillas dobles o simples (`''' ... '''` o `""" ... """`).

```{tip}
Para recuperar el docstring de una función usar cualquiera de los siguientes métodos:
- Usar el atributo `.__doc__` de la función.
- Usar la función `inspect.getdoc()` del módulo `inspect` (es necesario importarlo).
```

<br/>

### Estilo Google

El formato general para una descripción siguiendo el estilo _google_ es:

```
"""
Descripción de la función

Args:
    arg_1 (dtype[, optional]): Descripción del parámetro, se agrega _optional_ si es un parámetro opcional.
    arg_2 (dtype[, optional]): Descripción del parámetro, se agrega _optional_ si es un parámetro opcional.
    ...

Returns:
    dtype: Descripción opcional del valor retornado

Raises:
    ErrorType: Descripción de cualquier error intencionalmente arrojado.
    ...

Notes:
    Notas.
"""
```

<br/>

### Estilo Numpy

El formato general para una descripción siguiendo el estilo _numpy_ es:

```
"""
Descripción de la función

Parameters:
-----------
arg_1: dtype[, optional]
    Descripción del parámetro, se agrega _optional_ si es un parámetro opcional.
arg_2: dtype[, optional]
    Descripción del parámetro, se agrega _optional_ si es un parámetro opcional.
    [Default_value]
...

Returns:
--------
dtype
    Descripción del objeto retornado
"""
```

<br/>

---
(func-parametros)=
## Parámetros

En Python al llamar una función sus parámetros pueden ser definidos usando su nombre (_keyword_) o su posición. Si no se utilizan los _keywords_ al llamar la función, el orden como se ingresen los parámetros debe de ser el mismo que el orden de cómo se definió la función. Si se utilizan los _keywords_ entonces se pueden poner en cualquier orden.

```python
# Si una función se definió como:
def my_function(param1, param2, param3):
    # function body

# Definir los parámetros por posición, implica que:
my_function(val1, val2, val3)

# Equivale a:
my_function(param1=val1, param2=val2, param3=val3)
```

Los parámetros se pueden definir en un orden distinto si se usan los _keywords_:
```python
# Llamar a un función por keywords
my_function(param3=val3, param1=val1, param2=val2)
```

Es posible hacer que los parámetros solo se puedan definir por _keywords_ usando un `*`:
```python
# Todos los parametros despues de * deben ser definidos por keywords
def my_function(params, *, keyword_params, ...):
    # function body
```
- En este caso todos los parámetros antes del `*` se pueden definir por _keyword_ o por posición, pero todos los parámetros después del `*` se deben definir por _keyword_.
- El `*` se puede poner en cualquier parte, incluso al principio.

<br/>

---
### Valores por default

Los parámetros de las funciones pueden tener valores por default que se difinen al momento de definir la función:

:::{warning}
Los valores por default deben ser tipos inmutables para evitar comportamientos inesperados en la función. Los tipos inmutables son:
- `int`
- `float`
- `bool`
- `string`
- `bytes`
- `tuple`
- `frozenset`
- `None` 
:::

```python
# Valores por default
def function_name(param1=val1, param2=val2):
    """docstring"""
    # function body
    return expression
```
- En este ejemplo, ambos parámetros tienen valores por default
- Al momento de llamar la función es posible indicar valores distintos a los valores por default.
- Si se omite algún parámetro al llamar la función, se usa su valor por default en caso de que tenga.

<br/>

---
(func-params-arb)=
### Parámetros arbitrarios

#### Posicionales

Si no se sabe cuántos parámetros posicionales serán necesarios pasar a la función, se puede usar `*args` al momento de definir la función, de esta forma la función recibe un `tuple` de parámetros y se accede a ellos de la misma manera como se accede a los tuples:
```python
# Definir función con *args
def my_function(*args, keyword1=val1, ...):
    # function body
```
- `args` es un nombre arbitario del parámetro, pero ese recomienda usar ese tal cual. Ese nombre se usará dentro de la función (sin el asterisco). Será un `tuple` dentro de la función.
- Cada argumento se separa con una coma y deben de ser todos del mismo tipo de dato.
- Se pueden especificar además otros parámetros con nombres.
- Todos los parámetros posteriores a `*args` se deben de definir por _keywords_.

:::{warning} Si los parámetro por _keyword_ no tienen valores por default, al llamar a la función se tiene que definir por keywords y no por posición, porque si no se indica el nombre se supondrá que forma parte de `*args`.
:::

**Ejemplo**: A continuación se define una función que recibe un número arbitrario de números y un valor inicial y calcula la multiplicación del valor inicial y todos los números recibidos.

```python
# Definir la función
def product(*numbers, initial=1):
    total = initial
    for n in numbers:
        total *= n
    return total

# Llamando la función
print(product(4, 4))

# Llamando la función indicando el paramtro por keyword
product(4, 5, 2, initial=3)
```
- En el ejemplo anterior si no se indicará `initial=3` y solo se pusiera el 3, entonces el 3 formaría parte de `*numbers`.

<br/>

#### Keywords

Si no se sabe cuántos _keywords_ necesita la función se puede usar `**kwargs` al momento de definir la función. De esta manera se pasará un `dict` a la función con los keywords y sus respectivos valores, dentro de la función se accederá a ellos con el nombre haciendo subsetting del diccionario.
```python
# Definir función con **kwargs
def my_function(**kwargs):
    # function body
```
- `kwargs` es un nombre arbitrario del parámetro, se recomienda usar ese tal cual, ese nombre se usará dentro de la función. Será un diccionario dentro de la función.
- Al momento de llamar la función se tienen que pasar las _keywords_ y sus valores en pares `keyword=value`:
```python
# AL llamar una función con **kwargs usar keyword=value
my_function(keyword1=val1, ...)

# Se puede definir un dict X con los key-value
X = {"keyword1": val1, ...}

# Desempacar los key-value en la función con el operador **
my_function(**X) # Equivale a my_function(keyword1=val1, ...)
```

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

<br/>

---
(func-retornar)=
## Retornar valores

Para que la función retorne un valor es necesario usar la palabra reservada `return`:
```python
# Definir función que retorne un valor
def function_name(param1, param2, ...):
    # function body
    return value
```
- `return` es la última línea que se ejecutará en el código, una vez aparezca un `return` el resto de la función (en caso de que exista) ya no se ejecutará.
- Si se quiere retornar más de un valor se recomienda que estén dentro de un `tuple`. Recordar que para crear un tuple, basta con separar los elementos con coma, no es necesario usar los paréntesis, es decir, `return a, b, c` equivale a `return (a, b, c)`.
- También es posible retornar un `dict` en lugar de un `tuple`.
- Si una función no retorna ningún valor, implícitamente retornará `None`.

```{caution}
En lugar de usar `return` se podría usar `yield`, en ese caso se retornaría un _generator_, para más información revisar {doc}`./generators`.
```

Se puede retornar toda clase de objetos, incluyendo otras funciones. Si se retorna una función y se asigna a un objeto entonces ese objeto funcionará como la función que se retornó, ejemplo:
```{code-cell} ipython3
# Definir una función que retorna print con sep="\n"
def print2(*args):
    return print(*args, sep="\n")

# Asignar la función a X
X = print2

# Ahora X funcionará como un print(*args, sep="\n")
X("foo", "bar")
```

<br/>

---
## Sentencia Pass

Una función no puede estar vacía. Si por alguna razón se necesita que una función esté vacía, se tiene que usar la palabra reservada `pass`, para evitar un error.
```python
# Definir función vacía
def my_function():
    pass
```

<br/>

---
## Llamar a una función

Para llamar a un función simplemente se usa su nombre y entre paréntesis los valores de los parámetros (en caso de que existan).
```python
# Llamar a la función "function_name"
function_name(val1, val2, ...)
```
- Si la función no tiene parámetros no poner nada dentro de los paréntesis, pero sí debe de llevar los paréntesis.
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

<br/>

---
(functions-nested-functions)=
## Funciones Anidadas

Las funciones anidadas son funciones dentro de otras funciones. Al trabajar con funciones anidades se deben de tener en cuenta los {ref}`functions-scopes` de las variables y objetos para evitar comportamientos inesperados.

```python
# Estructura básica de una función anidada
def outer(outer_params):
    # outer function body
    
    def inner(inner_params):
        # Inner function body
```
**Notas**:
- Se pueden anidar tantas funciones como sean necesarias, en este ejemplo solo se anidaron dos funciones.
- La definición de las funciones internas se puede hacer en cualquier parte del cuerpo de la función externa, simplemente tener en cuenta que se debe de definir antes de ser llamada.
- Las funciones internas pueden acceder a las objetos y parámetros de la función externa siempre y cuando el nombre no entre en conflicto con una variable definida localmente. Tener en cuenta el siguiente orden al momento de determinar en valor de una variable en una función interna:
    1. **Ámbito Local**: Primero se verifica si la variable está definida en el ámbito local.
    2. **Ámbito Contenedor**: Si la variable no se encuentra en el ámbito local, se buscan en el ámbito contenedor, es decir, en la función o funciones padres de la función hija.
    3. **Ámbito Global**: En caso de que la variable siga sin encontrarse en el ámbito contenedor entonces se buscará en el ámbito global, que son las objetos definidas en el _script_ principal.
    4. **Ámbito Built-in**: Finalmente se busca la variable en el módulo built-in de Python. 

:::{caution}
En los ámbito locales las variables de los ámbitos contenedores y globales solo son accesibles para lectura, pero no para escritura, a menos de que se usen las _keywords_ `nonlocal` y `global`, como se revisa en la siguiente sección.
:::

Es común que la función padre retorne la llamada a la función hija.

```python
# Estructura básica de una función anidada
def outer(outer_params):
    # outer function body
    
    def inner(inner_params):
        # Inner function body

    return inner(inner_args)
```

En lugar de que la función padre retorne la llamada a la función hija, podría retornarla como objeto, de tal forma que las llamadas a la función padre retornen objetos que son funciones por sí mismas. 

```python
# Estructura básica de una función anidada
def outer():
    # outer function body
    
    def inner(inner_params):
        # Inner function body

    return inner
```
- En este ejemplo es importante que la función _inner_ no utilice ninguna variable del ámbito contenedor, ya que en ese caso probablemente se trataría de un {ref}`Closure <functions-closures>`.

**Ejemplo**

```python
# Definir función padre
def raise_val():
    # Definir función hija
    def inner(x):
        raised = x ** 2
        return raised
    # Retornar función hija
    return inner

square = raise_val()
result = square(3) # Retorna 9
```

---
(functions-closures)=
## Closures

Un _closure_ es una función que tiene las siguientes características:
- Está definida dentro de otra función (una función anidada).
- Captura variables del _enclosing scope_ (ámbito contenedor), es decir, las variables de la función que la contiene.
- Retiene esas variables incluso después de que el ámbito envolvente haya terminado su ejecución.

```python
# Estructura básica de una función anidada
def outer(outer_params):
    # outer function body
    
    def inner(inner_params):
        # Inner function body

    return inner
```
- Es importante destacar que para que _inner_ efectivamente sea un _closure_ **debe** de capturar variables del _enclosing scope_, ya sea los parámetros de _outer_ o variables definidas en el cuerpo de _outer_.

:::{tip}
Para verificar que una función sea un _closure_ se puede usar el atributo `.__closure__`, si la función no es un _closure_ retorna `None`, en caso contrario retorna un `tuple`.
:::

Un closure “recuerda” el entorno en el que fue creado, permitiendo que una función anidada siga accediendo a variables locales de su función contenedora incluso después de que la función contenedora haya terminado su ejecución..

**Ejemplo**

A continuación se presenta un ejemplo de un _closure_

```{code-cell} ipython3
def raise_val(n):
    """Retorna la función hija"""
    def inner(x):
        """Eleva x a la potencia n"""
        raised = x ** n
        return raised
    return inner

square = raise_val(2)
cube = raise_val(3)
print(square(2), cube(4))
```
- Al usar `square = raise_val(2)` se crea una función que retorna `raised = x ** 2`, es decir la función _inner_ retiene el valor de _n=2_ a pesar de que ya terminó la ejecución de _raise_val(2)_.
- Al usar `cube = raise_val(3)` se crea una función que retorna `raised = x ** 3`, es decir la función _inner_ retiene el valor de _n=3_ a pesar de que ya terminó la ejecución de _raise_val(3)_.
- Se genera un _closure_ diferente cada vez que se asigna el resultado de la función externa a una variable y esos _closures_ se almacenan en memoria.

:::{note}
Un uso común de los _closures_ son los {doc}`./decorators`.
:::

<br/>

---
(functions-scopes)=
## Scopes

En Python existen cuatro tipos principales de _scopes_ (ámbitos): 

1. **Ámbito Local**: Es el ámbito dentro de una función o método. Las variables definidas aquí solo son accesibles dentro de esa función. Una vez que la función o método ha terminado de ejecutarse, las variables definidas aquí ya no están disponibles.
2. **Ámbito Contenedor**: Se refiere al ámbito de una función que contiene otra función anidada. Es el ámbito intermedio entre local y global.
3. **Ámbito Global**: Es el ámbito del módulo o _script_ donde se ejecuta el código. Las variables definidas aquí son accesibles en cualquier parte del módulo.
4. **Ámbito Built-in**: Contiene todas las funciones y constantes predefinidas de Python (por ejemplo, `print`, `None`, etc.). Este ámbito siempre está disponible en cualquier programa.

Existen dos _keywords_ que permiten modificar variables fuera del _local scope_, ya sea en el _enclosing scope_ (con `nonlocal`) o en el _global scope_ (con `global`). Sin ellas, las variables en estos niveles son solo de lectura dentro de una función.

- `nonlocal`: Se utiliza para referirse a variables definidas en el _enclosing scope_ de una función anidada. Permite modificar esas variables desde la función anidada. `nonlocal` no puede acceder al _global scope_ ni al _built-in scope_, solo al ámbito envolvente.
- `global`: Se utiliza para referirse a variables definidas en el _global scope_. Permite modificar esas variables desde dentro de una función.

**Ejemplo**:
```{code-cell} ipython3
# Variable global
x = 15 

# Función padre
def outer_function():
    # Variable en el ámbito contenedor
    y = 5
    # Otra variable en el ámbito contenedor
    x = 5 
    # función hoja
    def inner_function():
        # Acceder a la variable no local x
        nonlocal x 
        # Modifical la variable no local x
        x += y 
        print("inner: ", x)
    inner_function()
    print("outer: ", x)

outer_function()
print("global: ", x)
```
- En este ejemplo `x = 15` es una variable global porque está definida en el ámbito global.
- `y = 5` es una variable en el _enclosing scope_ porque está definida dentro de la función padre de una función anidada.
- `x = 5` es una variable en el _enclosing scope_ porque está definida dentro de la función padre de una función anidada.
- Al usar `nonlocal x` dentro de `inner_function`, entonces `x` valdrá 5, porque se está accediendo a la variable no local `x = 5`. Por lo tanto `x` es una variable no local en _inner function_. Básicamente ahora la variable `x` tanto en `inner_function` como en `outer_function` son la misma variable.
- Como `inner_function()` modifica el valor de la variable `nonlocal x` entonces ahora la variable local `x` en la función padre vale 10, en lugar de 5. El valor de la variable global no cambia porque no se accedió a ella y por lo tanto no se modificó.
- Notar que si en lugar de usar `nonlocal x` se usará `global x` dentro de `inner_function`, entonces `x` valdría 15 en `inner_function` y en el ambien global, pero no en `outer_function`, porque se estaría accediendo a la variable global `x = 15` y después de la modificación tanto "_inner_ x" como "_global_ x" valdrían 20, pero "_outer_ x" seguiría valiendo 5.

<br/>

---
## Recursión

La recursión sucede cuando dentró de una función, la función se llama a sí misma. Se debe de tener cuidado de que la función termine en algún momento y de que no se consuma demasiada memoria para procesarla.
```python
def my_function(...):
    # function body
        
    my_function(...)
        
    # function body
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

<br/>

---
## Recuperar código de una función

Para obtener el código de una función es necesario importar el módulo `inspect` (módulo _built-in_), posteriormente usar la función `getsource()`.
```python
# Importar módulo
import inspect

# Recuperar el código fuente
lines = inspect.getsource(function_name)

# Imprimir el código fuente
print(lines)
```
- Siendo _function_name_ el nombre de una función.

<br/>

---
## Atributos

Las funciones son objetos de tipo `function`, por lo tanto tienen algunos atributos. A continuación se presentan algunos atributos del tipo `function`. Para más información visitar la [documentación](https://docs.python.org/3/reference/datamodel.html#user-defined-functions) de Python.

| Atributo    | Descripción |
| :---: | :--- |
| `__closure__` | Retorna `tuple` de _células_ con los _bindings_ de las variables capturadas por el _closure_. |
| `__doc__` | Retorna el docstring de la función. |
| `__name__` | Retorna el nombre con el cual esta función fue definida. |
| `__defaults__` | `tuple` de cualquier valor predeterminado para los parámetros posicionales o _keywords_. |
| `__kwdefaults__` | Mapeo de cualquier valor predeterminado para los parámetros _keywords_. |
| `__module__` | Nombre del módulo en el cual esta función fue definida. |





