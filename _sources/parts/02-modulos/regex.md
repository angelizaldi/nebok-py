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

# Regex

Una “expresión regular” es una secuencia de caracteres para identificar y extraer patrones en cadenas. Para usar _regular expressions_ es necesario importar el módulo `re`.
```python
# Importar el módulo
import re
```

Un patrón en expresiones regulares se conforma de:
- **Texto**: Coincide tal cual como se indique en la cadena.
- {ref}`caracteres-especiales` y {ref}`sec-especiales`: Son metacaracteres que significan algo en especial. Visitar sus respectivas secciones para más información.

Si una o más partes de la cadena coinciden con el patrón entonces se dice que hay un "_Match_".

:::{attention}
Para un tratado más completo de este módulo visitar la [documentación](https://docs.python.org/3/library/re.html) de Python.
:::

<br>

---
## Buscar patrones usando regex

Para buscar un patrón usando _regular expressions_ se puede hacer principalmente de dos formas.

:::{attention}
Los patrones de expresiones regulares se indican utilizando cadenas _crudas_ ({ref}`str-raw`), es decir, como `r'regex_pattern'`.
:::


**1.** Usar directamente las {ref}`funciones-regex` para buscar patrones. Por ejemplo `re.search()`, `re.match()` o `re.findall()`. En este caso se debe de proveer tanto del patrón a buscar, como de la cadena donde se va a buscar el patrón. Ejemplo:

:::{note}
Las principales funciones son:
- `re.search()`: Retorna un objeto `Match` con la primer coincidencia.
- `re.match()`: Retorna un objeto `Match` con la primer coincidencia si el patrón está al inicio de la cadena.
- `re.findall()`: Retorna `list` con todas las coincidencias.

Hay más, revisar {ref}`funciones-regex`.
:::

```{code-cell} python3
# Importar el módulo
import re

# Definir una cadena
X="abc 123 xyz"

# Buscar un patrón en la cadena
result=re.search(r"\d+", X)

# Imprimir resultado
print(result.group(0))
```

**2.** Usar la función `re.compile()` para compilar un patrón y retornar un objeto `Pattern` y posteriormente usar los {ref}`pattern-metodos` de `Pattern` para buscar coincidencias como `Pattern.search()`, `Pattern.match()` o `Pattern.findall()`. En este caso, el patrón a buscar se indica en la función `re.compile()` y la cadena donde se va a buscar se indica como argumento de los métodos de `Pattern`. Esta opción es particularmente útil si se utilizará en múltiples ocasiones un mismo patrón. Ejemplo:

:::{note}
Las principales métodos son:
- `Pattern.search()`: Retorna un objeto `Match` con la primer coincidencia.
- `Pattern.match()`: Retorna un objeto `Match` con la primer coincidencia si el patrón está al inicio de la cadena.
- `Pattern.findall()`: Retorna `list` con todas las coincidencias.

Hay más, revisar {ref}`pattern-metodos`.
:::

```{code-cell} python3
# Importar el módulo
import re

# Definir una cadena
X="abc 123 xyz"

# Compilar un patrón
pattern=re.compile(r"\d+")

# Buscar el patrón en X
result=pattern.search(X)

# Imprimir el patrón encontrado
print(result.group(0))
```

<br><br>

---
## Búsqueda _greedy_ y _non-greedy_

Se refiere a la manera como se realiza la búsqueda del patrón, cuando se utilizan los cuantificadores `*`, `+`, `?` o `{min, max}` en un patrón, para ello se agrega un `?` extra.

- **Greedy**: Coincide la mayor cantidad de caracteres posibles. Retorna el _match_ más largo. Los cuantificadores `*`, `+`, `?` o `{min, max}` son greedy por default.
- **Non-greedy**: Coincide la menor cantidad de caracteres posibles. Retorna el _match_ más corto. Se agrega el metacaracter `?`.

La forma como funciona es que los caracteres especiales `*`, `+`, `?` o `{min, max}` tienen dos posibles opciones. Tomando a `+` como ejemplo, significa "**una vez** o **más veces** el caracter a la izquierda". Por default se buscará que sea **más veces**, pero si se agrega un `?` entonces se forzará a que sea **una vez**. De tal forma que tenemos:
- `+`: Más de una vez.
- `+?`: Una vez.
- `*`: Más de una vez.
- `*?`: Cero veces.
- `{min, max}`: _max_ veces.
- `{min, max}?`: _min_ veces.
- `?`: Una vez.
- `??`: Cero veces.

<br>

***Ejemplo***: En este ejemplo se puede observar cómo se modifica la búsqueda de patrones dependiendo de si es una búsqueda _greedy_ o _non-greedy_. El patrón que se está buscando son caracteres numéricos.

```{code-cell} python3
# Importar el módulo
import re

# Definir la cadena
cadena="123abc"

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

La funcionalidad general cuando solo se captura un solo grupo depende de la función/método que se use:

**1.** Si se usa `re.search()` o `Pattern.search()` se recupera solo la primer coincidencia que satisface el patrón en la cadena (ambos retornan un objeto _Match_). 

El método `Match.group()` retorna el grupo capturado, el cual recibe como argumento un número entero, tener en cuenta lo siguiente al definir el argumento:
- Si no se indica ningún argumento equivale a usar cero _0_.
- Si se indica cero _0_ entonces se retorna toda la primer coincidencia con el patrón, no solo el grupo, sino todo el patrón.
- Si se indica uno _1_ entonces se retorna solo la primer coincidencia del grupo.


```{code-cell} python3
# Importar el módulo
import re

# Definir una cadena
X="abc 123 #&@ 789"

# Compilar el patrón definiendo un grupo
result=re.search(r"(\d+)", X)

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
X="abc 123 #&@ 789"

# Compilar el patrón definiendo un grupo
result=re.search(r"\w+ (\d+)", X)

# Recuperar el patrón
print(f"Patrón: {result.group(0)}", end="\n"*2)

# Recuperar el grupo
print(f"Grupo: {result.group(1)}")
```

**2.** Si se desea recuperar todas las coincidencias se puede usar la función `re.findall()` o el método `Pattern.findall()`.

```{code-cell} python3
# Importar el módulo
import re

# Definir una cadena
X="abc 123 #&@ 789"

# Compilar el patrón definiendo un grupo
result=re.findall(r"(\d+)", X)

# Recuperar el patrón
print(f"Resultado de r\'(\d+)\': {result}", end="\n"*2)

# Compilar el patrón definiendo un grupo
result2=re.findall(r"\w+ (\d+)", X)

# Recuperar el patrón
print(f"Resultado de r\'\w+ (\d+)\': {result2}")
```
- _result_ retorna dos coincidencias porque hay dos subcadenas en _X_ que representan uno o más dígitos.
- _result2_ retorna solo una coincidencia porque solo hay una subcadena que representa uno o más dígitos y que están después de uno o más caracteres alfabéticos, seguido de un espacio en blanco, lo cual solo se satisface con "123".

<br>

### Capturando múltiples grupos

Es posible recuperar dos o más grupos. Tener en cuenta que para recuperar un grupo específico se debe indicar su índice en el mismo orden en el que aparece en el patrón. El comportamiento dependerá de la función/método que se use:

**1.** Si se usa `re.search()` o `Pattern.search()` se recupera solo las primeras coincidencias que satisfacen el patrón en la cadena (ambos retornan un objeto _Match_). 

El método `Match.group()` retorna el grupo capturado, el cual recibe como argumento un número entero, tener en cuenta lo siguiente al definir el argumento:
- Si no se indica ningún argumento equivale a usar cero _0_.
- Si se indica cero _0_ entonces se retorna la coincidencia del primer grupo.
- Si se indica uno _1_ entonces se retorna la coincidencia del segundo grupo.
- Aplicar la misma lógica anterior para recuperar coincidencias del resto de los grupos.

**Ejemplo**: 

En este ejemplo se busca un patrón que consista de una palabra, un espacio y un conjunto de números, únicamente se capturará la primer coincidencia y posteriormente se recuperan los grupos capturados con el método `.group()`.

```{code-cell} python3
# Importar el módulo
import re

# Definir una cadena
X="abc 123 #&@ xyz 789"

# Compilar el patrón definiendo un grupo
result=re.search(r"(\w+) (\d+)", X)

# Recuperar el patrón buscado
print(f"Patrón: {result.group(0)}", end="\n"*2)

# Recuperar el grupo 1
print(f"Grupo 1: {result.group(1)}", end="\n"*2)

# Recuperar el grupo 2
print(f"Grupo 2: {result.group(2)}")
```
- Notar que para recuperar cada grupo se debe usar `result.group(ind)` con el _índice_ apropiado.

**2.** Si se usa `re.findall()` o `Pattern.findall()` entonces se recupera una lista de tuplas con las coindidencias. En el siguiente ejemplo se capturan todas las coincidencias de palabras, seguidas por números, separados por un espacio:

```{code-cell} python3
# Importar el módulo
import re

# Definir una cadena
X="abc 123 #&@ xyz 789"

# Compilar el patrón definiendo dos grupos
result=re.findall(r"(\w+) (\d+)", X)

# Recuperar los grupos
print(f"Resultado de r\'\w+ (\d+)\': {result}")
```
- Notar que se retorna una lista con dos elementos, porque se encontraron dos coincidencias, además cada elemento es un `tuple` de dos elementos, porque se están capturando dos grupos en cada coincidencia.

### Grupos no capturados

Es posible indicar un grupo que no debe de ser capturado, pero sí debe de haber una coincidencia, esto es útil para grupos que no pretende recuperar su valor posteriormente. Para ello al inicio del grupo se debe de usar `?:`.

**Ejemplo**: 

En este ejemplo se busca un patrón que consista de una palabra, un espacio y un conjunto de números, sin embargo únicamente se captura al grupo del conjunto de número.

```{code-cell} python3
# Importar el módulo
import re

# Definir una cadena
X="abc 123 #&@ xyz 789"

# Compilar el patrón definiendo un grupo
result=re.search(r"(?:\w+) (\d+)", X)

# Recuperar el patrón buscado
print(f"Patrón: {result.group(0)}", end="\n"*2)

# Recuperar el grupo 1
print(f"Grupo 1: {result.group(1)}", end="\n"*2)
```
- Notar que debe haber una coincidencia con el primer grupo, pero no es capturado y por lo tanto no se puede recuperar.

:::{tip}
Un caso común de uso de grupos no capturados es cuando un patrón tiene dos posibles variantes:

<code>
X="abc 123%  xyz 789#"
result=re.findall(r"(\d+)(?:%|#)", X)
</code>

En este ejemplo se retornarían ambos números _123_ y _789_, independientemente de si terminan con _%_ o _#_.
:::

### Grupos con nombres

Es posible asignarle un nombre a un grupo utilizaldo <code>?P\<<i>group_name</i>></code>. Posteriormente se puede recuperar la coincidencia con el nombre.

**Ejemplo**: 

En este ejemplo se busca un patrón que consista de una palabra, un espacio y un conjunto de números, se capturan las coincidencias y se nombran _letters_ y _numbers_ respectivamente, para después recuperar los grupos capturados por su nombre.

```{code-cell} python3
# Importar el módulo
import re

# Definir una cadena
X="abc 123 #&@ xyz 789"

# Compilar el patrón definiendo un grupo
result=re.search(r"(?P<letters>\w+) (?P<numbers>\d+)", X)

# Recuperar el patrón buscado
print(f"Patrón: {result.group('letters')}", end="\n"*2)

# Recuperar el grupo 1
print(f"Grupo 1: {result.group('numbers')}", end="\n"*2)
```
- Notar que se recuperó el grupo con el nombre que se le dio.

:::{tip}
Un caso común de uso de grupos no capturados es cuando un patrón tiene dos posibles variantes:

<code>
X="abc 123%  xyz 789#"
result=re.findall(r"(\d+)(?:%|#)", X)
</code>

En este ejemplo se retornarían ambos números _123_ y _789_, independientemente de si terminan con _%_ o _#_.
:::

<br>

### Backreferences

En un patrón se puede hacer referencia a un grupo dentro de ese mismo patrón. Existen tres meneras para hacer referencia a grupos:
- Con `\1`, `\2`, ...: Se hace referencia al grupo 1, grupo 2, etc.
- Con su nombre usando <code>(?P=<i>group_name</i>)</code>: Se hace refencia al grupo con el nombre _group_name_. Es necesario usar los parentesis para evitar un error. En la función `re.sub(pattern, repl)`, solo se puede como argumento de _pattern_. Como argumento de _repl_ se debe usar <code>\g\<<i>group_name</i>></code>.
- Con su nombre usando <code>\g\<<i>group_name</i>></code>: Se hace refencia al grupo con el nombre _group_name_. **Importante**: Esta notación solo se usa para hacer reemplazos con la función `re.sub(pattern, repl)`, como argumento de _repl_. Como argumento de _pattern_ se debe usar <code>(?P=<i>group_name</i>)</code>.

**Ejemplo**: 

En este ejemplo se busca un patrón que consista de una palabra, un espacio, un conjunto de números, un espacio y exactamente la misma palabra previamente encontrado. Es decir, solo habrá una coincidencia si hay un conjunto de números entre la misma palabra en ambos extremos.

```{code-cell} python3
# Importar el módulo
import re

# Definir una cadena
X="abc 123 xyz 789 xyz"

# Compilar el patrón definiendo un grupo
result=re.search(r"(\w+) (\d+) \1", X)

# Recuperar el patrón buscado
print(f"Patrón: {result.group(0)}", end="\n"*2)

# Recuperar el grupo 1
print(f"Grupo 1: {result.group(1)}", end="\n"*2)

# Recuperar el grupo 2
print(f"Grupo 2: {result.group(2)}")
```
- Notar que se definió el patrón con la coincidencia del primer grupo, de tal forma que el patrón aplicado en realidad fue `(xyz) (\d+) xyz`, pero lo anterior dependió de que hubiera digitos entre las mismas letras a ambos extremos, lo cual lo se satisface con _xyz_.
- Lo anterior también se hubiera conseguido con nombre usando: `result=re.search(r"(?P<letters>\w+) (\d+) (?P=letters)", X)`

### Lookaround

Es una estrategia para verificar que se cumpla cierta condición antes o después de un patrón, donde esas condiciones son otros patrones. Estas condicionales se definen como un grupo pero no serán capturados.
- **Antes** (_look-ahead_):
    - Positiva: Verifica que exista un subpatrón antes del patrón principal, se utiliza la sintaxis: <code>(?<=<i>pattern</i>)</code>
    - Negativa: Verifica que no exista un subpatrón antes del patrón principal, se utiliza la sintaxis: <code>(?<!<i>pattern</i>)</code>
- **Después**  (_look-behind_):
    - Positiva: Verifica que exista un subpatrón después del patrón principal, se utiliza la sintaxis: <code>(?=<i>pattern</i>)</code>
    - Negativa: Verifica que no exista un subpatrón después del patrón principal, se utiliza la sintaxis: <code>(?=<i>pattern</i>)</code>

```python
# Look-ahead positivo
pattern=r'main_pattern(?=sub_pattern)'

# Look-ahead negativo
pattern=r'main_pattern(?!sub_pattern)'

# Look-behind positivo
pattern=r'(?<=sub_pattern)main_pattern'

# Look-behind negativo
pattern=r'(?<!sub_pattern)main_pattern'
```

**Ejemplo**: 

En este ejemplo se busca un patrón que consista de una palabra seguida de un espacio y un conjunto de números.

```{code-cell} python3
# Importar el módulo
import re

# Definir una cadena
X="abc 123 opq 789 xyz"

# Compilar el patrón definiendo un grupo
result=re.search(r"\w+(?=\s\d+)", X)

# Recuperar la coincidencia
print(f"Patrón: {result.group(0)}")
```
- Notar que la primer coincidencia que cumple el patrón es _abc_, aunque también _opq_ la cumple.
- Otras alternativas con esa misma cadena y _lookaround_:
    -  Palabra **no** seguida de un espacio y un conjunto de números: `re.search(r"\w+(?!\s\d+)", X) -> 'xyz'`
    -  Palabra precedida de un conjunto de números y un espacio: `re.search(r"(?<=\d+\s)\w+", X) -> 'opq'`
    -  Palabra **no** precedida de un conjunto de números y un espacio: `re.search(r"(?<!\d+\s)\w+", X) -> 'abc'`

<br>

---
## Sustituyendo patrones

En esta sección se cubre lo básico de cómo usar la función `re.sub()` para reemplazar patrones en una cadena por otros. La función `re.sub()` reemplaza todos los patrones encontrados por otra expresión, se puede limitar el número de reemplazos con el parámetro _count_.

En su forma más simple reemplaza todas las coincidencias por otra cadena. Por ejemplo, reemplazar todos las subcadenas que sean dígitos por un "-".

```{code-cell} python3
# Importar el módulo
import re

# Definir una cadena
X="abc 123 #&@ xyz 789"

# Reemplazar el patrón
result=re.sub(r"\d+", "-", X)

# Imprimir resultado
print(result)
```

Es posible recuperar la coincidencia usando grupos para incluirla en el reemplazo utilizando `\1` para recuperar el primer grupo, `\2` para el segundo grupo, etc. Por ejemplo, reemplazar todas las subcadenas que sean dígitos por la misma subcadena entre paréntesis

```{code-cell} python3
# Importar el módulo
import re

# Definir una cadena
X="abc 123 #&@ 789"

# Reemplazar el patrón 
result=re.sub(r"(\d+)", r"(\1)", X)

# Imprimir resultado
print(result)
```
- Un mismo grupo se puede utilizar más de una vez en el reemplazo. Por ejemplo, si en lugar de usar `r"(\1)"` se usará `r"(\1-\1)"`, entonces `123` se reemplazaría por `(123-123)`.


Tener en cuenta que lo que se reemplaza es toda la coincidencia, no solo el grupo. En el siguiente ejemplo el patrón es uno o más caracteres alfabéticos, un espacio y uno o más dígitos y se cambiarán el orden en que aparece el patrón.

```{code-cell} python3
# Importar el módulo
import re

# Definir una cadena
X="abc 123 xyz 789"

# Reemplazar el patrón
result=re.sub(r"(\w+) (\d+)", r"\2 \1", X)

# Imprimir resultado
print(result)
```
- En este ejemplo hay dos coincidencias `abc 123` y `xyz 789`, por lo tanto lo que se intercambia es el orden en cada coincidencia.

Finalmente, es posible usar una función para reemplazar la coincidencia, esta función recibe como parámetro un objeto _Match_. En el siguiente ejemplo se busca uno o más caracteres alfabéticos y se reemplaza por la misma cadena pero en mayúsculas.

```{code-cell} python3
# Importar el módulo
import re

# Definir una cadena
X="abc 123 #&@ 789 zyx"

# Reemplazar el patrón "abc"
result=re.sub(r"(\w+)", lambda match: match.group().upper(), X)

# Imprimir resultado
print(result)
```
- En este ejemplo hay dos coincidencias con el patrón `abc` y `zxy`.
- En este ejemplo en particular usar `match.group()` equivale a usar `match.group(0)` y `match.group(1)`.

<br>

---
## Flags

A continuación se presenta una lista de _flags_ para modificar el comportamiento de las {ref}`funciones-regex` o de los métodos de objetos como {ref}`objeto-match` u {ref}`objeto-pattern`. Las _flags_ se ponen como argumentos de las funciones como `re.search()`, `re.match()` o `re.find_all()` o de los métodos del objeto `Pattern`.

:::{warning}
La mayoría de las _flags_ tienen 2 posibles formas de representarlas, en la tabla se presentan ambas formas separadas por `|`, pero solo se debe usar una de las dos formas.
:::


```{list-table}
:header-rows: 1

* - Flag
  - Descripción
* - [A | ASCII] (https://docs.python.org/3/library/re.html#re.A)
  - Hace que `\w`, `\W`, `\b`, `\B`, `\d`, `\D`, `\s` y `\S` realicen solo coincidencias ASCII en lugar de coincidencias Unicode completas.
* - [DEBUG](https://docs.python.org/3/library/re.html#re.DEBUG)
  - Muestra información de depuración sobre la expresión compilada.
* - [I | IGNORECASE](https://docs.python.org/3/library/re.html#re.I)
  - Indica que se realicen las coincidencias sin distinción entre mayúsculas y minúsculas.
* - [L | LOCALE](https://docs.python.org/3/library/re.html#re.L)
  - Hace que `\w`, `\W`, `\b`, `\B` y coincidencias sin distinción entre mayúsculas y minúsculas dependientes de la configuración regional actual.
* - [M | MULTILINE](https://docs.python.org/3/library/re.html#re.M)
  - Hace que el carácter de patrón '^' coincide con el principio de la cadena y al comienzo de cada línea (inmediatamente después de cada salto de línea); y el carácter de patrón '$' coincide al final de la cadena y al final final de cada línea (inmediatamente antes de cada salto de línea).
* - [NOFLAG](https://docs.python.org/3/library/re.html#re.NOFLAG)
  - Indica que no se aplique ningúna flag, el valor es 0.
* - [S | DOTALL](https://docs.python.org/3/library/re.html#re.S)
  - Indica que el carácter especial '.' coincida con cualquier carácter, incluido un nueva línea (`\n`).
* - [U | UNICODE](https://docs.python.org/3/library/re.html#re.S)
  - Esta _flag_ no tiene efecto alguno.
* - [X | VERBOSE](https://docs.python.org/3/library/re.html#re.X)
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
X="abc 123 ABC 456 AbC"

# Encontrar el patrón "abc"
result=re.findall(r"abc", X)

# Imprimir resultado
print(f"Resultado de buscar \'abc\': {result}")

# Ignorando minúsculas y mayúsculas
result2=re.findall(r"abc", X, re.I)

# Imprimir resultado
print(f"Resultado de buscar \'abc\' con re.I: {result2}")
```

<br><br>

---
(funciones-regex)=
## Funciones

A continuación se presenta una lista de funciones del módulo `re`.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [compile](https://docs.python.org/3/library/re.html#re.compile)(pattern, flags=0)
  - Compila un patrón de expresión regular en un objeto de expresión regular, que se puede usar para hacer coincidir usando `match()`, `search()` y otros métodos.
* - [escape](https://docs.python.org/3/library/re.html#re.escape)(pattern)
  - Para indicar que se ignores caracteres especiales en el patrón.
* - [findall](https://docs.python.org/3/library/re.html#re.findall)(pattern, string, flags=0)
  - Devuelve todas las coincidencias no superpuestas del patrón en la cadena como `list`. Si no se encuentran coincidencias entonces devuélve una lista vacía. Cuando _pattern_ tiene grupos, retorma `list` de `tuples`, donde cada elemento del `tuple` es un grupo.
* - [finditer](https://docs.python.org/3/library/re.html#re.finditer)(pattern, string, flags=0)
  - Retorna un `iterator` que produce objetos _Match_ sobre todas las coincidencias que no se superponen para el patrón en la cadena.
* - [fullmatch](https://docs.python.org/3/library/re.html#re.fullmatch)(pattern, string, flags=0)
  - Si toda la cadena coincide con el patrón de expresión regular, devuelve un objeto _Match_ correspondiente. Retorna `None` si la cadena no coincide con el patrón.
* - [match](https://docs.python.org/3/library/re.html#re.match)(pattern, string, flags=0)
  - Retorna un objeto _Match_ si se encuentra un patrón al principio de una cadena. Retorna `None` si la cadena no coincide con el patrón.
* - [purge](https://docs.python.org/3/library/re.html#re.purge)()
  - Borra la caché de expresiones regulares.
* - [search](https://docs.python.org/3/library/re.html#re.search)(pattern, string, flags=0)
  - Retorna un objeto _Match_ si se encuentra un patrón en una cadena. Si hay más de una coincidencia, solo devolverá la información de la primera coincidencia.
* - [split](https://docs.python.org/3/library/re.html#re.split)(pattern, string, maxsplit=0, flags=0)
  - Divide la cadena por las ocurrencias del patrón. Si los paréntesis de captura son utilizado en el patrón, también se devuelve el texto de todos los grupos en el patrón como parte de la lista resultante.
* - [sub](https://docs.python.org/3/library/re.html#re.sub)(pattern, repl, string, count=0, flags=0)
  - Reemplaza un patrón por otro en una cadena. Por default reemplaza todos los patrones que se encuentren.
* - [subn](https://docs.python.org/3/library/re.html#re.subn)(pattern, repl, string, count=0, flags=0)
  - Realiza la misma operación que `sub()`, pero devuelva un `tuple` _(new_string, number_of_subs_made)_.
```

<br><br>

(objeto-pattern)=
## Objeto Regular Expression

Los objetos de expresión regular `Pattern` son objetos que son retornados por la función `re.compile()`. Estos objetos se pueden usar para buscar coincidencias.

<br>

---
### Crear un objeto Pattern

Para crear un objeto `Pattern` se debe de usar la función `re.compile()`, donde se indique la expresión regular a buscar.


```{code-cell} python3
# Importar el módulo
import re

# Crear el objeto
pattern=re.compile(r"$a\d*")

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

(pattern-metodos)=
### Métodos

A continuación se presenta una lista de los métodos de instancia de `Pattern`. 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [findall](https://docs.python.org/3/library/re.html#re.Pattern.findall)(string[, pos[, endpos]])
  - Devuelve todas las coincidencias no superpuestas del patrón en la cadena como `list`. Si no se encuentran coincidencias entonces devuélve una lista vacía. Cuando _pattern_ tiene grupos, retorma `list` de `tuple`, donde cada elemento del `tuple` es un grupo.
* - [finditer](https://docs.python.org/3/library/re.html#re.Pattern.finditer)(string[, pos[, endpos]])
  - Retorna un `iterator` que produce objetos _Match_ sobre todas las coincidencias que no se superponen para el patrón en la cadena.
* - [fullmatch](https://docs.python.org/3/library/re.html#re.Pattern.fullmatch)(string[, pos[, endpos]])
  - Si toda la cadena coincide con el patrón de expresión regular, devuelve un objeto _Match_ correspondiente. Retorna `None` si la cadena no coincide con el patrón.
* - [match](https://docs.python.org/3/library/re.html#re.Pattern.match)(string[, pos[, endpos]])
  - Retorna un objeto _Match_ si se encuentra un patrón al principio de una cadena. Retorna `None` si la cadena no coincide con el patrón.
* - [search](https://docs.python.org/3/library/re.html#re.Pattern.search)(string[, pos[, endpos]])
  - Retorna un objeto _Match_ si se encuentra un patrón en una cadena. Si hay más de una coincidencia, solo devolverá la información de la primera coincidencia.
* - [split](https://docs.python.org/3/library/re.html#re.Pattern.split)(string, maxsplit=0)
  - Divide la cadena por las ocurrencias del patrón. Si los paréntesis de captura son utilizado en el patrón, también se devuelve el texto de todos los grupos en el patrón como parte de la lista resultante.
* - [sub](https://docs.python.org/3/library/re.html#re.Pattern.sub)(repl, string, count=0)
  - Reemplaza un patrón por otro en una cadena. Por default reemplaza todos los patrones que se encuentren.
* - [subn](https://docs.python.org/3/library/re.html#re.Pattern.subn)(repl, string, count=0)
  - Realiza la misma operación que `sub()`, pero devuelva un `tuple` _(new_string, number_of_subs_made)_.
```

<br>

---
(objeto-match)=
## Objeto Match

Los objetos _Match_ son objetos que son retornados por funciones como `re.match()` o `re.search()` o por métodos como `Pattern.match()` o `Pattern.search()`. En ellos está contenida la información de la primer coincidencia de un patrón. 


```{code-cell} python3
# Importar el módulo
import re

# Definir una cadena
X="abc 123 xyz"

# Compilar un patrón
pattern=re.compile(r"\d+")

# Buscar el patrón en X
M=pattern.search(X)

# Imprimir el tipo de M
print(type(M), end="\n"*2)

# Imprimir el patrón encontrado
print(M.group(0))
```

Posteriormente se pueden usar sus atributos y métodos para recuperar información sobre el objeto, entre otras acciones.

<br>

---
### Atributos

A continuación se presenta una lista de los atributos de instancia de _Match_. 

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - [endpos](https://docs.python.org/3/library/re.html#re.Match.endpos)
  - El valor de _endpos_ que se pasó a `search()` o `match()` de un objeto `regex`.
* - [lastgroup](https://docs.python.org/3/library/re.html#re.Match.lastgroup)
  - El nombre del último grupo de captura coincidente, o `None` si el grupo no tienen un nombre, o si ningún grupo coincidió en absoluto.
* - [lastindex](https://docs.python.org/3/library/re.html#re.Match.lastindex)
  - El índice del último grupo de captura coincidente, o `None` si no hay grupo que coincidió en absoluto.
* - [pos](https://docs.python.org/3/library/re.html#re.Match.pos)
  - El valor de _pos_ que se pasó a los métodos `search()` o `match()` de un objeto `regex`.
* - [re](https://docs.python.org/3/library/re.html#re.Match.re)
  - Retorna el objeto `regex` (el patrón) cuyo `match()` o `search()` produjo esta instancia de _Match_.
* - [string](https://docs.python.org/3/library/re.html#re.Match.string)
  - La cadena pasada a `match()` o `search()`.
```

<br>

### Métodos

A continuación se presenta una lista de los métodos de instancia de _Match_. 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [end](https://docs.python.org/3/library/re.html#re.Match.start)([group])
  - Retorna la posición en la cadena, donde termina la coincidencia.
* - [expand](https://docs.python.org/3/library/re.html#re.Match.expand)(template)
  - Devuelve la cadena obtenida al hacer sustitución usando _backslash_ en la plantilla de cadena _template_, como lo hace el método `sub()`.
* - [group](https://docs.python.org/3/library/re.html#re.Match.group)([group1, ...])
  - Devuelve uno o más subgrupos de la coincidencia.
* - [groupdict](https://docs.python.org/3/library/re.html#re.Match.groupdict)(default=None)
  - Devuelve un diccionario que contiene todos los subgrupos con nombre de la coincidencia, la _key_ es el nombre del subgrupo.
* - [groups](https://docs.python.org/3/library/re.html#re.Match.groups)(default=None)
  - Devuelve una tupla que contiene todos los subgrupos de la coincidencia.
* - [span](https://docs.python.org/3/library/re.html#re.Match.span)([group])
  - Para una coincidencia _m_, retorna la posición inicial y final de la primer coincidencia del patrón `(m.start(group), m.end(group))`.
* - [start](https://docs.python.org/3/library/re.html#re.Match.start)([group])
  - Retorna la posición en la cadena, donde empieza la coincidencia.
```

<br><br>

(caracteres-especiales)=
## Caracteres especiales

A continuación se presenta una lista de caracteres especiales para conformar las expresiones regulares. 

:::{note} Para más información consultar la [documentacón](https://docs.python.org/3/library/re.html#regular-expression-syntax) de Python.
:::

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

<br/>

(sec-especiales)=
## Secuencias especiales

A continuación se presenta una lista de secuencias especiales que utilizan el símbolo "`\`" para conformar las expresiones regulares. 

:::{note} Para más información consultar la [documentacón](https://docs.python.org/3/library/re.html#regular-expression-syntax) de Python.
:::

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