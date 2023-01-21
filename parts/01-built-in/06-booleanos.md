# Valores booleanos

Son valores que toman las palabras reservadas `True` y `False`. Normalmente resultan de alguna comparación con operadores de comparación, membresía o identidad. Los valores booleanos tienen valores numéricos equivalentes donde `True` es igual a 1 y `False` es igual a cero.

La función `bool()` convierte cualquier objeto en `True` o `False`. Casi todos los objetos son considerados `True` a excepción de unos cuantos. Los objetos que retornan `False` al utilizarlos con la función `bool()` son:
- `False`: Palabra reservada `False`.
- `None`: Palabra reservada `None`.
- `0`: Número cero entero.
- `0.0`: Número cero flotante.
- `""`: Cadena vacía.
- `()`: Tuple vacío.
- `[]`: Lista vacía.
- `{}`: Diccionario vacío.
