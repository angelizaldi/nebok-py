# For Loop

Es una estructura cíclica que se usa para iterar sobre un objeto iterable. Se ejecuta una o más expresiones, para cada uno de los elementos del iterable.
```python
# Sintaxis básica de for loop
for key in iterable:
    # for body

# Con múltiples keys (ejm de 2)
for key1, key2 in iterable:
    # for body
```
- _key_ es un nombre arbitrario. Ese nombre es el que se utilizará dentro _for body_ para hacer referencia al elemento del iterable en cada iteración.
- _iterable_ es un un objeto `iterable` (consultar [Tipos de datos](tipos-datos.md)). En algunos casos los elementos de _iterable_ pueden ser otros objetos iterables, por lo que se puede hacer {ref}`unpacking <list-unpack>` de los elementos y poner tantos _keys_ como objetos retornados separados por coma.

```{warning} Es muy importante que se respete la indentación, esa es la forma como Python determina qué parte del código forma parte de cada bloque de la estructura. Los dos puntos indican el inicio de un bloque que debe de estar indentado.
```

```{tip} 
Para iterar por rangos numéricos se recomienda usar la función `range()`.
```

<br/>

---
## Sentencias

Son palabras reservadas para manipular el comportamiento del cíclo:
- `break`: Se detiene la iteración y se sale del cíclo.
- `continue`: Se detiene la iteración actual y se pasa a la siguiente iteración.
- `pass`: Un cíclo `for` no puede estar vacío, si por alguna razón se necesita un `for` vacío usar `pass` para evitar un error.
- `else`: Se ejecuta un código una vez que el cíclo ya se terminó de ejecutar. Esta parte no se ejecuta si se usa un `break`. La sintaxis es:
```python
# Uso de la sentencia else
for key in iterable:
    expression
else:
    expression
```
