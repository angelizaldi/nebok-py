# Anexos

## Frecuencias y _offsets_

El argumento _freq_ de muchas funciones y métodos que tienen que ver con datos de tipo `datime-like`, `timedelta-like` o `period-like` se puede definir de las siguientes maneras:

---
(pd-anexos-offsets)=
### Alias de _offsets_

Los alias para frecuencias comunes en series de tiempo. 

```{list-table}
:header-rows: 1

* - Código
  - Descripción
* - B
  - Frecuencia de días hábiles.
* - BME
  - Frecuencia de fin de mes hábil.
* - BMS
  - Frecuencia de inicio del mes hábil.
* - BQE
  - Frecuencia de cierre del trimestre comercial.
* - BQS
  - Frecuencia de inicio del trimestre comercial.
* - BYE
  - Frecuencia de cierre de ejercicio.
* - BYS
  - Frecuencia de inicio del año comercial.
* - C
  - frecuencia de días hábiles personalizada.
* - CBME
  - frecuencia de fin de mes comercial personalizada.
* - CBMS
  - frecuencia de inicio de mes comercial personalizada.
* - D
  - Frecuencia del día calendario.
* - ME
  - Frecuencia de fin de mes.
* - MS
  - Frecuencia de inicio del mes.
* - QE
  - frecuencia de fin de trimestre.
* - QS
  - Frecuencia de inicio del trimestre.
* - SME
  - Frecuencia de fin de mes (día 15 y fin de mes).
* - SMS
  - Frecuencia de inicio quincenal (1º y 15º).
* - W
  - frecuencia semanal.
* - YE
  - Frecuencia de fin de año.
* - YS
  - Frecuencia de inicio del año.
* - bh
  - Frecuencia del horario comercial.
* - cbh
  - frecuencia de horario comercial personalizada.
* - h
  - Horas.
* - min
  - Minutos.
* - ms
  - Milisegundos.
* - ns
  - Nanosegundos.
* - s
  - Segundos.
* - us
  - Microsegundos.
```

:::{tip}
Se pueden crear _offsets_ más específicos indicando valores numéricos, junto con combinaciones de varios códigos, por ejemplo, `5h30min`.
:::

<br/>

---
### Alias de periodos

Los alias para frecuencias comunes en series de tiempo. 

```{list-table}
:header-rows: 1

* - Código
  - Descripción
* - B
  - Frecuencia de días hábiles.
* - D
  - Frecuencia del día calendario.
* - M
  - frecuencia mensual.
* - Q
  - frecuencia trimestral.
* - W
  - frecuencia semanal.
* - Y
  - frecuencia anual.
* - h
  - frecuencia horaria.
* - min
  - frecuencia minuciosa.
* - ms
  - milisegundos.
* - ns
  - nanosegundos.
* - s
  - en segundo lugar la frecuencia.
* - us
  - microsegundos.
```

<br/>

---
### Alias con prefijos

Se pueden añadir prefijos a los alias de frecuencias para crear frecuencias indicando días de la semanas o meses específicos.

:::{caution}
La tabla muestra frecuencias del tipo `(B)Q(E)(S)` esto para indicar que se puede aplicar en cualquiera de las variantes de `Q`, por ejemplo:
- `QE`
- `QS`
- `BQE`
- `BQS`
:::

```{list-table}
:header-rows: 1

* - Código
  - Descripción
* - (B)Q(E)(S)
  - Frecuencia trimestral, el año finaliza en octubre.
* - (B)Q(E)(S)-DEC
  - Frecuencia trimestral, el año finaliza en diciembre. Lo mismo que "QE".
* - (B)Q(E)(S)-JAN
  - Frecuencia trimestral, el año finaliza en enero.
* - (B)Q(E)(S)-FEB
  - Frecuencia trimestral, el año finaliza en febrero.
* - (B)Q(E)(S)-MAR
  - Frecuencia trimestral, el año finaliza en marzo.
* - (B)Q(E)(S)-APR
  - Frecuencia trimestral, el año finaliza en abril.
* - (B)Q(E)(S)-MAY
  - Frecuencia trimestral, el año finaliza en mayo.
* - (B)Q(E)(S)-JUN
  - Frecuencia trimestral, el año finaliza en junio.
* - (B)Q(E)(S)-JUL
  - Frecuencia trimestral, el año finaliza en julio.
* - (B)Q(E)(S)-AUG
  - Frecuencia trimestral, el año finaliza en agosto.
* - (B)Q(E)(S)-SEP
  - Frecuencia trimestral, el año finaliza en septiembre.
* - (B)Q(E)(S)-NOV
  - Frecuencia trimestral, el año finaliza en noviembre.
* - (B)Y(E)(S)-NOV
  - Frecuencia anual, anclada a finales de noviembre.
* - (B)Y(E)(S)-DEC
  - Frecuencia anual, anclada a finales de diciembre. Lo mismo que 'YE'.
* - (B)Y(E)(S)-JAN
  - Frecuencia anual, anclada a finales de enero.
* - (B)Y(E)(S)-FEB
  - Frecuencia anual, anclada a finales de febrero.
* - (B)Y(E)(S)-MAR
  - Frecuencia anual, anclada a finales de marzo.
* - (B)Y(E)(S)-APR
  - Frecuencia anual, anclada a finales de abril.
* - (B)Y(E)(S)-MAY
  - Frecuencia anual, anclada a finales de mayo.
* - (B)Y(E)(S)-JUN
  - Frecuencia anual, anclada a finales de junio.
* - (B)Y(E)(S)-JUL
  - Frecuencia anual, anclada a finales de julio.
* - (B)Y(E)(S)-AUG
  - Frecuencia anual, anclada a finales de agosto.
* - (B)Y(E)(S)-SEP
  - Frecuencia anual, anclada a finales de septiembre.
* - (B)Y(E)(S)-OCT
  - Frecuencia anual, anclada a finales de octubre.
* - W-FRI
  - Frecuencia semanal (viernes).
* - W-MON
  - Frecuencia semanal (lunes).
* - W-SAT
  - Frecuencia semanal (sábados).
* - W-SUN
  - Frecuencia semanal (domingos). Igual que "W".
* - W-THU
  - Frecuencia semanal (jueves).
* - W-TUE
  - Frecuencia semanal (martes).
* - W-WED
  - Frecuencia semanal (miércoles).
```
<br/>

Para más información visitar la [documentación](https://pandas.pydata.org/docs/user_guide/timeseries.html#offset-aliases).
