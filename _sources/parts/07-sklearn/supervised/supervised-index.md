# Aprendizaje supervisado

En esta sección se encuentran los algoritmos que aprenden a partir de datos etiquetados para hacer predicciones o clasificaciones. Los módulos incluyen modelos lineales (como regresión lineal y logística), árboles de decisión, máquinas de vectores de soporte (SVM), métodos basados en vecinos (KNN) y enfoques probabilísticos como Naive Bayes. También se incluyen técnicas de ensamblaje, como Random Forest y Gradient Boosting, que combinan múltiples modelos para mejorar el rendimiento.

:::{warning}
A continuación no se enlistan todos los módulo de _scikit-learn_ relacionados con aprendizaje supervisado. Para más información visitar la [documentación](https://scikit-learn.org/stable/api/index.html) de `sklearn`.
:::

| Módulo            | Descripción                                                                                                                                 |
|----------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| {doc}`ensamble<./ensamble>`| Contiene métodos de ensamblaje, como Random Forest y Gradient Boosting, que combinan múltiples modelos para mejorar la precisión y robustez. |
| {doc}`linear_model<./linear_model>`| Implementa modelos lineales, como regresión lineal, regresión logística y Ridge/Lasso, útiles para problemas de regresión y clasificación.|
| {doc}`naive_bayes<./naive_bayes>`| Implementa el clasificador Naive Bayes, útil para tareas de clasificación, especialmente con datos de texto. |
| {doc}`neighbors<./neighbors>`| Contiene algoritmos basados en vecinos, como K-Nearest Neighbors (KNN), para clasificación y regresión. |
| {doc}`svm<./svm>`| Implementa Máquinas de Vectores de Soporte (SVM) para clasificación y regresión, útiles para problemas con fronteras de decisión complejas.|
| {doc}`tree<./tree>`| Contiene algoritmos basados en árboles, como árboles de decisión y bosques aleatorios, para clasificación y regresión.|

<br/>

---
## Tabla de contenido

```{tableofcontents}
````