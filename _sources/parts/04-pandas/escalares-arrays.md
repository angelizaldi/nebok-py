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

# Escalares y Arrays

En esta sección se revisan brevemente algunos escalares y _arrays_ de `pandas` que no son soportados por `numpy`. 

| Tipo de Dato | Escalar | _Array_ | Alias en cadena |
| --- | --- | --- | --- |
| Datetime | {ref}`pandas-scalars-timestamp` | [pd.arrays.DatetimeArray](https://pandas.pydata.org/docs/reference/api/pandas.arrays.DatetimeArray.html#pandas.arrays.DatetimeArray) | `'datetime64[ns, <tz>]'` |
| Timedelta | {ref}`pandas-scalars-timedelta` | [pd.arrays.TimedeltaArray](https://pandas.pydata.org/docs/reference/api/pandas.arrays.TimedeltaArray.html) | `'timedelta64[<freq>]'` |
| Period | {ref}`pandas-scalars-period` | [pd.arrays.PeriodArray](https://pandas.pydata.org/docs/reference/api/pandas.arrays.PeriodArray.html#pandas.arrays.PeriodArray) | `'period[<freq>]'` |
| Interval | {ref}`pandas-scalars-interval` | [pd.arrays.IntervalArray](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntervalArray.html#pandas.arrays.IntervalArray) | `'interval'`, `'Interval'`, `'Interval[<numpy_dtype>]'`, `'Interval[datetime64[ns, <tz>``'`, `'Interval[timedelta64[<freq>``'` |
| Categorical | (none) | [pd.Categorical](https://pandas.pydata.org/docs/reference/arrays.html#categoricals) | `'category'` | 
| String | `str` | [pd.arrays.StringArray](https://pandas.pydata.org/docs/reference/arrays.html#strings) | `'string'` |
| Nullable Integer | (none) | [pd.arrays.IntegerArray](https://pandas.pydata.org/docs/reference/arrays.html##nullable-integer) | `'Int8'`, `'Int16'`, `'Int32'`, `'Int64'`, `'UInt8'`, `'UInt16'`, `'UInt32'`, `'UInt64'` |
| Nullable Float  | (none) | [pd.arrays.FloatingArray](https://pandas.pydata.org/docs/reference/arrays.html#nullable-float) | `'Float32'`, `'Float64'` |
| Nullable Boolean  | `bool` | [pd.arrays.BooleanArray](https://pandas.pydata.org/docs/reference/arrays.html#nullable-boolean) | `'boolean'` |
| Sparse | (none) | [pd.arrays.SparseArray](https://pandas.pydata.org/docs/reference/arrays.html#sparse) | `'Sparse'`, `'Sparse[int`'`, `'Sparse[float`'` |

:::{caution}
En esta sección se revisarán solo los primeros cuatro (`Timestamp`, `Timedeltas`, `Period` e `Intervals`). Para más información sobre el resto de tipos digirse a los links de la tabla.
:::

<br/>

## Creación de _arrays_

Para crear objetos con algún tipo de dato con arrays o escalares presentados en esta sección se puede usar el parámetro _dtype_ y el alias en cadena del tipo de dato o a la clase de `pandas` equivalente. Ejemplo con `Series` de _nullable integer_:
```python
# Con alias de cadena
s = pd.Series(data, dtype='Int32')

# Con la clase
s = pd.Series(data, dtype=pd.Int32Dtype())
```


Para crear concretamente un _arreglo_ usar la función `pd.array()`:
```python
# Con alias de cadena
a = pd.array(data, dtype='Int32')

# Con la clase
a = pd.array(data, dtype=pd.Int32Dtype())
```
- En este ejemplo se retornaría un objeto de tipo `pd.arrays.IntegerArray`.

---
(pandas-scalars-timestamp)=
## Timestamp

El tipo `Timestamp` es un escalar similar a `datetime.datetime` y cuyo _array_ equivalente es `pd.arrays.DatetimeArray`. A diferencia de `np.datetime`, `pd.arrays.DatetimeArray` permite especificar la zona horaria.

Para crear un escalar `Timestamp` o un _array_ `DatetimeArray` se pueden usar los constructores:

```{list-table}
:header-rows: 1

* - Constructor
  - Descripción
* - [Timestamp](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.html)([ts_input, year, month, day, ...])
  - Reemplaza de `pandas` del objeto `datetime.datetime`.
* - [arrays.DatetimeArray](https://pandas.pydata.org/docs/reference/api/pandas.arrays.DatetimeArray.html)(values[, dtype, freq, copy])
  - _Array_ de `pandas` para datos de fecha y hora compatibles con _tz_ o sin _tz_.
* - [DatetimeTZDtype](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeTZDtype.html)([unit, tz])
  - Tipo de dato de fecha y hora que reconoce la zona horaria. Se puede usar como argumento del parámetro _dtype_.
```
- Existen diversas formas de específicar la fecha-tiempo en `Timestamp`, las principales son:
    -  `str`: Cadena que representa una fecha-tiempo, se puedo usar ISO 8601 u otros formatos.
    -  `year`, `month`, `day`, `hour`, `minute`, `second`, `microsecond`: Indicando los elementos individuales de la fecha y tiempo.
    -  Para más formas visitar el link en la tabla.
- Para la zona horaria se puede usar cadena del tipo `'Continent/City'`, parar conocer las posibles opciones visitar [esta página](http://www.healthstream.com/hlchelp/Administrator/Classes/HLC_Time_Zone_Abbreviations.htm).

**Ejemplo**
```{code-cell} ipython3
# Importar librería
import pandas as pd

# Con cadena ISO 8601
print(pd.Timestamp('2021-01-15T12:30:45'))

# Con cadena
print(pd.Timestamp('15/01/2021 12:30:45'))

# Indicando elementos individuales
print(pd.Timestamp(year=2021, month=12, day=15, hour=12, minute=30, second=45))
```

<br/>

---
### Atributos de `Timestamp`

:::{caution}
Algunos de estos atributos son atributos de clase y otros son atributos de instancia. Recordar que `pd.Timestamp` es una subclase de `datetime.datetime`, por lo que se puede consultar la sección de `ref`{builtin-datetime-datetime} para más información.
:::

Atributos de la clase `Timestamp`:
- `.asm8`: Retorna el objeto como `numpy.datetime64`.
- `.day`: Día del mes.
- `.day_of_week`: El día de la semana, donde lunes=0 y domingo=6.
- `.day_of_year`: El día ordinal del año.
- `.dayofweek`: El día de la semana, donde lunes=0, domingo=6.
- `.dayofyear`: El día ordinal del año.
- `.days_in_month`: Retorna el número de días en el mes.
- `.daysinmonth`: Retorna el número de días en el mes.
- `.fold`: Entre _\[0, 1]_. Se utiliza para eliminar la ambigüedad de los tiempos de pared durante un intervalo repetido..
- `.hour`: La Hora.
- `.is_leap_year`: Indica si la fecha pertenece a un año bisiesto.
- `.is_month_end`: Indica si la fecha es el último día del mes.
- `.is_month_start`: Indica si la fecha es el primer día del mes.
- `.is_quarter_end`: Indica si la fecha es el último día del trimestre.
- `.is_quarter_start`: Indica si la fecha es el primer día del trimestre.
- `.is_year_end`: Indica si la fecha es el último día del año.
- `.is_year_start`: Indica si la fecha es el primer día de un año.
- `.max`: La máxima fecha y hora representable, `datetime(MAXYEAR, 12, 31, 23, 59, 59, 999999, tzinfo=None)`.
- `.microsecond`: Los microsegundos.
- `.min`: La mínima fecha y hora representable, `datetime(MINYEAR, 1, 1, tzinfo=None)`.
- `.minute`: Los minutos.
- `.month`: El mes, donde enero=1, diciembre=12.
- `.nanosecond`: Los nanosegundos.
- `.quarter`: El trimestre.
- `.resolution`: La diferencia más pequeña posible entre objetos datetime no iguales, `timedelta(microsegundos=1)`.
- `.second`: Los segundos.
- `.tz`: Retorna la zona horaria.
- `.tzinfo`: Retorna la zona horaria.
- `.unit`: La abreviatura asociada a self._creso.
- `.value`: .
- `.week`: Retorna el número de semana del año.
- `.weekofyear`: Retorna el número de semana del año.
- `.year`: El año.
- Para más información visitar la [documentación](https://pandas.pydata.org/docs/reference/arrays.html#properties) de `pandas`.

<br/>

---
### Métodos de `Timestamp`

:::{caution}
Algunos de estos métodos son métodos de clase y otros son métodos de instancia. Recordar que `pd.Timestamp` es una subclase de `datetime.datetime`, por lo que se puede consultar la sección de `ref`{builtin-datetime-datetime} para más información.
:::

A continuación se enlistan los métodos de la clase `Timestamp`. 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [Timestamp.as_unit](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.as_unit.html)(unit[, round_ok])
  - Convierte el valor `int64` subyacente a la unidad dada.
* - [Timestamp.astimezone](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.astimezone.html)(tz)
  - Convierte la zona horaria a otra zona horaria. Modificando el tiempo.
* - [Timestamp.ceil](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.ceil.html)(freq[, ambiguous, nonexistent])
  - Redondea hacía arriba los datos a la frecuencia especificada.
* - [Timestamp.combine](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.combine.html)(date, time)
  - Combina objetos de tipo `datetime.date` y `datetime.time` en `Timestamp` con los mismos campos de fecha y hora.
* - [Timestamp.ctime](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.ctime.html)()
  - Retorna una cadena de estilo `ctime()`.
* - [Timestamp.date](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.date.html)()
  - Retorna un objeto de tipo `datetime.date` con el mismo año, mes y día.
* - [Timestamp.day_name](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.day_name.html)([locale])
  - Retorna el nombre del día con la configuración regional especificada.
* - [Timestamp.dst](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.dst.html)()
  - Retorna el ajuste por el horario de verano (DST).
* - [Timestamp.floor](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.floor.html)(freq[, ambiguous, nonexistent])
  - Redondea hacía abajo los datos a la frecuencia especificada.
* - [Timestamp.fromordinal](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.fromordinal.html)(ordinal[, tz])
  - Construye un `Timestamp` a partir de un ordinal gregoriano proléptico.
* - [Timestamp.fromtimestamp](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.fromtimestamp.html)(ts)
  - Construye un `Timestamp` desde la marca de tiempo POSIX usando la zona horaria local.
* - [Timestamp.isocalendar](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.isocalendar.html)()
  - Retorna un `namedtuple` que contiene año, número de semana y día de la semana.
* - [Timestamp.isoformat](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.isoformat.html)([sep, timespec])
  - Retorna el tiempo en un formato según ISO 8601.
* - [Timestamp.isoweekday](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.isoweekday.html)()
  - Retorna el día de la semana.
* - [Timestamp.month_name](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.month_name.html)([locale])
  - Retorna el nombre del mes con la configuración regional especificada.
* - [Timestamp.normalize](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.normalize.html)()
  - Normaliza la el _timestamp_ hasta la medianoche, preservando la información de tz.
* - [Timestamp.now](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.now.html)([tz])
  - Retorna un nuevo objeto `Timestamp` que representa la hora actual.
* - [Timestamp.replace](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.replace.html)([year, month, day, hour, ...])
  - Implementa `datetime.replace`. Retorna la misma fecha-tiempo con una modificación en los elementos especificados.
* - [Timestamp.round](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.round.html)(freq[, ambiguous, nonexistent])
  - Redondea la fecha-tiempo a la resolución especificada.
* - [Timestamp.strftime](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.strftime.html)(format)
  - Retorna una cadena con un formato especificado de la fecha-tiempo.
* - [Timestamp.time](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.time.html)()
  - Retorna el objeto `datetime.time` con la misma hora pero con `tzinfo=None`.
* - [Timestamp.timestamp](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.timestamp.html)()
  - Retorna la marca de tiempo POSIX como `float`.
* - [Timestamp.timetuple](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.timetuple.html)()
  - Retorna un `tuple` con los elementos de la fecha-tiempo, compatible con `time.localtime()`.
* - [Timestamp.timetz](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.timetz.html)()
  - Retorna el objeto `datetime.time` con la misma hora y mismo _tzinfo_.
* - [Timestamp.to_datetime64](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.to_datetime64.html)()
  - Retorna un objeto `numpy.datetime64`.
* - [Timestamp.to_julian_date](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.to_julian_date.html)()
  - Convierte `Timestamp` en una fecha juliana.
* - [Timestamp.to_numpy](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.to_numpy.html)([dtype, copy])
  - Retorna un objeto `numpy.datetime64`.
* - [Timestamp.to_period](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.to_period.html)([freq])
  - Retorna un período del cual esta fecha-tiempo es una observación.
* - [Timestamp.to_pydatetime](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.to_pydatetime.html)([warn])
  - Convierte un objeto `Timestamp` en un objeto de fecha y hora nativo de Python.
* - [Timestamp.today](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.today.html)([tz])
  - Retorna una fecha-tiempo con la hora actual en la zona horaria local.
* - [Timestamp.toordinal](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.toordinal.html)()
  - Retorna un ordinal gregoriano proléptico.
* - [Timestamp.tz_convert](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.tz_convert.html)(tz)
  - Convierte la zona horaria de a otra zona horaria, modificando el tiempo.
* - [Timestamp.tz_localize](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.tz_localize.html)(tz[, ambiguous, ...])
  - Convierte la zona horaria de a otra zona horaria, Modifica la hora.
* - [Timestamp.tzname](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.tzname.html)()
  - Retorna el nombre de la zona horaria.
* - [Timestamp.utcfromtimestamp](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.utcfromtimestamp.html)(ts)
  - Construye una fecha-hora _UTC_ con reconocimiento de zona horaria a partir de una marca de tiempo POSIX.
* - [Timestamp.utcnow](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.utcnow.html)()
  - Retorna una nueva fecha-tiempo que representa el día y la hora _UTC_.
* - [Timestamp.utcoffset](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.utcoffset.html)()
  - Retorna el desplazamiento _utc_.
* - [Timestamp.utctimetuple](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.utctimetuple.html)()
  - Retorna un `tuple` de tiempo _UTC_, compatible con `time.localtime()`.
* - [Timestamp.weekday]: 
  - Retorna el día de la semana.
```

<br/>

---
(pandas-scalars-timedelta)=
## Timedelta

`pd.Timedelta` representa la diferencia entre dos fechas-tiempo, es similar a `datetime.timedelta`. Su equivalente en _array_ es `pd.arrays.TimedeltaArray`.

Para crear un escalar `Timedelta` o un _array_ `TimedeltaArray` se pueden usar los constructores:

```{list-table}
:header-rows: 1

* - Constructor
  - Descripción
* - [Timedelta](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.html)([value, unit]): 
  - Representa una duración, que es la diferencia entre dos fechas y tiempo.
* - [arrays.TimedeltaArray](https://pandas.pydata.org/docs/reference/api/pandas.arrays.TimedeltaArray.html)(values[, dtype, freq, ...]): 
  - _Array_ de `pandas` para _timedeltas_.
```

<br/>

---
### Atributos de `Timedelta`

:::{caution}
Algunos de estos atributos son atributos de clase y otros son atributos de instancia. Recordar que `pd.Timedelta` es una subclase de `datetime.timedelta`, por lo que se puede consultar la sección de `ref`{builtin-datetime-timedelta} para más información.
:::

Atributos de la clase `Timedelta`. 
- `.asm8`: Retorna una vista escalar de un _array_ numpy `timedelta64`.
- `.components`: Retorna los componentes como un `namedtuple`.
- `.days`: Retorna los días del `Timedelta`.
- `.max`: El mayor objeto timedelta posible, `timedelta(days=999999999, hours=23, minutes=59, seconds=59, microseconds=999999)`.
- `.microseconds`: Retorna el número de microsegundos.
- `.min`: El menor objeto timedelta posible, `timedelta(-999999999)`.
- `.nanoseconds`: Retorna el número de nanosegundos _n_, donde _0 <= n < 1_ microsegundos.
- `.resolution`: La diferencia más pequeña posible entre objetos timedelta no iguales, `timedelta(microseconds=1)`.
- `.seconds`: Retorna el total de horas, minutos y segundos del `Timedelta` como segundos.
- `.unit`: .
- `.value`: .
- `.view(dtype)`: Compatibilidad con _viesws_ de arrays.
- Para más información visitar la [documentación](https://pandas.pydata.org/docs/reference/arrays.html#id1) de `pandas`.

<br/>

---
### Métodos de `Timedelta`

:::{caution}
Algunos de estos métodos son métodos de clase y otros son métodos de instancia. Recordar que `pd.Timedelta` es una subclase de `datetime.timedelta`, por lo que se puede consultar la sección de `ref`{builtin-datetime-timedelta} para más información.
:::

A continuación se enlistan los métodos de la clase `Timedelta`. 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [Timedelta.as_unit](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.as_unit.html)(unit[, round_ok])
  - Convierte el valor `int64` subyacente a la unidad dada.
* - [Timedelta.ceil](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.ceil.html)(freq)
  - Redondea hacía arriba la duración a la frecuencia especificada.
* - [Timedelta.floor](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.floor.html)(freq)
  - Redondea hacía abajo la duración a la frecuencia especificada.
* - [Timedelta.isoformat](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.isoformat.html)()
  - Retorna la duración en un formato según ISO 8601.
* - [Timedelta.round](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.round.html)(freq)
  - Redondea la duración a la frecuencia especificada.
* - [Timedelta.to_numpy](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.to_numpy.html)([dtype, copy])
  - Convierte el `Timedelta` a `timedelta64` de `numpy`.
* - [Timedelta.to_pytimedelta](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.to_pytimedelta.html)()
  - Convierte el `Timedelta` en un objeto `datetime.timedelta`.
* - [Timedelta.to_timedelta64](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.to_timedelta64.html)()
  - Retorna un objeto `numpy.timedelta64` con precisión 'ns'.
* - [Timedelta.total_seconds](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.total_seconds.html)()
  - Segundos totales en la duración.
```

---
(pandas-scalars-period)=
## Period

El tipo `Period` representa intervalos de tiempo y cuyo _array_ equivalente es `pd.arrays.PeriodArray`. 

Para crear un escalar `Period` o un _array_ `PeriodArray` se pueden usar los constructores:

```{list-table}
:header-rows: 1

* - Constructor
  - Descripción
* - [Period](https://pandas.pydata.org/docs/reference/api/pandas.Period.html)([value, freq, ordinal, year, month, ...])
  - Representa un periodo de tiempo.
* - [arrays.PeriodArray](https://pandas.pydata.org/docs/reference/api/pandas.arrays.PeriodArray.html)(values[, dtype, freq, copy])
  - _Array_ de `pandas` para periodos de tiempo.
* - [PeriodDtype](https://pandas.pydata.org/docs/reference/api/pandas.PeriodDtype.html)(freq)
  - Tipo de dato de periodos de tiempo. Se puede usar como argumento del parámetro _dtype_.
```

<br/>

---
### Atributos de `Period`

Atributos de la clase `Timedelta`:
- `.day`: Recupera el día del mes en el que cae un período.
- `.day_of_week`: Día de la semana en el que se encuentra el período, siendo lunes=0 y domingo=6.
- `.day_of_year`: Retorna el día del año.
- `.dayofweek`: Día de la semana en el que se encuentra el período, siendo lunes=0 y domingo=6.
- `.dayofyear`: Retorna el día del año.
- `.days_in_month`: Recupera el número total de días del mes en los que cae este período.
- `.daysinmonth`: Recupera el número total de días del mes en los que cae este período.
- `.end_time`: Recupera el `Timestamp` del final del período.
- `.freq`: .
- `.freqstr`: Retorna una representación de cadena de la frecuencia.
- `.hour`: Recupera el componente de hora del día del Período.
- `.is_leap_year`: Retorna `True` si el año del período es bisiesto.
- `.minute`: Recupera el minuto del componente de hora del Período.
- `.month`: Devuelva el mes en el que cae este Período.
- `.ordinal`: .
- `.quarter`: Retorna el trimestre en el que cae este Período.
- `.qyear`: Ejercicio económico en el que se encuentra el Periodo según su trimestre de inicio.
- `.second`: Recupera el componente de segundos del Periodo.
- `.start_time`: Recupera el `Timestamp` del inicio del período.
- `.week`: Recupera la semana del año en el período determinado.
- `.weekday`: Día de la semana en el que se encuentra el período, siendo lunes=0 y domingo=6.
- `.weekofyear`: Recupera la semana del año en el período determinado.
- `.year`: Devuelve el año en el que cae este Período.

<br/>

---
### Métodos de `Period`

Lorem ipsum dolor sit amet, consectetur adipiscing elit. 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [Period.asfreq](https://pandas.pydata.org/docs/reference/api/pandas.Period.asfreq.html)(freq[, how])
  - Convierte el período a la frecuencia deseada, al inicio o al final del intervalo.
* - [Period.now](https://pandas.pydata.org/docs/reference/api/pandas.Period.now.html)(freq)
  - Retorna el período de la fecha actual.
* - [Period.strftime](https://pandas.pydata.org/docs/reference/api/pandas.Period.strftime.html)(fmt)
  - Retorna una representación de cadena con determinado formato del `Period`.
* - [Period.to_timestamp](https://pandas.pydata.org/docs/reference/api/pandas.Period.to_timestamp.html)([freq, how])
  - Retorna la representación `Timestamp` del período.
```

<br/>

---
(pandas-scalars-interval)=
## Interval

El tipo `Interval` representa intervalos arbitrarios y cuyo _array_ equivalente es `pd.arrays.IntervalArray`. 

Para crear un escalar `Interval` o un _array_ `IntervalArray` se pueden usar los constructores:

```{list-table}
:header-rows: 1

* - Constructor
  - Descripción
* - [Period](https://pandas.pydata.org/docs/reference/api/pandas.Period.html)([left, right, closed])
  - Objeto inmutable que representa un intervalo arbitrario.
* - [arrays.IntervalArray](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntervalArray.html)(data[, closed, dtype, ...])
  - _Array_ de `pandas` para intervalos.
* - [IntervalDtype](https://pandas.pydata.org/docs/reference/api/pandas.IntervalDtype.html)([subtype, closed])
  - Tipo de dato de intervalos. Se puede usar como argumento del parámetro _dtype_.
```

<br/>

---
### Atributos de `Interval`

Atributos de la clase `Interval`:
- `.closed`: Cadena que describe el lado inclusivo de los intervalos.
- `.closed_left`: Verifica si el intervalo está cerrado en el lado izquierdo.
- `.closed_right`: Verifica si el intervalo está cerrado en el lado derecho.
- `.is_empty`: Indica si un intervalo está vacío, lo que significa que no contiene puntos.
- `.left`: Límite izquierdo para el intervalo.
- `.length`: Retorna la longitud del intervalo.
- `.mid`: Retorna el punto medio del intervalo.
- `.open_left`: Verifica si el intervalo está abierto en el lado izquierdo.
- `.open_right`: Verifica si el intervalo está abierto en el lado derecho.
- `.overlaps`: Verifica si dos objetos de intervalo se superponen.
- `.right`: Límite derecho para el intervalo.
