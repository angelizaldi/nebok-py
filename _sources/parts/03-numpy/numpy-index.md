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
import numpy as np
```
- `np` es el nombre por convención.
- En este sitio se utilizará `np` como alias.

Para conocer la versión de `numpy` instalada usar:
```python
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
| `int8`       | `np.byte`    | `'i1'`           | Entero de 8 bits (-128 a 127) | |
| `int16`      | `np.short`   | `'i2'`           | Entero de 16 bits (-32768 a 32767)| |
| `int32`      | `np.intc`   | `'i4'`           | Entero de 32 bits                | |
| `int64`      | `np.int_`   | `'i8'`           | Entero de 64 bits                | `int` |
| `uint8`      | `np.ubyte`   | `'u1'`           | Entero sin signo de 8 bits (0 a 255) |
| `uint16`     | `np.ushort`  | `'u2'`           | Entero sin signo de 16 bits (0 a 65535)|
| `uint32`     | `np.uintc`  | `'u4'`           | Entero sin signo de 32 bits       | |
| `uint64`     | `np.uint`  | `'u8'`           | Entero sin signo de 64 bits       | |
| `float16`    | `np.half` | `'f2'`           | Punto flotante de 16 bits         | |
| `float32`    | `np.single` | `'f4'`           | Punto flotante de 32 bits         | |
| `float64`    | `np.double` | `'f8'`           | Punto flotante de 64 bits         | `float` |
| `float128`    | `np.longdouble` | `'f16'`          | Punto flotante de 128 bits         | |
| `complex64`  | `np.csingle` | `'c8'`         | Número complejo de 64 bits        | |
| `complex128` | `np.cdouble`| `'c16'`        | Número complejo de 128 bits       | `complex` |
| `complex256` | `np.clongdouble`| `'c32'`        | Número complejo de 256 bits       | |

Además existen los siguientes otros tipos de datos:

| Objeto NumPy        | Código en Cadena | Descripción                            | Tipo _built-in_ de Python relacionado |
|---------------------|------------------|----------------------------------------|---------|
| `np.str_`          | `'U'`            | Cadena _unicode_       | `str` |
| `np.bool_`          | `'?'`            | Tipo booleano (`True` o `False`)       | `bool` |
| `np.bytes_`          | `'b'`            | Tipo booleano (`True` o `False`)       | `bytes`
| `np.datetime64`     | `'M'`   | Fecha y hora                           | `datetime.datetime` |
| `np.timedelta64`    | `'m'`  | Diferencia entre dos fechas y horas    | `datetime.timedelta` |
| `np.object_`        | `'O'`            | Objeto genérico (cualquier tipo de dato)| `object` |

:::{caution}
La gran mayoría de tipos en `numpy` tienen alias, por ejemplo `np.float_` es un alias de `np.double`, para revisar los alias visitar la [documentación](https://numpy.org/doc/stable/reference/arrays.scalars.html#built-in-scalar-types) de `numpy`, particularmente la sección de [Otros alias](https://numpy.org/doc/stable/reference/arrays.scalars.html#other-aliases).
:::


:::{important}
Para una lista completa visitar la [documentación](https://numpy.org/doc/stable/reference/arrays.scalars.html) de `numpy`.
:::

<br/>

## Tabla de contenido


```{tableofcontents}
````