# Resampler

El objeto `Resampler` es un objeto retornado por lo métodos `DateFrame.resample()` o `Series.resample()`. Se utiliza para calcular agregados o transformar los datos a una nueva frecuencia, en una serie de tiempo. En esta sección se enlistarán los métodos de este objeto. Algunas características de este objeto son:
- Los grupos de datos están basados en periodos de tiempo con una frecuencia específica.
- Permite cálculo de agregados.
- Permite modificar la frecuencia de la serie. Ver {ref}`cookbook-resampling`.
- Permite manejar los valores perdidos.
- El objeto es "encadenable" (_pipe_), lo que permite múltiples operaciones al mismo tiempo.

<br/>

---
## Aggregates

Métodos para cálculos estadísticos y _aggregates_. 

```{list-table}
:header-rows: 1
:name: pandas-resampler-methods-aggregate

* - Método
  - Descripción
* - [Resampler.count](https://pandas.pydata.org/docs/reference/api/pandas.core.resample.Resampler.count.html)()
  - Calcula el recuento del grupo, excluyendo los valores faltantes.
* - [Resampler.first](https://pandas.pydata.org/docs/reference/api/pandas.core.resample.Resampler.first.html)([numeric_only, min_count, ...])
  - Determina la primer entrada de cada columna dentro de cada grupo.
* - [Resampler.last](https://pandas.pydata.org/docs/reference/api/pandas.core.resample.Resampler.last.html)([numeric_only, min_count, skipna])
  - Determina la última entrada de cada columna dentro de cada grupo.
* - [Resampler.max](https://pandas.pydata.org/docs/reference/api/pandas.core.resample.Resampler.max.html)([numeric_only, min_count])
  - Calcula el valor máximo del grupo.
* - [Resampler.mean](https://pandas.pydata.org/docs/reference/api/pandas.core.resample.Resampler.mean.html)([numeric_only])
  - Calcula la media de los grupos, excluyendo los valores faltantes.
* - [Resampler.median](https://pandas.pydata.org/docs/reference/api/pandas.core.resample.Resampler.median.html)([numeric_only])
  - Calcula la mediana de los grupos, excluyendo los valores faltantes.
* - [Resampler.min](https://pandas.pydata.org/docs/reference/api/pandas.core.resample.Resampler.min.html)([numeric_only, min_count])
  - Calcula el valor mínimo del grupo.
* - [Resampler.nunique](https://pandas.pydata.org/docs/reference/api/pandas.core.resample.Resampler.nunique.html)(*args, **kwargs)
  - Retorna el número de elementos únicos en el grupo.
* - [Resampler.ohlc](https://pandas.pydata.org/docs/reference/api/pandas.core.resample.Resampler.ohlc.html)(*args, **kwargs)
  - Calcula los valores de apertura, máximo, mínimo y cierre de un grupo, excluyendo los valores faltantes.
* - [Resampler.prod](https://pandas.pydata.org/docs/reference/api/pandas.core.resample.Resampler.prod.html)([numeric_only, min_count])
  - Calcular el producto de los valores del grupo.
* - [Resampler.quantile](https://pandas.pydata.org/docs/reference/api/pandas.core.resample.Resampler.quantile.html)([q])
  - Retorna el cuantil indicado.
* - [Resampler.sem](https://pandas.pydata.org/docs/reference/api/pandas.core.resample.Resampler.sem.html)([ddof, numeric_only])
  - Calcula el error estándar de la media de los grupos, excluyendo los valores faltantes.
* - [Resampler.size](https://pandas.pydata.org/docs/reference/api/pandas.core.resample.Resampler.size.html)()
  - Determina el tamaño de los grupos.
* - [Resampler.std](https://pandas.pydata.org/docs/reference/api/pandas.core.resample.Resampler.std.html)([ddof, numeric_only])
  - Calcula la desviación estándar de los grupos, excluyendo los valores faltantes.
* - [Resampler.sum](https://pandas.pydata.org/docs/reference/api/pandas.core.resample.Resampler.sum.html)([numeric_only, min_count])
  - Calcula la suma de los valores del grupo.
* - [Resampler.var](https://pandas.pydata.org/docs/reference/api/pandas.core.resample.Resampler.var.html)([ddof, numeric_only])
  - Calcula la varianza de los grupos, excluyendo los valores faltantes.
```

