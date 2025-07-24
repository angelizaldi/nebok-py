# Learning API

Es la interfaz principal para entrenar, ajustar y utilizar modelos. Proporciona las funciones necesarias para entrenar modelos, realizar predicciones y ajustar hiperparámetros. Está diseñada para ser flexible y fácil de usar, permitiendo a los usuarios trabajar con diferentes tipos de datos y configuraciones. 

:::{caution}
Las funciones de esta API requieren que los datos sea de tipo `DMatrix`.
:::

:::{note}
Para más información visitar la [documentación](https://xgboost.readthedocs.io/en/stable/python/python_api.html#module-xgboost.training) de _XGBoost_.
:::


## Funciones

Functiones de _Learning API_. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [xgboost.cv](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.cv)(params,  dtrain,  ...)
  - Validación cruzada con parámetros dados.
* - [xgboost.train](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.train)(params,  dtrain, ...)
  - Entrena un _booster_ con los parámetros dados.
```

<br/>

### Notas de _cv_

[xgboost.cv](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.cv): _Cross validation_. El objeto retornado contiene los _score/error_ del _train_ y _test_, tanto las medias como la desviaciones para cada _fold_. Si `as_pandas=True` entonces se retorna `DataFrame`, las columnas tienen nombres como _'test-metric-mean'_ y _'test-metric-std'_, siendo _metric_ el nombre de la métrica que se usó, lo mismo para _train_.
```python
# Sintaxis de llamada
xgb.cv(params, dtrain, num_boost_round=10, nfold=3, stratified=False, folds=None, metrics=(),
       obj=None, feval=None, maximize=None, early_stopping_rounds=None, fpreproc=None, 
       as_pandas=True, verbose_eval=None, show_stdv=True, seed=0, callbacks=None, shuffle=True, 
       custom_metric=None)
```
- **Parámetros:**
    - **params** - `dict`: Parámetros del _booster_, es decir del estimador. Tanto las llaves como los valores son `str`, excepto si el valor es `int` o `float`. Ver {ref}`xgb-parameters`.
    - **dtrain** - `Dmatrix`: Datos a ser entrenados. Tiene que ser un objeto creado con `xgboost.DMatrix()`.
    - **num_boost_round** - `int`: Número de interaciones del _boosting_ (número de modelos del _base learner_).
    - **nfold** - `int`: Número de _folds_ en el _CV_.
    - **metrics** - `str` o `list de str`: Métricas a usar durante el _CV_. Ver {ref}`parameters-eval_metric`.
        - Para clasificación se recomienda: `'error'`, `'logloss'` o `'auc'`.
        - Para regresión se recomienda:  `'rmse'` o `'mae'`
    - **stratified** - `bool`: Realizar un muestreo estratificado.
    - **early_stopping_rounds** - `int`: Número de _rounds_ mínimos en el que se debe de mejorar el _score_ para continuar con el ciclo.
    - **shuffle** - `bool`: Mezcla los datos antes de crear los _folds_.
    - **as_pandas** - `bool`: Para indicar que se retornen los resultados como `DataFrame`.
- **Retorna:**
    - `list` o `DataFrame`.

#### Uso

La forma básica de usar esta función es la siguiente:

```python
# Importar función y parámetros
from xgboost import cv
import xgboost as xgb
import numpy as np

# Convertir datos a formato DMatrix (optimizado para XGBoost)
dtrain = xgb.DMatrix(X, label=y)  # X: features, y: target

# Definir parámetros del modelo (similar a XGBClassifier/XGBRegressor)
params = {
    'objective': 'binary:logistic',  # Objetivo (ej. reg:linear, multi:softmax)
    'max_depth': 3,
    'learning_rate': 0.1,
    'subsample': 0.8,
    'colsample_bytree': 0.8,
    'eval_metric': 'logloss',  # Métrica (ej. rmse, mae, auc, error)
    'seed': 42
}

# Ejecutar validación cruzada
cv_results = cv(
    params=params,
    dtrain=dtrain,
    num_boost_round=100,  # Número máximo de árboles
    nfold=5,             # Número de folds (k-fold)
    stratified=True,     # Estratificación para clasificación
    early_stopping_rounds=10,  # Detención temprana
    shuffle=True,        # Barajar datos antes de dividir
    verbose_eval=True    # Mostrar progreso
)

# --- Resultados ---
# Mejor número de boosting rounds (según early stopping)
best_num_rounds = cv_results.shape[0] - 1  # Última iteración válida
print(f"Mejor número de árboles: {best_num_rounds}")

# Mejor métrica de validación (ej. para logloss, busca el mínimo)
best_metric = np.min(cv_results['test-logloss-mean'])
print(f"Mejor logloss promedio: {best_metric:.4f}")

# Gráfico de métricas (requiere matplotlib)
import matplotlib.pyplot as plt
plt.plot(cv_results['test-logloss-mean'], label='Val LogLoss')
plt.legend()
plt.show()

# --- Opcional: Entrenar modelo final con los mejores rounds ---
model = xgb.train(
    params=params,
    dtrain=dtrain,
    num_boost_round=best_num_rounds
)
```
- El nombre de las columna de _cv_results_ puede variar dependiento de la métrica elegida.

<br/>

### Notas de _train_

[xgboost.train](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.train): Entrena un modelo de _XGBoost_ utilizando una `DMatrix` como entrada.
```python
# Sintaxis de llamada
xgb.train(params, dtrain, num_boost_round=10, *, evals=None, obj=None, feval=None, 
       maximize=None, early_stopping_rounds=None, evals_result=None, verbose_eval=True, 
       xgb_model=None, callbacks=None, custom_metric=None)
```

**Parámetros:**
- **params** - `dict`: Diccionario de parámetros para el booster (árboles, regresión lineal, etc.). Incluye parámetros como `objective`, `eta`, `max_depth`, etc.
- **dtrain** - `DMatrix`: Los datos de entrenamiento en formato `DMatrix` de XGBoost.
- **num_boost_round** - `int`: Número total de rondas de boosting (número de árboles a construir).
- **evals** - `list` de `tuple`: Lista de conjuntos de datos de evaluación (como `DMatrix`, etiqueta) para monitorear el rendimiento durante el entrenamiento. Por ejemplo: `[(dtrain, 'train'), (dval, 'eval')]`.
- **early_stopping_rounds** - `int`, `None`: Si se proporciona, el entrenamiento se detendrá anticipadamente si la métrica de evaluación no mejora durante este número de rondas consecutivas. Requiere la presencia de `evals`.
- **verbose_eval** - `bool`, `int`: Controla la frecuencia con la que se imprimen los resultados de la evaluación durante el entrenamiento. `True` o `1` imprime en cada ronda, un entero positivo imprime cada N rondas, y `False` o `0` no imprime.

**Retorna:**
- `Booster`.

:::{note}
Ver {ref}`Booster-methods` para revisar los métodos.
:::

#### Uso

La forma básica de usar esta función es la siguiente:

```python
# Importar módulos necesarios
import xgboost as xgb
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt

# 1. Preparación de datos
# Convertir a DMatrix (formato óptimo para XGBoost)
dtrain = xgb.DMatrix(X_train, label=y_train)  
dval = xgb.DMatrix(X_val, label=y_val)        

# 2. Definición de parámetros
params = {
    'booster': 'gbtree',           # Tipo de modelo (gbtree, gblinear, dart)
    'objective': 'reg:squarederror', # Objetivo (regresión)
    # 'objective': 'binary:logistic' # Para clasificación binaria
    'max_depth': 3,                # Profundidad máxima
    'eta': 0.1,                    # Learning rate (tasa de aprendizaje)
    'subsample': 0.8,              % Muestras por árbol
    'colsample_bytree': 0.8,       % Características por árbol
    'alpha': 0.1,                  # Regularización L1
    'lambda': 1.0,                 # Regularización L2
    'eval_metric': 'rmse',         # Métrica de evaluación
    # 'eval_metric': ['rmse', 'mae'] # Múltiples métricas
    'seed': 42                     # Semilla aleatoria
}

# 3. Entrenamiento del modelo
evals = [(dtrain, 'train'), (dval, 'val')]  # Conjuntos para evaluación

model = xgb.train(
    params=params,
    dtrain=dtrain,
    num_boost_round=1000,          # Número máximo de iteraciones
    evals=evals,                   # Conjuntos de evaluación
    early_stopping_rounds=50,      # Paciencia para early stopping
    verbose_eval=10,               # Mostrar progreso cada 10 iteraciones
    # callbacks=[custom_callback]   # Callbacks personalizados (opcional)
)

# 4. Predicción
dtest = xgb.DMatrix(X_test)       # Datos de prueba en formato DMatrix
y_pred = model.predict(dtest)     # Predicciones

# --- Análisis de resultados ---
# Mejor iteración (si se usó early stopping)
print(f"Mejor iteración: {model.best_iteration}")

# Importancia de características
importance = model.get_score(importance_type='gain')
print("Importancia de características:", importance)

# Gráfico de importancia
xgb.plot_importance(model, max_num_features=10)
plt.show()

# Gráfico de árboles (primer árbol)
xgb.plot_tree(model, num_trees=0)
plt.show()

# Guardar modelo
model.save_model('modelo_xgb.json')

# Cargar modelo
loaded_model = xgb.Booster()
loaded_model.load_model('modelo_xgb.json')
```