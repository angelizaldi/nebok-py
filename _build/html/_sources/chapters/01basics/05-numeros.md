# Números

Existen tres tipos de datos numéricos en python `int`, `float` y `complex`. 

---
## Números flotantes
Para que un valor sea `float` se debe de agregar un punto `.` al número, sino lo incluye ya.

```python
# esto es un tipo de dato int:
2

# esto es un tipo de dato float:
2.
```

---
## Notación científica
Es posible indicar los números en en notación científica. Ejemplos:
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
Se puede crear un `NaN` ("Not a Number") con:
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
