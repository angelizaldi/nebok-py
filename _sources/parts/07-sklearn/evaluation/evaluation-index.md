# Evaluación y selección del modelo

Esta sección se enfoca en medir el rendimiento de los modelos y seleccionar los mejores. Los módulos proporcionan herramientas para validación cruzada, búsqueda de hiperparámetros, métricas de evaluación (como precisión, _recall_ y _F1-score_) y métodos para seleccionar _features_ relevantes. También incluye estimadores _"dummy"_ que sirven como referencia para comparar modelos más complejos.

| Módulo      | Descripción                                                                                                                                 |
|----------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| {doc}`dummy<./dummy>` | Proporciona estimadores _"dummy"_ que realizan predicciones simples, útiles como línea base para comparar modelos más complejos.|
| {doc}`feature_selection<./feature_selection>` | Ofrece métodos para seleccionar los _features_ más relevantes de un _dataset_, y eliminación recursiva de _features_. |
| {doc}`metrics<./metrics>`  | Proporciona funciones para evaluar el rendimiento de modelos, como precisión, _recall_, _F1-score_ y matrices de confusión.|
| {doc}`model_selection<./model_selection>`| Ofrece herramientas para la selección y evaluación de modelos, como validación cruzada, búsqueda de hiperparámetros y división de datos.  |


<br/>

---
## Tabla de contenido

```{tableofcontents}
````