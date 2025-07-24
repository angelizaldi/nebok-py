# Feature Selection

Ofrece métodos para seleccionar los _features_ más relevantes de un _dataset_, y eliminación recursiva de _features_. Para importar este módulo o una clase o función específica usar:

```python
# Importar módulo
from sklearn import feature_selection

# Importar clase específica
from sklearn.feature_selection import ClassName

# Importar función específica
from sklearn.feature_selection import func_name
```
- _ClassName_ o _func_name_ es el nombre de la clase o función respectivamente.

:::{note}
Para más información de esta librería visitar la [documentación](https://scikit-learn.org/stable/api/sklearn.feature_selection.html) de `sklearn`.
:::

<br/>

## Clases

Clases implementadas en el módulo `feature_selection`.

```{list-table}
:header-rows: 1

* - Clase
  - Descripción
* - [GenericUnivariateSelect](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.GenericUnivariateSelect.html)(score_func=<functionf_classif>, ...)
  - Selector de _features_ univariados con estrategia configurable.
* - [RFE](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFE.html)(estimator, ...)
  - Clasificación de _features_ con eliminación recursiva de _features_.
* - [RFECV](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFECV.html)(estimator, ...)
  - Eliminación recursiva de _features_ con validación cruzada para seleccionar _features_.
* - [SelectFdr](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectFdr.html)(score_func=<functionf_classif>, ...)
  - Filtro: Selecciona los valores _p_ para una tasa estimada de "descubrimientos falsos".
* - [SelectFpr](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectFpr.html)(score_func=<functionf_classif>, ...)
  - Filtro: Selecciona los valores _p_ debajo de alfa según una prueba _FPR_.
* - [SelectFromModel](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectFromModel.html)(estimator, ...)
  - Metatransformador para seleccionar _features_ basados en pesos de importancia.
* - [SelectFwe](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectFwe.html)(score_func=<functionf_classif>, ...)
  - Filtro: Selecciona los valores _p_ correspondientes a la tasa de error por _Family-wise_.
* - [SelectKBest](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectKBest.html)(score_func=<functionf_classif>, ...)
  - Selecciona los _features_ según las _k_ puntuaciones más altas.
* - [SelectPercentile](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectPercentile.html)(score_func=<functionf_classif>, ...)
  - Selecciona los _features_ según un percentil de las puntuaciones más altas.
* - [SelectorMixin](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectorMixin.html)()
  - Transformador _mixin_ que realiza la selección de _features_ dada una máscara de soporte.
* - [SequentialFeatureSelector](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SequentialFeatureSelector.html)(estimator, ...)
  - Transformador que realiza la selección secuencial de _features_.
* - [VarianceThreshold](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.VarianceThreshold.html)(threshold=0.0)
  - Selector de _features_ que elimina todas los _features_ de baja varianza.
```

<br/>

### RFE

[RFE](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFE.html): Selecciona _features_ de manera recursiva, eliminando las menos importantes según un modelo base (como regresión lineal o SVM). Es útil para reducción de dimensionalidad y selección de _features_ para mejorar la eficiencia y rendimiento de modelos.
```python
# Sintaxis de llamada
RFE(estimator, *, n_features_to_select=None, step=1, verbose=0, importance_getter='auto')
```
**Parámetros:**
- **estimator** - `estimator`: Es el modelo base con el que el transformador se basará, debe tener el método `.fit()` y el atributo `feature_importances_` o `.coef_`.
- **n_features_to_select** - `int` o `float`: Número de _features_ a elegir, si es `int` es la cantidad, si es `float` es el porcentaje.

#### Atributos

Atributos de la clase `RFE`.

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - **classes_**
  - Etiquetas de las clases disponibles cuando el estimador es un clasificador.
* - **estimator_**
  - El estimador ajustado utilizado para seleccionar los _features_.
* - **feature_names_in_**
  - Nombres de los _features_ observados durante el ajuste. Definido sólo cuando _X_ tiene nombres de _features_ que son todos cadenas. 
* - **n_features_**
  - El número de _features_ seleccionados.
* - **n_features_in_**
  - Número de _features_ observados durante el ajuste. Sólo se define si el estimador subyacente expone dicho atributo durante el ajuste. 
* - **ranking_**
  - La clasificación de los _features_, de forma que `ranking_[i]` corresponde a la posición en la clasificación de la característica i-ésima.
* - **support_**
  - La máscara de los _features_ seleccionados.
```

#### Métodos

Métodos de la clase `RFE`.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [decision_function](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFE.html#sklearn.feature_selection.RFE.decision_function)(X)
  - Calcula la función de decisión de _X_.
* - [fit](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFE.html#sklearn.feature_selection.RFE.fit)(X,  y,  **fit_params)
  - Ajusta el modelo _RFE_ y, a continuación, el estimador subyacente a los _features_ seleccionados.
* - [fit_transform](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFE.html#sklearn.feature_selection.RFE.fit_transform)(X,  y=None,  **fit_params)
  - Ajusta a los datos, luego los transforma.
* - [inverse_transform](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFE.html#sklearn.feature_selection.RFE.inverse_transform)(X)
  - Invierte la operación de transformación.
* - [predict](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFE.html#sklearn.feature_selection.RFE.predict)(X,  **predict_params)
  - Reduce _X_ a los _features_ seleccionados y predeci utilizando el estimador.
* - [predict_log_proba](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFE.html#sklearn.feature_selection.RFE.predict_log_proba)(X)
  - Predice las probabilidades logarítmicas de clase para _X_.
* - [predict_proba](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFE.html#sklearn.feature_selection.RFE.predict_proba)(X)
  - Predice probabilidades de clase para _X_.
* - [score](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFE.html#sklearn.feature_selection.RFE.score)(X,  y,  **score_params)
  - Reduce _X_ a los _features_ seleccionados y devuelve la puntuación del estimador.
* - [transform](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFE.html#sklearn.feature_selection.RFE.transform)(X)
  - Reduce _X_ a los _features_ seleccionados.
```

<br/>

### SelectFromModel

[SelectFromModel](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectFromModel.html): Selecciona _features_ basándose en la importancia de las mismas, según un modelo base (como árboles de decisión o modelos lineales con regularización). Es útil para selección automática de _features_ relevantes para simplificar modelos y evitar el sobreajuste.
```python
# Sintaxis de llamada
SelectPercentile(estimator, *, threshold=None, prefit=False, norm_order=1, max_features=None, importance_getter='auto')
```
**Parámetros:**
- **estimator** - `estimator`: Es el modelo base con el que el transformador se basará, debe tener el método `.fit()` y el atributo `feature_importances_` o `.coef_`.
- **threshold** - `str` o `float`: El valor del _threshold_ usado para la selección de _features_. Valores por encima o iguales a este valor se mantiene. Si es `str` puede ser _'median'_, _'mean'_, etc. También se pueden escalar como _'1.25*mean'_.

#### Atributos

Atributos de la clase `SelectFromModel`.

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - **estimator_**
  - El estimador base a partir del cual se construye el transformador. Este atributo sólo existe cuando se ha llamado a `.fit()`. Si `prefit=True`, es una copia en profundidad del estimador. Si `prefit=False`, es un clon del estimador y se ajusta a los datos pasados a `fit()` o `partial_fit()`.
* - **feature_names_in_**
  - Nombres de los _features_ observados durante el ajuste. Definido sólo cuando _X_ tiene nombres de _features_ que son todos cadenas. 
* - **max_features_**
  - Número máximo de _features_ calculados durante el ajuste. Sólo se define si _max_features_ no es `None`. Si _max_features_ es un `int` entonces `max_features_ = max_features`. Si _max_features_ es un `callable`, entonces `max_features_ = max_features(X)`.
* - **n_features_in_**
  - Número de _features_ observados durante el ajuste.
* - **threshold_**
  - Valor umbral utilizado para la selección de _features_.
```

#### Métodos

Métodos de la clase `SelectFromModel`.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [fit](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectFromModel.html#sklearn.feature_selection.SelectFromModel.fit)(X,  y=None,  **fit_params)
  - Ajusta el metatransformador `SelectFromModel`.
* - [fit_transform](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectFromModel.html#sklearn.feature_selection.SelectFromModel.fit_transform)(X,  y=None,  **fit_params)
  - Ajusta a los datos, luego los transforma.
* - [inverse_transform](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectFromModel.html#sklearn.feature_selection.SelectFromModel.inverse_transform)(X)
  - Invierte la operación de transformación.
* - [partial_fit](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectFromModel.html#sklearn.feature_selection.SelectFromModel.partial_fit)(X,  y=None,  **partial_fit_params)
  - Ajusta el metatransformador `SelectFromModel` sólo una vez.
* - [transform](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectFromModel.html#sklearn.feature_selection.SelectFromModel.transform)(X)
  - Reduce _X_ a los _features_ seleccionados.
```

<br/>

### SelectPercentile

[SelectPercentile](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectPercentile.html): Selecciona un porcentaje de las _features_ más importantes según una métrica estadística (como chi-cuadrado o ANOVA F-value). Es útil para la reducción de dimensionalidad en problemas de clasificación o regresión, especialmente con muchas _features_.
```python
# Sintaxis de llamada
SelectPercentile(score_func=<function f_classif>, *, percentile=10)
```
**Parámetros:**
- **score_func** - `callable`: Función que tome dos arreglos _X_ y _y_ retorne un par de arrays `(scores, p-values)` o un solo array con los _scores_. Algunas opciones son:
    - _f_classif_: Para problemas de clasificación.
    - _f_regression_: Para problemas de regresión.
- **percentile** - `int`: Porcentaje de _features_ a mantener.

#### Atributos

Atributos de la clase `SelectPercentile`.

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - **feature_names_in_**
  - Nombres de las _features_ observados durante el ajuste. Definido sólo cuando _X_ tiene nombres de _features_ que son todos cadenas. 
* - **n_features_in_**
  - Número de _features_ vistos durante el ajuste.
* - **pvalues_**
  - Valores _p_ de las puntuaciones de las _features_, `None` si _score_func_ devuelve sólo puntuaciones.
* - **scores_**
  - _Scores_ de los _features_.
```

#### Métodos

Métodos de la clase `SelectPercentile`.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [fit](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectPercentile.html#sklearn.feature_selection.SelectPercentile.fit)(X, y=None)
  - Corre la función de puntuación en _(X, y)_ y retorna los _features_ apropiados.
* - [fit_transform](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectPercentile.html#sklearn.feature_selection.SelectPercentile.fit_transform)(X,  y=None,  **fit_params)
  - Ajusta a los datos, luego los transforma..
* - [inverse_transform](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectPercentile.html#sklearn.feature_selection.SelectPercentile.inverse_transform)(X)
  - Invierte la operación de transformación.
* - [transform](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectPercentile.html#sklearn.feature_selection.SelectPercentile.transform)(X)
  - Reduce _X_ a los _features_ seleccionados.
```

<br/>

## Funciones

Funciones implementadas en el módulo `feature_selection`.

```{list-table}
:header-rows: 1

* - Clase
  - Descripción
* - [chi2](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.chi2.html)(X, y)
  - Calcula las estadísticas de _chi-cuadrado_ entre cada _feature_ no negativa y la clase.
* - [f_classif](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.f_classif.html)(X, y)
  - Calcula el valor _F_ de ANOVA para la muestra proporcionada.
* - [f_regression](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.f_regression.html)(X, y, ...)
  - Pruebas de regresión lineal univariada que devuelven valores _p_ y estadísticos _F_.
* - [mutual_info_classif](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.mutual_info_classif.html)(X, y, ...)
  - Estima información mutua para una variable objetivo discreta.
* - [mutual_info_regression](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.mutual_info_regression.html)(X, y, ...)
  - Estima información mutua para una variable objetivo continua.
* - [r_regression](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.r_regression.html)(X, y, ...)
  - Calcula la _r_ de Pearson para cada _feature_ y el objetivo.
```