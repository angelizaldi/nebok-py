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

Una “_expresión regular_” es una secuencia de caracteres para identificar y extraer patrones en cadenas. Para usar _regular expressions_ es necesario importar el módulo `re`.
```python
# Importar el módulo
import re
```

Un patrón en expresiones regulares se conforma de:
- Texto: Coincide tal cual como se indique en la cadena.
- {ref}`caracteres-especiales` y {ref}`sec-especiales`: Son metacaracteres que significan algo en especial. Visitar sus respectivas secciones para más información.

Si una o más partes de la cadena coinciden con el patrón entonces se dice que hay un "_Match_".

<br>

---
## Buscar patrones usando regex

Para buscar un patrón usando regular expressions se puede hacer principalmente de dos formas.

:::{attention}
Los patrones de expresiones regulares se indican utilizando cadenas _crudas_ (_"raw strings"_), es decir, como `r'regex_pattern'`.
:::


**1.** Usar directamente las {ref}`funciones-regex` para buscar patrones. Por ejemplo `re.search()`, `re.match()` o `re.findall()`. En este caso se debe de proveer tanto del patrón a buscar como de la cadena donde se va a buscar el patrón. Ejemplo:

```{code-cell} python3
# Importar el módulo
import re

# Definir una cadena
X = "abc 123 xyz"

# Buscar un patrón en la cadena
result = re.search(r"\d+", X)

# Imprimir resultado
print(result.group(0))
```

**2.** Usar la función `re.compile()` para compilar un patrón y retornar un objeto `Pattern` y posteriormente usar los {ref}`pattern-metodos` de `Pattern` para buscar coincidencias como `Pattern.search()`, `Pattern.match()` o `Pattern.findall()`. En este caso, el patrón a buscar se indica en la función `re.compile()` y la cadena donde se va a buscar se indica como argumento de los métodos de `Pattern`. Esta opción es particularmente útil si se utilizará en múltiples ocasiones un mismo patrón. Ejemplo:

```{code-cell} python3
# Importar el módulo
import re

# Definir una cadena
X = "abc 123 xyz"

# Compilar un patrón
pattern = re.compile(r"\d+")

# Buscar el patrón en X
result = pattern.search(X)

# Imprimir el patrón encontrado
print(result.group(0))
```

<br><br>

---
## Búsqueda greedy y non-greedy

Se refiere a la manera como se realiza la búsqueda del patrón, cuando se utilizan los caracteres especiales (cuantificadores) `*`, `+`, `?` o `{min, max}` en un patrón, para ello se agrega un `?` extra.

- **Greedy**: Coincide la mayor cantidad de caracteres posibles. Retorna el match más largo. Los caracteres especiales `*`, `+`, `?` o `{min, max}` son greedy por default.
- **Non-greedy**: Coincide la menor cantidad de caracteres posibles. Retorna el match más corto. Se agrega el metacaracter `?`.

La forma como funciona es que los caracteres especiales `*`, `+`, `?` o `{min, max}` tienen dos posibles opciones. Tomando a `+` como ejemplo, significa **una vez** o **más veces** el caracter a la izquierda. Por default se buscará que sea **más veces**, pero si se agrega un `?` entonces se forzará a que sea **una vez**. De tal forma que tenemos:
- `+`: Más de una vez.
- `+?`: Una vez.
- `*`: Más de una vez.
- `*?`: Cero veces.
- `{min, max}`: _max_ veces.
- `{min, max}?`: _min_ veces.
- `?`: Una vez.
- `??`: Cero veces.

<br>

***Ejemplo***: En este ejemplo se puede observar cómo se modifica la búsqueda de patrones dependiendo de si es una búsqueda greedy o non-greedy. El patrón que se está buscando son caracteres numéricos.

```{code-cell} python3
# Importar el módulo
import re

# Definir la cadena
cadena = "123abc"

# Cualquier dígito una o **mas veces** -> "123"
print(re.search(r"\d+", cadena).group(0), end="\n"*2)

# Cualquier dígito **una** o mas veces -> "1"
print(re.search(r"\d+?", cadena).group(0), end="\n"*2) 

# Cualquier dígito cero o **mas veces** -> "123"
print(re.search(r"\d*", cadena).group(0), end="\n"*2) 

# Cualquier dígito **cero** o mas veces -> ""
print(re.search(r"\d*?", cadena).group(0), end="\n"*2) 

# Cualquier dígito cero o **una vez** -> "1"
print(re.search(r"\d?", cadena).group(0), end="\n"*2) 

# Cualquier dígito **cero** o una vez -> ""
print(re.search(r"\d??", cadena).group(0), end="\n"*2) 

# Cualquier dígito mínimo 2 y máximo **3 veces** -> "123"
print(re.search(r"\d{2,3}", cadena).group(0), end="\n"*2) 

# Cualquier dígito mínimo **2** y máximo 3 veces -> "12"
print(re.search(r"\d{2,3}?", cadena).group(0)) 
```

