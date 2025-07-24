# Naive bayes

Este modulo implementa algoritmos de _Naive Bayes_, que son métodos de _supervised learning_ basados en el teorema de Bayes con supuestos de la independencia de los _features_. Es necesario un modelo generador que especifica el proceso aleatorio hipotético que genera los datos para cada _label_. Para importar este módulo o una función específica usar:

```python
# Importar módulo
from sklearn import naive_bayes

# Importar clase específica
from sklearn.naive_bayes import ClassName

# Importar función específica
from sklearn.naive_bayes import func_name
```
- _ClassName_ o _func_name_ es el nombre de la clase o función respectivamente.

:::{note}
Para más información de este módulo visitar la [documentación](https://scikit-learn.org/stable/api/sklearn.naive_bayes.html) de `sklearn`.
:::

<br/>

## Clases

```{list-table}
:header-rows: 1

* - Clase
  - Descripción
* - [BernoulliNB](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.BernoulliNB.html)(...)
  - Clasificador _naive_ de Bayes para modelos multivariados de Bernoulli.
* - [CategoricalNB](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.CategoricalNB.html)(...)
  - Clasificador _naive_ de Bayes para features categóricas.
* - [ComplementNB](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.ComplementNB.html)(...)
  - Clasificador _naive_ de Bayes de complemento descrito en Rennie et al. (2003).
* - [GaussianNB](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html)(...)
  - _Gaussian Naive Bayes_.
* - [MultinomialNB](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.MultinomialNB.html)(...)
  - Clasificador _naive_ de Bayes para modelos multinomiales.
```

### GaussianNB

[GaussianNB](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html): Implementa el clasificador _Naive Bayes_ basado en la distribución gaussiana (normal). Asume que las características siguen una distribución normal y es eficiente para problemas de clasificación, especialmente con datos continuos.
```python
# Sintaxis de llamada
GaussianNb(*, priors=None, var_smoothing=1e-09)
```

#### Atributos

Atributos de la clase `GaussianNB`.

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - **class_count_**
  - Número de muestras de entrenamiento observadas en cada clase.
* - **class_prior_**
  - Probabilidad de cada clase.
* - **classes_**
  - Etiquetas de clase conocidas por el clasificador.
* - **epsilon_**
  - Valor aditivo absoluto a las desviaciones.
* - **feature_names_in_**
  - Nombres de las _features_ observadas durante el ajuste. Definido sólo cuando _X_ tiene nombres de rasgos que son todos cadenas. 
* - **n_features_in_**
  - Número de _features_ vistos durante el ajuste.
* - **theta_**
  - Media de cada _feature_ por clase.
* - **var_**
  - Varianza de cada _feature_ por clase.
```

#### Métodos

Métodos de la clase `GaussianNB`.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [fit](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html#sklearn.naive_bayes.GaussianNB#sklearn.naive_bayes.GaussianNB.fit)(X,  y,  sample_weight=None)
  - Ajusta el modelo _Gaussian Naive Bayes_ a _X, y_.
* - [partial_fit](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html#sklearn.naive_bayes.GaussianNB#sklearn.naive_bayes.GaussianNB.partial_fit)(X,  y,  classes=None,  sample_weight=None)
  - Ajuste incremental en un lote de muestras.
* - [predict](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html#sklearn.naive_bayes.GaussianNB#sklearn.naive_bayes.GaussianNB.predict)(X)
  - Realiza la clasificación en una matriz de vectores de prueba _X_.
* - [predict_joint_log_proba](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html#sklearn.naive_bayes.GaussianNB#sklearn.naive_bayes.GaussianNB.predict_joint_log_proba)(X)
  - Retorna estimaciones conjuntas de probabilidad logarítmica para el vector de prueba _X_.
* - [predict_log_proba](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html#sklearn.naive_bayes.GaussianNB#sklearn.naive_bayes.GaussianNB.predict_log_proba)(X)
  - Retorna estimaciones de probabilidad logarítmica para el vector de prueba _X_.
* - [predict_proba](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html#sklearn.naive_bayes.GaussianNB#sklearn.naive_bayes.GaussianNB.predict_proba)(X)
  - Retorna estimaciones de probabilidad para el vector de prueba _X_.
* - [score](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html#sklearn.naive_bayes.GaussianNB#sklearn.naive_bayes.GaussianNB.score)(X,  y,  sample_weight=None)s
  - Retorna la precisión media en los datos de prueba _y_.
```
