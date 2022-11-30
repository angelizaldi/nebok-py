
# Valores booleanos

Son valores que toman las palabras reservadas `True` y `False`. Normalmente resultan de alguna comparación con operadores de comparación, membresía o identidad.

`bool()` Sirve para evaluar cualquier objeto como `True` o `False`. Casi todos los tipos de objetos son considerados `True` a excepción de unos cuantos, como se verá más adelante.
```python
bool(x)
```
- x `objeto`

Los objetos que retornan `False` al utilizarlos con la función `bool()` son:
- `False`: Palabra reservada `False`.
- `None`: Palabra reservada `None`.
- `0`: Número cero entero.
- `0.0`: Número cero flotante.
- `""`: Cadena vacía.
- `()`: Tuple vacío.
- `[]`: Lista vacía.
- `{}`: Diccionario vacío.
