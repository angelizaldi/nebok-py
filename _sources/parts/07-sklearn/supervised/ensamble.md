# Ensamble

Contiene métodos de ensamblaje, como _Random Forest_ y _Gradient Boosting_, que combinan múltiples modelos para mejorar la precisión y robustez. Para importar este módulo o una clase específica usar:

```python
# Importar módulo
from sklearn import ensemble

# Importar clase específica
from sklearn.ensemble import ClassName
```
- _ClassName_ es el nombre de la clase.

:::{note}
Para más información de este módulo visitar la [documentación](https://scikit-learn.org/stable/api/sklearn.ensemble.html) de `sklearn`.
:::

<br/>

## Clases

Clases implementadas en el modulo `ensemble`. 

```{list-table}
:header-rows: 1

* - Clase
  - Descripción
* - [AdaBoostClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html)(estimator=None, ...)
  - Un clasificador AdaBoost.
* - [AdaBoostRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostRegressor.html)(estimator=None, ...)
  - Un regresor de AdaBoost.
* - [BaggingClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingClassifier.html)(estimator=None, n_estimators=10, ...)
  - Un clasificador Bagging.
* - [BaggingRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingRegressor.html)(estimator=None, n_estimators=10, ...)
  - Un regresor Bagging.
* - [ExtraTreesClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesClassifier.html)(n_estimators=100, ...)
  - Un clasificador _extra-trees_.
* - [ExtraTreesRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesRegressor.html)(n_estimators=100, ...)
  - Un regresor _extra-trees_.
* - [GradientBoostingClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html)(...)
  - _Gradient Boosting_ para la clasificación.
* - [GradientBoostingRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html)(...)
  - _Gradient Boosting_ para la regresión.
* - [HistGradientBoostingClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html)(loss='log_loss', ...)
  - _Gradient Boosting Classification Tree_ basado en histogramas.
* - [HistGradientBoostingRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html)(loss='squared_error', ...)
  - _Gradient Boosting Regression Tree_ basado en histograma.
* - [IsolationForest](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html)(...)
  - Algoritmo de _Isolation Forest_.
* - [RandomForestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html)(n_estimators=100, ...)
  - Un clasificador de _random forest_.
* - [RandomForestRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html)(n_estimators=100, ...)
  - Un regresor de _random forest_.
* - [RandomTreesEmbedding](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomTreesEmbedding.html)(n_estimators=100, ...)
  - Un conjunto de _random trees_.
* - [StackingClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.StackingClassifier.html)(estimators, final_estimator=None, ...)
  - Pila de estimadores con un clasificador final.
* - [StackingRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.StackingRegressor.html)(estimators, final_estimator=None, ...)
  - Pila de estimadores con un regresor final.
* - [VotingClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.VotingClassifier.html)(estimators, ...)
  - Clasificador de reglas de votación suave/mayoritaria para estimadores _unfitted_.
* - [VotingRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.VotingRegressor.html)(estimators, ...)
  - Predicción de votación regresor para estimadores _unfitted_.
```

<br/>

### AdaBoostClassifier

[AdaBoostClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html): Implementa el algoritmo AdaBoost, que combina múltiples clasificadores débiles (generalmente árboles de decisión) en un clasificador fuerte. Ajusta los pesos de las muestras para enfocarse en los errores anteriores.
```python
# Sintaxis de llamada
AdaBoostClassifer(estimator=None, *, n_estimators=50, learning_rate=1.0, 
                  algorithm='deprecated', random_state=None)
```
**Parámetros:**
- **base_estimator** - `object`: Un modelo (una instancia de un modelo como `DecisionTreeClassifier`, `Kmeans`, etc.). Si no se especifica se utilizara un `DecisionTreeClassifier`.
- **n_estimators** - `int`: Número máximo de estimators en el cual el _boosting_ es terminado.
- **learning_rate** - `float: [0, inf]`: Peso aplicado a cada clasificador en cada iteración de refuerzo. Una mayor tasa de aprendizaje aumenta la contribución de cada clasificador. Existe un equilibrio entre los parámetros _learning_rate_ y _n_estimators_.

#### Uso

La forma básica de usar este clase es la siguiente:

```python
# Importar clase
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier

# Inicializar el modelo base (opcional, por defecto es DecisionTreeClassifier con max_depth=1)
base_model = DecisionTreeClassifier(max_depth=1, random_state=42)

# Inicializar el AdaBoostClassifier
model = AdaBoostClassifier(
    base_estimator=base_model,  # Modelo base (por defecto es DecisionTreeClassifier)
    n_estimators,            # Número de estimadores (modelos base)
    learning_rate,          # Tasa de aprendizaje
)

# Ajustar el modelo
model.fit(X, y) 

# Predecir etiquetas para nuevos datos
y_pred = model.predict(X_new)

# Predecir probabilidades (para clasificación binaria o multiclase)
y_proba = model.predict_proba(X_new)  # Devuelve las probabilidades para cada clase

# Importancia de las características (basada en los pesos de los estimadores)
feature_importances = model.feature_importances_  # Muestra la importancia de cada característica

# Acceder a los estimadores base
base_estimators = model.estimators_  # Lista de los modelos base entrenados
```
- No estrictamente tiene que ser `DecisionTreeClassifier` el modelo base.

<br/>

#### Atributos

Atributos de la clase `AdaBoostClassifier`. 

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - **classes_**
  - Las etiquetas de las clases.
* - **estimator_**
  - El estimador base del que se cultiva el _ensamble_. 
* - **estimator_errors_**
  - Error de clasificación para cada estimador en el _boosted ensemble_.
* - **estimator_weights_**
  - Pesos para cada estimador en el _boosted ensemble_.
* - **estimators_**
  - La colección de subestimadores ajustados.
* - **feature_importances_**
  - Los _feature importances_ basadas en la impureza.
* - **feature_names_in_**
  - Nombres de los _features_ vistas durante el ajuste. Definido solo cuando _X_ tiene nombres de _features_ que son todos cadenas.
* - **n_classes_**
  - El número de clases.
* - **n_features_in_**
  - Número de _features_ vistos durante el ajuste.
```

<br/>

#### Métodos

Métodos de la clase `AdaBoostClassifier`. 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [decision_function](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html#sklearn.ensemble.AdaBoostClassifier.decision_function)(X)
  - Calcula la función de decisión de _X_.
* - [fit](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html#sklearn.ensemble.AdaBoostClassifier.fit)(X,  y,  sample_weight=None)
  - Construye un _boosted_ clasificador/regresor del conjunto de entrenamiento _(X, y)_.
* - [predict](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html#sklearn.ensemble.AdaBoostClassifier.predict)(X)
  - Predice clases para _X_.
* - [predict_log_proba](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html#sklearn.ensemble.AdaBoostClassifier.predict_log_proba)(X)
  - Predice las _log-probabilities_ de clase para _X_.
* - [predict_proba](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html#sklearn.ensemble.AdaBoostClassifier.predict_proba)(X)
  - Predice las probabilidades de clase para _X_.
* - [score](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html#sklearn.ensemble.AdaBoostClassifier.score)(X,  y,  sample_weight=None)
  - Retorna la precisión media en los datos y etiquetas del _test_ dado.
* - [staged_decision_function](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html#sklearn.ensemble.AdaBoostClassifier.staged_decision_function)(X)
  - Calcula la función de decisión de _X_ para cada iteración del _boosting_.
* - [staged_predict](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html#sklearn.ensemble.AdaBoostClassifier.staged_predict)(X)
  - Retorna predicciones _staged_ para _X_.
* - [staged_predict_proba](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html#sklearn.ensemble.AdaBoostClassifier.staged_predict_proba)(X)
  - Predice las probabilidades de clase para _X_.
* - [staged_score](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html#sklearn.ensemble.AdaBoostClassifier.staged_score)(X,  y,  sample_weight=None)
  - Retorna _staged scores_ para _X_, _y_.
```

### BagginClassifer

[BaggingClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingClassifier.html): Aplica el método de Bagging (Bootstrap Aggregating) para entrenar múltiples modelos en subconjuntos aleatorios del dataset y combina sus predicciones (por votación) para mejorar la estabilidad y precisión.
```python
# Sintaxis de llamada
BagginClassifer(estimator=None, n_estimators=10, *, max_samples=1.0, max_features=1.0, 
                bootstrap=True, bootstrap_features=False, oob_score=False, 
                warm_start=False, n_jobs=None, random_state=None, verbose=0)
```

**Parámetros:**
- **base_estimator** - `object`: Es un modelo (o sea un objeto creado con una función del tipo `DecisionTreeClassifier`, `Kmeans`, etc.). Si no se especifica se utilizara un `DecisionTreeClassifier`.
- **n_estimators** - `int`: Número de modelos base en el ensamble.
- **max_samples** - `int` o `float`: El número de muestras a extraer de X para entrenar cada estimador base (con reemplazo por defecto), si es `int` es número de muestra, si es `float` es un porcentaje del total de muestras.
- **max_features** - : `int` o `float`: El número de _features_ a extraer de X para entrenar cada estimador base (sin reemplazo por defecto), si es `int` es número de _features_, si es `float` es un porcentaje del total de _features_.
- **oob_score** - `bool`: Indica si se utilizan muestras fuera de la bolsa (_out of bag_) para estimar el error de generalización. Solo disponible si `bootstrap = True`.

#### Uso

La forma básica de usar este clase es la siguiente:

```python
# Importar clase
from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier

# Inicializar el modelo base
base_model = DecisionTreeClassifier(max_depth)

# Inicializar el BaggingClassifier
model = BaggingClassifier(
    base_estimator=base_model,  # Modelo base para hacer bagging
    n_estimators,               # Número de modelos base
    max_samples,            # Fracción de muestras para entrenar cada modelo base
    max_features            # Fracción de características para entrenar cada modelo base
)

# Ajustar el modelo
model.fit(X, y) 

# Predecir etiquetas para nuevos datos
y_pred = model.predict(X_new) 

# Predecir probabilidades (si el modelo base lo soporta)
y_proba = model.predict_proba(X_new)

# Acceder a los modelos base individuales
base_models = model.estimators_ 

# Extraer score oob
oob_accuracy = bc.oob_score_
```
- No estrictamente tiene que ser `DecisionTreeClassifier` el modelo base.

<br/>

#### Atributos

Atributos de la clase `BagginClassifer`. 

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - **classes_**
  - Las etiquetas de las clases.
* - **estimator_**
  - El estimador base del que se basa el ensamble.
* - **estimators_**
  - La colección de estimadores de base ajustados.
* - **estimators_features_**
  - El subconjunto de _features_ para cada estimador base.
* - **estimators_samples_**
  - El subconjunto de muestras para cada estimador base.
* - **feature_names_in_**
  - Nombres de los _features_ vistos durante el ajuste. Definido solo cuando _X_ tiene nombres de _features_ que son todos cadenas.
* - **n_classes_**
  - El número de clases.
* - **n_features_in_**
  - Número de _features_ vistos durante el ajuste.
* - **oob_decision_function_**
  - Función de decisión calculada con una estimación _out-of-bag_ en el conjunto _training_.
* - **oob_score_**
  - Puntaje del conjunto de datos del _training_ obtenido utilizando una estimación _out-of-bag_. Este atributo existe solo cuando _oob_score_ es `True`.
```

<br/>

#### Métodos

Métodos de la clase `BagginClassifer`. 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [decision_function](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingClassifier.html#sklearn.ensemble.BaggingClassifier.decision_function)(X)
  - Promedio de las funciones de decisión de los clasificadores base.
* - [fit](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingClassifier.html#sklearn.ensemble.BaggingClassifier.fit)(X,  y,  , ...)
  - Construye un conjunto de estimadores del conjunto _training_ _(X, y)_.
* - [predict](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingClassifier.html#sklearn.ensemble.BaggingClassifier.predict)(X)
  - Predice clases para _X_.
* - [predict_log_proba](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingClassifier.html#sklearn.ensemble.BaggingClassifier.predict_log_proba)(X)
  - Predice las _log-probabilities_ de clase para _X_.
* - [predict_proba](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingClassifier.html#sklearn.ensemble.BaggingClassifier.predict_proba)(X)
  - Predice las probabilidades de clase para _X_.
* - [score](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingClassifier.html#sklearn.ensemble.BaggingClassifier.score)(X,  y,  sample_weight=None)
  - Retorna la precisión media en los datos y etiquetas del _test_ dados.
```

<br/>

### BagginRegressor

[BaggingRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingRegressor.html): Similar a `BaggingClassifier`, pero diseñado para problemas de regresión. Combina las predicciones de múltiples modelos entrenados en subconjuntos aleatorios del dataset.
```python
# Sintaxis de llamada
BagginRegressor(estimator=None, n_estimators=10, *, max_samples=1.0, max_features=1.0, 
                bootstrap=True, bootstrap_features=False, oob_score=False, warm_start=False, 
                n_jobs=None, random_state=None, verbose=0)
```
**Parámetros:**
- **base_estimator** - `object`: Es un modelo (o sea un objeto creado con una función de regresión del tipo `DecisionTreeRegressor`, etc.). Si no se especifica se utilizara un `DecisionTreeRegressor`.
- **n_estimators** - `int`: Número de modelos base en el esemble.


#### Atributos

Atributos de la clase `BagginRegressor`. 

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - **estimator_**
  - El estimador base del que se basa el ensamble.
* - **estimators_**
  - La colección de subestimadores ajustados.
* - **estimators_features_**
  - La colección de estimadores de base ajustados.
* - **estimators_samples_**
  - El subconjunto de muestras para cada estimador base.
* - **feature_names_in_**
  - Nombres de los _features_ vistos durante el ajuste. Definido solo cuando _X_ tiene nombres de _features_ que son todos cadenas.
* - **n_features_in_**
  - Número de _features_ vistos durante el ajuste.
* - **oob_prediction_**
  - Función de decisión calculada con una estimación _out-of-bag_ en el conjunto _training_.
* - **oob_score_**
  - Puntaje del conjunto de datos del _training_ obtenido utilizando una estimación _out-of-bag_. Este atributo existe solo cuando _oob_score_ es `True`.
```

<br/>

#### Métodos

Métodos de la clase `BagginRegressor`.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [fit](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingRegressor.html#sklearn.ensemble.BaggingRegressor.fit)(X,  y,  , ...)
  - Construye un conjunto de estimadores del conjunto _training_ _(X, y)_.
* - [predict](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingRegressor.html#sklearn.ensemble.BaggingRegressor.predict)(X)
  - Predice el objetivo de regresión para _X_.
* - [score](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingRegressor.html#sklearn.ensemble.BaggingRegressor.score)(X,  y,  sample_weight=None)
  - Retorna el coeficiente de determinación de la predicción.
```

<br/>

### GradientBoostingClassifier

[GradientBoostingClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html): Implementa _Gradient Boosting_, un método que construye modelos secuencialmente, donde cada nuevo modelo corrige los errores del anterior. Es muy efectivo para problemas de clasificación.
```python
# Sintaxis de llamada
GradientBoostingClassfier(*, loss='log_loss', learning_rate=0.1, n_estimators=100, subsample=1.0, 
                          criterion='friedman_mse', min_samples_split=2, min_samples_leaf=1, 
                          min_weight_fraction_leaf=0.0, max_depth=3, min_impurity_decrease=0.0, init=None, 
                          random_state=None, max_features=None, verbose=0, max_leaf_nodes=None, 
                          warm_start=False, validation_fraction=0.1, n_iter_no_change=None, tol=0.0001, 
                          ccp_alpha=0.0) 
```
**Parámetros:**
- **loss** - {'deviance', 'exponential'}: Función de pérdida a ser optimizada.
- **learning_rate** - `float`: Determina el grado de contribución de cada aprendiz al resultado final.
- **n_estimators** - `int`: Número de _boosting stages_ a realizar.
- **max_depth** - `int`: Profundidad máxima de los estimadores de clasificación individuales.
- **random_state** - `int` o `RandomState Instance`: Controla la aleatoriedad del estimador.
- **n_iter_no_change** - `int`: Se utiliza para terminar el entrenamiento del modelo cuando nuevos árboles no están mejorando el _validation score_. Este número determina la cantidad de árboles previos que no mejoraron el _score_ y por lo tanto se detendrá el ajuste, para ello _n_estimators_ tuvo que ser un número grande.

#### Uso

La forma básica de usar este clase es la siguiente:

```python
# Importar clase
from sklearn.ensemble import GradientBoostingClassifier

# Inicializar el modelo
model = GradientBoostingClassifier(
    n_estimators,  # Número de árboles (etapas de boosting)
    learning_rat,  # Tasa de aprendizaje
    max_depth=3,        # Profundidad máxima de cada árbol
)

# Ajustar el modelo
model.fit(X, y) 

# Predecir etiquetas para nuevos datos
y_pred = model.predict(X_new)

# Predecir probabilidades (para clasificación binaria o multiclase)
y_proba = model.predict_proba(X_new)  # Devuelve las probabilidades para cada clase

# Importancia de las características
feature_importances = model.feature_importances_  # Muestra la importancia de cada característica

# Puntajes de decisión (valores antes de aplicar la función de pérdida)
decision_scores = model.decision_function(X_new)
```

<br/>


#### Atributos

Atributos de la clase `GradientBoostingClassifier`. 

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - **classes_**
  - Las etiquetas de las clases.
* - **estimators_**
  - La colección de subestimadores ajustados. _n_trees_per_iteration\__ es 1 para la clasificación binaria, de lo contrario _n_classes\__.
* - **feature_importances_**
  - Los _feature importances_ basadas en la impureza.
* - **feature_names_in_**
  - Nombres de los _features_ vistos durante el ajuste. Definido solo cuando _X_ tiene nombres de _features_ que son todos cadenas.
* - **init_**
  - El estimador que proporciona las predicciones iniciales. Establecer a través del argumento _init_.
* - **max_features_**
  - El valor inferido de _max_features_.
* - **n_classes_**
  - El número de clases.
* - **n_estimators_**
  - Se especifica el número de estimadores seleccionados por la parada temprana (si se especifica _n_iter_no_change_). De lo contrario, está configurado en _n_estimators_. 
* - **n_features_in_**
  - Número de _features_ vistos durante el ajuste.
* - **n_trees_per_iteration_**
  - El número de árboles que se construyen en cada iteración. Para clasificadores binarios, esto siempre es 1. 
* - **oob_improvement_**
  - La mejora en la pérdida en las muestras fuera de bolsa en relación con la iteración anterior. 
* - **oob_score_**
  - El último valor de la pérdida en las muestras fuera de bolsa.
* - **oob_scores_**
  - La historia completa de los valores de pérdida en las muestras fuera de bolsa.
* - **train_score_**
  - El puntaje _i-th_ de `train_score_[i]`, es la pérdida del modelo en la iteración _i_ en la muestra _in-bag_. Si `subsample == 1`, esta es la pérdida en los datos del _training_.
```

<br/>

#### Métodos


Métodos de la clase `GradientBoostingClassifier`. 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [apply](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier.apply)(X)
  - Aplica árboles en el conjunto a _X_, retorna índices de la hoja.
* - [decision_function](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier.decision_function)(X)
  - Calcula la función de decisión de _X_.
* - [fit](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier.fit)(X,  y,  sample_weight=None,  monitor=None)
  - Ajusta el modelo de _gradient boosting_.
* - [predict](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier.predict)(X)
  - Predice la clase para _X_.
* - [predict_log_proba](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier.predict_log_proba)(X)
  - Predice las probabilidades de registro de clase para X.. Predict class log-probabilities for X.
* - [predict_proba](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier.predict_proba)(X)
  - Predice las _log-probabilities_ de clase para _X_.
* - [score](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier.score)(X,  y,  sample_weight=None)
  - Retorna la precisión media en los datos y etiquetas del _test_ dados.
* - [staged_decision_function](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier.staged_decision_function)(X)
  - Calcula la función de decisión de _X_ en cada etapa.
* - [staged_predict](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier.staged_predict)(X)
  - Retorna predicciones de clase para _X_ en cada etapa.
* - [staged_predict_proba](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier.staged_predict_proba)(X)
  - Predice las probabilidades de clase para _X_ en cada etapa.
```

<br/>

### GradientBoostingRegressor

[GradientBoostingRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html): Implementa _Gradient Boosting_, un método que construye modelos secuencialmente, donde cada nuevo modelo corrige los errores del anterior.
```python
# Sintaxis de llamada
GradientBoostingClassfier(*, loss='squared_error', learning_rate=0.1, n_estimators=100, subsample=1.0, 
                          criterion='friedman_mse', min_samples_split=2, min_samples_leaf=1, 
                          min_weight_fraction_leaf=0.0, max_depth=3, min_impurity_decrease=0.0, init=None, 
                          random_state=None, max_features=None, alpha=0.9, verbose=0, max_leaf_nodes=None, 
                          warm_start=False, validation_fraction=0.1, n_iter_no_change=None, tol=0.0001, 
                          ccp_alpha=0.0) 
```
**Parámetros:**
- **loss** - {_‘squared_error’, ‘absolute_error’, ‘huber’, ‘quantile’_}: Función de pérdida a ser optimizada.
- **learning_rate** - `float`: Determina el grado de contribución de cada aprendiz al resultado final.
- **n_estimators** - `int`: Número de _boosting stages_ a realizar.
- **max_depth** - `int`: Profundidad máxima de los estimadores de clasificación individuales.
- **random_state** - `int` o `RandomState Instance`: Controla la aleatoriedad del estimador.
- **n_iter_no_change** - `int`: Se utiliza para terminar el entrenamiento del modelo cuando nuevos árboles no están mejorando el _validation score_. Este número determina la cantidad de árboles previos que no mejoraron el _score_ y por lo tanto se detendrá el ajuste, para ello _n_estimators_ tuvo que ser un número grande.

#### Uso

La forma básica de usar este clase es la siguiente:

```python
# Importar clase
from sklearn.ensemble import GradientBoostingRegressor

# Inicializar el modelo
model = GradientBoostingRegressor(
    n_estimators,  # Número de árboles (etapas de boosting)
    learning_rate,  # Tasa de aprendizaje
    max_depth,        # Profundidad máxima de cada árbol
)

# Ajustar el modelo
model.fit(X, y) 

# Predecir valores para nuevos datos
y_pred = model.predict(X_new) 

# Importancia de las características
feature_importances = model.feature_importances_  # Muestra la importancia de cada característica

# Error en cada etapa (pérdida)
train_errors = model.train_score_ 
```

<br/>


#### Atributos

Atributos de la clase `GradientBoostingRegressor`. 

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - **estimators_**
  - La colección de subestimadores ajustados. _n_trees_per_iteration\__ es 1 para la clasificación binaria, de lo contrario _n_classes\__.
* - **feature_importances_**
  - Los _feature importances_ basadas en la impureza.
* - **feature_names_in_**
  - Nombres de los _features_ vistos durante el ajuste. Definido solo cuando _X_ tiene nombres de _features_ que son todos cadenas.
* - **init_**
  - El estimador que proporciona las predicciones iniciales. Establecer a través del argumento _init_.
* - **max_features_**
  - El valor inferido de _max_features_.
* - **n_estimators_**
  - Se especifica el número de estimadores seleccionados por la parada temprana (si se especifica _n_iter_no_change_). De lo contrario, está configurado en _n_estimators_. 
* - **n_trees_per_iteration_**
  - El número de árboles que se construyen en cada iteración. Para clasificadores binarios, esto siempre es 1. 
* - **oob_improvement_**
  - La mejora en la pérdida en las muestras fuera de bolsa en relación con la iteración anterior. 
* - **oob_score_**
  - El último valor de la pérdida en las muestras fuera de bolsa.
* - **oob_scores_**
  - La historia completa de los valores de pérdida en las muestras fuera de bolsa.
* - **train_score_**
  - El puntaje _i-th_ de `train_score_[i]`, es la pérdida del modelo en la iteración _i_ en la muestra _in-bag_. Si `subsample == 1`, esta es la pérdida en los datos del _training_.
```

<br/>

#### Métodos


Métodos de la clase `GradientBoostingRegressor`. 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [apply](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier.apply)(X)
  - Aplica árboles en el conjunto a _X_, retorna índices de la hoja.
* - [fit](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier.fit)(X,  y,  sample_weight=None,  monitor=None)
  - Ajusta el modelo de _gradient boosting_.
* - [predict](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier.predict)(X)
  - Predice la regresión para _X_.
* - [score](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier.score)(X,  y,  sample_weight=None)
  - Retorna los coeficientes de determinación de la predicción.
* - [staged_predict](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier.staged_predict)(X)
  - Retorna la regresión para _X_ en cada etapa.
```

<br/>

### RandomForestClassifier

[RandomForestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html): Combina múltiples árboles de decisión entrenados en subconjuntos aleatorios del dataset y características. Realiza predicciones por votación mayoritaria, lo que reduce el sobreajuste y mejora la precisión. Es similiar a un _Bagging Classifier_ pero utiliza como base estimator un decision tree, además se hace un muestreo de los _features_.
```python
# Sintaxis de llamada
RandomForestClassifier(n_estimators=100, *, criterion='gini', max_depth=None, 
                       min_samples_split=2, min_samples_leaf=1, min_weight_fraction_leaf=0.0, 
                       max_features='sqrt', max_leaf_nodes=None, min_impurity_decrease=0.0, 
                       bootstrap=True, oob_score=False, n_jobs=None, random_state=None, 
                       verbose=0, warm_start=False, class_weight=None, ccp_alpha=0.0, 
                       max_samples=None, monotonic_cst=None). 
```
**Parámetros:**
- **n_estimators** - `int`: Número de árboles en el bosque.
- **criterion** - {'gini', 'entropy'}: Función para medir la impuridad de un nodo.
- **max_depth** - `int`: Profundidad máxima del árbol.
- **min_samples_leaf** - `int` o `float`: Número mínimo de muestras necesarias para dividir un nodo.
- **random_state** - `int` o `RandomState Instance`: Controla la aleatoriedad del estimador. Los _feature_ siempre son permutados aleatoriamente en cada _split_.
- **max_features** - {'auto', 'sqrt', 'log2'}, `int`, `float` o `None`: Número de _features_ a considerar al hacer el _split_.
    - `str`: Algunos de los siguientes valores:
        - _auto_ o _sqrt_: Se determina usando `sqrt(n_features)`. Valor por default.
        - _log2_: Se determina usando `log2(n_features)`.
    - `int`: Tamaño de la muestra de _features_ en cada _split_.
    - `float`: Proporción de _features_ que determina el tamaño de la muestra de _features_ en cada _split_. Si es 1.0 entonces equivaldría a no hacer muestreo en los _features_.
    - `None`: Entonces `max_features=n_features` (no hacer muestreo en los _features_).


#### Uso

La forma básica de usar este clase es la siguiente:

```python
# Importar clase
from sklearn.ensemble import RandomForestClassifier

# Inicializar el modelo
model = RandomForestClassifier(
    n_estimators,  # Número de árboles en el bosque
    max_depth=,       # Profundidad máxima de cada árbol
    max_features='sqrt'  # Número de características a considerar en cada división ('sqrt' es común)
)

# Ajustar el modelo
model.fit(X, y) 

# Predecir etiquetas para nuevos datos
y_pred = model.predict(X_new) 

# Predecir probabilidades (para clasificación binaria o multiclase)
y_proba = model.predict_proba(X_new)

# Importancia de las características
feature_importances = model.feature_importances_  # Muestra la importancia de cada característica en el modelo

# Acceder a los árboles individuales
trees = model.estimators_  # Lista de los árboles de decisión entrenados
```

Patrones útiles:

```python
# Graficar features importances
importances_rf = pd.Series(rf.feature_importances_, index = X.columns)
sorted_importances_rf = importances_rf.sort_values()
sorted_importances_rf.plot(kind='barh')
plt.show()
```

<br/>

#### Atributos

Atributos de la clase `RandomForestClassifier`. 

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - **classes_**
  - Las etiquetas de las clases (problema de salida única) o un `list` de arreglos de etiquetas de clase (problema de salida múltiple).
* - **estimator_**
  - La plantilla estimadora hija utilizada para crear la colección de subestimadores ajustados. 
* - **estimators_**
  - La colección de subestimadores ajustados.
* - **estimators_samples_**
  - El subconjunto de muestras para cada estimador base.
* - **feature_importances_**
  - Los _feature importances_ basadas en la impureza.
* - **feature_names_in_**
  - Nombres de los _features_ vistos durante el ajuste. Definido solo cuando _X_ tiene nombres de _features_ que son todos cadenas.
* - **n_classes_**
  - El número de clases (problema de salida única) o un `list` que contiene el número de clases para cada salida (problema de salida múltiple).
* - **n_features_in_**
  - Número de _features_ vistos durante el ajuste.
* - **n_outputs_**
  - El número de salidas cuando se realiza el ajuste.
* - **oob_decision_function_**
  - Función de decisión calculada con una estimación _out-of-bag_ en el conjunto _training_.
* - **oob_score_**
  - Puntaje del conjunto de datos del _training_ obtenido utilizando una estimación _out-of-bag_. Este atributo existe solo cuando _oob_score_ es `True`.
```

<br/>

#### Métodos

Métodos de la clase `RandomForestClassifier`. 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [apply](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier.apply)(X)
  - Aplica árboles en el conjunto a _X_, retorna índices de la hoja.
* - [decision_path](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier.decision_path)(X)
  - Retorna el camino de decisión en el bosque.
* - [fit](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier.fit)(X,  y,  sample_weight=None)
  - Construye un bosque de árboles a partir del conjunto de entrenamiento _(X, y)_.
* - [predict](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier.predict)(X)
  - Predice las clases para _X_.
* - [predict_log_proba](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier.predict_log_proba)(X)
  - Predice las _log-probabilities_ de clase para _X_.
* - [predict_proba](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier.predict_proba)(X)
  - Predice las probabilidades de clase para _X_.
* - [score](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier.score)(X,  y,  sample_weight=None)
  - Retorna la precisión media en los datos y etiquetas del _test_ dados.
```

<br/>

### RandomForestRegressor

[RandomForestRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html): Similar a `RandomForestClassifier`, pero diseñado para problemas de regresión. Combina las predicciones de múltiples árboles de decisión para obtener una estimación más robusta.
```python
# Sintaxis de llamada
RandomForestRegressor(n_estimators=100, *, criterion='squared_error', max_depth=None, 
                      min_samples_split=2, min_samples_leaf=1, min_weight_fraction_leaf=0.0, 
                      max_features=1.0, max_leaf_nodes=None, min_impurity_decrease=0.0, 
                      bootstrap=True, oob_score=False, n_jobs=None, random_state=None, verbose=0, 
                      warm_start=False, ccp_alpha=0.0, max_samples=None, monotonic_cst=None). 
```
**Parámetros:**
- **n_estimators** - `int`: Número de árboles en el bosque.
- **criterion** - {'squared_error', 'absolute_error', 'poisson'}: Función para medir la impuridad de un nodo.
- **max_depth** - `int` o `None`: Profundidad máxima del árbol. Si se establece como `None` entonces la profundidad de cada árbol será la máxima.
- **min_samples_leaf** - `int` o `float`: Número mínimo de muestras necesarias para dividir un nodo.
- **random_state** - `int` o `RandomState Instance`: Controla la aleatoriedad del estimador. Los _feature_ siempre son permutados aleatoriamente en cada _split_.
- **max_features** - {'auto', 'sqrt', 'log2'}, `int`, `float` o `None`: Número de _features_ a considerar al hacer el _split_.
    - `str`: Algunos de los siguientes valores:
        - _auto_ o _sqrt_: Se determina usando `sqrt(n_features)`. Valor por default.
        - _log2_: Se determina usando `log2(n_features)`.
    - `int`: Tamaño de la muestra de _features_ en cada _split_.
    - `float`: Proporción de _features_ que determina el tamaño de la muestra de _features_ en cada _split_. Si es 1.0 entonces equivaldría a no hacer muestreo en los _features_.
    - `None`: Entonces `max_features = n_features` (no hacer muestreo en los _features_).

#### Atributos

Atributos de la clase `RandomForestRegressor`. 

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - **estimator_**
  - La plantilla estimadora hija utilizada para crear la colección de subestimadores ajustados. 
* - **estimators_**
  - La colección de subestimadores ajustados.
* - **estimators_features_**
  - La colección de estimadores de base ajustados.
* - **estimators_samples_**
  - El subconjunto de muestras para cada estimador base.
* - **feature_names_in_**
  - Nombres de los _features_ vistos durante el ajuste. Definido solo cuando _X_ tiene nombres de _features_ que son todos cadenas.
* - **n_features_in_**
  - Número de _features_ vistos durante el ajuste.
* - **n_features_out_**
  - El número de salidas cuando se realiza el ajuste.
* - **oob_prediction_**
  - Función de decisión calculada con una estimación _out-of-bag_ en el conjunto _training_.
* - **oob_score_**
  - Puntaje del conjunto de datos del _training_ obtenido utilizando una estimación _out-of-bag_. Este atributo existe solo cuando _oob_score_ es `True`.
```

#### Métodos

Métodos de la clase `RandomForestRegressor`. 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [apply](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#sklearn.ensemble.RandomForestRegressor.apply)(X)
  - Aplica árboles en el conjunto a _X_, retorna índices de la hoja.
* - [decision_path](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#sklearn.ensemble.RandomForestRegressor.decision_path)(X)
  - Retorna el camino de decisión en el bosque.
* - [fit](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#sklearn.ensemble.RandomForestRegressor.fit)(X,  y,  sample_weight=None)
  - Construye un bosque de árboles a partir del conjunto de entrenamiento _(X, y)_.
* - [predict](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#sklearn.ensemble.RandomForestRegressor.predict)(X)
  - Predice el objetivo de regresión para _X_.
* - [score](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#sklearn.ensemble.RandomForestRegressor.score)(X,  y,  sample_weight=None)
  - Retorna el coeficiente de determinación de la predicción.
```

<br/>

### VotingClassifier

[VotingClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.VotingClassifier.html): Permite combinar las predicciones de múltiples modelos de clasificación (como SVM, árboles, regresión logística, etc.) mediante votación mayoritaria o ponderada para mejorar el rendimiento.
```python
# Sintaxis de llamada
VotingClassifier(estimators, *, voting='hard', weights=None, n_jobs=None, 
                 flatten_transform=True, verbose=False)
```
**Parámetros:**
- **estimators** - `list` de `2-tuple`: Cada `tuple` consta de un nombre `str` y un estimator (modelo) `estimator`.

#### Uso

La forma básica de usar este clase es la siguiente:

```python
# Importar clase
from sklearn.ensemble import VotingClassifier

# Crear lista de estimators
classifiers = [('Estimator Name 1', estimator1), ('Estimator Name 2', estimator2), ...]

model = VotingClassifier(
    classifiers,
    voting='soft'  # 'soft' para usar probabilidades, 'hard' para usar predicciones directas
)

# Ajustar el modelo
model.fit(X, y) 

# Predecir etiquetas para nuevos datos
y_pred = model.predict(X_new)

# Predecir probabilidades (si voting='soft')
y_proba = model.predict_proba(X_new)  # Devuelve las probabilidades para cada clase
```

<br/>

#### Atributos

Atributos de la clase `VotingClassifier`. 

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - **classes_**
  - Las etiquetas de las clases.
* - **estimators_**
  - La colección de subestimadores ajustados como se define en _estimators_ que no son _"drop"_.
* - **feature_names_in_**
  - Nombres de los _features_ vistos durante el ajuste. Definido solo cuando _X_ tiene nombres de _features_ que son todos cadenas.
* - **le_**
  - Transformador utilizado para codificar las etiquetas durante el ajuste y descodificación durante la predicción.
* - **n_features_in_**
  - Número de _features_ vistas durante el ajuste.
* - **named_estimators_**
  - Atributo para acceder a cualquier subestimador ajustado por su nombre.
```

<br/>

#### Métodos

Métodos de la clase `VotingClassifier`. 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [fit](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.VotingClassifier.html#sklearn.ensemble.VotingClassifier.fit)(X,  y,  , ...)
  - Ajusta los estimadores.
* - [fit_transform](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.VotingClassifier.html#sklearn.ensemble.VotingClassifier.fit_transform)(X,  y=None,  **fit_params)
  - Etiquetas o probabilidades de clase de devolución para cada estimador.
* - [predict](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.VotingClassifier.html#sklearn.ensemble.VotingClassifier.predict)(X)
  - Predice las etiquetas de clase para _X_.
* - [predict_proba](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.VotingClassifier.html#sklearn.ensemble.VotingClassifier.predict_proba)(X)
  - Predice las probabilidades de clase para _X_.
* - [score](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.VotingClassifier.html#sklearn.ensemble.VotingClassifier.score)(X,  y,  sample_weight=None)
  - Retorna la precisión media en los datos y etiquetas de _test_ dados.
* - [transform](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.VotingClassifier.html#sklearn.ensemble.VotingClassifier.transform)(X)
  - Etiquetas o probabilidades de clase de devolución para _X_ para cada estimador.
```

### Métodos _get_ y _set_

A continuación se enlistan los métodos _get_ y _set_ que son comunes en muchas clases de este módulo.

| Método               | Descripción                                                                                                           |
|----------------------|-----------------------------------------------------------------------------------------------------------------------|
| **set_params**       | Permite establecer los parámetros del modelo. Recibe un diccionario de parámetros y sus valores para configurar el modelo. |
| **get_params**       | Devuelve un diccionario con los parámetros actuales del modelo. Útil para inspeccionar la configuración del modelo.   |
| **set_score_request**| (Opcional) Solicita que se almacenen ciertos datos durante el proceso de evaluación del modelo, como puntuaciones intermedias. |
| **get_feature_names_out** | Devuelve los nombres de las características generadas por el modelo, útil en transformadores o modelos que modifican características. |