<br/>

---
## Aplicación de función

Métodos para aplicar funciones o transformaciones a los datos del objeto. 

```{list-table}
:header-rows: 1
:name: pandas-resampler-methods-apply

* - Método
  - Descripción
* - [Resampler.aggregate](https://pandas.pydata.org/docs/reference/api/pandas.core.resample.Resampler.aggregate.html)([func])
  - Calcula _aggregates_ usando una o más operaciones sobre el eje especificado.
* - [Resampler.apply](https://pandas.pydata.org/docs/reference/api/pandas.core.resample.Resampler.apply.html)([func])
  - Aplica funciones usando una o más operaciones sobre el eje especificado.
* - [Resampler.pipe](https://pandas.pydata.org/docs/reference/api/pandas.core.resample.Resampler.pipe.html)(func, *args, **kwargs)
  - Aplica la función _func_ a este objeto `Resampler` y retorna su resultado.
* - [Resampler.transform](https://pandas.pydata.org/docs/reference/api/pandas.core.resample.Resampler.transform.html)(arg, *args, **kwargs)
  - Función de llamada que produce un índice similar `Series` en cada grupo.
```

<br/>

---
## Indexación e iteración

Métodos para selección de elementos o iteración sobre los elementos. 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [Resampler.__iter__](https://pandas.pydata.org/docs/reference/api/pandas.core.resample.Resampler.__iter__.html)()
  - Iterador de grupo.
* - [Resampler.asfreq](https://pandas.pydata.org/docs/reference/api/pandas.core.resample.Resampler.asfreq.html)([fill_value])
  - Retorna los valores a la nueva frecuencia, esencialmente realiza un reindexación, con posbilidad de indicar un valor para los valores _NA_.
* - [Resampler.get_group](https://pandas.pydata.org/docs/reference/api/pandas.core.resample.Resampler.get_group.html)(name[, obj])
  - Retorna un `DataFrame` del grupo con el nombre proporcionado.
* - [Resampler.groups](https://pandas.pydata.org/docs/reference/api/pandas.core.resample.Resampler.groups.html)()
  - Retorna un `dict` de tipo {nombre del grupo -> etiquetas de grupo}.
* - [Resampler.indices](https://pandas.pydata.org/docs/reference/api/pandas.core.resample.Resampler.indices.html)()
  - Retorna un `dict` de tipo {nombre del grupo -> índices del grupo}.
```

<br/>

---
## Valores perdidos

Métodos útiles cuando se realiza _upsampling_ y se generan valores perdidos. 

```{list-table}
:header-rows: 1
:name: pandas-resampler-methods-upsamplig

* - Método
  - Descripción
* - [Resampler.bfill](https://pandas.pydata.org/docs/reference/api/pandas.core.resample.Resampler.bfill.html)([limit])
  - Rellena hacia atrás los valores faltantes en los datos.
* - [Resampler.ffill](https://pandas.pydata.org/docs/reference/api/pandas.core.resample.Resampler.ffill.html)([limit])
  - Rellena los valores hacia adelante los valores faltantes en los datos.
* - [Resampler.fillna](https://pandas.pydata.org/docs/reference/api/pandas.core.resample.Resampler.fillna.html)(method[, limit])
  - Rellena los valores faltantes indicando un método específico.
* - [Resampler.interpolate](https://pandas.pydata.org/docs/reference/api/pandas.core.resample.Resampler.interpolate.html)([method, axis, limit, ...])
  - Interpola valores entre marcas de tiempo según diferentes métodos.
* - [Resampler.nearest](https://pandas.pydata.org/docs/reference/api/pandas.core.resample.Resampler.nearest.html)([limit])
  - Rellena los valores faltantes utilizando el valor más cercano.
```
