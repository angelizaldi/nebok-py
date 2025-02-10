# Neighbors

Este módulo implementa algoritmos _k-nearest neighbors_ (kNN). Para importar este módulo o una clase/función específica usar

```python
# Importar módulo
from sklearn import neighbors

# Importar clase específica
from sklearn.neighbors import class_name

# Importar función específica
from sklearn.neighbors import func_name
```

## Clases

```{list-table}
:header-rows: 1

* - Clase
  - Descripción
* - [BallTree](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.BallTree.html)()
  - BallTree para problemas N-puntos generalizados y rápidos.. BallTree for fast generalized N-point problems.
* - [KDTree](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KDTree.html)()
  - KDTree para problemas N-puntos generalizados y rápidos.. KDTree for fast generalized N-point problems.
* - [KNeighborsClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html)(n_neighbors=5, ...)
  - Clasificador que implementa la votación de los k vecinos más cercanos.. Classifier implementing the k-nearest neighbors vote.
* - [KNeighborsRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsRegressor.html)(n_neighbors=5, ...)
  - Regresión basada en k vecinos más cercanos.. Regression based on k-nearest neighbors.
* - [KNeighborsTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsTransformer.html)(*, mode='distance', n_neighbors=5, algorithm='auto', leaf_size=30, metric='minkowski', p=2, metric_params=None, n_jobs=None)
  - Transforma X en un gráfico (ponderado) de k vecinos más cercanos.. Transform X into a (weighted) graph of k nearest neighbors.
* - [KernelDensity](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KernelDensity.html)(*, bandwidth=1.0, algorithm='auto', kernel='gaussian', metric='euclidean', atol=0, rtol=0, breadth_first=True, leaf_size=40, metric_params=None)
  - Estimación de la densidad del kernel.. Kernel Density Estimation.
* - [LocalOutlierFactor](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.LocalOutlierFactor.html)(n_neighbors=20, ...)
  - Detección de valores atípicos no supervisada mediante el factor de valor atípico local (LOF).. Unsupervised Outlier Detection using the Local Outlier Factor (LOF).
* - [NearestCentroid](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestCentroid.html)(metric='euclidean', ...)
  - Clasificador de centroide más cercano.. Nearest centroid classifier.
* - [NearestNeighbors](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestNeighbors.html)(*, n_neighbors=5, radius=1.0, algorithm='auto', leaf_size=30, metric='minkowski', p=2, metric_params=None, n_jobs=None)
  - Aprendiz no supervisado para implementar búsquedas de vecinos.. Unsupervised learner for implementing neighbor searches.
* - [NeighborhoodComponentsAnalysis](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NeighborhoodComponentsAnalysis.html)(n_components=None, ...)
  - Análisis de componentes del vecindario.. Neighborhood Components Analysis.
* - [RadiusNeighborsClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.RadiusNeighborsClassifier.html)(radius=1.0, ...)
  - Clasificador que implementa una votación entre vecinos dentro de un radio determinado.. Classifier implementing a vote among neighbors within a given radius.
* - [RadiusNeighborsRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.RadiusNeighborsRegressor.html)(radius=1.0, ...)
  - Regresión basada en vecinos dentro de un radio fijo.. Regression based on neighbors within a fixed radius.
* - [RadiusNeighborsTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.RadiusNeighborsTransformer.html)(*, mode='distance', radius=1.0, algorithm='auto', leaf_size=30, metric='minkowski', p=2, metric_params=None, n_jobs=None)
  - Transforma X en un gráfico (ponderado) de vecinos más cercanos que un radio.. Transform X into a (weighted) graph of neighbors nearer than a radius.
* - [kneighbors_graph](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.kneighbors_graph.html)(X, n_neighbors, ...)
  - Calcula el gráfico (ponderado) de k-vecinos para puntos en X.. Compute the (weighted) graph of k-Neighbors for points in X.
* - [radius_neighbors_graph](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.radius_neighbors_graph.html)(X, radius, ...)
  - Calcular el gráfico (ponderado) de vecinos para puntos en X.. Compute the (weighted) graph of Neighbors for points in X.
* - [sort_graph_by_row_values](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.sort_graph_by_row_values.html)(graph, copy=False, warn_when_not_sorted=True)
  - Ordene un gráfico disperso de modo que cada fila se almacene con valores crecientes.. Sort a sparse graph such that each row is stored with increasing values.
```

## Funciones

```{list-table}
:header-rows: 1

* - Clase
  - Descripción
* - [kneighbors_graph](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.kneighbors_graph.html)(X, n_neighbors, ...)
  - Calcula el gráfico (ponderado) de k-vecinos para puntos en X.. Compute the (weighted) graph of k-Neighbors for points in X.
* - [radius_neighbors_graph](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.radius_neighbors_graph.html)(X, radius, ...)
  - Calcular el gráfico (ponderado) de vecinos para puntos en X.. Compute the (weighted) graph of Neighbors for points in X.
* - [sort_graph_by_row_values](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.sort_graph_by_row_values.html)(graph, copy=False, warn_when_not_sorted=True)
  - Ordene un gráfico disperso de modo que cada fila se almacene con valores crecientes.. Sort a sparse graph such that each row is stored with increasing values.
```

