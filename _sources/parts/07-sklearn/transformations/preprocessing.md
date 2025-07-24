# Preprocessing

Proporciona herramientas para preprocesar datos, como escalado, normalización, codificación de variables categóricas y manejo de valores faltantes.
- **Escalado**: Consiste en ajustar los valores numéricos de las variables a un rango específico, como _\[0,1]_ o una distribución con media 0 y desviación estándar 1. Se usa para evitar que _features_ con valores grandes dominen a otras más pequeñas en modelos sensibles a la magnitud (como regresión logística o redes neuronales).
- **Normalización**: Se refiere a transformar los datos para que tengan una distribución específica (por ejemplo, una distribución normal). A veces se usa como sinónimo de escalado, pero puede incluir técnicas como transformación logarítmica o _Box-Cox_ para hacer que los datos se ajusten mejor a una distribución normal.
- **Codificación de variables categóricas**: Convierte variables categóricas en valores numéricos para que puedan ser utilizadas en modelos de machine learning. Métodos comunes incluyen:
    - _One-Hot Encoding_: Crea una columna binaria para cada categoría.
    - _Label Encoding_: Asigna un número entero a cada categoría.
    - _Target Encoding_: Sustituye cada categoría por la media del target en esa categoría.
- **Manejo de valores faltantes**: Se refiere a tratar datos ausentes en un dataset. Algunas estrategias incluyen:
    - Eliminación de filas o columnas (si hay muchos valores faltantes).
    - Imputación con media, mediana o moda (para datos numéricos o categóricos).
    - Modelado de imputación (como _KNN Imputer_ o regresión). Ver {doc}`./impute`.

Para importar este módulo o una clase o función específica usar:

```python
# Importar módulo
from sklearn import preprocessing

# Importar clase específica
from sklearn.preprocessing import ClassName

# Importar función específica
from sklearn.preprocessing import func_name
```
- _ClassName_ o _func_name_ es el nombre de la clase o función respectivamente.

