# Tipos de Datos

Los principales tipos de datos built-in de Python se resumen a continuación. Para más información seguir en link de cada uno de ellos:

- Valor nulo.
    - {ref}`tipos-none`: Constante que representa la ausencia de valor.
- Booleano:
    - {ref}`bool <tipos-none>`: `True` o `False`. Se puede considerar con un subtipo numérico.
- {ref}`tipos-numericos`:
    - `int`: Números enteros.
    - `float`: Números flotantes.
    - `complex`: Números complejos.
- Cadenas:
    - {doc}`str <./str>`: Cadenas de caracteres.
- Secuencias:
    - {doc}`list <./lists>`: Contenedor de objetos mutable.
    - {doc}`tuple <./tuples>`: Contenedor de objetos inmutable.
- Sets
    - {doc}`str <./sets>`: Contenedor de objetos únicos mutable.
    - [frozenset](https://docs.python.org/3/library/stdtypes.html#frozenset): Contenedor de objetos únicos inmutable.
- Mappings :
    - {doc}`dict <./dicts>`: Contenedor de objetos en pares _key-value_.

<br>

---
## Clasificación de los Tipos de Datos

Tener en cuenta la siguiente clasificación de tipos ya que constante se puede referir a varios tipos de acuerdo a las siguientes categorías:

- Mutabilidad:
    - Inmutables:
        - `int`
        - `float`
        - `bool`
        - `string`
        - `bytes`
        - `tuple`
        - `frozenset`
        - `None` 
    - Mutables:
        - `list`
        - `dict`
        - `set`
        - `bytearray`
        - `objects`
        - `functions`  
- Escalares (`scalar`): Son tipos que almacenan un solo valor (a excepción de `str`), incluye a:
    - `bool`
    - `int`
    - `float`
    - `complex`
    - `str`
    - `None`
<br>
- Secuencias (`sequence`): Son tipos que tienen una colección **ordenada** de elementos, incluye a:
    - `list`
    - `tuple`
    - `range`
    - `str`
<br>
- Iterables (`iterable`): Son tipos sobre los que se puede iterar, incluye a:
    - `list`
    - `tuple`
    - `range`
    - `str`
    - `set`
    - `dict`

:::{caution}
Notar que la principal diferencia entre `sequence` e `iterable`, es que los elementos de `sequence` están ordenados, es decir, cada elemento tiene un índice único asociado y por lo tanto se pueden indexar, mientras que los `iterable` no.

Todos los `sequence` son `iterable`, pero no al revés.
:::