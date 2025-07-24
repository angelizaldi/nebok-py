# Scikit Learn

_sklearn_ es una librería que se utiliza principalmente para preprocesar, ajustar, evaluar y optimizar modelos de machine learning, supervisados y no supervisados. Es recomendado importar clases o funciones específicas de cada módulo o el módulo completo, en lugar de la librería completa.

Para utilizar _sklearn_ es necesario instalarlo. Desde la terminal usar:
```shell
# Con pip
pip install sklearn

# Con conda
conda install sklearn
```

Una vez instalado se debe de importar
```python
# Importar módulo
from sklearn import ensemble

# Importar clase específica
from sklearn.module_name import ClassName

# Importar función específica
from sklearn.module_name import func_name
``` 
- _module_name_ es el nombre del módulo que se desea importar.
- _ClassName_ o _func_name_ es el nombre de la clase o función respectivamente.

:::{warning}
En este sitio no se recopilan todos los módulos de _sklearn_. Para más información de esta librería visitar la [documentación](https://scikit-learn.org/stable/api/index.html) y [guía de usuario](https://scikit-learn.org/stable/user_guide.html) de _sklearn_.
:::

## Estructura

A continuación se presenta un breve descripción de cómo está estructura esta librería en este sitio.

:::{warning}
A continuación no se enlistan todos los módulo de _scikit-learn_. Para una lista completa visitar la [documentación](https://scikit-learn.org/stable/api/index.html) de _sklearn_.
:::

### Aprendizaje supervisado

En esta sección se encuentran los algoritmos que aprenden a partir de datos etiquetados para hacer predicciones o clasificaciones. Los módulos incluyen modelos lineales (como regresión lineal y logística), árboles de decisión, máquinas de vectores de soporte (SVM), métodos basados en vecinos (KNN) y enfoques probabilísticos como Naive Bayes. También se incluyen técnicas de ensamblaje, como Random Forest y Gradient Boosting, que combinan múltiples modelos para mejorar el rendimiento.

| Módulo            | Descripción                                                                                                                                 |
|----------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| {doc}`ensamble<./supervised/ensamble>`| Contiene métodos de ensamblaje, como Random Forest y Gradient Boosting, que combinan múltiples modelos para mejorar la precisión y robustez. |
| {doc}`linear_model<./supervised/linear_model>`| Implementa modelos lineales, como regresión lineal, regresión logística y Ridge/Lasso, útiles para problemas de regresión y clasificación.|
| {doc}`naive_bayes<./supervised/naive_bayes>`| Implementa el clasificador Naive Bayes, útil para tareas de clasificación, especialmente con datos de texto. |
| {doc}`neighbors<./supervised/neighbors>`| Contiene algoritmos basados en vecinos, como K-Nearest Neighbors (KNN), para clasificación y regresión. |
| {doc}`svm<./supervised/svm>`| Implementa Máquinas de Vectores de Soporte (SVM) para clasificación y regresión, útiles para problemas con fronteras de decisión complejas.|
| {doc}`tree<./supervised/tree>`| Contiene algoritmos basados en árboles, como árboles de decisión y bosques aleatorios, para clasificación y regresión.|

### Aprendizaje no supervisado

Esta sección incluye técnicas que permiten encontrar patrones o estructuras en datos sin etiquetas. Los módulos aquí se centran en _clustering_ (agrupamiento de datos), reducción de dimensionalidad (para simplificar datos manteniendo su esencia) y estimación de densidades probabilísticas. Algunos ejemplos son algoritmos de clustering como _K-Means_, métodos de descomposición como PCA y modelos de mezclas gaussianas.

| Módulo               | Descripción                                                                                                                                 |
|----------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| {doc}`cluster<./unsupervised/cluster>`  | Incluye algoritmos de _clustering_, como _K-Means_ y _DBSCAN_, para agrupar datos en conjuntos basados en similitudes.  |
| {doc}`decomposition<./unsupervised/decomposition>`  | Contiene algoritmos de descomposición de matrices, como PCA y NMF, para reducir la dimensionalidad o extraer _features_ latentes. |
| {doc}`mixture<./unsupervised/mixture>`  | Implementa modelos de mezclas gaussianas (GMM) para clustering y estimación de densidades probabilísticas.  |

### Evaluación y selección del modelo

Esta sección se enfoca en medir el rendimiento de los modelos y seleccionar los mejores. Los módulos proporcionan herramientas para validación cruzada, búsqueda de hiperparámetros, métricas de evaluación (como precisión, _recall_ y _F1-score_) y métodos para seleccionar _features_ relevantes. También incluye estimadores _"dummy"_ que sirven como referencia para comparar modelos más complejos.

| Módulo      | Descripción                                                                                                                                 |
|----------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| {doc}`dummy<./evaluation/dummy>` | Proporciona estimadores _"dummy"_ que realizan predicciones simples, útiles como línea base para comparar modelos más complejos.|
| {doc}`feature_selection<./evaluation/feature_selection>` | Ofrece métodos para seleccionar los _features_ más relevantes de un _dataset_, y eliminación recursiva de _features_. |
| {doc}`metrics<./evaluation/metrics>`  | Proporciona funciones para evaluar el rendimiento de modelos, como precisión, _recall_, _F1-score_ y matrices de confusión.|
| {doc}`model_selection<./evaluation/model_selection>`| Ofrece herramientas para la selección y evaluación de modelos, como validación cruzada, búsqueda de hiperparámetros y división de datos.  |

### Transformaciones

En esta sección se agrupan los módulos que preparan y transforman los datos antes de aplicar modelos de aprendizaje automático. Esto incluye preprocesamiento (escalado, normalización, codificación de variables categóricas), manejo de valores faltantes, extracción de _features_ (especialmente para datos no estructurados como texto) y técnicas de reducción de dimensionalidad no lineal, como _t-SNE_.

| Módulo         | Descripción                                                                                                                                 |
|----------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| {doc}`feature_extraction<./transformations/feature_extraction>`| Proporciona métodos para extraer _features_ de datos no estructurados, como texto o imágenes, utilizando técnicas como _Bag of Words_ o _TF-IDF_. |
| {doc}`impute<./transformations/impute>`| Ofrece herramientas para imputar valores faltantes en los datos, como la imputación por media, mediana o KNN. |
| {doc}`manifold<./transformations/manifold>` | Ofrece técnicas de aprendizaje de variedades, como _t-SNE_ e _Isomap_, para visualización y reducción de dimensionalidad no lineal.|
| {doc}`preprocessing<./transformations/preprocessing>`  | Proporciona herramientas para preprocesar datos, como escalado, normalización, codificación de variables categóricas y manejo de valores faltantes. |

### Pipelines y modelos compuestos

Esta categoría facilita la creación de flujos de trabajo complejos al encadenar múltiples pasos de preprocesamiento y modelado en un solo objeto. Los módulos permiten construir pipelines para automatizar procesos, crear modelos compuestos y diseñar transformadores personalizados. Esto es especialmente útil para mantener un código organizado y realizar validación cruzada de manera eficiente.

| Módulo               | Descripción                                                                                                                                 |
|----------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| {doc}`compose<./pipelines-and-compose/compose>`  | Proporciona herramientas para crear modelos compuestos y transformadores personalizados, útiles para flujos de trabajo avanzados.  |
| {doc}`pipeline<./pipelines-and-compose/pipeline>` | Permite crear pipelines para encadenar múltiples pasos de preprocesamiento y modelos en un solo objeto, facilitando flujos de trabajo complejos. |


<br/>

## Uso

Todos los algoritmos ya sean preprocesamiento, algoritmos supervisados o no supervisados son implementados como clases en _sklearn_ y se denominan _estimators_ El uso común de los _estimators_ es el siguiente.
1. Importar la clase correspondiente a ese modelo. <br/> `from sklearn.module import ClassName`
    - _module_ es el nombre del módulo. Los módulos contienen clases para crear los estimadores y otras utilidades.
    - _ClassName_ es el nombre de la clase (también se pueden importar funciones y otros objetos).
2. Seleccionar los hiperparámetros e inicializar el modelo con los valores deseados. El modelo aún no se aplica, lo único que se realiza en este paso es almacenar el modelo y sus parámetros: <br/> `model = ClassName(hyperparameters)`
    - _hyperparameters_ son los argumentos de los modelos que influyen en la calidad del modelo.
3. Organizar los datos en la matriz de _features_ _X_ y el vector _target_ _y_. Se debe satisfacer que _X_ sea tipo `2D ndarray`, `DataFrame` o `sparse matrix`, mientras que _y_ sea `1D ndarray` o `Series` según _Class_.
4. Dividir la matriz de _features_ y el vector _target_ entre el training y testing data. Este paso no es indispensable, depende de los datos y el contexto en el que se está trabajando: <br/> `X_train, X_test, y_train, y_test = train_test_split(X, y, ...)`
    - _X_ es la matriz de _features_.
    - _y_ es el vector _target_.
5. Ajustar el modelo a los datos utilizando el método `.fit()` de cualquier modelo: <br/> `model.fit(X_train, y_train) # Puede ser solo X y y`
    - No estrictamente se tiene que usar los objetos del _split_, pueden ser otros. 
    - No todos los modelos necesitan dos parámetros. Revisar los parámetros de cada modelo.
6. Aplicar el modelo a nuevos datos. Para supervised learning usualmente se usará el método `.predict()` y para unsupervised learning se utilizarán los métodos `.transform()` o `.predict()`. El método `.transform()` también se utiliza para preprocessing. <br/> `y_pred = model.predict(X_test) # Supervised o unsupervised learning` <br/> `y_pred = model.transform(X_test) # Unsupervised learning`

En resumen se seguirían los siguientes pasos
```python
# Importar la clase
from sklearn.module import ClassName

# Inicializar modelo
model = ClassName(hyperparameters)

# Splitear los datos, opcional
X_train, X_test, y_train, y_test = train_test_split(X, y, ...)

# Ajustar el modelo
model.fit(X_train, y_train) # Puede ser solo X y y

# Aplicar el modelo a nuevos datos
y_pred = model.predict(X_test) # Supervised o unsupervised learning
y_pred = model.transform(X_test) # Unsupervised learning
```

<br/>

---
## Tabla de contenido

```{tableofcontents}
````