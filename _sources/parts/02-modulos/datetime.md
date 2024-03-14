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

# Datetime

Es un módulo para trabajar con datos de tipo fecha y tiempo. Es necesario importarlo:

```python
# Importar todo el módulo
import datetime

# Importar una clase específica
from datetime import class_name
```
- _class_name_ es el nombre de clase que se desea importar,
- Estos solo son dos ejemplos de como importar el módulo, se puede usar cualquier rutina de importación, como importar con alias, importar constantes específicas, etc.

---
(datetime-iso)=
## ISO 8601

Muchos métodos de este módulo utilizan el formato ISO 8601, el cual es el siguiente para fechas:
> YYYY-MM-DD
- YYYY: Año de cuatro dígitos, desde 0000 a 9999.
- MM: Mes de dos dígitos, del 01 a 12.
- DD: Día de dos dígitos, del 01 al 31.

y el siguiente para fechas y tiempo:
> YYYY-MM-DDTHH:MM:SS
- YYYY: Año de cuatro dígitos, desde 0000 a 9999.
- MM: Mes de dos dígitos, del 01 a 12.
- DD: Día de dos dígitos, del 01 al 31.
- HH: Horas de dos dígitos, desde 00 a 23.
- MM: Minutos de dos dígitos, desde 00 a 59.
- SS: Segundos de dos dígitos, desde 00 a 59.

---
## Clases

