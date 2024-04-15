# Tipos de datos

Los principales tipos de datos built-in de Python se resumen a continuación:

- Numéricos:
    - `int`: Números enteros.
    - `float`: Números flotantes.
    - `complex`: Números complejos.
- Booleanos
    - `bool`: Valores booleanos. Se puede considerar con un subtipo numérico.
- Secuencias:
    - `list`: Contenedor de objetos mutable.
    - `tuple`: Contenedor de objetos inmutable.
- Cadenas:
    - `str`: Cadenas de caracteres.
- Sets
    - `set`: Contenedor de objetos únicos mutable.
    - `frozenset`: Contenedor de objetos únicos inmutable.
- Mappings :
    - `dict`: Diccionario.
    
## Clasificación de los tipos de datos

Tener en cuenta la siguiente clasificación:

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
Notar que la principal diferencia entre `sequence` e `iterable`, es que los elementos de `sequence` están ordenados, es decir, cada elemento tiene un índice único asociado y por lo tanto se pueden indexar (hacer _subsetting_), mientras que los `iterable` no.

Todos los `sequence` son `iterable`, pero no al revés.
:::