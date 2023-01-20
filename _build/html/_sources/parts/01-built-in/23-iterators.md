# Iterators

Un `iterator` es un objeto que es iterable, es decir que se puede acceder a sus elementos uno por uno. Técnicamente hablando, en Python un iterator es un objeto que se le puede aplicar los protócolos `__iter__()` y `__next__()`.

Se puede obtener un `iterator` de los objetos iterables (`list`, `tuple`, `set`, `dict` y `str`)  con `iter()`.

**iter**:

`iter()`: Convierte un objeto iterable en un `iterator`
```python
	Y = iter(X)
```

**Parámetros:**
- **`X`** \- `iterable`: Un objeto iterable.
- **`Y`** \- `object`: Es una variable que almacenará los elementos, para acceder a ellos usar `next()`.

**Retorna:**
-  `iterator`.

---
**next**:

`next()`: Devuelve cada uno de los elementos extraídos por `iter()`, uno a la vez. Para acceder a los elementos se tiene que ejecutar `next()` una vez por elemento. Cuando ya no haya elementos aparecerá un error `StopIteration`.
```python
	next(Y, [default])
```

**Parámetros:**
- **`Y`** \- `iterator`: Es un objeto creado con `iter()`.
- **`defaul`** \- `object`: Es un valor a retornar cuando ya no haya elemento en `y`, en lugar de `StopIteration`.

**Retorna:**
-  `object`.