<br><br>

---
## Capturando grupos

Si se desea recuperar solo una parte del patrón usado, y no todo, se puede encerrar entre paréntesis el grupo de caracteres que se desea recuperar. Un patrón puede tener uno o más grupos.

---
### Capturando un grupo

La funcionalidad general cuando solo se captura un solo grupo es la siguiente:

Si se usa `re.search()` o `Pattern.search()` se recupera solo la primer coincidencia que satisface el patrón en la cadena. 

El método `Match.group()` retorna el grupo capturado, el cual recibe como argumento un número entero, tener en cuenta lo siguiente:
- Si no se indica ningún argumento equivale a usar cero `0`.
- Si se indica cero `0` entonces se retorna toda la primer coincidencia con el patrón, no solo el grupo, sino todo el patrón.
- Si se indica uno `1` entonces se retorna solo la primer coincidencia del grupo.


```{code-cell} python3
# Importar el módulo
import re

# Definir una cadena
X = "abc 123 #&@ 789"

# Compilar el patrón definiendo un grupo
result = re.search(r"(\d+)", X)

# Recuperar el patrón
print(f"Patrón: {result.group(0)}")

# Recuperar el grupo
print(f"Grupo: {result.group(1)}")
```
- En en el ejemplo anterior, el patrón `\d+` significa que se debe coincidir con uno o más dígitos. 
- `result.group(0)` y `result.group(1)` retornan el mismo resultado porque el patrón `r"(\d+)"` es igual al grupo capturado (todo el patrón está entre paréntesis). 

Si se indica un patrón más complejo el resultado será diferente.

```{code-cell} python3
# Importar el módulo
import re

# Definir una cadena
X = "abc 123 #&@ 789"

# Compilar el patrón definiendo un grupo
result = re.search(r"\w+ (\d+)", X)

# Recuperar el patrón
print(f"Patrón: {result.group(0)}", end="\n"*2)

# Recuperar el grupo
print(f"Grupo: {result.group(1)}")
```

Como se comentó anteriormente, `re.seach()` solo retorna la primer coincidencia. Si se desea recuperar todas las coincidencias se puede usar la función `re.findall()` o el método `Pattern.findall()`.

```{code-cell} python3
# Importar el módulo
import re

# Definir una cadena
X = "abc 123 #&@ 789"

# Compilar el patrón definiendo un grupo
result = re.findall(r"(\d+)", X)

# Recuperar el patrón
print(f"Resultado de r\'(\d+)\': {result}", end="\n"*2)

# Compilar el patrón definiendo un grupo
result2 = re.findall(r"\w+ (\d+)", X)

# Recuperar el patrón
print(f"Resultado de r\'\w+ (\d+)\': {result2}")
```
- `result` retorna dos coincidencias porque hay dos subcadenas en `X` que representan uno o más dígitos.
- `result2` retorna solo una coincidencia porque solo hay una subcadena que representa uno o más dígitos y que están después de uno o más caracteres alfabéticos, seguido de un espacio en blanco, lo cual solo se satisface con "123".

<br>

---
### Capturando múltiples grupos

Es posible recuperar dos o más grupos. Tener en cuenta que para recuperar un grupo específico se debe indicar su índice en el mismo orden en el que aparece en el patrón

```{code-cell} python3
# Importar el módulo
import re

# Definir una cadena
X = "abc 123 #&@ xyz 789"

# Compilar el patrón definiendo un grupo
result = re.search(r"(\w+) (\d+)", X)

# Recuperar el patrón buscado
print(f"Patrón: {result.group(0)}", end="\n"*2)

# Recuperar el grupo 1
print(f"Grupo 1: {result.group(1)}", end="\n"*2)

# Recuperar el grupo 2
print(f"Grupo 2: {result.group(2)}")
```

