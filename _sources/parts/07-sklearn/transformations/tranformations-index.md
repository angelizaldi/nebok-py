# Transformaciones

En esta sección se agrupan los módulos que preparan y transforman los datos antes de aplicar modelos de aprendizaje automático. Esto incluye preprocesamiento (escalado, normalización, codificación de variables categóricas), manejo de valores faltantes, extracción de _features_ (especialmente para datos no estructurados como texto) y técnicas de reducción de dimensionalidad no lineal, como _t-SNE_.

| Módulo         | Descripción                                                                                                                                 |
|----------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| {doc}`feature_extraction<./feature_extraction>`| Proporciona métodos para extraer _features_ de datos no estructurados, como texto o imágenes, utilizando técnicas como _Bag of Words_ o _TF-IDF_. |
| {doc}`impute<./impute>`| Ofrece herramientas para imputar valores faltantes en los datos, como la imputación por media, mediana o KNN. |
| {doc}`manifold<./manifold>` | Ofrece técnicas de aprendizaje de variedades, como _t-SNE_ e _Isomap_, para visualización y reducción de dimensionalidad no lineal.|
| {doc}`preprocessing<./preprocessing>`  | Proporciona herramientas para preprocesar datos, como escalado, normalización, codificación de variables categóricas y manejo de valores faltantes. |

<br/>

---
## Tabla de contenido

```{tableofcontents}
````