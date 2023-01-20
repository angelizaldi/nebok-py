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

# Regular Expressions

Un “_regular expression_” es una secuencia de caracteres para identificar y extraer patrones en cadenas. Para usar “regular expressions” es necesario importar el módulo {re}.
```python
import re
```

Un patrón en expresiones regulares se conforma de:
- texto.
- Metacaracteres y secuencias especiales.

Si una o más partes de la cadena coinciden con el patrón entonces se dice que hay un "_Match_".

## Greedy y Non-Greedy

Se refiere a la manera como se realiza la búsqueda del patrón, cuando se utilizan los metacaracteres `*`, `+`, `?` o `{num, num}` en un patrón, para ello se agrega un `?` extra.

- **Greedy**: Coincide la mayor cantidad de caracteres posibles. Retorna el match más largo. Los metacaracteres `*`, `+`, `?` o `{num, num}` son greedy por default.
- **Non-greedy**: Coincide la menor cantidad de caracteres posibles. Retorna el match más corto. Se agrega el metacaracter `?`.

La forma como funciona es que los metacaracteres `*`, `+`, `?` o `{min, max}` tienen dos posibles opciones, por ejemplo, tomando `+`, significa **una vez** o **más veces** el caracter a la izquierda. Por default se buscará que sea **más veces**, pero si se agrega un `?` entonces se forzará a que sea **una vez**. De tal forma que tenemos entonces:
- `+`: Más de una vez.
- `+?`: Una vez.
- `*`: Más de una vez.
- `*?`: Cero veces.
- `{min, max}`: _max_ veces.
- `{min, max}?`: _min_ veces.
- `?`: Una vez.
- `??`: Cero veces.

Ejemplo
```{code-cell} python3
import re

cadena = "123abc"

# Cualquier caracter numerico una o **mas veces** -> "123"
print(re.search(r"\d+", cadena).group(0))

# Cualquier caracter numerico **una** o mas veces -> "1"
print(re.search(r"\d+?", cadena).group(0)) 

# Cualquier caracter numerico cero o **mas veces** -> "123"
print(re.search(r"\d*", cadena).group(0)) 

# Cualquier caracter numerico **cero** o mas veces -> ""
print(re.search(r"\d*?", cadena).group(0)) 
```

## Capturando grupos

Si se desea recuperar solo una parte del patrón usado, y no todo, se puede encerrar entre paréntesis el grupo de caracteres que se desea recuperar. Un patrón puede tener uno o más grupos.

## Flags

## Funciones

## Objeto Regular Expression

## Objeto Match

