# Datasets

Este módulo tiene funciones para importar varios _datasets_ predefinidos y para generar datos artificiales. Para importar los  _datasets_ o los generadores es necesario importar el módulo datasets o una función en concreto:

```python
# Importar módulo
from sklearn import datasets

# Importar clase específica
from sklearn.compose import ClassName

# Importar función específica
from sklearn.datasets import func_name
```
- func_name_ es el nombre de la función.

## Funciones

Funciones implementadas en el módulo ``

### Cargar _datasets_

Funciones para cargar datos predefinidos. Su uso básico sería:

```python
# Importar módulo
from sklearn import datasets

# Cargar dataset
dataset = datasets.func_name()

# Recuperar datos
X, y = dataset.data, dataset.target

# Opcionalmente convertir X en DataFrame
df = pd.DataFrame(X, columns=dataset.feature_names)
```

:::{note}
Muchas de las siguientes funciones retornan un objeto `Bunch`, que básicamente es una subclase de `dict`, que también permite acceder a los elementos por la notación punto `my_bunch.key_name`. Todos los métodos de `dict` se pueden usar en `Bunch`. Algunas llaves comumes del los objetos retornados son:
- _data_ - `ndarray`: Los datos del dataset (matriz de _features_).
- _target_ - `ndarray`: La columna _target_.
- _feature_names_ - `list`: Nombre de las columnas del _dataset_.
- _target_names_ - `ndarray`: En problemas de clasificación, son las posibles categorías del _target_.
- _DESCR_ - `str`: Descripción del _dataset_.
- _filename_ - `str`: Ruta donde está almacena el archivo en la computadora.

**Importante**: Existen otras llaves dependiendo del _dataset_, revisar la documentació de cada función.
:::

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [clear_data_home](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.clear_data_home.html)(data_home=None)
  - Borra todo el contenido de la caché de inicio de datos.
* - [dump_svmlight_file](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.dump_svmlight_file.html)(X, y, f, ...)
  - Almacena el conjunto de datos en formato de archivo _svmlight_ / _libsvm_.
* - [fetch_20newsgroups](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_20newsgroups.html)(, ...)
  - Carga los nombres de archivo y los datos del conjunto de datos de 20 grupos de noticias (clasificación).
* - [fetch_20newsgroups_vectorized](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_20newsgroups_vectorized.html)(, ...)
  - Carga y vectoriza el conjunto de datos de 20 grupos de noticias (clasificación).
* - [fetch_california_housing](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_california_housing.html)(, ...)
  - Carga el conjunto de datos de viviendas de California (regresión).
* - [fetch_covtype](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_covtype.html)(, ...)
  - Carga el conjunto de datos de cobertura (clasificación).
* - [fetch_file](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_file.html)(url, folder=None, local_filename=None, sha256=None, n_retries=3, delay=1)
  - Retorna un archivo de la web si no está ya presente en la carpeta local.
* - [fetch_kddcup99](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_kddcup99.html)(, ...)
  - Carga el conjunto de datos _kddcup99_ (clasificación).
* - [fetch_lfw_pairs](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_lfw_pairs.html)(, ...)
  - Carga el conjunto de datos de pares _Labeled Faces in the Wild (LFW)_ (clasificación).
* - [fetch_lfw_people](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_lfw_people.html)(, ...)
  - Carga el conjunto de datos de personas _Labeled Faces in the Wild (LFW)_ (clasificación).
* - [fetch_olivetti_faces](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_olivetti_faces.html)(, ...)
  - Carga el conjunto de datos de rostros _Olivetti de AT&T_ (clasificación).
* - [fetch_openml](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_openml.html)(name:str|None=None, ...)
  - Retorna un conjunto de datos de _openml_ por nombre o id del conjunto de datos.
* - [fetch_rcv1](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_rcv1.html)(, ...)
  - Carga el conjunto de datos multietiqueta _RCV1_ (clasificación).
* - [fetch_species_distributions](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_species_distributions.html)(, ...)
  - Cargador para el conjunto de datos de distribución de especies de Phillips et.
* - [get_data_home](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.get_data_home.html)(data_home=None)
  - Retorna la ruta del directorio de datos de scikit-learn.
* - [load_breast_cancer](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_breast_cancer.html)(, ...)
  - Carga y retorna el conjunto de datos cáncer de mama wisconsin (clasificación).
* - [load_diabetes](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_diabetes.html)(, ...)
  - Carga y retorna el conjunto de datos de diabetes (regresión).. Load and return the diabetes dataset (regression).
* - [load_digits](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html)(, ...)
  - Carga y retorna el conjunto de datos de dígitos (clasificación).. Load and return the digits dataset (classification).
