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

# Generators

Un `generator` es una función que retorna un `iterator`, sobre el cual se puede iterar un elemento a la vez.
- Es más sencillo de trabajar con `generators` que con `iterators`. 
- Para crear un `generator` basta con utilizar dentro de una función uno o más `yield` en lugar de `return`. 
- Con `return` la función termina completamente, mientras que con `yield`, la función es pausada, conservando su último estado y es reactivada en llamadas posteriores.

Para poder acceder a los elementos del _generator_ es neceario utilizar la función `next()`, el cual retornará cada elemento a la vez. También es posible acceder a los elementos del _generator_ por medio de un cíclo como se verá más adelante.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [next](https://docs.python.org/3/library/functions.html#next)(iterator, default)
  - Recupera cada uno de los elementos de un `iterator`, uno a la vez. Si se proporcionó _default_, retorna ese valor cuando ya no haya elementos en el `iterator`, en caso contrario retornar `StopIteration`.
```


```python
# Plantilla general de un Generator
def generator_name(params):
    expression1
    yield x1
    
    expression2 
    yield x2
    
    ...

# Utilizando el generator
X = generator_name(args)
next(X)
...
```
- No es necesario asignar el generator a una variable, se puede iterar directmente sobre el objeto o utilizarlo como argumento de otras funciones.
- Sobre _X_ se puede aplicar `next()`. En la primer llamada de `next()` se ejecuta el _expression1_ hasta que encuentra el primer `yield`, se almacena los valores de las variables locales, posteriormente, si se vuelve a llamar `next()` continua ejecutando el _expression2_ hasta que encuentra el segundo `yield` y así hasta que ya no haya más `yield`. 


```{warning} 
El objeto generator solo puede ser iterable una vez.
```

Si se usa un `for loop` en un objeto generator, se obtendrá cada elemento del generator de forma automática.
```python
# Iterando sobre un generator
X = generator_name(args):
for i in X
    # for body
    
# Se puede iterar directamente sobre el generator
for i in generator_name(args):
    # for body
```

<br>

**Ejemplo**: En el siguiente ejemplo se define un generator que genera una secuencia de números. En este ejemplo se recupera el primer elemento con `next()` y el resto dentro de un `for loop`.

```{code-cell} python3
# Definir el generator
def my_range(n):
    i = 0
    while i < n:
        yield i
        i += 1

# Asignar a una variable
X = my_range(5)

# Recuperar el primer elemento:
print("Primer elemento:", next(X))
        
# Recuperar el resto de los elementos: 
print("Resto de los elementos")
for i in X:
    print(i)

# Tratar de recuperar otro elemento
print(next(X, "empty"))
```
- Después de agotar todos los elementos en el `for loop`, si se trata de recuperar otro elemento se retorna un error `StopIteration` o en este caso, un valor por default.

<br/>

---
## Generator Expression

Es como un _list comprehenssion_, pero en lugar de devolver una lista, devuelve un objeto `generator`. Tener en cuenta las siguientes características:
- Un _generator expression_ produce un solo elemento, cada vez que es llamado con `next()`. 
- Es útil si se van a generar muchos valores, en ese caso es mejor generarlos poco a poco. 
- La sintaxis es similar a las _lists comprehenssion_, pero se usan paréntesis
```python
# Uso básico de un generator expression
X = [expression for i in collection]
```
- _collection_ es cualquier `iterable`.
- _expression_ es cualquier expresión cuya evaluación retorne un objeto.
- _X_ es el objeto donde se almacenará el objeto `generator` y sobre el cual se aplicará la función `next()` o usar directamente dentro de un `for loop` para ejecutarlo todo.
- _expression_ es lo que devolverá el _generator expression_ cada vez que sea llamado con `next()`.

:::{tip} Los generator expression pueden ser usados como argumento de funciones que reciben un `iterable`, en ese caso, no es necesario poner los paréntesis.

<code>
sum(expression for i in iterable) 
</code>

En este caso devolverá la suma de todos los elementos del generator.
:::

Los _generator expression_ también pueden tener condicionales, tanto en la parte de _expression_ como en la parte de _collection_, de manera que solo a cierto elementos se les aplique el código o de que dependiendo del resultado de la _expression_ se ponga un valor u otro. Sintaxis:

**En el iterable**: En este caso _expression_ solo se evalua si los elementos de _collection_ cumplen una condición.
```python
# generator expression con condicional en collection
X = (expression for i in collection if condition)
```

**En la _expression_**: En este caso el elemento de `X` dependerá del resultado de _condition_.
```python
# generator expression con condicional en expression
X = (expression_true if condition else expression_false for i in collection)
```

:::{note}
Se pueden utilizar ambos tipos de condicionales al mismo tiempo.
:::

Es posible además anidar más de una colección de manera similar a como se anidarían cíclos:
```python
# Generator expression anidado
X = (expression for i in collection1 for j in collection2)
```

**Ejemplo**: 
Encontrar los elementos al cuadrado de un rango numérico, solo si el número es par.
```{code-cell} ipython3
# Definir un iterable
numeros = range(1, 11)

# Definir el generator expression 
pares_cuadrados = (numero**2 for numero in numeros if numero % 2 == 0)

# Imprimir primer elemento del generator
print(next(pares_cuadrados))
```