## KNeighborsClassifier

```{list-table}
:header-rows: 1

* - Constructor
  - Descripción
* - [KNeighborsClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html)(n_neighbors=5, ...)
  - Clasificador que implementa la votación de los _k_ vecinos más cercanos.
```

### Atributos

Atributos de la clase `KNeighborsClassifier`. 

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - **classes_**
  - Etiquetas de clase conocidas por el clasificador.. Class labels known to the classifier.
* - **effective_metric_**
  - La métrica de distancia utilizada. Será la misma que el parámetro métrico o un sinónimo de este, por ejemplo, "euclidiano" si el parámetro métrico se establece en "minkowski" y el parámetro p se establece en 2.. The distance metric used. It will be same as the metric parameter or a synonym of it, e.g. ‘euclidean’ if the metric parameter set to ‘minkowski’ and p parameter set to 2.
* - **effective_metric_params_**
  - Argumentos de palabras clave adicionales para la función métrica. Para la mayoría de las métricas, serán iguales que con el parámetro metric_params, pero también pueden contener el valor del parámetro p si el atributoeffective_metric_ está configurado como ‘minkowski’.. Additional keyword arguments for the metric function. For most metrics will be same with metric_params parameter, but may also contain the p parameter value if the effective_metric_ attribute is set to ‘minkowski’.
* - **feature_names_in_**
  - Nombres de las características observadas durante el ajuste. Se definen únicamente cuando X tiene nombres de características que son todas cadenas. Se agregaron en la versión 1.0.. Names of features seen during fit. Defined only when X has feature names that are all strings. Added in version 1.0.
* - **n_features_in_**
  - Número de características observadas durante el ajuste. Agregado en la versión 0.24.. Number of features seen during fit. Added in version 0.24.
* - **n_samples_fit_**
  - Número de muestras en los datos ajustados.. Number of samples in the fitted data.
* - **outputs_2d_**
  - ´False´ cuando la forma de y es (n_muestras, ) o (n_muestras, 1) durante el ajuste, de lo contrario ´True´.. `False` when y’s shape is (n_samples, ) or (n_samples, 1) during fit otherwise `True`.
```

### Métodos

Métodos de la clase `KNeighborsClassifier`.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [fit](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html#sklearn.neighbors.KNeighborsClassifier.fit)(X,  y)
  - Ajusta el clasificador de k vecinos más cercanos del conjunto de datos de entrenamiento.. Fit the k-nearest neighbors classifier from the training dataset.
* - [kneighbors](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html#sklearn.neighbors.KNeighborsClassifier.kneighbors)(X=None,  n_neighbors=None,  return_distance=True)
  - Encuentra los K-vecinos de un punto.. Find the K-neighbors of a point.
* - [kneighbors_graph](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html#sklearn.neighbors.KNeighborsClassifier.kneighbors_graph)(X=None,  n_neighbors=None,  mode='connectivity')
  - Calcula el gráfico (ponderado) de k-vecinos para puntos en X.. Compute the (weighted) graph of k-Neighbors for points in X.
* - [predict](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html#sklearn.neighbors.KNeighborsClassifier.predict)(X)
  - Predice las etiquetas de clase para los datos proporcionados.. Predict the class labels for the provided data.
* - [predict_proba](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html#sklearn.neighbors.KNeighborsClassifier.predict_proba)(X)
  - Retorna estimaciones de probabilidad para los datos de prueba X.. Return probability estimates for the test data X.
* - [score](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html#sklearn.neighbors.KNeighborsClassifier.score)(X,  y,  sample_weight=None)
  - Retorna la precisión media de los datos de prueba y las etiquetas proporcionados.. Return the mean accuracy on the given test data and labels.
```

<br/>

---
#### Métodos _set_ y _get_

Métodos para recuperar o establecer parámetros de la clase `KNeighborsClassifier`. 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [get_metadata_routing](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html#sklearn.neighbors.KNeighborsClassifier.get_metadata_routing)()
  - Retorna la ruta de metadatos de este objeto.. Get metadata routing of this object.
* - [get_params](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html#sklearn.neighbors.KNeighborsClassifier.get_params)(deep=True)
  - Retorna parámetros para este estimador.. Get parameters for this estimator.
* - [set_params](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html#sklearn.neighbors.KNeighborsClassifier.set_params)(**params)
  - Establece los parámetros de este estimador.. Set the parameters of this estimator.
* - [set_score_request](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html#sklearn.neighbors.KNeighborsClassifier.set_score_request)(*,  sample_weight: bool | None | str = '$UNCHANGED$')
  - Solicita metadatos pasados ​​al método de puntuación.. Request metadata passed to the score method.
```

<br/>