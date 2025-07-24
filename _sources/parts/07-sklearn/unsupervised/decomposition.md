---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Decomposition

Contiene algoritmos de descomposición de matrices, como PCA y NMF, para reducir la dimensionalidad o extraer _features_ latentes. Para importar este módulo o una clase o función específica usar:

```python
# Importar módulo
from sklearn import decomposition

# Importar clase específica
from sklearn.decomposition import ClassName

# Importar función específica
from sklearn.decomposition import func_name
```
- _ClassName_ o _func_name_ es el nombre de la clase o función respectivamente.

:::{note}
Para más información de esta librería visitar la [documentación](https://scikit-learn.org/stable/api/sklearn.decomposition.html) de `sklearn`.
:::

<br/>

## Clases

Clases implementadas en el módulo `decomposition`.

```{list-table}
:header-rows: 1

* - Clase
  - Descripción
* - [DictionaryLearning](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.DictionaryLearning.html)(n_components=None, ...)
  - Aprendizaje de diccionarios.
* - [FactorAnalysis](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.FactorAnalysis.html)(n_components=None, ...)
  - Análisis factorial (AF).
* - [FastICA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.FastICA.html)(n_components=None, ...)
  - _FastICA_: un algoritmo rápido para el análisis de componentes independientes.
* - [IncrementalPCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.IncrementalPCA.html)(n_components=None, ...)
  - Análisis incremental de componentes principales (IPCA).
* - [KernelPCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.KernelPCA.html)(n_components=None, ...)
  - Análisis de componentes principales Kernel (KPCA).
* - [LatentDirichletAllocation](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.LatentDirichletAllocation.html)(n_components=10, ...)
  - Asignación latente de Dirichlet con algoritmo Bayes variacional en línea.
* - [MiniBatchDictionaryLearning](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchDictionaryLearning.html)(n_components=None, ...)
  - Aprendizaje de diccionarios en _Mini-batch_.
* - [MiniBatchNMF](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchNMF.html)(n_components='auto', ...)
  - Factorización de matrices no negativas (NMF) en _Mini-batch_.
* - [MiniBatchSparsePCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchSparsePCA.html)(n_components=None, ...)
  - Análisis de componentes principales dispersos en _Mini-batch_.
* - [NMF](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.NMF.html)(n_components='auto', ...)
  - Factorización de matrices no negativas (NMF).
* - [PCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html)(n_components=None, ...)
  - Análisis de componentes principales (PCA).
* - [SparseCoder](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.SparseCoder.html)(dictionary, ...)
  - Codificación dispersa.
* - [SparsePCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.SparsePCA.html)(n_components=None, ...)
  - Análisis de componentes principales dispersos (SparsePCA).
* - [TruncatedSVD](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.TruncatedSVD.html)(n_components=2, ...)
  - Reducción de la dimensionalidad mediante _SVD_ truncada (también conocido como LSA).
```

<br/>

### PCA

[PCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html): Realiza Análisis de Componentes Principales, una técnica de reducción de dimensionalidad que transforma los datos en un conjunto de componentes ortogonales (lineales) que capturan la mayor varianza. Útil para visualización de datos de alta dimensión, eliminación de ruido, preparación de datos para modelos de aprendizaje automático, entre otros.

:::{caution}
Si los _features_ están en una matriz _sparse_ se recomienda usar `TruncatedSVD`.
:::

```python
# Sintaxis de llamada
PCA(n_components=None, *, copy=True, whiten=False, svd_solver='auto', tol=0.0, 
    iterated_power='auto', n_oversamples=10, power_iteration_normalizer='auto', 
    random_state=None)
```
**Parámetros:**
- **n_components** - `int`, `float` o {'mle'}: Es la cantidad de componentes (_features_) a mantener (los de con mayor varianza). Si no se especifica, todos los componentes se mantienen. Se puede poner el porcentaje de varianza a preservar en lugar del número de componentes.
- **random_state** - `int` o `RandomState Instance`: Controla la aleatoriedad del estimador.
- **whitten** - `int`: Escala los componentes principales (los vectores _.component\__) al multiplicarlos por la raíz cuadrada de _n_samples_ y dividirlos por los valores singulares.

<br/>

**Uso**:

La forma básica de usar este clase es la siguiente:

```python
# Importar clase
from sklearn.decomposition import PCA

# Inicializar el modelo PCA
model = PCA(n_components=2)  # n_components es el número de componentes principales

# Ajustar el modelo
model.fit(X) 

# Ajustar el modelo y transformar los datos
X_transformed = model.fit_transform(X) 

# Transformar datos
X_transformed = model.transform(X) 

# Obtener la varianza explicada por cada componente
explained_variance = model.explained_variance_ratio_

# Reconstruir los datos originales (aproximación)
X_reconstructed = model.inverse_transform(X_transformed)  # Aproximación de los datos originales
```
- _features_ será la matriz con dimensionalidad reducida (la cantidad de _features_ será igual al argumento de _n_components_).

<br/>

Patrones útiles:

```python
# Graficar componentes
model = PCA()
pca_features = model.fit_transform(X)
xs = pca_features[:,0]
ys = pca_features[:,1]
plt.scatter(xs, ys) # Centrados al origen con correlación de 0
plt.axis('equal')
plt.show()

# Graficar componentes principales (en 2D) como vectores
plt.scatter(X.iloc[:,0], X.iloc[:,1])
model = PCA()
model.fit(X)
mean = model.mean_
first_pc = model.components_[0,:]
plt.arrow(mean[0], mean[1], first_pc[0], first_pc[1], color='red', width=0.01)
plt.axis('equal')
plt.show()

# Graficar componentes con más varianza (como barras)
pipeline.fit(X)
model = PCA()
pca = model.fit(X)
features = range(pca.n_components_)
plt.bar(features, pca.explained_variance_)
plt.xlabel('PCA feature')
plt.ylabel('variance')
plt.xticks(features)
plt.show()
```

<br/>

**Ejemplo**

En este ejemplo se reduce la dimensionalidad del dataset iris a 2D.

```{code-cell} ipython3
# Importaciones
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA

# Cargar dataset
iris = sns.load_dataset('iris')
X = iris.iloc[:, :4].values 

# Aplicar PCA con 2 componentes
pca = PCA(n_components=2) 
pca.fit(X)
X_transformed = pca.transform(X)

# Recuperar componentes
xs = X_transformed[:,0]
ys = X_transformed[:,1]

# Graficar features
plt.scatter(xs, ys, c=iris.species.astype('category').cat.codes, cmap='Dark2') 
plt.show()
```


<br/>

#### Atributos

Atributos de la clase `PCA`.

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - **components_**
  - Ejes principales en el espacio de _features_, que representan las direcciones de máxima varianza en los datos. Equivalentemente, los vectores singulares de los datos de entrada centrados, paralelos a sus vectores propios. Los componentes se ordenan por _explained_variance\__ decreciente.
* - **explained_variance_**
  - La cantidad de varianza explicada por cada uno de los componentes seleccionados. La estimación de la varianza utiliza _n_samples_ - 1 grados de libertad. Igual a _n_components_ mayores valores propios de la matriz de covarianza de _X_.
* - **explained_variance_ratio_**
  - Porcentaje de varianza explicado por cada uno de los componentes seleccionados. Si no se establece _n_components_, se almacenan todos los componentes y la suma de los coeficientes es igual a 1,0.
* - **feature_names_in_**
  - Nombres de los _features_ observados durante el ajuste. Definido sólo cuando _X_ tiene nombres que son todos cadenas.
* - **mean_**
  - Media empírica por _feature_, estimada a partir del conjunto de entrenamiento. Igual a `X.mean(axis=0)`.
* - **n_components_**
  - El número estimado de componentes. Cuando _n_components_ se establece en _'mle'_ o un número entre 0 y 1 (con `svd_solver=='full'`) este número se estima a partir de los datos de entrada. De lo contrario, es igual al parámetro _n_components_, o el valor menor de _n_features_ y _n_samples_ si _n_components_ es `None`.
* - **n_features_in_**
  - Número de _features_ vistos durante el ajuste.
* - **n_samples_**
  - Número de muestras en los datos de entrenamiento.
* - **noise_variance_**
  - La covarianza estimada del ruido según el modelo _Probabilistic PCA_ de Tipping y Bishop 1999.
* - **singular_values_**
  - Los valores singulares correspondientes a cada uno de los componentes seleccionados. Los valores singulares son iguales a las 2-normas de las variables _n_components_ en el espacio de dimensión inferior.
```

#### Métodos

Métodos de la clase `PCA`.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [fit](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA.fit)(X,  y=None)
  - Ajusta el modelo con _X_.
* - [fit_transform](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA.fit_transform)(X,  y=None)
  - Ajusta el modelo con _X_ y aplica la reducción de dimensionalidad a _X_.
* - [inverse_transform](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA.inverse_transform)(X)
  - Transforma los datos a su espacio original.
* - [score](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA.score)(X,  y=None)
  - Retorna la _log-likelihood_ media de todas las muestras.
* - [score_samples](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA.score_samples)(X)
  - Retorna la _log-likelihood_ de cada muestra.
* - [transform](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA.transform)(X)
  - Aplica reducción de dimensionalidad a _X_.
```

<br/>

### NMF

[NMF](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.NMF.html): Realiza una _Factorización de Matrices No Negativas_, una técnica de reducción de dimensionalidad que descompone una matriz en dos matrices no negativas, útil para datos no negativos. Encuentra dos matrices no negativas cuyo producto se aproxime a la matriz no negativa _X_. Útil para extracción de temas en textos, procesamiento de imágenes, recomendación de productos, entre otros.
```python
# Sintaxis de llamada
NMF(n_components='auto', *, init=None, solver='cd', beta_loss='frobenius', tol=0.0001, 
    max_iter=200, random_state=None, alpha_W=0.0, alpha_H='same', l1_ratio=0.0, verbose=0, 
    shuffle=False)
```
**Parámetros:**
- **n_components** - `int`: Número de componentes. Si no se especifica se utilizan todos los _features_.

:::{tip}
Si los resultados de `.transform()` se normalizan, por ejemplo, con `sklearn.preprocessing.normalize()`, entonces si se multiplica por el producto punto una fila normalizada concreta contra la matriz normalizada, entonces se calculará la similitud de coseno, para identificar observaciones similares:

```python
# Definir pipeline
nmf = NMF(n_components = 20)
normalizer = Normalizer()
pipeline = make_pipeline(nmf, normalizer)

# Tranformar datos
norm_features = pipeline.fit_transform(X)

# Convertir a DataFrame
df = pd.DataFrame(norm_features, index = sample_names)

# Recuperar fila concreta
row = df.loc['index_name']

# Realizar multiplicación punto
similarities = df.dot(row)

# Recuperar observaciones con mayores similitudes.
print(similarities.nlargest())
```
:::

<br/>

**Uso**:

```python
# Importar clase
from sklearn.decomposition import NMF

# Inicializar el modelo NMF
model = NMF(n_components)  # n_components es el número de temas o componentes

# Ajustar el modelo
model.fit(X)

# Ajustar el modelo y transformar los datos
W = model.fit_transform(X)

# Transformar datos
W = model.transform(X)

# Obtener la matriz de componentes (H)
H = model.components_  # Representa los temas o patrones subyacentes

# Reconstruir la matriz original (aproximación)
X_reconstructed = W @ H 
```
- _W_ será la matriz con dimensionalidad reducida (la cantidad de _features_ será igual al argumento de _n_components_), pero mantendrá el número de _samples_, es decir un _shape (n_samples, n_components)_.
- _H_ será la matriz de factorización tendrá _shape_, _(n_components, n_features)_, donde _n_features_ son los cantidad de _features_ originales en _X_

#### Atributos

Atributos de la clase `NMF`.

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - **components_**
  - Matriz de factorización, a veces denominada "diccionario".
* - **feature_names_in_**
  - Nombres de los _features_ observados durante el ajuste. Definido sólo cuando _X_ tiene nombres que son todos cadenas.
* - **n_components_**
  - El número de componentes. Es el mismo que el parámetro _n_components_ si se ha dado. De lo contrario, será el mismo que el número de _features_.
* - **n_features_in_**
  - Número de _features_ vistos durante el ajuste.
* - **n_iter_**
  - Número real de iteraciones.
* - **reconstruction_err_**
  - Norma de Frobenius de la diferencia matricial, o divergencia beta, entre los datos de entrenamiento _X_ y los datos reconstruidos WH a partir del modelo ajustado.
```

#### Métodos

Métodos de la clase `NMF`.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [fit](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.NMF.html#sklearn.decomposition.NMF.fit)(X,  y=None,  **params)
  - Aprende un modelo NMF para los datos _X_.
* - [fit_transform](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.NMF.html#sklearn.decomposition.NMF.fit_transform)(X,  y=None,  W=None,  H=None)
  - Aprende un modelo NMF para los datos _X_ y devuelve los datos transformados.
* - [inverse_transform](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.NMF.html#sklearn.decomposition.NMF.inverse_transform)(X=None,  , ...)
  - Transforma los datos a su espacio original.
* - [transform](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.NMF.html#sklearn.decomposition.NMF.transform)(X)
  - Transforma los datos _X_ según el modelo NMF ajustado.
```

<br/>

## Funciones

Funciones implementadas en el módulo `decomposition`.

```{list-table}
:header-rows: 1

* - Clase
  - Descripción
* - [dict_learning](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.dict_learning.html)(X, n_components, ...)
  - Resuelve un problema de factorización matricial de aprendizaje de diccionario.
* - [dict_learning_online](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.dict_learning_online.html)(X, n_components=2, ...)
  - Resuelve un problema de factorización matricial de aprendizaje de diccionario en línea.
* - [fastica](https://scikit-learn.org/stable/modules/generated/fastica-function.html)()
  - Realiza un análisis rápido de componentes independientes.
* - [non_negative_factorization](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.non_negative_factorization.html)(X, W=None, H=None, n_components='auto', ...)
  - Calcula la factorización de matrices no negativas (NMF).
* - [sparse_encode](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.sparse_encode.html)(X, dictionary, ...)
  - Codificación dispersa.
```