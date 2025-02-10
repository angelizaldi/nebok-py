# Numpy

`numpy` es una librería que se utiliza principalmente para computo científico en Python. Contiene el objeto `ndarray` y una gran cantidad de funciones para operaciones matemáticas, álgebra lineal, estadística, manipulación de arrays, entre muchas otras. 

Para utilizar `numpy` es necesario instalarlo. Desde la terminal usar:
```
# Con pip
pip install numpy

# Con conda
conda install numpy
```

Una vez instalado se debe de importar
```python
# Importar numpy a la sesión activa
import numpy as np
```
- `np` es el nombre por convención.
- En este sitio se utilizará `np` como alias.

Para conocer la versión de `numpy` instalada usar:
```python
# Concer la versión de numpy instalada
np.__version__ 
```

<br/>

---
(numpy-tipos-datos)=
## Tipos de datos

`numpy` puede crear _arrays_ de los principales tipos _built-in_ de escalares en Python, sin embargo `numpy` extiende los tipos de datos escalares hasta 24. A continuación se enlistan los principales tipos numéricos.

:::{note}
El tipo por default en `numpy` es `np.double`.
:::

| Tipo de Dato | Clase de `numpy` | Código en Cadena | Descripción | Tipo _built-in_ de Python relacionado |
|--------------|--------------|------------------|----------------------------------|-----------|
| _int8_       | `np.byte`    | `'i1'`           | Entero de 8 bits (-128 a 127) | |
| _int16_      | `np.short`   | `'i2'`           | Entero de 16 bits (-32768 a 32767)| |
| _int32_      | `np.intc`   | `'i4'`           | Entero de 32 bits                | |
| _int64_      | `np.int_`   | `'i8'`           | Entero de 64 bits                | `int` |
| _uint8_      | `np.ubyte`   | `'u1'`           | Entero sin signo de 8 bits (0 a 255) |
| _uint16_     | `np.ushort`  | `'u2'`           | Entero sin signo de 16 bits (0 a 65535)|
| _uint32_     | `np.uintc`  | `'u4'`           | Entero sin signo de 32 bits       | |
| _uint64_     | `np.uint`  | `'u8'`           | Entero sin signo de 64 bits       | |
| _float16_    | `np.half` | `'f2'`           | Punto flotante de 16 bits         | |
| _float32_    | `np.single` | `'f4'`           | Punto flotante de 32 bits         | |
| _float64_    | `np.double` | `'f8'`           | Punto flotante de 64 bits         | `float` |
| _float128_    | `np.longdouble` | `'f16'`          | Punto flotante de 128 bits         | |
| _complex64_  | `np.csingle` | `'c8'`         | Número complejo de 64 bits        | |
| _complex128_ | `np.cdouble`| `'c16'`        | Número complejo de 128 bits       | `complex` |
| _complex256_ | `np.clongdouble`| `'c32'`        | Número complejo de 256 bits       | |

Además existen los siguientes otros tipos de datos:

| Clase de `numpy`    | Código en Cadena | Descripción                            | Tipo _built-in_ de Python relacionado |
|---------------------|------------------|----------------------------------------|---------|
| _np.str\__           | `'U'`            | Cadena _unicode_       | `str` |
| _np.bool_          | `'?'`            | Tipo booleano (`True` o `False`)       | `bool` |
| _np.bytes__         | `'b'`            | Tipo booleano (`True` o `False`)       | `bytes`
| _np.datetime64_     | `'M'`   | Fecha y hora                           | `datetime.datetime` |
| _np.timedelta64_    | `'m'`  | Diferencia entre dos fechas y horas    | `datetime.timedelta` |
| _np.object__        | `'O'`            | Objeto genérico (cualquier tipo de dato)| `object` |


