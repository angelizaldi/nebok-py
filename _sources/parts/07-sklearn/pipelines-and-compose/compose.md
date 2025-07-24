# Compose

Proporciona herramientas para crear modelos compuestos y transformadores personalizados, útiles para flujos de trabajo avanzados. Para importar este módulo o una clase o función específica usar:

```python
# Importar módulo
from sklearn import compose

# Importar clase específica
from sklearn.compose import ClassName

# Importar función específica
from sklearn.compose import func_name
```
- _ClassName_ o _func_name_ es el nombre de la clase o función respectivamente.

:::{note}
Para más información de esta librería visitar la [documentación](https://scikit-learn.org/stable/api/sklearn.compose.html) de `sklearn`.
:::

<br/>

## Clases

Clases implementadas en el módulo `compose`.

```{list-table}
:header-rows: 1

* - Clase
  - Descripción
* - [ColumnTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html)(transformers, ...)
  - Aplica transformadores a las columnas de un arreglo o `DataFrame`.
* - [TransformedTargetRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.compose.TransformedTargetRegressor.html)(regressor=None, ...)
  - Metaestimador de regresión sobre un _target_ transformado.
```

<br/>

### ColumnTransformer

[ColumnTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html): Aplica transformadores (como los del módulo `prepocessing`) a columnas de un arreglo o un `DataFrame`. Permite hacer _subsets_ de columnas para aplicar transformadores específicos. Si algunas columnas no se van a transformar utilizar el parámetro _remainder_. Es útil para preprocesamiento de _datasets_ con columnas heterogéneas (por ejemplo, escalado de columnas numéricas y codificación _one-hot_ de columnas categóricas).
```python
# Sintaxis de llamada
ColumnTransformer(transformers, *, remainder='drop', sparse_threshold=0.3, n_jobs=None, 
                  transformer_weights=None, verbose=False, verbose_feature_names_out=True, 
                  force_int_remainder_cols=True)
```
**Parámetros:**
- **transformers** - `list` de `3-tuple`: Una lista de tuples `(name, transformer, columns)` especificando los transformadores a las columnas.
    - _name_ - `str`: Nombre del paso.
    - _transformer_ - `estimator` o {'drop', 'passthrough'}: Indica la tranformación que se hara a esa columna o conjunto de columnas.
        - `estimator`: Estimador (modelo) que soporta los métodos `.fit()` y `.transform()`. Puede ser un `Pipeline`.
        - _'drop'_: Es para indicar que se eliminen las columnas.
        - _'passthrough'_: Es para indicar que a las columnas no se les haga ninguna transformación.
    - _columns_ - `str`, `array-like` de `str`, `int`, `array-like` de `int`, `array-like` de `bool`, `slice` o `callable`: Para indicar los índices de las columnas, por número o nombre.
- **remainder** - {'drop', 'passthrough'} o `estimator`: Por default las columnas que no se transformen serán eliminadas (_'drop'_). Para no eliminar ni transformarlas usar _'passthrough'_.
- **sparse_threshold** - `float`: Si el _output_ de los transformadores es `sparse` entonces, los resultados se apilaran si la densidad general es menor a este valor. Usar `sparse_threshold=0` para siempre retornar _dense_.

#### Atributos

Atributos de la clase `ColumnTransformer`.

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - **feature_names_in_**
  - Nombres de los _features_ observados durante el ajuste. Definido sólo cuando _X_ tiene nombres de _features_ que son todos cadenas.
* - **n_features_in_**
  - Número de _features_ vistos durante el ajuste. Sólo se define si los transformadores subyacentes exponen dicho atributo al ajustar.
* - **named_transformers_**
  - Accede al transformador ajustado por su nombre.
* - **output_indices_**
  - Un diccionario de cada nombre de transformador a una rebanada, donde la rebanada corresponde a índices en la salida transformada. Esto es útil para inspeccionar qué transformador es responsable de qué _feature(s)_ transformado(s).
* - **sparse_output_**
  - _Flag_ booleana que indica si la salida de _transform_ es una matriz dispersa o un array denso, que depende de la salida de los transformadores individuales y del parámetro _sparse_threshold_.
* - **transformers_**
  - La colección de transformadores ajustados como tuplas de `(name, transformer, columns)`.
```

#### Métodos

Métodos de la clase `ColumnTransformer`.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [fit](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer.fit)(X,  y=None,  **params)
  - Ajusta todos los transformadores utilizando _X_.
* - [fit_transform](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer.fit_transform)(X,  y=None,  **params)
  - Ajusta todos los transformadores, transforma los datos y concatena los resultados.
* - [transform](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer.transform)(X,  **params)
  - Transforma _X_ por separado mediante cada transformador, concatena los resultados.
```

<br/>

## Funciones

Funciones implementadas en el módulo `compose`.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [make_column_selector](https://scikit-learn.org/stable/modules/generated/sklearn.compose.make_column_selector.html)(pattern=None, ...)
  - Crea una `callable` para seleccionar las columnas que se utilizarán con `ColumnTransformer`.
* - [make_column_transformer](https://scikit-learn.org/stable/modules/generated/sklearn.compose.make_column_transformer.html)(*transformers, remainder='drop', sparse_threshold=0.3, n_jobs=None, verbose=False, verbose_feature_names_out=True, force_int_remainder_cols=True)
  - Construye un `ColumnTransformer` a partir de los transformadores dados.
```

<br/>


### Notas de _make_column_selector_

[make_column_selector](https://scikit-learn.org/stable/modules/generated/sklearn.compose.make_column_selector.html): Crea una función para seleccionar columnas de un dataset con base al tipo de dato o al nombre de las columnas usando _REGEX_. La función retorna solo el nombre de las columnas que cumplen las condiciones como `list`. Básicamente retornará un `Callable` que al pasarle un `DataFrame` retornará `list` con el nombre de las columnas que satisfacen las condiciones.
```python
# Sintaxis de llamada
make_column_selector(pattern=None, dtype_include=None, dtype_exclude=None)
```
**Parámetros:**
- **pattern** - `str`: Patrón en el nombre para incluir las columnas que cumplan con él.
- **dtype_include** - `dtype` o `list` de `dtype`: Tipos de datos de las columnas a incluir en la selección.
- **dtype_exclude** - `dtype` o `list` de `dtype`: Tipos de datos de las columnas a exluir en la selección.