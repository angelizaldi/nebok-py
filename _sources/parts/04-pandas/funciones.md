# Funciones

En esta sección se enlistan las funciones que forman parte de la librería `pandas`.

---
## Creación y conversión de objetos

### Numéricas

Lorem ipsum dolor sit amet, consectetur adipiscing elit. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [to_numeric](https://pandas.pydata.org/docs/reference/api/pandas.to_numeric.html)(arg[, errors, downcast, ...])
  - Convierte un objeto a un tipo numérico, si la conversión es posible.
```

<br/>

### Fechas y tiempo

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [bdate_range](https://pandas.pydata.org/docs/reference/api/pandas.bdate_range.html)([start, end, periods, freq, tz, ...])
  - Retorna un `DatetimeIndex` con una frecuencia específica con el día hábil como predeterminado.
* - [date_range](https://pandas.pydata.org/docs/reference/api/pandas.date_range.html)([start, end, periods, freq, tz, ...])
  - Retorna un `DatetimeIndex` con una frecuencia específica.
* - [interval_range](https://pandas.pydata.org/docs/reference/api/pandas.interval_range.html)([start, end, periods, freq, ...])
  - Genera un `IntervalIndex` indicando las características del intervalo.
* - [period_range](https://pandas.pydata.org/docs/reference/api/pandas.period_range.html)([start, end, periods, freq, name])
  - Retorna un `PeriodIndex` de frecuencia fija.
* - [timedelta_range](https://pandas.pydata.org/docs/reference/api/pandas.timedelta_range.html)([start, end, periods, freq, ...])
  - Retorna un `TimedeltaIndex` de frecuencia fija con el día como valor predeterminado.
* - [to_datetime](https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html)(arg[, errors, dayfirst, ...])
  - Convierte el argumento a `datetime64`.
* - [to_timedelta](https://pandas.pydata.org/docs/reference/api/pandas.to_timedelta.html)(arg[, unit, errors])
  - Convierte el argumento a `timedelta64`.
```

<br/>

## Datos perdidos

Funciones que retornan información sobre valores nulos en objetos. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [isna](https://pandas.pydata.org/docs/reference/api/pandas.isna.html)(obj)
  - Detecta valores nulos para un objeto similar a un arreglo.
* - [isnull](https://pandas.pydata.org/docs/reference/api/pandas.isnull.html)(obj)
  - Detecta valores nulos para un objeto similar a un arreglo.
* - [notna](https://pandas.pydata.org/docs/reference/api/pandas.notna.html)(obj)
  - Detecta valores no nulos para un objeto similar a un arreglo.
* - [notnull](https://pandas.pydata.org/docs/reference/api/pandas.notnull.html)(obj)
  - Detecta valores no nulos para un objeto similar a un arreglo.
```

<br/>

## Graficado

Funciones útiles para crear gráficas de objetos. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [andrews_curves](https://pandas.pydata.org/docs/reference/api/pandas.plotting.andrews_curves.html)(frame, class_column[, ax, ...])
  - Genera un gráfico `matplotlib` para visualizar grupos de datos multivariados.
* - [autocorrelation_plot](https://pandas.pydata.org/docs/reference/api/pandas.plotting.autocorrelation_plot.html)(series[, ax])
  - Gráfico de autocorrelación para series de tiempo.
* - [bootstrap_plot](https://pandas.pydata.org/docs/reference/api/pandas.plotting.bootstrap_plot.html)(series[, fig, size, samples])
  - Gráfico Bootstrap sobre estadísticas medias, medianas y de rango medio.
* - [boxplot](https://pandas.pydata.org/docs/reference/api/pandas.plotting.boxplot.html)(data[, column, by, ax, fontsize, ...])
  - Crea un diagrama de caja a partir de las columnas de un `DataFrame` .
* - [deregister_matplotlib_converters](https://pandas.pydata.org/docs/reference/api/pandas.plotting.deregister_matplotlib_converters.html)()
  - Remueve los _formateadores_ y _convertidores_ de `pandas`.
* - [lag_plot](https://pandas.pydata.org/docs/reference/api/pandas.plotting.lag_plot.html)(series[, lag, ax])
  - Gráfico de defases para series de tiempo.
* - [parallel_coordinates](https://pandas.pydata.org/docs/reference/api/pandas.plotting.parallel_coordinates.html)(frame, class_column[, ...])
  - Trazado de coordenadas paralelas.
* - [plot_params](https://pandas.pydata.org/docs/reference/api/pandas.plotting.plot_params.html)()
  - Almacena opciones de trazado de `pandas`.
* - [radviz](https://pandas.pydata.org/docs/reference/api/pandas.plotting.radviz.html)(frame, class_column[, ax, color, ...])
  - Traza un conjunto de datos multidimensional en 2D.
* - [register_matplotlib_converters](https://pandas.pydata.org/docs/reference/api/pandas.plotting.register_matplotlib_converters.html)()
  - Registra _formateadores_ y _convertidores_ de `pandas` con `matplotlib`.
* - [scatter_matrix](https://pandas.pydata.org/docs/reference/api/pandas.plotting.scatter_matrix.html)(frame[, alpha, figsize, ax, ...])
  - Grafica una matriz de diagramas de dispersión.
* - [table](https://pandas.pydata.org/docs/reference/api/pandas.plotting.table.html)(ax, data, **kwargs)
  - Función auxiliar para convertir `DataFrame` y `Series` a `matplotlib.table`.
```

<br/>

## Hash

Funciones útiles para retornar objetos _hash_ de arrays u objetos de `pandas`. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [util.hash_array](https://pandas.pydata.org/docs/reference/api/pandas.util.hash_array.html)(vals[, encoding, hash_key, ...])
  - Dado un arreglo 1d, devuelve un arreglo de números enteros deterministas.
* - [util.hash_pandas_object](https://pandas.pydata.org/docs/reference/api/pandas.util.hash_pandas_object.html)(obj[, index, ...])
  - Retorna un _hash_ de datos del `Index`/`Series`/`DataFrame`.
```

<br/>

---
## Información sobre tipos de fecha y hora

Funciones útiles para inferir frecuencias o formatos en datos que representan fechas y tiempo. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [infer_freq](https://pandas.pydata.org/docs/reference/api/pandas.infer_freq.html)(index)
  - Infiere la frecuencia más probable dado el índice de entrada.
* - [tseries.api.guess_datetime_format](https://pandas.pydata.org/docs/reference/api/pandas.tseries.api.guess_datetime_format.html)(dt_str[, ...])
  - Determina el formato de fecha y hora de una cadena de fecha y hora. El valor retornado contendrá el formatos con {ref}`Códigos de fechas <date-codes>`. Para usar esta función se puede importar como `from pandas.tseries.api import guess_datetime_format`.
```

<br/>

## Manipulación De Datos

### Categorización

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [cut](https://pandas.pydata.org/docs/reference/api/pandas.cut.html)(x, bins[, right, labels, retbins, ...])
  - Crea categorías de acuerdo a qué rango pertenece un valor. Las categorías estarán jerarquizadas. No garantiza que cada _bin_ tenga el mismo número de _data points_, para ellos usar la función `pd.qcut()`.
* - [factorize](https://pandas.pydata.org/docs/reference/api/pandas.factorize.html)(values[, sort, use_na_sentinel, ...])
  - Codifica el objeto asignándole a cada categoría un valor único en una variable categórica.
* - [qcut](https://pandas.pydata.org/docs/reference/api/pandas.qcut.html)(x, q[, labels, retbins, precision, ...])
  - Divide una columna en _q_ categorías, basado en cuantiles. Produce una variable categórica para indicar a cuál cuantil pertenece. Garantiza _bins_ del mismo tamaño.
```

<br/>

### Dummies, crosstab, eval y unique

Lorem ipsum dolor sit amet, consectetur adipiscing elit. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [crosstab](https://pandas.pydata.org/docs/reference/api/pandas.crosstab.html)(index, columns[, values, rownames, ...])
  - Retorna una tabla de contingencia, que retorna el número de ocurrencias para combinaciones de valores de dos columnas.
* - [eval](https://pandas.pydata.org/docs/reference/api/pandas.eval.html)(expr[, parser, engine, local_dict, ...])
  - Evalua una cadena que describe operaciones entre elementos de un objeto. **EJEMPLO**
* - [from_dummies](https://pandas.pydata.org/docs/reference/api/pandas.from_dummies.html)(data[, sep, default_category])
  - Crea una columna categórica a partie de un `DataFrame` con _dummy variables_.
* - [get_dummies](https://pandas.pydata.org/docs/reference/api/pandas.get_dummies.html)(data[, prefix, prefix_sep, ...])
  - Convierte variables categóricas en _dummy variables_. Básicamentecada valor único de una columna categórica la convierte en una nueva columna, cuyos valores contendrán unos y ceros indicando si cada fila tenía ese valor categórico.
* - [unique](https://pandas.pydata.org/docs/reference/api/pandas.unique.html)(values)
  - Retorna los valores únicos basados ​​en una tabla _hash_.
```

<br/>

### Reshaping

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [lreshape](https://pandas.pydata.org/docs/reference/api/pandas.lreshape.html)(data, groups[, dropna])
  - Modifica la forma de los datos tabular de _wide format_ a _long format_. Operación contraria a _pivot_. Ofrece más versatibilidad que `pd.melt()`.
* - [melt](https://pandas.pydata.org/docs/reference/api/pandas.melt.html)(frame[, id_vars, value_vars, var_name, ...])
  - Modifica la forma de los datos tabular de _wide format_ a _long format_. Operación contraria a _pivot_. Para un mayor control en el _reshaping_ usar la función `pd.lreshape()`.
* - [pivot](https://pandas.pydata.org/docs/reference/api/pandas.pivot.html)(data, *, columns[, index, values])
  - Sirve para modificar una tabla de _long format_ a _wide format_. Esta función no soporta _aggregates_, para ello utilizar `pd.pivot_table()`.
* - [pivot_table](https://pandas.pydata.org/docs/reference/api/pandas.pivot_table.html)(data[, values, index, columns, ...])
  - Sirve para modificar una tabla de _long format_ a _wide format_. Para cada valor único de una columna categórica calcula algo sobre los valores de una columna de valores. También se puede hacer lo mismo para las combinaciones únicas de los valores de dos o más columnas categóricas y se puede hacer más de un calculo sobre las columna de valores.
* - [wide_to_long](https://pandas.pydata.org/docs/reference/api/pandas.wide_to_long.html)(df, stubnames, i, j[, sep, suffix])
  - Modifica la forma de los datos tabular de _wide format_ a _long format_. Operación contraria a _pivot_.
```

<br/>

### Uniones y apilaciones

```{list-table}
:header-rows: 1
:name: pandas-func-joins

* - Función
  - Descripción
* - [concat](https://pandas.pydata.org/docs/reference/api/pandas.concat.html)(objs, *[, axis, join, ignore_index, ...])
  - Concatena objetos pandas a lo largo de un eje particular. La concatenación se puede hacer por posición o por índices. Además se puede especificar que se cree una `MultiIndex` que indique a que objeto pertenece cada parte.
* - [merge](https://pandas.pydata.org/docs/reference/api/pandas.merge.html)(left, right[, how, on, left_on, ...])
  - Une `DataFrame` o `Series` con nombre, de una manera similar a un _join_ de SQL. Permite indicar el tipo de _join_ y se puede hacer con base a valores de columnas o los índices.
* - [merge_asof](https://pandas.pydata.org/docs/reference/api/pandas.merge_asof.html)(left, right[, on, left_on, ...])
  - Es similar a un _left-join_, con la diferencia de que las coincidencias de los _ids_ no tienen que ser idénticas, sino aproximaciones. Es útil con objetos con fechas y tiempos. Ambos objetos deben estar ordenador por la columna/índice que se usará como _id_.
* - [merge_ordered](https://pandas.pydata.org/docs/reference/api/pandas.merge_ordered.html)(left, right[, on, left_on, ...])
  - Ejecuta un _join_ con opción de rellenar o interpolar valores nulos.
```

<br/>

---
## I/O

### Archivo de texto

Funciones útiles para I/O de archivos de texto como csv, tsv, etc. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [DataFrame.to_csv](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html)([path_or_buf, sep, na_rep, ...])
  - Exporta el objeto en un archivo de valores separados por comas (csv).
* - [read_csv](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)(filepath_or_buffer, *[, sep, ...])
  - Importa un archivo de valores separados por comas (csv) en `DataFrame`.
* - [read_fwf](https://pandas.pydata.org/docs/reference/api/pandas.read_fwf.html)(filepath_or_buffer, *[, colspecs, ...])
  - Importa una tabla de con delimitadores fijos en `DataFrame`.
* - [read_table](https://pandas.pydata.org/docs/reference/api/pandas.read_table.html)(filepath_or_buffer, *[, sep, ...])
  - Importa un archivo delimitado en `DataFrame`.
```

<br/>

### Excel

Funciones útiles para archivos de _Excel_. 

**EJEMPLOS**

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [DataFrame.to_excel](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_excel.html)(excel_writer, *[, ...])
  - Exporta un objeto en una hoja de Excel.
* - [ExcelFile](https://pandas.pydata.org/docs/reference/api/pandas.ExcelFile.html)(path_or_buffer[, engine, ...])
  - Clase para analizar hojas tabulares de Excel en objetos `DataFrame`.
* - [ExcelFile.book](https://pandas.pydata.org/docs/reference/api/pandas.ExcelFile.book.html)()
  - .
* - [ExcelFile.parse](https://pandas.pydata.org/docs/reference/api/pandas.ExcelFile.parse.html)([sheet_name, header, names, ...])
  - Lee un archivo de excel y lo convierte a un `DataFrame`.
* - [ExcelFile.sheet_names](https://pandas.pydata.org/docs/reference/api/pandas.ExcelFile.sheet_names.html)()
  - Lee un archivo de excel y lo convierte a un
* - [ExcelWriter](https://pandas.pydata.org/docs/reference/api/pandas.ExcelWriter.html)(path[, engine, date_format, ...])
  - Clase para escribir objetos `DataFrame` en hojas de Excel.
* - [Styler.to_excel](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.to_excel.html)(excel_writer[, sheet_name, ...])
  - Exporta un objeto `Styler` en una hoja de Excel.
* - [read_excel](https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html)(io[, sheet_name, header, names, ...])
  - Importa un archivo de Excel en un `DataFrame`.
```

<br/>

### Feather

Funciones útiles para archivos _feather_. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [DataFrame.to_feather](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_feather.html)(path, **kwargs)
  - Exporta un `DataFrame` al formato binario  _feather_.
* - [read_feather](https://pandas.pydata.org/docs/reference/api/pandas.read_feather.html)(path[, columns, use_threads, ...])
  - Importa un objeto con formato _feather_ desde la ruta del archivo.
```

<br/>

### HDFStore

Funciones útiles para archivos _HDFStore_. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [HDFStore.append](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.append.html)(key, value[, format, axes, ...])
  - Agrega a la tabla en el archivo.
* - [HDFStore.get](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.get.html)(key)
  - Importa el objeto de `pandas` almacenado en el archivo.
* - [HDFStore.groups](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.groups.html)()
  - Retorna un `list` de todos los nodos de nivel superior.
* - [HDFStore.info](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.info.html)()
  - Retorna información detallada sobre el archivo.
* - [HDFStore.keys](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.keys.html)([include])
  - Retorna un `list` de claves correspondientes a objetos almacenados en _HDFStore_.
* - [HDFStore.put](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.put.html)(key, value[, format, index, ...])
  - Exporta un objeto en _HDFStore_.
* - [HDFStore.select](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.select.html)(key[, where, start, stop, ...])
  - Importa el objeto de `pandas` almacenado en el archivo, opcionalmente según los criterios de _where_.
* - [HDFStore.walk](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.walk.html)([where])
  - Recorra la jerarquía de grupos de _pytables_ para objetos de `pandas`.
* - [read_hdf](https://pandas.pydata.org/docs/reference/api/pandas.read_hdf.html)(path_or_buf[, key, mode, errors, ...])
  - Importa un archivo _HDFStore_.
```

<br/>

### HTML

Funciones útiles para archivos _HTML_. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [DataFrame.to_html](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_html.html)([buf, columns, col_space, ...])
  - Exporta un `DataFrame` como una tabla HTML.
* - [Styler.to_html](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.to_html.html)([buf, table_uuid, ...])
  - Exporta un objeto `Styler`  a una tabla, búfer o cadena un objeto a un archivo HTML-CSS.
* - [read_html](https://pandas.pydata.org/docs/reference/api/pandas.read_html.html)(io, *[, match, flavor, header, ...])
  - Importa tablas HTML en un `list` de objetos `DataFrame`.
```

<br/>

### JSON

Funciones útiles para archivos _JSON_. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [DataFrame.to_json](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_json.html)([path_or_buf, orient, ...])
  - Convierte el objeto en una cadena JSON.
* - [build_table_schema](https://pandas.pydata.org/docs/reference/api/pandas.io.json.build_table_schema.html)(data[, index, ...])
  - Crea un esquema de tabla desde `data`.
* - [json_normalize](https://pandas.pydata.org/docs/reference/api/pandas.json_normalize.html)(data[, record_path, meta, ...])
  - Normalice datos JSON semiestructurados en una tabla plana.
* - [read_json](https://pandas.pydata.org/docs/reference/api/pandas.read_json.html)(path_or_buf, *[, orient, typ, ...])
  - Convierte una cadena JSON en un objeto pandas.
```

<br/>

### LaTeX

Funciones útiles para archivos de _LaTeX_. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [DataFrame.to_latex](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_latex.html)([buf, columns, header, ...])
  - Representa un objeto en una tabla tabular de LaTeX.
* - [Styler.to_latex](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.to_latex.html)([buf, column_format, ...])
  - Exporta un objeto Styler en un archivo, búfer o cadena en formato LaTeX.
```

<br/>

### ORC

Funciones útiles para archivos _ORC_. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [DataFrame.to_orc](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_orc.html)([path, engine, index, ...])
  - Exporta un `DataFrame` al formato _ORC_.
* - [read_orc](https://pandas.pydata.org/docs/reference/api/pandas.read_orc.html)(path[, columns, dtype_backend, ...])
  - Importa un objeto _ORC_ desde la ruta del archivo, devolviendo un `DataFrame`.
```

<br/>

### Parquet

Funciones útiles para archivos _Parquet_. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [DataFrame.to_parquet](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_parquet.html)([path, engine, ...])
  - Exporta un `DataFrame` al formato _parquet_ binario.
* - [read_parquet](https://pandas.pydata.org/docs/reference/api/pandas.read_parquet.html)(path[, engine, columns, ...])
  - Importa un objeto _parquet_ desde la ruta del archivo, devolviendo un `DataFrame`.
```

<br/>

### Pickle

Funciones útiles para archivos con extensión `.pkl`. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [DataFrame.to_pickle](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_pickle.html)(path, *[, compression, ...])
  - Serializa el objeto en un archivo `.pkl`.
* - [read_pickle](https://pandas.pydata.org/docs/reference/api/pandas.read_pickle.html)(filepath_or_buffer[, ...])
  - Importa un objeto de `pandas` (o cualquier objeto) desde un archivo `.pkl`.
```

<br/>

### Portapapeles

Funciones para copiar y pegar datos desde el portapapeles. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [DataFrame.to_clipboard](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_clipboard.html)(*[, excel, sep])
  - Copie el objeto al portapapeles del sistema.
* - [read_clipboard](https://pandas.pydata.org/docs/reference/api/pandas.read_clipboard.html)([sep, dtype_backend])
  - Pegue texto del portapapeles y pasarlo a `pd.read_csv()`.
```

<br/>

### SAS

Funciones útiles para archivos de _SAS_.  

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [read_sas](https://pandas.pydata.org/docs/reference/api/pandas.read_sas.html)(filepath_or_buffer, *[, format, ...])
  - Importa archivos _SAS_ almacenados en formato _XPORT_ o _SAS7BDAT_.
```

<br/>

### SPSS

Funciones útiles para archivos de _SPSS_. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [read_spss](https://pandas.pydata.org/docs/reference/api/pandas.read_spss.html)(path[, usecols, ...])
  - Importa archivos _SPSS_ desde la ruta del archivo y devuelva un `DataFrame`.
```

<br/>

### SQL

Funciones útiles para importar o exportar datos desde una base de datos SQL. 

**EJEMPLO** de cómo crear conexión y funciones.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [DataFrame.to_sql](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_sql.html)(name, con, *[, schema, ...])
  - Escribe registros almacenados en un `DataFrame` a una base de datos SQL.
* - [read_sql](https://pandas.pydata.org/docs/reference/api/pandas.read_sql.html)(sql, con[, index_col, ...])
  - Lee un _query_ o una tabla de una base de datos en un `DataFrame`. **ejemplo**
* - [read_sql_query](https://pandas.pydata.org/docs/reference/api/pandas.read_sql_query.html)(sql, con[, index_col, ...])
  - Ejecuta un _query_ y guarda el resultado en un `DataFrame`.
* - [read_sql_table](https://pandas.pydata.org/docs/reference/api/pandas.read_sql_table.html)(table_name, con[, schema, ...])
  - Lee una tabla de una base de datos. en un `DataFrame`.
```

<br/>

### Stata

Funciones útiles para trabajar con archivos de _Stata_. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [DataFrame.to_stata](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_stata.html)(path, *[, convert_dates, ...])
  - Exporta `DataFrame` al formato de datos _Stata_.
* - [StataReader.data_label](https://pandas.pydata.org/docs/reference/api/pandas.io.stata.StataReader.data_label.html)()
  - Etiqueta de datos de retorno del archivo _Stata_.
* - [StataReader.value_labels](https://pandas.pydata.org/docs/reference/api/pandas.io.stata.StataReader.value_labels.html)()
  - Retorna un `dict` anidado asociando cada nombre de variable a su valor y etiqueta.
* - [StataReader.variable_labels](https://pandas.pydata.org/docs/reference/api/pandas.io.stata.StataReader.variable_labels.html)()
  - Retorna un `dict` asociando cada nombre de variable con la etiqueta correspondiente.
* - [StataWriter.write_file](https://pandas.pydata.org/docs/reference/api/pandas.io.stata.StataWriter.write_file.html)()
  - Exporta `DataFrame` al formato de datos _Stata_.
* - [read_stata](https://pandas.pydata.org/docs/reference/api/pandas.read_stata.html)(filepath_or_buffer, *[, ...])
  - Importa el archivo un _Stata_ en `DataFrame`.
```

<br/>

### XML

Funciones útiles para archivos _XML_.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [DataFrame.to_xml](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_xml.html)([path_or_buffer, index, ...])
  - Renderizar un `DataFrame` a un documento XML.
* - [read_xml](https://pandas.pydata.org/docs/reference/api/pandas.read_xml.html)(path_or_buffer, *[, xpath, ...])
  - Importa un documento _XML_ en un objeto `DataFrame`.
```

