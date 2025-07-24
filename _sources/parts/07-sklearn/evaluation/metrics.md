# Metrics

Proporciona funciones para evaluar el rendimiento de modelos, como precisión, _recall_, _F1-score_ y matrices de confusión. Para importar este módulo o una clase o función específica usar:

```python
# Importar módulo
from sklearn import metrics

# Importar clase específica
from sklearn.metrics import ClassName

# Importar función específica
from sklearn.metrics import func_name
```
- _ClassName_ o _func_name_ es el nombre de la clase o función respectivamente.

:::{note}
Para más información de esta librería visitar la [documentación](https://scikit-learn.org/stable/api/sklearn.metrics.html) de `sklearn`.
:::

<br/>

## Clases - Visualización.

Clases implementadas en el módulo `metrics` para visualización. Incluye herramientas para visualizar métricas, como curvas _ROC_, curvas de precisión-recall y matrices de confusión.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [ConfusionMatrixDisplay](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.ConfusionMatrixDisplay.html)(confusion_matrix, ...)
  - Visualización de la matriz de confusión.
* - [DetCurveDisplay](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.DetCurveDisplay.html)(, ...)
  - Visualización de la curva DET.
* - [PrecisionRecallDisplay](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PrecisionRecallDisplay.html)(precision, recall, ...)
  - Visualización _Precision-Recall_.
* - [PredictionErrorDisplay](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PredictionErrorDisplay.html)(, ...)
  - Visualización del error de predicción de un modelo de regresión.
* - [RocCurveDisplay](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.RocCurveDisplay.html)(, ...)
  - Visualización de la curva _ROC_.
```

<br/>

## Funciones

Funciones implementadas en el módulo `metrics`. A continuación se presena un pequeño resumen por sección:
- **Biclustering**: Esta sección incluye métricas específicas para evaluar modelos de _biclustering_, que agrupan filas y columnas simultáneamente.
- **Clasificación**: Contiene métricas para evaluar modelos de clasificación, como precisión, _recall_, _F1-score_, matriz de confusión y curva _ROC_. Estas métricas son esenciales para medir la efectividad de los clasificadores.
- **Clusters**: Proporciona métricas para evaluar algoritmos de _clustering_, como el índice de silueta, el coeficiente de correlación de Rand ajustado y la homogeneidad. Estas métricas miden la calidad de los agrupamientos.
- **Distancias**: Aquí se describen métricas de distancia utilizadas para medir la similitud o disimilitud entre muestras, como la distancia euclidiana, la distancia de Manhattan y la distancia de coseno. Son útiles en _clustering_ y vecinos más cercanos (KNN).
- **Interfaz selección de modelo**: Herramientas útiles para definir las reglas para evaluar un modelo.
- **Pares de muestras**: Contiene funciones para calcular métricas de similitud o distancia entre pares de muestras, como la matriz de kernel y la matriz de distancias. Estas funciones son útiles en algoritmos que requieren comparaciones por pares.
- **Ranking _multilabel_**: Esta sección se enfoca en métricas para problemas de clasificación multietiqueta y ranking, como la precisión promedio (_average precision_) y la pérdida de ranking (_ranking loss_). Son útiles cuando cada muestra puede tener múltiples etiquetas.
- **Regresión**: Aquí se encuentran métricas para evaluar modelos de regresión, como el error cuadrático medio (MSE), el error absoluto medio (MAE) y el coeficiente de determinación ($R^2$). Estas métricas miden la precisión de las predicciones en problemas de regresión.

### Biclustering

Esta sección incluye métricas específicas para evaluar modelos de _biclustering_, que agrupan filas y columnas simultáneamente.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [consensus_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.consensus_score.html)(a, b, ...)
  - La similitud de dos conjuntos de _biclusters_.
```

<br/>

### Clasificación

Contiene métricas para evaluar modelos de clasificación, como precisión, _recall_, _F1-score_, matriz de confusión y curva _ROC_. Estas métricas son esenciales para medir la efectividad de los clasificadores.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [accuracy_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html)(y_true, y_pred, ...)
  - Puntuación de la clasificación de _accuracy_.
* - [auc](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.auc.html)(x, y)
  - Calcula el área bajo la curva (_AUC_) utilizando la regla trapezoidal.
* - [average_precision_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.average_precision_score.html)(y_true, y_score, ...)
  - Calcula la precisión media (AP) a partir de las puntuaciones de las predicciones.
* - [balanced_accuracy_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.balanced_accuracy_score.html)(y_true, y_pred, ...)
  - Calcula el _balanced accuracy_.
* - [brier_score_loss](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.brier_score_loss.html)(y_true, y_proba=None, ...)
  - Calcula la pérdida de puntuación Brier.
* - [class_likelihood_ratios](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.class_likelihood_ratios.html)(y_true, y_pred, ...)
  - Calcula los _likelihood ratios_ positivos y negativos de la clasificación binaria.
* - [classification_report](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.classification_report.html)(y_true, y_pred, ...)
  - Crea un informe de texto que muestre las principales métricas de clasificación.
* - [cohen_kappa_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.cohen_kappa_score.html)(y1, y2, ...)
  - Calcula la _kappa de Cohen_: una estadística que mide la concordancia _inter-annotator_.
* - [confusion_matrix](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html)(y_true, y_pred, ...)
  - Calcula la matriz de confusión para evaluar la precisión de una clasificación.
* - [d2_log_loss_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.d2_log_loss_score.html)(y_true, y_pred, ...)
  - Función de puntuación $D^2$, fracción de pérdida logarítmica explicada.
* - [dcg_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.dcg_score.html)(y_true, y_score, ...)
  - Calcula la ganancia acumulada descontada (_Discounted Cumulative Gain_).
* - [det_curve](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.det_curve.html)(y_true, y_score, pos_label=None, sample_weight=None)
  - Calcula los porcentajes de error para distintos umbrales de probabilidad.
* - [f1_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html)(y_true, y_pred, ...)
  - Calcula la puntuación _F1_, también conocida como puntuación F equilibrada o medida F.
* - [fbeta_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.fbeta_score.html)(y_true, y_pred, ...)
  - Calcula la puntuación F-beta.
* - [hamming_loss](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.hamming_loss.html)(y_true, y_pred, ...)
  - Calcula la pérdida media de Hamming.
* - [hinge_loss](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.hinge_loss.html)(y_true, pred_decision, ...)
  - Pérdida media _hinge_ (no regularizada).
* - [jaccard_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.jaccard_score.html)(y_true, y_pred, ...)
  - Puntuación del coeficiente de similitud de Jaccard.
* - [log_loss](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.log_loss.html)(y_true, y_pred, ...)
  - Pérdida logarítmica (_log loss_), también conocida como pérdida logística o pérdida de entropía cruzada.
* - [matthews_corrcoef](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.matthews_corrcoef.html)(y_true, y_pred, ...)
  - Calcula el coeficiente de correlación de Matthews (CCM).
* - [multilabel_confusion_matrix](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.multilabel_confusion_matrix.html)(y_true, y_pred, ...)
  - Calcula una matriz de confusión para cada clase o muestra.
* - [ndcg_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.ndcg_score.html)(y_true, y_score, ...)
  - Calcula la ganancia acumulada descontada normalizada (_Normalized Discounted Cumulative Gain_).
* - [precision_recall_curve](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_recall_curve.html)(y_true, y_score=None, ...)
  - Calcula los pares _precision-recall_ para diferentes _thresholds_ de probabilidad.
* - [precision_recall_fscore_support](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_recall_fscore_support.html)(y_true, y_pred, ...)
  - Calcula la precisión, _recall_, la medida F y el soporte para cada clase.
* - [precision_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_score.html)(y_true, y_pred, ...)
  - Calcula la precisión.
* - [recall_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.recall_score.html)(y_true, y_pred, ...)
  - Calcula el _recall_.
* - [roc_auc_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_auc_score.html)(y_true, y_score, ...)
  - Calcula el área bajo la curva _ROC_ (_Receiver Operating Characteristic Curve_) a partir de las puntuaciones de predicción.
* - [roc_curve](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_curve.html)(y_true, y_score, ...)
  - Calcula la característica operativa del receptor (ROC).
* - [top_k_accuracy_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.top_k_accuracy_score.html)(y_true, y_score, ...)
  - Puntuación de clasificación _Top-k Accuracy_.
* - [zero_one_loss](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.zero_one_loss.html)(y_true, y_pred, ...)
  - Pérdida de clasificación cero-uno.
```

<br/>

#### Notas de _accuracy_score_

[accuracy_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html): Proporción entre las predicciones correctas y las predicciones totales. Toma un valor entre 1 y 0, entre más alto mejor. No es un buen score en dataset no balanceados.
```python
# Sintaxis de llamada
accuracy_score(y_true, y_pred, *, normalize=True, sample_weight=None)
```
**Parámetros:**
- **y_true** - `array-like`: Valores del _target_ reales. También puede ser _y_test_.
- **y_pred** - `array-like`: Valores del _target_ estimados.
- **normalize** - `bool`: Para indicar que se retorne el número de muestras correctamente clasificadas en lugar de la proporción.
- **sample_weight** - `array-like`: Ponderaciones de las muestras.

<br/>

#### Notas de _classification_report_

[classification_report](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.classification_report.html): Devuelve un reporte que muestra las principales métricas de clasificación (_precision_, _recall_ y _f1-score_) además de _support_ que básicamente indica el número de _samples_ en cada etiqueta.
```python
# Sintaxis de llamada
classification_report(y_true, y_pred, *, labels=None, target_names=None, sample_weight=None, 
                      digits=2, output_dict=False, zero_division='warn')
```
**Parámetros:**
- **y_true** - `array-like`: Valores del target reales.
- **y_pred** - `array-like`: Valores del target estimados.

<br/>

#### Notas de _confusion_matrix_

```{image} ../../images/confussion-matrix.png
:name: confussion-matrix
:width: 300px
:align: center
```

[confusion_matrix](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html): Calcula la matriz de confusión para evaluar la precisión de una clasificación.
```python
# Sintaxis de llamada
confusion_matrix(y_true, y_pred, *, labels=None, sample_weight=None, normalize=None)
```
**Parámetros:**
- **y_true** - `array-like`: Valores del _target_ reales.
- **y_pred** - `array-like`: Valores del _target_ estimados.
- **labels** - `array-like`: Lista de etiquetas para indexar la matriz. Por default es `0, 1`, donde 0 es `False` y 1 es `True`, IMPORTATE: Si se modifica este atributo el _output_ será diferente, por default el de la imagen que se muestra anteriormente.
- **sample_weight** - `array-like`: Ponderaciones de las muestras.
- **normalize** - {'true', 'pred', 'all'}: Normaliza la matriz sobre los valores verdaderos (filas), valores estimados (columnas) o todas.
- En el caso de dos variables se puede extraer los valores de la siguiente manera: <br/> `tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()` <br/> Donde:
    - tn: _true negatives_.
    - fp: _false positives_.
    - fn: _false ngatives_.
    - tp: _true positives_.

**Retorna:**
- `ndarray`.

<br/>

#### Notas de _classification_report_

[roc_auc_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_auc_score.html): Calcula el área bajo la curva _ROC_. Entre más grande mejor el modelo.
```python
# Sintaxis de llamada
roc_auc_score(y_true, y_score, *, average='macro', sample_weight=None, max_fpr=None, 
              multi_class='raise', labels=None)
```
**Parámetros:**
- **y_true** - `ndarray`: Etiquetas binarias reales. 
- **y_score** - `ndarray`: _Scores_ del _target_, podrían ser probabilidades estimadas de cada clase (método `.predict_proba()`), medidas del _non-thresholds_ (del método `.decision_function()`). Si es con `.predict_proba()` se debe pasar solo la columna con las probabilidades de la clase 1, es decir, `X.predict_proba(X_test)[:, 1]`.

**Retorna:**
- `ndarray`.

<br/>

#### Notas de _roc_auc_score_

[roc_auc_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_auc_score.html): : Calcula el área bajo la curva ROC.
```python
# Sintaxis de llamada
roc_auc_score(y_true, y_score, *, average='macro', sample_weight=None, max_fpr=None, multi_class='raise', 
              labels=None)
```
**Parámetros:**
- **y_true** - `ndarray`: Etiquetas binarias reales.
- **y_score** - `ndarray`: Scores del target:
    - Caso binario: Podrían ser probabilidades estimadas de cada clase (método `.predict_proba()`, evaluado en _X_new_ y seleccionando únicamente la primer columna: `: X.predict_proba(X_test)[:, 1]` o medidas del _non-thresholds_ (del método `.decision_function()`).
    - Otros casos revisar documentación.

**Retorna:**
- `ndarray`.

#### Notas de _roc_curve_

[roc_curve](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_curve.html): Calcula el _receiver operating characteristic_ (ROC). Se utiliza estricatamente en tareas de clasificación binaria. Para gráficar se utiliza _fpr_ en el eje _x_ y _tpr_ en el eje _y_.
```python
# Sintaxis de llamada
roc_curve(y_true, y_score, *, pos_label=None, sample_weight=None, drop_intermediate=True)
```
**Parámetros:**
- **y_true** - `ndarray`: Etiquetas binarias reales. Si las etiquetas no son _-1_ y _1_ o _0_ y _1_ entonces se deben de indicar explícitamente en _pos_label_.
- **y_score** - `ndarray`: _Scores_ del _target_, podrían ser probabilidades estimadas de cada clase (método `.predict_proba()`), medidas del _non-thresholds_ (del método `.decision_function()`). Si es con `.predict_proba()` se debe pasar solo la columna con las probabilidades de la clase 1, es decir, `X.predict_proba(X_test)[:, 1]`.

**Retorna:**
- _fpr_: `ndarray`.
- _tpr_: `ndarray`.
- _thresholds_: `ndarray`.

Uso básico:

```python
# Importar función
from sklearn.metrics import roc_curve

# Usando probabilidades
y_pred_prob = est.predict_proba(X_test)[:,1]
fpr, tpr, thresholds = roc_curve(y_test, y_pred_prob)

# Graficar
plt.plot([0, 1], [0, 1], 'k--')
plt.plot(fpr, tpr)
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.show()
```
- Una clasificación binaria podría ser regresión logística.

<br/>

### Clusters

Proporciona métricas para evaluar algoritmos de _clustering_, como el índice de silueta, el coeficiente de correlación de Rand ajustado y la homogeneidad. Estas métricas miden la calidad de los agrupamientos.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [adjusted_mutual_info_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.adjusted_mutual_info_score.html)(labels_true, labels_pred, ...)
  - Información mutua ajustada entre dos _clusters_.
* - [adjusted_rand_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.adjusted_rand_score.html)(labels_true, labels_pred)
  - Índice Rand ajustado al azar.
* - [calinski_harabasz_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.calinski_harabasz_score.html)(X, labels)
  - Calcula la puntuación de Calinski y Harabasz.
* - [cluster.contingency_matrix](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.cluster.contingency_matrix.html)(labels_true, labels_pred, ...)
  - Construye una matriz de contingencia que describe la relación entre las etiquetas.
* - [cluster.pair_confusion_matrix](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.cluster.pair_confusion_matrix.html)(labels_true, labels_pred)
  - Matriz de confusión de pares resultante de dos _clusters_.
* - [completeness_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.completeness_score.html)(labels_true, labels_pred)
  - Calcula la métrica de integridad de un etiquetado de _clusters_ dada una verdad básica.
* - [davies_bouldin_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.davies_bouldin_score.html)(X, labels)
  - Calcula la puntuación de Davies-Bouldin.
* - [fowlkes_mallows_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.fowlkes_mallows_score.html)(labels_true, labels_pred, ...)
  - Mide la similitud de dos _clusters_ de un conjunto de puntos.
* - [homogeneity_completeness_v_measure](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.homogeneity_completeness_v_measure.html)(labels_true, labels_pred, ...)
  - Calcula las puntuaciones de homogeneidad, exhaustividad y _V-Measure_.
* - [homogeneity_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.homogeneity_score.html)(labels_true, labels_pred)
  - Métrica de homogeneidad de un etiquetado de _clusters_ dada una verdad básica.
* - [mutual_info_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mutual_info_score.html)(labels_true, labels_pred, ...)
  - Información mutua entre dos _clusters_.
* - [normalized_mutual_info_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.normalized_mutual_info_score.html)(labels_true, labels_pred, ...)
  - Información mutua normalizada entre dos _clusters_.
* - [rand_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.rand_score.html)(labels_true, labels_pred)
  - Índice Rand.
* - [silhouette_samples](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.silhouette_samples.html)(X, labels, ...)
  - Calcula el coeficiente de silueta de cada muestra.
* - [silhouette_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.silhouette_score.html)(X, labels, ...)
  - Calcula el coeficiente de silueta medio de todas las muestras.
* - [v_measure_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.v_measure_score.html)(labels_true, labels_pred, ...)
  - Etiquetado de _clusters_ con medida _V_ dada una verdad básica.
```

<br/>

### Distancias

Aquí se describen métricas de distancia utilizadas para medir la similitud o disimilitud entre muestras, como la distancia euclidiana, la distancia de Manhattan y la distancia de coseno. Son útiles en _clustering_ y vecinos más cercanos (KNN).

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [DistanceMetric](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.DistanceMetric.html)()
  - Interfaz uniforme para funciones métricas de distancia rápidas (euclidiana, la distancia de Manhattan, entre otras).
```

<br/>

### Interfaz selección de modelo

Herramientas útiles para definir las reglas para evaluar un modelo.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [check_scoring](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.check_scoring.html)(estimator=None, scoring=None, ...)
  - Determina el métrico a partir de las opciones del usuario.
* - [get_scorer](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.get_scorer.html)(scoring)
  - Retorna un métrico de cadena.
* - [get_scorer_names](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.get_scorer_names.html)()
  - Obtiene los nombres de todos los metricos disponibles.
* - [make_scorer](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.make_scorer.html)(score_func, ...)
  - Crea un métrico a partir de una métrica de rendimiento o una función de pérdida.
```

<br/>

### Pares de muestas

Contiene funciones para calcular métricas de similitud o distancia entre pares de muestras, como la matriz de kernel y la matriz de distancias. Estas funciones son útiles en algoritmos que requieren comparaciones por pares.

:::{caution}
Las métricas aquí presentadas son del módulo _pairwise_.
:::

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [pairwise.additive_chi2_kernel](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.additive_chi2_kernel.html)(X, Y=None)
  - Calcula el kernel chi-cuadrado aditivo entre las observaciones en _X_ y _Y_.
* - [pairwise.chi2_kernel](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.chi2_kernel.html)(X, Y=None, gamma=1.0)
  - Calcula el kernel exponencial chi-cuadrado entre _X_ y _Y_.
* - [pairwise.cosine_distances](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_distances.html)(X, Y=None)
  - Calcula la distancia coseno entre las muestras en _X_ y _Y_.
* - [pairwise.cosine_similarity](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html)(X, Y=None, dense_output=True)
  - Calcula la similitud coseno entre las muestras en _X_ y _Y_.
* - [pairwise.distance_metrics](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.distance_metrics.html)()
  - Métricas válidas para _pairwise_distances_.
* - [pairwise.euclidean_distances](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.euclidean_distances.html)(X, Y=None, ...)
  - Calcula la matriz de distancia entre cada par de una matriz de vectores _X_ y _Y_.
* - [pairwise.haversine_distances](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.haversine_distances.html)(X, Y=None)
  - Calcula la distancia Haversine entre las muestras en _X_ y _Y_.
* - [pairwise.kernel_metrics](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.kernel_metrics.html)()
  - Métricas válidas para _pairwise_kernels_.
* - [pairwise.laplacian_kernel](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.laplacian_kernel.html)(X, Y=None, gamma=None)
  - Calcula el kernel laplaciano entre _X_ y _Y_.
* - [pairwise.linear_kernel](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.linear_kernel.html)(X, Y=None, dense_output=True)
  - Calcula el kernel lineal entre _X_ y _Y_.
* - [pairwise.manhattan_distances](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.manhattan_distances.html)(X, Y=None)
  - Calcula las distancias L1 entre los vectores en _X_ y _Y_.
* - [pairwise.nan_euclidean_distances](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.nan_euclidean_distances.html)(X, Y=None, ...)
  - Calcula las distancias euclidianas en presencia de valores perdidos.
* - [pairwise.paired_cosine_distances](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.paired_cosine_distances.html)(X, Y)
  - Calcula las distancias coseno emparejadas entre _X_ y _Y_.
* - [pairwise.paired_distances](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.paired_distances.html)(X, Y, ...)
  - Calcula las distancias emparejadas entre _X_ y _Y_.
* - [pairwise.paired_euclidean_distances](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.paired_euclidean_distances.html)(X, Y)
  - Calcula las distancias euclídeas emparejadas entre _X_ y _Y_.
* - [pairwise.paired_manhattan_distances](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.paired_manhattan_distances.html)(X, Y)
  - Calcula las distancias L1 emparejadas entre _X_ y _Y_.
* - [pairwise.pairwise_kernels](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.pairwise_kernels.html)(X, Y=None, metric='linear', ...)
  - Calcula el kernel entre las matrices _X_ y la matriz opcional _Y_.
* - [pairwise.polynomial_kernel](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.polynomial_kernel.html)(X, Y=None, degree=3, gamma=None, coef0=1)
  - Calcula el kernel polinómico entre _X_ y _Y_.
* - [pairwise.rbf_kernel](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.rbf_kernel.html)(X, Y=None, gamma=None)
  - Calcula el kernel rbf (gaussiano) entre _X_ y _Y_.
* - [pairwise.sigmoid_kernel](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.sigmoid_kernel.html)(X, Y=None, gamma=None, coef0=1)
  - Calcula el kernel sigmoide entre _X_ y _Y_.
* - [pairwise_distances](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances.html)(X, Y=None, metric='euclidean', ...)
  - Calcula la matriz de distancias a partir de una matriz de vectores _X_ y _Y_ opcional.
* - [pairwise_distances_argmin](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances_argmin.html)(X, Y, ...)
  - Calcula distancias mínimas entre un punto y un conjunto de puntos.
* - [pairwise_distances_argmin_min](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances_argmin_min.html)(X, Y, ...)
  - Calcula distancias mínimas entre un punto y un conjunto de puntos.
* - [pairwise_distances_chunked](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances_chunked.html)(X, Y=None, ...)
  - Genera una matriz de distancia trozo a trozo con reducción opcional.
```

<br/>

### Ranking _multilabel_

Esta sección se enfoca en métricas para problemas de clasificación multietiqueta y ranking, como la precisión promedio (_average precision_) y la pérdida de ranking (_ranking loss_). Son útiles cuando cada muestra puede tener múltiples etiquetas.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [coverage_error](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.coverage_error.html)(y_true, y_score, ...)
  - Medida del error de cobertura.
* - [label_ranking_average_precision_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.label_ranking_average_precision_score.html)(y_true, y_score, ...)
  - Calcula la precisión media basada en la clasificación.
* - [label_ranking_loss](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.label_ranking_loss.html)(y_true, y_score, ...)
  - Calcula el ranking de la medida de pérdida.
```

<br/>

### Regresión

Aquí se encuentran métricas para evaluar modelos de regresión, como el error cuadrático medio (MSE), el error absoluto medio (MAE) y el coeficiente de determinación (R²). Estas métricas miden la precisión de las predicciones en problemas de regresión.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [d2_absolute_error_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.d2_absolute_error_score.html)(y_true, y_pred, ...)
  - $D^2$ función de puntuación de regresión, fracción del error absoluto explicado.
* - [d2_pinball_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.d2_pinball_score.html)(y_true, y_pred, ...)
  - $D^2$ función de puntuación de regresión, fracción de pérdida de _pinball_ explicada.
* - [d2_tweedie_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.d2_tweedie_score.html)(y_true, y_pred, ...)
  - $D^2$ función de puntuación de regresión, fracción de desviación de Tweedie explicada.
* - [explained_variance_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.explained_variance_score.html)(y_true, y_pred, ...)
  - Función de puntuación de regresión de la varianza explicada.
* - [max_error](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.max_error.html)(y_true, y_pred)
  - Calcula el error residual máximo.
* - [mean_absolute_error](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_absolute_error.html)(y_true, y_pred, ...)
  - Error absoluto medio de pérdida por regresión.
* - [mean_absolute_percentage_error](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_absolute_percentage_error.html)(y_true, y_pred, ...)
  - Porcentaje medio de error absoluto (MAPE) de pérdida por regresión.
* - [mean_gamma_deviance](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_gamma_deviance.html)(y_true, y_pred, ...)
  - Pérdida por regresión de desviación Gamma media.
* - [mean_pinball_loss](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_pinball_loss.html)(y_true, y_pred, ...)
  - Pérdida de _pinball_ para la regresión cuantílica.
* - [mean_poisson_deviance](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_poisson_deviance.html)(y_true, y_pred, ...)
  - Pérdida por regresión de la desviación media de Poisson.
* - [mean_squared_error](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_error.html)(y_true, y_pred, ...)
  - Pérdida por regresión del error cuadrático medio.
* - [mean_squared_log_error](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_log_error.html)(y_true, y_pred, ...)
  - Pérdida por regresión del error logarítmico cuadrático medio.
* - [mean_tweedie_deviance](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_tweedie_deviance.html)(y_true, y_pred, ...)
  - Pérdida por regresión de la desviación media de Tweedie.
* - [median_absolute_error](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.median_absolute_error.html)(y_true, y_pred, ...)
  - Pérdida por regresión del error absoluto medio.
* - [r2_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html)(y_true, y_pred, ...)
  - $R^2$ (coeficiente de determinación) función de puntuación de regresión.
* - [root_mean_squared_error](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.root_mean_squared_error.html)(y_true, y_pred, ...)
  - Pérdida por regresión del error cuadrático medio.
* - [root_mean_squared_log_error](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.root_mean_squared_log_error.html)(y_true, y_pred, ...)
  - Pérdida por regresión del error logarítmico cuadrático medio.
```

### Notas de _mean_squared_error_

[mean_squared_error](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_error.html): Calcula el MSE (promedio del cuadrado de las diferencias entre las valores reales y las prediciones) de un modelo de regresión. Entre más pequeño mejor (en relación con la escala de los datos).
```python
# Sintaxis de llamada
mean_squared_error(y_true, y_pred, *, sample_weight=None, multioutput='uniform_average')
```
**Parámetros:**
- **y_true** - `array-like`: Valores del target reales. También puede ser y_test.
- **y_pred** - `array-like`: Valores del target estimados.
- **sample_weight** - `array-like`: Ponderaciones de las muestras.