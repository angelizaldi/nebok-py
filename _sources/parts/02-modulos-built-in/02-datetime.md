# Datetime

Es un módulo para trabajar con datos de tipo fecha. Es necesario importar el módulo `datetime`:
```python
# Importar todo el módulo
import datetime

# Importar una clase específica
from datetime import class_name
```
- _class_name_ es el nombre de clase que se desea importar,
- Estos solo son dos ejemplos de como importar el módulo, se puede usar cualquier rutina de importación, como importar con alias, importar funciones, constantes específicas, etc.

---
## ISO 8601

Muchos métodos de este módulo utilizan el formato ISO 8601, el cual es el siguiente:
> YYYY-MM-DDTHH:MM:SS

- YYYY: Año de cuatro dígitos, desde 0000 a 9999.
- MM: Mes de dos dígitos, del 01 a 12.
- DD: Día de dos dígitos, del 01 al 31.
- HH: Horas de dos dígitos, desde 00 a 23.
- MM: Minutos de dos dígitos, desde 00 a 59.
- SS: Segundos de dos dígitos, desde 00 a 59.

---
## Funciones

Funciones del módulo `datetime`.

<a name='strptime'></a>
**strptime**:

`datetime.strptime()`: Retorna un objeto datetime, pasando una cadena que contiene la fecha, e indicando las partes como códigos.
```python
datetime.strptime(date_string, format)
```

**Parámetros:**
- **`date_string`** \- `str`: La fecha. Los números que sean de un solo dígito (1-9) deben de tener un 0 antes.
- **`format`** \- `str`: Contiene los {ref}`date_codes` de la fecha, respetando la forma como está escrita en date_string, por ejemplo, si `date_string` = “21 June, 2018” entonces `format=“%d %B, %Y”`.

**Retorna:**
- `datetime`.

<br><br>

---
## Clases

Existen diferentes tipos de datos de fecha y tiempo, cada tipo es una clase dentro del módulo `datetime` y cada clase tiene métodos y atributos diferentes:
- `date`: (año, mes, día), Asume el calendario gregoriano.
- `time`: (hora, minuto, segundo, microsegundo, zona horaria), Asume que cada día tiene exactamente 24 horas, cada hora 60 minutos y cada minuto 60 segundos.
- `datetime`: (año, mes, día, hora, minuto, segundo, microsegundo, zona horaria), Combinación de `date` y `time`.
- `timedelta`: Representa la diferencia de dos fechas o tiempos. Se pueden hacer operaciones aritméticas con ojetos timedelta. 
- `tzinfo`: Objetos con información sobre la zona horaria.
- `timezone`: Implementar la clase base abstracta `tzinfo` como un desfase dijo de UTC.

```{warning}
En este sitio solo se presentarán las clases `date`, `time`, `datetime` y `timedelta`. Para más información sobre el módulo en general visitar la [página oficial](https://docs.python.org/3.8/library/datetime.html#module-datetime) de Python.
```

---
## Datetime

```{warning}
En este sitio no se documenta todas las características de la clase `datetime`, para un tratado completo visitar la [página oficial](https://docs.python.org/3/library/datetime.html#datetime-objects) de Python.
```

`datetime` es una clase que representa fechas y tiempo. Para crear una fecha y tiempo se puede usar el constructor o algunos métodos de clase también lo permiten.

**datetime**:

`datetime.datetime()`: Retorna una fecha y tiempo dando los parámetros individuales.
```python
datetime.datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0)
```

**Parámetros:**
- **`year`**, **`month`**, **`day`** \- `int`: Parámetros obligatorios.
- **`hour`**, **`minute`**, **`second`**, **`microsecond`** \- `int`: Parámetros opcionales, por default son cero.
- **`tzinfo`** \- `str`, `timezone`: Es la zona horaria, puedes usar un objeto creado con `datetime.timezone()` o usar una cadena, para ver las zonas horarias disponibles ver [Zonas Horarias](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).


**Retorna:**
- `datetime`.