:::{note}
Para más información de esta librería visitar la [documentación](https://scikit-learn.org/stable/api/sklearn.preprocessing.html) de `sklearn`.
:::

<br/>

## Clases

Clases implementadas en el módulo `preprocessing`.

```{list-table}
:header-rows: 1

* - Clase
  - Descripción
* - **Escalado y Normalización**
  -
* - [KernelCenterer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.KernelCenterer.html)()
  - Centra una matriz de núcleo arbitraria _K_.
* - [MaxAbsScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MaxAbsScaler.html)(...)
  - Escala cada _feature_ por su valor absoluto máximo.
* - [MinMaxScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html)(feature_range=(0, 1), ...)
  - Transforma las _features_ escalando cada una de ellas a un rango determinado.
* - [Normalizer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.Normalizer.html)(norm='l2', ...)
  - Normaliza las muestras individualmente a la norma unitaria.
* - [PowerTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PowerTransformer.html)(method='yeo-johnson', ...)
  - Aplica una transformada de potencia en función de las _features_ para que los datos sean más gaussianos.
* - [RobustScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.RobustScaler.html)(...)
  - Escala las _features_ utilizando estadísticas robustas a los valores atípicos.
* - [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html)(...)
  - Estandariza las _features_ eliminando la media y escalando a la varianza unitaria.
* - **Codificación de Variables Categóricas**
  - 
* - [Binarizer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.Binarizer.html)(...)
  - Binariza los datos (establecer los valores de las _features_ en 0 o 1) según un umbral.
* - [LabelBinarizer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelBinarizer.html)(...)
  - Binariza las etiquetas de forma _one-vs-all_.
* - [LabelEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html)()
  - Codifica etiquetas del _target_ con valor entre 0 y _n_classes-1_.
* - [MultiLabelBinarizer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MultiLabelBinarizer.html)(...)
  - Transformación entre iterable de iterables y un formato multietiqueta.
* - [OneHotEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html)(...)
  - Codifica las _features_ categóricas como una matriz numérica _one-hot_.
* - [OrdinalEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OrdinalEncoder.html)(...)
  - Codifica las _features_ categóricas como una matriz de enteros.
* - [TargetEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.TargetEncoder.html)(categories='auto', target_type='auto', ...)
  - Codificador de _targets_ para _targets_ de regresión y clasificación.
* - **Transformaciones de _Features_**
  - 
* - [FunctionTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.FunctionTransformer.html)(func=None, inverse_func=None, ...)
  - Construye un transformador a partir de un `callable` arbitrario.
* - [KBinsDiscretizer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.KBinsDiscretizer.html)(n_bins=5, ...)
  - Divide los datos continuos en intervalos.
* - [PolynomialFeatures](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html)(degree=2, ...)
  - Genera _features_ polinómicas y de interacción.
* - [QuantileTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.QuantileTransformer.html)(...)
  - Transforma _features_ utilizando información de cuantiles.
* - [SplineTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.SplineTransformer.html)(n_knots=5, degree=3, ...)
  - Genera bases _B-spline_ univariantes para las _features_.
```

<br/>

### FunctionTransformer

[FunctionTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.FunctionTransformer.html): Aplica una función personalizada a los datos durante el preprocesamiento. Útil para transformaciones específicas que no están cubiertas por otras clases. Cualquier función que se use tendrá los métodos `.fit()` y `.transform()` disponibles. Es útil para transformaciones personalizadas, como logaritmos, exponenciales o funciones definidas por el usuario y para permitir que cualquier función se convierta en un objeto de un `Pipeline` pueda procesar.
```python
# Sintaxis de llamada
FunctionTransformer(func=None, inverse_func=None, *, validate=False, accept_sparse=False, 
                    check_inverse=True, feature_names_out=None, kw_args=None, 
                    inv_kw_args=None)
```
**Parámetros:**
- **func** - `callable`: Función a usar para la transformación. La función debe recibir una matriz de _(n_samples, n_features)_ y retornar una matriz que mantenga el número de _samples_, pero potencialmente cambiando los _features_.
- **inverse_func** - `callable`: Función a usar para la inversa de la transformación.
- **validate** - `bool`: Indica si se debe verificar la matriz de entrada _X_ antes de llamar a _func_.
    - `False`: No hay validación de entrada.
    - `True`: _X_ se convertirá en una matriz dispersa o matriz de _numpy_ bidimensional. Si la conversión no es posible, se genera una excepción.

#### Uso

Uso básico de esta clase:

```python
# Importar clase
from sklearn.preprocessing import FunctionTransformer

# Crear estimator personalizado con lambda
my_transformer = FunctionTransformer(lambda x: ...)

# Crear estimator personalizado con función
def my_function(df, ...):
    # data body
    return X # X debe ser una matriz con n_samples
my_transformer = FunctionTransformer(my_function)
```

#### Atributos

Atributos de la clase `FunctionTransformer`.

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - **feature_names_in_**
  - Nombres de los _features_ observados durante el ajuste. Definido sólo cuando _X_ tiene nombres que son todos cadenas.
* - **n_features_in_**
  - Número de _features_ vistos durante el ajuste.
```

#### Métodos

Métodos de la clase `FunctionTransformer`.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [fit](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.FunctionTransformer.html#sklearn.preprocessing.FunctionTransformer.fit)(X,  y=None)
  - Ajusta el transformador comprobando _X_.
* - [fit_transform](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.FunctionTransformer.html#sklearn.preprocessing.FunctionTransformer.fit_transform)(X,  y=None,  **fit_params)
  - Ajusta a los datos, luego los transformar.
* - [inverse_transform](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.FunctionTransformer.html#sklearn.preprocessing.FunctionTransformer.inverse_transform)(X)
  - Transforma _X_ utilizando la función inversa.
* - [transform](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.FunctionTransformer.html#sklearn.preprocessing.FunctionTransformer.transform)(X)
  - Transforma _X_ utilizando la función _forward_.
```

<br/>

### LabelEncoder

[LabelEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html): Convierte valores categóricos en valores entre 0 y _n_classes - 1_. En esta transformación se debe de usar en el _target_ y no en los _feature_. Es útil par codificación de etiquetas para problemas de clasificación, como en árboles de decisión o SVM.
```python
# Sintaxis de llamada
LabelEnconder()
```
**Parámetros:**
- No tiene argumentos.

#### Atributos

Atributos de la clase `LabelEncoder`.

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - **classes_**
  - Las etiquetas de las clases.
```

#### Métodos

Métodos de la clase `LabelEncoder`.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [fit](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html#sklearn.preprocessing.LabelEncoder.fit)(y)
  - Ajusta codificador de etiquetas.
* - [fit_transform](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html#sklearn.preprocessing.LabelEncoder.fit_transform)(y)
  - Ajusta el codificador de etiquetas y devuelve las etiquetas codificadas.
* - [inverse_transform](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html#sklearn.preprocessing.LabelEncoder.inverse_transform)(y)
  - Retorna las etiquetas a la codificación original.
* - [transform](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html#sklearn.preprocessing.LabelEncoder.transform)(y)
  - Transforma etiquetas a codificación normalizada.
```

<br/>

### MinMaxScaler

[MinMaxScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html): Escala _features_ a un rango específico (por defecto, _\[0, 1]_) restando el mínimo y dividiendo por el rango. Es útil para preparación de datos para modelos sensibles a la escala, como redes neuronales o algoritmos basados en distancias.
```python
# Sintaxis de llamada
MinMaxScaler(feature_range=(0, 1), *, copy=True, clip=False)
```
**Parámetros:**
- **feature_range** - `2-tuple`: Valores mínimo y máximo del rango de los datos transformados.
- **copy** - `bool`: Realiza la transformación _in-place_, en lugar de retornar un nuevo objeto.

#### Atributos

Atributos de la clase `MinMaxScaler`.

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - **data_max_**
  - Valor máximo visto en los datos por cada _feature_.
* - **data_min_**
  - Valor mínimo visto en los datos por cada _feature_.
* - **data_range_**
  - Rango (_data_max\__ - _data_min\__) visto en los datos por cada _feature_.
* - **feature_names_in_**
  - Nombres de los _features_ observados durante el ajuste. Definido sólo cuando _X_ tiene nombres que son todos cadenas.
* - **min_**
  - Ajusta para el mínimo por cada _feature_.. Equivale a `min - X.min(axis=0) * self.scale_`.
* - **n_features_in_**
  - Número de _features_ vistos durante el ajuste.
* - **n_samples_seen_**
  - El número de muestras procesadas por el estimador. Se restablecerá en las nuevas llamadas al ajuste, pero se incrementa en las llamadas a _partial_fit_.
* - **scale_**
  - Escala relativa de los datos por cada _feature_. Equivalente a `(max - min) / (X.max(axis=0) - X.min(axis=0))`.
```

#### Métodos

Métodos de la clase `MinMaxScaler`.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [fit](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html#sklearn.preprocessing.MinMaxScaler.fit)(X,  y=None)
  - Calcula el mínimo y el máximo que se utilizarán para el escalado posterior.
* - [fit_transform](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html#sklearn.preprocessing.MinMaxScaler.fit_transform)(X,  y=None,  **fit_params)
  - Ajusta a los datos, luego los transforma.
* - [inverse_transform](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html#sklearn.preprocessing.MinMaxScaler.inverse_transform)(X)
  - Deshace la escala de _X_ según _feature_range_.
* - [partial_fit](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html#sklearn.preprocessing.MinMaxScaler.partial_fit)(X,  y=None)
  - Cálculo de mínimos y máximos en _X_ para su posterior escalado.
* - [transform](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html#sklearn.preprocessing.MinMaxScaler.transform)(X)
  - Escala los _features_ de _X_ según _feature_range_.
```

<br/>

### Normalizer

[Normalizer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.Normalizer.html): Normaliza muestras individuales (filas) para que tengan una norma unitaria (por ejemplo, norma L1 o L2). Es útil para preprocesamiento de datos para algoritmos sensibles a la magnitud, como KNN o _clustering_.
```python
# Sintaxis de llamada
Normalizer(norm='l2', *, copy=True)
```
**Parámetros:**
- **norm** - {'l1', 'l2', 'max'}: Norma a utilizar para normalizar cada muestra diferente de cero.

#### Atributos

Atributos de la clase `Normalizer`.

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - **feature_names_in_**
  - Nombres de los _features_ observados durante el ajuste. Definido sólo cuando _X_ tiene nombres que son todos cadenas.
* - **n_features_in_**
  - Número de _features_ vistos durante el ajuste.
```

#### Métodos

Métodos de la clase `Normalizer`.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [fit](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.Normalizer.html#sklearn.preprocessing.Normalizer.fit)(X,  y=None)
  - Sólo valida los parámetros del estimador.
* - [fit_transform](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.Normalizer.html#sklearn.preprocessing.Normalizer.fit_transform)(X,  y=None,  **fit_params)
  - Ajusta a los datos, luego los transformar.
* - [transform](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.Normalizer.html#sklearn.preprocessing.Normalizer.transform)(X,  copy=None)
  - Escala cada fila no nula de _X_ a norma unitaria.
```

<br/>

### OneHotEncoder

[OneHotEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html): Convierte variables categóricas en una matriz binaria (_one-hot encoding_), donde cada categoría se representa como un vector binario. Crea columnas nuevas por cada categoría, donde cada columna indica con valores `bool` si la fila contenía esa categoría. Útil cuando las categorías no están jerarquizadas. No se recomineda usar si una columna tiene más de 15 categorías distintas. **IMPORTANTE**: por default retornará un arreglo `sparse`. Es útil para codificación de categorías nominales para modelos como regresión logística o redes neuronales.

:::{tip}
Alternativamente se podría usar la función `.get_dummies()` de _pandas_. Revisar {ref}`pd-function-data-manipulation`.
:::

```python
# Sintaxis de llamada
OneHotEncoder(*, categories='auto', drop=None, sparse_output=True, dtype='numpy.float64', 
              handle_unknown='error', min_frequency=None, max_categories=None, 
              feature_name_combiner='concat')
```
**Parámetros:**
- **categories - {'auto'} o `list` de `array-like`: Categorías por _feature_.
    - 'auto': Se determinan las categorías automáticamente.
    - list: Para indicar manualmente las categoriás de cada _feature_ (empatadas por posición).
- **drop** - {'first', 'if_binary'} o `array-like`: Para especificar cómo eliminar una categoría por cada _feature_.
    - 'first': Elimina la primer categoría.
    - 'if_binary': Elimina la primer categoría en _features_ que solo tienen dos categorías.
    - `array-like`: Para indicar cada categoría a eliminar de cada _feature_.
- **sparse** - `bool`: Para indicar que se retorne una matriz `sparse` (`True`) o un `ndarray` (`False`).
- **dtype** - `bool`: El tipo de dato deseado del _output_.
- **handle_unknown** - {'error', 'ignore'}: Para indicar si arrojar un error o si ignorar cuando hay un _feature_ categórico desconocido durante la transformación (que no estaba cuando se ajustó con el método `.fit()`).

#### Atributos

Atributos de la clase `OneHotEncoder`.

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - **categories_**
  - Las categorías de cada _feature_ determinados durante el ajuste (en orden de los _features_ en _X_ y correspondientes con la salida de la transformación). Esto incluye la categoría especificada en _drop_ (si existe).
* - **drop_idx_**
  - `drop_idx_[i]` es el índice en `categories_[i]` de la categoría que debe eliminarse para cada _feature_. `drop_idx_[i] = None` si no debe eliminarse ninguna categoría del _feature_ con índice _i_, por ejemplo cuando `drop='if_binary'` y el _feature_ no es binario. `drop_idx_ = None` si se conservarán todas los _features_ transformados.
* - **feature_name_combiner**
  - `callable` con el _signature_ `def callable(input_feature, category)` que devuelve una cadena. Se utiliza para crear nombres de _features_ que serán devueltos por `get_feature_names_out()`.
* - **feature_names_in_**
  - Nombres de los _features_ observados durante el ajuste. Definido sólo cuando _X_ tiene nombres que son todos cadenas.
* - **infrequent_categories_**
  - Categorías poco frecuentes para cada _feature_.
* - **n_features_in_**
  - Número de _features_ vistos durante el ajuste.
```

#### Métodos

Métodos de la clase `OneHotEncoder`.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [fit](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder.fit)(X,  y=None)
  - Ajusta `OneHotEncoder` a _X_.
* - [fit_transform](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder.fit_transform)(X,  y=None,  **fit_params)
  - Ajusta a los datos, luego los transforma.
* - [inverse_transform](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder.inverse_transform)(X)
  - Convierte los datos de nuevo a la representación original.
* - [transform](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder.transform)(X)
  - Transforma _X_ utilizando la codificación _one-hot_.
```

<br/>

### OrdinalEncoder

[OrdinalEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OrdinalEncoder.html): Convierte variables categóricas en valores enteros ordinales (por ejemplo, "bajo", "medio", "alto" a 0, 1, 2). Útil cuando los valores de las categorías pueden ser jerarquizados. Por default esta función no puede determinar la jerarquía de las categorías, para ello utiliza el parámetro _categories_. Es útil para codificación de categorías ordinales para modelos que requieren entradas numéricas, como árboles de decisión.
```python
# Sintaxis de llamada
OrdinalEncoder(*, categories='auto', dtype='numpy.float64', handle_unknown='error', 
               unknown_value=None, encoded_missing_value=nan, min_frequency=None, 
               max_categories=None)
```
**Parámetros:**
- **categories** - {'auto'} o `list` de `array-like`: Categorías por _feature_.
    - 'auto': Se determinan las categorías automáticamente.
    - `array-like`: Para indicar manualmente las categoriás de cada _feature_ (empatadas por posición). Las categorías numéricas deben de estar ordenadas.
- **dtype** - `dtype`: El tipo de dato deseado del output.
- **handle_unknown** - {'error', 'use_encoded_value}: Para indicar si arrojar un error o si asignar el valor contenido en _unknown_value_ cuando hay un _feature_ categórico desconocido durante la transformación (que no estaba cuando se ajustó con el método `.fit()`).
- **unknown_value** - `int` o `np.nan`: Valor a usar cuando `handle_unknown='used_encoded_value'`. Debe de ser un valor distinto a cualquier usado para las otras categorías. Se puede usar -1.

#### Atributos

Atributos de la clase `OrdinalEncoder`.

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - **categories_**
  - Las categorías de cada _feature_ determinados durante el ajuste (en orden de los _features_ en _X_ y correspondientes con la salida de la transformación). Esto incluye la categoría especificada en _drop_ (si existe).
* - **feature_names_in_**
  - Nombres de los _features_ observados durante el ajuste. Definido sólo cuando _X_ tiene nombres que son todos cadenas.
* - **infrequent_categories_**
  - Categorías poco frecuentes por cada _feature_.
* - **n_features_in_**
  - Número de _features_ vistos durante el ajuste.
```

#### Métodos

Métodos de la clase `OrdinalEncoder`.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [fit](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#sklearn.preprocessing.OrdinalEncoder.fit)(X,  y=None)
  - Ajusta el `OrdinalEncoder` a _X_.
* - [fit_transform](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#sklearn.preprocessing.OrdinalEncoder.fit_transform)(X,  y=None,  **fit_params)
  - Ajusta a los datos, luego los transformar.
* - [inverse_transform](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#sklearn.preprocessing.OrdinalEncoder.inverse_transform)(X)
  - Convierte los datos de nuevo a la representación original.
* - [transform](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#sklearn.preprocessing.OrdinalEncoder.transform)(X)
  - Transforma _X_ en códigos ordinales.
```

<br/>

### PolynomialFeatures

[PolynomialFeatures](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html): Genera una nueva matriz de los _feature_, que consiste en todas las combinaciones polinomiales de los _features_ con un grado menor o igual al grado especificado, es decir, para cada valor de cada _feature_ cálcula $x^2$, $x^3$, etc, hasta el grado que se indique, también puede generar _features_ que son interacciones entre otros _features_ por ejemplo $x_1*x_2$. Es útil para ajustar regresiones de un grado mayor a uno con `LinearRegression()`. Es útil para mejorar modelos lineales al incluir interacciones y términos no lineales, como en regresión polinómica. **IMPORTANTE**: Puede provocar _overfitting_.
```python
# Sintaxis de llamada
PolynomialFeatures(degree=2, *, interaction_only=False, include_bias=True, order='C')
```

**Parámetros:**
- **degree** - `int`: El grado de los _features_ polinomiales.
- **interaction_only** - `bool`: Si es `True`, solo se producen funciones de interacción que no incluyen al grado mayor de cada _feature_.
- **include_bias** - `bool`: Para indicar si incluir una columnas _'bias'_, un _feature_ en el que todas las potencias polinomiales son cero (una columna de unos). Si se quiere usar `LinearRegression()` para ajustar un modelo a unos datos no lineales utilizar `False`.

#### Atributos

Atributos de la clase `PolynomialFeatures`.

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - **feature_names_in_**
  - Nombres de los _features_ observados durante el ajuste. Definido sólo cuando _X_ tiene nombres que son todos cadenas.
* - **n_features_in_**
  - Número de _features_ vistos durante el ajuste.
* - **n_output_features_**
  - El número total de _features_ polinómicos de salida. El número de _features_ de salida se calcula iterando sobre todas las combinaciones de _features_ de entrada de tamaño adecuado.
* - **powers_**
  - Exponente para cada una de las entradas en la salida.
```

#### Métodos

Métodos de la clase `PolynomialFeatures`.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [fit](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html#sklearn.preprocessing.PolynomialFeatures.fit)(X,  y=None)
  - Calcula el número de _features_ de salida.
* - [fit_transform](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html#sklearn.preprocessing.PolynomialFeatures.fit_transform)(X,  y=None,  **fit_params)
  - Ajusta a los datos, luego los transforma.
* - [transform](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html#sklearn.preprocessing.PolynomialFeatures.transform)(X)
  - Transforma datos en _features_ polinómicos.
```

<br/>

### StandardScaler

[StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html): Estandariza _features_ al restar la media y escalar a la varianza unitaria (media = 0, desviación estándar = 1). Es útil para preparación de datos para modelos sensibles a la escala, como SVM, regresión lineal o KNN.
```python
# Sintaxis de llamada
StandardScaler(*, copy=True, with_mean=True, with_std=True)
```
**Parámetros:**
- **copy** - `bool`: Realiza la estandarización _in-place_, en lugar de retornar un nuevo objeto.
- **with_mean** - `bool`: Si es `True` entonces para la estandarización se utiliza la media de cada _feature_. Si es `False` se utiliza la media como 0.
- **with_std** - `bool`: Si es `True` entonces para la estandarización se utiliza la desviación estándar de cada _feature_. Si es `False` se utiliza la _std_ como 1.


#### Uso

Uso básico de esta clase:

```python
# Importar clase
from sklearn.preprocessing import StandardScaler

# Inicializar clase
scaler = StandardScaler()

# Ajustar
scaler.fit(X)

# Transformar
samples_scaled = scaler.transform(X)

# Se puede ajustar y transformar al mismo tiempo
samples_scaled = scaler.fit_transform(X)
```

#### Atributos

Atributos de la clase `StandardScaler`.

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - **feature_names_in_**
  - Nombres de los _features_ observados durante el ajuste. Definido sólo cuando _X_ tiene nombres dque son todos cadenas.
* - **mean_**
  - El valor medio de cada _feature_ en el conjunto de entrenamiento. Igual a `None` cuando `with_mean=False` y `with_std=False`.
* - **n_features_in_**
  - Número de _features_ vistos durante el ajuste.
* - **n_samples_seen_**
  - El número de muestras procesadas por el estimador para cada _feature_. Si no faltan muestras, _n_samples_seen_ será un entero; en caso contrario, será una matriz de tipo `int` . Si se utiliza _sample_weights_ será un `float` (si no faltan datos) o una matriz de tipo `float` que suma los pesos vistos hasta ahora. Se restablecerá en las nuevas llamadas al ajuste, pero se incrementa en las llamadas a _partial_fit_.
* - **scale_**
  - Escala relativa por _feature_ de los datos para lograr una media cero y una varianza unitaria. Generalmente esto se calcula usando `np.sqrt(var_)`. Si una varianza es cero, no se podrá lograr la varianza unitaria, y los datos se dejan como están, dando un factor de escala de 1. _scale\__ es igual a `None` cuando `with_std=False`.
* - **var_**
  - La varianza de cada _feature_ en el conjunto de entrenamiento. Se utiliza para calcular _scale\__. Igual a `None` cuando `with_mean=False` y `with_std=False`.
```

#### Métodos

Métodos de la clase `StandardScaler`.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [fit](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler.fit)(X,  y=None,  sample_weight=None)
  - Calcula la media y la _std_ que se utilizarán para el escalado posterior.
* - [fit_transform](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler.fit_transform)(X,  y=None,  **fit_params)
  - Ajusta a los datos, luego los transformar.
* - [inverse_transform](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler.inverse_transform)(X,  copy=None)
  - Escala los datos a la representación original.
* - [partial_fit](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler.partial_fit)(X,  y=None,  sample_weight=None)
  - Calcula en línea de la media y la _std_ en _X_ para su posterior escalado.
* - [transform](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler.transform)(X,  copy=None)
  - Realiza la normalización centrando y escalando.
```

<br/>

---
## Funciones

Funciones implementadas en el módulo `preprocessing`.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [add_dummy_feature](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.add_dummy_feature.html)(X, value=1.0)
  - Aumenta el conjunto de datos con una _feature_ ficticia adicional.
* - [binarize](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.binarize.html)(X, ...)
  - Umbral booleano de matriz tipo _array_ o _scipy.sparse_.
* - [label_binarize](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.label_binarize.html)(y, ...)
  - Binariza las etiquetas como _one-vs-all_.
* - [maxabs_scale](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.maxabs_scale.html)(X, ...)
  - Escala cada _feature_ al rango [-1, 1] sin romper la dispersión.
* - [minmax_scale](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.minmax_scale.html)(X, feature_range=(0, 1), ...)
  - Transforma las _features_ escalando cada una de ellas a un rango determinado.
* - [normalize](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.normalize.html)(X, norm='l2', ...)
  - Escala los vectores de entrada individualmente a norma unitaria (longitud del vector).
* - [power_transform](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.power_transform.html)(X, method='yeo-johnson', ...)
  - Transformación paramétrica monotónica para que los datos sean más gaussianos.
* - [quantile_transform](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.quantile_transform.html)(X, ...)
  - Transforma _features_ utilizando información de cuantiles.
* - [robust_scale](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.robust_scale.html)(X, ...)
  - Normalizar un conjunto de datos a lo largo de cualquier eje.
* - [scale](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.scale.html)(X, ...)
  - Normalizar un conjunto de datos a lo largo de cualquier eje.
```

<br/>

### Notas de _normalize_

[normalize](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.normalize.html): Escala los vectores de entrada individualmente a norma unitaria. Retorna dos objetos, X y norms.
```python
# Sintaxis de llamada
normalize(X, norm='l2', *, axis=1, copy=True, return_norm=False)
```
**Parámetros:**
- **X** - {array-like, sparse-matrix}: Datos a normalizer.
- **norm** - {'l1', 'l2', 'max'}: Norma a utilizar para normalizar cada muestra diferente de cero.

**Retorna:**
- _X_: `ndarray` o `sparse matrix` de _shape (n_samples, n_features)_.
- _norms_: `ndarray` de _shape (n_samples,)_ si `axis=1` sino _(n_features,)_

<br/>