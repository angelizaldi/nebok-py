# Pipeline

Permite crear _pipelines_ para encadenar múltiples pasos de preprocesamiento y modelos en un solo objeto, facilitando flujos de trabajo complejos. Para importar este módulo o una clase o función específica usar:

```python
# Importar módulo
from sklearn import pipeline

# Importar clase específica
from sklearn.pipeline import ClassName

# Importar función específica
from sklearn.pipeline import func_name
```
- _ClassName_ o _func_name_ es el nombre de la clase o función respectivamente.

:::{note}
Para más información de esta librería visitar la [documentación](https://scikit-learn.org/stable/api/sklearn.pipeline.html) de `sklearn`.
:::

<br/>

## Clases

Clases implementadas en el módulo `pipeline`.

```{list-table}
:header-rows: 1

* - Clase
  - Descripción
* - [FeatureUnion](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.FeatureUnion.html)(transformer_list, ...)
  - Concatena los resultados de varios objetos transformadores.
* - [Pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html)(steps, ...)
  - Una secuencia de transformadores de datos con un predictor final opcional.
```

<br/>


### FeatureUnion

[FeatureUnion](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.FeatureUnion.html): Combina múltiples transformadores en un solo objeto, aplicándolos en paralelo a los datos y concatenando los resultados. Útil para aplicar diferentes transformaciones a un mismo dataset, por ejemplo, aplicar un transformador a _features_ numéricos y otro a _features_ de texto.
```python
# Sintaxis de llamada
FeatureUnion(transformer_list, *, n_jobs=None, transformer_weights=None, verbose=False, 
             verbose_feature_names_out=True)
```
**Parámetros:**
- **transformer_list** - `list` de `2-tuples`: Los `tuples` están conformado por un nombre `str` y un tranformador `estimator`.

#### Atributos

Uso básico de esta clase:

```python
# Importar clase
from sklearn.pipeline import FeatureUnion 

# Aplicar feature union
union = FeatureUnion([
    ('numeric', numeric_transformer),
    ('text', numeric_transformer) ])
```

#### Atributos

Atributos de la clase `FeatureUnion`.

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - **feature_names_in_**
  - Nombres de los _features_ observados durante el ajuste.
* - **n_features_in_**
  - Número de _features_ observados durante el ajuste.
* - **named_transformers**
  - Objeto tipo diccionario, con los siguientes atributos. Atributo de sólo lectura para acceder a cualquier parámetro del transformador por nombre dado por el usuario. Las llaves son nombres de transformadores y los valores son parámetros de transformadores.
```

#### Métodos

Métodos de la clase `FeatureUnion`.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [fit](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.FeatureUnion.html#sklearn.pipeline.FeatureUnion.fit)(X,  y=None,  **fit_params)
  - Ajusta todos los transformadores utilizando _X_.
* - [fit_transform](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.FeatureUnion.html#sklearn.pipeline.FeatureUnion.fit_transform)(X,  y=None,  **params)
  - Ajusta todos los transformadores, transforma los datos y concatena los resultados.
* - [transform](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.FeatureUnion.html#sklearn.pipeline.FeatureUnion.transform)(X,  **params)
  - Transforma _X_ por separado mediante cada transformador, concatena los resultados.
```

<br/>


### Pipeline

[Pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html): Permite encadenar múltiples pasos de preprocesamiento y modelado en un solo objeto. Cada paso es una tupla que contiene un nombre y un transformador o estimador. El _output_ de un paso será el _input_ del siguiente paso. Es útil para la simplificación de flujos de trabajo complejos, como aplicar escalado, selección de _features_ y entrenamiento de modelos en un solo proceso. También facilita la validación cruzada y la reproducción de experimentos.

:::{tip}
Alternativamente se puede usar la función {ref}`make_pipeline() <pipeline-make-pipeline>` que es más simple de usar.
:::

```python
# Sintaxis de llamada
Pipeline(steps, *, transform_input=None, memory=None, verbose=False)
```
**Parámetros:**
- **steps** - `list` de `tuple`: Pasos que serán encadenados. Cada `tuple` consiste de un nombre `str` y un estimador (`estimator` o `transformer` que implemente los métodos `.fit()` o `.transform()`) o un modelo de `XGBoost`. Incluso puede ser otro `Pipeline`.

#### Uso

La forma básica de usar este clase es la siguiente:

```python
# Importar la clase
from sklearn.model_selection import Pipeline

# Inicializar transformadores, estimadores, etc.
imp = Imputer(...) # Ejm con 'Imputer'
encod = Encoder(...) # Ejm con 'Encoder'
scal = Scaler(...) # Ejm con 'Scaler'
... # Inicializar cualquier instancia necesaria
est = Estimator(...)

# Definir los pasos
steps = [('imputation', imp), ('encoding', encod), ('scaling', scal), ..., ('estimator', est)]

# Inicializar Pipeline
pipeline = Pipeline(steps)

# Ajustar Pipeline
pipeline.fit(X_train, y_train)

# Predecir en nuevas muestras
prediction = pipeline.predict(X_test)

# Evaluar el Pipeline
score = pipeline.score(X_test, y_test)
````

#### Atributos

Atributos de la clase `Pipeline`.

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - **classes_**
  - Las etiquetas de las clases.
* - **feature_names_in_**
  - Nombres de los _features_ observados durante el primer paso del método de ajuste.
* - **n_features_in_**
  - Número de _features_ observados durante el primer paso del método de ajuste.
* - **named_steps**
  - Accede a los pasos por nombre.
```

#### Métodos

Métodos de la clase `Pipeline`.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [decision_function](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline.decision_function)(X,  **params)
  - Transforma los datos y aplica la _decision_function_ con el estimador final.
* - [fit](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline.fit)(X,  y=None,  **params)
  - Ajusta el modelo.
* - [fit_predict](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline.fit_predict)(X,  y=None,  **params)
  - Transforma los datos y aplica _fit_predict_ con el estimador final.
* - [fit_transform](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline.fit_transform)(X,  y=None,  **params)
  - Ajusta el modelo y transforma con el estimador final.
* - [inverse_transform](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline.inverse_transform)(X=None,  , ...)
  - Aplica _inverse_transform_ para cada paso en orden inverso.
* - [predict](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline.predict)(X,  **params)
  - Transforma los datos y aplica la predicción con el estimador final.
* - [predict_log_proba](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline.predict_log_proba)(X,  **params)
  - Transforma los datos y aplica _predict_log_proba_ con el estimador final.
* - [predict_proba](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline.predict_proba)(X,  **params).
  - Transforma los datos y aplica _predict_proba_ con el estimador final.
* - [score](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline.score)(X,  y=None,  sample_weight=None,  **params)
  - Transforma los datos y aplica el _score_ con el estimador final.
* - [score_samples](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline.score_samples)(X)
  - Transforma los datos y aplica _score_samples_ con el estimador final.
* - [transform](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline.transform)(X,  **params)
  - Transforma los datos y aplica la transformación con el estimador final.
```

<br/>

## Funciones

Funciones implementadas en el módulo `pipeline`.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [make_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html)(*steps, memory=None, transform_input=None, verbose=False)
  - Construye un `Pipeline` a partir de los estimadores dados.
* - [make_union](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_union.html)(*transformers, n_jobs=None, verbose=False)
  - Construye un `FeatureUnion` de los transformadores dados.
```

<br/>

(pipeline-make-pipeline)=
### Notas de _make_pipeline_


[make_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html): Construye un `Pipeline` con los modelos dados. Es una versión más sencilla que `Pipeline()`, no se le ponen nombres a cada paso, sus nombres serán los nombres de cada clase en minúsculas.
```python
# Sintaxis de llamada
make_pipeline(*steps, memory=None, transform_input=None, verbose=False)
```
**Parámetros:**
- **steps**: Estimadores (modelos), con sus respectivos parámetros, solo separar por coma cada estimador. También puede ser un modelo de `XGBoost`.

**Retorna:**
- `Pipeline`