<br><br>

---
### Atributos de instancia

Los atributos de istancia se aplican directamente sobre un objeto `datetime`
```python
X.part_name
```
- X \- `datetime.datetime`: Objeto.
- _part_name_ es el nombre de la parte que se quiere recuperar, las opciones son:
    - `year`: Retorna el año.
    - `month`: Retorna el mes.
    - `day`: Retornar el día.
    - `hour`: Retorna las horas.
    - `minute`: Retorna los minutos.
    - `seconds`: Retorna los segundos.
    - `microsecond`: Retorna los microsegundos.
    - `tzinfo`: Retorna la zona horaria.

---
### Métodos

#### Métodos de clase

Son métodos que se aplican directamente sobre la clase `datetime.datetime`.

```{list-table} TITLE
:header-rows: 1

* - Funciones
  - Descripción
* - [now](#now)(`tz=None`)
  - Retorna la fecha y hora actual del sistema.
* - [today](#today)(``)
  - Retorna la fecha actual del sistema. incluirá información del tiempo y la zona horaria.
* - [fromtimestamp](#fromtimestamp)(`timestamp, [tz=None]`)
  - Retorna la fecha y tiempo correspondiente a un timestamp.
* - [fromisoformat](#fromisoformat)(`date_string`)
  - Retorna una fecha pasando una cadena que representa una fecha en ISO 8601.
* - [fromisocalender](#fromisocalender)(`year, week, day`)
  - Retorna una fecha pasando sus elementos individuales, excluyendo los elementos correspondientes al tiempo.
```

----
#### Métodos de instancia

Son métodos que se aplican directamente en instancias (objetos) de la clase `datetime.datetime`.

```{list-table} TITLE
:header-rows: 1

* - Funciones
  - Descripción
* - [replace](#replace)(`part=val, ...`)
  - Retorna la misma fecha con una modificación en los elementos...
* - [strftime](#strftime)(`format`)
  - Retorna una cadena con una fecha en un formato personalizado.
* - [date](#date)(``)
  - Retorna la fecha de un objeto, excluyendo el tiempo.
* - [time](#time)(``)
  - Retorna el tiempo de un objeto, excluyendo la fecha.
* - [X.timetz](#timetz)(``)
  - Retorna el tiempo con información de la zona horaria de un objeto.
* - [tzname](#tzname)(``)
  - Retorna el nombre de la zona horaria de un objeto.
* - [timestamp](#timestamp)(``)
  - Retorna cuántos segundos han pasado desde el primero de enero de 1970...
* - [weekday](#weekday)(``)
  - Retorna el día de la semana de la fecha. Lunes es cero, domingo es...
* - [isoweekday](#isoweekday)(``)
  - Retorna el día de la semana de la fecha. Lunes es uno, domingo es...
* - [isocalender](#isocalender)(` `)
  - Retorna un `tuple` con los elementos de la fecha respetando ISO.
* - [isoformat](#isoformat)(``)
  - Retorna una cadena con los elementos de la fecha, respetando ISO 8601.
* - [astimezone](#astimezone)(`tz = None`)
  - Retorna la fecha y tiempo en una nueva zona horaria. Modifica los...
```

---
## Date

```{warning}
En este sitio no se documenta todas las características de la clase `date`, para un tratado completo visitar la [página oficial](https://docs.python.org/3.11/library/datetime.html#date-objects) de Python.
```

`date` es una clase que representa fechas. Para crear una fecha se puede usar el constructor o algunos métodos de clase también lo permiten.

---
**date**:

`datetime.date()`: Retorna una fecha dando los parámetros individuales.
```python
datetime.date(year, month, day)
```

**Parámetros:**
- **`year`**, **`month`**, **`day`** \- `int`: Valores correspondientes al año, mes y día.

**Retorna:**
- `date`.

<br><br>

---
### Atributos de instancia

