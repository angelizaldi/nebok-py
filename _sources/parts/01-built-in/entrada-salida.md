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

:::{note}
En {doc}`../08-otros/IPython` también existe la función `display()` para imprimir objetos. 
:::

```{code-cell} ipython3
# Imprimir hola mundo
print("Hola Mundo!", end="\n"*2)

# Imprimir el resultado de una expresión
print(5+10)
```
