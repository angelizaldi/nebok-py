# Linear model

Implementa modelos lineales, como regresión lineal, regresión logística y Ridge/Lasso, útiles para problemas de regresión y clasificación. Para importar este módulo o una clase o función específica usar:

```python
# Importar módulo
from sklearn import linear_model

# Importar clase específica
from sklearn.linear_model import ClassName

# Importar función específica
from sklearn.linear_model import func_name
```
- _ClassName_ o _func_name_ es el nombre de la clase o función respectivamente.

:::{note}
Para más información de este módulo visitar la [documentación](https://scikit-learn.org/stable/api/sklearn.linear_model.html) de `sklearn`.
:::

<br/>

## Clases

Clases implementadas en el módulo _linear_model`. A continuación se presenta un pequeño resumen de cada sección.
- **Clasificadores lineales**: Esta sección se enfoca en modelos lineales utilizados para clasificación, como la regresión logística y el clasificador lineal SVM (_Support Vector Machine_). Estos modelos son ideales para problemas donde la relación entre las _features_ y las etiquetas es lineal o puede aproximarse linealmente.
- **GLM para regresión**: Esta sección cubre modelos lineales generalizados (GLM), que extienden la regresión lineal para manejar distribuciones no normales de la variable objetivo. Son útiles para problemas donde la relación entre las _features_ y la variable objetivo no es estrictamente lineal.
- **Regresores bayesianos**: Contiene modelos de regresión basados en enfoques bayesianos, como _Bayesian Ridge_ y ARD (_Automatic Relevance Determination_). Estos modelos incorporan prioridades probabilísticas sobre los parámetros, lo que permite estimaciones más robustas en presencia de incertidumbre.
- **Regresores con selección de variable**: Esta sección incluye modelos de regresión que incorporan selección de variables para mejorar la generalización y reducir el sobreajuste. Ejemplos son _Lasso_ (regularización L1) y _Elastic Net_, que combinan regularizaciones L1 y L2.
- **Regresores lineales**: Aquí se encuentran los modelos de regresión lineal clásicos, como la regresión lineal ordinaria (OLS) y _Ridge_ (regularización L2). Estos modelos predicen una variable continua asumiendo una relación lineal entre las _features_ y la variable objetivo.
- **Regresores _multi-task_**: Esta sección trata sobre modelos de regresión lineal que pueden manejar múltiples tareas simultáneamente (_multi-task learning_), que son útiles cuando varias variables objetivo están relacionadas.
- **Regresores robustos a _outliers_**: Aquí se encuentran modelos de regresión diseñados para ser robustos frente a valores atípicos (_outliers_). Ejemplos incluyen RANSAC (_RANdom SAmple Consensus_) y Theil-Sen, que son menos sensibles a datos corruptos o anómalos.

<br/>

### Clasificadores lineales

Esta sección se enfoca en modelos lineales utilizados para clasificación, como la regresión logística y el clasificador lineal SVM (_Support Vector Machine_). Estos modelos son ideales para problemas donde la relación entre las _features_ y las etiquetas es lineal o puede aproximarse linealmente.

```{list-table}
:header-rows: 1

* - Clase
  - Descripción
* - [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html)(penalty='l2', ...)
  - Clasificador de regresión logística (también conocido como _Logit, Maxent_).
* - [LogisticRegressionCV](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html)(...)
  - Clasificador de regresión logística CV (también conocido como _Logit, Maxent_).
* - [PassiveAggressiveClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.PassiveAggressiveClassifier.html)(...)
  - Clasificador pasivo agresivo.
* - [Perceptron](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Perceptron.html)(...)
  - Clasificador de perceptrón lineal.
* - [RidgeClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeClassifier.html)(alpha=1.0, ...)
  - Clasificador usando regresión _Ridge_.
* - [RidgeClassifierCV](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeClassifierCV.html)(alphas=(0.1, 1.0, 10.0), ...)
  - Clasificador de _Ridge_ con validación cruzada incorporada.
* - [SGDClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html)(loss='hinge', ...)
  - Clasificadores lineales (SVM, regresión logística, etc.) con entrenamiento SGD.
* - [SGDOneClassSVM](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDOneClassSVM.html)(nu=0.5, ...)
  - Resuelve SVM lineal de una clase usando descenso de gradiente estocástico.
```

<br/>

#### LogisticRegression

[LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html): Implementa la regresión logística, un modelo lineal utilizado para problemas de clasificación binaria o multiclase. Ajusta los coeficientes de las _features_ para predecir probabilidades utilizando una función logística.
```python
# Sintaxis de llamada
LogisticRegression(penalty='l2', *, dual=False, tol=0.0001, C=1.0, fit_intercept=True, 
                   intercept_scaling=1, class_weight=None, random_state=None, solver='lbfgs', 
                   max_iter=100, multi_class='deprecated', verbose=0, warm_start=False, 
                   n_jobs=None, l1_ratio=None)
```
**Parámetros:**
- **penalty** - {'l1', 'l2', 'elasticnet', 'none'}: Especifica la normal de penalización:
    - _l1_: Agrega una penalización L1.
    - _l2_: Agrega una penalización L2.
    - _elasticnet_: Se agregan penalizaciones L1 y L2.
    - `None`: No se agrega ninguna penalización. Equivale a establecer _C_ como infinito con `penalty='l2'`.
- **C** - `float`: Indica la inversa de la fuerza de regularización. Valores más pequeños significan regularización más fuerte y viceversa.
- **solver** - {'newton-cg', 'lbfgs', 'liblinear', 'sag', 'saga'}: Algoritmo a usar en el problema de optimización.

##### Uso

La forma básica de usar este clase es la siguiente:

```python
# Importar clase
from sklearn.linear_model import LogisticRegression

# Inicializar modelo
logreg = LogisticRegression()

# Ajustar modelo
logreg.fit(X_train, y_train)

# Predecir en nuevas muestras
prediction = logreg.predict(X_test)

# Evaluar el modelo
score = logreg.score(X_test, y_test)
```

##### Atributos

Atributos de la clase `LogisticRegression`.

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - **classes_**
  - Un `list` de etiquetas de clase conocidas por el clasificador.
* - **coef_**
  - Coeficiente de los _features_ en la función de decisión.
* - **feature_names_in_**
  - Nombres de los _features_ observadas durante el ajuste. Definido sólo cuando _X_ tiene nombres de rasgos que son todos cadenas. 
* - **intercept_**
  - Intercepción (también conocido como sesgo) añadido a la función de decisión.
* - **n_features_in_**
  - Número de _features_ vistas durante el ajuste. 
* - **n_iter_**
  - Número real de iteraciones para todas las clases.
```

##### Métodos

Métodos de la clase `LogisticRegression`.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [decision_function](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression.decision_function)(X)
  - Predice las puntuaciones de confianza de las muestras.
* - [densify](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression.densify)()
  - Convierte la matriz de coeficientes al formato de matriz densa.
* - [fit](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression.fit)(X,  y,  sample_weight=None)
  - Ajusta el modelo según los datos de entrenamiento dados.
* - [predict](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression.predict)(X)
  - Predice etiquetas de clase para muestras en _X_.
* - [predict_log_proba](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression.predict_log_proba)(X)
  - Predice el logaritmo de las estimaciones de probabilidad.
* - [predict_proba](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression.predict_proba)(X)
  - Estimaciones de probabilidad.
* - [score](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression.score)(X,  y,  sample_weight=None)
  - Retorna la precisión media en los datos de prueba y etiquetas dados.
* - [sparsify](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression.sparsify)()
  - Convierte la matriz de coeficientes a formato disperso.
```

<br/>

### GLM para regresión

Esta sección cubre modelos lineales generalizados (GLM), que extienden la regresión lineal para manejar distribuciones no normales de la variable objetivo. Son útiles para problemas donde la relación entre los _features_ y la variable objetivo no es estrictamente lineal.

```{list-table}
:header-rows: 1

* - Clase
  - Descripción
* - [GammaRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.GammaRegressor.html)(...)
  - Modelo lineal generalizado con una distribución gamma.
* - [PoissonRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.PoissonRegressor.html)(...)
  - Modelo lineal generalizado con una distribución de Poisson.
* - [TweedieRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.TweedieRegressor.html)(...)
  - Modelo lineal generalizado con una distribución de Tweedie.
```

<br/>

### Regresores bayesianos

Contiene modelos de regresión basados en enfoques bayesianos, como _Bayesian Ridge_ y ARD (_Automatic Relevance Determination_). Estos modelos incorporan prioridades probabilísticas sobre los parámetros, lo que permite estimaciones más robustas en presencia de incertidumbre.

```{list-table}
:header-rows: 1

* - Clase
  - Descripción
* - [ARDRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ARDRegression.html)(...)
  - Regresión bayesiana ARD.
* - [BayesianRidge](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.BayesianRidge.html)(...)
  - Regresión de _Ridge_ bayesiana.
```

<br/>

### Regresiones con selección de variables

Esta sección incluye modelos de regresión que incorporan selección de variables para mejorar la generalización y reducir el sobreajuste. Ejemplos son _Lasso_ (regularización L1) y _Elastic Net_, que combinan regularizaciones L1 y L2.

```{list-table}
:header-rows: 1

* - Clase
  - Descripción
* - [ElasticNet](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html)(alpha=1.0, ...)
  - Regresión lineal con antecedentes L1 y L2 combinados como regularizador.
* - [ElasticNetCV](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNetCV.html)(...)
  - Modelo de red elástica con ajuste iterativo a lo largo de una ruta de regularización.
* - [Lars](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lars.html)(...)
  - Modelo de regresión de ángulo mínimo (A.K.A).
* - [LarsCV](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LarsCV.html)(...)
  - Modelo de regresión de ángulo de mínimo validado cruzado.
* - [Lasso](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html)(alpha=1.0, ...)
  - Modelo lineal entrenado con L1 Prior como regularizador (también conocido como _Lasso_).
* - [LassoCV](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoCV.html)(...)
  - Modelo lineal de _Lasso_ con ajuste iterativo a lo largo de una ruta de regularización.
* - [LassoLars](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoLars.html)(alpha=1.0, ...)
  - Modelo de _Lasso_ con la regresión de ángulo menor A.K.A.
* - [LassoLarsCV](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoLarsCV.html)(...)
  - Lasso validados cruzados, utilizando el algoritmo Lars.
* - [LassoLarsIC](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoLarsIC.html)(criterion='aic', ...)
  - Modelo de _Lasso_ ajustado con LARS usando BIC o AIC para la selección del modelo.
* - [OrthogonalMatchingPursuit](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.OrthogonalMatchingPursuit.html)(...)
  - Modelo de búsqueda de correspondencia ortogonal (OMP).
* - [OrthogonalMatchingPursuitCV](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.OrthogonalMatchingPursuitCV.html)(...)
  - Modelo de persecución ortogonal de coincidencia ortogonal (OMP).
```

<br/>

#### Lasso

[Lasso](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html): Es una variante de la regresión lineal que incluye regularización L1 (norma L1). Esta regularización tiende a producir coeficientes exactamente cero, lo que ayuda en la selección de _features_ y previene el sobreajuste.
```python
# Sintaxis de llamada
Lasso(alpha=1.0, *, fit_intercept=True, precompute=False, copy_X=True, max_iter=1000, 
      tol=0.0001, warm_start=False, positive=False, random_state=None, selection='cyclic')
```
**Parámetros:**
- **alpha** - `float` o `ndarray`: Fuerza de la regularización, debe ser mayor que cero.
    - Si es cero es una regresión lineal estándar.
    - Si se define este valor por debajo del default (1.0) es muy probable que se tenga que incrementar _max_iter_.
- **fit_intercept** - `bool`: Para indicar si se debe calcular la intercepción para este modelo. Si es `False`, se espera que los datos estén "centrados al origen".

##### Uso

La forma básica de usar este clase es la siguiente:

```python
# Importar clase
from sklearn.linear_model import Lasso

# Inicializar modelo
lasso = Lasso(alpha)

# Ajustar modelo
lasso.fit(X_train, y_train)

# Predecir en nuevas muestras
prediction = lasso.predict(X_test)

# Evaluar el modelo
score = lasso.score(X_test, y_test)
```

##### Atributos

Atributos de la clase `Lasso`.

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - **coef_**
  - Vector de parámetros (_w_ en la fórmula de la función de costes).
* - **dual_gap_**
  - Dado parámetro _alpha_, los huecos duales al final de la optimización, mismo _shape_ que cada observación de _y_.
* - **feature_names_in_**
  - Nombres de los _features_ observadas durante el ajuste. Definido sólo cuando _X_ tiene nombres de rasgos que son todos cadenas. 
* - **intercept_**
  - Término independiente en la función de decisión.
* - **n_features_in_**
  - Número de _features_ vistas durante el ajuste. 
* - **n_iter_**
  - Número de iteraciones ejecutadas por el solucionador de descenso de coordenadas para alcanzar la tolerancia especificada.
* - **sparse_coef_**
  - Representación dispersa del _coef\__ ajustado.
```

##### Métodos

Métodos de la clase `Lasso`.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [fit](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html#sklearn.linear_model.Lasso.fit)(X,  y,  sample_weight=None,  check_input=True)
  - Ajusta del modelo con descenso de coordenadas.
* - [predict](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html#sklearn.linear_model.Lasso.predict)(X)
  - Predice utilizando el modelo lineal.
* - [score](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html#sklearn.linear_model.Lasso.score)(X,  y,  sample_weight=None)
  - Retorna el coeficiente de determinación de la predicción.
* - [static path](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html#sklearn.linear_model.Lasso.path)(X,  y, ...)
  - Calcula la trayectoria de la red elástica con descenso por coordenadas.
```

<br/>

### Regresores lineales

Aquí se encuentran los modelos de regresión lineal clásicos, como la regresión lineal ordinaria (OLS). Estos modelos predicen una variable continua asumiendo una relación lineal entre los _features_ y la variable objetivo.

```{list-table}
:header-rows: 1

* - Clase
  - Descripción
* - [LinearRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html)(...)
  - Regresión lineal de mínimos cuadrados ordinarios.
* - [Ridge](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html)(alpha=1.0, ...)
  - Mínimos cuadrados lineales con regularización L2.
* - [RidgeCV](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeCV.html)(alphas=(0.1, 1.0, 10.0), ...)
  - Regresión de _Ridge_ con validación cruzada incorporada.
* - [SGDRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDRegressor.html)(loss='squared_error', ...)
  - Modelo lineal instalado minimizando una pérdida empírica regularizada con SGD.
```

<br/>

#### LinearRegression

[LinearRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html): Implementa la regresión lineal ordinaria, un modelo que ajusta una línea (o hiperplano) a los datos para predecir valores continuos. Minimiza la suma de los errores al cuadrado entre las predicciones y los valores reales. Puede ajustar líneas, planos e hiperplanos.
```python
# Sintaxis de llamada
LinearRegression(*, fit_intercept=True, copy_X=True, n_jobs=None, positive=False)
```
**Parámetros:**
- **fit_intercept** - `bool`: Para indicar si se debe calcular la intercepción para este modelo. Si es `False`, se espera que los datos estén "centrados al origen".

##### Uso

La forma básica de usar este clase es la siguiente:

```python
# Importar clase
from sklearn.linear_model import LinearRegression

# Inicializar modelo
reg = LinearRegression()

# Ajustar modelo
reg.fit(X_train, y_train)

# Predecir en nuevas muestras
prediction = knn.predict(X_test)

# Evaluar el modelo
score = knn.score(X_test, y_test)
```
- _X_test_ debe ser un `2D array-like`, con el mismo número de columnas que _X_train_. En lugar de ser el _test_ set simplemente podrían ser muestras nuevas.

##### Atributos

Atributos de la clase `LinearRegression`.

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - **coef_**
  - Coeficientes estimados para el problema de regresión lineal. Si se pasan multiples _targets_ durante el ajuste (_y_ es 2D), se retorna una matriz 2D de forma 
  _(n_targets, n_features)_, mientras que si sólo se pasa un objetivo, se trata de una matriz 1D de longitud _n_features_.
* - **feature_names_in_**
  - Nombres de los _features_ observadas durante el ajuste. Definido sólo cuando _X_ tiene nombres de rasgos que son todos cadenas.
* - **intercept_**
  - Término independiente en el modelo lineal. Se establece en _0.0_ si `fit_intercept= False`.
* - **n_features_in_**
  - Número de _features_ vistas durante el ajuste.
* - **rank_**
  - Rango de la matriz _X_. Sólo disponible cuando _X_ es denso.
* - **singular_**
  - Valores singulares de _X_. Sólo disponible cuando _X_ es denso.
```

##### Métodos

Métodos de la clase `LinearRegression`.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [fit](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression.fit)(X,  y,  sample_weight=None)
  - Ajusta del modelo lineal.
* - [predict](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression.predict)(X)
  - Predice utilizando el modelo lineal.
* - [score](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression.score)(X,  y,  sample_weight=None)
  - Retorna el coeficiente de determinación de la predicción.
```

<br/>

#### Ridge

[Ridge](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html): Es una variante de la regresión lineal que incluye regularización L2 (norma L2). Esta regularización reduce la magnitud de los coeficientes sin eliminarlos por completo, lo que ayuda a manejar la multicolinealidad y el sobreajuste.
```python
# Sintaxis de llamada
Ridge(alpha=1.0, *, fit_intercept=True, copy_X=True, max_iter=None, tol=0.0001, 
      solver='auto', positive=False, random_state=None)
```
**Parámetros:**
- **alpha** - `float` o `ndarray`: Fuerza de la regularización, debe ser mayor que cero.
    - Si fuera cero sería equivalente a una regresión lineal simple.
    - Entre más bajo menor será la regularización y podría producir _ovefitting_.
    - Entre más alto mayor será la regularización y podría producir _underfitting_.
- **fit_intercept** - `bool`: Para indicar si se debe calcular la intercepción para este modelo. Si es `False`, se espera que los datos estén "centrados al origen".

##### Uso

La forma básica de usar este clase es la siguiente:

```python
# Importar clase
from sklearn.linear_model import Ridge

# Inicializar modelo
ridge = Ridge(alpha)

# Ajustar modelo
ridge.fit(X_train, y_train)

# Predecir en nuevas muestras
prediction = ridge.predict(X_test)

# Evaluar el modelo
score = ridge.score(X_test, y_test)
```
- _X_test_ debe ser un `2D array-like`, con el mismo número de columnas que _X_train_. En lugar de ser el _test_ set simplemente podrían ser muestras nuevas.

##### Atributos

Atributos de la clase `Ridge`.

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - **coef_**
  - Vector(es) de peso.
* - **feature_names_in_**
  - Nombres de los _features_ observadas durante el ajuste. Definido sólo cuando _X_ tiene nombres de rasgos que son todos cadenas. 
* - **intercept_**
  - Término independiente en la función de decisión. Se establece en _0.0_ si `fit_intercept= False`.
* - **n_features_in_**
  - Número de _features_ vistas durante el ajuste. 
* - **n_iter_**
  - Número real de iteraciones para cada objetivo. 
* - **solver_**
  - El solucionador utilizado en el momento del ajuste por las rutinas de cálculo.
```

##### Métodos

Métodos de la clase `Ridge`.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [fit](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html#sklearn.linear_model.Ridge.fit)(X,  y,  sample_weight=None)
  - Ajusta del modelo de regresión de _Ridge_.
* - [predict](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html#sklearn.linear_model.Ridge.predict)(X)
  - Predice utilizando el modelo lineal.
* - [score](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html#sklearn.linear_model.Ridge.score)(X,  y,  sample_weight=None)
  - Retorna el coeficiente de determinación de la predicción.
```

<br/>

#### RidgeCV

[RidgeCV](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeCV.html): Similar a `Ridge`, pero incluye validación cruzada integrada para seleccionar automáticamente el mejor valor del parámetro de regularización (_alpha_). Es útil para optimizar el modelo sin necesidad de ajustar manualmente este parámetro.
```python
# Sintaxis de llamada
RidgeCV(alphas=(0.1, 1.0, 10.0), *, fit_intercept=True, scoring=None, cv=None, gcv_mode=None, 
        store_cv_results=None, alpha_per_target=False, store_cv_values='deprecated')
```
**Parámetros:**
- **alphas** - `ndarray (nalphas,)`: Array de alphas a probar. Entre más alto el alfa, mayor será la regularización.
- **fit_intercept** - `bool`: Para indicar si se debe calcular la intercepción para este modelo. Si es `False`, se espera que los datos estén "centrados al origen".
- **cv** - `int`, `cross-validation generator` o `iterator`: Determina la estrategia de división.
    - `None`: Utiliza el valor por default de 5.
    - `int`: Especifica el número de _folds_ en (Stratified) `Kfold()`.
    - Hay clases que generan estrategias de división como `LeaveOneOut()`, `StratifiedKFold()`, etc. ver {doc}`../evaluation/model_selection`.

##### Atributos

Atributos de la clase `RidgeCV`.

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - **alpha_**
  - Parámetro de regularización estimado o, si `alpha_per_target=True`, el parámetro de regularización estimado para cada objetivo.
* - **best_score_**
  - Puntuación del estimador base con mejor alfa, o, si `alpha_per_target=True`, una puntuación para cada objetivo.
* - **coef_**
  - Vector(es) de peso.
* - **cv_results_**
  - Valores de validación cruzada para cada alfa (sólo disponible si `store_cv_results=True` y `cv=None`). Después de llamar a `.fit()`, este atributo contendrá los errores medios al cuadrado si la puntuación es `None` en caso contrario contendrá valores de predicción estandarizados por punto. 
* - **feature_names_in_**
  - Nombres de los _features_ observadas durante el ajuste. Definido sólo cuando _X_ tiene nombres de rasgos que son todos cadenas. 
* - **intercept_**
  - Término independiente en la función de decisión. Se establece en _0.0_ si `fit_intercept= False`.
* - **n_features_in_**
  - Número de _features_ vistas durante el ajuste.
```

##### Métodos

Métodos de la clase `RidgeCV`.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [fit](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeCV.html#sklearn.linear_model.RidgeCV.fit)(X,  y,  sample_weight=None,  **params)
  - Ajusta del modelo de regresión _Ridge_ con cv.
* - [predict](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeCV.html#sklearn.linear_model.RidgeCV.predict)(X)
  - Predice utilizando el modelo lineal.
* - [score](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeCV.html#sklearn.linear_model.RidgeCV.score)(X,  y,  sample_weight=None)
  - Retorna el coeficiente de determinación de la predicción.
```

<br/>

### Regresores _multi-task_

Esta sección trata sobre modelos de regresión lineal que pueden manejar múltiples tareas simultáneamente (_multi-task learning_), que son útiles cuando varias variables objetivo están relacionadas.

```{list-table}
:header-rows: 1

* - Clase
  - Descripción
* - [MultiTaskElasticNet](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskElasticNet.html)(alpha=1.0, ...)
  - Modelo ElasticNet de múltiples tareas entrenado con la norma mixta L1/L2 como regularizador.
* - [MultiTaskElasticNetCV](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskElasticNetCV.html)(...)
  - Modelo ElasticNet de múltiples L1/L2 con validación cruzada incorporada.
* - [MultiTaskLasso](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskLasso.html)(alpha=1.0, ...)
  - Modelo _Lasso_ de múltiples tareas entrenado con norma mixta L1/L2 como regularizador.
* - [MultiTaskLassoCV](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskLassoCV.html)(...)
  - Modelo _Lasso_ de múltiples tareas L1/L2 con validación cruzada incorporada.
```

<br/>

### Regresores robustos a _outliers_

Aquí se encuentran modelos de regresión diseñados para ser robustos frente a valores atípicos (_outliers_). Ejemplos incluyen RANSAC (_RANdom SAmple Consensus_) y Theil-Sen, que son menos sensibles a datos corruptos o anómalos.

```{list-table}
:header-rows: 1

* - Clase
  - Descripción
* - [HuberRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.HuberRegressor.html)(...)
  - Modelo de regresión lineal regularizado de L2 que es robusto para los valores atípicos.
* - [QuantileRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.QuantileRegressor.html)(...)
  - Modelo de regresión lineal que predice cuantiles condicionales.
* - [RANSACRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RANSACRegressor.html)(estimator=None, ...)
  - Algoritmo RANSAC (RANdom SAmple Consensus).
* - [TheilSenRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.TheilSenRegressor.html)(...)
  - Estimador de Theil-Sen: modelo robusto de regresión multivariante.
```

<br/>

## Funciones

Funciones implementadas en el módulo `linear_model`. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [PassiveAggressiveRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.PassiveAggressiveRegressor.html)(...)
  - Regresor pasivo agresivo.
* - [enet_path](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.enet_path.html)(X, y, ...)
  - Calcula la ruta neta elástica con descenso de coordenadas.
* - [lars_path](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.lars_path.html)(X, y, Xy=None, ...)
  - Calcula la regresión de ángulo mínimo o la ruta _Lasso_ utilizando el algoritmo LARS.
* - [lars_path_gram](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.lars_path_gram.html)(Xy, Gram, ...)
  - `lars_path()` en el modo de estadísticas suficientes.
* - [lasso_path](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.lasso_path.html)(X, y, ...)
  - Calcula la ruta _Lasso_ con descenso de coordenadas.
* - [orthogonal_mp](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.orthogonal_mp.html)(X, y, ...)
  - _Orthogonal Matching Pursuit_ (OMP).
* - [orthogonal_mp_gram](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.orthogonal_mp_gram.html)(Gram, Xy, ...)
  - _Gram Orthogonal Matching Pursuit_ (OMP).
* - [ridge_regression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ridge_regression.html)(X, y, alpha, ...)
  - Resuelve la ecuación Ridge por el método de ecuaciones normales.
```

<br/>
