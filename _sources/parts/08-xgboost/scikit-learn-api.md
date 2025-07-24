# Scikit-Learn API

Es la _API_ que tiene parámetros definidos por _default_ dependiendo de la función que se use y se puede trabajar con estructuras de datos como `DataFrame`, `ndarray` y `sparse`. Tiene una _API_ similar a la _sklearn_.

:::{caution}
Todas las funciones de esta _API_ utilizan como _booster_ (_base learner_) árboles de decisión. Para usar modelos lineales usar {doc}`./learning-api`.
:::

:::{note}
Para más información visitar la [documentación](https://xgboost.readthedocs.io/en/stable/python/python_api.html#module-xgboost.sklearn) de _XGBoost_.
:::

Resumen de las clases presentadas en esta sección:

| Clase                          | Descripción                                                                                   |
|--------------------------------|-----------------------------------------------------------------------------------------------|
| [XGBClassifier](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBClassifier)               | Implementa un modelo de clasificación basado en _Gradient Boosting_. Útil para problemas de clasificación binaria o multiclase. |
| [XGBRFClassifier](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBRFClassifier)             | Implementa un modelo de clasificación basado en _Random Forest_ utilizando _XGBoost_. Adecuado para problemas de clasificación. |
| [XGBRFRegressor](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBRFRegressor)              | Implementa un modelo de regresión basado en _Random Forest_ utilizando _XGBoost_. Combina múltiples árboles para mejorar la precisión. |
| [XGBRanker](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBRanker)                   | Diseñado para problemas de _ranking_. Aprende a ordenar elementos basándose en _features_ y grupos de datos. |
| [XGBRegressor](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBRegressor)                | Implementa un modelo de regresión basado en _Gradient Boosting_. Ideal para problemas de predicción de valores continuos. |

<br/>

## XGBClassifier

Implementa un modelo de clasificación basado en _Gradient Boosting_. Útil para problemas de clasificación binaria o multiclase.

```{list-table}
:header-rows: 1

* - Constructor
  - Descripción
* - [xgboost.XGBClassifier](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBClassifier)(...)
  - Implementación de la _API Scikit-Learn_ para la clasificación en _XGBoost_.
```

:::{caution}
A continuación no se enlistan todos los parámetros de la clase, para más información consultar el link.
:::

```python
# Sintaxis de llamada
xgb.XGBClassifier(*, objective='binary:logistic', **kwargs)
```
- **Parámetros:**
    - **n_estimators** - `int`: Número de boosting rounds.
    - **learning_rate** - `int`: Tasa de aprendizaje del _boosting_ (eta de xgb)
    - **max_depth** - `int`: Profundidad máxima de árbol para los estudiantes base.
    - **subsample** - `int`: Relación de submuestras de la instancia de entrenamiento.
    - **colsample_bytree** - `int`: Relación de submuestras de columnas al construir cada árbol.
    - **eval_metric** - `int`: Métrica utilizada para monitorizar el resultado del entrenamiento y la detención anticipada.
    - **objective** - `str`, `tuple`, `Callable`: Especifica la tarea de aprendizaje y el aprendizaje objetivo o una función objetivo personalizada a usar. Ver {ref}`parameters-objective`, pero lo más común para clasificación binaria es `'binary:logistic'` y para multiclases puede ser `'multi:softprob'` para probabilidades y `'multi:softmax'` para clases 
    - **random_state** - `int`: Semilla del generador de número aleatorios.
- **Retorna:**
    - `XGBClassifier`.

### Uso

La forma básica de usar este clase es la siguiente:

```python
# Importar clase
from xgboost import XGBClassifier

# Inicializar el modelo
model = XGBClassifier(
    n_estimators=100,      # Número de árboles (boosting rounds)
    learning_rate=0.1,     # Tasa de aprendizaje (eta)
    max_depth=3,           # Profundidad máxima del árbol
    subsample=0.8,         # Fracción de muestras usadas por árbol
    colsample_bytree=0.8,  # Fracción de características usadas por árbol
    objective='binary:logistic',  # Función de pérdida (para binario)
    eval_metric='logloss', # Métrica de evaluación
    random_state=42,       # Semilla para reproducibilidad
    early_stopping_rounds=10,  # Detención temprana si no mejora
    use_label_encoder=False  # Evita warning en versiones recientes
)

# Ajustar el modelo (con conjunto de validación para early stopping)
model.fit(
    X, y,
    eval_set=[(X_val, y_val)],  # Datos de validación (opcional)
    verbose=True  # Muestra progreso del entrenamiento
)

# Predecir etiquetas para nuevos datos
y_pred = model.predict(X_new)

# Predecir probabilidades (para clasificación)
y_proba = model.predict_proba(X_new)  # Devuelve matriz [prob_clase_0, prob_clase_1]

# --- Opcionales ---
# Importancia de características (ganancia, peso, cobertura)
feature_importances = model.feature_importances_
print("Importancia de características:", feature_importances)

# Obtener los mejores scores de evaluación (si se usó eval_set)
best_score = model.best_score
print("Mejor métrica de validación:", best_score)

# Árboles individuales (para inspección)
trees = model.get_booster().get_dump()
print(f"Número total de árboles: {len(trees)}")

# Guardar modelo (formato nativo de XGBoost)
model.save_model('modelo_xgboost.json')  # También .bin, .ubj

# Cargar modelo previamente guardado
model.load_model('modelo_xgboost.json')
```

<br/>

### Atributos

Atributos de la clase `XGBClassifier`. 

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - **best_iteration**
  - La mejor iteración obtenida por _early stopping_. Es _0-based_, por ejemplo, si la mejor iteración es la primera ronda, entonces la _best_iteration_ es 0.
* - **best_score**
  - La mejor puntuación obtenida por _early stopping_.
* - **coef_**
  - Propiedad coeficientes.
* - **feature_importances_**
  - Propiedad de importancia de _features_, el retorno depende del parámetro _importancia_type_.
* - **feature_names_in_**
  - Nombres de los _features_ vistos durante el ajuste.
* - **intercept_**
  - Propiedad de intercepción (sesgo).
* - **n_features_in_**
  - Número de _features_ vistos durante el ajuste.
```

<br/>

### Métodos

Métodos de la clase `XGBClassifier`. 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [apply](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBClassifier.apply)(X,  iteration_range=None)
  - Retorna la hoja predicha cada árbol para cada muestra. Si el modelo está entrenado con _early stopping_, entonces la _best_iteration_ se usa automáticamente.
* - [evals_result](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBClassifier.evals_result)()
  - Retorna los resultados de la evaluación.
* - [fit](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBClassifier.fit)(X,  y,  , ...)
  - Ajusta el _gradient boosting classifier_.
* - [load_model](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBClassifier.load_model)(fname)
  - Carga el modelo desde un archivo o un _bytearray_.
* - [predict](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBClassifier.predict)(X,  output_margin=False,  validate_features=True,  ...)
  - Predice con _X_. Si el modelo está entrenado con _early stopping_, entonces la _best_iteration_ se usa automáticamente. El estimador usa _inplace_predict_ de forma predeterminada.
* - [predict_proba](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBClassifier.predict_proba)(X,  validate_features=True, ...)
  - Predice la probabilidad de que cada muestra de _X_ sea de una clase dada. Si el modelo está entrenado con _early stopping_, entonces la _best_iteration_ se usa automáticamente.
* - [save_model](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBClassifier.save_model)(fname)
  - Guarda el modelo en un archivo.
* - [score](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBClassifier.score)(X,  y,  sample_weight=None)
  - Retorna la precisión media en los datos y etiquetas del _test data_.
* - **Recuperar y Establecer**
  - 
* - [get_booster](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBClassifier.get_booster)()
  - Retorna el `Booster` subyacente de este modelo.
* - [get_metadata_routing](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBClassifier.get_metadata_routing)()
  - Recupera el enrutamiento de metadatos de este objeto.
* - [get_num_boosting_rounds](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBClassifier.get_num_boosting_rounds)()
  - Retorna el número de rondas de _xgboost boosting_.
* - [get_params](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBClassifier.get_params)(deep=True)
  - Retorna parámetros.
* - [get_xgb_params](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBClassifier.get_xgb_params)()
  - Recupera parámetros específicos de _xgboost_.
* - [set_fit_request](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBClassifier.set_fit_request)(...)
  - Los metadatos de solicitud pasados al método`.fit()`.
* - [set_params](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBClassifier.set_params)(**params)
  - Establece los parámetros de este estimador.
* - [set_predict_proba_request](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBClassifier.set_predict_proba_request)(...)
  - Los metadatos de solicitud pasados al método `.predict_proba()`.
* - [set_predict_request](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBClassifier.set_predict_request)(...)
  - Los metadatos de solicitud pasados ​​al método `.predict()`.
* - [set_score_request](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBClassifier.set_score_request)(...)
  - Los metadatos de solicitud pasados al método `.score()`.
```

<br/>

## XGBRFClassifier

Implementa un modelo de clasificación basado en _Random Forest_ utilizando _XGBoost_. Adecuado para problemas de clasificación. 

```{list-table}
:header-rows: 1

* - Constructor
  - Descripción
* - [xgboost.XGBRFClassifier](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBRFClassifier)(...)
  - API Scikit-Learn para _random forest classification_.
```

<br/>

### Atributos

Atributos de la clase . 

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - **best_iteration**
  - La mejor iteración obtenida por _early stopping_. Es _0-based_, por ejemplo, si la mejor iteración es la primera ronda, entonces la _best_iteration_ es 0.
* - **best_score**
  - La mejor puntuación obtenida por _early stopping_.
* - **coef_**
  - Propiedad coeficientes.
* - **feature_importances_**
  - Propiedad de importancia de _features_, el retorno depende del parámetro _importancia_type_.
* - **feature_names_in_**
  - Nombres de los _features_ vistos durante el ajuste.
* - **intercept_**
  - Propiedad de intercepción (sesgo).
* - **n_features_in_**
  - Número de _features_ vistos durante el ajuste.
```

<br/>

### Métodos

Métodos de la clase . 

```{list-table}
:header-rows: 1

* - Métodos
  - Descripción
* - [apply](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBRFClassifier.apply)(X,  iteration_range=None)
  - Retorna la hoja predicha cada árbol para cada muestra. Si el modelo está entrenado con _early stopping_, entonces la _best_iteration_ se usa automáticamente.
* - [evals_result](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBRFClassifier.evals_result)()
  - Retorna los resultados de la evaluación.
* - [fit](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBRFClassifier.fit)(X,  y,  , ...)
  - Ajusta el _gradient boosting classifier_.
* - [load_model](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBRFClassifier.load_model)(fname)
  - Carga el modelo desde un archivo o un _bytearray_.
* - [predict](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBRFClassifier.predict)(X,  output_margin=False,  validate_features=True,  ...)
  - Predice con _X_. Si el modelo está entrenado con _early stopping_, entonces la _best_iteration_ se usa automáticamente. El estimador usa _inplace_predict_ de forma predeterminada.
* - [predict_proba](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBRFClassifier.predict_proba)(X,  validate_features=True, ...)
  - Predice la probabilidad de que cada muestra de _X_ sea de una clase dada. Si el modelo está entrenado con _early stopping_, entonces la _best_iteration_ se usa automáticamente.
* - [save_model](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBRFClassifier.save_model)(fname)
  - Guarda el modelo en un archivo.
* - [score](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBRFClassifier.score)(X,  y,  sample_weight=None)
  - Retorna la precisión media en los datos y etiquetas del _test data_.
* - **Recuperar y Establecer**
  - 
* - [get_booster](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBRFClassifier.get_booster)()
  - Retorna el `Booster` subyacente de este modelo.
* - [get_metadata_routing](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBRFClassifier.get_metadata_routing)()
  - Recupera el enrutamiento de metadatos de este objeto.
* - [get_num_boosting_rounds](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBRFClassifier.get_num_boosting_rounds)()
  - Retorna el número de rondas de _xgboost boosting_.
* - [get_params](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBRFClassifier.get_params)(deep=True)
  - Retorna parámetros.
* - [get_xgb_params](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBRFClassifier.get_xgb_params)()
  - Recupera parámetros específicos de _xgboost_.
* - [set_fit_request](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBRFClassifier.set_fit_request)(...)
  - Los metadatos de solicitud pasados al método`.fit()`.
* - [set_params](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBRFClassifier.set_params)(**params)
  - Establece los parámetros de este estimador.
* - [set_predict_proba_request](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBRFClassifier.set_predict_proba_request)(...)
  - Los metadatos de solicitud pasados al método `.predict_proba()`.
* - [set_predict_request](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBRFClassifier.set_predict_request)(...)
  - Los metadatos de solicitud pasados ​​al método `.predict()`.
* - [set_score_request](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBRFClassifier.set_score_request)(...)
  - Los metadatos de solicitud pasados al método `.score()`.
```

<br/>

## XGBRFRegressor

Implementa un modelo de regresión basado en _Random Forest_ utilizando _XGBoost_. Combina múltiples árboles para mejorar la precisión.

```{list-table}
:header-rows: 1

* - Constructor
  - Descripción
* - [xgboost.XGBRFRegressor](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBRFRegressor)(...)
  - API Scikit-Learn para _random forest regression_.
```

<br/>

### Atributos

Atributos de la clase `XGBRFRegressor`. 

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - **best_iteration**
  - La mejor iteración obtenida por _early stopping_. Es _0-based_, por ejemplo, si la mejor iteración es la primera ronda, entonces la _best_iteration_ es 0.
* - **best_score**
  - La mejor puntuación obtenida por _early stopping_.
* - **coef_**
  - Propiedad coeficientes.
* - **feature_importances_**
  - Propiedad de importancia de _features_, el retorno depende del parámetro _importancia_type_.
* - **feature_names_in_**
  - Nombres de los _features_ vistos durante el ajuste.
* - **intercept_**
  - Propiedad de intercepción (sesgo).
* - **n_features_in_**
  - Número de _features_ vistos durante el ajuste.
```

<br/>

### Métodos

Métodos de la clase `XGBRFRegressor`. 

```{list-table}
:header-rows: 1

* - Métodos
  - Descripción
* - [apply](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBRFRegressor.apply)(X,  iteration_range=None)
  - Retorna la hoja predicha cada árbol para cada muestra. Si el modelo está entrenado con _early stopping_, entonces la _best_iteration_ se usa automáticamente.
* - [evals_result](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBRFRegressor.evals_result)()
  - Retorna los resultados de la evaluación.
* - [fit](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBRFRegressor.fit)(X,  y,  , ...)
  - Ajusta el _gradient boosting_.
* - [load_model](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBRFRegressor.load_model)(fname)
  - Carga el modelo desde un archivo o un _bytearray_.
* - [predict](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBRFRegressor.predict)(X,  output_margin=False,  validate_features=True,  ...)
  - Predice con _X_. Si el modelo está entrenado con _early stopping_, entonces la _best_iteration_ se usa automáticamente. El estimador usa _inplace_predict_ de forma predeterminada.
* - [save_model](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBRFRegressor.save_model)(fname)
  - Guarda el modelo en un archivo.
* - [score](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBRFRegressor.score)(X,  y,  sample_weight=None)
  - Retorna el coeficiente de determinación de la predicción.
* - **Recuperar y Establecer**
  - 
* - [get_booster](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBRFRegressor.get_booster)()
  - Retorna el `Booster` subyacente de este modelo.
* - [get_metadata_routing](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBRFRegressor.get_metadata_routing)()
  - Recupera el enrutamiento de metadatos de este objeto.
* - [get_num_boosting_rounds](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBRFRegressor.get_num_boosting_rounds)()
  - Retorna el número de rondas de _xgboost boosting_.
* - [get_params](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBRFRegressor.get_params)(deep=True)
  - Retorna parámetros.
* - [get_xgb_params](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBRFRegressor.get_xgb_params)()
  - Recupera parámetros específicos de _xgboost_.
* - [set_fit_request](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBRFRegressor.set_fit_request)(...)
  - Los metadatos de solicitud pasados al método`.fit()`.
* - [set_params](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBRFRegressor.set_params)(**params)
  - Establece los parámetros de este estimador.
* - [set_predict_request](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBRFRegressor.set_predict_request)(...)
  - Los metadatos de solicitud pasados ​​al método `.predict()`.
* - [set_score_request](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBRFRegressor.set_score_request)(...)
  - Los metadatos de solicitud pasados al método `.score()`.
```

<br/>

## XGBRanker

Diseñado para problemas de _ranking_. Aprende a ordenar elementos basándose en _features_ y grupos de datos.

```{list-table}
:header-rows: 1

* - Constructor
  - Descripción
* - [xgboost.XGBRanker](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBRanker)(...)
  - Implementación de la API Scikit-Learn para _ranking_.
```

<br/>

### Atributos

Atributos de la clase `XGBRanker`. 

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - **best_iteration**
  - La mejor iteración obtenida por _early stopping_. Es _0-based_, por ejemplo, si la mejor iteración es la primera ronda, entonces la _best_iteration_ es 0.
* - **best_score**
  - La mejor puntuación obtenida por _early stopping_.
* - **coef_**
  - Propiedad coeficientes.
* - **feature_importances_**
  - Propiedad de importancia de _features_, el retorno depende del parámetro _importancia_type_.
* - **feature_names_in_**
  - Nombres de los _features_ vistos durante el ajuste.
* - **intercept_**
  - Propiedad de intercepción (sesgo).
* - **n_features_in_**
  - Número de _features_ vistos durante el ajuste.
```

<br/>

### Métodos

Métodos de la clase `XGBRanker`. 

```{list-table}
:header-rows: 1

* - Métodos
  - Descripción
* - [apply](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBRanker.apply)(X,  iteration_range=None)
  - Retorna la hoja predicha cada árbol para cada muestra. Si el modelo está entrenado con _early stopping_, entonces la _best_iteration_ se usa automáticamente.
* - [evals_result](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBRanker.evals_result)()
  - Retorna los resultados de la evaluación.
* - [fit](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBRanker.fit)(X,  y,  , ...)
  - Ajusta el _gradient boosting ranker_.
* - [load_model](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBRanker.load_model)(fname)
  - Carga el modelo desde un archivo o un _bytearray_.
* - [predict](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBRanker.predict)(X,  output_margin=False,  validate_features=True,  ...)
  - Predice con _X_. Si el modelo está entrenado con _early stopping_, entonces la _best_iteration_ se usa automáticamente. El estimador usa _inplace_predict_ de forma predeterminada.
* - [save_model](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBRanker.save_model)(fname)
  - Guarda el modelo en un archivo.
* - [score](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBRanker.score)(X,  y)
  - Evalúa la puntuación de los datos utilizando la última métrica de evaluación. Si el modelo está entrenado con _early stopping_, entonces la _best_iteration_ se usa automáticamente.
* - **Recuperar y Establecer**
  - 
* - [get_booster](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBRanker.get_booster)()
  - Retorna el `Booster` subyacente de este modelo.
* - [get_metadata_routing](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBRanker.get_metadata_routing)()
  - Recupera el enrutamiento de metadatos de este objeto.
* - [get_num_boosting_rounds](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBRanker.get_num_boosting_rounds)()
  - Retorna el número de rondas de _xgboost boosting_.
* - [get_params](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBRanker.get_params)(deep=True)
  - Retorna parámetros.
* - [get_xgb_params](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBRanker.get_xgb_params)()
  - Recupera parámetros específicos de _xgboost_.
* - [set_fit_request](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBRanker.set_fit_request)(...)
  - Los metadatos de solicitud pasados al método`.fit()`.
* - [set_params](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBRanker.set_params)(**params)
  - Establece los parámetros de este estimador.
* - [set_predict_request](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBRanker.set_predict_request)(...)
  - Los metadatos de solicitud pasados ​​al método `.predict()`.
```

<br/>

## XGBRegressor

Implementa un modelo de regresión basado en _Gradient Boosting_. Ideal para problemas de predicción de valores continuos.

```{list-table}
:header-rows: 1

* - Constructor
  - Descripción
* - [xgboost.XGBRegressor](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBRegressor)(...)
  - Implementación de la API Scikit-Learn para regresión.
```

:::{caution}
A continuación no se enlistan todos los parámetros de la clase, para más información consultar el link.
:::

```python
# Sintaxis de llamada
xgb.XGBRegressor(*, objective='reg:squarederror', **kwargs)
```
- **Parámetros:**
    - **n_estimators** - `int`: Número de árboles de boosting.
    - **learning_rate** - `float`: Tasa de aprendizaje del boosting.
    - **max_depth** - `int`: Profundidad máxima de cada árbol.
    - **subsample** - `float`: Fracción de muestras por árbol.
    - **colsample_bytree** - `float`: Fracción de columnas por árbol.
    - **objective** - `str`, `callable`: Función objetivo a minimizar.
    - **eval_metric** - `str`, `list` de `str`, `callable`: Métrica(s) de evaluación.
    - **random_state** - `int`, `numpy.random.Generator`, `None`: Semilla para reproducibilidad.
    - **early_stopping_rounds** - `int`, `None`: Rondas sin mejora para detener el entrenamiento.
    - **booster** - `str`, `callable`: Tipo de modelo base (árbol, lineal, etc.).
    - **seed** - `int`: Semilla para el _boosting_.
- **Retorna:**
    - `XGBRegressor`.

:::{note}
Nombre de las loss function en xgboost (argumento objective):
- `reg:linear`: Regresión lineal.
- `reg:logistic`: Regresión logística para clasificación.
- `binary:logistic`: Cuando se desea cuantificar la probabilidad de pertener a clases en lugar de simplemente la decisión.
:::

### Uso

La forma básica de usar este clase es la siguiente:

<br/>

```python
# Importar clase
from xgboost import XGBRegressor

# Inicializar el modelo
model = XGBRegressor(
    n_estimators=100,       # Número de árboles (boosting rounds)
    learning_rate=0.1,      # Tasa de aprendizaje (eta)
    max_depth=3,            # Profundidad máxima del árbol
    subsample=0.8,          # Fracción de muestras por árbol
    colsample_bytree=0.8,   # Fracción de características por árbol
    objective='reg:squarederror',  # Función de pérdida para regresión
    eval_metric='rmse',     # Métrica de evaluación (ej: 'mae', 'rmse')
    random_state=42,        # Semilla para reproducibilidad
    early_stopping_rounds=10,  # Detención temprana
    booster='gbtree'       # Tipo de modelo (gbtree, gblinear o dart)
)

# Ajustar el modelo (con conjunto de validación opcional)
model.fit(
    X, y,
    eval_set=[(X_val, y_val)],  # Datos de validación (opcional)
    verbose=True  
)

# Predecir valores para nuevos datos
y_pred = model.predict(X_new)

# --- Opcionales ---
# Importancia de características (ganancia, peso, cobertura)
feature_importances = model.feature_importances_
print("Importancia de características:", feature_importances)

# Obtener el mejor score de validación (si se usó eval_set)
if hasattr(model, 'best_score'):
    print(f"Mejor {model.eval_metric}: {model.best_score:.4f}")

# Gráfico de importancia de características
from xgboost import plot_importance
import matplotlib.pyplot as plt
plot_importance(model)
plt.show()

# Guardar modelo en formato nativo
model.save_model('xgb_regressor.json')

# Cargar modelo pre-entrenado
model.load_model('xgb_regressor.json')
```

<br/>

### Atributos

Atributos de la clase `XGBRegressor`. 

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - **best_iteration**
  - La mejor iteración obtenida por _early stopping_. Es _0-based_, por ejemplo, si la mejor iteración es la primera ronda, entonces la _best_iteration_ es 0.
* - **best_score**
  - La mejor puntuación obtenida por _early stopping_.
* - **coef_**
  - Propiedad coeficientes.
* - **feature_importances_**
  - Propiedad de importancia de _features_, el retorno depende del parámetro _importancia_type_.
* - **feature_names_in_**
  - Nombres de los _features_ vistos durante el ajuste.
* - **intercept_**
  - Propiedad de intercepción (sesgo).
* - **n_features_in_**
  - Número de _features_ vistos durante el ajuste.
```
<br/>

### Métodos

Métodos de la clase `XGBRegressor`. 

```{list-table}
:header-rows: 1

* - Métodos
  - Descripción
* - [apply](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBRegressor.apply)(X,  iteration_range=None)
  - Retorna la hoja predicha cada árbol para cada muestra. Si el modelo está entrenado con _early stopping_, entonces la _best_iteration_ se usa automáticamente.
* - [evals_result](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBRegressor.evals_result)()
  - Retorna los resultados de la evaluación.
* - [fit](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBRegressor.fit)(X,  y,  , ...)
  - Ajusta el _gradient boosting_.
* - [load_model](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBRegressor.load_model)(fname)
  - Carga el modelo desde un archivo o un _bytearray_.
* - [predict](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBRegressor.predict)(X,  output_margin=False,  validate_features=True,  ...)
  - Predice con _X_. Si el modelo está entrenado con _early stopping_, entonces la _best_iteration_ se usa automáticamente. El estimador usa _inplace_predict_ de forma predeterminada.
* - [save_model](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBRegressor.save_model)(fname)
  - Guarda el modelo en un archivo.
* - [score](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBRegressor.score)(X,  y,  sample_weight=None)
  - Retorna el coeficiente de determinación de la predicción.
* - **Recuperar y Establecer**
  - 
* - [get_booster](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBRegressor.get_booster)()
  - Retorna el `Booster` subyacente de este modelo.
* - [get_metadata_routing](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBRegressor.get_metadata_routing)()
  - Recupera el enrutamiento de metadatos de este objeto.
* - [get_num_boosting_rounds](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBRegressor.get_num_boosting_rounds)()
  - Retorna el número de rondas de _xgboost boosting_.
* - [get_params](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBRegressor.get_params)(deep=True)
  - Retorna parámetros.
* - [get_xgb_params](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBRegressor.get_xgb_params)()
  - Recupera parámetros específicos de _xgboost_.
* - [set_fit_request](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBRegressor.set_fit_request)(...)
  - Los metadatos de solicitud pasados al método`.fit()`.
* - [set_params](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBRegressor.set_params)(**params)
  - Establece los parámetros de este estimador.
* - [set_predict_request](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBRegressor.set_predict_request)(...)
  - Los metadatos de solicitud pasados ​​al método `.predict()`.
* - [set_score_request](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBRegressor.set_score_request)(...)
  - Los metadatos de solicitud pasados al método `.score()`.
```