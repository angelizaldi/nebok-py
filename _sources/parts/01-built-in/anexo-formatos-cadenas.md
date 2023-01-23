---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python
---

# Formatos de cadena

Para dar formatos en el método `str.format()` y en f-strings, se utiliza dos puntos y el formato que se quiere dar dentro de las llaves `{}`:
```python
# f-string
f"... {expression:format}"

# método format
"... {expression:format} ...".format(...)
```
- <code><i> format </i></code>: Es el formato que se quiere dar.

Los formatos disponibles son:

```{list-table}
:header-rows: 1
:name: label-to-reference

* - Formato.
  - Resultado.
* - `{expression:<N}`
  - Alinear el texto a la izquierda, dejando _N_ espacios en blanco a la derecha.
* - `{expression:>N}`
  - Alinear el texto a la derecha, dejando _N_ espacios en blanco a la izquierda.
* - `{expression:^N}`
  - Alinear el texto al centro, dejando _N/2_ espacios en blanco a la der. e izq.
* - `{expression:+}`
  - Imprimir el signo del número, positivos y negativos.
* - `{expression:-}`
  - Imprimir el signo del número, solo el de los negativos.
* - `{expression:,}`
  - Separar con una coma los miles.
* - `{expression:.Ne}`
  - Imprimir el número en formato científico, con la e en minúscula, con _N_ decimales.
* - `{expression:.NE}`
  - Imprimir el número en formato científico, con la E en minúscula, con _N_ decimales.
* - `{expression:.Nf}`
  - Imprimir un número décimal, con _N_ decimales.
* - `{expression:.N%}`
  - Imprimir un número en formato de porcentaje, con _N_ décimales, el número tiene que ser >0 y <1.
* - `{expression:s}`
  - Dar formato como cadena.
* - `{expression:date-format}`
  - Imprimir una fecha, en un formato específico, utilizando los códigos de fechas, junto con otros caracteres. Por ejemplo `%Y-%m-%d`.
```
- _N_: Son números enteros, suelen ser opcionales.
- _expression_: Es la expresión, número, cadena, etc. a la que se le dará formato.

<br>

**Ejemplos***

```{code-cell} python3
# Definir la variable
x = 1897.9876

# Diversos formatos que se pueden aplicar a "x".
print(f"Sin formato: {x}", end="\n"*2)

print(f"Separar los miles: {x:,}", end="\n"*2)

print(f"Notación científica con 1 décimal: {x:.1e}", end="\n"*2)

print(f"Con tres décimales (redondea): {x:.3f}", end="\n"*2)

print(f"Combinación de separación de miles y 2 décimales: {x:,.2f}", end="\n"*2)
```