Los atributos de istancia se aplican directamente sobre un objeto de la clase `datetime.date`.
```python
X.part_name
```
- X \- `datetime.date`: Objeto.
- _part_name_ es el nombre de la parte que se quiere recuperar, las opciones son:
    - `year`: Retorna el año.
    - `month`: Retorna el mes.
    - `day`: Retornar el día.
   
---
### Métodos

#### Métodos de clase

Son métodos que se aplican directamente sobre la clase `datetime.date`.

```{list-table} TITLE
:header-rows: 1

* - Funciones
  - Descripción
* - [today](#today_d)(``)
  - Retorna la fecha actual del sistema.
* - [fromtimestamp](#fromtimestamp_d)(`timestamp`)
  - Retorna la fecha correspondiente a un timestamp.
* - [fromisoformat](#fromisoformat_d)(`date_string`)
  - Retorna una fecha pasando una cadena que representa una fecha en ISO 8601.
* - [fromisocalender](#fromisocalender_d)(`year, week, day`)
  - Retorna una fecha pasando sus elementos individuales, excluyendo los elementos correspondientes al tiempo.
```

---
#### Métodos de instancia

Son métodos que se aplican directamente en instancias (objetos) de la clase `datetime.date`.

```{list-table} TITLE
:header-rows: 1

* - Funciones
  - Descripción
* - [replace](#replace_d)(`part=val, ...`)
  - Retorna la misma fecha con una modificación en los elementos...
* - [strftime](#strftime_d)(`format`)
  - Retorna una cadena con una fecha en un formato personalizado.
* - [date](#date_d)(``)
  - Retorna la fecha de un objeto.
* - [weekday](#weekday_d)(``)
  - Retorna el día de la semana de la fecha. Lunes es cero, domingo es...
* - [isoweekday](#isoweekday_d)(``)
  - Retorna el día de la semana de la fecha. Lunes es uno, domingo es...
* - [isocalender](#isocalender_d)(``)
  - Retorna un `tuple` con los elementos de la fecha respetando ISO.
* - [isoformat](#isoformat_d)(``)
  - Retorna una cadena con los elementos de la fecha, respetando ISO 8601.
```

---
## Time

```{warning}
En este sitio no se documenta todas las características de la clase `time`, para un tratado completo visitar la [página oficial](https://docs.python.org/3.11/library/datetime.html#time-objects) de Python.
```

`time` es una clase que representa tiempos. Para crear un tiempo se puede usar el constructor o algunos métodos de clase también lo permiten.

**time**:

`datetime.time()`: Retorna una fecha y tiempo dando los parámetros individuales.
```python
datetime.time(hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0)
```

**Parámetros:**
- **`hour`**, **`minute`**, **`second`**, **`microsecond`** \- `int`: Parámetros, por default son cero.
- **`tzinfo`** \- `str`, `timezone`: Es la zona horaria, puedes usar un objeto creado con `datetime.timezone()` o usar una cadena, para ver las zonas horarias disponibles ver [Zonas Horarias](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).


**Retorna:**
- `time`.

<br><br>

---
### Atributos de instancia

Los atributos de istancia se aplican directamente sobre un objeto `datetime.time`.
```python
X.part_name
```
- X \- `datetime.time`: Objeto.
- _part_name_ es el nombre de la parte que se quiere recuperar, las opciones son:
    - `hour`: Retorna las horas.
    - `minute`: Retorna los minutos.
    - `seconds`: Retorna los segundos.
    - `microsecond`: Retorna los microsegundos.
    - `tzinfo`: Retorna la zona horaria.

---
### Métodos

#### Métodos de clase


```{list-table} TITLE
:header-rows: 1

* - Funciones
  - Descripción
* - [fromisoformat](#fromisoformat_t)(`time_string`)
  - Retorna un tiempo pasando una cadena que representa un tiempo en ISO 8601.
```

---
#### Métodos de instancia

Son métodos que se aplican directamente en instancias (objetos) de la clase `datetime.time`.

