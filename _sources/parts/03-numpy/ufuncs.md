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

# Ufuncs

Las _ufuncs_ (_universal functions_) son funciones especiales de `numpy` que permiten operar sobre objetos `ndarray` de manera vectorizada o _element-wise_ (elemento por elemento). Existen de dos tipos, unitarias y binarias, dependiendo de la cantidad de operandos.

:::{important}
No todas las funciones en `numpy` son _ufunc_. Para una lista completa de las funciones _ufunc_ visitar la [documetación](https://numpy.org/doc/stable/reference/ufuncs.html#available-ufuncs) de `numpy`. En esta sitio las _ufunc_ se pueden encontrar principalmente en las siguientes secciones.
- [Matemáticas y numéricas](./matematicas-numericas.md).
- [Operadores](./operadores.md).
- [Información](./informacion.md).
:::

:::{tip}
Las funciones _ufunc_ de `numpy` también se pueden usar en los objetos de `pandas` como `DataFrame` y `Series`.
:::

Para saber si una función es _ufunc_ usar:
```python
# Retorna el tipo de una función
type(function_name) # -> Debe retornar <class ‘numpy.ufunc’>

# Veririfacr el tipo de una función
type(function_name) == np.ufunc # Retorna True o False
```

<br/>

## Párametros comunes

Las funciones _ufunc_ comparten varios parámetros. A continuación se explicarán los más comunes, para una lista completa visitar la [documentación](https://numpy.org/doc/stable/reference/ufuncs.html) de `numpy`.
- `where` \- `array-like` de `bool` (_mask_): Array booleano, para indicar en qué elementos sí aplicar la función y cuáles dejar intactos.
- `dtype` \- `dtype`: Define el tipo de dato que deben de tener los elementos retornados.
- `out`  \- `object` de tipo `ndarray` o `None`: Es para indicar el objeto donde se almacenará el resultado, es posible poner el mismo objeto en el que se está haciendo la operación para que sea _in-place_.


<br/>

---
## Ufuncs personalizadas

Para crear una _ufuncs_ personalizadas, primero se debe definir una función de manera tradicional o utilizar una _built-in_, posteriormente se debe de agregar la función a la librería _ufunc_ de `numpy` con `frompyfunc()`.

[numpy.frompyfunc](https://numpy.org/doc/stable/reference/generated/numpy.frompyfunc.html#numpy-frompyfunc)(func, /, nin, nout, *\[, identity])
- `function` \-  `function`: Es el nombre de una función de Python.
- `nin` \- `int`: Número de argumentos de ingreso.
- `nout` \- `int`: Número de objetos retornados por la función.

```python
# Definir función
def my_func(params):
    # function body

# Agregar función a la librerica ufuc    
my_ufunc = np.frompyfunc(my_func)
```

**Ejemplo**

En este ejemplo se convertirá la función `str.center(string, width[, fillchar)` en una _ufunc_.

```{code-cell} ipython3
# Importar numpy
import numpy as np

# Convertir función a ufunc
ucenter = np.frompyfunc(str.center, 3, 1)

# Usar función
ucenter(np.array(["abc", "A", "12345"]), 7, "*")
```

<br/>

Lo anterior también se habría logrado usando:
```python
# Usando el metodo en cada cadena
np.array(["abc".center(7, "*"), "A".center(7, "*"), "12345".center(7, "*")])

# Aplicando map
np.array([*map(str.center, ["abc", "A", "12345"], [7]*3, ['*']*3)])
```

---
## Atributos

Atributos de las funciones `ufunc`. 

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - `__doc__`
  - Cadena de documentación para cada _ufunc_.
* - `__name__`
  - El nombre de la _ufunc_.
* - [ufunc.identity](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.identity.html)
  - El elemento identidad de la _ufunc_, si tiene (identidad como el concepto matemático de elemento identidad en operaciones).
* - [ufunc.nargs](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.nargs.html)
  - El número de argumentos.
* - [ufunc.nin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.nin.html)
  - El número de entradas.
* - [ufunc.nout](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.nout.html)
  - El número de salidas.
* - [ufunc.ntypes](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.ntypes.html)
  - El número de tipos.
* - [ufunc.signature](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.signature.html)
  - Definición de los elementos centrales sobre los que opera una _ufunc_ generalizada.
* - [ufunc.types](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.types.html)
  - Retorna un ´list´ con tipos agrupados _entrada->salida_.
```

<br>

## Métodos

Métodos de las funciones `ufunc`. 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [ufunc.accumulate](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.accumulate.html)(array[, axis, dtype, out])
  - Acumula el resultado de aplicar el operador a todos los elementos. Equivale a hacer cálculos acumulados.
* - [ufunc.at](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.at.html)(a, indices[, b])
  - Realiza una operación _in\-place_ sin búfer en `a` para los elementos especificados por `indices`. Un mismo índice puede aparecer múltiples veces en `indices` y la operación se aplicaría ese mismo número de veces a ese elemento.
* - [ufunc.outer](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.outer.html)(A, B, /, **kwargs)
  - Aplica la operación _ufunc_ a todos los pares _(a, b)_ con _a_ en `A` y _b_ en `B` (en el producto cartesiando de `A` y `B`).
* - [ufunc.reduce](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.reduce.html)(array[, axis, dtype, out, ...])
  - Reduce la dimensión de ´array´ a uno (vector), aplicando la _ufunc_ a lo largo de un eje. Equivale a hacer _aggregates_.
* - [ufunc.reduceat](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.reduceat.html)(array, indices[, axis, ...])
  - Realiza una reducción (local) con cortes especificados en un solo eje.
```

### Ejemplos

A continuación se presentan ejemplos de algunos métodos seleccionados (para más ejemplos presionar sobre el nombre de cada método en la tabla de métodos para dirigirse a la documentación de `numpy`).

```{code-cell} ipython3
# Definir el array
a = np.array([1, 2, 3])

# Ejemplo de accumulate
print("Acumulado: ", np.add.accumulate(a), end='\n'*2)

# Ejemplo de reduce
print("Aggregate: ", np.add.reduce(a), end='\n'*2)

# Ejemplo de outer
print("Producto cartesiano: \n", np.power.outer(a, a), end='\n'*2)
```