:::{caution}
La gran mayoría de tipos en `numpy` tienen alias, por ejemplo `np.float_` es un alias de `np.double`, para revisar los alias visitar la [documentación](https://numpy.org/doc/stable/reference/arrays.scalars.html#built-in-scalar-types) de `numpy`, particularmente la sección de [Otros alias](https://numpy.org/doc/stable/reference/arrays.scalars.html#sized-aliases).
:::

:::{important}
Para una lista completa visitar la [documentación](https://numpy.org/doc/stable/reference/arrays.scalars.html) de `numpy`.
:::

<br/>

---
### Crear escalares

Es posible crear escalares de los tipos de datos de `numpy`. Para ello se puede usar cualquiera de las clases enlistadas anteriormente y un valor válido correspondiente a la clase:
```python
# Ejemplo de escalar numérico
np.single(3.14) # Opción con la clase
np.float32(3.14) # Opción con el alias de la clase

# Ejemplo de escalas de cadena
np.str_("Hola mundo!")

# Ejemplo de escalar booleano
np.bool_(True)

# Ejemplo de escalar de fecha y tiempo
np.datetime64('2000-01-01')
```
- Se puede usar tanto las clases como sus alias para crear los escalares.

---
(numpy-tipo-datos-array)=
### Indicar el tipo de dato de un _array_

Se puede usar la función `np.array()` junto con el parámetro _dtype_ asignado a una clase del escalar, su alias o su código para indicar el tipo de dato, como argumento se debe de pasar un valor válido correspondiente al tipo de dato indicado:

:::{tip}
La función `np.array()` no es la única que acepta el parámetro _dtype_, otras {doc}`Funciones <creacion-arrays>` como `np.arange()` también lo admiten y es útil para crear rangos de fechas.
:::

```python
# Ejemplo de array numérico
np.array([3.14, 3.15], dtype=np.single) # Opción con la clase
np.array([3.14, 3.15], dtype=np.float32) # Opción con el alias de la clase
np.array([3.14, 3.15], dtype='f') # Opción con el código de la clase

# Ejemplo de array de cadenas
np.array(["Hola", "mundo!"], dtype=np.str_)
np.array(["Hola", "mundo!"], dtype='U')

# Ejemplo de array booleano
np.array([True, False], dtype=np.bool)
np.array([True, False], dtype=np.bool_)
np.array([True, False], dtype='?')

# Ejemplo de array de fechas y tiempo
np.array(['2000-01-01', '2000-01-02'], dtype=np.datetime64)
np.array(['2000-01-01', '2000-01-02'], dtype='datetime64[D]')
np.array(['2000-01-01', '2000-01-02'], dtype='M')
```

--- 
### Datetimes y Timedeltas

En los tipos _np.datetime64_ y _np.timedelta64_ se pueden indicar la unidad en la que están los datos, tomar en cuenta lo siguiente:
- `np.datetime64`:
    - Representa un desfase desde 1970-01-01 00\:00:00.
    - Se puede definir de las siguientes maneras:
        - Como un número (es necesario indicar una unidad), tener en cuenta que el resultado será un desfase desde 1970-01-01 00\:00:00.
        - Como una cadena que respete _ISO 8601_ o el formato _datetime_, se puede forzar una unidad al indicarla.
        - Como _NaT_ que representa un valor que no es una fecha.
        - Si se define en el parámetro _dtype_ se debe de poner como una cadena y entre corchetes indicar la unidad: `datetime64[unit]`.
        - Ejemplos: <br/> `np.datetime64('2005-02-25T03:30') # -> np.datetime64('2005-02-25T03:30')` <br/> `np.datetime64(1, 'Y') # -> np.datetime64('1971')` <br/> `np.datetime64('2005-02') # -> np.datetime64('2005-02')` <br/> `np.datetime64('2005-02', 'D') # -> np.datetime64('2005-02-01')` <br/> `np.datetime64('nat') # -> np.datetime64('NaT')`
- `np.timedelta`:
    - Representa una diferencia entre dos fechas y tiempos.
    - Se puede definir de las siguientes maneras:
        - Como un número (es necesario indicar una unidad). Para _timedeltas_ más complejos (de múltiples unidades) se pueden sumar/restar _timedeltas_ para conseguir el valor deseado.
        - Como _NaT_ que representa un valor que no es una fecha.
        - Si se define en el parámetro _dtype_ se debe de poner como una cadena y entre corchetes indicar la unidad: `timedelta64[unit]`.
        - Ejemplos: <br/> `np.timedelta64(1, 'D') # -> np.timedelta64(1,'D')` <br/> `np.timedelta64('nAt') # -> np.timedelta64('NaT')`

Las unidades válidas son las siguientes:

```{list-table}
:header-rows: 1

* - Código
  - Descripción
* - D
  - Día.
* - M
  - Mes.
* - W
  - Semana.
* - Y
  - año.
* - h
  - Horas.
* - m
  - Minutos.
* - s
  - Segundos.
* - ms
  - Milisegundos.
* - us
  - Microsegundos.
* - ns
  - Nanosegundos.
```
Para más información visitar la [documentación](https://numpy.org/doc/stable/reference/arrays.datetime.html#datetime-units) de `numpy`.

<br/>

---
## Tabla de contenido

```{tableofcontents}
````