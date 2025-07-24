# Dummy

Proporciona estimadores _"dummy"_ que realizan predicciones simples, útiles como línea base para comparar modelos más complejos. Para importar este módulo o una clase o función específica usar:

```python
# Importar módulo
from sklearn import dummy

# Importar clase específica
from sklearn.dummy import ClassName

# Importar función específica
from sklearn.dummy import func_name
```
- _ClassName_ o _func_name_ es el nombre de la clase o función respectivamente.

:::{note}
Para más información de esta librería visitar la [documentación](https://scikit-learn.org/stable/api/sklearn.dummy.html) de `sklearn`.
:::

<br/>

## Clases

Clases implementadas en el módulo `dummy`.

```{list-table}
:header-rows: 1

* - Clase
  - Descripción
* - [DummyClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.dummy.DummyClassifier.html)(...)
  - Clasificador que realiza predicciones que ignoran los _features_ de entrada.
* - [DummyRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.dummy.DummyRegressor.html)(...)
  - Regresor que realiza predicciones utilizando reglas sencillas.
```

### DummyClassifier

[DummyClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.dummy.DummyClassifier.html): Implementa un clasificador _"dummy"_ que realiza predicciones simples, como predecir siempre la clase mayoritaria o una clase aleatoria. Es útil para establecer una línea base para comparar el rendimiento de modelos más complejos en problemas de clasificación.
```python
# Sintaxis de llamada
DummyClassifier(, strategy='prior', random_state=None, constant=None)
```

**Parámetros:**
- **strategy** - {'most_frequent', 'prior', 'stratified', 'uniform', 'constant'}: Estrategia a usar para hacer las predicciones.
    - _most_frequent_: Siempre retorna la etiqueta más frecuente. Particularmente útil para datos no balanceados.
    - _prior_: Siempre retorna la etiqueta más frecuente.
    - _stratified_: Realiza un muestreo aleatorio de vectores _one-hot_ de una distribución multinomial parametrizada por las probabilidades empíricas a priori de las etiquetas del _target_. Básicamente genera predicciones con base a la distribución de las etiquetas.
    - _uniform_: Genera prediciones uniformes aleatorias de la lista de etiquetas únicas del _target_, de manera que cada etiqueta tenga la misma probabilidad. Por ejemplo en una clasificación binaria cada etiqueta saldrá en aproximadamente el 50%.
    - _constant_: Siempre predice una etiqueta constante proveída por el usuario.
- **random_state** - `int`, `RandomState Instance`: Semilla del generador de números pseudo aleatorios, útil para reproducibilidad.
- **constant** - `int`, `str` o `arraylike (n_outputs)`: La constante en caso de que `strategy='constant'`.

#### Atributos

Atributos de la clase `DummyClassifier`.

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - **class_prior_**
  - Frecuencia de cada clase observada en _y_. En los problemas de clasificación con varias salidas, se calcula independientemente para cada salida.
* - **classes_**
  - Etiquetas de clase únicas observadas en _y_. Para los problemas de clasificación con varias salidas, este atributo es un `list` de matrices, ya que cada salida tiene un conjunto independiente de clases posibles.
* - **feature_names_in_**
  - Nombres de las características observadas durante el ajuste. Definido sólo cuando _X_ tiene nombres que son todos cadenas.
* - **n_classes_**
  - Número de etiquetas para cada salida.
* - **n_features_in_**
  - Número de _features_ observados durante el ajuste.
* - **n_outputs_**
  - Número de salidas.
* - **sparse_output_**
  - `True` si la matriz devuelta por `.predict()` debe estar en formato _CSC_ disperso. Se establece automáticamente en `True` si la entrada y se pasa en formato disperso.
```

#### Métodos

Métodos de la clase `DummyClassifier`.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [fit](https://scikit-learn.org/stable/modules/generated/sklearn.dummy.DummyClassifier.html#sklearn.dummy.DummyClassifier.fit)(X,  y,  sample_weight=None)
  - Ajusta el clasificador de referencia.
* - [predict](https://scikit-learn.org/stable/modules/generated/sklearn.dummy.DummyClassifier.html#sklearn.dummy.DummyClassifier.predict)(X)
  - Realiza la clasificación en los vectores de prueba _X_.
* - [predict_log_proba](https://scikit-learn.org/stable/modules/generated/sklearn.dummy.DummyClassifier.html#sklearn.dummy.DummyClassifier.predict_log_proba)(X)
  - Retorna estimaciones de probabilidad logarítmica para los vectores de prueba _X_.
* - [predict_proba](https://scikit-learn.org/stable/modules/generated/sklearn.dummy.DummyClassifier.html#sklearn.dummy.DummyClassifier.predict_proba)(X)
  - Retorna estimaciones de probabilidad para los vectores de prueba _X_.
* - [score](https://scikit-learn.org/stable/modules/generated/sklearn.dummy.DummyClassifier.html#sklearn.dummy.DummyClassifier.score)(X,  y,  sample_weight=None)
  - Retorna la precisión media en los datos de prueba y etiquetas dados.
```