Si se usa `re.findall()` o `Pattern.findall()` entonces se recupera una lista de tuplas con las coindidencias:

```{code-cell} python3
# Importar el módulo
import re

# Definir una cadena
X = "abc 123 #&@ xyz 789"

# Compilar el patrón definiendo dos grupos
result = re.findall(r"(\w+) (\d+)", X)

# Recuperar los grupos
print(f"Resultado de r\'\w+ (\d+)\': {result}")
```

<br><br>

---
## Sustituyendo patrones

En esta sección se cubre lo básico de cómo usar la función `re.sub()` para reemplazar patrones en una cadena por otros. La función `re.sub()` reemplaza todos los patrones encontrados por otra expresión, se puede limitar el número de reemplazos con el parámetro `count`.

En su forma más simple reemplaza todas las coincidencias por otra cadena. Por ejemplo, reemplazar todos las subcadenas que sean dígitos por un "-".

```{code-cell} python3
# Importar el módulo
import re

# Definir una cadena
X = "abc 123 #&@ xyz 789"

# Encontrar el patrón
result = re.sub(r"\d+", "-", X)

# Imprimir resultado
print(result)
```

Es posible recuperar la coincidencia usando grupos para incluirla en el reemplazo utilizando `\1` para recuperar el primer grupo, `\2` para el segundo grupo, etc. Por ejemplo, reemplazar todas las subcadenas que sean dígitos por la misma subcadena entre paréntesis

```{code-cell} python3
# Importar el módulo
import re

# Definir una cadena
X = "abc 123 #&@ 789"

# Encontrar el patrón 
result = re.sub(r"(\d+)", r"(\1)", X)

# Imprimir resultado
print(result)
```
- Un mismo grupo se puede utilizar más de una vez en el reemplazo. Por ejemplo, si en lugar de usar `r"(\1)"` se usará `r"(\1-\1)"`, entonces `123` se reemplazaría por `(123-123)`.


Tener en cuenta que lo que se reemplaza es toda la coincidencia, no solo el grupo. En el siguiente ejemplo el patrón es uno o más caracteres alfabéticos, un espacio y uno o más dígitos y se cambiarán el orden en que aparece el patrón.

```{code-cell} python3
# Importar el módulo
import re

# Definir una cadena
X = "abc 123 xyz 789"

# Encontrar el patrón
result = re.sub(r"(\w+) (\d+)", r"\2 \1", X)

# Imprimir resultado
print(result)
```
- En este ejemplo hay dos coincidencias `abc 123` y `xyz 789`, por lo tanto lo que se intercambia es el orden en cada coincidencia.

Finalmente, es posible usar una función para reemplazar la coincidencia, esta función recibe como parámetro un objeto `Match`. En el siguiente ejemplo se busca uno o más caracteres alfabéticos y se reemplaza por la misma cadena pero en mayúsculas.

```{code-cell} python3
# Importar el módulo
import re

# Definir una cadena
X = "abc 123 #&@ 789 zyx"

# Encontrar el patrón "abc"
result = re.sub(r"(\w+)", lambda match: match.group().upper(), X)

# Imprimir resultado
print(result)
```
- En este ejemplo hay dos coincidencias con el patrón `abc` y `zxy`.
- En este ejemplo en particular usar `match.group()` equivale a usar `match.group(0)` y `match.group(1)`.

<br><br>

---
## Flags

A continuación se presenta una lista de `flags` para modificar el comportamiento de las {ref}`funciones-regex` o de los métodos de objetos como {ref}`objeto-match` o {ref}`objeto-pattern`. Las flags se ponen como argumentos de las funciones como `re.search()`, `re.match()` o `re.find_all()` o de los métodos del objeto `Pattern`.

Listado de flags:

:::{warning}
La mayoría de las flags tienen 2 posibles formas de representarlas, aquí solo se presenta una de esas formas. Presionar en el nombre de cada flag para dirigirse a la documentación de Python para obtener más información.
:::


