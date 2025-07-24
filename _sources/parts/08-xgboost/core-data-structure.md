# Core Data Structure

En esta sección se presentan las estructuras de datos principales que _XGBoost_ utiliza para almacenar y manipular datos durante el entrenamiento y la predicción.

:::{caution}
En general solo se trabajará con la clase `Booster` y `DMatrix`.
:::

:::{note}
Para más información visitar la [documentación](https://xgboost.readthedocs.io/en/stable/python/python_api.html#module-xgboost.core) de _XGBoost_.
:::

## Booster

`Booster` es la clase que representa el modelo entrenado en _XGBoost_. Contiene los árboles de decisión y otros parámetros del modelo.

```{list-table}
:header-rows: 1

* - Constructor
  - Descripción
* - [xgboost.Booster](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.Booster)(params=None,  cache=None,  model_file=None)
  - Un `Booster` de XGBoost. Es el modelo que contiene rutinas de bajo nivel para entrenamiento, predicción y evaluación.
```

<br/>

### Atributos de _Booster_

Atributos de la clase `Booster`. 

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - **best_iteration**
  - La mejor iteración durante el entrenamiento.
* - **best_score**
  - La mejor puntuación de evaluación durante el entrenamiento.
* - **feature_names**
  - Nombres de los _features_ de este _booster_. Pueden establecerse directamente mediante datos de entrada o por asignación.
* - **feature_types**
  - Tipos de _features_ para este _booster_. Puede establecerse directamente por datos de entrada o por asignación. Véase `DMatrix` para más detalles.
```

<br/>

(Booster-methods)=
### Métodos de _Booster_

Métodos de la clase `Booster`. 

```{list-table}
:header-rows: 1

* - method
  - Descripción
* - [attr](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.Booster.attr)(key)
  - Retorna atributos del _`Booster`_ como cadenas.
* - [attributes](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.Booster.attributes)()
  - Retorna los atributos almacenados en el _`Booster`_ como diccionario.
* - [boost](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.Booster.boost)(dtrain,  iteration,  grad,  hess)
  - Aumenta el _booster_ durante una iteración con estadísticas de gradiente personalizadas. Esta función no debe ser llamada directamente por los usuarios.
* - [copy](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.Booster.copy)()
  - Copia el objeto _booster_.
* - [dump_model](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.Booster.dump_model)(fout,  fmap='',  with_stats=False,  ...)
  - Exporta el modelo en un archivo de texto o _JSON_. A diferencia de `save_model()`, el formato de salida se utiliza principalmente para la visualización o la interpretación, por lo que es más legible, pero no se puede cargar de nuevo a _XGBoost_.
* - [eval](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.Booster.eval)(data,  name='eval',  iteration=0)
  - Evalúa el modelo _on mat_.
* - [eval_set](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.Booster.eval_set)(evals,  iteration=0,  feval=None,  ...)
  - Evalúa un conjunto de datos.
* - [inplace_predict(data, iteration_range=](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.Booster.inplace_predict)(data,  iteration_range=(0,  0),  predict_type='value', ...)
  - A diferencia del método `predict()`, no almacena en caché el resultado de la predicción.
* - [load_config](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.Booster.load_config)(config)
  - Carga la configuración devuelta por _save_config_.
* - [load_model](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.Booster.load_model)(fname)
  - Carga el modelo desde un archivo o _bytearray_.. Load the model from a file or a bytearray
* - [num_boosted_rounds](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.Booster.num_boosted_rounds)()
  - Retorna el número de _boosted rounds_. Para _gblinear_ esto se restablece a 0 después de serializar el modelo.
* - [num_features](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.Booster.num_features)()
  - Número de _features_ en el _booster_.
* - [predict](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.Booster.predict)(data,  output_margin=False,  pred_leaf=False,  ...)
  - Predice con _data_. Se utilizará el modelo completo a menos que se especifique _iteration_range_, lo que significa que el usuario tendrá que trocear el modelo o utilizar el atributo _best_iteration_ para obtener la predicción del mejor modelo obtenido tras un _early stopping_.
* - [save_config](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.Booster.save_config)()
  - Muestra la configuración de los parámetros internos del _`Booster`_ como una cadena JSON.
* - [save_model](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.Booster.save_model)(fname)
  - Guarda el modelo en un archivo.
* - [save_raw](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.Booster.save_raw)(raw_format='ubj')
  - Guarda el modelo en una representación en memoria intermedia en lugar de en un archivo.
* - [trees_to_dataframe](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.Booster.trees_to_dataframe)(fmap='')
  - Convierte un modelo de árbol _boosted_ en un `DataFrame`.
* - [update](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.Booster.update)(dtrain,  iteration,  fobj=None)
  - Actualización para una iteración, con la función objetivo calculada internamente. Esta función no debe ser llamada directamente por los usuarios.
* - **Establecer y Recuperar**
  -
* - [get_dump](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.Booster.get_dump)(fmap='',  with_stats=False,  dump_format='text')
  - Exporta el modelo como `list` de cadenas. A diferencia de `save_model()`, el formato de salida se utiliza principalmente para la visualización o la interpretación, por lo que es más legible, pero no se puede cargar de nuevo a _XGBoost_.
* - [get_fscore](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.Booster.get_fscore)(fmap='')
  - Recupera la importancia de cada _feature_.
* - [get_score](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.Booster.get_score)(fmap='',  importance_type='weight')
  - Retorna la importancia de cada _feature_.
* - [get_split_value_histogram](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.Booster.get_split_value_histogram)(feature,  fmap='',  bins=None,  ...)
  - Retorna el histograma de valores divididos de un _feature_.
* - [set_attr](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.Booster.set_attr)(**kwargs)
  - Establece atributos del _`Booster`_.
* - [set_param](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.Booster.set_param)(params,  value=None)
  - Establece los parámetros en el _`Booster`_.
```

<br/>

(Dmatrix)=
## DMatrix

`DMatrix` es la estructura de datos principal en _XGBoost_. Es una matriz optimizada para almacenar datos de entrada (_features_ y etiquetas) en un formato eficiente que _XGBoost_ puede procesar rápidamente. Puede soportar `ndarray` de _numpy_, `DataFrame` de _pandas_, `sparse` de _scipy_, entre otros.

```{list-table}
:header-rows: 1

* - Constructor
  - Descripción
* - [xgboost.DMatrix](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.DMatrix)(data,  label=None, ...)
  - Matriz de datos utilizada en _XGBoost_.
```
**Parámetros:**
- **data** - `array`, `sparse`, `DataFrame`: Datos para la `Dmatrix` (_feature matrix_).
- **label** - `array-like`: Vector del _target_ del _training_ (_y_).

<br/>

### Atributos de _DMatrix_

Atributos de la clase `DMatrix`. 

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - **feature_names**
  - Etiquetas para los _features_ (etiquetas de las columnas).
* - **feature_types**
  - Tipo de los _features_ (tipos de las columnas).
```

<br/>

### Métodos de _DMatrix_

Métodos de la clase `DMatrix`. 

```{list-table}
:header-rows: 1

* - Métodos
  - Descripción
* - [data_split_mode](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.DMatrix.data_split_mode)()
  - Retorna el modo de división de datos de la `DMatrix`.
* - [num_col](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.DMatrix.num_col)()
  - Retorna el número de columnas (_features_) en la `DMatrix`.
* - [num_nonmissing](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.DMatrix.num_nonmissing)()
  - Retorna el número de valores no nulos en la `DMatrix`.
* - [num_row](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.DMatrix.num_row)()
  - Retorna el número de filas de la `DMatrix`.
* - [save_binary](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.DMatrix.save_binary)(fname,  silent=True)
  - Guarda `DMatrix` en un búfer _XGBoost_. El binario guardado se puede cargar posteriormente proporcionando la ruta a `xgboost.DMatrix()` como entrada.
* - [slice](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.DMatrix.slice)(rindex,  allow_groups=False)
  - Corta la `DMatrix` y devuelve una nueva `DMatrix` que sólo contiene _rindex_.
* - **Recuperar**
  -
* - [get_base_margin](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.DMatrix.get_base_margin)()
  - Retorna el margen base de la `DMatrix`.
* - [get_data](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.DMatrix.get_data)()
  - Retorna los predictores de `DMatrix` como una matriz _CSR_. Este _getter_ es principalmente para propósitos de prueba. Si se trata de una `DMatrix` cuantificada, se devuelven los valores cuantificados en lugar de los valores de entrada.
* - [get_float_info](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.DMatrix.get_float_info)(field)
  - Retorna la propiedad `float` de la `DMatrix`.
* - [get_group](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.DMatrix.get_group)()
  - Retorna el grupo de la `DMatrix`.
* - [get_label](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.DMatrix.get_label)()
  - Retorna la etiqueta de la `DMatrix`.
* - [get_quantile_cut](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.DMatrix.get_quantile_cut)()
  - Retorna cortes cuantílicos para la cuantificación.
* - [get_uint_info](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.DMatrix.get_uint_info)(field)
  - Retorna la propiedad _integer_ sin signo de la `DMatrix`.
* - [get_weight](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.DMatrix.get_weight)()
  - Retorna la ponderación de la `DMatrix`.
* - **Establecer**
  -
* - [set_base_margin](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.DMatrix.set_base_margin)(margin)
  - Establece el margen base del _booster_ para empezar.
* - [set_float_info](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.DMatrix.set_float_info)(field,  data)
  - Establece la propiedad `float` en la `DMatrix`.
* - [set_float_info_npy2d](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.DMatrix.set_float_info_npy2d)(field,  data)
  - Para la entrada de `ndarrays` 2D.
* - [set_group](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.DMatrix.set_group)(group)
  - Establece el tamaño del grupo de `DMatrix` (utilizado para _ranking_).
* - [set_info](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.DMatrix.set_info)(, ...)
  - Establecer la meta-información para `DMatrix`. Ver _doc string_ para `xgboost.DMatrix`.
* - [set_label](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.DMatrix.set_label)(label)
  - Establece la etiqueta de `DMatrix`.
* - [set_uint_info](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.DMatrix.set_uint_info)(field,  data)
  - Establece la propiedad de tipo _uint_ en la `DMatrix`.
* - [set_weight](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.DMatrix.set_weight)(weight)
  - Establece la ponderación de cada instancia.
```

<br/>

## DataIter

Interfaz usada para `iterators` de los datos definidos por el usuario. La mayoría de las veces, los usuarios no necesitan interactuar con esta clase directamente.

```{list-table}
:header-rows: 1

* - Constructor
  - Descripción
* - [xgboost.DataIter](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.DataIter)(cache_prefix=None,  release_data=True)
  - La interfaz para el iterador de datos definido por el usuario.
```

<br/>

### Atributos de _DataIter_

Atributos de la clase . 

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - **proxy**
  - Manejador del proxy `DMatrix`.
```

<br/>

### Métodos de _DataIter_

Métodos de la clase . 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [abstract next](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.DataIter.next)(input_data)
  - Establece el siguiente lote de datos.
* - [abstract reset](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.DataIter.reset)()
  - Reinicia el iterador de datos. Prototipo de función definida por el usuario.
* - [get_callbacks](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.DataIter.get_callbacks)(enable_categorical)
  - Retorna funciones de _callback_ para iterar en C. Esta es una función interna.
* - [reraise](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.DataIter.reraise)()
  - Anula la excepción lanzada durante la iteración.
```

<br/>

## QuantileDMatrix

Una versión optimizada de `DMatrix` que utiliza cuantiles para mejorar la eficiencia en el entrenamiento con _datasets_ grandes.

```{list-table}
:header-rows: 1

* - Constructor
  - Descripción
* - [xgboost.QuantileDMatrix](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.QuantileDMatrix)(data,  label=None,  , ...)
  - Una variante de `DMatrix` que genera datos cuantificados directamente a partir de los datos de entrada para el método del árbol hist. Esta `DMatrix` está diseñada principalmente para ahorrar memoria en el entrenamiento evitando el almacenamiento intermedio.
```

:::{note}
Todos los atributos y métodos de {ref}`Dmatrix` también están disponibles para `QuantileDMatrix`.
:::

<br/>