Existen diferentes tipos de datos de fecha y tiempo, cada tipo es una clase dentro del módulo `datetime` y cada clase tiene métodos y atributos diferentes:
- [date](https://docs.python.org/3/library/datetime.html#date-objects): (año, mes, día), Asume el calendario gregoriano.
- [time](https://docs.python.org/3/library/datetime.html#time-objects): (hora, minuto, segundo, microsegundo, zona horaria), Asume que cada día tiene exactamente 24 horas, cada hora 60 minutos y cada minuto 60 segundos.
- [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects): (año, mes, día, hora, minuto, segundo, microsegundo, zona horaria), Combinación de `date` y `time`.
- [timedelta](https://docs.python.org/3/library/datetime.html#timedelta-objects): Representa la diferencia de dos fechas o tiempos. Se pueden hacer operaciones aritméticas con objetos `timedelta`. 
- [tzinfo](https://docs.python.org/3/library/datetime.html#tzinfo-objects): Objetos con información sobre la zona horaria.
- [timezone](https://docs.python.org/3/library/datetime.html#timezone-objects): Implementa la clase base abstracta `tzinfo` como un desfase fijo de UTC.

```{warning}
En este sitio solo se presentarán las clases `date`, `time`, `datetime` y `timedelta`.
```

---
## Constantes

A continuación se presenta una lista de las constantes disponibles en el módulo `datetime`. 

```{list-table}
:header-rows: 1

* - Constante
  - Descripción
* - [MAXYEAR](https://docs.python.org/3/library/datetime.html#datetime.MAXYEAR)
  - El mayor número de año permitido en un objeto de fecha o fecha y tiempo. `MAXYEAR` es 9999.
* - [MINYEAR](https://docs.python.org/3/library/datetime.html#datetime.MINYEAR)
  - El número de año más pequeño permitido en un objeto de fecha o fecha y tiempo. `MINYEAR` es 1.
```

---
## Datetime


```{warning}
En este sitio no se documenta todas las características de la clase `datetime`, para un tratado completo visitar la [documentación](https://docs.python.org/3/library/datetime.html#datetime-objects) de Python.
```

`datetime` es una clase que representa fechas y tiempo. Algunas características de estos objetos son:
- Es inmutable: No se puede modificar una vez creado.
- Es _hashable_: Se puede utilizar como _key_ de un diccionario.

```{list-table}
:header-rows: 1

* - Constructor
  - Descripción
* - [datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime)(year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0)
  - Los argumentos de `year`, `month` y `day` son obligatorios. `tzinfo` puede ser `None`, o un instancia de la subclase `tzinfo`. Los argumentos restantes deben ser números enteros.
```
**Notas**:
- **`tzinfo`** \- `str`, `tzinfo`: Es la zona horaria, se puede usar un objeto creado con `datetime.tzinfo()` o usar una cadena, para ver las zonas horarias disponibles visitar [Zonas Horarias](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).

<br>

---
### Crear una fecha y tiempo

Existen diversas formas para crear una instancia de `datetime`. A continuación se presentan algunas de las más comunes.

**1. Con el constructor**: Se puede usa el constructor `datetime.datetime()` para crear una fecha pasando individualmente cada uno los componentes:

```{code-cell} python3
# Importar la clase
from datetime import datetime

# Crear una instancia
X = datetime(2020, 1, 1, 12, 30, 30)

# Imprimir la instancia
print(X)
```

**2. Con el método de clase fromisoformat()**: Se puede usar el método de clase `datetime.datetime.fromisoformat()` pasando una cadena que represente una fecha y tiempo respetando ISO 8601.

```{code-cell} python3
# Importar la función
from datetime import datetime

# Crear una instancia
X = datetime.fromisoformat("2020-01-01T12:30:30")

# Imprimir la instancia
print(X)
```

**3. Con el método de clase strptime()**: Se puede usar el método de clase `datetime.datetime.strptime()` pasando una cadena que represente una fecha indicando el formato en el que está la cadena con los {ref}`codigos-formatos-fechas`.

```{code-cell} python3
# Importar la clase
from datetime import datetime

# Crear una instancia
X = datetime.strptime("12:30, 1 Jan, 2020", "%H:%M, %d %b, %Y")

# Imprimir la instancia
print(X)
```

:::{note}
Existen más métodos para crear fechas y tiempo, revisar {ref}`datetime-metodos-clase`.
:::

<br>

---
### Recuperar componentes de una fecha

Para recuperar los componentes de una fecha utilizar los {ref}`datetime-atributos-instancia`.

<br>

---
### Operaciones con objetos datetime

Las operaciones válidas que se pueden hacer con objetos `datetime` son:
- `datetime2 = datetime1 + timedelta`: A un objeto `datetime` sumarle un objeto `timedelta` y retornar un objeto `datetime`.
- `datetime2 = datetime1 - timedelta`: A un objeto `datetime` restarle un objeto `timedelta` y retornar un objeto `datetime`.
- `timedelta = datetime1 - datetime2`: Restar dos objetos `datetime` y retornar un objeto `timedelta`.
- `datetime1 < datetime2`: Usar {ref}`built-in-operadores-comparacion` con dos objetos `datetime`.

<br>

---
### Atributos de clase

A continuación se presenta una lista de atributos de clase. Tener en cuenta que los atributos de clase son atributos asociados con la clase misma y no con las instancias.

Ejemplo de cómo usar un atributo de clase:

```{code-cell} python3
# Importar clase
from datetime import datetime

# Usar un atributo de clase
print(datetime.max)
```

<br/>

Lista de atributos de clase de `datetime.datetime`.

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - [max](https://docs.python.org/3/library/datetime.html#datetime.datetime.max)
  - La máxima fecha y hora representable, `datetime(MAXYEAR, 12, 31, 23, 59, 59, 999999, tzinfo=None)`.
* - [min](https://docs.python.org/3/library/datetime.html#datetime.datetime.min)
  - La mínima fecha y hora representable, `datetime(MINYEAR, 1, 1, tzinfo=None)`.
* - [resolution](https://docs.python.org/3/library/datetime.html#datetime.datetime.resolution)
  - La diferencia más pequeña posible entre objetos `datetime` no iguales, `timedelta(microsegundos=1)`.
```

<br>

(datetime-atributos-instancia)=
### Atributos de instancia

Los atributos de instancia se aplican directamente sobre un objeto `datetime`. 

Ejemplo de cómo usar un atributo de instancia:

```{code-cell} python3
# Importar clase
from datetime import datetime

# Crear una instancia
X = datetime(2020, 1, 1)

# Usar un atributo de instancia
print(X.year)
```

<br/>

Lista de atributos de instancia de `datetime.datetime`.

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - [day](https://docs.python.org/3/library/datetime.html#datetime.datetime.day)
  - Entre 1 y el número de días del mes dado del año dado.
* - [fold](https://docs.python.org/3/library/datetime.html#datetime.datetime.fold)
  - Entre [0, 1]. Se utiliza para eliminar la ambigüedad de los tiempos de pared durante un intervalo repetido.
* - [hour](https://docs.python.org/3/library/datetime.html#datetime.datetime.hour)
  - En rango (24).
* - [microsecond](https://docs.python.org/3/library/datetime.html#datetime.datetime.microsecond)
  - En rango (1000000).
* - [minute](https://docs.python.org/3/library/datetime.html#datetime.datetime.minute)
  - En rango (60).
* - [month](https://docs.python.org/3/library/datetime.html#datetime.datetime.month)
  - Entre 1 y 12 inclusivo.
* - [second](https://docs.python.org/3/library/datetime.html#datetime.datetime.second)
  - En rango (60).
* - [tzinfo](https://docs.python.org/3/library/datetime.html#datetime.datetime.tzinfo)
  - El objeto pasado como argumento de `tzinfo` al constructor de `datetime`, o `None` si no se pasó ninguno.
* - [year](https://docs.python.org/3/library/datetime.html#datetime.datetime.year)
  - Entre `MINYEAR` y `MAXYEAR` inclusivo.
```

<br>

(datetime-metodos-clase)=
### Métodos de clase

Son métodos que se aplican directamente sobre la clase `datetime.datetime`. 

Ejemplo de cómo usar un método de clase:

```{code-cell} python3
# Importar clase
from datetime import datetime

# Usar método de la clase
X = datetime.fromisoformat('2011-11-04')

# Imprimir x
print(X)
```

<br/>

Lista de métodos de la clase `datetime.datetime`.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [combine](https://docs.python.org/3/library/datetime.html#datetime.datetime.combine)(date, time, tzinfo=self.tzinfo)
  - Devuelve un nuevo objeto de fecha y hora cuyos componentes de fecha son iguales a el objeto `date` dado, y cuyos componentes de tiempo son iguales a los del objeto `time` dado.
* - [fromisocalendar](https://docs.python.org/3/library/datetime.html#datetime.datetime.fromisocalendar)(year, week, day)
  - Devuelve una fecha y hora correspondiente a la fecha del calendario ISO especificada por `year`, `week` y `day`.
* - [fromisoformat](https://docs.python.org/3/library/datetime.html#datetime.datetime.fromisoformat)(date_string)
  - Devuelve una fecha y hora correspondiente a una cadena de fecha en cualquier formato válido ISO 8601.
* - [fromordinal](https://docs.python.org/3/library/datetime.html#datetime.datetime.fromordinal)(ordinal)
  - Devuelve la fecha y hora correspondiente al ordinal gregoriano proléptico, donde el 1 de enero del año 1 tiene el ordinal 1.
* - [fromtimestamp](https://docs.python.org/3/library/datetime.html#datetime.datetime.fromtimestamp)(timestamp, tz=None)
  - Devuelve la fecha y hora locales correspondientes a la marca de tiempo POSIX, como es devuelto por time.time().
* - [now](https://docs.python.org/3/library/datetime.html#datetime.datetime.now)(tz=None)
  - Devuelve la fecha y hora locales actuales.
* - [strptime](https://docs.python.org/3/library/datetime.html#datetime.datetime.strptime)(date_string, format)
  - Devuelve una fecha y hora correspondiente a `date_string`, de acuerdo con `format`.
* - [today](https://docs.python.org/3/library/datetime.html#datetime.datetime.today)()
  - Devuelve la fecha y hora local actual, con `tzinfo` `None`.
* - [utcfromtimestamp](https://docs.python.org/3/library/datetime.html#datetime.datetime.utcfromtimestamp)(timestamp)
  - Devuelve la fecha y hora UTC correspondiente a la marca de tiempo POSIX, con `tzinfo` `None`.
* - [utcnow](https://docs.python.org/3/library/datetime.html#datetime.datetime.utcnow)()
  - Devuelve la fecha y hora UTC actuales, con `tzinfo` `None`.
```

<br>

### Métodos de instancia

Son métodos que se aplican directamente en instancias (objetos) de la clase `datetime.datetime`. 

Ejemplo de cómo usar un método de instancia:

```{code-cell} python3
# Importar clase
from datetime import datetime

# Crear una instancia
X = datetime(2020, 1, 1, 12, 30, 30)

# Usar un método de instancia
print(X.timestamp())
```

<br/>

A continuación la lista de métodos de instancia de la clase `datetime.datetime`.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [astimezone](https://docs.python.org/3/library/datetime.html#datetime.datetime.astimezone)(tz=None)
  - Devuelve un objeto `datetime` con el nuevo atributo `tzinfo` igual a `tz`, ajustando los datos de fecha y hora para que el resultado sea la misma hora UTC que `self`, pero en la hora local de `tz`.
* - [ctime](https://docs.python.org/3/library/datetime.html#datetime.datetime.ctime)()
  - Devuelve una cadena que representa la fecha y la hora.
* - [date](https://docs.python.org/3/library/datetime.html#datetime.datetime.date)()
  - Retorna la fecha de un objeto, excluyendo el tiempo.
* - [dst](https://docs.python.org/3/library/datetime.html#datetime.datetime.dst)()
  - Si `tzinfo` es `None`, devuelve `None`, de lo contrario, devuelve `self.tzinfo.dst(self)`.
* - [isocalendar](https://docs.python.org/3/library/datetime.html#datetime.datetime.isocalendar)()
  - Devuelve un `namedtuple` con con tres componentes: `year`, `week` y `day`.
* - [isoformat](https://docs.python.org/3/library/datetime.html#datetime.datetime.isoformat)(sep='T', timespec='auto')
  - Devuelve una cadena que representa la fecha y la hora en formato ISO 8601.
* - [isoweekday](https://docs.python.org/3/library/datetime.html#datetime.datetime.isoweekday)()
  - Devuelve el día de la semana como un número entero, donde el lunes es 1 y el domingo es 7.
* - [replace](https://docs.python.org/3/library/datetime.html#datetime.datetime.replace)(year=self.year, month=self.month, day=self.day, hour=self.hour, minute=self.minute, second=self.second, microsecond=self.microsecond, tzinfo=self.tzinfo, *, fold=0)
  - Retorna la misma fecha con una modificación en los elementos especificados. Si se modifica la zona horaria (`tzinfo`), no se modificará la hora, solo la información de la zona horaria, para modificar la hora, usar el método `datetime.datetime.astimezone()`.
* - [strftime](https://docs.python.org/3/library/datetime.html#datetime.datetime.strftime)(format)
  - Devuelve una cadena que representa la fecha y la hora, controlada por un formato explícito.
* - [time](https://docs.python.org/3/library/datetime.html#datetime.datetime.time)()
  - Retorna el tiempo de un objeto, excluyendo la fecha.
* - [timestamp](https://docs.python.org/3/library/datetime.html#datetime.datetime.timestamp)()
  - Devolver el _timestamp_ POSIX correspondiente a la instancia `datetime` (número de segundos que han pasado desde el primero de enero de 1970 hasta la fecha actual).
* - [timetuple](https://docs.python.org/3/library/datetime.html#datetime.datetime.timetuple)()
  - Devuelve un `time.struct_time` como el que devuelve `time.localtime()`.
* - [timetz](https://docs.python.org/3/library/datetime.html#datetime.datetime.timetz)()
  - Retorna el tiempo con información de la zona horaria de un objeto.
* - [toordinal](https://docs.python.org/3/library/datetime.html#datetime.datetime.toordinal)()
  - Devuelve el ordinal gregoriano proléptico de la fecha. Lo mismo que `self.date().toordinal()`.
* - [tzname](https://docs.python.org/3/library/datetime.html#datetime.datetime.tzname)()
  - Si `tzinfo` es `None`, devuelve `None`, de lo contrario, devuelve `self.tzinfo.tzname(self)`.
* - [utcoffset](https://docs.python.org/3/library/datetime.html#datetime.datetime.utcoffset)()
  - Si `tzinfo` es `None`, devuelve `None`, de lo contrario, devuelve `self.tzinfo.utcoffset(self)`.
* - [utctimetuple](https://docs.python.org/3/library/datetime.html#datetime.datetime.utctimetuple)()
  - Si la instancia `d` de `datetime` es _naive_, esto es lo mismo que `d.timetuple()` excepto que `tm_isds`t se fuerza a 0 sin importar qué retorne `d.dst()`.
* - [weekday](https://docs.python.org/3/library/datetime.html#datetime.datetime.weekday)()
  - Devuelve el día de la semana como un número entero, donde el lunes es 0 y el domingo es 6.
```

<br>
<br>

---
## Date

```{warning}
En este sitio no se documenta todas las características de la clase `date`, para un tratado completo visitar la [documentación](https://docs.python.org/3.11/library/datetime.html#date-objects) de Python.
```

`date` es una clase que representa fechas. Algunas características de estos objetos son:
- Es inmutable: No se puede modificar una vez creado.
- Es _hashable_: Se puede utilizar como _key_ de un diccionario.


```{list-table}
:header-rows: 1

* - Constructor
  - Descripción
* - [date](https://docs.python.org/3/library/datetime.html#datetime.date)(year, month, day)
  - Todos los argumentos son necesarios. Los argumentos deben ser números enteros.
```

<br>

### Crear una fecha

Existen diversas formas para crear una instancia de `date`. A continuación se presentan algunas de las más comunes.

**1. Con el constructor**: Se puede usa el constructor `datetime.date()` para crear una fecha pasando individualmente cada uno los componentes:

```{code-cell} python3
# Importar la clase
from datetime import date

# Crear una instancia
X = date(2020, 1, 1)

# Imprimir la instancia
print(X)
```

**2. Con el método de clase fromisoformat()**: Se puede usar el método de clase `datetime.date.fromisoformat()` pasando una cadena que represente una fecha y tiempo respetando ISO 8601.

```{code-cell} python3
# Importar la función
from datetime import date

# Crear una instancia
X = date.fromisoformat("2020-01-01")

# Imprimir la instancia
print(X)
```

:::{note}
Existen más métodos para crear fechas, revisar {ref}`date-metodos-clase`.
:::

<br>

---
### Recuperar componentes de una fecha

Para recuperar los componentes de una fecha utilizar los {ref}`date-atributos-instancia`.

<br>

---
### Operaciones con objetos datetime

Las opciones válidas que se pueden hacer con objetos `date` son:
- `date2 = date1 + timedelta`: A un objeto `date` sumarle un objeto `timedelta` y retornar un objeto `date`.
- `date2 = date1 - timedelta`: A un objeto `date` restarle un objeto `timedelta` y retornar un objeto `date`.
- `timedelta = datetime1 - datetime2`: Restar dos objetos `date` y retornar un objeto `timedelta`.
- `date1 < date2`: Usar {ref}`built-in-operadores-comparacion` con dos objetos `date`.

<br/>

---
### Atributos de clase

A continuación se presenta una lista de atributos de clase. Tener en cuenta que los atributos de clase son atributos asociados con la clase misma y no con las instancias.

Ejemplo de cómo usar un atributo de clase:

```{code-cell} python3
# Importar clase
from datetime import date

# Usar un atributo de clase
print(date.max)
```

<br/>

Lista de atributos de clase de `datetime.datetime`.

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - [max](https://docs.python.org/3/library/datetime.html#datetime.date.max)
  - La máxima fecha representable, `date(MAXYEAR, 12, 31)`.
* - [min](https://docs.python.org/3/library/datetime.html#datetime.date.min)
  - La mínima fecha representable, `date(MINYEAR, 1, 1)`.
* - [resolution](https://docs.python.org/3/library/datetime.html#datetime.date.resolution)
  - La diferencia más pequeña posible entre objetos de fecha no iguales, `timedelta(days=1)`.
```

<br>

(date-atributos-instancia)=
### Atributos de instancia

Los atributos de instancia se aplican directamente sobre un objeto `datetime`. 

Ejemplo de cómo usar un atributo de instancia:

```{code-cell} python3
# Importar clase
from datetime import date

# Crear una instancia
X = date(2020, 1, 1)

# Usar un atributo de instancia
print(X.year)
```

<br/>

Lista de atributos de instancia de `datetime.date`.


```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - [day](https://docs.python.org/3/library/datetime.html#datetime.date.day)
  - Entre 1 y el número de días del mes dado del año dado.
* - [month](https://docs.python.org/3/library/datetime.html#datetime.date.month)
  - Entre 1 y 12 inclusive.
* - [year](https://docs.python.org/3/library/datetime.html#datetime.date.year)
  - Entre `MINYEAR` y `MAXYEAR` inclusivo.
```
 
<br> 
 
(date-metodos-clase)=
### Métodos de clase


Son métodos que se aplican directamente sobre la clase `datetime.date`. 


Ejemplo de cómo usar un método de clase:

```{code-cell} python3
# Importar clase
from datetime import date

# Usar método de la clase
X = date.fromisoformat('2011-11-04')

# Imprimir x
print(X)
```

<br/>

Lista de métodos de la clase `datetime.date`.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [fromisocalendar](https://docs.python.org/3/library/datetime.html#datetime.date.fromisocalendar)(year, week, day)
  - Devuelve una fecha correspondiente a la fecha del calendario ISO especificada por año, semana y día.
* - [fromisoformat](https://docs.python.org/3/library/datetime.html#datetime.date.fromisoformat)(date_string)
  - Retorna una fecha correspondiente a una cadena que representa una fecha dada en cualquier formato válido ISO 8601.
* - [fromordinal](https://docs.python.org/3/library/datetime.html#datetime.date.fromordinal)(ordinal)
  - Devuelve la fecha correspondiente al ordinal gregoriano proléptico, donde el 1 de enero del año 1 tiene el ordinal 1.
* - [fromtimestamp](https://docs.python.org/3/library/datetime.html#datetime.date.fromtimestamp)(timestamp)
  - Devuelve la fecha local correspondiente a la marca de tiempo POSIX, como es devuelto por `time.time()`.
* - [today](https://docs.python.org/3/library/datetime.html#datetime.date.today)()
  - Devuelve la fecha local actual.
```

<br>

### Métodos de instancia

Son métodos que se aplican directamente en instancias (objetos) de la clase `datetime.datetime`. 

Ejemplo de cómo usar un método de instancia:

```{code-cell} python3
# Importar clase
from datetime import date

# Crear una instancia
X = date(2020, 1, 1)

# Usar un método de instancia
print(X.ctime())
```

<br/>

A continuación la lista de métodos de instancia de la clase `datetime.datetime`.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [ctime](https://docs.python.org/3/library/datetime.html#datetime.date.ctime)()
  - Devuelve una cadena que representa la fecha.
* - [isocalendar](https://docs.python.org/3/library/datetime.html#datetime.date.isocalendar)()
  - Devuelve un `namedtuple` con tres componentes: `year`, `week` y `day`.
* - [isoformat](https://docs.python.org/3/library/datetime.html#datetime.date.isoformat)()
  - Devuelve una fecha correspondiente a una cadena de representa una fecha en cualquier formato válido ISO 8601.
* - [isoweekday](https://docs.python.org/3/library/datetime.html#datetime.date.isoweekday)()
  - Devuelve el día de la semana como un número entero, donde el lunes es `1` y el domingo es `7`.
* - [replace](https://docs.python.org/3/library/datetime.html#datetime.date.replace)(year=self.year, month=self.month, day=self.day)
  - Devuelve una fecha con el mismo valor, excepto para aquellos parámetros a los que se le dieron nuevos valores.
* - [strftime](https://docs.python.org/3/library/datetime.html#datetime.date.strftime)(format)
  - Devuelve una cadena que representa la fecha, controlada por una cadena de formato explícito.
* - [timetuple](https://docs.python.org/3/library/datetime.html#datetime.date.timetuple)()
  - Devuelve un `time.struct_time` como el que devuelve `time.localtime()`.
* - [toordinal](https://docs.python.org/3/library/datetime.html#datetime.date.toordinal)()
  - Devuelve el ordinal gregoriano proléptico de la fecha, donde 1 de enero del año 1 tiene ordinal 1.
* - [weekday](https://docs.python.org/3/library/datetime.html#datetime.date.weekday)()
  - Devuelve el día de la semana como un número entero, donde el lunes es `0` y el domingo es `6`.
```

<br>
<br>

---
## Time

```{warning}
En este sitio no se documenta todas las características de la clase `time`, para un tratado completo visitar la [documentación](https://docs.python.org/3.11/library/datetime.html#time-objects) de Python.
```

`time` es una clase que representa tiempos. Algunas características de estos objetos son:
- Es inmutable: No se puede modificar una vez creado.
- Es _hashable_: Se puede utilizar como _key_ de un diccionario.

```{list-table}
:header-rows: 1

* - Constructor
  - Descripción
* - [time](https://docs.python.org/3/library/datetime.html#datetime.time)(hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0)
  - Todos los argumentos son opcionales. `tzinfo` puede ser `None`, o una instancia de la subclase `tzinfo`. Los argumentos restantes deben ser números enteros.
```
**Notas**:
- **`tzinfo`** \- `str`, `timezone`: Es la zona horaria, se puede usar un objeto creado con `datetime.timezone()` o usar una cadena, para ver las zonas horarias disponibles ver [Zonas Horarias](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).

<br>

---
### Crear un tiempo

Existen diversas formas para crear una instancia de `time`. A continuación se presentan algunas de las más comunes.

**1. Con el constructor**: Se puede usa el constructor `datetime.time()` para crear tiempos pasando individualmente cada uno los componentes:

```{code-cell} python3
# Importar la clase
from datetime import time

# Crear una instancia
X = time(12, 30, 30)

# Imprimir la instancia
print(X)
```

**2. Con el método de clase fromisoformat()**: Se puede usar el método de clase `datetime.time.fromisoformat()` pasando una cadena que represente un tiempo respetando ISO 8601.

```{code-cell} python3
# Importar la función
from datetime import time

# Crear una instancia
X = time.fromisoformat("12:30:30")

# Imprimir la instancia
print(X)
```

<br>

---
### Recuperar componentes de un tiempo

Para recuperar los componentes de un tiempo utilizar los {ref}`time-atributos-instancia`.

<br/>

---
### Atributos de clase

A continuación se presenta una lista de atributos de clase. Tener en cuenta que los atributos de clase son atributos asociados con la clase misma y no con las instancias.

Ejemplo de cómo usar un atributo de clase:

```{code-cell} python3
# Importar clase
from datetime import time

# Usar un atributo de clase
print(time.max)
```

<br/>

Lista de atributos de clase de `datetime.time`.

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - [max](https://docs.python.org/3/library/datetime.html#datetime.time.max)
  - El máximo tiempo representable, `time(23, 59, 59, 999999)`.
* - [min](https://docs.python.org/3/library/datetime.html#datetime.time.min)
  - El mínimo tiempo representable, `time(0, 0, 0, 0)`.
* - [resolution](https://docs.python.org/3/library/datetime.html#datetime.time.resolution)
  - La diferencia más pequeña posible entre objetos `time` no iguales, `timedelta(microseconds=1)`.
```

<br>

(time-atributos-instancia)=
### Atributos de instancia

Los atributos de instancia se aplican directamente sobre un objeto `time`. 

Ejemplo de cómo usar un atributo de instancia:

```{code-cell} python3
# Importar clase
from datetime import time

# Crear una instancia
X = time(12, 30, 30)

# Usar un atributo de instancia
print(X.hour)
```

<br/>

Lista de atributos de instancia de `datetime.time`.


```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - [fold](https://docs.python.org/3/library/datetime.html#datetime.time.fold)
  - En [0, 1]. Se utiliza para eliminar la ambigüedad de los tiempos de pared durante un intervalo repetido.
* - [hour](https://docs.python.org/3/library/datetime.html#datetime.time.hour)
  - En rango (24).
* - [microsecond](https://docs.python.org/3/library/datetime.html#datetime.time.microsecond)
  - En rango (1000000).
* - [minute](https://docs.python.org/3/library/datetime.html#datetime.time.minute)
  - En rango (60).
* - [second](https://docs.python.org/3/library/datetime.html#datetime.time.second)
  - En rango (60).
* - [tzinfo](https://docs.python.org/3/library/datetime.html#datetime.time.tzinfo)
  - El objeto pasado como argumento de `tzinfo` al constructor de `time`, o `None` si no se pasó ninguno.
```
 
<br> 
 
### Métodos de clase


Son métodos que se aplican directamente sobre la clase `datetime.time`. 

Ejemplo de cómo usar un método de clase:

```{code-cell} python3
# Importar clase
from datetime import time

# Usar método de la clase
X = time.fromisoformat('12:30:30')

# Imprimir x
print(X)
```

<br/>

Lista de métodos de la clase `datetime.time`.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [fromisoformat](https://docs.python.org/3/library/datetime.html#datetime.time.fromisoformat)(time_string)
  - Retorna una hora correspondiente a un `time_string` en cualquier formato válido ISO 8601.
```

<br>

### Métodos de instancia

Son métodos que se aplican directamente en instancias (objetos) de la clase `datetime.time`. 

Ejemplo de cómo usar un método de instancia:

```{code-cell} python3
# Importar clase
from datetime import time

# Crear una instancia
X = time(12, 30, 30)

# Usar un método de instancia
print(X.isoformat())
```

<br/>

A continuación la lista de métodos de instancia de la clase `datetime.datetime`.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [isoformat](https://docs.python.org/3/library/datetime.html#datetime.time.isoformat)(timespec='auto')
  - Devuelve una cadena que representa la hora en formato ISO 8601
* - [replace](https://docs.python.org/3/library/datetime.html#datetime.time.replace)(hour=self.hour, minute=self.minute, second=self.second, microsecond=self.microsecond, tzinfo=self.tzinfo, *, fold=0)
  - Retorna una hora con el mismo valor, excepto por aquellos atributos a los que se les dio un nuevo valor.
* - [strftime](https://docs.python.org/3/library/datetime.html#datetime.time.strftime)(format)
  - Devuelve una cadena que representa la hora, controlada por una cadena de formato explícita.
* - [tzname](https://docs.python.org/3/library/datetime.html#datetime.time.tzname)()
  - Si `tzinfo` es `None`, devuelve `None`, de lo contrario, devuelve `self.tzinfo.tzname(None)`.
```

<br>
<br>

---
(timedelta)=
## Timedelta

```{warning}
En este sitio no se documenta todas las características de la clase `timedelta`, para un tratado completo visitar la [documentación](https://docs.python.org/3.11/library/datetime.html#timedelta-objects) de Python.
```

`timedelta` es una clase que representa diferencias entre tiempos o fechas.


```{list-table}
:header-rows: 1

* - Constructor
  - Descripción
* - [timedelta](https://docs.python.org/3/library/datetime.html#datetime.timedelta)(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
  - Todos los argumentos son opcionales y su valor predeterminado es `0`. Los argumentos pueden ser números `int` o `float`, y pueden ser positivos o negativos.
```

<br>

---
### Crear un timedelta

Para crear una instancia de `timdelta` se puede usa el constructor `datetime.timedelta()` indicando los componentes y sus valores:

```{code-cell} python3
# Importar la clase
from datetime import timedelta

# Crear una instancia
X = timedelta(days=1, seconds=50, milliseconds=0, minutes=30, hours=3)

# Imprimir la instancia
print(X)
```

<br/>

---
### Operaciones con objetos timedelta

Es posible realizar operaciones aritméticas con objetos `timedelta`. 

**Suma y resta de objetos `timedelta`**:

Se pueden sumar o restar dos objetos `timedelta` con los operadores `+` y `-` respectivamente y retornar otro objeto `timedelta`. Ejemplo:

```{code-cell} python3
# Importar clase
from datetime import timedelta

# Definir dos objetos timedelta
X = timedelta(days=1, minutes=30, seconds=30)
Y = timedelta(days=1, minutes=30)

# Suma y restar objetos timedelta
print(f"Suma: {X+Y}")
print(f"Resta: {X-Y}")
```

<br/>

**Multiplicar un objeto timedelta por un número**:

Se puede multiplicar un objeto `timedelta` por un número `int` o `float` con el operador `*` y retornar otro objeto `timedelta`. Cada componente se multiplicará por el factor indicado. Ejemplo:

```{code-cell} python3
# Importar clase
from datetime import timedelta

# Definir objeto
X = timedelta(days=1, minutes=30, seconds=30)

# Suma y restar objetos timedelta
print(f"Multiplicar por entero: {X*2}")
print(f"Multiplicar por flotante: {X*2.5}")
```

<br/>

**Dividir un objeto timedelta**:

Es posible dividir un objeto `timedelta` entre otro objeto `timedelta` o entre un número `int` o `float` con el operador `/` y retornar otro objeto `timedelta`. Ejemplo:

```{code-cell} python3
# Importar clase
from datetime import timedelta

# Definir dos objetos timedelta
X = timedelta(days=1, minutes=30)
Y = timedelta(minutes=30)

# Divir 2 objetos timedelta
print(f"Dividir X entre Y: {X/Y}", end="\n"*2)

# Dividir un objeto timedelta entre un número
print(f"Dividir Y entre 30: {Y/30}")
```

Es posible además calcular el módulo o la división parte entera con los operadores `%` y `//` respectivamente o con la función `divmode()`. 

Para más información visitar la [documentación](https://docs.python.org/3/library/datetime.html#timedelta-objects) de Python.

<br/>

---
### Atributos de clase

A continuación se presenta una lista de atributos de clase. Tener en cuenta que los atributos de clase son atributos asociados con la clase misma y no con las instancias.

Ejemplo de cómo usar un atributo de clase:

```{code-cell} python3
# Importar clase
from datetime import timedelta

# Usar un método de clase
print(timedelta.max)
```

<br/>

Lista de atributos de clase de `datetime.timedelta`.

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - [max](https://docs.python.org/3/library/datetime.html#datetime.timedelta.max)
  - El mayor objeto `timedelta` posible, `timedelta(days=999999999, hours=23, minutes=59, seconds=59, microseconds=999999)`.
* - [min](https://docs.python.org/3/library/datetime.html#datetime.timedelta.min)
  - El menor objeto `timedelta` posible, `timedelta(-999999999)`.
* - [resolution](https://docs.python.org/3/library/datetime.html#datetime.timedelta.resolution)
  - La diferencia más pequeña posible entre objetos `timedelta` no iguales, `timedelta(microseconds=1)`.
```

<br>

### Métodos de instancia

Son métodos que se aplican directamente en instancias (objetos) de la clase `datetime.timedelta`. 

Ejemplo de cómo usar un método de instancia:

```{code-cell} python3
# Importar clase
from datetime import timedelta

# Crear una instancia
X = timedelta(days=5)

# Usar un método de instancia
print(X.total_seconds())
```

<br/>

A continuación la lista de métodos de instancia de la clase `datetime.timedelta`.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [total_seconds](https://docs.python.org/3/library/datetime.html#datetime.timedelta.total_seconds)()
  - Devuelve el número total de segundos contenidos en el `timedelta`.
```

<br>
<br>

---
(codigos-formatos-fechas)=
## Códigos de fechas

A continuación se presentan los códigos de fechas y tiempo que usan los métodos como `strftime()` o `strptime()`. Esta no es una lista completa, para una lista completa visitar [esta página](https://strftime.org/).

```{list-table}
:header-rows: 1
:name: date_codes

* - Código
  - Elemento
* - `%A`
  - Nombre día de la semana completo.
* - `%w`
  - Número de la semana (del 0-6, donde 0 es domingo).
* - `%d`
  - Día de mes (1-31).
* - `%b`
  - Nombre abreviado del mes.
* - `%B`
  - Nombre completo del mes.
* - `%m`
  - Número del mes (1-12).
* - `%y`
  - Año abreviado.
* - `%Y`
  - Año completo.
* - `%H`
  - Hora (0-24).
* - `%I`
  - Hora (0-12).
* - `%M`
  - Minutos (0-60).
* - `%S`
  - Segundos (0-60).
* - `%Z`
  - Nombre de la zona Horaria.
```
