# Estadísticas

Funciones para cálculos estadísticos.

:::{warning}
Para una lista completa visitar la [documentación](https://numpy.org/doc/stable/reference/routines.statistics.html#statistics) de `numpy`.
:::

---
## Correlaciones

Funciones para cálculos de convarianzas y correlaciones.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [corrcoef](https://numpy.org/doc/stable/reference/generated/numpy.corrcoef.html)(x[, y, rowvar, bias, ddof, dtype])
  - Devuelve los coeficientes de correlación producto-momento de Pearson.
* - [correlate](https://numpy.org/doc/stable/reference/generated/numpy.correlate.html)(a, v[, mode])
  - Correlación cruzada de dos arreglos unidimensionales.
* - [cov](https://numpy.org/doc/stable/reference/generated/numpy.cov.html)(m[, y, rowvar, bias, ddof, fweights, ...])
  - Estima la matriz de covarianza, dados los datos y pesos.
```

<br>

## Estadísticos de orden

Funciones para cálculos de rangos, cuantiles y percentiles. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [nanpercentile](https://numpy.org/doc/stable/reference/generated/numpy.nanpercentile.html)(a, q[, axis, out, ...])
  - Calcula el percentil q-ésimo de los datos a lo largo del eje especificado, ignorando los valores `NaN`.
* - [nanquantile](https://numpy.org/doc/stable/reference/generated/numpy.nanquantile.html)(a, q[, axis, out, ...])
  - Calcula el cuantil q-ésimo de los datos a lo largo del eje especificado, ignorando los valores `NaN`.
* - [percentile](https://numpy.org/doc/stable/reference/generated/numpy.percentile.html)(a, q[, axis, out, ...])
  - Calcula el percentil q-ésimo de los datos a lo largo del eje especificado.
* - [ptp](https://numpy.org/doc/stable/reference/generated/numpy.ptp.html)(a[, axis, out, keepdims])
  - Rango de valores (máximo - mínimo) a lo largo de un eje.
* - [quantile](https://numpy.org/doc/stable/reference/generated/numpy.quantile.html)(a, q[, axis, out, overwrite_input, ...])
  - Calcula el cuantil q-ésimo de los datos a lo largo del eje especificado.
```

<br>

## Histogramas

Funciones para cálculo de histogramas. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [bincount](https://numpy.org/doc/stable/reference/generated/numpy.bincount.html)(x, /[, weights, minlength])
  - Cuenta el número de ocurrencias de cada valor en la matriz de entradas no negativas.
* - [digitize](https://numpy.org/doc/stable/reference/generated/numpy.digitize.html)(x, bins[, right])
  - Devuelve los índices de los _bins_ a los que pertenece cada valor en el arreglo de entrada.
* - [histogram](https://numpy.org/doc/stable/reference/generated/numpy.histogram.html)(a[, bins, range, density, weights])
  - Calcula el histograma de un conjunto de datos.
* - [histogram2d](https://numpy.org/doc/stable/reference/generated/numpy.histogram2d.html)(x, y[, bins, range, density, ...])
  - Calcula el histograma bidimensional de dos muestras de datos.
* - [histogram_bin_edges](https://numpy.org/doc/stable/reference/generated/numpy.histogram_bin_edges.html)(a[, bins, range, weights])
  - Función para calcular solo los extremos de los _bins_ utilizados por la función `np.histogram()`.
* - [histogramdd](https://numpy.org/doc/stable/reference/generated/numpy.histogramdd.html)(sample[, bins, range, density, ...])
  - Calcula el histograma multidimensional de algunos datos.
```

<br>

## Medidas de dispersión

Funciones para cálculo de medidas de dispersión como varianzas y desviaciones estándar. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [nanstd](https://numpy.org/doc/stable/reference/generated/numpy.nanstd.html)(a[, axis, dtype, out, ddof, ...])
  - Calcula la desviación estándar a lo largo del eje especificado, ignorando los `NaN`.
* - [nanvar](https://numpy.org/doc/stable/reference/generated/numpy.nanvar.html)(a[, axis, dtype, out, ddof, ...])
  - Calcula la varianza a lo largo del eje especificado, ignorando los `NaN`.
* - [std](https://numpy.org/doc/stable/reference/generated/numpy.std.html)(a[, axis, dtype, out, ddof, keepdims, where])
  - Calcula la desviación estándar a lo largo del eje especificado.
* - [var](https://numpy.org/doc/stable/reference/generated/numpy.var.html)(a[, axis, dtype, out, ddof, keepdims, where])
  - Calcula la varianza a lo largo del eje especificado.
```

<br>

## Medidas de tendencia central

Funciones para cálculo de medidadas de tendencia cental como medias y medianas. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [average](https://numpy.org/doc/stable/reference/generated/numpy.average.html)(a[, axis, weights, returned, keepdims])
  - Calcula el promedio ponderado a lo largo del eje especificado.
* - [mean](https://numpy.org/doc/stable/reference/generated/numpy.mean.html)(a[, axis, dtype, out, keepdims, where])
  - Calcula la media aritmética a lo largo del eje especificado.
* - [median](https://numpy.org/doc/stable/reference/generated/numpy.median.html)(a[, axis, out, overwrite_input, keepdims])
  - Calcula la mediana a lo largo del eje especificado.
* - [nanmean](https://numpy.org/doc/stable/reference/generated/numpy.nanmean.html)(a[, axis, dtype, out, keepdims, where])
  - Calcula la media aritmética a lo largo del eje especificado, ignorando `NaNs`. alt: None
* - [nanmedian](https://numpy.org/doc/stable/reference/generated/numpy.nanmedian.html)(a[, axis, out, overwrite_input, ...])
  - Calcula la mediana a lo largo del eje especificado, ignorando los `NaN`.
```

<br>

