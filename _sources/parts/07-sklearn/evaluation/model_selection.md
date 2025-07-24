# Model Selection

Ofrece herramientas para la selección y evaluación de modelos, como validación cruzada, búsqueda de hiperparámetros y división de datos. Para importar este módulo o una clase o función específica usar:

```python
# Importar módulo
from sklearn import model_selection

# Importar clase específica
from sklearn.model_selection import ClassName

# Importar función específica
from sklearn.model_selection import func_name
```
- _ClassName_ o _func_name_ es el nombre de la clase o función respectivamente.

:::{note}
Para más información de esta librería visitar la [documentación](https://scikit-learn.org/stable/api/sklearn.model_selection.html) de `sklearn`.
:::

<br/>

## Clases

Clases implementadas en el módulo `model_selection`. A continuación se presenta un resumen de los tipos de clases:
- **Splitters**: Contiene herramientas para dividir datos en conjuntos de entrenamiento y prueba, como `KFold` y `StratifiedKFold`. Útil para validación cruzada y evaluación de modelos.
- **Optimizadores de hiperparámetros**: Incluye métodos para optimizar hiperparámetros, como `GridSearchCV` y `RandomizedSearchCV`. Permite encontrar la mejor combinación de hiperparámetros para un modelo.
- **Optimización del modelo post-ajuste**: Proporciona técnicas para ajustar modelos después de su entrenamiento, como `learning_curve` y `validation_curve`. Ayuda a diagnosticar problemas como sobreajuste o subajuste.
- **Visualización**: Incluye herramientas para visualizar resultados de la selección de modelos, como gráficos de curvas de aprendizaje y validación. Facilita la interpretación de los resultados.

### Optimizadores de hiperparámetros

Incluye métodos para optimizar hiperparámetros. Permite encontrar la mejor combinación de hiperparámetros para un modelo. 

```{list-table}
:header-rows: 1

* - Clase
  - Descripción
* - [GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html)(estimator, param_grid, ...)
  - Búsqueda exhaustiva sobre valores de parámetros especificados para un estimador.
* - [HalvingGridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.HalvingGridSearchCV.html)(estimator, param_grid, ...)
  - Búsqueda sobre valores de parámetros especificados con división sucesiva por la mitad.
* - [HalvingRandomSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.HalvingRandomSearchCV.html)(estimator, param_distributions, ...)
  - Búsqueda aleatoria de hiperparámetros.
* - [ParameterGrid](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.ParameterGrid.html)(param_grid)
  - Malla de parámetros con un número discreto de valores para cada uno.
* - [ParameterSampler](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.ParameterSampler.html)(param_distributions, n_iter, ...)
  - Generador sobre parámetros muestreados a partir de distribuciones dadas.
* - [RandomizedSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html)(estimator, param_distributions, ...)
  - Búsqueda aleatoria de hiperparámetros.
```

<br/>

#### GridSearchCV

[GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html): Realiza una búsqueda exhaustiva de hiperparámetros sobre una cuadrícula predefinida, utilizando validación cruzada para evaluar cada combinación. y retorna información sobre la combinación de valores con mejor desempeño. Se calcularán _subscores_ por cada _fold_ del CV, con base a esos _scores_ se eligirá los parámetros, estimadores o preprocesadores que tuvieron mejor desempeño y se ajustará un modelo con todos los datos con esos parámetros. Es útil para optimización de hiperparámetros para mejorar el rendimiento de modelos, como SVM, _Random Forest_ o regresión logística.

:::{caution}
Esta clase puede ser computacionalmente costosa.
:::

```python
# Sintaxis de llamada
GridSearchCV(estimator, param_grid, *, scoring=None, n_jobs=None, refit=True, cv=None, 
             verbose=0, pre_dispatch='2*n_jobs', error_score=nan, return_train_score=False)
```
**Parámetros:**
- **estimator** - `estimator object`: Objeto del modelo, puede ser un `Pipeline` o un modelo de `XGBoost`.
- **param_grid** - `dict` o `list de dict`:
    - `dict`: Diccionario cuyas llaves (`str`) son los nombres de los parámetros, estimadores o preprocesadores y como valores `array-like` con los posibles valores de esos parámetros
    - `list de dict`: Lista del diccionarios como el descrito en el _bullet_ anterior, en ese caso cada diccionario se evaluará de manera independiente al resto.
    - **IMPORTANTE**: Si _estimator_ es `Pipeline` para referirse a los nombres del parámetro usar la siguiente sintaxis como llaves: `'estimator__parameter'`, (doble guíon bajo) donde _estimator_ es el nombre del modelo/transformador en el `Pipeline` (definido en _steps_) y _parameter_ es el nombre del parámetro. Se puede usar `estimator.get_params().keys()` para ver las llaves. Por ejemplo, si _steps_ se definió como `steps = [(('estimator', est)]` entonces, usar <br/> `{'estimator__hyp_name': array_like_object}`
- **scoring** - `str`, `callable`, `list`, `tuple` o `dict`: Estrategia para evaluar el desempeño del modelo cross-validated en el conjunto _test_.
    - Un solo score: Puede ser `str` o `callable`.
    - Múltiples _scores_: `list` o `tuples` de `str` únicos, `callable` o un `dict` con el nombre de las métricas como llaves y `callable` como valores.
- **n_jobs** - `int`: Para paralelizar el proceso en los núcleos CPU de la computadora, si se usa -1 indica que se usen todos los núcleos disponibles.
- **cv** - `int`, `cross-validation generator` o `iterator`: Determina la estrategia de división.
    - `None`: Utiliza el valor por default de 5.
    - `int`: Especifica el número de _folds_ en (_Stratified_) _Kfold_.
    - `cross-validation generator`: Hay clases que generan estrategias de división como `LeaveOneOut()`, etc. Ver {ref}`model-selection-splitters`.

##### Uso

La forma básica de usar este clase es la siguiente:

```python
# Importar la clase
from sklearn.model_selection import GridSearchCV

# Definir dict de valores de los hiperparámetros
param_grid = {'hyp_name': array_like_object, ...}

# Definir estimador
est = Estimator()

# Definir el GridSearch
est_cv = GridSearchCV(est, param_grid, scoring, cv=5)

# Ajustar modelo
est_cv.fit(X, y)

# Imprimir mejores parámetros
print(est_cv.best_params_)

# Imprimir mejor score
print(est_cv.best_score_)

# Recuperar mejor modelo
best_model = est_cv.best_estimator_
````
- _best_model_ será un `estimator` al cual se le pueden aplicar cualquier método como `.predict()`, `.score()`, etc.

##### Atributos

Atributos de la clase `GridSearchCV`.

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - **best_estimator_**
  - Estimador elegido por la búsqueda, es decir, el estimador que dio la puntuación más alta (o la pérdida más pequeña si se especifica) en los datos omitidos. No disponible si `refit=False`.
* - **best_index_**
  - El índice (de las matrices `cv_results_`) que corresponde a la mejor parametrización candidata.
* - **best_params_**
  - Parámetro que ha dado los mejores resultados en los datos de retención.
* - **best_score_**
  - Puntuación media de validación cruzada del _best_estimator_.
* - **classes_**
  - Etiquetas de clase.
* - **cv_results_**
  - Un `dict` con claves como encabezados de columna y valores como columnas, que pueden importarse a un `DataFrame`.
* - **feature_names_in_**
  - Nombres de las características vistas durante el ajuste. Sólo se define si `best_estimator_`.
* - **multimetric_**
  - Indica si los _scorers_ computan o no varias métricas.
* - **n_features_in_**
  - Número de _features_ observados durante el ajuste.
* - **n_splits_**
  - El número de divisiones de validación cruzada (_folds_/iteraciones).
* - **refit_time_**
  - Segundos utilizados para volver a ajustar el mejor modelo en todo el conjunto de datos.
* - **scorer_**
  - Función de puntuación utilizada en los datos retenidos para elegir los mejores parámetros del modelo.
```

##### Métodos

Métodos de la clase `GridSearchCV`.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [decision_function](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV.decision_function)(X)
  - Llama a la _decision_function_ en el estimador con los mejores parámetros encontrados.
* - [fit](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV.fit)(X,  y=None,  **params)
  - Ejecuta el ajuste con todos los conjuntos de parámetros.
* - [inverse_transform](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV.inverse_transform)(X=None,  Xt=None)
  - Llama a _inverse_transform_ en el estimador con los mejores params encontrados.
* - [predict](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV.predict)(X)
  - Llama a _predect_ en el estimador con los mejores parámetros encontrados.
* - [predict_log_proba](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV.predict_log_proba)(X)
  - Llama a _predict_log_proba_ en el estimador con los mejores parámetros encontrados.
* - [predict_proba](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV.predict_proba)(X)
  - Llama a _predict_proba_ en el estimador con los mejores parámetros encontrados.
* - [score](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV.score)(X,  y=None,  **params)
  - Retorna la puntuación en los datos dados, si el estimador ha sido reajustado.
* - [score_samples](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV.score_samples)(X)
  - Llama a _score_samples_ en el estimador con los mejores parámetros encontrados.
* - [transform](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV.transform)(X)
  - Llama a la transformación en el estimador con los mejores parámetros encontrados.
```

<br/>

#### RandomizedSearchCV

[RandomizedSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html): Realiza una selección aleatoria de  valores de parámetros para un estimador (modelo) de manera iterariva para seleccionar la combinación que genera el mejor desempeño. Retorna información sobre la combinación de valores con mejor desempeño.
```python
# Sintaxis de llamada
RandomizedSearchCV(estimator, param_distributions, *, n_iter=10, scoring=None, n_jobs=None, 
                   refit=True, cv=None, verbose=0, pre_dispatch='2*n_jobs', 
                   random_state=None, error_score=nan, return_train_score=False)
```
**Parámetros:**
- **estimator** - `estimator object`: Objeto del modelo.
- **param_distributions** - `dict` o `list de dict`:
    - `dict`: Diccionario cuyas llaves (`str`) son los nombres de los parámetros y como valores son distribuciones de probabilidad o `list` con los posibles valores de esos parámetros.
    - `list de dict`: Lista del diccionarios como el descrito en el _bullet_ anterior, se usa este tipo cuando se quiere probar distintos preprocesadores con distintos estimadores, en ese caso cada `dict` será un conjunto de preprocesadores/estimadores a probar.
    - **IMPORTANTE**: Si _estimator_ es `Pipeline` para referirse a los nombres del parámetro usar la siguiente sintaxis como llaves: `estimator__parameter`, (doble guíon bajo) donde _estimator_ es el nombre del modelo en el `Pipeline` y _parameter_ es el nombre del parámetro. Puedes usar `estimator.get_params().keys()` para ver las llaves.
- **n_iter** - `int`: Número de iteraciones en las que en cada uno los parámetros serán seleccionados al azar.
- **scoring** - `str`, `callable`, `list`, `tuple` o `dict`: Estrategia para evaluar el desempeño del modelo _cross-validated_ en el conjunto _test_.
    - Un solo score: Puede ser `str` o `callable`.
    - Múltiples _scores_: `list` o `tuples` de `str` únicos, `callable` o un `dict` con el nombre de las métricas como llaves y `callable` como valores.
- **cv** - `int`, `iterator`, `None` o `cross-validation generator`: Determina la estrategia de _cross-validation splitting_.
    - `None`: Utiliza el valor por default de 5.
    - `int`: Especifica el número de _folds_ en (_Stratified_) _Kfold_.
    - `cross-validation generator`: Hay clases que generan estrategias de división como `LeaveOneOut()`, etc. Ver {ref}`model-selection-splitters`.
- **random_state** - `int`, `RandomState Instance`: Semilla del generador de números pseudo aleatorios, útil para reproducibilidad.

##### Uso

La forma básica de usar este clase es la siguiente:

```python
# Importar la clase
from sklearn.model_selection import RandomizedSearchCV

# Definir dict de valores de los hiperparámetros
param_dist = {'hyp_name': array_like_object, ...}

# Definir estimador
est = Estimator()

# Definir el GridSearch
est_cv = RandomizedSearchCV(est, param_dist, cv=5)

# Ajustar modelo
est_cv.fit(X, y)

# Imprimir mejores parámetros
print(est_cv.best_params_)

# Imprimir mejor score
print(est_cv.best_score_)
````

##### Atributos

Atributos de la clase `RandomizedSearchCV`.

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - **best_estimator_**
  - Estimador elegido por la búsqueda, es decir, el estimador que dio la puntuación más alta (o la pérdida más pequeña si se especifica) en los datos omitidos. No disponible si `refit=False`.
* - **best_index_**
  - El índice (de las matrices `cv_results_`) que corresponde a la mejor parametrización candidata.
* - **best_params_**
  - Parámetro que ha dado los mejores resultados en los datos de retención.
* - **best_score_**
  - Puntuación media de validación cruzada del _best_estimator_.
* - **classes_**
  - Etiquetas de clase.
* - **cv_results_**
  - Un `dict` con claves como encabezados de columna y valores como columnas, que pueden importarse a un `DataFrame`.
* - **feature_names_in_**
  - Nombres de las características vistas durante el ajuste. Sólo se define si `best_estimator_`.
* - **multimetric_**
  - Indica si los _scorers_ computan o no varias métricas.
* - **n_features_in_**
  - Número de _features_ observados durante el ajuste.
* - **n_splits_**
  - El número de divisiones de validación cruzada (_folds_/iteraciones).
* - **refit_time_**
  - Segundos utilizados para volver a ajustar el mejor modelo en todo el conjunto de datos.
* - **scorer_**
  - Función de puntuación utilizada en los datos retenidos para elegir los mejores parámetros del modelo.
```

##### Métodos

Métodos de la clase `RandomizedSearchCV`.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [decision_function](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#sklearn.model_selection.RandomizedSearchCV.decision_function)(X)
  - Llama a la _decision_function_ en el estimador con los mejores parámetros encontrados.
* - [fit](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#sklearn.model_selection.RandomizedSearchCV.fit)(X,  y=None,  **params)
  - Ejecuta el ajuste con todos los conjuntos de parámetros.
* - [inverse_transform](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#sklearn.model_selection.RandomizedSearchCV.inverse_transform)(X=None,  Xt=None)
  - Llama a _inverse_transform_ en el estimador con los mejores params encontrados.
* - [predict](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#sklearn.model_selection.RandomizedSearchCV.predict)(X)
  - Llama a _predect_ en el estimador con los mejores parámetros encontrados.
* - [predict_log_proba](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#sklearn.model_selection.RandomizedSearchCV.predict_log_proba)(X)
  - Llama a _predict_log_proba_ en el estimador con los mejores parámetros encontrados.
* - [predict_proba](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#sklearn.model_selection.RandomizedSearchCV.predict_proba)(X)
  - Llama a _predict_proba_ en el estimador con los mejores parámetros encontrados.
* - [score](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#sklearn.model_selection.RandomizedSearchCV.score)(X,  y=None,  **params)
  - Retorna la puntuación en los datos dados, si el estimador ha sido reajustado.
* - [score_samples](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#sklearn.model_selection.RandomizedSearchCV.score_samples)(X)
  - Llama a _score_samples_ en el estimador con los mejores parámetros encontrados.
* - [transform](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#sklearn.model_selection.RandomizedSearchCV.transform)(X)
  - Llama a la transformación en el estimador con los mejores parámetros encontrados.
```



<br/>

### Optimización del modelo post-ajuste

Proporciona técnicas para ajustar modelos después de su entrenamiento. Ayuda a diagnosticar problemas como sobreajuste o subajuste. 

```{list-table}
:header-rows: 1

* - Clase
  - Descripción
* - [FixedThresholdClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.FixedThresholdClassifier.html)(estimator, ...)
  - Clasificador binario que establece manualmente el umbral de decisión.
* - [TunedThresholdClassifierCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TunedThresholdClassifierCV.html)(estimator, ...)
  - Clasificador que ajusta posteriormente el umbral de decisión mediante validación cruzada.
```

<br/>

(model-selection-splitters)=
### Splitters

Contiene herramientas para dividir datos en conjuntos de entrenamiento y prueba. Útil para validación cruzada y evaluación de modelos.

:::{tip}
Revisar también la función {ref}`train_test_split()<model-selection-train-test-split>`.
:::

```{list-table}
:header-rows: 1

* - Clase
  - Descripción
* - [GroupKFold](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GroupKFold.html)(n_splits=5, ...)
  - Variante del iterador _K-fold_ con grupos no solapados.
* - [GroupShuffleSplit](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GroupShuffleSplit.html)(n_splits=5, ...)
  - Iterador de validación cruzada _Shuffle-Group(s)-Out_.
* - [KFold](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html)(n_splits=5, ...)
  - Validador cruzado _K-fold_.
* - [LeaveOneGroupOut](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LeaveOneGroupOut.html)()
  - Validador cruzado _"Leave One Group Out"_.
* - [LeaveOneOut](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LeaveOneOut.html)()
  - Validador cruzado _Leave-One-Out_.
* - [LeavePGroupsOut](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LeavePGroupsOut.html)(n_groups)
  - Dejar _P_ grupo(s) fuera del validador cruzado.
* - [LeavePOut](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LeavePOut.html)(p)
  - Validador cruzado _Leave-P-Out_.
* - [PredefinedSplit](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.PredefinedSplit.html)(test_fold)
  - Validador cruzado dividido predefinido.
* - [RepeatedKFold](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RepeatedKFold.html)(...)
  - Validador cruzado _K-fold_ repetido.
* - [RepeatedStratifiedKFold](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RepeatedStratifiedKFold.html)(...)
  - Validador cruzado _K-fold_ estratificado repetido.
* - [ShuffleSplit](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.ShuffleSplit.html)(n_splits=10, ...)
  - Validador cruzado de permutación aleatoria.
* - [StratifiedGroupKFold](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedGroupKFold.html)(n_splits=5, shuffle=False, random_state=None)
  - Variante del iterador _K-fold_ estratificado con grupos no solapados.
* - [StratifiedKFold](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedKFold.html)(n_splits=5, ...)
  - Validador cruzado _K-fold_ estratificado.
* - [StratifiedShuffleSplit](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedShuffleSplit.html)(n_splits=10, ...)
  - Validador cruzado estratificado `ShuffleSplit`.
* - [TimeSeriesSplit](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html)(n_splits=5, ...)
  - Validador cruzado de series de tiempo.
```

<br/>

#### GroupKFold

[GroupKFold](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GroupKFold.html): Crea un cross validaton con no _overlapping groups_. El mismo grupo no aparecerá en dos diferentes _folds_, cada grupo solo podrá ser _train_ o _test_, pero no ambos.
```python
# Sintaxis de llamada
GroupKFold(n_splits=5, *, shuffle=False, random_state=None)
```
**Parámetros:**
- **n_splits** - `int`: Número de _folds_, debe ser mayor que dos.
- **shuffle** - `bool`: Para indicar que los datos se ordenen aleatoriamente previo a realizar los _folds_.
- **random_state** - `int` o `RandomInstance`: Semilla para controlar la aleatoriedad en cada _fold_.

:::{note}
Esta clase no tiene atributos.
:::

##### Métodos

Métodos de la clase `GroupKFold`.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [get_n_splits](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GroupKFold.html#sklearn.model_selection.GroupKFold.get_n_splits)(X=None,  y=None,  groups=None)
  - Retorna el número de iteraciones de división en el validador cruzado.
* - [split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GroupKFold.html#sklearn.model_selection.GroupKFold.split)(X,  y=None,  groups=None)
  - Genera índices para dividir los datos en conjunto de entrenamiento y de prueba.
```

<br/>

#### KFold

[KFold](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html): Crea un _cross validation_ de k-folds. En cada iteración se utiliza _k fold_ como _test set_.
```python
# Sintaxis de llamada
KFold(n_splits=5, *, shuffle=False, random_state=None)
```
**Parámetros:**
- **n_splits** - `int`: Número de _folds_, debe ser mayor que dos.
- **shuffle** - `bool`: Para indicar que los datos se ordenen aleatoriamente previo a realizar los _folds_.
- **random_state** - `int` o `RandomInstance`: Semilla para controlar la aleatoriedad en cada _fold_.

:::{note}
Esta clase no tiene atributos.
:::

##### Métodos

Métodos de la clase `KFold`.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [get_n_splits](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html#sklearn.model_selection.KFold.get_n_splits)(X=None,  y=None,  groups=None)
  - Retorna el número de iteraciones de división en el validador cruzado.
* - [split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html#sklearn.model_selection.KFold.split)(X,  y=None,  groups=None)
  - Genera índices para dividir los datos en conjunto de entrenamiento y de prueba.
```

<br/>

#### LeaveOneOut

[LeaveOneOut](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LeaveOneOut.html): Crea un cross validation leave one out. Cada sample (cada observación) es usada como el _test_ (singleton) y resto como el training. Es equivalente a `Kfold(n_saplits=n_samples)`.
```python
# Sintaxis de llamada
LeaveOneOut()
```
**Parámetros:**
- No tiene parámetros.

:::{note}
Esta clase no tiene atributos.
:::

##### Métodos

Métodos de la clase `LeaveOneOut`.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [get_n_splits](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LeaveOneOut.html#sklearn.model_selection.LeaveOneOut.get_n_splits)(X=None,  y=None,  groups=None)
  - Retorna el número de iteraciones de división en el validador cruzado.
* - [split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LeaveOneOut.html#sklearn.model_selection.LeaveOneOut.split)(X,  y=None,  groups=None)
  - Genera índices para dividir los datos en conjunto de entrenamiento y de prueba.
```

<br/>

#### ShuffleSplit

[ShuffleSplit](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.ShuffleSplit.html): Crea un _cross validation_ de tipo _leave one out_. Cada _sample_ (cada observación) es usada como el _test_ (_singleton_) y el resto como el _training_. Es equivalente a `KFold(n_splits=n)`.
```python
# Sintaxis de llamada
ShuffleSplit(n_splits=10, *, test_size=None, train_size=None, random_state=None)
```

**Parámetros:**
- **n_splits** - `int`: Número de _re-shufflings_ y de iteraciones de _splits_.
- **test_size** - `float` o `int`: Si es `float` es un porcentaje de los datos, entre 0 y 1 , si es entero es el número de muestras. Si es `None` será el complemento de _train_size_. Si _train_size_ es `None` será 0.1.
- **train_size** - `bool`: Si es `float` es un porcentaje de los datos, entre 0 y 1 , si es entero es el número de muestras. Si es `None` será el complemento del _test_size_.
- **shuffle** - `bool`: Para indicar que los datos se orden aleatoriamente previo a realizar los _folds_.

:::{note}
Esta clase no tiene atributos.
:::


##### Métodos

Métodos de la clase `ShuffleSplit`.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [get_n_splits](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.ShuffleSplit.html#sklearn.model_selection.ShuffleSplit.get_n_splits)(X=None,  y=None,  groups=None)
  - Retorna el número de iteraciones de división en el validador cruzado.
* - [split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.ShuffleSplit.html#sklearn.model_selection.ShuffleSplit.split)(X,  y=None,  groups=None)
  - Genera índices para dividir los datos en conjunto de entrenamiento y de prueba.
```

<br/>

#### StratifiedKFold

[StratifiedKFold](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedKFold.html): Crea un _cross validation_ de _k-folds_ estratificado. Preserva el porcentaje de muestras en cada clase (el número de observaciones para cada etiqueta única del _target_). Se prefiere esta estrategia en problemas de clasificación.
```python
# Sintaxis de llamada
StratifiedKFold(n_splits=5, *, shuffle=False, random_state=None)
```
**Parámetros:**
- **n_splits** - `int`: Número de _folds_, debe ser mayor que dos.
- **shuffle** - `bool`: Para indicar que los datos se ordenen aleatoriamente previo a realizar los _folds_.
- **random_state** - `int` o `RandomInstance`: Semilla para controlar la aleatoriedad en cada _fold_.

:::{note}
Esta clase no tiene atributos.
:::

##### Métodos

Métodos de la clase `StratifiedKFold`.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [get_n_splits](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedKFold.html#sklearn.model_selection.StratifiedKFold.get_n_splits)(X=None,  y=None,  groups=None)
  - Retorna el número de iteraciones de división en el validador cruzado.
* - [split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedKFold.html#sklearn.model_selection.StratifiedKFold.split)(X,  y=None,  groups=None)
  - Genera índices para dividir los datos en conjunto de entrenamiento y de prueba.
```

<br/>

#### StratifiedShuffleSplit

[StratifiedShuffleSplit](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedShuffleSplit.html): Crea un _ShuffleSplit_ estratificado. Preserva el porcentaje de muestras en cada clase (el número de observaciones para cada etiqueta única del _target_).
```python
# Sintaxis de llamada
StratifiedShuffleSplit(n_splits=10, *, test_size=None, train_size=None, random_state=None)
```
**Parámetros:**
- **n_splits** - `int`: Número de _re-shufflings_ y de iteraciones de splits.
- **test_size** - `float`, `int`, `None`: Tamaño del _test_.
    - `float`: Representa un porcentaje de los datos, entre 0 y 1.
    - `int`: Representa el número se muestras.
    - `None`: Será el complemento de _train_size_. Nota: Si _train_size_ es `None` será 0.1.
- **train_size** - `float`, `int`, `None`: Tamaño del _train_.
    - `float`: Representa un porcentaje de los datos, entre 0 y 1.
    - `int`: Representa el número se muestras.
    - `None`: Será el complemento de _test_size_. Nota: Si _test_size_ es `None` será 0.9.
- **random_state** - `int` o `RandomInstance`: Semilla para controlar la aleatoriedad en cada _fold_.

:::{note}
Esta clase no tiene atributos.
:::

##### Métodos

Métodos de la clase `StratifiedShuffleSplit`.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [get_n_splits](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedShuffleSplit.html#sklearn.model_selection.StratifiedShuffleSplit.get_n_splits)(X=None,  y=None,  groups=None)
  - Retorna el número de iteraciones de división en el validador cruzado.
* - [split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedShuffleSplit.html#sklearn.model_selection.StratifiedShuffleSplit.split)(X,  y=None,  groups=None)
  - Genera índices para dividir los datos en conjunto de entrenamiento y de prueba.
```

<br/>

#### TimeSeriesSplit

[TimeSeriesSplit](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html): Crea un _cross validation_ de series de tiempo. Es una variación del _kfold_, en el que en cada _split_ se retorna los primero _k folds_ como _train_ y el _(k+1) fold_ como el _test_.
```python
# Sintaxis de llamada
TimeSeriesSplit(n_splits=5, *, max_train_size=None, test_size=None, gap=0)
```
**Parámetros:**
- **n_splits** - `int`: Número de _folds_, debe ser mayor que dos.

:::{note}
Esta clase no tiene atributos.
:::

##### Métodos

Métodos de la clase `TimeSeriesSplit`.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [get_n_splits](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html#sklearn.model_selection.TimeSeriesSplit.get_n_splits)(X=None,  y=None,  groups=None)
  - Retorna el número de iteraciones de división en el validador cruzado.
* - [split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html#sklearn.model_selection.TimeSeriesSplit.split)(X,  y=None,  groups=None)
  - Genera índices para dividir los datos en conjunto de entrenamiento y de prueba.
```

<br/>

### Visualización

Incluye herramientas para visualizar resultados de la selección de modelos, como gráficos de curvas de aprendizaje y validación. Facilitan la interpretación de los resultados.

```{list-table}
:header-rows: 1

* - Clase
  - Descripción
* - [LearningCurveDisplay](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LearningCurveDisplay.html)(...)
  - Visualización de la curva de aprendizaje.
* - [ValidationCurveDisplay](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.ValidationCurveDisplay.html)(...)
  - Visualización de la curva de validación.
```

<br/>

## Funciones

Funciones implementadas en el módulo `model_selection`.

### Splitters

Contiene herramientas para dividir datos en conjuntos de entrenamiento y prueba, como `train_test_split`.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [check_cv](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.check_cv.html)(cv=5, y=None, ...)
  - Utilidad de comprobación de entrada para construir un validador cruzado.
* - [train_test_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html)(*arrays, test_size=None, train_size=None, random_state=None, shuffle=True, stratify=None)
  - Divide matrices o arreglos en subconjuntos aleatorios de entrenamiento y prueba.
```

(model-selection-train-test-split)=
#### Notas de _train_test_split_

[train_test_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html): Divide un _dataset_ en los _subsets_ aleatorios _test_ y _training_, tanto variables dependientes e independientes. Retorna dos arrays (_train_ y _test_ en ese orden) por cada _array_ de entrada. Por ejemplo para dos datos de entrada (_X, y_) retornará: _X_train_, _X_test_, _y_train_, _y_test_.
```python
# Sintaxis de llamada
train_test_split(*arrays, test_size=None, train_size=None, random_state=None, shuffle=True, 
                 stratify=None)
```
**Parámetros:**
- **arrays** - `array-like`: Son los _arrays_ de los _features_ (_X_) y _target_ (_y_) (variables dependientes e independientes respectivamente), en ese orden, separadas por coma. No estrictamente se tiene que ingresar los dos, podría ser solo uno, o incluso 3 o más, en ese caso se retornará un split (2 objetos) por cada dataset. Se retornan en el orden en que se puso en este argumento.
- **test_size** - `float` o `int`: Si es `float` es la proporción de datos que se incluirán en el subset de _test_. Si es `int` es el tamaño de la muestra de _test_.
- **train_size** - `float` o `int`: Si es `float` es la proporción de datos que se incluirán en el subset de _train_. Si es `int` es el tamaño de la muestra de _train_.
- **random_state** - `int`, `RandomState Instance`: Semilla del generador de números pseudo aleatorios, útil para reproducibilidad.
- **shuffle** - `bool`: Para indicar el orden de los datos de modifique aleatoriamente antes de dividir del dataset.
- **stratify** - `array-like`, `None`: Para hacer el _split_ de una manera estratificada, utiliza los _labels_ de este array. Se utiliza principalmente para problemas de clasificación.

**Retorna:**
- `list` de longitud `2*len(arrays)`.

Uso básico:

```python
# Import función
from sklearn.model_selection import train_test_split

# Realizar split como % del test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=21, stratify=y)
```

### Validación del modelo

Ofrece funciones para validar modelos. Evalúan el rendimiento del modelo utilizando validación cruzada.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [cross_val_predict](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_predict.html)(estimator, X, y=None, ...)
  - Genera estimaciones de validación cruzada para cada punto de datos de entrada..
* - [cross_val_score](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_score.html)(estimator, X, y=None, ...)
  - Evalúa un puntuación mediante validación cruzada.
* - [cross_validate](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html)(estimator, X, y=None, ...)
  - Evalúa la(s) métrica(s) mediante validación cruzada y registra también los tiempos de ajuste/puntuación.
* - [learning_curve](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.learning_curve.html)(estimator, X, y, ...)
  - Curva de aprendizaje.
* - [permutation_test_score](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.permutation_test_score.html)(estimator, X, y, ...)
  - Evalúa la importancia de una puntuación validada de forma cruzada con permutaciones.
* - [validation_curve](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.validation_curve.html)(estimator, X, y, ...)
  - Curva de validación.
```

#### Notas de _cross_val_score_

[cross_val_score](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_score.html): Evalúa un puntuación mediante validación cruzada.
```python
# Sintaxis de llamada
cross_val_score(estimator, X, y=None, *, groups=None, scoring=None, cv=None, n_jobs=None, 
                verbose=0, params=None, pre_dispatch='2*n_jobs', error_score=nan)
```
**Parámetros:**
- **estimator** - `estimator object`: Objeto de un modelo que implementa el método `.fit()`. También puede ser un _Pipeline_.
- **X** - `array-like`: Los datos a ajustar (_features_).
- **y** - `array-like`: La variable _target_ (_response_).
- **cv** - `int`, `cross-validation generator` o `iterator`: Determina la estrategia de división.
    - `None`: Utiliza el valor por default de 5.
    - `int`: Especifica el número de _folds_ en (_Stratified_) `Kfold()`.
    - Cualquier instancia de una clase de {ref}`model-selection-splitters`.
- **scoring** - `str` o `callable`: Métrica a usar para medir la calidad del modelo. Por default se utiliza el _score_ usado en cada _estimator_ (modelo) si existe. Ver {doc}`../anexos`

**Retorna:**
- `ndarray` de puntajes.

Uso básico:

```python
# Importar función
from sklearn.model_selection import cross_val_score

# Definir estimador
est = Estimator(hyperparams)

# Aplicar el cv por número de folds
cv_results = cross_val_score(est, X, y, cv=5)
```