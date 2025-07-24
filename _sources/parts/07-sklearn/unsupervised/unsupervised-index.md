# Aprendizaje no supervisado

Esta sección incluye técnicas que permiten encontrar patrones o estructuras en datos sin etiquetas. Los módulos aquí se centran en _clustering_ (agrupamiento de datos), reducción de dimensionalidad (para simplificar datos manteniendo su esencia) y estimación de densidades probabilísticas. Algunos ejemplos son algoritmos de clustering como _K-Means_, métodos de descomposición como PCA y modelos de mezclas gaussianas.

:::{warning}
A continuación no se enlistan todos los módulo de _scikit-learn_ relacionados con aprendizaje no supervisado. Para más información visitar la [documentación](https://scikit-learn.org/stable/api/index.html) de `sklearn`.
:::

| Módulo               | Descripción                                                                                                                                 |
|----------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| {doc}`cluster<./cluster>`  | Incluye algoritmos de _clustering_, como _K-Means_ y _DBSCAN_, para agrupar datos en conjuntos basados en similitudes.  |
| {doc}`decomposition<./decomposition>`  | Contiene algoritmos de descomposición de matrices, como PCA y NMF, para reducir la dimensionalidad o extraer _features_ latentes. |
| {doc}`mixture<./mixture>`  | Implementa modelos de mezclas gaussianas (GMM) para clustering y estimación de densidades probabilísticas.  |


En los algoritmos no supervisados los _datasets_ no se separan en _test_ y _train_, sino que que las predicciones se hacen sobre el mismo _dataset_ que se utilizó para entrenar el modelo o también sobre nuevas muestras.

<br/>

---
## Tabla de contenido

```{tableofcontents}
````