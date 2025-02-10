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

# Variables y Constantes

En esta sección se explica brevemente la declaración de constantes y variables en Python.

## Constantes

De manera nativa Python no proporciona ningún método para definir constantes inmutables. Sin embargo existen algunas constantes predeterminadas en la librería estándar:
- {ref}`False y True <built-in-operadores-bool>`.
- {ref}`tipos-none`.
- {ref}`const-ellipsis`.
- [NotImplemented](https://docs.python.org/3/library/constants.html#NotImplemented).

A pesar de que Python no fuerza la inmutabilidad de las constantes, existe la siguiente convención para declarar constantes:
- Poner los nombres en mayúsculas separando cada palabra con guiones bajos.

```python
# Ejemplos de cómo declarar una constante
PI = 3.141516
MI_CONSTANTE = 100
```

Algunas opciones para poder crear constantes insmutables en Python son las siguientes:

**Con DataClasses**:
Se puede definir una clase de constantes con el _decorator_ `dataclass` y el parámetro `frozen=True`, de esta manera no se podrán modificar las constantes:

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Constants:
    PI: float = 3.14159
    GRAVITY: float = 9.8
```
- Para usar las constantes se tendría que crear una instancia de la clase y acceder a sus atributos.

<br>

**Con el módulo typing**:
Se puede usar la clase `Final` del módulo _built-in_ `typing` para declarar constantes inmutables.

```python
from typing import Final

PI: Final = 3.14159
GRAVITY: Final = 9.8
```

:::{note}
Para más información de este módulo visitar la [documentación](https://docs.python.org/3/library/typing.html#typing-support-for-type-hints) de Python.
:::

<br>

(const-ellipsis)=
### Ellipsis

La constante `Ellipsis` funciona igual que la literal `...`, entre las funcionalidades de esta constante están las siguientes:

:::{note}
El uso de la literal `...` es preferible sobre la constante `Ellipsis`.
:::

#### Marcador de posición

Permite definir estructuras de control y funciones vacías sin que se arroje un error, de manera similar como lo haría la palabra reservada `pass`.
```python
# Definir función vacía
def my_function():
    ...

# Definir función vacía
def my_function():
    Ellipsis
```

(const-ellipsis-slicing)=
#### Slicing en numpy

Permite hacer {ref}`numpy-arrays-slicing` en arreglos multidimensionales de `numpy`. Básicamente la _Ellipsis_ indica que se expandan a tantos _slicings_ (`:`) como sean necesarios para completar las dimensiones que faltan. Cuando aparece:
- Al inicio: Se refiere a las dimensiones principales.
- En el medio: Se refiere a dimensiones intermedias.
- Al final: Se refiere a las dimensiones finales.

```python
# Slicing al inicio:
X[..., j] # Equivale a X[Ellipsis, j]

# Slicing intermedio:
X[k, ..., j] # Equivale a X[k, Ellipsis, j]

# Slicing al final:
X[i, ...] # Equivale a X[i, Ellipsis]
```
Para entender lo anterior supongamos que se tiene un array 4D con _shape_ _(blocks, depth, rows, columns)_, entonces:
- `X[..., j]` equivale a `X[:, :, :, j]`
- `X[b, ..., j]` equivale a `X[b, :, :, j]`
- `X[b, ...]` equivale a `X[b, :, :, :]`

:::{caution}
No es posible usar _ellipsis_ múltiples veces, por ejemplo `X[..., i, ...]` no está permitido.
:::

**Ejemplo**

```{code-cell} ipython3
# Definir un array 4D
import numpy as np
array_4d = np.arange(1, 17).reshape((2, 2, 2, 2))
print('Array: ', array_4d, end='\n'*2, sep='\n')

# Aplicar ellipsis al inicio
print('Slicing al incio: ', array_4d[..., -1], end='\n'*2, sep='\n')

# Aplicar ellipsis en medio
print('Slicing intermedio: ', array_4d[0, ..., -1], end='\n'*2, sep='\n')

# Aplicar ellipsis al final
print('Slicing al final: ', array_4d[0, ...], sep='\n')
```
**Notas**:
- `array_4d[..., -1]`: Equivale a seleccionar la última "columna" para todas las filas, rebanadas y "bloques" (segunda, tercera y cuarta dimensión repectivamente).
- `array_4d[0, ..., -1]`: Equivale a seleccionar la última "columna" para todas las filas, rebanadas y del primer "bloque" (segunda, tercera y cuarta dimensión repectivamente).
- `array_4d[0, ...]`: Equivale a seleccionar todo el primer "bloque" (cuarta dimensión).


#### Type Hints

_Type Hinting_ se refiere a declarar variables, parámetros, funciones, entre otros objetos de algún tipo de dato específico. La `Ellipsis` es útil particularmente en las siguientes situaciones:

:::{warning}
Python no verifica estas restricciones durante la ejecución, como su nombre lo indica son _pistas_ de los tipos de datos de las variables, mas no se fuerza a que las variables sean de ese tipo, excepto si se ejecuta el _script_ con [mypy](https://mypy-lang.org/), en ese caso sí se arrojará un error si se violan las restriciones de los tipos de datos.
:::

- Declarar un `tuple` de un tipo heterogéneo de longitud variable.

```python
# Tuple de enteros de longitud variable
numbers: tuple[int, ...] 

numbers = (1, 2, 3, 4, 5)
```

- Especificar que un `Callable` puede aceptar cualquier parámetro.

Un `Callable` especifica los argumentos que debe de recibir una función y el tipo de dato retornado. Los `Callable` se pueden especificar con la clase `Callable` del módulo _built-in_ [typing](https://docs.python.org/3/library/typing.html#typing-support-for-type-hints).
```python
# Importar clase
from typing import Callable

# Parámetro Callable
def calculate(i: int, action: Callable[..., int], *args: int) -> int:
    return action(i, *args)

# Función Callable
def func_with_args(*args: int) -> Callable[..., int]:
    ...
```
- **Parámetro**: En este ejemplo `Callable` indica que _action_ es una función que puede tomar cualquier cantidad y tipo de argumentos, pero debe de retornar un entero.
- **Función**: En este ejemplo `Callable` indica que _func_with_args_ puede tomar cualquier cantidad y tipo de argumentos, pero debe de retornar un entero.

<br>

---
## Variables

Las variables permiten almacenar objetos de los diferentes tipos de datos por medio de un nombre. Las variables en Python tienen las siguientes características:
- No necesitan declararse con algun tipo de dato en específico, son dinámicas.
- No necesitan declararse, basta con asignarles un valor.
- Las variables pueden almacenar cualquier tipo de objeto, incluyendo funciones y clases.
- Los nombres de las variables son sensibles a mayúsculas y minúsculas y deben de seguir las siguientes reglas:
    - Debe de empezar con una letras o un guión bajo (_).
    - La variables puede contener letras, números y guiones bajos.
    - Las {ref}`keywords` no pueden usarse como nombres de variables.
- Las variables almacenan la referencia a los objetos en memoria, no los objetos en sí.
- Las variables tienen diferentes {ref}`functions-scopes` que indican en qué partes del código se puede acceder al contenido de la variable.

```python
# Definir varible con valor nulo
x = None

# Definir varible con valor booleano
x = True

# Definir varible con valor numérico
y = 10

# Definir variable con una cadena
my_string = "Python"

# Realizar una operación con una variable
result = y * 10 
```

:::{tip}
Para conocer el tipo de dato de una varible se puede usar la función `type()`.
:::