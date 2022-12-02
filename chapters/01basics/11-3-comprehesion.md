# List comprehension

Son sets que se crean a partir procesos iterativos con la estructura `for`. Sintaxis:
```python
X = {expression for i in collection}
```
donde:
- _collection_ es cualquier `iterable`
- _expression_ es cualquier expresión cuya evaluación retorne un objeto.

Lo anterior equivale a:
```python
X = []
for i in collection:
    X.add(expression)
```

Los sets comprehension también pueden tener condicionales, tanto en la parte de _expression_ como en la parte de _collection_, de manera que solo a cierto elementos se les aplique el código o de que dependiendo del resultado de _expression_ se ponga un valor u otro. Sintaxis:

En el iterable:
```python
X = {expression for i in collection if condition}
```

En la _expression_:
```python
X = {val_true if condition else val_false for i in collection}
```