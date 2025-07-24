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
- [](datetime-date): (año, mes, día), Asume el calendario gregoriano.
- [](datetime-time): (hora, minuto, segundo, microsegundo, zona horaria), Asume que cada día tiene exactamente 24 horas, cada hora 60 minutos y cada minuto 60 segundos.
- [](datetime-datetime): (año, mes, día, hora, minuto, segundo, microsegundo, zona horaria), Combinación de `date` y `time`.
- [](datetime-timedelta): Representa la diferencia de dos fechas o tiempos. Se pueden hacer operaciones aritméticas con objetos `timedelta`. 
- [tzinfo](https://docs.python.org/3/library/datetime.html#tzinfo-objects): Objetos con información sobre la zona horaria.
- [timezone](https://docs.python.org/3/library/datetime.html#timezone-objects): Implementa la clase base abstracta `tzinfo` como un desfase fijo de UTC.

```{warning}
En este sitio solo se presentarán las clases `date`, `time`, `datetime` y `timedelta`.
```

<br/>

---
(datetime-datetime)=
### Datetime


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
  - Los argumentos de _year_, _month_ y _day_ son obligatorios. `tzinfo` puede ser `None`, o un instancia de la subclase `tzinfo`. Los argumentos restantes deben ser números enteros.
```
**Notas**:
- `tzinfo` \- `tzinfo`: Es la zona horaria. Para más información ver {ref}`datetime-zonas-horarias`.

<br/>

---
#### Crear un _datetime_

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
Existen más métodos para crear fechas y tiempo, revisar {ref}`datetime-datetime-metodos-clase`.
:::

<br/>

---
#### Dar formato concreto a _datetime_

Para darle un formato concreto a un objeto `datetime` y retornarlo como cadena se puede usar el método de instancia `datetime.strftime()`, para ello se debe indicar una cadena con los {ref}`Códigos de fechas <date-codes>`.

```{code-cell} python3
# Crear una instancia
X = datetime.fromisoformat("2020-01-01 12:30:00")

# Imprimir la instancia en un formato concreto
print(X.strftime('%B %d, %Y at %H %p'))
```

<br/>

---
#### Operaciones con objetos _datetime_

Las opciones válidas que se pueden hacer con objetos `datetime` son:
- **Sumar o restar _timedelta_**: A un objeto `datetime` se le puede sumar o restar un objeto `timedelta` y retornar un objeto `datetime`. <br/> `datetime2 = datetime + timedelta` <br/> `datetime2 = datetime1 - timedelta`
- **Diferencia entre _datetimes_**: Se pueden restar dos objetos `datetime` y retornar un objeto `timedelta`. <br/> `timedelta = datetime1 - datetime2`
- **Comparaciones**: Se pueden usar operadores de  {ref}`built-in-operadores-comparacion` con dos objetos `datetime` y retornar `bool`. <br/> `datetime1 < datetime2 # Ejm. con '<'`

:::{tip}
Muchas funciones que aceptan valores numéricos como `min()` o `max()` se pueden usar con objetos `datetime` ya que se puede considerar a los objetos `datetime` como valores numéricos.
:::

<br/>

---
#### Atributos de clase de _datetime_

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

<br/>

(datedatetime-time-atributos-instancia)=
#### Atributos de instancia de _datetime_

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

:::{tip}
Para retornar el día de la semana revisar los métodos de instancia `.weekday()` y `.isoweekday()`.
:::

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - [day](https://docs.python.org/3/library/datetime.html#datetime.datetime.day)
  - Entre 1 y el número de días del mes dado del año dado.
* - [fold](https://docs.python.org/3/library/datetime.html#datetime.datetime.fold)
  - Entre [0, 1]. Se utiliza para eliminar la ambigüedad de los tiempos de pared durante un intervalo repetido.
* - [hour](https://docs.python.org/3/library/datetime.html#datetime.datetime.hour)
  - En rango (00 a 23).
* - [microsecond](https://docs.python.org/3/library/datetime.html#datetime.datetime.microsecond)
  - En rango (1000000).
* - [minute](https://docs.python.org/3/library/datetime.html#datetime.datetime.minute)
  - En rango (00 a 59).
* - [month](https://docs.python.org/3/library/datetime.html#datetime.datetime.month)
  - Entre 1 y 12 inclusivo.
* - [second](https://docs.python.org/3/library/datetime.html#datetime.datetime.second)
  - En rango (00 a 59).
* - [tzinfo](https://docs.python.org/3/library/datetime.html#datetime.datetime.tzinfo)
  - El objeto pasado como argumento de `tzinfo` al constructor de `datetime`, o `None` si no se pasó ninguno.
* - [year](https://docs.python.org/3/library/datetime.html#datetime.datetime.year)
  - Entre `MINYEAR` y `MAXYEAR` inclusivo.
```

<br/>

(datetime-datetime-metodos-clase)=
#### Métodos de clase de _datetime_

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


```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [combine](https://docs.python.org/3/library/datetime.html#datetime.datetime.combine)(date, time, tzinfo=self.tzinfo)
  - Devuelve un nuevo objeto de fecha y hora cuyos componentes de fecha son iguales a el objeto _date_ dado, y cuyos componentes de tiempo son iguales a los del objeto _time_ dado.
* - [fromisocalendar](https://docs.python.org/3/library/datetime.html#datetime.datetime.fromisocalendar)(year, week, day)
  - Devuelve una fecha y hora correspondiente a la fecha del calendario ISO especificada por _year_, _week_ y _day_.
* - [fromisoformat](https://docs.python.org/3/library/datetime.html#datetime.datetime.fromisoformat)(date_string)
  - Devuelve una fecha y hora correspondiente a una cadena de fecha en cualquier formato válido ISO 8601.
* - [fromordinal](https://docs.python.org/3/library/datetime.html#datetime.datetime.fromordinal)(ordinal)
  - Devuelve la fecha y hora correspondiente al ordinal gregoriano proléptico, donde el 1 de enero del año 1 tiene el ordinal 1.
* - [fromtimestamp](https://docs.python.org/3/library/datetime.html#datetime.datetime.fromtimestamp)(timestamp, tz=None)
  - Devuelve la fecha y hora locales correspondientes a la marca de tiempo POSIX, como es devuelto por `time.time()`.
* - [now](https://docs.python.org/3/library/datetime.html#datetime.datetime.now)(tz=None)
  - Devuelve la fecha y hora locales actuales.
* - [strptime](https://docs.python.org/3/library/datetime.html#datetime.datetime.strptime)(date_string, format)
  - Devuelve una fecha y hora correspondiente a _date_string_, de acuerdo con _format_.
* - [today](https://docs.python.org/3/library/datetime.html#datetime.datetime.today)()
  - Devuelve la fecha y hora local actual, con `tzinfo` `None`.
* - [utcfromtimestamp](https://docs.python.org/3/library/datetime.html#datetime.datetime.utcfromtimestamp)(timestamp)
  - Devuelve la fecha y hora UTC correspondiente a la marca de tiempo POSIX, con `tzinfo` igual a `None`.
* - [utcnow](https://docs.python.org/3/library/datetime.html#datetime.datetime.utcnow)()
  - Devuelve la fecha y hora UTC actuales, con `tzinfo` igual a `None`.
```

<br/>

#### Métodos de instancia de _datetime_

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

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [astimezone](https://docs.python.org/3/library/datetime.html#datetime.datetime.astimezone)(tz=None)
  - Devuelve un objeto `datetime` con el nuevo atributo `tzinfo` igual a _tz_, ajustando los datos de fecha y hora para que el resultado sea la misma hora UTC que `self`, pero en la hora local de _tz_.
* - [ctime](https://docs.python.org/3/library/datetime.html#datetime.datetime.ctime)()
  - Devuelve una cadena que representa la fecha y la hora.
* - [date](https://docs.python.org/3/library/datetime.html#datetime.datetime.date)()
  - Retorna la fecha de un objeto, excluyendo el tiempo.
* - [dst](https://docs.python.org/3/library/datetime.html#datetime.datetime.dst)()
  - Si `tzinfo` es `None`, devuelve `None`, de lo contrario, devuelve `self.tzinfo.dst(self)`.
* - [isocalendar](https://docs.python.org/3/library/datetime.html#datetime.datetime.isocalendar)()
  - Devuelve un `namedtuple` con con tres componentes: _year_, _week_ y _day_.
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
  - Si la instancia _d_ de `datetime` es _naive_, este método se comporta igual que `d.timetuple()` excepto que _tm_isdst_ se fuerza a 0 sin importar qué retorne `d.dst()`.
* - [weekday](https://docs.python.org/3/library/datetime.html#datetime.datetime.weekday)()
  - Devuelve el día de la semana como un número entero, donde el lunes es 0 y el domingo es 6.
```

<br/>
<br/>

---
(datetime-date)=
### Date

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

<br/>

#### Crear un _date_

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
Existen más métodos para crear fechas, revisar {ref}`datetime-date-metodos-clase`.
:::

<br/>

---
#### Dar formato concreto a _date_

Para darle un formato concreto a un objeto `date` y retornarlo como cadena se puede usar el método de instancia `date.strftime()`, para ello se debe indicar una cadena con los {ref}`Códigos de fechas <date-codes>`.

```{code-cell} python3
# Crear una instancia
X = date.fromisoformat("2020-01-01")

# Imprimir la instancia en un formato concreto
print(X.strftime('%B %d, %Y'))
```

<br/>

---
#### Operaciones con objetos _date_

Las opciones válidas que se pueden hacer con objetos `date` son:
- **Sumar o restar _timedelta_**: A un objeto `date` se le puede sumar o restar un objeto `timedelta` y retornar un objeto `date`. <br/> `date2 = date1 + timedelta` <br/> `date2 = date1 - timedelta`
- **Diferencia entre _dates_**: Se pueden restar dos objetos `date` y retornar un objeto `timedelta`. <br/> `timedelta = date1 - date2`
- **Comparaciones**: Se pueden usar operadores de  {ref}`built-in-operadores-comparacion` con dos objetos `date` y retornar `bool`. <br/> `date1 < date2 # Ejm. con '<'`

:::{tip}
Muchas funciones que aceptan valores numéricos como `min()` o `max()` se pueden usar con objetos `date` ya que se puede considerar a los objetos `date` como valores numéricos.
:::

<br/>

---
#### Atributos de clase de _date_

A continuación se presenta una lista de atributos de clase. Tener en cuenta que los atributos de clase son atributos asociados con la clase misma y no con las instancias.

Ejemplo de cómo usar un atributo de clase:

```{code-cell} python3
# Importar clase
from datetime import date

# Usar un atributo de clase
print(date.max)
```

<br/>

Lista de atributos de clase de `datetime.date`.

:::{tip}
Para retornar el día de la semana revisar los métodos de instancia `.weekday()` y `.isoweekday()`.
:::

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

<br/>

(datetime-date-atributos-instancia)=
#### Atributos de instancia de _date_

Los atributos de instancia se aplican directamente sobre un objeto `date`. 

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
 
<br/> 
 
(datetime-date-metodos-clase)=
#### Métodos de clase de _date_


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

<br/>

#### Métodos de instancia de _date_

Son métodos que se aplican directamente en instancias (objetos) de la clase `datetime.date`. 

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

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [ctime](https://docs.python.org/3/library/datetime.html#datetime.date.ctime)()
  - Devuelve una cadena que representa la fecha.
* - [isocalendar](https://docs.python.org/3/library/datetime.html#datetime.date.isocalendar)()
  - Devuelve un `namedtuple` con tres componentes: _year_, _week_ y _day_.
* - [isoformat](https://docs.python.org/3/library/datetime.html#datetime.date.isoformat)()
  - Devuelve una fecha correspondiente a una cadena de representa una fecha en cualquier formato válido ISO 8601.
* - [isoweekday](https://docs.python.org/3/library/datetime.html#datetime.date.isoweekday)()
  - Devuelve el día de la semana como un número entero, donde el lunes es _1_ y el domingo es _7_.
* - [replace](https://docs.python.org/3/library/datetime.html#datetime.date.replace)(year=self.year, month=self.month, day=self.day)
  - Devuelve una fecha con el mismo valor, excepto para aquellos parámetros a los que se le dieron nuevos valores.
* - [strftime](https://docs.python.org/3/library/datetime.html#datetime.date.strftime)(format)
  - Devuelve una cadena que representa la fecha, controlada por una cadena de formato explícito.
* - [timetuple](https://docs.python.org/3/library/datetime.html#datetime.date.timetuple)()
  - Devuelve un `time.struct_time` como el que devuelve `time.localtime()`.
* - [toordinal](https://docs.python.org/3/library/datetime.html#datetime.date.toordinal)()
  - Devuelve el ordinal gregoriano proléptico de la fecha, donde 1 de enero del año 1 tiene ordinal 1.
* - [weekday](https://docs.python.org/3/library/datetime.html#datetime.date.weekday)()
  - Devuelve el día de la semana como un número entero, donde el lunes es _0_ y el domingo es _6_.
```

<br/>
<br/>

---
(datetime-time)=
### Time

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
- `tzinfo` \- `tzinfo`: Es la zona horaria. Para más información ver {ref}`datetime-zonas-horarias`.

<br/>

---
#### Crear un _time_

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

<br/>

---
#### Dar formato concreto a _time_

Para darle un formato concreto a un objeto `time` y retornarlo como cadena se puede usar el método de instancia `time.strftime()`, para ello se debe indicar una cadena con los {ref}`Códigos de fechas <date-codes>`.

```{code-cell} python3
# Crear una instancia
X = time.fromisoformat("12:30:00")

# Imprimir la instancia en un formato concreto
print(X.strftime('at %H.%-M %p'))
```

<br/>

---
#### Atributos de clase de _time_

A continuación se presenta una lista de atributos de clase. Tener en cuenta que los atributos de clase son atributos asociados con la clase misma y no con las instancias.

Ejemplo de cómo usar un atributo de clase:

```{code-cell} python3
# Importar clase
from datetime import time

# Usar un atributo de clase
print(time.max)
```

<br/>

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

<br/>

(datetime-time-atributos-instancia)=
#### Atributos de instancia de _time_

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
 
<br/> 
 
#### Métodos de clase de _time_

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

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [fromisoformat](https://docs.python.org/3/library/datetime.html#datetime.time.fromisoformat)(time_string)
  - Retorna una hora correspondiente a un _time_string_ en cualquier formato válido ISO 8601.
```

<br/>

#### Métodos de instancia de _time_

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

<br/>
<br/>

---
(datetime-timedelta)=
### Timedelta

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

<br/>

---
#### Crear un _timedelta_

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
#### Operaciones con objetos _timedelta_

Es posible realizar operaciones aritméticas con objetos `timedelta`. Para más información visitar la [documentación](https://docs.python.org/3/library/datetime.html#timedelta-objects) de Python.

- **Suma y resta de objetos _timedelta_**: Se pueden sumar o restar dos objetos `timedelta` con los operadores `+` y `-` respectivamente y retornar otro objeto `timedelta`. <br/> `timedelta3 = timedelta1 + timedelta2` <br> `timedelta3 = timedelta1 + timedelta2`
- **Multiplicar un objeto timedelta por un número**: Se puede multiplicar un objeto `timedelta` por un número `int` o `float` con el operador `*` y retornar otro objeto `timedelta`. Cada componente se multiplicará por el factor indicado. <br/> `timedelta2 = timedelta1 * int` <br> `timedelta2 = timedelta1 * float`
- **Dividir un objeto timedelta**: Es posible dividir un objeto `timedelta` entre otro objeto `timedelta` o entre un número `int` o `float` con el operador `/` y retornar otro objeto `timedelta`. <br/> `timedelta3 = timedelta1 / timedelta2` <br/> `timedelta2 = timedelta1 / int` <br> `timedelta2 = timedelta1 / float` <br> Es posible además calcular el módulo o la división parte entera con los operadores `%` y `//` respectivamente o con la función `divmode()`. 

<br/>

---
#### Atributos de clase de _timedelta_

A continuación se presenta una lista de atributos de clase. Tener en cuenta que los atributos de clase son atributos asociados con la clase misma y no con las instancias.

Ejemplo de cómo usar un atributo de clase:

```{code-cell} python3
# Importar clase
from datetime import timedelta

# Usar un método de clase
print(timedelta.max)
```

<br/>

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

<br/>

#### Atributos de instancia de _timedelta_

Los atributos de instancia se aplican directamente sobre un objeto `timedelta`. 

Ejemplo de cómo usar un atributo de instancia:

```{code-cell} python3
# Importar clase
from datetime import timedelta

# Crear una instancia
X = timedelta(days=1, minutes=30)

# Usar un atributo de instancia
print(X.seconds)
```

<br/>

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - [days](https://docs.python.org/3/library/datetime.html#datetime.timedelta.days)
  - Entre -999,999,999 y 999,999,999 inclusivos.
* - [seconds](https://docs.python.org/3/library/datetime.html#datetime.timedelta.seconds)
  - Entre 0 y 86,399 inclusivos.
* - [microseconds](https://docs.python.org/3/library/datetime.html#datetime.timedelta.microseconds)
  - Entre 0 y 999,999 inclusivos.
```

<br/>

#### Métodos de instancia de _timedelta_

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

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [total_seconds](https://docs.python.org/3/library/datetime.html#datetime.timedelta.total_seconds)()
  - Devuelve el número total de segundos contenidos en el `timedelta`.
```

<br/>

---
(datetime-zonas-horarias)=
## Zonas horarias

### Crear objeto con zona horaria

Para crear un objeto `datetime` o `time` con zona horaria existen dos alternativas:

**1. Usando _timedelta_ y _timezone_**: Es posible usar un objeto `timedelta` para indicar el desplazamiento con respecto al timepo universal coordinado [UTC](https://es.wikipedia.org/wiki/Tiempo_universal_coordinado) y utilizar este desfase en la función `timezone()` asignándolo al parámetro `tzinfo` . Ejemplo:

```python
from datetime import datetime, timedelta, timezone

# Definir desfase con respecto a UTC
MX = timezone(timedelta(hours=-6))

# Definir zona horaria
dt = datetime(2017, 12, 30, 15, 9, 3, tzinfo = MX)
```

**2. Usar módulo _zoneinfo_**: Se puede usar el constructor de la clase [ZoneInfo](https://docs.python.org/3/library/zoneinfo.html#zoneinfo.ZoneInfo) del módulo _built-in_ [zoneinfo](https://docs.python.org/3/library/zoneinfo.html), junto con una cadena del tipo _’Continent/City’_ para indicar la zona horaria. Para ver las zonas horarias disponibles usar la función [zoneinfo.available_timezones()](https://docs.python.org/3/library/zoneinfo.html#zoneinfo.available_timezones). Alternativamente revisar [Zonas Horarias](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).

```python
from datetime import datetime
from zoneinfo import ZoneInfo

# Especificar zona horaria
MX = ZoneInfo("America/Mexico_City ")

# Definir zona horaria
dt = datetime(2017, 12, 30, 15, 9, 3, tzinfo = MX)
```

**3. Usar módulo _dateutil_**: Se puede usar la función [gettz](https://dateutil.readthedocs.io/en/stable/tz.html#dateutil.tz.gettz) del módulo `tz` del paquete [dateutil](https://dateutil.readthedocs.io/en/stable/index.html) (es necesario instalarlo), junto con una cadena del tipo _’Continent/City’_ para indicar la zona horaria. Para ver las zonas horarias revisar [Zonas Horarias](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).

```python
from datetime import datetime
from dateutil import tz

# Especificar zona horaria
MX = tz.gettz("America/Mexico_City ")

# Definir zona horaria
dt = datetime(2017, 12, 30, 15, 9, 3, tzinfo = MX)
```

<br/>

### Cambiar zona horaria

Para modficar la zona horaria de un objeto se puede hacer de dos maneras, una manteniendo la misma hora y otro modificando la hora para ajustarla a la nueva zona horaria:

:::{tip}
Para usar la zona horaria _UTC_ usar el atributo `.utc` de la clase `datetime.timezone`: <br/> `tz=timezone.utc`
:::

**1. Mantener misma hora**: Para modificar la zona horaria pero mantener la misma hora se puede usar el método `.replace()` y usar un argumento válido de nueva la zona horaria con `tzinfo`:

```python
# Reemplazar zona horaria
dt.replace(tzinfo=ZoneInfo("America/Mexico_City"))
```

**2. Modifcar hora**: Para modificar la zona horaria y ajustarla a una nueva zona horaia se puede usar el método `.astimezone()`:

:::{warning}
Este método solo es válido con objetos `datetime.datetime`.
:::

```python
# Reemplazar zona horaria
dt.astimezone(tz=ZoneInfo("America/Mexico_City "))
```

<br/>

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

<br/>

---
(codigos-formatos-fechas)=
## Códigos de fechas

A continuación se presentan los códigos de fechas y tiempo que usan los métodos como `strftime()` o `strptime()`. Esta no es una lista completa, para una lista completa visitar [esta página](https://strftime.org/).

```{list-table}
:header-rows: 1
:name: date-codes

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
