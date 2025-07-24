# _None_, _bool_ y Numéricos

En esta sección se presentan los tipos de datos `None`, `bool`, `int`, `float` y `complex`.

:::{note}
Para más información visitar la documentación de Python:
- [None](https://docs.python.org/3/library/constants.html#None).
- [bool](https://docs.python.org/3/library/stdtypes.html#boolean-type-bool)
- [Numéricos](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex).
:::

<br/>

---
(tipos-none)=
## None

`None` es una constante especial en Python que representa un valor nulo. Las principales características de este tipo de dato son:
- Es la única instancia de la clase `NoneType`.
- Es el valor retornado por default por funciones que no retornan nada.
- Es una valor inmutable, es decir, que no se puede modificar de ninguna manera.
- Algunos casos de uso cómunes son:
    - Como argumento por default de funciones.
    - Para inicializar variables.
    - Para indicar explícitamente la ausencia de valor.
- Para verificar que un valor es `None` se debe de usar el operador `is`. No se puede usar operadores de comparación como `==` o `!=`. 

```python
# Verificar que variable sea un valor nulo
x is None

# Verificar que variable no sea un valor nulo
x is not None
```

<br>

---
(tipos-bool)=
## Bool

`bool` es un tipo de dato que únicamente puede tomar las palabras reservadas `True` y `False`.
- Los valores booleanos tienen valores numéricos equivalentes donde `True` es igual a 1 y `False` es igual a cero.
- También existen expresiones booleanas que retornan un valor booleano y normalmente son resultado de alguna comparación con {ref}`built-in-operadores-comparacion`, {ref}`built-in-operadores-membresia` o {ref}`built-in-operadores-identidad` y que junto con los {ref}`built-in-operadores-bool` pueden formar expresiones más complejas. 

```python
# Definir varible como un valor booleano
x = True

# Definir varible como un valor booleano
y = False

# Expresión que retorna un valor booleano
z = 5 > 10 # Retorna False

# Operadores booleanos
(z or not y) and x # Retorna True
```

La función `bool()` convierte cualquier objeto en `True` o `False`. Casi todos los objetos son considerados `True` a excepción de unos cuantos. Los objetos que retornan `False` al utilizarlos con la función `bool()` son:
- `False`: Palabra reservada `False`.
- `None`: Palabra reservada `None`.
- `0`: Número cero entero.
- `0.0`: Número cero flotante.
- `""`: Cadena vacía.
- `()`: Tuple vacío.
- `[]`: Lista vacía.
- `{}`: Diccionario vacío.

**Ejemplo**:

```python
# Retorna False
bool([])

# Retorna True
bool(10)
```

<br/>

---
(tipos-numericos)=
## Númericos

Existen tres tipos de datos numéricos en Python `int`, `float` y `complex`. 

<br/>

---
### Int y Float

Son los dos tipos _built-in_ numéricos de Python.
- `int`: Corresponde a los números enteros. Están limitados solo por la memoria disponible en la computadora.
- `float`: Corresponde a los números con decimales.
    - Para que un valor sea `float` se debe de agregar un punto `.` al número, sino lo incluye ya, por ejemplo:

```python
# Tipo de dato "int"
2

# Tipo de dato "float"
2.
```

Se pueden usar las funciones `int()` y `float()` para convertir otros objetos en números enteros o flotantes, respectivamente, por ejemplo, para convertir valores `bool` o `str` a números. Además en la función `int()` se puede proveer del argumento _base_ para indicar la base del número que pase.

:::{caution}
Tener en cuenta las siguientes características al realizar operaciones entre diferentes tipos:
- `int` y `float`: Implícitamente los valores `int` se convertirán a `float` y el resultado será `float`.
    - En el caso de la división siempre se retorna `float` incluso si ambos operandos son `int`. 
- `bool` con `int` o `float`: Implícitamente los valores `bool` se convierten a `int` o `float` según sea el caso.
- `str` con `int` o `float`: No se realiza una conversión implícita entre `str` y los tipos numéricos por lo que se arroja un error `TypeError`.
:::

Es posible usar guión bajo como separador de miles para escribir cifras muy grandes y facilitar la lectura de los números:

```python
# Escribir entero con separador de miles
x = 1_345_234_432 # Equivale a: 1345234432

```

<br/>

#### Notación Científica

Es posible indicar los números en notación científica. Ejemplos:

```python
# Formas de representar el número 1000.0
1e3
1E3 

# Forma de representar el número 0.001
1e-3
```

<br/>

#### Valor Infinito

Se pueden crear valores que representen el infinito con:

```python
# Infinito positivo
float("inf")

# Infinito negativo
float("-inf")
```

```{note}
Otras forma de crear un valor que represente el infinito:
- `math.inf`: Paquete built-it `math`.
- `numpy.inf`: Paquete `numpy`.
```

<br/>

#### NaN - Not a Number

Se puede crear un `NaN` ("_Not a Number_") con:
```python
# Not-a-Number
float("NaN")
```

```{note}
Otras forma de crear un valor que represente un "Not a Number":
- `math.nan`: Paquete built-it `math`.
- `numpy.nan`: Paquete `numpy`.
```

<br/>

#### Métodos de int

Métodos de la clase `int`.

:::{caution}
Para usar métodos de la clase `int` directamente sobre una literal se debe de poner la literal entre paréntesis, de la siguiente manera: <br/> `(10).is_integer()`
:::

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [as_integer_ratio](https://docs.python.org/3/library/stdtypes.html#int.as_integer_ratio)()
  - Devuelve un par de números enteros cuya razón es igual al entero original y tiene un denominador positivo. La razón entera de los números enteros es siempre el entero como numerador y 1 como denominador.
* - [bit_count](https://docs.python.org/3/library/stdtypes.html#int.bit_count)()
  - Devuelve la cantidad de unos en la representación binaria del valor absoluto del entero. Esto también se conoce como recuento de población.
* - [bit_length](https://docs.python.org/3/library/stdtypes.html#int.bit_length)()
  - Devuelve la cantidad de bits necesarios para representar un número entero en binario, excluyendo el signo y los ceros iniciales.
* - [from_bytes](https://docs.python.org/3/library/stdtypes.html#int.from_bytes)(bytes, byteorder='big', *, signed=False)
  - Método de clase. Devuelve el entero representado por la matriz de bytes dada.
* - [is_integer](https://docs.python.org/3/library/stdtypes.html#int.is_integer)()
  - Devuelve `True` siempre. Existe para compatibilidad con `float.is_integer()`.
* - [to_bytes](https://docs.python.org/3/library/stdtypes.html#int.to_bytes)(length=1, byteorder='big', *, signed=False)
  - Devuelve una matriz de bytes que representan un entero.
```

<br/>

#### Métodos de float

Métodos de la clase `float`.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [as_integer_ratio](https://docs.python.org/3/library/stdtypes.html#float.as_integer_ratio)()
  - Devuelve un par de números enteros cuya razón es exactamente igual al número flotante original. La razón está en términos mínimos y tiene un denominador positivo. Genera `OverflowError` en valores infinitos y un `ValueError` en _NaN_.
* - [fromhex](https://docs.python.org/3/library/stdtypes.html#float.fromhex)(s)
  - Método de clase para devolver el valor flotante representado por una cadena hexadecimal _s_. La cadena _s_ puede tener espacios en blanco iniciales y finales.
* - [hex](https://docs.python.org/3/library/stdtypes.html#float.hex)()
  - Devuelve una representación de un número de punto flotante como una cadena hexadecimal. Para números de punto flotante finitos, esta representación siempre incluirá un _0x_ inicial y un _p_ y exponente finales.
* - [is_integer](https://docs.python.org/3/library/stdtypes.html#float.is_integer)()
  - Devuelve `True` si la instancia flotante es finita con valor integral y `False` en caso contrario.
```

<br/>

---
### Complex

Corresponde a los números complejos, para poder utilizarlo se agrega una jota `j` al final del número. Ejemplos:

```python
# Un número imaginario.
0+1j 

# Un número complejo.
3+5j
```

<br/>

#### Métodos de complex

Métodos de la clase `complex`.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [conjugate](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)()
  - Conjugado del número complejo.
```