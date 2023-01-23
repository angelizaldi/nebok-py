# For Loop.

Es un cíclo que se usa para iterar sobre un objeto iterable. Se ejecuta una o más expresiones para cada uno de los elementos del iterable.
```python
# Plantilla básica de un for loop
for key in iterable:
    expression
```
- _key_ es un nombre arbitrario. Ese nombre es el que se utilizará dentro de código para hacer referencia al elemento del iterable en cada iteración.
- _iterable_ es un un objeto `iterable` (consultar [Tipos de datos](tipos-datos.md)). En algunos casos _iterable_ retorna 2 o más objetos en cada iteración, se debe de poner tantos _keys_ como objetos retornados separados por coma.
- Se puede poner más de un iterable, en ese caso se deben de poner la cantidad de keys correspondientes.

```{warning} Es muy importante que se respete la indentación, esa es la forma como Python determina qué parte del código forma parte de cada bloque de la estructura. Los dos puntos indican el inicio de un bloque que debe de estar indentado.
```

```{tip} 
Para iterar por rangos numéricos se recomienda usar la función `range()`.
```

---
## Sentencias

Son palabras reservadas para manipular el comportamiento del cíclo:
- `break`: Se detiene la iteración y se sale del cíclo.
- `continue`: Se detiene la iteración actual y se pasa a la siguiente iteración.
- `pass`: Un cíclo `for` no puede estar vacío, si por alguna razón se necesita un `for` vacío usar `pass` para evitar un error.
- `else`: Se ejecuta un código una vez que el cíclo ya se terminó de ejecutar. Esta parte no se ejecuta si se usa un `break`. La sintaxis es:
```python
# Plantila básica de un for loop - else
for key in iterable:
    expression
else:
    expression
```

---
## Funciones útiles

Algunas funciones útiles al definir iterables son:
- `range`: Retorna rangos numéricos.
- `enumerate`: Retorna tuplas de un rango numérico y los elementos de un iterable.
- `zip`: Retorna tuplas de elementos de iterables.

Para más información consultar [Funciones built-in](func-built-in.md)