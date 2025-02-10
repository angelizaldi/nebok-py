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

```{attention} En esta sección solo se cubre lo básico en relación a _decorators_ y no pretende cubrir extensamente el tema. Se recomienda consultar otras fuentes para saber más del tema.
```

- Un "_decorator_" modifica el comportamiento de una función, puede modificar los _inputs_, los _outputs_ o modificar el comportamiento como tal de la función. 
- Los _decorators_ reciben una función como parámetro y retornan otra función. 
- Los _decorators_ se utilizan junto con el símbolo `@` y se ponen justo arriba de la función que se quierer alterar.

```python
# Utilizar un decorator
@my_decorator
def my_function(params):
    # function body
```

Los _decorators_ son útiles cuando se quiere añadir un comportamientos en común a múltiples funciones. Sería poco útil desarrollar un _decorator_ que solo se utilizará en una única función. Los _decorators_ podrían entonces compactar la cantidad de código necesario para definir tales funciones.

<br/>

---
## Crear un decorator

Para crear un _decorator_ tener en cuenta lo siguiente:
- Se tiene que crear una función anidada. 
- La función padre debe de recibir como argumento la función que se va a modificar y retornar una función hija. 
- La función hija recibe los argumentos de la función que se va a modificar (si tiene) y realizar cualquier modificación o comportamiento de la función original.
- La función hija puede o no retornar objetos, dependiendo de las intenciones del decorador.
```python
# Plantilla general de un decorator

# Definir el decorator
def decorator_function(my_function):
    ...
    # Definir la función interna
    def inner_function(args):
        # Aqui se define cualquier modificación a my_function
        ...
        # No es obligatorio retornar algo
        return something
    # Retornar la función interna
    return inner_function

# Utilizar el decorator
@decorator_function
def my_function(args):
    ...
    
# Usar el @ equivale a hacer lo siguiente:
my_function = decorator_function(my_function)
```
- _decorator_function_: Es el nombre de una función que recibe como argumento otra función que es justamente la que va a decorar, en este caso _my_function_.
- _decorator_function_ suele ser un {ref}`Closure <functions-closures>`.
- Después de usar el _decorator_ _my_function_ tendrá las modificaciones definidas en _inner_function_.

:::{tip}
Es posible que el decorator reciba otros argumentos aparte de la función, para ello se debe de encapsular el _decorator_ dentro de una función que retorne el decorador, y es esta función la que recibirá los argumentos extras. Al utilizar el decorador se deben de pasar los argumentos: <br/> `@my_decorator(args)`
:::

<br>

**Ejemplo**: El siguiente ejemplo modifica el comportamiento de la función _fecha_, esta función retorna la fecha actual con ayuda de la función `datetime.datetime.today()`. Sin el _decorator_ el valor retornado sería similar a `datetime.datetime(YYY, MM, DD, HH, MM, SS)`, pero con el _decorator_ retorna una cadena en un formato `"YYYY-MM-DD"`.

```{code-cell} ipython3
from datetime import datetime

# Definir el decorator
def decorator_formato(fecha):
    # Definir la función interna
    def formato():
        # Modificar el comportamiento de "fecha()"
        return fecha().strftime("%Y-%m-%d")
    # Retornar la función interna
    return formato

# Aplicar el decorator a "fecha()"
@decorator_formato
def fecha():
    return datetime.today()

print(fecha())
```
