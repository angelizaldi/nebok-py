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

# Decorators

```{attention} En esta sección solo se cubre lo básico en relación a decorators y no pretende cubrir extensamente el tema. Se recomienda consultar otras fuentes para saber más del tema.
```

- Un "_decorator_" modifica el comportamiento de una función, puede modificar los inputs, los outputs o modificar el comportamiento como tal de la función. 
- Los decorators reciben una función como parámetros y retornan otra. 
- Los decorators se utilizan junto con el símbolo `@` y se ponen justo arriba de la función que se quierer alterar:

---
## Crear un decorator:

- Para crear un decorator se tiene que crear una función anidada. 
- La función padre debe de recibir como argumento la función que se va a modificar y retornar una función hija. 
- La función hija recibe los argumentos de la función que se va a modificar (si tiene) y realizar cualquier modificación o comportamiento de la función original.
- La función hija puede o no retornar objetos, dependiendo de las intenciones del decorador.
```python
# Definir el decorator
def decorator_function(function):
    ...
    def inner_function(args):
        # Aqui se define cualquier modificación a function
        ...
        # No es obligatorio retornar algo
        return something
    return inner_function

# Utilizar el decorator
@decorator_function
def my_function(args):
    ...
    
# Usar el @ equivale a hacer lo siguiente:
my_function = decorator_function(my_function)
```
- _decorator_function_: Es una función que recibe como argumento otra función que es justamente la que va a decorar, en este caso function.
- _decorator funcion_ suele ser un "_closure_".
- Después de usar el decorator _my_function_ tendrá las modificaciones definidas en _inner_function_.

Ejemplo:
El siguiente ejemplo modifica el comportamiento de la función `_fecha_`, esta función retorna la fecha actual con ayuda de la función `datetime.datetime.today()`, sin el decorator el valor retornado sería similar a `datetime.datetime(YYY, MM, DD, HH, MM, SS)`, pero con el decorator retorna una cadena en un formato `"YYYY-MM-DD"`.

```{code-cell} ipython3
from datetime import datetime

def format_decorator(fecha):
    def formatter():
        return fecha().strftime("%Y-%m-%d")
    return formatter

@format_decorator
def fecha():
    return datetime.today()

print(fecha())
```