```{list-table}
:header-rows: 1

* - Flag
  - Descripción
* - [A](https://docs.python.org/3/library/re.html#re.A)
  - Hace que `\w`, `\W`, `\b`, `\B`, `\d`, `\D`, `\s` y `\S` realicen solo coincidencias ASCII en lugar de coincidencias Unicode completas.
* - [DEBUG](https://docs.python.org/3/library/re.html#re.DEBUG)
  - Muestra información de depuración sobre la expresión compilada.
* - [I](https://docs.python.org/3/library/re.html#re.I)
  - Indica que se realicen las coincidencias sin distinción entre mayúsculas y minúsculas.
* - [L](https://docs.python.org/3/library/re.html#re.L)
  - Hace que `\w`, `\W`, `\b`, `\B` y coincidencias sin distinción entre mayúsculas y minúsculas dependientes de la configuración regional actual.
* - [M](https://docs.python.org/3/library/re.html#re.M)
  - Hace que el carácter de patrón '^' coincide con el principio de la cadena y al comienzo de cada línea (inmediatamente después de cada salto de línea); y el carácter de patrón '$' coincide al final de la cadena y al final final de cada línea (inmediatamente antes de cada salto de línea).
* - [NOFLAG](https://docs.python.org/3/library/re.html#re.NOFLAG)
  - Indica que no se aplique ningúna flag, el valor es 0.
* - [S](https://docs.python.org/3/library/re.html#re.S)
  - Indica que el carácter especial '.' coincida con cualquier carácter, incluido un nueva línea (`\n`).
* - [X](https://docs.python.org/3/library/re.html#re.X)
  - Esta flag permite escribir expresiones regulares que se ven mejor y son más legible al permitir separar visualmente secciones lógicas del patrón y añadir comentarios.
```

<br>

---
### Ejemplo de uso: 

A continuación se ejemplifica como usar la flag `re.I` para no hacer distintinción entre mayúsculas y minúsculas al momento de hacer una búsqueda. Notar que esta misma flag también se puede expresar como `re.IGNORECASE`.


```{code-cell} python3
# Importar el módulo
import re

# Definir una cadena
X = "abc 123 ABC 456 AbC"

# Encontrar el patrón "abc"
result = re.findall(r"abc", X)

# Imprimir resultado
print(f"Resultado de buscar \'abc\': {result}")

# Ignorando minúsculas y mayúsculas
result2 = re.findall(r"abc", X, re.I)

# Imprimir resultado
print(f"Resultado de buscar \'abc\' con re.I: {result2}")
```

<br><br>

---
(funciones-regex)=
## Funciones

