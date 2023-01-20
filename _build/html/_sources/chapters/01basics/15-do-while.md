# Do While

El cíclo `while` ejecuta un código mientras una condición sea `True`.
```python
while condition:
    expression
```
- _condition_ es una expresión que utiliza operadores de comparación o `bool()`, o en general cualquier expresión que retorne `True` o `False`.

```{warning} Es muy importante que se respete la indentación, esa es la forma como Python determina qué parte del código forma parte de cada bloque de la estructura. Los dos puntos indican el inicio de un bloque que debe de estar indentado.
```

```{warning} El ciclo `while` necesita una variable que se vaya actualizando en el código de la estructura y que se utilice en la condición. Excepto si se usa la sentencia `break`.
```

---
## Sentencias

Son palabras reservadas para manipular el comportamiento del cíclo:
- `break`: Se detiene la iteración y se sale del cíclo.
- `continue`: Se detiene la iteración actual y se pasa a la siguiente iteración.
- `pass`: Un cíclo `for` no puede estar vacío, si por alguna razón se necesita un `for` vacío usar `pass` para evitar un error.
- `else`: Se ejecuta un código una vez que el cíclo ya se terminó de ejecutar. Esta parte no se ejecuta si se usa un `break`. La sintaxis es:
```python
while condition:
    expression
else:
    expression
```

