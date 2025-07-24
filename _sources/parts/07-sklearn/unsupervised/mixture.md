# Mixture

Algoritmos de modelado _mixture_. Para importar este módulo o una clase o función específica usar:

```python
# Importar módulo
from sklearn import mixture

# Importar clase específica
from sklearn.mixture import ClassName

# Importar función específica
from sklearn.mixture import func_name
```
- _ClassName_ o _func_name_ es el nombre de la clase o función respectivamente.

:::{note}
Para más información de esta librería visitar la [documentación](https://scikit-learn.org/stable/api/sklearn.mixture.html) de `sklearn`.
:::

<br/>

## Clases

Clases implementadas en el módulo `mixture`.

```{list-table}
:header-rows: 1

* - Clase
  - Descripción
* - [BayesianGaussianMixture](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.BayesianGaussianMixture.html)(, ...)
  - Estimación bayesiana variacional de una mezcla gaussiana.
* - [GaussianMixture](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.GaussianMixture.html)(n_components=1, ...)
  - Mezcla gaussiana.
```

### GaussianMixture

`sklearn.cluster.GaussianMixture()`: Implementa un modelo de mezclas gaussianas (GMM), que asume que los datos están generados por una combinación de distribuciones gaussianas. Útil para clustering probabilístico. Puede servir como alternativa a _K-means_. Es útil para agrupamiento de datos con superposición de _clusters_, estimación de densidades, detección de anomalías.
```python
# Sintaxis de llamada
GaussianMixture(n_components=1, *, covariance_type='full', tol=0.001, reg_covar=1e-06, 
                max_iter=100, n_init=1, init_params='kmeans', weights_init=None, 
                means_init=None, precisions_init=None, random_state=None, 
                warm_start=False, verbose=0, verbose_interval=10)
```
**Parámetros:**
- **n_components** - `int`: Número de componentes mixtos.
- **covariance_type** - {'full', 'tied', 'diag', 'spherical'}: Describe el tipo de parámatros de covarianza a usar. Controla los grados de libertad en la forma de cada _cluster_.

#### Atributos

Atributos de la clase `GaussianMixture`.

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - **converged_**
  - `True` cuando se alcanzó la convergencia del mejor ajuste de EM, `False` de lo contrario.
* - **covariances_**  
  - La covarianza de cada componente del _mixture_. La forma depende del tipo de covarianza: (_n_components_,) si es _'spherical'_, (_n_features_, _n_features_) si es _'tied'_, (_n_components_, _n_features_) si es _'diag'_, (_n_components_, _n_features_, _n_features_) si es _'full'_.
* - **feature_names_in_**
  - Nombres de los _features_ observados durante el ajuste. Definido sólo cuando _X_ tiene nombres que son todos cadenas.
* - **lower_bound_**
  - Valor límite inferior de la _log-likelihood_ (de los datos de entrenamiento con respecto al modelo) del mejor ajuste de EM.
* - **means_**
  - La media de cada componente del _mixture_.
* - **n_features_in_**
  - Número de _features_ vistos durante el ajuste.
* - **n_iter_**
  - Número de pasos utilizados por el mejor ajuste de EM para alcanzar la convergencia.
* - **precisions_**
  - Las matrices de precisión de cada componente del _mixture_.
* - **precisions_cholesky_**
  - La descomposición cholesky de las matrices de precisión de cada componente del _mixture_. 
* - **weights_**
  - Los pesos de cada uno de los componentes del _mixture_.
```

#### Métodos

Métodos de la clase `GaussianMixture`.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [aic](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.GaussianMixture.html#sklearn.mixture.GaussianMixture.aic)(X)
  - Criterio de información de Akaike para el modelo actual en la entrada _X_.
* - [bic](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.GaussianMixture.html#sklearn.mixture.GaussianMixture.bic)(X)
  - Criterio de información bayesiano para el modelo actual sobre la entrada _X_.
* - [fit](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.GaussianMixture.html#sklearn.mixture.GaussianMixture.fit)(X,  y=None)
  - Estima los parámetros del modelo con el algoritmo EM.
* - [fit_predict](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.GaussianMixture.html#sklearn.mixture.GaussianMixture.fit_predict)(X,  y=None)
  - Estima los parámetros del modelo utilizando _X_ y predece las etiquetas para _X_.
* - [predict](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.GaussianMixture.html#sklearn.mixture.GaussianMixture.predict)(X)
  - Predice las etiquetas de las muestras de datos en _X_ utilizando el modelo entrenado.
* - [predict_proba](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.GaussianMixture.html#sklearn.mixture.GaussianMixture.predict_proba)(X)
  - Evalúa la densidad de los componentes de cada muestra.
* - [sample](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.GaussianMixture.html#sklearn.mixture.GaussianMixture.sample)(n_samples=1)
  - Genera muestras aleatorias a partir de la distribución gaussiana ajustada.
* - [score](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.GaussianMixture.html#sklearn.mixture.GaussianMixture.score)(X,  y=None)
  - Calcula la _log-likelihood_ media por muestra de los datos _X_ dados.
* - [score_samples](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.GaussianMixture.html#sklearn.mixture.GaussianMixture.score_samples)(X)
  - Calcula la _log-likelihood_ de cada muestra.
```
