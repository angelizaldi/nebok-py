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

# Sets

Corresponde al tipo `set`. Son objetos iterables para almacener múltiples elementos en una sola variable. Algunas características del tipo de dato` set` son:
- Se pueden almacenar diferentes tipos de datos en un `set`.
- Los elementos no están ordenados, por lo tanto no se puede acceder a ellos por medio de índices.
- Un mismo valor **no** puede existir múltiples veces en una `set`.
- Es mutable: Se pueden modificar una vez creado el `set`. 
- Es un iterable: Se puede iterar por sus elementos y se puede usar la palabra reservada `in` para verificar memebresía.

Para más información visitar la [documentación](https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset) de Python.

---
## Creación de sets

Existen dos métodos principales para crear una sets:

**1.** Poner los elementos, separados por coma, dentro de llaves `{}`:
```python
X = {x1, x2, ..., xn}
```
- Recordar que los elementos deben de ser únicos.


**2.** Convertir un `iterable` es un `set` con la función `set()`:
```python
# Convertir el iterable Y a un set
X = set(Y)
```
- Si `Y` tenía elementos repetidos, entonces solo se mantendrá una copia de ellos en `X`.

Otra forma de crear un `set` es con ref`{set-comp}`.

---
## Selección de elementos

No se puede extraer los elementos de un set. La única forma para acceder a los elementos de un set es en un `for loop` (ver {ref}`iteracion-sets`) o conviertiendo el `set` en `list` o alguna otra secuencia.

---
##  Agregar y eliminar elementos

Para agregar y eliminar elementos de un `set` usar los siguientes métodos:
- Para agregar:
  - Agregar un elemento al set usar el método `set.add`.
  - Concatenar sets usar el método `set.update`.

- Para eliminar:
  - Eliminar todos los elementos usar el método `set.clear`.
  - Eliminar un elemento específico usar el método `set.discard`. 
  - Eliminar y retornar un elemento específico usar el método `set.pop`.
  - Eliminar un elemento específico y retornar error si no existe usar el método `set.remove`.
 
```{note}
Para más información de esos métodos consultar la sección de {ref}`Metodos-Agregar <set-metodos-agregar>` y {ref}`Metodos-Eliminar <set-metodos-eliminar>`.
```

Para eliminar todo el `set` (no solo sus elementos) se puede usar la palabra reservada `del`:
```python
# Si X es un set
del X
```

---
## Verificar que un elemento exista en un set:
Para verificar si un elemento está dentro de un `set` usar el operador de membresía `in`:
```python
# Si X es un set
x in X
```
- Alternativamente se puede usar `not in`.

---
(iteracion-sets)=
## Iteración en sets

Para interar sobre todos los elementos de una `set` se puede usar un `for loop`. 
```python
# Iterar sobre los elementos del set X:
for ele in X:
    ...
```

```{caution} Como los sets no están indexados el orden en el que aparecen los elementos puede diferir si se itera un mismo set varias veces.
```

---
## Operaciones entre conjuntos

Los `set` básicamente son la representación de un conjunto matemático en Python, es decir, una colección de elementos únicos. Por ello se puede realizar operaciones entre sets de la misma manera como se hacen operaciones entre conjuntos. A continuación se enlistan las operaciones disponibles:
- **Unión**: Para determinar la unión de dos sets se usa el operador `|`: <br> `X|Y`
- **Intersección**: Para determinar la intersección de dos sets se usa el operador `&`: <br> `X&Y`.
- **Diferencia**: Para determinar la diferenca de dos sets se usa el operador `-`: <br> `X-Y`.
- **Diferencia simétrica**: Para determinar la diferencia simétrica de dos sets se usa el operador `^`: <br> `X^Y`.
- **Subconjunto propio**: Para determinar si un set es un subcojunto propio se puede usar los operadores `<` o `>`: <br> `X<Y` o `X>Y`.
- **Subconjunto**: Para determinar si un set es un subcojunto se puede usar los operadores `<=` o `>=`: <br> `X<=Y` o `X>=Y`.

Todos estos operadores tienen sus métodos equivalente los cuales se pueden encontrar en {ref}`Metodos-Operaciones <set-metodos-operaciones>` y {ref}`Metodos-Información <set-metodos-informacion>`.

---
(set-comp)=
## Set comprehension

Son sets que se crean a partir procesos iterativos con la estructura `for`. Sintaxis:
```python
X = {expression for i in collection}
```
donde:
- _collection_ es cualquier `iterable`
- _expression_ es cualquier expresión cuya evaluación retorne un objeto.

Los sets comprehension pueden tener condicionales, tanto en la parte de _expression_ como en la parte de _collection_, de manera que solo a cierto elementos se les aplique el código o de que dependiendo del resultado de _expression_ se ponga un valor u otro. Sintaxis:

**En el iterable**: En este caso _expression_ solo se evalua si los elementos de _collection_ cumplen una condición.
```python
X = {expression for i in collection if condition}
```

**En la _expression_**: En este caso el elemento de `X` dependerá del resultado de _condition_.
```python
X = {val_true if condition else val_false for i in collection}
```

---
## Métodos de sets

En esta sección se enlistan los métodos del tipo `set` por categorias. 

Tener en cuenta que los métodos generalmente se aplican sobre un objeto de tipo `set`, por ejemplo, si `X` es `set`, entonces se utiliza <code>X.<i>method_name</i></code>. Sin embargo es posible usar el `set` como argumento de <code>set.<i>method_name</i></code>. Por ejemplo.

