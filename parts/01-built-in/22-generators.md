# Generators

- Es una función que retorna un `iterator`, sobre el cual se puede iterar un elemento a la vez.
- Es más sencillo de trabajar con `generators` que con `iterators`. 
- Para crear un `generator` basta con utilizar dentro de una función uno o más `yield` en lugar de `return`. 
- Con `return` la función termina completamente, mientras que con `yield`, la función es pausada y conservando su último estado y es reactivada en llamadas posteriores. 
```python
# Ejemplo de un generator
def generator_name(...):
    expression1
    yield x1
    
    expression2 
    yield x2
    
    ...

# Utilizando el generator
X = generator_name(...)
next(X)
...
```
- Básicamente la función se asigna a un objeto `X`, posteriormente sobre este objeto `X` se puede aplicar `next()`. En la primer llamada de `next()` se ejecuta el _expression1_ hasta que encuentra el primer `yield`, se almacena los valores de las variables locales, posteriormente, si se vuelve a llamar `next()` continua ejecutando el _expression2_ hasta que encuentra el segundo `yield` y así hasta que ya no haya más `yield`. 


```{warning} 
El objeto generator solo puede ser iterable una vez.
```

Si se usa un `for loop` en un objeto generator, se obtendrá cada elemento del generator de forma automática.
```python
# Iterando sobre un generator
X = generator_name()
for i in X
    ...
```

## Generator Expression:

- Es como un _list comprehenssion_, pero en lugar de devolver una lista, devuelve un objeto `generator`
- El generator expression produce un solo elemento, cada vez que es llamado con `next()`. 
- Es útil si se van a generar muchos valores, en ese caso es mejor generarlos poco a poco. 
- La sintaxis es similar a las _lists comprehenssion_, pero se usan paréntesis
```python
# Sintaxis de un generator expression
X = (expression for i in iterable)
```
- `X` es el objeto donde se almacenará el objeto `generator` y sobre el cual se aplicará la función `next()` o usar directamente dentro de un `for loop` para ejecutarlo todo.
- _expression_ es lo que devolverá el generator expression cada vez que sea llamado con `next()`.
- _i_ es un nombre arbitrario para referirse a los elementos del iterable en la parte de _expression_.
- `iterable` es un objeto en el que se puede iterar.

```{tip} Los generator expression pueden ser usados como argumento de funciones que reciben un `iterable`, en ese caso, no es necesario poner los paréntesis.

<code> python
sum(expression for i in iterable) 
</code>

En este caso devolverá la suma de todos los elementos del generator.
```

```{note}
Es posible usar condicionales dentro del generator expression al igual que con list comprehenssions.
```

