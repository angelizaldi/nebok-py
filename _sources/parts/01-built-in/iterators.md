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

# Iterators

Un `iterator` es un objeto que es iterable, es decir que se puede acceder a sus elementos uno por uno. Técnicamente hablando, en Python un iterator es un objeto que se le puede aplicar los protócolos `__iter__()` y `__next__()`.

Se puede obtener un `iterator` de los objetos iterables (`list`, `tuple`, `set`, `dict` y `str`)  con `iter()`.


```{list-table} iter
:header-rows: 1

* - Funciones
  - Descripción
* - [iter](https://docs.python.org/3/library/functions.html#iter)(object)
  - Convierte un `iterable` en un `iterator`.
* - [next](https://docs.python.org/3/library/functions.html#next)(iterator, default)
  - Recupera cada uno de los elementos de un `iterator`, uno a la vez. Si se proporcionó `default`, retorna ese valor cuando ya no haya elementos en el `iterator`, en caso contrario retornar `StopIteration`.
```

<br>

**Ejemplo**: A continuación se presenta un sencillo ejemplo del uso de iterators:

```{code-cell} ipython3
# Crear un objeto iterable
X = ["a", "b", "c"]

# Crear un iterator desde X
iter_X = iter(X)

# Recuperar el primer elemento:
print("Primer elemento:", next(iter_X))

# Recuperar el resto de los elementos: 
print("Resto de los elementos:")
for i in iter_X:
    print(i)
    
# Tratar de recuperar otro elemento
print(next(iter_X, "empty"))
```
- Si se itera sobre un `iterator` no es necesario usar `next()` y por default la iteración se detendrá en el último elemento.
- Después de agotar todos los elementos en el `for loop`, si se trata de recuperar otro elemento se retorna un error `StopIteration` o en este caso, un valor por default.