* - [load_files](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_files.html)(container_path, ...)
  - Carga archivos de texto con categorías como nombres de subcarpetas.. Load text files with categories as subfolder names.
* - [load_iris](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html)(, ...)
  - Carga y retorna el conjunto de datos del iris (clasificación).. Load and return the iris dataset (classification).
* - [load_linnerud](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_linnerud.html)(, ...)
  - Carga y retorna el conjunto de datos Linnerud de ejercicio físico.
* - [load_sample_image](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_sample_image.html)(image_name)
  - Carga el `ndarray` de una sola imagen de muestra.
* - [load_sample_images](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_sample_images.html)()
  - Carga imágenes de muestra para su manipulación.
* - [load_svmlight_file](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_svmlight_file.html)(f, ...)
  - Carga conjuntos de datos en formato _svmlight_ / _libsvm_ en una matriz CSR dispersa.
* - [load_svmlight_files](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_svmlight_files.html)(files, ...)
  - Carga conjuntos de datos de varios archivos en formato _SVMlight_.
* - [load_wine](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_wine.html)(, ...)
  - Carga y retorna el conjunto de datos de vino (clasificación).
```

<br/>

### Generadores de datos

Funciones para generar datos artificiales.

:::{note}
Las funciones aquí enlistadas retornan 2 o más objetos cada una, revisar la documentación para revisar los objetos retornados de cada una.
:::

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [make_biclusters](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_biclusters.html)(shape, n_clusters, ...)
  - Genera una matriz de estructura diagonal de bloque constante para biclustering.
* - [make_blobs](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_blobs.html)(n_samples=100, n_features=2, ...)
  - Genera blobs gaussianos isotrópicos para la agrupación.
* - [make_checkerboard](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_checkerboard.html)(shape, n_clusters, ...)
  - Genera una matriz con estructura de damero de bloques para biclustering.
* - [make_circles](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_circles.html)(n_samples=100, ...)
  - Crea un círculo grande que contenga un círculo más pequeño en 2d.
* - [make_classification](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_classification.html)(n_samples=100, n_features=20, ...)
  - Genera un problema aleatorio de clasificación de _n_ clases.
* - [make_friedman1](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_friedman1.html)(n_samples=100, n_features=10, ...)
  - Genera el problema de regresión _"Friedman #1"_.
* - [make_friedman2](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_friedman2.html)(n_samples=100, ...)
  - Genera el problema de regresión _"Friedman #2"_.
* - [make_friedman3](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_friedman3.html)(n_samples=100, ...)
  - Genera el problema de regresión _"Friedman #3"_.
* - [make_gaussian_quantiles](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_gaussian_quantiles.html)(, ...)
  - Genera muestras gaussianas isotrópicas y etiquetas por cuantiles.
* - [make_hastie_10_2](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_hastie_10_2.html)(n_samples=12000, ...)
  - Genera datos para la clasificación binaria utilizada en _Hastie et al. 2009, Ejemplo 10.2_.
* - [make_low_rank_matrix](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_low_rank_matrix.html)(n_samples=100, n_features=100, ...)
  - Genera una matriz de _low rank_ mayoritariamente con valores singulares en forma de campana.
* - [make_moons](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_moons.html)(n_samples=100, ...)
  - Crea dos medios círculos intercalados.
* - [make_multilabel_classification](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_multilabel_classification.html)(n_samples=100, n_features=20, ...)
  - Genera un problema de clasificación aleatoria multietiqueta.
* - [make_regression](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_regression.html)(n_samples=100, n_features=100, ...)
  - Genera un problema de regresión aleatoria.
* - [make_s_curve](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_s_curve.html)(n_samples=100, ...)
  - Genera un conjunto de datos de la curva _S_.
* - [make_sparse_coded_signal](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_sparse_coded_signal.html)(n_samples, ...)
  - Genera una señal como una combinación dispersa de elementos del diccionario.
* - [make_sparse_spd_matrix](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_sparse_spd_matrix.html)(n_dim=1, ...)
  - Genera una matriz simétrica y definida positiva dispersa.
* - [make_sparse_uncorrelated](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_sparse_uncorrelated.html)(n_samples=100, n_features=10, ...)
  - Genera un problema de regresión aleatorio con diseño disperso no correlacionado.
* - [make_spd_matrix](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_spd_matrix.html)(n_dim, ...)
  - Genera una matriz aleatoria simétrica y definida positiva.
* - [make_swiss_roll](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_swiss_roll.html)(n_samples=100, ...)
  - Genera un conjunto de datos de _rollo suizo_.
```