A Continuación se presenta una lista de funciones del módulo `re`.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [compile](https://docs.python.org/3/library/re.html#re.compile)(pattern, flags=0)
  - Compila un patrón de expresión regular en un objeto de expresión regular, que se puede usar para hacer coincidir usando `match()`, `search()` y otros métodos.
* - [escape](https://docs.python.org/3/library/re.html#re.escape)(pattern)
  - Para indicar que se ignores caracteres especiales en el patrón.
* - [findall](https://docs.python.org/3/library/re.html#re.findall)(pattern, string, flags=0)
  - Devuelve todas las coincidencias no superpuestas del patrón en la cadena como `list`. Si no se encuentran coincidencias entonces devuélve una lista vacía. Cuando `pattern` tiene grupos, retorma `list` de `tuples`, donde cada elemento del `tuple` es un grupo.
* - [finditer](https://docs.python.org/3/library/re.html#re.finditer)(pattern, string, flags=0)
  - Retorna un `iterator` que produce objetos `match` sobre todas las coincidencias que no se superponen para el patrón en la cadena.
* - [fullmatch](https://docs.python.org/3/library/re.html#re.fullmatch)(pattern, string, flags=0)
  - Si toda la cadena coincide con el patrón de expresión regular, devuelve un objeto `match` correspondiente. Retorna `None` si la cadena no coincide con el patrón.
* - [match](https://docs.python.org/3/library/re.html#re.match)(pattern, string, flags=0)
  - Retorna un objeto `match` si se encuentra un patrón al principio de una cadena. Retorna `None` si la cadena no coincide con el patrón.
* - [purge](https://docs.python.org/3/library/re.html#re.purge)()
  - Borre la caché de expresiones regulares.
* - [search](https://docs.python.org/3/library/re.html#re.search)(pattern, string, flags=0)
  - Retorna un objeto `match` si se encuentra un patrón en una cadena. Si hay más de una coincidencia, solo devolverá la información de la primera coincidencia.
* - [split](https://docs.python.org/3/library/re.html#re.split)(pattern, string, maxsplit=0, flags=0)
  - Divide la cadena por las ocurrencias del patrón. Si los paréntesis de captura son utilizado en el patrón, también se devuelve el texto de todos los grupos en el patrón como parte de la lista resultante.
* - [sub](https://docs.python.org/3/library/re.html#re.sub)(pattern, repl, string, count=0, flags=0)
  - Reemplaza un patrón por otro en una cadena. Por default reemplaza todos los patrones que se encuentren.
* - [subn](https://docs.python.org/3/library/re.html#re.subn)(pattern, repl, string, count=0, flags=0)
  - Realiza la misma operación que `sub()`, pero devuelva un `tuple` `(new_string, number_of_subs_made)`.
```

<br><br>

---
(objeto-pattern)=
## Objeto Regular Expression

Los objetos de regular expression `Pattern` son objetos que son retornados por la función `re.compile()`. Estos objetos se pueden usar para buscar coincidencias.

<br>

---
### Crear un objeto Pattern

Para crear un objeto `Pattern` se debe de usar la función `re.compile()`, donde se indique la expresión regular a buscar.


```{code-cell} python3
# Importar el módulo
import re

# Crear el objeto
pattern = re.compile(r"$a\d*")

# Imprimir el tipo de pattern
print(type(pattern))
```

Posteriormente se pueden usar sus atributos y métodos para recuperar información sobre el objeto o realizar búsqueda de patrones, entre otras acciones.


<br>

---
### Atributos

A continuación se presenta una lista de los atributos de instancia de `Pattern`. 

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - [flags](https://docs.python.org/3/library/re.html#re.Pattern.flags)
  - Las flags de coincidencia de expresiones regulares.
* - [groupindex](https://docs.python.org/3/library/re.html#re.Pattern.groupindex)
  - Un diccionario que mapea cualquier nombre de grupo simbólico definido por `(?P<id>)` para agrupar números.
* - [groups](https://docs.python.org/3/library/re.html#re.Pattern.groups)
  - El número de grupos de captura en el patrón.
* - [pattern](https://docs.python.org/3/library/re.html#re.Pattern.pattern)
  - La cadena de patrón a partir de la cual se compiló el objeto `Pattern`.
```

<br>

---
(pattern-metodos)=
### Métodos

A continuación se presenta una lista de los métodos de instancia de `Pattern`. 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [findall](https://docs.python.org/3/library/re.html#re.Pattern.findall)(string[, pos[, endpos]])
  - Devuelve todas las coincidencias no superpuestas del patrón en la cadena como `list`. Si no se encuentran coincidencias entonces devuélve una lista vacía. Cuando `pattern` tiene grupos, retorma `list` de `tuple`, donde cada elemento del `tuple` es un grupo.
* - [finditer](https://docs.python.org/3/library/re.html#re.Pattern.finditer)(string[, pos[, endpos]])
  - Retorna un `iterator` que produce objetos `match` sobre todas las coincidencias que no se superponen para el patrón en la cadena.
* - [fullmatch](https://docs.python.org/3/library/re.html#re.Pattern.fullmatch)(string[, pos[, endpos]])
  - Si toda la cadena coincide con el patrón de expresión regular, devuelve un objeto `match` correspondiente. Retorna `None` si la cadena no coincide con el patrón.
* - [match](https://docs.python.org/3/library/re.html#re.Pattern.match)(string[, pos[, endpos]])
  - Retorna un objeto `match` si se encuentra un patrón al principio de una cadena. Retorna `None` si la cadena no coincide con el patrón.
* - [search](https://docs.python.org/3/library/re.html#re.Pattern.search)(string[, pos[, endpos]])
  - Retorna un objeto `match` si se encuentra un patrón en una cadena. Si hay más de una coincidencia, solo devolverá la información de la primera coincidencia.
* - [split](https://docs.python.org/3/library/re.html#re.Pattern.split)(string, maxsplit=0)
  - Divide la cadena por las ocurrencias del patrón. Si los paréntesis de captura son utilizado en el patrón, también se devuelve el texto de todos los grupos en el patrón como parte de la lista resultante.
* - [sub](https://docs.python.org/3/library/re.html#re.Pattern.sub)(repl, string, count=0)
  - Reemplaza un patrón por otro en una cadena. Por default reemplaza todos los patrones que se encuentren.
* - [subn](https://docs.python.org/3/library/re.html#re.Pattern.subn)(repl, string, count=0)
  - Realiza la misma operación que `sub()`, pero devuelva un `tuple` `(new_string, number_of_subs_made)`.
```

<br><br>

---
(objeto-match)=
## Objeto Match

Los objetos `Match` son objetos que son retornados por funciones como `re.match()` o `re.search()` o por métodos como `Pattern.match()` o `Pattern.search()`. En ellos está contenida la información de la primer coincidencia de un patrón. 


```{code-cell} python3
# Importar el módulo
import re

# Definir una cadena
X = "abc 123 xyz"

# Compilar un patrón
pattern = re.compile(r"\d+")

# Buscar el patrón en X
M = pattern.search(X)

# Imprimir el tipo de M
print(type(M), end="\n"*2)

# Imprimir el patrón encontrado
print(M.group(0))
```

Posteriormente se pueden usar sus atributos y métodos para recuperar información sobre el objeto, entre otras acciones.

<br>

---
### Atributos

A continuación se presenta una lista de los atributos de instancia de `Match`. 

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - [endpos](https://docs.python.org/3/library/re.html#re.Match.endpos)
  - El valor de `endpos` que se pasó a `search()` o `match()` de un objeto `regex`.
* - [lastgroup](https://docs.python.org/3/library/re.html#re.Match.lastgroup)
  - El nombre del último grupo de captura coincidente, o `None` si el grupo no tienen un nombre, o si ningún grupo coincidió en absoluto.
* - [lastindex](https://docs.python.org/3/library/re.html#re.Match.lastindex)
  - El índice del último grupo de captura coincidente, o `None` si no hay grupo que coincidió en absoluto.
* - [pos](https://docs.python.org/3/library/re.html#re.Match.pos)
  - El valor de `pos` que se pasó a los métodos `search()` o `match()` de un objeto `regex`.
* - [re](https://docs.python.org/3/library/re.html#re.Match.re)
  - Retorna el objeto `regex` (el patrón) cuyo `match()` o `search()` produjo esta instancia de `match`.
* - [string](https://docs.python.org/3/library/re.html#re.Match.string)
  - La cadena pasada a `match()` o `search()`.
```

<br>

---
### Métodos

A continuación se presenta una lista de los métodos de instancia de `Match`. 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [end](https://docs.python.org/3/library/re.html#re.Match.start)([group])
  - Retorna la posición en la cadena, donde termina la coincidencia.
* - [expand](https://docs.python.org/3/library/re.html#re.Match.expand)(template)
  - Devuelve la cadena obtenida al hacer sustitución usando _backslash_ en la plantilla de cadena `template`, como lo hace el método `sub()`.
* - [group](https://docs.python.org/3/library/re.html#re.Match.group)([group1, ...])
  - Devuelve uno o más subgrupos de la coincidencia.
* - [groupdict](https://docs.python.org/3/library/re.html#re.Match.groupdict)(default=None)
  - Devuelve un diccionario que contiene todos los subgrupos con nombre de la coincidencia, la _key_ es el nombre del subgrupo.
* - [groups](https://docs.python.org/3/library/re.html#re.Match.groups)(default=None)
  - Devuelve una tupla que contiene todos los subgrupos de la coincidencia.
* - [span](https://docs.python.org/3/library/re.html#re.Match.span)([group])
  - Para una coincidencia `m`, retorna la posición inicial y final de la primer coincidencia del patrón `(m.start(group), m.end(group))`.
* - [start](https://docs.python.org/3/library/re.html#re.Match.start)([group])
  - Retorna la posición en la cadena, donde empieza la coincidencia.
```

<br><br>

---
(caracteres-especiales)=
## Caracteres especiales

A continuación se presenta una lista de caracteres especiales para conformar las expresiones regulares. Para más información consultar la [documentacón](https://docs.python.org/3/library/re.html#regular-expression-syntax) de Python.

```{list-table}
:header-rows: 1
:name: table-caracteres-especiales

* - Carácter
  - Descripción
  - Ejemplo
* - `[]`
  - Un conjunto de caracteres. Se busca cualquier caracter contenido en el conjunto. Aquí no se pueden poner metaracteres ni secuencias especiales. Para representar rangos de letras y números usar a-z, A-Z y 0-9.
  - `[a-m]`: De la "a" a la "m". <br>
    `[^a-c]`: Cualquier carácter excepto "a", "b" o "c". En este caso `^` es negación. <br>
    `[#$&]`: Cualquier carácter "#", "$" o "&".
* - `\`
  - Para insertar {ref}`sec-especiales`. También para poder incluir caracteres como los caracteres especiales.
  - `\d` : Un número del 0-9. <br>
    `\.$`: La cadena termine con un punto. <br>
    `\$\d+`: La cadena contiene un símbolo "$" seguido de uno o más dígitos.
* - `.`
  - Cualquier carácter. Excepto una línea nueva. Para también incluir saltos de línea usar la flag `S` o `DOTALL`.
  - `he..o`: Cualquier cadena que empiece con "he", seguido de dos caracteres cualesquiera y termine con "o".
* - `^`
  - La cadena empiece con.
  - `^he`: La cadena mpiece con "he".
* - `$`
  - La cadena termine con.
  - `llo$`: La cadena ermine con "llo".
* - `*`
  - Cero o más ocurrencias del caracter a la izquierda.
  - `aix*`: El patrón "ai" seguido por cero o más "x".
* - `+`
  - Una o más ocurrencias del caracter a la izquierda.
  - `aix+`: El patrón "ai" seguido por una o más "x".
* - `?`
  - Cero o una ocurrencia del caracter a la izquierda.
  - `aix?`: El patrón "ai" seguido por cero o una "x".
* - `{}`
  - Número específico de ocurrencias del caracter a la izquierda.
  - `al{N}`: Buscar el patrón "a" seguido por _N_ "l". <br>
    `al{N,M}`: Buscar el patrón "a" seguido por mínimo _N_ "l" y máximo _M_ "l". Si se omite _M_ sería infinto y si se omite _N_ sería cero.
* - `|`
  - O
  - `falls|stays`: Buscar cualquiera de esos dos patrones.
* - `()`
  - Agrupar sub-patrones
  - `(a|b|c)xz`: Busque el patrón "a", "b" o "c" seguido de "xz". Indican el comienzo y fin de un grupo.
```

---
(sec-especiales)=
## Secuencias especiales

A continuación se presenta una lista de secuencias especiales que utilizan el símbolo "`\`" para conformar las expresiones regulares. Para más información consultar la [documentacón](https://docs.python.org/3/library/re.html#regular-expression-syntax) de Python.

```{list-table}
:header-rows: 1
:name: table-secuencias-especiales

* - Secuencia
  - Descripción
  - Ejemplo
* - `\A`
  - Retorna una coincidencia si los caracteres específicados están al principio de una cadena.
  - `r"\Athe"`: La cadena empiece con "the".
* - `\b`
  - Retorna una coincidencia si los caracteres específicados están presentes al principio o al final de una palabra de la cadena.
  - `r"\bain"`: Alguna palabra de la cadena empiece con "ain". <br>
    `r"ain\b"`: Alguna palabra de la cadena termine con "ain".
* - `\B`
  - Retorna una coincidencia si los caracteres específicados están presentes, pero NO están al princio o al final de las palabras de una cadena.
  - `r"\Bain"`: "ain" esté presente en la cadena, pero no al pincipio de ninguna palabra. <br>
    `r"ain\B"`: "ain" esté presente en la cadena, pero no al final de ninguna palabra.
* - `\d`
  - Representa un carácter numérico del 0-9.
  - `r"\d"`: La cadena contiene dígitos (0-9).
* - `\D`
  - Representa un caracter que no sea numérico.
  - `r"\D"`: La cadena no contiene dígitos.
* - `\s`
  - Representa una caracter que sea un espacio en blanco (`\n`, `\t`, `' '`, etc.).
  - `r"\s"`: La cadena contiene espacios en blanco.
* - `\S`
  - Representa una caracter que no sea un espacio en blanco (`\n`, `\t`, `' '`, etc.).
  - `r"\S"`: La cadena no contiene espacios en blanco.
* - `\w`
  - Representa un caracter que sea a-Z, 0-9 o guión bajo "_".
  - `r"\w"`: La cadena contiene caracteres de a-Z, 0-9 o "_".
* - `\W`
  - Representa un caracter que no sea a-Z, 0-9 o guión bajo "_".
  - `r"\W"`: La cadena no contiene caracteres de a-Z, 0-9 o "_".
* - `\Z`
  - Retorna una coincidencia si los caracteres específicados están al final de una cadena
  - `r"/Zend"`: La cadena termina con "end".
```