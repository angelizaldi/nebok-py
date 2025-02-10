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

# Funciones

En esta sección se enlistan las funciones que forman parte de la librería de `pandas`.

---
## Creación y conversión de objetos

Funciones para crear objetos nuevos o convertir objetos a otros tipos.

### Numéricas

Funciones que convierten objetos a tipos numéricos.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [to_numeric](https://pandas.pydata.org/docs/reference/api/pandas.to_numeric.html)(arg[, errors, downcast, ...])
  - Convierte un objeto a un tipo numérico, si la conversión es posible.
```

<br/>

### Fechas y tiempo

Funciones que generar o convierten objetos a tipos `datetime-like`.

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
  - Convierte el argumento a `datetime64`. Es posible indicar el formato en el está las fechas usando {ref}`codigos-formatos-fechas`.
* - [to_timedelta](https://pandas.pydata.org/docs/reference/api/pandas.to_timedelta.html)(arg[, unit, errors])
  - Convierte el argumento a `timedelta64`.
```

Patrones útiles:
```python
# Convertir columna a datetine
df['date_col']=pd.to_datetime(df['col'])

# Crear rango de fechas con periodos especificos y freq especifica
pd.date_range(start='YYYY-MM-DD', periods, freq)
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

Funciones con diversas utilidades. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [crosstab](https://pandas.pydata.org/docs/reference/api/pandas.crosstab.html)(index, columns[, values, rownames, ...])
  - Retorna una tabla de contingencia, que retorna el número de ocurrencias para combinaciones de valores de dos columnas.
* - [eval](https://pandas.pydata.org/docs/reference/api/pandas.eval.html)(expr[, parser, engine, local_dict, ...])
  - Evalua una cadena que describe operaciones entre elementos de un objeto.
* - [from_dummies](https://pandas.pydata.org/docs/reference/api/pandas.from_dummies.html)(data[, sep, default_category])
  - Crea una columna categórica a partie de un `DataFrame` con _dummy variables_.
* - [get_dummies](https://pandas.pydata.org/docs/reference/api/pandas.get_dummies.html)(data[, prefix, prefix_sep, ...])
  - Convierte variables categóricas en _dummy variables_. Básicamentecada valor único de una columna categórica la convierte en una nueva columna, cuyos valores contendrán unos y ceros indicando si cada fila tenía ese valor categórico.
* - [unique](https://pandas.pydata.org/docs/reference/api/pandas.unique.html)(values)
  - Retorna los valores únicos basados ​​en una tabla _hash_.
```

#### Notas de _crosstab_

[crosstab](https://pandas.pydata.org/docs/reference/api/pandas.crosstab.html): Retorna una tabla de contingencia, que retorna el número de ocurrencias para combinaciones de valores de dos columnas categóricas.
```python
pd.crosstab(index, columns, values=None, rownames=None, colnames=None, aggfunc=None, margins=False)
```
**Parámetros:**
- **index** - `array-like`, `Series` o `list` de `array`, `Series`: Son los valores que contiene los elementos que irán en las filas.
- **columns** - `array-like`, `Series` o `list` de `array`, `Series`: Son los valores que contiene los elementos que irán en las columnas.
- **values** - `array-like`: Valores a los que se aplicará las funciones de agregación. Es necesario que aggfunc sea especificado.
- **rownames** - `sequence`: Nombres a dar a las filas del resultado.
- **colnames** - `sequence`: Nombres a dar las columnas del resultado.
- **aggfunc** - `function` o `sequence` de `function`: Funciones de agregación a aplicar a los valores dados por el parámetro values para cada combinación de filas y columnas identificada.
- **margins** - `booleano`: Si toma el valor `True`, la tabla resultante incluirá totales.

Patrones útiles:
```python
# Generar tabla de contigencia
table=pd.crosstab(ri['col1'], ri['col2'])
```

<br/>

### Reshaping

Modifican la estructura (_shape_) de un objeto.

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

Funciones útiles para apilar objetos o unir objetos de manera similar a un _join_ de _SQL_.

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
  - Es similar a un _left-join_, con la diferencia de que las coincidencias de los _ids_ no tienen que ser idénticas, sino aproximaciones. Es útil con objetos con fechas y tiempos. Ambos objetos deben estar ordenados por la columna/índice que se usará como _id_.
* - [merge_ordered](https://pandas.pydata.org/docs/reference/api/pandas.merge_ordered.html)(left, right[, on, left_on, ...])
  - Ejecuta un _join_ con opción de rellenar o interpolar valores nulos. Útil para trabajar en _joins_ basados en fechas (ordenados).
```

#### Notas de _concat_

[concat](https://pandas.pydata.org/docs/reference/api/pandas.concat.html): Concatena objetos `DataFrame` ya sea de manera vertical u horizontal. Se conserva los índices de los objetos originales.
```python
pd.concat(objs, axis=0, join='outer', ignore_index=False, keys=None, verify_integrity=False)
```

**Parámetros:**
- **objs** - `sequence` de `Series` o `DataFrame`: Los objetos que se van a concatenar.
- **axis** - {0 o 'index', 1 o 'columns'}: Para indicar si de manera vertical u horizontal.
- **join** - {'inner', 'outer'}: Para indicar el tipo de _join_ con los labels del eje de las columnas. 'inner' para intersección, 'outer' para unión. Los valores en las columnas que no compartan serán `NaN`.
- **ignore_index** - `bool`: Si es `True`, entonces se reinicia el índice para todas las observacioes (de 0 a n-1).
- **keys** - `sequence` de `str` o `int`: Es para indicar que se ponga una clave al índice para identificar cuáles observaciones pertenecen a cuál `DataFrame`. Es una lista del mismo tamaño que el número de DataFrames. Los elementos se empatan por posición con los objetos.
- **verify_integrity** - `bool`: Es para verificar que no haya índices repetidos entre las tablas que se van a unir. En caso de que sea `True` y sí haya índices duplicados, se arrojará un error.

```python
# Concatenación vertical básica
concat_df=pd.concat([df1, df2])

# Concatenación, reiniciando índice y agregando keys
concat_df=pd.concat([df1, df2, ...]), ignore_index=True, keys=['df1','df2', ...])
```

#### Notas de _merge_

[merge](https://pandas.pydata.org/docs/reference/api/pandas.merge.html): Une `DataFrames` o `Series`, de una manera similar a un _join_ en _SQL_. El `DataFrame` resultante ignora el `Index`, a menos de que éste se haya usado para el hacer el _join_.
```python
pd.merge(left, right, how='inner', on=None, left_on=None, right_on=None, left_index=False, right_index=False, suffixes=('_x', '_y'), validate=None)[]
```

**Parámetros:**
- **left** - `DataFrame`: Tabla de la izquierda.
- **right** - `DataFrame` o `series`: Tabla de la derecha.
- **how** - {'left', 'right', 'outer', 'inner', 'cross'}: El tipo de _join_ que se realizará. 'outer' es similar a full outer join de SQL.
    - `inner`: Crea una tabla donde los _ids_ de ambas tablas coinciden.
    - `left`: Con base a los _id_ de la izquierda agrega los que también están en la derecha.
    - `right`: Con base a los _id_ de la derecha agrega los que también están a la izquierda.
    - `outer`: Retorna todos los records de las tablas, haciendo los _joins_ posibles.
    - `cross`: Equivale a hacer todas las combinaciones posibles de _ids_, sin importar si coinciden o no.
- **on** - `label` o `list`: La columna o nombre del índice sobre las cuales se hará el join. Debe de estar en _left_ y _right_. Por default usa como _keys_ las columnas que tienen el mismo nombre en ambos objetos.
- **left_on**, **right_on** - `label` o `list`: Las columnas o nombres del índice sobre las cuales se hará el _join_, una para la _left_ y otra para _right_.
- **left_index**, **right_index** - `bool`: Es para indicar que se use el índice de la tabla _left_ y _right_ respectivamente, para hacer el _join_.
- **suffixes** - `2 - list-like` de `str`: Es para indicar el sujifo que se agregará a cada columna, dependiendo de a cuál tabla pertenece. Solo a aquellas que tienen el mismo nombre en ambas tablas. La lista debe ser de longitud 2.
- **indicator** - `bool` o `str`: Para indicar si se debe de agregar una columna que indique el origen de cada fila. Si se para `str` es para modificar el nombre de esta columna que por default es '_merge'.
- **validate** - `str`: Verifica que el tipo de join haya sido de un tipo específico, como 'ono_to_one' o '1:1', 'one_to_many' o '1:m', 'many_to_one' o 'm:1' y 'many_to_many' o 'm:m'.

```python
# Hacer inner join con base a columna/índice en común
df_merged=pd.merge(df, other_df, on='col')

# Hacer inner join con base mútiples columnas/multiIndex
df_merged=pd.merge(df, other_df, on=['col1', 'col2', ...])

# Hacer inner join con a lon índices
df_merged=pd.merge(df, other_df, left_index=True, right_index=True)

# Hacer inner join con base a índices
df_merged=pd.merge(df, other_df, left_on='indName', right_on='indName')

# Hacer múltiples inner joins en columna en común
pd.merge(df, other_df, on='col').merge(df3, on='col').merge(df4, on='col')
```
- Para cualquier otro tipo de _join_ usar el parámetro _how_.

**Ejemplo**:

```{code-cell} ipython3
import pandas as pd

# Dataset 1: Información del empleado
employees=pd.DataFrame({
    'employee_id': [1, 2, 3, 4, 5],
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'department': ['HR', 'Engineering', 'Engineering', 'Marketing', 'HR']
})

print("Employees Dataset:", employees, sep='\n', end='\n'*2)

# Dataset 2: Salarios de los empleados
salaries=pd.DataFrame({
    'employee_id': [3, 4, 5, 6],
    'salary': [70000, 80000, 60000, 75000],
    'bonus': [5000, 8000, 4000, 6000]
})

print("Salaries Dataset:", salaries, sep='\n', end='\n'*2)

# Inner join en columna en común
inner_merge=pd.merge(employees, salaries, on='employee_id', how='inner')
print("Columna en común:", inner_merge, sep='\n', end='\n'*2)

# Inner join entre dos columnas
salaries_renamed=salaries.rename(columns={'employee_id': 'id'})
diff_key_merge=pd.merge(employees, salaries_renamed, left_on='employee_id', right_on='id', how='inner')
print("Diferentes columnas:", diff_key_merge, sep='\n', end='\n'*2)

# Inner join con base al índice
employees_indexed=employees.set_index('employee_id')
salaries_indexed=salaries.set_index('employee_id')
merged_on_index=pd.merge(employees_indexed, salaries_indexed, left_index=True, right_index=True, how='inner')
print("Índice:", merged_on_index, sep='\n')
```

<br/>

## I/O

Funciones la la entrada y salida de datos en diversos formatos.

### Archivo de texto

Funciones útiles para I/O de archivos de texto como csv, tsv, etc. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [DataFrame.to_csv](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html)([path_or_buf, sep, na_rep, ...])
  - Exporta el objeto en un archivo de valores separados por comas (csv).
* - [read_csv](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)(filepath_or_buffer, *[, sep, ...])
  - Importa un archivo de valores separados por comas (csv) en un `DataFrame`. También lee archivo csv comprimidos en _'gzip'_, _'bz2'_, _'zip'_ o _'xz'_. Para más información de esta función revisar las notas.
* - [read_fwf](https://pandas.pydata.org/docs/reference/api/pandas.read_fwf.html)(filepath_or_buffer, *[, colspecs, ...])
  - Importa una tabla de con delimitadores fijos en un `DataFrame`.
* - [read_table](https://pandas.pydata.org/docs/reference/api/pandas.read_table.html)(filepath_or_buffer, *[, sep, ...])
  - Importa un archivo delimitado en un `DataFrame`.
```

#### Notas de _read_csv_

[read_csv](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html): Lee un archivo y lo convierte en un `DataFrame`, por default utiliza _coma_ (,) como separador, pero se puede especifcar cualquier separador. También puede leer archivos _csv_ comprimidos en '_gzip_', _'bz2'_, _'zip'_ o _'xz'_. `read_table()` tiene los mismos parámetros pero tiene como separador por default la tabulación ('_\t_').

:::{caution}
La lista de parámetros no es una lista exhaustiva, revisar documentación oficial.
:::

```python
# Sintaxis de llamada
pd.read_csv(filepath, sep=',', header='infer', names=None, index_col=None, 
            usecols=None, squeeze=False, dtype=None, converters=None, 
            true_values=None, false_values=None,  skiprows=None, skipfooter=0, 
            nrows=None, na_values=None, parse_dates=False, dayfirst=False, 
            chunksize=None, thousands=None)
```

**Parámetros:**
- **filepath** - `str`, `path`: Es la ruta del archivo en la computadora, incluyendo el nombre del archivo y la extensión. También puede ser una _URL_ que tenga un archivo _csv_ o un archivo de texto en general, indicando el sepador apropiado.
- **sep** - `str`: Es para indicar de qué forma están separados los datos en el archivo. Incluso puede ser una _regular expression_ indicando la forma cómo están separado los datos.
- **header** - `int` o `list` de `int`: Es para indicar la fila que tiene los nombres de cada columna y el inicio de los datos. Si es `None` se pone como nombres los índices de las columnas (de 0 a _n-1_).
- **names** - `array-like` de `str`: Es para indicar explícitamente los nombres de las columnas, no se permiten duplicados. Debe de tener los nombres de todas las columnas en el archivo.
- **index_col** - `int`, `str`, `sequence` de `int` o `str`, `False`: Es para indicar la(s) columna(s) del archivo _csv_ que se debe de usar como índice, ya sea que se pase el índice `int` (empezando en cero) de la columna o el nombre `str`. Si es con base a más de una columna (multi índice) pasar una lista. `False` se usa para forzar a `pandas` a no usar la primer columna como índice, útil cuando existe una columna en el archivo que no tiene nombre.
- **usecols** - `list-like` de `int` o `str`: Es para indicar que se importen solo unas columnas en específico. Pueden ser los índices o los nombres que se dieron con names o los que se infirieron con header, el orden de las columnas en la lista se ignora.
- **squeeze** - `bool`: Si el archivo solo tiene una columna, entonces indica que se retorne `Series` en lugar de `DataFrame`.
- **dtype** - `type-name` o `dict`: El tipo de datos que tendrán las columnas. Puede ser un diccionario con el nombre de las columnas como _keys_ y el tipo de dato como los _values_. Revisar también el argumento _converters_. ADVERTENCIA: Si se indica alguna columna como `bool` automáticamentes los valores `NaN` y valores no reconocidos se convertirán a `True`.
- **converters** - `dict` de `function` o `callable`: Diccionario para aplicar una función a determinadas columnas. Las _keys_ son los nombres `str` o índice `int` de las columnas y _values_ son las funciones.
- **true_values**, **false_values** - `list`: Valores a ser considerados como `True` y `False` respectivamente.
- **skiprows** - `int`, `list-like` o `callable`: Es para indicar cuántas filas al inicio descartar.
  - `int`: Número de filas a omitir.
  - `list`: Índices de las filas a omitir (empieza en cero).
  - `callable`: Debe retornar `bool` para indicar `True` si descartar o `False` para conservar.
- **skipfooter** - `int`: Es para indicar cuántas filas al final descartar.
- **nrows** - `int`: Es para indicar cuántas filas importar.
- **na_values** - `scalar`, `str`, `list-like` o `dict`: Es para indicar qué cadenas se deben de considerar como _NA_. Por default se considerán: _'', '#N/A', '#N/A N/A', '#NA', '-1.#IND', '-1.#QNAN', '-NaN', '-nan', '1.#IND', '1.#QNAN', '\`NA`', 'N/A', 'NA', 'NULL', 'NaN', 'n/a', 'nan', 'null'_.
    - Si es un diccionario es para especificar valores `NaN` para cada columna, los _keys_ son los nombres (`str`) de las columnas y los _values_ (`list` de `str`) los valores a considerar _NA_.
- **parse_dates** - `bool`, `list` de `int` o `str`, `list` de `list` o `dict`: Es para indicar si alguna columna se debe de importar en formato de fecha. La columna debe de estar en algún formato estándar, si no es el caso, importa el archivo y despues convertir la columna con `to_datetime()` de `pandas`. También revisa el argumento _dayfirst_.
    - `bool`: Si es `True` entonces el índice se convertirá en fecha.
    - `list` de `int` o `str`: Si es una lista de enteros o de cadenas entonces se pasan los índices o los nombres de las columnas que se deben de convertir en fecha.
    - `list` de `list`: Si es una lista de listas, los valores de las listas interiores deben de tener índices o nombres de columnas y esas columnas se unirán y las convierte fecha en una sola columna.
    - `dict`: Si es un diccionario, las llaves serán los nombres de la nuevas columnas con fechas y los valores son los índices/nommbre de las columnas a convertir en fecha, pueden ser una lista con más de un índice/nombre que se combinarán en una sola. Los nombres de keys no pueden ser igual a ningún nombre en el archivo.
- **dayfirst** - `bool`: Es para indicar que las columnas de fechas están en formato _DD/MM/YYYY_.
- **chunksize** - `int`: Para indicar el número de filas a retornar en un objeto `TextFileReader` para iteración. Sirve para importar el contenido del archivo por partes en lugar de todo completo.
- **thousands** - `str`: Para indicar el separados de miles, como _','_ o _'.'_.
- **on_bad_lines** - {'error', 'warn', 'skip'}: Específica qué se debe se hacer en caso de que exista una línea 'corrupta'.
  - `error`: Se arroja un error.
  - `warn`: Se arroja una advertencia y se salta esa línea.
  - `skip`: Se salta la línea sin arrojar error ni advertencia.
- **Otros**: `true_values`, `false_values`.

**Retorna:**
- `DataFrame` o `TextParser`.

**Patrones útiles**

```python
# Lees csv
df=pd.read_csv('path/to/file.tsv')

# Especificar separador
df=pd.read_csv('path/to/file.csv', sep='\t')

# Importar columnas específicas
cols=['col1', 'col2', ...] # Alt por índice: [0, 1, ...]
df=pd.read_csv('path/to/file.csv', usecols=cols)

# Especificar tipo de datos de algunas/todas columnas
dtypes={'col1': dtype1, 'col2': dtype2, ...}
df=pd.read_csv('path/to/file.csv', dtype=dtypes)

# Especificar columnas como fechas/tiempo
cols=['col1', 'col2', ...] # Concatenación: [['col1', 'col2', ...]]
df=pd.read_csv('path/to/file.csv', parse_dates=cols, [dayfirst=bool])
```

#### Uso de parámetro _chunksize_

El parámetro `chunksize` sirve para indicar el número de filas a retornar en un objeto `TextFileReader` para iteración. Sirve para importar el contenido del archivo por partes en lugar de todo completo.

**Ejemplo**:
En este ejemplo se lee un archivo de 1,000 líneas por iteración, en cada iteración se realiza una operación y se acumula el resultado de la operación en una variable. Una vez que el cíclo que termina se imprime el resultado de la operación para todos los _chunks_. De esta manera se puede operar el en archivo de manera eficiente sin necesidad de importarlo todo al mismo tiempo.

```python
import pandas as pd 
total=0

# Iterar en chunks
for chunk in pd.read_csv('data.csv', chunksize=1000): 
    total += sum(chunk['x'])

print(total)
```
- Notar que _chunk_ es un `DataFrame`.


<br/>

### Excel

Funciones útiles para archivos de _Excel_. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [DataFrame.to_excel](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_excel.html)(excel_writer, *[, ...])
  - Exporta un objeto en una hoja de Excel. Se usa junto con la clase {ref}`pandas-ExcelWriter`.
* - [ExcelFile](https://pandas.pydata.org/docs/reference/api/pandas.ExcelFile.html)(path_or_buffer[, engine, ...])
  - Clase para analizar hojas tabulares de Excel en objetos `DataFrame`. Ver {ref}`pandas-ExcelFile`.
* - [ExcelWriter](https://pandas.pydata.org/docs/reference/api/pandas.ExcelWriter.html)(path[, engine, date_format, ...])
  - Clase para escribir objetos `DataFrame` en hojas de Excel. Ver {ref}`pandas-ExcelWriter`.
* - [Styler.to_excel](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.to_excel.html)(excel_writer[, sheet_name, ...])
  - Exporta un objeto `Styler` en una hoja de Excel.
* - [read_excel](https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html)(io[, sheet_name, header, names, ...])
  - Importa un archivo de Excel en un `DataFrame`.
```

#### Notas de _read_excel_

[read_excel](https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html): Lee un archivo de excel y lo convierte a un `DataFrame`. Soporta _xls, xlsx, xlsm, xlsb, odf, ods_ y _odt_. Si el archivo tiene más de una hoja se retorna un. Si el archivo tiene múltiples hojas, por default se importar solo la primer hoja, si se indica `sheet_name=None`, entonces se retornará un `OrderedDict` (similar a un `dict`), donde las llaves serán los nombres de cada una de las hojas en el archivo y los valores su respectivo `DataFrame`.

:::{caution}
La lista de parámetros no es una lista exhaustiva, revisar documentación oficial.
:::

```python
# Sintaxis de llamada
pd.read_excel(io, sheet_name=0, header=0, names=None, index_col=None, 
              usecols=None, dtype=None, converters=None, skiprows=None, 
              skipfooter=0, nrows=None, na_values=None, parse_dates=False)
```
**Parámetros:**
- **io** - `str`, `ExcelFile`, `path object`, `file-like object`: Ruta del archivo en la computadora. Puede ser una _URL_.
- **sheet_name** - `str`, `int`, `list` o `None`: Para indicar cuáles hojas importar, por default importa solo la primera. Puede ser:.
    - `str`: El nombre de la hoja.
    - `int`: El índice, empezando desde cero.
    - `list`: Son para múltiples hojas, ya sea `int` o `str`.
    - `None`: Es para indicar que se importen todas las hojas.
- **header** - `None`, `int` o `list` de `int`: Es para indicar la fila (índice desde cero) que tiene los nombres de cada columna y el inicio de los datos. Si es una lista crea un multi índice. `None` se usa para decir que no hay _header_.
- **names** - `array-like` de `str`: Es para indicar explícitamente los nombres de las columnas, no se permiten duplicados.
- **index_col** - `int`, `secuencia` de `int`, `None`: Es para indicar la(s) columna(s) del archivo de excel que se debe de usar como índice
    - `int`: Índice de la columna
    - `list`: Si es con base a más de una columna (multi índice) pasar una lista.
    - `None`: Para omitir el índice.
- **usecols** - `list-like`, `str`, `None`: Es para indicar que se importen solo unas columnas en específico.
    - `list-like`: Pueden ser los índices o los nombres que se dieron con _names_ o los que se infirieron con _header_.
    - `str`: Puede ser una cadena con las letras de las columnas (A, B, C, etc) separadas por comas o por rangos (J:M), o una combinación de esos, por ejempo 'A:C, E'.
    - `None`: Se pasan todas las columnas.
- **dtype** - `type-name` o `dict`: El tipo de datos que tendrán las columnas. Puede ser un diccionario con el nombre de las columnas como keys y el tipo de dato como los valores. Revisar también el parámetro _converters_.
- **converters** - `dict` de `function` o `callable`: Diccionario para aplicar una función a determinadas columnas. Las llaves son los nombres `str` o índice `int` de las columnas y los valores son las funciones.
- **skiprows** - `int`, `list-like` o `callable`: Es para indicar cuántas filas al inicio descartar. Si es `callable` debe retornar `bool` para indicar `True` si descartar o `False` para conservar.
- **skipfooter** - `int`: Es para indicar cuántas filas al final descartar.
- **nrows** - `int`: Es para indicar cuántas filas importar. Consulta los parámetros _skiprows_ y _skipfooter_ para saltar solo filas al principio o al final del documento.
- **na_values** - `scalar`, `str`, `list-like` o `dict`: Para indicar cadenas adicionales a ser considerados como _Na/NaN_. Por default se considerán: _'', '#N/A', '#N/A N/A', '#NA', '-1.#IND', '-1.#QNAN', '-NaN', '-nan', '1.#IND', '1.#QNAN', '\`NA`', 'N/A', 'NA', 'NULL', 'NaN', 'n/a', 'nan', 'null'_.
    - `dict` es para especificar valores `NaN` por columna. 
- **parse_dates** - `bool`, `list-like`, `dict`: Es para indicar si alguna columna se debe de importar en formato de fecha.
    - `bool`: Si es `True` entonces el índice se convertirá en fecha.
    - `list-like`: Si es una lista de enteros o de cadenas entonces se pasan los índices o los nombres de las columnas que se deben de convertir en fecha.
    - `list` de `list`: Si es una lista de listas, los valores de las listas interiores deben de tener índices o nombres de columnas y esas columnas se unirán y las convierte fecha en una sola columna.
    - `dict`: Las llaves serán los nombres de la nuevas columnas con fechas y los valores son los índices de las columnas a convertir en fecha, pueden ser una lista con más de un índice que se combinarán en una sola.
- Otros: `true_values`, `false_values`. 

**Retorna:**
- `DataFrame` o `OrderedDict` de `DataFrame`.

Patrones útiles

```python
# Leer archivo y guardarlo como df
df=pd.read_excel('path/to/file.xlsx')

# Importar columnas específicas
cols=['col1', 'col2', ...] # Alt por índice: [0, 1, ...]
df=pd.read_excel('path/to/file.xlsx', usecols=cols)

# Especificar tipo de datos de algunas/todas columnas
dtypes={'col1': dtype1, 'col2': dtype2, ...}
df=pd.read_excel('path/to/file.xlsx', dtype=dtypes)
```

(pandas-ExcelFile)=
#### ExcelFile

Es una clase para importar hojas de Excel como `DataFrame`.

```python
# Importar la clase
import pandas as pd

# Definir ruta del archivo
path='urbanpop.xlsx'

# Crear conexión con el archivo
xlsx=pd.ExcelFile(path)

# Leer contenido de una hoja en un df
df=xlsx.parse('sheet_name') # También se puede usar el índice de la hoja
```
- En lugar de indicar el nombre de la hoja, se puede indicar el índice de la hoja. Los índices comienzan en cero.
- Para conocer los nombres de las hojas usar el atributo `.sheet_names`.

##### Atributos de ExcelFile

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [ExcelFile.book](https://pandas.pydata.org/docs/reference/api/pandas.ExcelFile.book.html)()
  - Retorna una instancia [Workbook](https://openpyxl.readthedocs.io/en/stable/api/openpyxl.workbook.workbook.html#openpyxl.workbook.workbook.Workbook) de la librería `openpyxl`. Esta clase tiene muchos más métodos y atributos que la clase `ExcelFile`.
* - [ExcelFile.sheet_names](https://pandas.pydata.org/docs/reference/api/pandas.ExcelFile.sheet_names.html)()
  - Nombre de las hojas del archivo de Excel.
```

##### Métodos de ExceFile

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - `ExcelFile.close`()
  - Cierra la conexión si es necesario.
* - [ExcelFile.parse](https://pandas.pydata.org/docs/reference/api/pandas.ExcelFile.parse.html)([sheet_name, header, names, ...])
  - Lee una hoja de un archivo de Excel y lo convierte a un `DataFrame`.
```

(pandas-ExcelWriter)=
#### ExcelWriter

Clase para escribir objetos `DataFrame` en hojas de Excel, se usa junto al método `DataFrame.to_excel()`:

```python
# Exportar objeto a libro de excel
with pd.ExcelWriter('path/to/file.xlsx') as writer:
    df.to_excel(writer, sheet_name='sheet_name')
    df2.to_excel(writer, sheet_name='sheet_name2')
    ...
```
- Hacerlo de esta forma es particularmente útil si se van exportar varios objetos en diferentes hojas al mismo tiempo.

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

Funciones útiles para archivos _HDFStore_ (extensión _.hdf5_ o _.h5_). 

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

Patrones útiles

```python
# Leer JSON indicando orientación
import pandas as pd
df=pd.read_json("path/to/file.json",orient='str')
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

Funciones útiles para archivos de _SAS_ (extensión _.sas7bdat_).  

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

:::{caution}
Todas las funciones de esta sección nesitan un objeto `Engine` de `sqlalchemy`.
:::

:::{tip}
Para más información sobre SQL consultar [Nebok-SQL](https://angelizaldi.github.io/nebok-sql/intro.html).
:::

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [DataFrame.to_sql](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_sql.html)(name, con, *[, schema, ...])
  - Escribe registros almacenados en un `DataFrame` a una base de datos SQL.
* - [read_sql](https://pandas.pydata.org/docs/reference/api/pandas.read_sql.html)(sql, con[, index_col, ...])
  - Lee un _query_ o una tabla de una base de datos en un `DataFrame`.
* - [read_sql_query](https://pandas.pydata.org/docs/reference/api/pandas.read_sql_query.html)(sql, con[, index_col, ...])
  - Ejecuta un _query_ y guarda el resultado en un `DataFrame`.
* - [read_sql_table](https://pandas.pydata.org/docs/reference/api/pandas.read_sql_table.html)(table_name, con[, schema, ...])
  - Lee una tabla de una base de datos en un `DataFrame`.
```

#### Engine

Para crear una instancia de la clase `Engine` revisar la siguiente plantilla:

```python
# importar función
from sqlalchemy import create_engine

# Definir elementos de la url
user_db="your_username"
password_db="your_password"
url_db="localhost:5432"
name_db="your_database"

postgres_url=f"postgresql://{user_db}:{password_db}@{url_db}/{name_db}"

# Crear engine
engine=create_engine(postgres_url)
```
- Se puede omitir la constraseña simplemente asignado `password_db=""`.
- En Postgre también se podría usar: `"postgresql+psycopg2://{user_db}:{password_db}@{url_db}/{name_db}"`
    - Es necesario tener instalado `psycopg2`. 
- En MySQL: `"mysql+pymysql://{user_db}:{password_db}@{url_db}/{name_db}"`
    - Es necesario tener instalado `pymysql`. 
- En SQLite: `"sqlite:///{name_db}"`
    - _name_db_ debe tener extensión _.db_ y debe estar en el directorio activo: `name_db="your_database.db"`
    - Si no está en el directorio activo se debe de indicar la ruta al archivo: `name_db="path/to/your_database.db"`

Una vez creado el _engine_ se puede usar cualquiera de las funciones para interactuar con la base de datos

```python
# Importaciones
from sqlalchemy import create_engine
import pandas as pd

# Crear engine
engine=create_engine(url)

# Leer un query
df=pd.read_sql_query("SELECT * FROM Orders", engine)
```

<br/>

### Stata

Funciones útiles para trabajar con archivos de _Stata_ (extensión _.dta_). 

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