```{code-cell} ipython3
# Definir el set
X = {"a", "b", "c"}

# Usar el metodo sobre el objeto
print(X.difference({"a", "c"}))

# Equivale a:
print(set.difference(X, {"a", "c"}))
```
- Tener en cuenta que en la segunda forma el `set` siempre debe de ser el primer argumento.

---
### Agregar elementos

Métodos para agregar elementos a un `set`. 

```{list-table} Agregar
:header-rows: 1
:name: set-metodos-agregar

* - Funciones
  - Descripción
* - [add](https://docs.python.org/3/library/stdtypes.html#frozenset.add)(elem)
  - Agrega un elemento al `set`.
```

---
### Eliminar elementos

Métodos para eliminar elementos de un `set`. 

```{list-table} Eliminar
:header-rows: 1
:name: set-metodos-eliminar

* - Funciones
  - Descripción
* - [discard](https://docs.python.org/3/library/stdtypes.html#frozenset.discard)(elem)
  - Elimina el elemento `elem` del `set` si está presente in-place.
* - [pop](https://docs.python.org/3/library/stdtypes.html#frozenset.pop)()
  - Elimina y devuelve un elemento arbitrario del conjunto. Retorna `KeyError` si el conjunto está vacío.
* - [clear](https://docs.python.org/3/library/stdtypes.html#frozenset.clear)()
  - Remueve todos los elementos del `set`.
* - [remove](https://docs.python.org/3/library/stdtypes.html#frozenset.remove)(elem)
  - Elimina el elemento `elem` del conjunto. Genera `KeyError` si `elem` no está en el conjunto.
```

---
### Información sobre el set

Métodos para recuperar información sobre el `set` en relación con otros objetos.

```{list-table} Información
:header-rows: 1
:name: set-metodos-informacion

* - Funciones
  - Descripción
* - [issuperset](https://docs.python.org/3/library/stdtypes.html#frozenset.issuperset)(other)
  - Retorna `True` si cada elemento en `other` está en el conjunto. Equivale al operador `>`.
* - [isdisjoint](https://docs.python.org/3/library/stdtypes.html#frozenset.isdisjoint)(other)
  - Devuelve `True` si el conjunto no tiene elementos en común con `other`. Los conjuntos son disjuntos si y sólo si su intersección es el conjunto vacío.
* - [issubset](https://docs.python.org/3/library/stdtypes.html#frozenset.issubset)(other)
  - Retorna `True` si cada elemento del conjunto está en `other`. Equivale al operador `<`.
```

---
### Operaciones

Métodos para realizar operaciones entre conjuntos y que retornan un nuevo `set`.

```{list-table} Operaciones
:header-rows: 1
:name: set-metodos-operaciones

* - Funciones
  - Descripción
* - [difference](https://docs.python.org/3/library/stdtypes.html#frozenset.difference)(*others)
  - Devuelve un nuevo conjunto con elementos que están en el conjunto que no están en los demás. Equivale a usar el operador `-`.
* - [union](https://docs.python.org/3/library/stdtypes.html#frozenset.union)(*others)
  - Devuelve un nuevo conjunto con elementos del conjunto y `*others`. Equivale a usar el operador `|`.
* - [intersection](https://docs.python.org/3/library/stdtypes.html#frozenset.intersection)(*others)
  - Devuelve un nuevo conjunto con elementos comunes al conjunto y `*others`. Equivale a usar el operador `&`.
* - [symmetric_difference](https://docs.python.org/3/library/stdtypes.html#frozenset.symmetric_difference)(other)
  - Devuelve un nuevo conjunto con elementos en el conjunto o en `other` pero no en ambos. Equivale a usar el operador `^`.
```

---
### Operaciones-inplace

Métodos para realizar operaciones entre conjuntos y que actualizan un `set` en lugar de retornar uno nuevo. Básicamente realizan las operaciones in-place.

```{list-table} Operaciones-inplace
:header-rows: 1

* - Funciones
  - Descripción
* - [difference_update](https://docs.python.org/3/library/stdtypes.html#frozenset.difference_update)(*others)
  - Actualiza el `set`, eliminando los elementos que se encuentren en `*other`. Equivale a usar el operador `-=`.
* - [update](https://docs.python.org/3/library/stdtypes.html#frozenset.update)(*others)
  - Actualiza un `set` con los elementos de `*others`. Equivale a usar el operador `|=`.
* - [intersection_update](https://docs.python.org/3/library/stdtypes.html#frozenset.intersection_update)(*others)
  - Actualiza el `set`, manteniendo solo los elementos que se encuentran en él y todos los demás. Equivale a usar el operador `&=`.
* - [symmetric_difference_update](https://docs.python.org/3/library/stdtypes.html#frozenset.symmetric_difference_update)(other)
  - Actualiza el `set`, conservando solo los elementos que se encuentran en cualquiera de los conjuntos, pero no en ambos. Equivale a usar el operador `^=`.
```

---
### Copiar

Método para realizar la copia de un `set`.

```{list-table} Copiar
:header-rows: 1

* - Funciones
  - Descripción
* - [copy](https://docs.python.org/3/library/stdtypes.html#frozenset.copy)()
  - Devuelve una copia superficial del `set`.
```

---
## Funciones útiles para listas

Algunas funciones built-in útiles para sets son:
- `len()`: Encontrar la longitud (número de elementos) del `set`.