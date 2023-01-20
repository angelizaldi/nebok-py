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

# List comprehension

Son listas que se crean a partir procesos iterativos con la estructura `for`. Sintaxis:
```python
X = [expression for i in collection]
```
donde:
- _collection_ es cualquier `iterable`
- _expression_ es cualquier expresión cuya evaluación retorne un objeto.

Lo anterior equivale a:
```python
X = []
for i in collection:
    X.append(expression)
```

Las list comprehension también pueden tener condicionales, tanto en la parte de _expression_ como en la parte de _collection_, de manera que solo a cierto elementos se les aplique el código o de que dependiendo del resultado de la _expression_ se ponga un valor u otro. Sintaxis:

En el iterable:
```python
X = [expression for i in collection if condition]
```

En la _expression_:
```python
X = [expression_true if condition else expression_false for i in collection]
```

Ejemplo:
```{code-cell} ipython3
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squared_even_numbers = [number**2 for number in numbers if number % 2 == 0]
print(squared_even_numbers)
```

> En el código anterior hubiera sido más eficiente utilizar la función `range()` para crear la secuencia de números.

