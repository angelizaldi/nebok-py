# Números

Existen tres tipos de datos numéricos en python `int`, `float` y `complex`. 

---
## Números enteros y flotantes

- Los números enteros corresponden al tipo `int`. Están limitados solo por la memoria disponible en la computadora.
- Los números con decimales corresponden al tipo `float`.
- Para que un valor sea `float` se debe de agregar un punto `.` al número, sino lo incluye ya, por ejemplo:
```python
# Tipo de dato "int"
2

# Tipo de dato "float"
2.
```

Se pueden usar las funciones `int()` y `float` para convertir otros objetos en números enteros o flotantes, respectivamente, por ejemplo, para convertir valores `bool` o `str` a números.

---
## Notación científica

Es posible indicar los números en notación científica. Ejemplos:

```python
# Formas de representar el número 1000.0
1e3
1E3 

# Forma de representar el número 0.001
1e-3
```

---
## Valor infinito

Se pueden crear valores que representen el infito con:

```python
# Infinito positivo
float("inf")

# Infinito negativo
float("-inf")
```

```{note}
Otras forma de crear un valor que represente el infinito:
- `math.inf`: Librería built-it `math`.
- `numpy.inf`: Librería `numpy`.
```

---
## NaN - Not a Number

Se puede crear un `NaN` ("_Not a Number_") con:
```python
float("NaN")
```

```{note}
Otras forma de crear un valor que represente un "Not a Number":
- `math.nan`: Librería built-it `math`.
- `numpy.nan`: Librería `numpy`.
```

---
## Números complejos. 

Se agrega una jota `j` al final del número. Ejemplos:
```python
# Un número imaginario.
0+1j 

# Un número complejo.
3+5j
```