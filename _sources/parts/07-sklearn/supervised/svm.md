# SVM

Implementa Máquinas de Vectores de Soporte (SVM) para clasificación y regresión, útiles para problemas con fronteras de decisión complejas. Para importar este módulo o una clase/función específica usar:

```python
# Importar módulo
from sklearn import svm

# Importar clase específica
from sklearn.svm import ClassName

# Importar función específica
from sklearn.svm import func_name
```
- _ClassName_ o _func_name_ es el nombre de la clase o función respectivamente.

:::{note}
Para más información de esta librería visitar la [documentación](https://scikit-learn.org/stable/api/sklearn.svm.html) de `sklearn`.
:::

<br/>

## Clases

Clases implementadas en el módulo `svm`. 

```{list-table}
:header-rows: 1

* - Clase
  - Descripción
* - [LinearSVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html)(penalty='l2', loss='squared_hinge', ...)
  - Clasificador _Linear Support Vector_.
* - [LinearSVR](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVR.html)(...)
  - Regresor _Linear Support Vector_.
* - [NuSVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVC.html)(...)
  - Clasificador _Nu-Support Vector_.
* - [NuSVR](https://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVR.html)(...)
  - Regresor _Nu-Support Vector_.
* - [OneClassSVM](https://scikit-learn.org/stable/modules/generated/sklearn.svm.OneClassSVM.html)(...)
  - Detección de valores atípicos no supervisados.
* - [SVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html)(...)
  - Clasificador _C-Support Vector_.
* - [SVR](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html)(...)
  - Regresor _Epsilon-Support Vector_.
```

<br/>

### SVC

[SVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html): Implementa Máquinas de Vectores de Soporte (SVM) para problemas de clasificación. Busca encontrar el hiperplano óptimo que separa las clases en el espacio de _features_, incluso en casos no lineales mediante el uso de kernels..
```python
# Sintaxis de llamada
SVC(*, C=1.0, kernel='rbf', degree=3, gamma='scale', coef0=0.0, shrinking=True, 
    probability=False, tol=0.001, cache_size=200, class_weight=None, verbose=False, 
    max_iter=-1, decision_function_shape='ovr', break_ties=False, random_state=None)
```
**Parámetros:**
- **C** - `float`: Parámetro de regularización. Debe ser mayor a cero. Determina la "dureza" del _margin_, para valores altos, las muestras no pueden estar en el _margin_. Para valores bajos las muestras pueden caer dentro del _margin_.
- **kernel** - {'linear', 'poly', 'rbf', 'sigmoid', 'precomputed'}: Especifica el tipo de kernel a ser usado en el algoritmo (la manera como serán separados los _clusters_).
    - 'linear': Equivale a una regresión logística (los _datapoints_ se pueden separar por rectas).
    - 'poly': Equivale a una regresión logística polinomial.
    - 'rbf' (default): Útil cuando los _datapoints_ están en formas de lunas o de círculo contenido uno dentro de otro.
- **gamma** - {'scale', 'auto'} o `float`: Coeficiente del kernel cuando kernel es 'poly', 'rbf' o 'sigmoid'. Valores más altos podrían provocar _overfitting_, valores más bajos generalizan mucho (son muy flexibles).

#### Atributos

Atributos de la clase `SVC`. 

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - **class_weight_**
  - Multiplicadores del parámetro _C_ para cada clase. Calculados a partir del parámetro _class_weight_.
* - **classes_**
  - Las etiquetas de las clases.
* - **coef_**
  - Pesos asignados a los _features_ cuando `kernel="lineal"`.
* - **dual_coef_**
  - Coeficientes duales del vector de soporte en la función de decisión, multiplicados por sus objetivos. Para multiclase, coeficiente para todos los clasificadores 1-vs-1. La disposición de los coeficientes en el caso multiclase es algo no trivial.
* - **feature_names_in_**
  - Nombres de los _features_ observados durante el ajuste. Definido sólo cuando _X_ tiene nombres de rasgos que son todos cadenas.
* - **fit_status_**
  - 0 si está correctamente ajustado, 1 en caso contrario (activará la advertencia).
* - **intercept_**
  - Constantes en la función de decisión.
* - **n_features_in_**
  - Número de _features_ vistos durante el ajuste.
* - **n_iter_**
  - Número de iteraciones ejecutadas por la rutina de optimización para ajustar el modelo. La forma de este atributo depende del número de modelos optimizados, que a su vez depende del número de clases.
* - **n_support_**
  - Número de vectores de soporte para cada clase.
* - **probA_**
  - Parámetro aprendido en el escalado de Platt cuando `probability=True`.
* - **probB_**
  - Parámetro aprendido en el escalado de Platt cuando `probability=True`.
* - **shape_fit_**
  - Matriz de dimensiones del vector de entrenamiento _X_.
* - **support_**
  - Índices de vectores soporte.
* - **support_vectors_**
  - Vectores de soporte. Una matriz vacía si el núcleo está precalculado.
```

#### Métodos

Métodos de la clase `SVC`.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [decision_function](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC.decision_function)(X)
  - Evalúa la función de decisión para las muestras en _X_.
* - [fit](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC.fit)(X,  y,  sample_weight=None)
  - Ajusta el modelo SVM según los datos de entrenamiento dados.
* - [predict](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC.predict)(X)
  - Realiza la clasificación de las muestras en _X_.
* - [predict_log_proba](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC.predict_log_proba)(X)
  - Calcula las probabilidades logarítmicas de los posibles resultados para las muestras en _X_.
* - [predict_proba](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC.predict_proba)(X)
  - Calcula las probabilidades de los posibles resultados de las muestras en _X_.
* - [score](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC.score)(X,  y,  sample_weight=None)
  - Retorna la precisión media en los datos de prueba y etiquetas dados.
```

<br/>

## Funciones

Funciones implementadas en el módulo `svm`. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [l1_min_c](https://scikit-learn.org/stable/modules/generated/sklearn.svm.l1_min_c.html)(X, y, ...)
  - Retorna el límite más bajo para _C_.
```