# Parámetros

En esta sección se enlistan parámetros de *XGBoost*.

## Parámetros generales

Los parámetros generales en *XGBoost* configuran aspectos fundamentales del modelo y su ejecución. Estos parámetros permiten ajustar el comportamiento del algoritmo para adaptarse mejor a diferentes entornos y necesidades.

:::{note}
Para más información visitar la [documentación](https://xgboost.readthedocs.io/en/stable/parameter.html#general-parameters) de _XGBoost_.
:::

| Parámetro | Descripción |
| :----------- | :---------- |
| `booster` - \[default= `gbtree`] | Define el tipo de modelo a usar. Puede ser `gbtree`, `gblinear` o `dart`; `gbtree` y `dart` utilizan modelos basados en árboles, mientras que `gblinear` utiliza funciones lineales. |
| `device` - \[default= `cpu`] | Especifica el hardware en el que se ejecutará el modelo. <br/> • `cpu`: Utiliza la CPU. <br/> • `cuda`: Utiliza una GPU (dispositivo CUDA). <br/> • `cuda <ordinal>`: *\<ordinal>* es un número entero que especifica el ordinal de la GPU (qué GPU desea usar si se tiene más de un dispositivo). <br/> • `gpu`: Selección predeterminada de dispositivos GPU de la lista de dispositivos disponibles y compatibles. <br/> • `gpu`: <ordinal>: Selección predeterminada de dispositivos GPU de la lista de dispositivos disponibles y compatibles.  |
| `verbosity` - \[default=`1`] | Verbosidad de la impresión de mensajes. Los valores válidos son 0 (silencio), 1 (advertencia), 2 (información), 3 (depuración).  |
| `validate_parameters` - \[default to `True`] | Cuando se establece en `True`, XGBoost realizará la validación de los parámetros de entrada para comprobar si se utiliza un parámetro o no. |
| `nthread` - \[default al número máximo de subprocesos disponibles] | Número de subprocesos paralelos utilizados para ejecutar XGBoost. |
| `disable_default_eval_metric` - \[default= `False`] | _Flag_ para deshabilitar la métrica predeterminada. Establézcalo en 1 o `True` para deshabilitarlo. |

<br/>

(xgb-parameters)=
## Parámetros del _Booster_

### _Tree Booster_

Parámetros cuando `booster=gbtree`.

:::{note}
Para más información visitar la [documentación](https://xgboost.readthedocs.io/en/stable/parameter.html#parameters-for-tree-booster) de _XGBoost_.
:::

| Parámetro | Descripción |
| :----------- | :---------- |
| `eta` - \[default=`0.3`, range: `[0,1]`, alias: `learning_rate`] | Contracción del tamaño del paso utilizada en la actualización para evitar el sobreajuste. |
| `gamma` - \[default=`0`, range: `[0,∞]`, alias: `min_split_loss`] | Reducción mínima de la pérdida requerida para hacer una partición adicional en un nodo hoja del árbol. Cuanto mayor sea `gamma`, más conservador será el algoritmo. |
| `max_depth` - \[default=`6`, range: `[0,∞]`, type=`int32`] | Profundidad máxima de un árbol. El aumento de este valor hará que el modelo sea más complejo y más propenso a sobreajustarse. `0` indica que no hay límite de profundidad. |
| `min_child_weight` - \[default=`1`, range: `[0,∞]`] | Suma mínima del peso de la instancia (hessiana) necesaria en un elemento hijo. |
| `max_delta_step` - \[default=`0`, range: `[0,∞]`] | Paso delta máximo que se permite que sea la salida de cada hoja. Si el valor se establece en 0, significa que no hay ninguna restricción. Si se establece en un valor positivo, puede ayudar a que el paso de actualización sea más conservador. |
| `subsample` - \[default=`1`, range: `(0,1]`] | Proporción de submuestras de las instancias de entrenamiento. Establecerlo en 0,5 significa que XGBoost muestrearía aleatoriamente la mitad de los datos de entrenamiento antes de entrenar el árbol. Y esto evitará el sobreajuste. |
| `sampling_method` - \[default= `uniform`] | Método que se va a utilizar para muestrear las instancias de entrenamiento. <br/> • `uniform`: Cada instancia de entrenamiento tiene la misma probabilidad de ser seleccionada. Por lo general, establecer la `subsample > = 0.5` para obtener buenos resultados. <br/> • `gradient_based`: La probabilidad de selección para cada instancia de entrenamiento es proporcional al valor absoluto regularizado de los gradientes |
| `colsample_bytree` - \[default=`1`, range: `(0, 1]`] | Es la proporción de submuestras de las columnas al construir cada árbol. El submuestreo se produce una vez por cada árbol construido. |
| `ccolsample_bylevel` - \[default=`1`, range: `(0, 1]`] | Es la proporción de submuestras de columnas para cada nivel. El submuestreo se produce una vez por cada nuevo nivel de profundidad alcanzado en un árbol. |
| `colsample_bynode` - \[default=`1`, range: `(0, 1]`] | Es la proporción de submuestras de columnas para cada nodo (división). El submuestreo se produce una vez cada vez que se evalúa una nueva división. |
| `lambda` - \[default=`1`, range: `[0,∞]`, alias: `reg_lambda`] | Término L2 de regularización de pesos. El aumento de este valor hará que el modelo sea más conservador. |
| `alpha` - \[default=`0`, range: `[0,∞]`, alias: `reg_alpha`] | Término L1 de regularización de pesos. El aumento de este valor hará que el modelo sea más conservador. |
| `tree_method` - \[default= `auto`, type=`string`] | El algoritmo de construcción de árbol utilizado en XGBoost. <br/> • `auto`: Igual que el método del árbol `hist`. <br/> • `exact`: Algoritmo _greedy_ exacto. Enumera todos los candidatos divididos. <br/> • `approx`: Algoritmo expansivo aproximado utilizando boceto de cuantiles e histograma de gradiente. <br/> • `hist`: Histograma más rápido, optimizado, algoritmo _greedy_ aproximado. |
| `scale_pos_weight` - \[default=`1`] | Controla el equilibrio de pesos positivos y negativos, útil para clases desequilibradas. |
| `updater` | Una cadena separada por comas que define la secuencia de actualizadores de árboles que se van a ejecutar, lo que proporciona una forma modular de construir y modificar los árboles. <br/> • `grow_colmaker`: Construcción de árboles basada en columnas no distribuidas. <br/> • `grow_histmaker`: Construcción de árboles distribuidos con división de datos basada en filas basada en una propuesta global de conteo de histogramas. <br/> • `grow_quantile_histmaker`: Árbol de crecimiento usando histograma cuantificado. <br/> • `grow_gpu_hist`: Habilitado cuando `tree_method` se establece en `hist` junto con `device=cuda`. <br/> • `grow_gpu_approx`: Habilitado cuando `tree_method` se establece en `approx` junto con `device=cuda`. <br/> • `sync`: Sincroniza los árboles en todos los nodos distribuidos. <br/> • `refresh`: Actualiza las estadísticas del árbol y/o los valores de las hojas en función de los datos actuales. Tenga en cuenta que no se realiza ningún submuestreo aleatorio de filas de datos. <br/> • `prune`: Poda las divisiones donde la pérdida < *min_split_loss* (o gamma) y los nodos que tienen una profundidad superior a `max_depth`. |
| `refresh_leaf` - \[default=`1`] | Este es un parámetro del actualizador de `refresh`. Cuando este indicador es 1, se actualizan las hojas de los árboles y las estadísticas de los nodos de los árboles. Cuando es 0, solo se actualizan las estadísticas del nodo. |
| `process_type` - \[default= `default`] | Un tipo de proceso de impulso que se va a ejecutar. <br/> • `default`: El proceso normal de impulso que crea nuevos árboles. <br/> • `update`: Comienza a partir de un modelo existente y solo actualiza sus árboles. En cada iteración de *boosting*, se toma un árbol del modelo inicial, se ejecuta una secuencia especificada de actualizadores para ese árbol y se agrega un árbol modificado al nuevo modelo. El nuevo modelo tendría el mismo número de árboles o uno menor, dependiendo del número de iteraciones de impulso realizadas. |
| `grow_policy` - \[default= `depthwise`] | Controla la forma en que se agregan nuevos nodos al árbol. Actualmente solo se admite si `tree_method=hist` o `tree_method=approx` . <br/> • `depthwise`: Dividir en los nodos más cercanos a la raíz. <br/> • `lossguide`: División en los nodos con mayor cambio de pérdida. |
| `max_leaves` - \[default=`0`, type=`int32`] | Número máximo de nodos que se van a agregar. No se utiliza por el método del árbol `exact`. |
| `max_bin` - \[default=`256`, type=`int32`] | Solo se usa si `tree_method` está establecido en `hist` o `approx`. |
| `num_parallel_tree` - \[default=`1`] | Número de árboles paralelos construidos durante cada iteración. Esta opción se utiliza para admitir el bosque aleatorio potenciado. |
| `monotone_constraints` | Restricción de la monotonicidad variable. |
| `interaction_constraints` | Restricciones para la interacción que representan interacciones permitidas. |
| `multi_strategy` - \[default = `one_output_per_tree`] | La estrategia utilizada para entrenar modelos de varios objetivos, incluida la regresión de varios objetivos y la clasificación de varias clases. <br/> • `one_output_per_tree`: Un modelo para cada objetivo. <br/> • `multi_output_tree`: Utilize árboles de varios objetivos. |

<br/>

### _DartTree Booster_

Parámetros cuando `booster=dart`.

:::{note}
Para más información visitar la [documentación](https://xgboost.readthedocs.io/en/stable/parameter.html#additional-parameters-for-dart-booster-booster-dart) de _XGBoost_.
:::

| Parámetro | Descripción |
| :----------- | :---------- |
| `sample_type` - \[default= `uniform`] | Tipo de algoritmo de muestreo. <br/> • `uniform`: Los árboles eliminados se seleccionan de manera uniforme. <br/> • `weighted`: Los árboles eliminados se seleccionan en proporción al peso. |
| `normalize_type` - \[default= `tree`] | Tipo de algoritmo de normalización. <br/> • `tree`: Los árboles nuevos tienen el mismo peso que cada uno de los árboles caídos. El peso de los árboles nuevos es *1 / (k + learning_rate)*. <br/> • `forest`: Los árboles nuevos tienen el mismo peso que la suma de los árboles eliminados (bosque). El peso de los árboles nuevos es *1 / (1 + learning_rate)*. |
| `rate_drop` - \[default=`0.0`, range: `[0.0, 1.0]`] | Tasa de deserción (una fracción de los árboles anteriores que eliminan durante la deserción). |
| `one_drop` - \[default=`0`] | Cuando esta marca está habilitada, siempre se elimina al menos un árbol durante la eliminación (permite la eliminación de binomio más uno o épsilon del documento DART original). |
| `skip_drop` - \[default=`0.0`, range: `[0.0, 1.0]`] | Probabilidad de omitir el procedimiento de eliminación durante una iteración de _boosting_. |


<br/>

### _LinearTree Booster_

Parámetros cuando `booster=gblinear`.

:::{note}
Para más información visitar la [documentación](https://xgboost.readthedocs.io/en/stable/parameter.html#parameters-for-linear-booster-booster-gblinear) de _XGBoost_.
:::

| Parámetro | Descripción |
| :----------- | :---------- |
| `lambda` - \[default=`0`, alias: `reg_lambda`] | Término L2 de regularización de pesos. El aumento de este valor hará que el modelo sea más conservador. Normalizado al número de ejemplos de entrenamiento. |
| `alpha` - \[default=`0`, alias: `reg_alpha`] | Término L1 de regularización de pesos. El aumento de este valor hará que el modelo sea más conservador. Normalizado al número de ejemplos de entrenamiento. |
| `eta` - \[default=`0.5`, alias: `learning_rate`, range: `[0,1]`] | Contracción del tamaño del paso utilizada en la actualización para evitar el sobreajuste. |
| `updater` - \[default= `shotgun`] | Elección del algoritmo para adaptarse al modelo lineal. <br/> • `shotgun`: Algoritmo de descenso de coordenadas paralelas basado en el algoritmo de _shotgun_. Utiliza el paralelismo '*hogwild*' y, por lo tanto, produce una solución no determinista en cada ejecución. <br/> • `coord_descent`: Algoritmo de descenso de coordenadas ordinario. También multiproceso, pero aún así produce una solución determinista. Cuando el parámetro del dispositivo se establece en cuda o gpu, se usaría una variante de GPU. |
| `feature_selector` - \[default= `cyclic`] | Selección de características y método de ordenado. <br/> • `cyclic`: Selección determinista mediante el ciclo de una en una de las características. <br/> • `shuffle`: Similar al cíclico, pero con un barajado aleatorio de funciones antes de cada actualización. <br/> • `random`: Un selector de coordenadas aleatorio (con reemplazo). <br/> • `greedy`: Selecciona la coordenada con la mayor magnitud de gradiente. Tiene una complejidad O(num_feature^2). Es totalmente determinista. <br/> • `thrifty`: Selector de características ahorrativo y aproximadamente _greedy_. Antes de las actualizaciones cíclicas, los reordenamientos de las características en magnitud descendente de sus cambios de peso univariados. Esta operación es multiproceso y es una aproximación de complejidad lineal de la selección expansiva cuadrática. |
| `top_k` - \[default=`0`] | El número de características principales que se van a seleccionar en el selector de características _greedy_ y _`thrifty`_. El valor de *0* significa usar todas las características. |

<br/>

## Tarea de aprendizaje

Especifican la tarea de aprendizaje y el objetivo de aprendizaje correspondiente.

:::{note}
Para más información visitar la [documentación](https://xgboost.readthedocs.io/en/stable/parameter.html#learning-task-parameters) de _XGBoost_.
:::

| Parámetro | Descripción |
| :----------- | :---------- |
| `objective` - \[default=`reg:squarederror`] | Define la función de pérdida que el modelo optimiza. Ver {ref}`parameters-objective`. |
| `base_score` | La puntuación de predicción inicial de todas las instancias, sesgo global. El parámetro se estima automáticamente para los objetivos seleccionados antes del entrenamiento. Para deshabilitar la estimación, especifique un argumento de número real. |
| `eval_metric` - \[default de acuerdo a `objective`] | Métricas de evaluación para los datos de validación, se asignará una métrica predeterminada de acuerdo con el objetivo (*rmse* para la regresión y *logloss* para la clasificación, *precisión promedio media* para `rank:map`, etc.). Ver {ref}`parameters-eval_metric`. |
| `seed` - \[default=`0`] | Semilla de número aleatorio. |
| `seed_per_iteration` - \[default= `false`] | Semilla PRNG determnísticamente a través del número de iterador. |

<br/>

(parameters-objective)=
### Objetivo

Define la función de pérdida que el modelo optimiza. La función de pérdida cuantifica la diferencia entre un valor predicho y su verdadero valor. El objetivo de los modelos es minimizar la función de pérdida.

| Objective | Descripción |
|-----------|-------------|
| `reg:squarederror` | Regresión con error cuadrático medio (MSE), estándar para tareas de regresión. |
| `reg:squaredlogerror` | Regresión con error cuadrático logarítmico (MSLE), útil cuando los errores relativos importan más que los absolutos. |
| `reg:logistic` | Regresión logística para clasificación binaria, devuelve valores entre 0 y 1. |
| `reg:pseudohubererror` | Regresión robusta basada en la función pseudo-Huber, tolerante a valores atípicos. |
| `reg:absoluteerror` | Regresión con error absoluto medio (MAE), menos sensible a outliers. |
| `reg:quantileerror` | Regresión cuantílica, permite predecir cuantiles específicos como la mediana. |
| `reg:gamma` | Regresión con función de pérdida basada en la distribución gamma, útil para datos sesgados positivamente. |
| `reg:tweedie` | Regresión Tweedie, útil para modelos que combinan propiedades de Poisson y Gamma (como seguros o energía). |
| `binary:logistic` | Clasificación binaria con salida probabilística (entre 0 y 1). |
| `binary:logitraw` | Clasificación binaria con salida cruda del logit (antes de aplicar sigmoid). |
| `binary:hinge` | Clasificación binaria con función de pérdida tipo SVM (hinge loss), útil para márgenes. |
| `count:poisson` | Regresión para conteo de eventos usando distribución de Poisson. |
| `survival:cox` | Modelo de supervivencia basado en la función de riesgo proporcional de Cox. |
| `survival:aft` | Modelo de supervivencia *Accelerated Failure Time* (AFT), útil para modelar tiempos de vida. |
| `multi:softmax` | Clasificación multiclase con salida de clase predicha (índice entero). Requiere `num_class`. |
| `multi:softprob` | Clasificación multiclase con salida de probabilidades por clase. Requiere `num_class`. |
| `rank:ndcg` | Optimización de ranking basada en la métrica NDCG (*Normalized Discounted Cumulative Gain*). |
| `rank:map` | Optimización de ranking según la métrica MAP (*Mean Average Precision*). |
| `rank:pairwise` | Ranking basado en comparación por pares, útil para tareas de ordenamiento. |

<br/>

(parameters-eval_metric)=
### Métrica de evaluación

Especifica la métrica de evaluación utilizada para medir el rendimiento del modelo, que varía según el objetivo definido.

| Métrica | Descripción | Tipo de problema |
|---------|-------------|------------------|
| `auc` | Área bajo la curva ROC (AUC), métrica estándar para clasificación binaria. | Clasificación binaria |
| `aucpr` | Área bajo la curva de *precisión-recall*, útil cuando hay desbalance de clases. | Clasificación binaria |
| `error` | Tasa de error (*error rate*), proporción de predicciones incorrectas en clasificación. | Clasificación binaria |
| `error@t` | Tasa de error considerando el top `t` de clases con mayor probabilidad. | Clasificación binaria |
| `logloss` | Log loss o pérdida logística, métrica estándar para clasificación binaria probabilística. | Clasificación binaria |
| `merror` | Tasa de error en clasificación multiclase (multiclass error). | Clasificación multiclase |
| `mlogloss` | Pérdida logística para clasificación multiclase (*multiclass log loss*). | Clasificación multiclase |
| `map` | MAP (*Mean Average Precision*), otra métrica clave en ranking y búsqueda. | Ranking |
| `map@n`, `ndcg@n`, `pre@n` | Versiones truncadas de `map`, `ndcg` y precisión, evaluadas hasta la posición `n` del ranking. | Ranking |
| `map-`, `ndcg-`, `map@n-`, `ndcg@n-` | Variantes de ranking que penalizan errores por debajo del ideal. | Ranking |
| `ndcg` | NDCG (*Normalized Discounted Cumulative Gain*), métrica común en tareas de ranking. | Ranking |
| `gamma-deviance` | Desviación gamma, métrica basada en la función de pérdida gamma. | Regresión |
| `gamma-nloglik` | Log-verosimilitud negativa para regresión basada en distribución gamma. | Regresión |
| `mae` | Error absoluto medio (*Mean Absolute Error*), menos sensible a valores atípicos que `rmse`. | Regresión |
| `mape` | Error porcentual absoluto medio (*Mean Absolute Percentage Error*), expresa el error como porcentaje. | Regresión |
| `mphe` | Error porcentual absoluto medio negativo (*Mean Pseudo Huber Error*), más robusto frente a outliers. | Regresión |
| `poisson-nloglik` | Log-verosimilitud negativa para regresión de conteos usando distribución de Poisson. | Regresión |
| `rmse` | Raíz del error cuadrático medio (*Root Mean Squared Error*), métrica estándar para regresión. | Regresión |
| `rmsle` | Raíz del error cuadrático logarítmico (*Root Mean Squared Log Error*), útil cuando importan los errores relativos. | Regresión |
| `tweedie-nloglik` | Log-verosimilitud negativa para regresión Tweedie. | Regresión |
| `aft-nloglik` | Log-verosimilitud negativa para modelos AFT en supervivencia. | Supervivencia |
| `cox-nloglik` | Log-verosimilitud negativa para el modelo de Cox en análisis de supervivencia. | Supervivencia |
| `interval-regression-accuracy` | Exactitud de regresión por intervalo, evalúa si la predicción cae dentro del intervalo objetivo. | Supervivencia |