```{list-table} TITLE
:header-rows: 1

* - Funciones
  - Descripción
* - [replace](#replace_t)(`part=val, ...`)
  - Retorna el mismo tiempo con una modificación en los elementos...
* - [strftime](#strftime_t)(`format`)
  - Retorna una cadena con el tiempo en un formato personalizado.
* - [tzname](#tzname)(``)
  - Retorna el nombre de la zona horaria de un objeto.
* - [isoformat](#isoformat)(``)
  - Retorna una cadena con los elementos del tiempo, respetando ISO 8601.
```

## Timedelta

```{warning}
En este sitio no se documenta todas las características de la clase `timedelta`, para un tratado completo visitar la [página oficial](https://docs.python.org/3.11/library/datetime.html#timedelta-objects) de Python.
```

`timedelta` es una clase que representa diferencias entre tiempos o fechas.

**timedelta**:

`datetime.timedelta()`: Crea objetos timedelta.
```python
datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
```

**Parámetros:**
- **`days`**, **`seconds`**, **`microseconds`**, **`milliseconds`**, **`minutes`**, **`hours`**, **`weeks`** \- `float` o `int`: Pueden ser números negativos.

**Retorna:**
- `timedelta`.

<br><br>

---
### Atributos de instancia

Los atributos de istancia se aplican directamente sobre un objeto `datetime.timedelta`.
```python
X.part_name
```
- X \- `datetime.time`: Objeto.
- _part_name_ es el nombre de la parte que se quiere recuperar, las opciones son:
    - `days`: Retorna los días.
    - `seconds`: Retorna los segundos.
    - `microsecond`: Retorna los microsegundos.

### Atributos de instancia

Son métodos que se aplican directamente en instancias (objetos) de la clase `datetime.timedelta`.

---
**total_seconds**:

`timedelta.total_seconds()`: Retorna el objeto timedelta en segundos.
```python
X.total_seconds()
```

**Parámetros:**
- **`X`** \- `timedelta`: Objeto.


**Retorna:**
- `int`.

<br><br>

---
## Códigos de fechas

