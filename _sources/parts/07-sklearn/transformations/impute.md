# Impute

Ofrece herramientas para imputar valores faltantes en los datos, como la imputación por media, mediana o KNN. Para importar este módulo o una clase o función específica usar:

```python
# Importar módulo
from sklearn import impute

# Importar clase específica
from sklearn.impute import ClassName

# Importar función específica
from sklearn.impute import func_name
```
- _ClassName_ o _func_name_ es el nombre de la clase o función respectivamente.

:::{note}
Para más información de esta librería visitar la [documentación](https://scikit-learn.org/stable/api/sklearn.impute.html) de `sklearn`.
:::

<br/>

## Clases

Clases implementadas en el módulo `impute`.

```{list-table}
:header-rows: 1

* - Clase
  - Descripción
* - [IterativeImputer](https://scikit-learn.org/stable/modules/generated/sklearn.impute.IterativeImputer.html)(estimator=None, ...)
  - Imputador multivariante que estima cada _feature_ a partir de todas las demás.
* - [KNNImputer](https://scikit-learn.org/stable/modules/generated/sklearn.impute.KNNImputer.html)(, ...)
  - Imputación para completar valores perdidos mediante _k-Nearest Neighbors_.
* - [MissingIndicator](https://scikit-learn.org/stable/modules/generated/sklearn.impute.MissingIndicator.html)(, ...)
  - Indicadores binarios para valores perdidos.
* - [SimpleImputer](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html)(, ...)
  - Imputación univariante para completar valores perdidos con estrategias sencillas.
```

<br/>

### SimpleImputer

`sklearn.preprocessing.SimpleImputer()`: Rellena valores faltantes en un dataset utilizando estrategias como la media, mediana, moda o un valor constante. Es útil para la preparación de datos con valores faltantes para modelos de _machine learning_, como regresión o _clustering_.
```python
# Sintaxis de llamada
SimpleImputer(*, missing_values=nan, strategy='mean', fill_value=None, copy=True, 
              add_indicator=False, keep_empty_features=False)
```
**Parámetros:**
- **missing_values** - `int`, `float`, `str`, `np.nan` o `None`: Para indicar la forma como están los `NaN`, pueder ser tal cual `NaN` u otra forma como 0, _NA_, etc.
- **strategy** - {'mean', 'median', 'most_frequent', 'constant'}: Estrategia de imputación.
- **fill_value** - `str` o `numeric`: Valor a utilizar cuando `strategy='contant'`.
- **copy** - `bool`: Para indicar si la imputación sea _in-place_.
- **add_indicator** - `bool`: Para indicar que en el _output_ se agregue un indicador de valores pérdidos.

#### Uso

La forma básica de usar este clase es la siguiente:

```python
# Importar la clase
from sklearn.model_selection import SimpleImputer

# Definir Imputer
imp = SimpleImputer(missing_values='NaN', strategy='mean') # Ejm con 'mean'

# Ajustar imputer
imp.fit(X)

# Aplicar transformación
X = imp.transform(X)
````

#### Atributos

Atributos de la clase `SimpleImputer`.

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - **feature_names_in_**
  - Nombres de las _features_ observados durante el ajuste. Definido sólo cuando _X_ tiene nombres que son todos cadenas.
* - **indicator_**
  - Indicador utilizado para añadir indicadores binarios para los valores que faltan. `None` si `add_indicator=False`.
* - **n_features_in_**
  - Número de _features_ vistos durante el ajuste.
* - **statistics_**
  - El valor de relleno de imputación para cada _feature_. El cálculo de estadísticas puede dar como resultado valores `np.nan`. Durante la transformación, se descartarán los _features_ que correspondan a estadísticas `np.nan`.
```

#### Métodos

Métodos de la clase `SimpleImputer`.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [fit](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html#sklearn.impute.SimpleImputer.fit)(X,  y=None)
  - Ajusta el _imputer_ en _X_.
* - [fit_transform](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html#sklearn.impute.SimpleImputer.fit_transform)(X,  y=None,  **fit_params)
  - Ajusta a los datos, luego los transforma.
* - [inverse_transform](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html#sklearn.impute.SimpleImputer.inverse_transform)(X)
  - Convierte los datos de nuevo a la representación original.
* - [transform](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html#sklearn.impute.SimpleImputer.transform)(X)
  - Imputa todos los valores que faltan en _X_.
```
