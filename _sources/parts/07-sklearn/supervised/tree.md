# Tree

Este módulo incluye algoritmos de árboles de decision, tanto de clasificación, como de regression. Para importar este módulo o una función específica usar:

```python
# Importar módulo
from sklearn import tree

# Importar clase específica
from sklearn.tree import ClassName

# Importar función específica
from sklearn.tree import func_name
```
- _ClassName_ o _func_name_ es el nombre de la clase o función respectivamente.

:::{note}
Para más información de este módulo visitar la [documentación](https://scikit-learn.org/stable/api/sklearn.tree.html) de `sklearn`.
:::

<br/>

## Clases

Clases implementadas en el módulo _tree_.

```{list-table}
:header-rows: 1

* - Clase
  - Descripción
* - [DecisionTreeClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html)(...)
  - Un clasificador de árbol de decisión.
* - [DecisionTreeRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html)(...)
  - Un regresor de árbol de decisión.
* - [ExtraTreeClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.tree.ExtraTreeClassifier.html)(...)
  - Un clasificador de árbol extremadamente aleatorizado.
* - [ExtraTreeRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.tree.ExtraTreeRegressor.html)(...)
  - Un regresor de árbol extremadamente aleatorizado.
```

<br/>

### DecisionTreeClassifier

[DecisionTreeClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html): Implementa un árbol de decisión para problemas de clasificación. Divide recursivamente el espacio de _features_ en regiones basadas en reglas de decisión, lo que permite interpretar fácilmente el modelo.
```python
# Sintaxis de llamada
DecisionTreeClassifier(*, criterion='gini', splitter='best', max_depth=None, min_samples_split=2, 
                       min_samples_leaf=1, min_weight_fraction_leaf=0.0, max_features=None, 
                       random_state=None, max_leaf_nodes=None, min_impurity_decrease=0.0, 
                       class_weight=None, ccp_alpha=0.0, monotonic_cst=None)
```
**Parámetros:**
- **criterion** - {'gini', 'entropy'}: Función para medir la impuridad de un nodo.
- **max_depth** - `int`: Profundidad máxima del árbol.
- **min_samples_leaf** - `int` o `float`: Número mínimo de muestras necesarias para dividir un nodo.
- **random_state** - `int` o `RandomState Instance`: Controla la aleatoriedad del estimador. Los _feature_ siempre son permutados aleatoriamente en cada _split_.

#### Uso

La forma básica de usar este clase es la siguiente:

```python
# Importar clase
from sklearn.tree import DecisionTreeClassifier

# Inicializar el modelo
model = DecisionTreeClassifier([criterion, max_depth])

# Ajustar el modelo
model.fit(X, y)

# Predecir etiquetas para nuevos datos
y_pred = model.predict(X_new)  # o X_test

# Predecir probabilidades (si es un problema de clasificación binaria o multiclase)
y_proba = model.predict_proba(X_new)  # Devuelve las probabilidades para cada clase

# Importancia de las características
feature_importances = model.feature_importances_  # Muestra la importancia de cada feature en el modelo
```

<br/>

#### Atributos

Atributos de la clase `DecisionTreeClassifier`. 

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - **classes_**
  - Las etiquetas de las clases (problema de salida única) o un `list` de arreglos de etiquetas de clase (problema de salida múltiples).
* - **feature_importances_**
  - Retorna los _feature importances_.
* - **feature_names_in_**
  - Nombres de los _features_ vistao durante el ajuste. Definido solo cuando _X_ tiene nombres de _features_ que son todos cadenas.
* - **max_features_**
  - El valor inferido de _max_features_.
* - **n_classes_**
  - El número de clases (para problemas de salida individuales), o un `list` que contiene el número de clases para cada salida (para problemas de salida múltiple).
* - **n_features_in_**
  - Número de _features_ vistos durante el ajuste.
* - **n_outputs_**
  - El número de salidas cuando se realiza el ajuste.
* - **tree_**
  - El objeto de árbol subyacente. Consultar `help(sklearn.tree._tree.tree)` para ver los atributos del objeto de árbol y comprender la estructura del árbol de decisión para el uso básico de estos atributos.
```

#### Métodos

Métodos de la clase `DecisionTreeClassifier`. 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [apply](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier.apply)(X,  check_input=True)
  - Retorna el índice del _leaf_ que se predice cada muestra.
* - [cost_complexity_pruning_path](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier.cost_complexity_pruning_path)(X,  y,  sample_weight=None)
  - Calcula el _pruning path_ durante _Minimal Cost-Complexity Pruning_.
* - [decision_path](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier.decision_path)(X,  check_input=True)
  - Retorna el camino de decisión en el árbol.
* - [fit](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier.fit)(X,  y,  sample_weight=None,  check_input=True)
  - Construye un clasificador de árbol de decisión del conjunto de _training_ `(X, y)`.
* - [predict](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier.predict)(X,  check_input=True)
  - Predice el valor de la clase para _X_.
* - [predict_log_proba](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier.predict_log_proba)(X)
  - Predice las _log-probabilities_ de clase de las muestras de entrada _X_.
* - [predict_proba](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier.predict_proba)(X,  check_input=True)
  - Predice las probabilidades de clase de las muestras de entrada _X_.
* - [score](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier.score)(X,  y,  sample_weight=None)
  - Retorna la precisión media en los datos y etiquetas de prueba dados.
```

<br/>

### DecisionTreeRegressor

[DecisionTreeRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html): Similar a `DecisionTreeClassifier`, pero diseñado para problemas de regresión. Predice valores continuos dividiendo el espacio de _features_ en regiones y asignando un valor constante a cada región.
```python
# Sintaxis de llamada
DecisionTreeRegressor(*, criterion='squared_error', splitter='best', max_depth=None, 
                      min_samples_split=2, min_samples_leaf=1, min_weight_fraction_leaf=0.0, 
                      max_features=None, random_state=None, max_leaf_nodes=None, 
                      min_impurity_decrease=0.0, ccp_alpha=0.0, monotonic_cst=None)
```
**Parámetros:**
- **criterion** - {'squared_error', 'friedman_mse', 'absolute_error', 'poisson'}: Función para medir la calidad de cada división de nodo.
- **max_depth** - `int`: Profundidad máxima del árbol.
- **min_samples_leaf** - `int` o `float`: Número mínimo de muestras necesarias para dividir un nodo.
- **random_state** - `int` o `RandomState Instance`: Controla la aleatoriedad del estimador. Los _features_ siempre son permutados aleatoriamente en cada _split_.

#### Uso

La forma básica de usar este clase es la siguiente:

```python
# Importar clase
from sklearn.tree import DecisionTreeRegressor

# Inicializar el modelo
model = DecisionTreeRegressor([criterion, max_depth]) 

# Ajustar el modelo
model.fit(X, y) 

# Predecir valores para nuevos datos
y_pred = model.predict(X_new)  # o X_test

# Importancia de las características
feature_importances = model.feature_importances_  # Muestra la importancia de cada característica en el modelo
```

#### Atributos

Atributos de la clase `DecisionTreeRegressor`. 

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - **feature_importances_**
  - Retorna los _feature importances_.
* - **feature_names_in_**
  - Nombres de los _features_ vistos durante el ajuste. Definido solo cuando _X_ tiene nombres de _features_ que son todos cadenas.
* - **max_features_**
  - El valor inferido de _max_features_.
* - **n_features_in_**
  - Número de _features_ vistos durante el ajuste.
* - **n_outputs_**
  - El número de _outputs_ cuando se realiza el ajuste.
* - **tree_**
  - El objeto de árbol subyacente. Consultar `help(sklearn.tree._tree.tree)` para ver los atributos del objeto de árbol y comprender la estructura del árbol de decisión para el uso básico de estos atributos.
```

#### Métodos

Métodos de la clase `DecisionTreeRegressor`. 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [apply](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor.apply)(X,  check_input=True)
  - Retorna el índice del _leaf_ que se predice cada muestra.
* - [cost_complexity_pruning_path](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor.cost_complexity_pruning_path)(X,  y,  sample_weight=None)
  - Calcula el _pruning path_ durante _Minimal Cost-Complexity Pruning_.
* - [decision_path](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor.decision_path)(X,  check_input=True)
  - Retorna el camino de decisión en el árbol.
* - [fit](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor.fit)(X,  y,  sample_weight=None,  check_input=True)
  - Construye un regresor de árbol de decisión del conjunto de entrenamiento `(X, y)`.
* - [predict](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor.predict)(X,  check_input=True)
  - Predice el valor de regresión para _X_.
* - [score](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor.score)(X,  y,  sample_weight=None)
  - Retorna el coeficiente de determinación de la predicción.
```

<br/>

## Funciones

Funciones implementadas en el módulo _tree_.

### Exportar

Funciones para realizar exportaciones del modelo. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [export_graphviz](https://scikit-learn.org/stable/modules/generated/sklearn.tree.export_graphviz.html)(decision_tree, out_file=None, ...)
  - Exporta un árbol de decisión en formato _DOT_.
* - [export_text](https://scikit-learn.org/stable/modules/generated/sklearn.tree.export_text.html)(decision_tree, ...)
  - Crea un informe de texto que muestre las reglas de un árbol de decisión.
```

### Graficar

Funciones para gráficar el modelo.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [plot_tree](https://scikit-learn.org/stable/modules/generated/sklearn.tree.plot_tree.html)(decision_tree, ...)
  - Grafica un árbol de decisión.
```

#### Notas de _plot_tree_

[plot_tree](https://scikit-learn.org/stable/modules/generated/sklearn.tree.plot_tree.html): Gráfica un árbol de decisión.
```python
# Sintaxis de llamada
plot_tree(decision_tree, *, max_depth=None, feature_names=None, class_names=None, 
          label='all', filled=False, impurity=True, node_ids=False, proportion=False, 
          rounded=False, precision=3, ax=None, fontsize=None)
```
**Parámetros:**
- **decision_tree** - `estimator`: El árbol de decisión a ser graficado.
- **feature_names** - `list de str`: Nombres de cada _feature_.
- **class_names** - `list de str o bool`: Nombres de cada clase en _target_ en orden numérico ascendente. Se puede usar el atributo `.classes_`.
- **impurity** - `bool`: Para indicar si se muestre la impuridad en cada nodo.

<br/>