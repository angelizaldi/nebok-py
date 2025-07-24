# Neighbors

Este módulo implementa algoritmos _k-nearest neighbors_ (kNN). Para importar este módulo o una clase/función específica usar:

```python
# Importar módulo
from sklearn import neighbors

# Importar clase específica
from sklearn.neighbors import ClassName

# Importar función específica
from sklearn.neighbors import func_name
```
- _ClassName_ o _func_name_ es el nombre de la clase o función respectivamente.

:::{note}
Para más información de este módulo visitar la [documentación](https://scikit-learn.org/stable/api/sklearn.neighbors.html) de `sklearn`.
:::

## Clases

Clases implementadas en el módulo _neighbors_.

```{list-table}
:header-rows: 1

* - Clase
  - Descripción
* - [BallTree](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.BallTree.html)()
  - _BallTree_ para problemas generalizados de N-puntos.
* - [KDTree](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KDTree.html)()
  - _KDTree_ para problemas generalizados N-puntos.
* - [KNeighborsClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html)(n_neighbors=5, ...)
  - Clasificador que implementa la votación de los _k_ vecinos más cercanos.
* - [KNeighborsRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsRegressor.html)(n_neighbors=5, ...)
  - Regresión basada en _k_ vecinos más cercanos.
* - [KNeighborsTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsTransformer.html)(...)
  - Transforma _X_ en un gráfico (ponderado) de _k_ vecinos más cercanos.
* - [KernelDensity](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KernelDensity.html)(...)
  - Estimación de la densidad del kernel.
* - [LocalOutlierFactor](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.LocalOutlierFactor.html)(n_neighbors=20, ...)
  - Detección de valores atípicos no supervisada mediante el factor de valor atípico local (LOF).
* - [NearestCentroid](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestCentroid.html)(metric='euclidean', ...)
  - Clasificador de centroide más cercano.
* - [NearestNeighbors](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestNeighbors.html)(...)
  - Algoritmo no supervisado para implementar búsquedas de vecinos.
* - [NeighborhoodComponentsAnalysis](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NeighborhoodComponentsAnalysis.html)(n_components=None, ...)
  - Análisis de componentes del vecindario.
* - [RadiusNeighborsClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.RadiusNeighborsClassifier.html)(radius=1.0, ...)
  - Clasificador que implementa una votación entre vecinos dentro de un radio determinado.
* - [RadiusNeighborsRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.RadiusNeighborsRegressor.html)(radius=1.0, ...)
  - Regresión basada en vecinos dentro de un radio fijo.
* - [RadiusNeighborsTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.RadiusNeighborsTransformer.html)(...)
  - Transforma _X_ en un gráfico (ponderado) de vecinos más cercanos en un radio.
```

<br/>

---
### KNeighborsClassifier

[KNeighborsClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html): Implementa el algoritmo de K-Vecinos Más Cercanos (_K-Nearest Neighbors_, KNN) para clasificación. Predice la clase de una muestra basándose en las clases de los _k_ vecinos más cercanos en el espacio de _features_.
```python
# Sintaxis de llamada
KneighborsClassifier(n_neighbors=5, *, weights='uniform', algorithm='auto', leaf_size=30, 
                     p=2, metric='minkowski', metric_params=None, n_jobs=None)
```
**Parámetros:**
- **n_neighbors** - `int`: Número de vecinos a utilizar.
- **weights** - {'uniform', 'distance'} o `callable`: Función de ponderaciones a usar en predicciones:
    - 'uniform': Cada punto en todos los vecindarios son igualmente ponderados.
    - 'distance': Pondera los puntos por la inversa de su distancia. Puntos más cercanos tendrán más influencia.
    - `callable`: Función definida por el usuario que acepte un `ndarray` de distancias y devuelva un `ndarray` de ponderaciones.
- **algorithm** - {'auto', 'ball_tree', 'kd_tree', 'brute'}: Algoritmo usado para calcular los vecinos más cercanos.
- **leaf_size** - `int`: Tamaño del _leaf_ en lo algoritmos `BallTree` y `KDTree`.

#### Uso

La forma básica de usar este clase es la siguiente:

```python
# Importar clase
from sklearn.neighbors import KNeighborsClassifier

# Inicializar modelo
knn = KNeighborsClassifier(n_neighbors=n)

# Ajustar modelo
knn.fit(X_train, y_train)

# Predecir en nuevas muestras
prediction = knn.predict(X_test)

# Evaluar el modelo
score = knn.score(X_test, y_test)
```
- _n_neighbors_ es el hiperparámetro más importante, entre más alto sea el número de _neighbors_, entonces más simple es el modelo, en cambio, entre menos _neighbors_ más complejo será el modelo. En el caso extremo en el que el número de vecinos sea igual al número de datos , entonces todos tendrán la misma predicción, la clase más común.
- _X_test_ debe ser un `2D array-like`, con el mismo número de columnas que _X_train_. En lugar de ser el _test_ set simplemente podrían ser muestras nuevas.

<br/>

#### Atributos

Atributos de la clase `KNeighborsClassifier`. 

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - **classes_**
  - Etiquetas de clase conocidas por el clasificador.
* - **effective_metric_**
  - La métrica de distancia utilizada. Será la misma que el parámetro métrico o un sinónimo de este.
* - **effective_metric_params_**
  - Argumentos _keywords_ adicionales para la función métrica.
* - **feature_names_in_**
  - Nombres de los _features_ observados durante el ajuste. Se definen únicamente cuando _X_ tiene nombres de _features_ que son todas cadenas.
* - **n_features_in_**
  - Número de los _features_ observados durante el ajuste.
* - **n_samples_fit_**
  - Número de muestras en los datos ajustados.
* - **outputs_2d_**
  - `False` cuando la forma de _y_ es `(n_muestras,)` o `(n_muestras, 1)` durante el ajuste, de lo contrario `True`.
```

<br/>

#### Métodos

Métodos de la clase `KNeighborsClassifier`.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [fit](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html#sklearn.neighbors.KNeighborsClassifier.fit)(X,  y)
  - Ajusta el clasificador de _k_ vecinos más cercanos del conjunto de datos de entrenamiento.
* - [kneighbors](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html#sklearn.neighbors.KNeighborsClassifier.kneighbors)(X=None,  n_neighbors=None,  return_distance=True)
  - Encuentra los K-vecinos de un punto.
* - [kneighbors_graph](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html#sklearn.neighbors.KNeighborsClassifier.kneighbors_graph)(X=None,  n_neighbors=None,  mode='connectivity')
  - Calcula el gráfico (ponderado) de k-vecinos para puntos en _X_.
* - [predict](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html#sklearn.neighbors.KNeighborsClassifier.predict)(X)
  - Predice las etiquetas de clase para los datos proporcionados.
* - [predict_proba](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html#sklearn.neighbors.KNeighborsClassifier.predict_proba)(X)
  - Retorna estimaciones de probabilidad para los datos de prueba _X_.
* - [score](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html#sklearn.neighbors.KNeighborsClassifier.score)(X,  y,  sample_weight=None)
  - Retorna la precisión media de los datos de prueba y las etiquetas proporcionados.
```

<br/>

---
### Kernel Density Estimation

[KernelDensity](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KernelDensity.html): Es una herramienta para estimación de densidad basada en kernels. Se utiliza para modelar la distribución de probabilidad de un conjunto de datos, lo que es útil en análisis exploratorio y aprendizaje no supervisado.
```python
# Sintaxis de llamada
KernelDensity(*, bandwidth=1.0, algorithm='auto', kernel='gaussian', metric='euclidean', 
              atol=0, rtol=0, breadth_first=True, leaf_size=40, metric_params=None)
```
**Parámetros:**
- **bandwidth** - `float`: _Bandwidth_ del kernel, controla el _trade off_ varianza-sesgo en la estimación de la densidad.
- **algorithm** - {'kd_tree', 'ball_tree', 'auto'}: Algoritmo de árbol de decisión a utilizar.
- **kernel** - {'gaussian', 'tophat', 'epanechnikov', 'exponential', 'linear', 'cosine'}: El kernel a utilizar.

<br/>

#### Atributos

Atributos de la clase `KernelDensity`. 

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - **bandwidth_**
  - Valor del _bandwidth_, dado directamente por el parámetro _bandwidth_ o estimado utilizando el método "Scott" o "Silverman".
* - **feature_names_in_**
  - Nombres de los _features_ vistos durante el ajuste. Definido solo cuando _X_ tiene nombres de _features_ que son todas las cadenas.
* - **n_features_in_**
  - Número de _features_ vistos durante el ajuste.
* - **tree_**
  - El algoritmo de árbol para problemas de _N_ puntos generalizados.
```

<br/>

#### Métodos

Métodos de la clase `KernelDensity`. 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [fit](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KernelDensity.html#sklearn.neighbors.KernelDensity.fit)(X,  y=None,  sample_weight=None)
  - Ajusta el modelo de densidad en los datos.
* - [sample](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KernelDensity.html#sklearn.neighbors.KernelDensity.sample)(n_samples=1,  random_state=None)
  - Genera muestras aleatorias del modelo.
* - [score](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KernelDensity.html#sklearn.neighbors.KernelDensity.score)(X,  y=None)
  - Calcula el _log-likelihood_ total del modelo.
* - [score_samples](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KernelDensity.html#sklearn.neighbors.KernelDensity.score_samples)(X)
  - Calcula el _log-likelihood_ de cada muestra del modelo.
```

<br/>

## Funciones

Funciones implementadas en el módulo _neighbors_.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [kneighbors_graph](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.kneighbors_graph.html)(X, n_neighbors, ...)
  - Calcula el gráfico (ponderado) de k-vecinos para puntos en _X_.
* - [radius_neighbors_graph](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.radius_neighbors_graph.html)(X, radius, ...)
  - Calcula el gráfico (ponderado) de vecinos para puntos en _X_.
* - [sort_graph_by_row_values](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.sort_graph_by_row_values.html)(graph, copy=False, ...)
  - Ordena un gráfico disperso de modo que cada fila se almacena con valores crecientes.
```
