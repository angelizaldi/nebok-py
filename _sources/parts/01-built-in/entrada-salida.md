---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python
---

# Impresión y solicitud de datos

En esta sección se enlistan las funciones para impimir valores en la consola o para solicitar el ingreso de datos desde la consola.

```{list-table}
:header-rows: 1

* - Funciones
  - Descripción
* - [print](https://docs.python.org/3/library/functions.html#print)(*objects, sep=' ', end='\n', file=None, flush=False)
  - Imprime en pantalla.
* - [input](https://docs.python.org/3/library/functions.html#input)(prompt)
  - Solicita ingresar datos al usuario mientras se ejecuta el programa.
```

## Impresión

| Función | Descripción |
| ------- | ----------- |
| [print](https://docs.python.org/3/library/functions.html#print)(*objects, sep=' ', end='\n', file=None, flush=False) |  Imprime en pantalla uno o más objetos. |
**Parámetros**:
- _*objects_: Objetos a imprimir, por default se llama al método `__str__()` de los objetos, si este método no está definido entonces se llama a `__repr__()`.
- _sep_ - `str`: Indica cómo separar cada objeto al momento de imprimirlo.
- _end_ - `str`: Indica cómo finalizar la impresión, después de imprimir todos los objetos. 

:::{note}
En {doc}`../appendix/IPython` también existe la función `display()` para imprimir objetos. 
:::

**Ejemplo**:

En este ejemplo de imprimie una cadena y posteriormente el resultadod de una expresión.

```{code-cell} ipython3
# Imprimir hola mundo
print("Hola Mundo!", end="\n"*2)

# Imprimir el resultado de una expresión
print(5+10)
```

<br/>

---
## Solicitud

| Función | Descripción |
| ------- | ----------- |
| [input](https://docs.python.org/3/library/functions.html#input)(prompt |  Solicita ingresar datos al usuario mientras se ejecuta el programa. |
**Parámetros**:
- _prompt_ - `str`: Mensaje que se mostrará al usuario al solicitar el ingreso de datos.

```python
# Uso básico
variable = input("Mensaje para el usuario: ")
```
- _variable_: Es la variable donde se almacenará el contenido ingresado por el usuario.

:::{caution}
`input()` siempre retorna una cadena (`str`). Si es necesario datos números se recomienda convertir con las función `int()` o `float()`.
:::