A continuación se presentan los códigos de fechas y tiempo que usan funciones y métodos como `strftime()` o `.strptime()`. Esta no es una lista completa, para una lista completa visitar la siguiente [página](https://strftime.org/).

```{list-table} Códigos de fechas.
:header-rows: 1
:name: date_codes

* - Códigos.
  - Elemento.
* - `%A`.
  - Nombre día de la semana completo.
* - `%w`.
  - Número de la semana (del 0-6, donde 0 es domingo).
* - `%d`.
  - Día de mes (1-31).
* - `%b`.
  - Nombre abreviado del mes.
* - `%B`.
  - Nombre completo del mes.
* - `%m`.
  - Número del mes (1-12).
* - `%y`.
  - Año abreviado.
* - `%Y`.
  - Año completo.
* - `%H`.
  - Hora (0-24).
* - `%I`.
  - Hora (0-12).
* - `%M`.
  - Minutos (0-60).
* - `%S`.
  - Segundos (0-60).
* - `%Z`.
  - Nombre de la zona Horaria.
```

---
## Listado de métodos.

Este es un listado completo de todas las clases. Se recomienda visitar la sección de cada clase para encontrar un método en particular.

**Datetime**

---
<a name='now'></a>
**now**:

`datetime.now()`: Retorna la fecha y hora actual del sistema.
```python
datetime.datetime.now(tz=None)
```

**Parámetros:**
- **`tz`** \- `str`, `timezone`: Se puede especificar la zona horaria.
- • Es similar a `datetime.today()` si `tz=None`.


**Retorna:**
- `datetime`.

<br><br>

---
<a name='today'></a>
**today**:

`datetime.today()`: Retorna la fecha actual del sistema. incluirá información del tiempo y la zona horaria.
```python
datetime.datetime.today()
```

**Parámetros:**
- No tiene argumentos.


**Retorna:**
- `datime`.

<br><br>

---
<a name='fromtimestamp'></a>
**fromtimestamp**:

`datetime.fromtimestamp()`: Retorna la fecha y tiempo correspondiente a un timestamp.
```python
datetime.datetime.fromtimestamp(timestamp, [tz=None])
```

**Parámetros:**
- **`timestamp`** \- `int`: Segundos que han pasado desde el primero de enero de 1970.
- **`tz`** \- `str`: Zona horara.


**Retorna:**
- `datetime`.

<br><br>

---
<a name='fromisoformat'></a>
**fromisoformat**:

`datetime.fromisoformat()`: Retorna una fecha pasando una cadena que representa una fecha en ISO 8601.
```python
datetime.datetime.fromisoformat(date_string)
```

**Parámetros:**
- **`date_string`** \- `str`: Cadena con la fecha respetando ISO 8601.


**Retorna:**
- `datetime`.

<br><br>

---
<a name='fromisocalender'></a>
**fromisocalender**:

`datetime.fromisocalender()`: Retorna una fecha pasando sus elementos individuales, excluyendo los elementos correspondientes al tiempo.
```python
datetime.datetime.fromisocalender(year, week, day)
```

**Parámetros:**
- **`year`**, **`month`**, **`day`** \- `int`: Valores correspondientes al año, mes y día.


**Retorna:**
- `datetime`.

<br><br>

---
<a name='replace'></a>
**replace**:

`datetime.replace()`: Retorna la misma fecha con una modificación en los elementos especificados. Si se modifica la zona horaria (`tzinfo`), no se modificará la hora, solo la información de la zona horaria, para modificar la hora, usar el método `datetime.datetime.astimezone()`.
```python
X.replace(part=val, ...)
```

**Parámetros:**
- **`X`** \- `datetime`: Objeto.
- **`part`** \- `arg`: Es el nombre de la parte de la fecha a remplazar, separa con comas las partes. Puede ser: `year`, `month`, `day`, `hour`, `minute`, `second`, `microsecond`, `tzinfo`.
- **`val`** \- `int` o `float`: Valor nuevo de `part`.


**Retorna:**
- `datetime`.

<br><br>

---
<a name='strftime'></a>
**strftime**:

`datetime.strftime()`: Retorna una cadena con la en una fecha en un formato personalizado.
```python
X.strftime(format)
```

**Parámetros:**
- **`X`** \- `datetime`: Objeto.
- **`format`** \- `str`: Formato de la fecha usando los {ref}`date_codes`.


**Retorna:**
- `str`.

<br><br>

---
<a name='date'></a>
**date**:

`datetime.date()`: Retorna la fecha de un objeto, excluyendo el tiempo.
```python
X.date()
```

**Parámetros:**
- **`X`** \- `datetime`: Objeto.
- No tiene argumentos.


**Retorna:**
- `date`.

<br><br>

---
<a name='time'></a>
**time**:

`datetime.time()`: Retorna el tiempo de un objeto, excluyendo la fecha.
```python
X.time()
```

**Parámetros:**
- **`X`** \- `datetime`: Objeto.
- No tiene argumentos.


**Retorna:**
- `time`.

<br><br>

---
<a name='timetz'></a>
**timetz**:

`datetime.timetz()`: Retorna el tiempo con información de la zona horaria de un objeto.
```python
X.timetz()
```

**Parámetros:**
- **`X`** \- `datetime`: Objeto.
- No tiene argumentos.


**Retorna:**
- `time`.

<br><br>

---
<a name='tzname'></a>
**tzname**:

`datetime.tzname()`: Retorna el nombre de la zona horaria, de X `datetime`.
```python
X.tzname()
```

**Parámetros:**
- **`X`** \- `datetime`: Objeto.
- No tiene argumentos.


**Retorna:**
- `None` o `str`.

<br><br>

---
<a name='timestamp'></a>
**timestamp**:

`datetime.timestamp`: Retorna cuántos segundos han pasado desde el primero de enero de 1970 de la fecha.
```python
X.timestamp()
```

**Parámetros:**
- **`X`** \- `datetime`: Objeto.
- No tiene argumentos.


**Retorna:**
- `float`.

<br><br>

---
<a name='weekday'></a>
**weekday**:

`datetime.weekday()`: Retorna el día de la semana de la fecha. Lunes es cero, domingo es seis.
```python
X.weekday()
```

**Parámetros:**
- **`X`** \- `datetime`: Objeto.
- No tiene argumentos.


**Retorna:**
- `int`.

<br><br>

---
<a name='isoweekday'></a>
**isoweekday**:

`datetime.isoweekday()`: Retorna el día de la semana de la fecha. Lunes es uno, domingo es siete.
```python
X.isoweekday()
```

**Parámetros:**
- **`X`** \- `datetime`: Objeto.
- No tiene argumentos.


**Retorna:**
- `int`.

<br><br>

---
<a name='isocalender'></a>
**isocalender**:

`datetime.isocalender()`: Retorna un `tuple` con los elementos de la fecha respetando ISO.
```python
X.isocalender( )
```

**Parámetros:**
- **`X`** \- `datetime`: Objeto.
- No tiene argumentos.


**Retorna:**
- `tuple`.

<br><br>

---
<a name='isoformat'></a>
**isoformat**:

`datetime.isoformat()`: Retorna una cadena con los elementos de la fecha, respetando ISO 8601.
```python
X.isoformat( )
```

**Parámetros:**
- **`X`** \- `datetime`: Objeto.
- No tiene argumentos.


**Retorna:**
- `str`.

<br><br>

---
<a name='astimezone'></a>
**astimezone**:

`datetime.astimezone()`: Retorna la fecha y tiempo en una nueva zona horaria. Modifica los valores para sincronizarlos con la zona horaria.
```python
X.astimezone(tz = None)
```

**Parámetros:**
- **`X`** \- `datetime`: Objeto.
- **`tz`** \- `str`, `timezone`: La nueva zona horaria a usar.


**Retorna:**
- `datetime`.

<br><br>

**Date**

---
<a name='today_d'></a>
**today**:

`date.today()`: Retorna la fecha actual del sistema. incluirá información del tiempo y la zona horaria.
```python
datetime.date.today()
```

**Parámetros:**
- No tiene argumentos.


**Retorna:**
- `date`.

<br><br>

---
<a name='fromtimestamp_d'></a>
**fromtimestamp**:

`date.fromtimestamp()`: Retorna la fecha y tiempo correspondiente a un timestamp.
```python
datetime.date.fromtimestamp(timestamp, [tz=None])
```

**Parámetros:**
- **`timestamp`** \- `int`: Segundos que han pasado desde el primero de enero de 1970.
- **`tz`** \- `str`: Zona horara.


**Retorna:**
- `date`.

<br><br>

---
<a name='fromisoformat_d'></a>
**fromisoformat**:

`date.fromisoformat()`: Retorna una fecha pasando una cadena que representa una fecha en ISO 8601.
```python
datetime.date.fromisoformat(date_string)
```

**Parámetros:**
- **`date_string`** \- `str`: Cadena con la fecha respetando ISO 8601.


**Retorna:**
- `date`.

<br><br>

---
<a name='fromisocalender_d'></a>
**fromisocalender**:

`date.fromisocalender()`: Retorna una fecha pasando sus elementos individuales, excluyendo los elementos correspondientes al tiempo.
```python
datetime.date.fromisocalender(year, week, day)
```

**Parámetros:**
- **`year`**, **`month`**, **`day`** \- `int`: Valores correspondientes al año, mes y día.


**Retorna:**
- `date`.

<br><br>

---
<a name='replace_d'></a>
**replace**:

`date.replace()`: Retorna la misma fecha con una modificación en los elementos especificados.
```python
X.replace(part=val, ...)
```

**Parámetros:**
- **`X`** \- `date`: Objeto.
- **`part`** \- `arg`: Es el nombre de la parte de la fecha a remplazar, separa con comas las partes. Puede ser: `year`, `month` y `day`.
- **`val`** \- `int` o `float`: Valor nuevo de `part`.


**Retorna:**
- `date`.

<br><br>

---
<a name='strftime_d'></a>
**strftime**:

`date.strftime()`: Retorna una cadena con la en una fecha en un formato personalizado.
```python
X.strftime(format)
```

**Parámetros:**
- **`X`** \- `date`: Objeto.
- **`format`** \- `str`: Formato de la fecha usando los {ref}`date_codes`.


**Retorna:**
- `str`.

<br><br>

---
<a name='weekday_d'></a>
**weekday**:

`date.weekday()`: Retorna el día de la semana de la fecha. Lunes es cero, domingo es seis.
```python
X.weekday()
```

**Parámetros:**
- **`X`** \- `date`: Objeto.
- No tiene argumentos.


**Retorna:**
- `int`.

<br><br>

---
<a name='isoweekday_d'></a>
**isoweekday**:

`date.isoweekday()`: Retorna el día de la semana de la fecha. Lunes es uno, domingo es siete.
```python
X.isoweekday()
```

**Parámetros:**
- **`X`** \- `date`: Objeto.
- No tiene argumentos.


**Retorna:**
- `int`.

<br><br>

---
<a name='isocalender_d'></a>
**isocalender**:

`date.isocalender()`: Retorna un `tuple` con los elementos de la fecha respetando ISO.
```python
X.isocalender( )
```

**Parámetros:**
- **`X`** \- `date`: Objeto.
- No tiene argumentos.


**Retorna:**
- `tuple`.

<br><br>

---
<a name='isoformat_d'></a>
**isoformat**:

`date.isoformat()`: Retorna una cadena con los elementos de la fecha, respetando ISO 8601.
```python
X.isoformat( )
```

**Parámetros:**
- **`X`** \- `date`: Objeto.
- No tiene argumentos.


**Retorna:**
- `str`.

<br><br>


**time**

---
<a name='fromisoformat_t'></a>
**fromisoformat**:

`time.fromisoformat()`: Retorna un tiempo pasando una cadena que representa un tiempo en ISO 8601.
```python
datetime.time.fromisoformat(time_string)
```

**Parámetros:**
- **`time_string`** \- `str`: Cadena con el tiempo respetando ISO 8601.


**Retorna:**
- `time`.

<br><br>

---
<a name='replace_t'></a>
**replace**:

`datetime.replace()`: Retorna el mismo tiempo con una modificación en los elementos especificados.
```python
X.replace(part=val, ...)
```

**Parámetros:**
- **`X`** \- `time`: Objeto.
- **`part`** \- `arg`: Es el nombre de la parte del tiempo a remplazar, separa con comas las partes. Puede ser: `hour`, `minute`, `second`, `microsecond`, `tzinfo`.
- **`val`** \- `int` o `float`: Valor nuevo de `part`.


**Retorna:**
- `time`.

<br><br>

---
<a name='strftime_t'></a>
**strftime**:

`time.strftime()`: Retorna una cadena con el tiempo en un formato personalizado.
```python
X.strftime(format)
```

**Parámetros:**
- **`X`** \- `time`: Objeto.
- **`format`** \- `str`: Formato de la fecha usando los {ref}`date_codes`.


**Retorna:**
- `str`.

<br><br>

---
<a name='tzname_t'></a>
**tzname**:

`datetime.tzname()`: Retorna el nombre de la zona horaria de un objeto.
```python
X.tzname()
```

**Parámetros:**
- **`X`** \- `time`: Objeto.
- No tiene argumentos.


**Retorna:**
- `None` o `str`.

<br><br>

---
<a name='isoformat_t'></a>
**isoformat**:

`time.isoformat()`: Retorna una cadena con los elementos del tiempo, respetando ISO 8601.
```python
X.isoformat( )
```

**Parámetros:**
- **`X`** \- `time`: Objeto.
- No tiene argumentos.


**Retorna:**
- `str`.