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

# Clusters

Este módulo implementa algoritmos para _clustering_. Esta dividido en dos submódulos.

:::{note}
Para más información visitar la [documentación](https://docs.scipy.org/doc/scipy/reference/cluster.html) de _scipy_.
:::

## Submódulo _vq_

Este submódulo se enfoca en la cuantización vectorial (_vectorial quantization_), que es una técnica para asignar vectores a un conjunto finito de "centros" o "códigos" predefinidos. Es útil para agrupar datos en _clusters_ basados en distancias. Algunos casos de usos son:
- Compresión de datos (por ejemplo, reducir colores en una imagen).
- Agrupamiento de datos en _clusters_ (por ejemplo, segmentación de clientes).
- Análisis de patrones en datos multidimensionales.

Para usar este submódulo es necesario importarlo

```python
# Importar vq
from scipy.clusters import vq

# Importar función específica
from scipy.clusters.vq import function_name
```
- _function_name_ es el nombre de la función que se desea importar.

:::{note}
Para más información visitar la [documentación](https://docs.scipy.org/doc/scipy/reference/cluster.vq.html#module-scipy.cluster.vq) de _scipy_.
:::

<br/>

### Funciones de _vq_

Funciones implementadas en el submódulo `vq`. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [kmeans](https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.vq.kmeans.html)(obs, k_or_guess, ...)
  - Realiza _K-means_ en un conjunto de vectores de observación que forman _K_ clústeres. Genera los centros de los clusters.
* - [kmeans2](https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.vq.kmeans2.html)(data, k, ...)
  - Clasifica un conjunto de observaciones en los grupos _K_ _clusters_ utilizando el algoritmo _K-Means_.
* - [vq](https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.vq.vq.html)(obs, code_book, ...)
  - Asigna códigos de un libro de códigos a observaciones, (asigna a las observaciones el cluster al que pertenece cada observación).
* - [whiten](https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.vq.whiten.html)(obs, ...)
  - Normaliza un grupo de observaciones por función por _feature_.
```

<br/>

#### Notas de _kmeans_

[kmeans](https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.vq.kmeans.html): Realiza _K-means_ en un conjunto de vectores de observación que forman _K_ clústeres. Genera los centros de los clusters.
`scipy.cluster.vq.kmeans()`: Realiza un agrupamiento k-means en k grupos en un `set` de vector de observaciones. Genera los centros de los clusters.
```python
# Sintaxis de llamada
vq.kmeans(obs, k_or_guess, iter=20, thresh=1e-05, check_finite=True, *, rng=None)
```
- **Principales Parámetros:**
    - **obs** - `ndarray `: Cada fila es un vector de observaciones. Las columnas son los feature. Debe de estar estandarizado con scipy.cluster.vq.whiten().
    - **k_or_guess** - `int` o `ndarray`: Número de centroides a generar.
    - **iter** - `int`: Número de veces a correr el k-means.
    - **thresh** - `float`: Umbral para indicar que se detenga el modelo si en cada iteración el mejorarmiento en el modelo es menor a este argumento.
    - **check_finite** - `bool`: Para indicar que se revise que las matrices de entrada solo tienen elementos finitos.
    - **seed** - `None`, `int`, `np.random.generator`: Semilla para inicializar el generador de números aletorios.
- **Retorna:**
    - **codebook** - `ndarray`: Una matriz de _k_ por _N_ de _k_ centroides.
    - **distortion** - `float`: La distancia euclidiana media (no cuadrada) entre las observaciones pasadas y los centroides generados.

Patrones útiles:

```python
# Graficar "elbow plot" para seleccionar número de clusters
distortions = []
num_clusters = range(1, 7) # Número de clusters a probar
for i in num_clusters:
    cluster_centers, distortion = kmeans(df[['x_scaled', 'y_scaled']], i)
    distortions.append(distortion)

elbow_plot = pd.DataFrame({'num_clusters': num_clusters, 'distortions': distortions})
sns.lineplot(x='num_clusters', y='distortions', data = elbow_plot)
plt.xticks(num_clusters)
plt.show()
```


**Uso**:

:::{caution}
En _clustering_ es recomendado normalizar los datos antes de aplicar `kmeans()`, para ello se puede usar la función `whiten`:

```
# Importar función
from scipy.cluster.vq import whiten

# Normalizar datos
obs = whiten(features)
```
:::

```python
# Importar funciones
from scipy.cluster.vq import kmeans

# Generar centroides
centroids, _ = kmeans(obs, k_or_guess)
```

<br/>

#### Notas de _vq_

[vq](https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.vq.vq.html): Asigna códigos de un libro de códigos a observaciones, (asigna a las observaciones el cluster al que pertenece cada observación).

`scipy.cluster.vq.vq()`: Asigna códigos desde un libro de códigos a las observaciones. (Asigna a las observaciones el cluster al que pertenece cada observación).
```python
# Sintaxis de llamada
vq.vq(obs, code_book, check_finite=True)
```
- **Principales Parámetros:**
    - **obs** - `ndarray `: Cada fila es un vector de observaciones. Las columnas son los feature. Debe de estar estandarizado con scipy.cluster.vq.whiten().
    - **code_book** - `ndarray`: Centro de los clusters. Generalmente es un array creado con scipy.cluster.vq.kmeans().
    - **check_finite** - `bool`: Para indicar que se revise que las matrices de entrada solo tienen elementos finitos.
- **Retorna:**
    - **code** - `ndarray`: Una matriz de longitud _M_ que contiene el índice del libro de códigos para cada observación.
    - **dist** - `ndarray`: La distorsión (distancia) entre la observación y su código más cercano.

**Uso**:

```python
# Importar funciones
from scipy.cluster.vq import vq
import seaborn as sns

# Generar cluster para cada datapoint
df['cluster_labels'], _ = vq(df, centroids)

# Graficar datos y el cluster
sns.scatterplot(x='x_coordinate', 
                y='y_coordinate',
                hue='cluster_labels', 
                data = df)
plt.show()
```
- Previamente se tuvo que haber generado los centroides _centroids_ con `kmeans()`.
- No necesariamente se tiene que generar una columna nueva, se puede asignar un objeto y hacer las manipulaciones correspondientes, pero esta es una forma muy fácil de indentificar el _cluster_ de cada punto, además que es útil para visualizar los datos.

<br/>

---
## Submódulo _hierarchy_

Este submódulo proporciona funciones para agrupación jerárquica y aglomerativa. Sus características incluyen generar grupos jerárquicos a partir de matrices de distancia, calcular estadísticas sobre grupos, y visualizar grupos con dendrogramas. Algunos casos de uso son:
- Visualización de relaciones jerárquicas en datos (por ejemplo, biología para agrupar genes o especies).
- Análisis de _clusters_ en datos donde no se conoce el número óptimo de grupos.
- Segmentación de datos en grupos naturales basados en similitudes.

Para usar este submódulo es necesario importarlo

```python
# Importar hierarchy
from scipy.clusters import hierarchy

# Importar función específica
from scipy.clusters.hierarchy import function_name
```
- _function_name_ es el nombre de la función que se desea importar.

:::{note}
Para más información visitar la [documentación](https://docs.scipy.org/doc/scipy/reference/cluster.hierarchy.html) de _scipy_.
:::

<br/>

### Clases de _hierarchy_

Clases implementadas en el submódulo `hierarchy`.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [ClusterNode](https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.ClusterNode.html)(id, ...)
  - Una clase de nodo de árbol para representar un clúster.
* - [DisjointSet](https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.DisjointSet.html)([elements])
  - La estructura de datos `DisjointSet` para consultas de conectividad incremental.
``` 

<br/>

(hierarchy-functions)=
### Funciones de _hierarchy_

Funciones implementadas en el submódulo `hierarchy`. 

:::{tip}
Alternativamente revisar {ref}`cluster-classes`, particularmente `KMeans()`.
:::

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - **Principales funciones**
  - 
* - [cut_tree](https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.cut_tree.html)(Z, ...)
  - Dada una _linkage matrix_ _z_, devuelve el _cut tree_.
* - [dendrogram](https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.dendrogram.html)(Z, ...)
  - Grafica la agrupación jerárquica como un dendrograma.
* - [linkage](https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.linkage.html)(y, ...)
  - Realiza agrupación jerárquica/aglomerativa. Calcula las distancias entre los _clusters_ en cada _stage_.
* - [fcluster](https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.fcluster.html)(Z, t, ...)
  - Forma grupos planos de la agrupación jerárquica definidas por la _linkage matrix_ dada. Crea la estiquetas sobre a cual cluster pertenece cada dato.
* - **Agrupación aglomerativa**
  - 
* - [average](https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.average.html)(y)
  - Realiza un _linkage average/UPGMA_ en una _distance matrix_ condensada.
* - [centroid](https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.centroid.html)(y)
  - Realiza un _linkage centroid/UPGMC_.
* - [complete](https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.complete.html)(y)
  - Realiza un _linkage complete/max/farthest_ en una _distance matrix_ condensada.
* - [linkage](https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.linkage.html)(y, ...)
  - Realizar agrupación jerárquica/aglomerativa. Calcula las distancias entre los _clusters_ en cada _stage_.
* - [median](https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.median.html)(y)
  - Realiza un _linkage median/WPGMC_.
* - [single](https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.single.html)(y)
  - Realiza un _linkage single/min/nearest_ en la _distance matrix_ condensada `y`.
* - [ward](https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.ward.html)(y)
  - Realiza el _linkage_ de Ward en una _distance matrix_ condensada.
* - [weighted](https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.weighted.html)(y)
  - Realiza un _linkage weighted/WPGMA_ en la _distance matrix_ condensada.
* - **Agrupación jeráquica a plana**
  - 
* - [fcluster](https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.fcluster.html)(Z, t, ...)
  - Forma grupos planos de la agrupación jerárquica definidas por la _linkage matrix_ dada. Crea la estiquetas sobre a cual cluster pertenece cada dato.
* - [fclusterdata](https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.fclusterdata.html)(X, t, ...)
  - Datos de observación de clúster utilizando una métrica dada.
* - [leaders](https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.leaders.html)(Z, T)
  - Retorna los nodos raíz en una agrupación jerárquica.
* - **Estadísticas en jerarquías**
  - 
* - [cophenet](https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.cophenet.html)(Z, ...)
  - Calcula las distancias cofenéticas entre cada observación en la agrupación jerárquica definida por el _linkage_ `Z`.
* - [from_mlab_linkage](https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.from_mlab_linkage.html)(Z)
  - Convierte una _linkage matrix_ generada por MATLAB (TM) a una nueva _linkage matrix_ compatible con este módulo.
* - [inconsistent](https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.inconsistent.html)(Z, ...)
  - Calcula las estadísticas de inconsistencia en una _linkage matrix_.
* - [maxRstat](https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.maxRstat.html)(Z, R, i)
  - Retorna la estadística máxima para cada grupo de cluster _non-singleton_ y sus hijos.
* - [maxdists](https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.maxdists.html)(Z)
  - Retorna la distancia máxima entre cualquier clúster que no sea _singleton_.
* - [maxinconsts](https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.maxinconsts.html)(Z, R)
  - Retorna el coeficiente de inconsistencia máxima para cada grupo no _singleton_ y sus hijos.
* - **Jerarquías a árboles**
  -
* - [cut_tree](https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.cut_tree.html)(Z, ...)
  - Dada una _linkage matrix_ _z_, devuelve el _cut tree_.
* - [leaves_list](https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.leaves_list.html)(Z)
  - Retorna un `list` de ids de los nodos de hojas.
* - [optimal_leaf_ordering](https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.optimal_leaf_ordering.html)(Z, y, ...)
  - Dada una _linkage matrix_ _Z_ y una distancia, reordena el _cut tree_.
* - [to_tree](https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.to_tree.html)(Z, ...)
  - Convierte una _linkage matrix_ en un objeto de árbol fácil de usar.
* - **Validaciones**
  -
* - [correspond](https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.correspond.html)(Z, Y)
  - Verifica la correspondencia entre matrices de _linkage_ y distancia condensada.
* - [is_isomorphic](https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.is_isomorphic.html)(T1, T2)
  - Determina si dos asignaciones de clúster diferentes son equivalentes.
* - [is_monotonic](https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.is_monotonic.html)(Z)
  - Retorna `True` si el _linkage_ aprobado es monotónico.
* - [is_valid_im](https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.is_valid_im.html)(R, ...)
  - Retorna `True` si la matriz de inconsistencia pasada es válida.
* - [is_valid_linkage](https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.is_valid_linkage.html)(Z, ...)
  - Verifica la validez de una _linkage matrix_.
* - [num_obs_linkage](https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.num_obs_linkage.html)(Z)
  - Retorna el número de observaciones originales de la _linkage matrix_ aprobada.
* - **Utilidades**
  -
* - [set_link_color_palette](https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.set_link_color_palette.html)(palette)
  - Esteblece una `list` de códigos de color _matplotlib_ para su uso en un dendrograma.
* - [to_mlab_linkage](https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.to_mlab_linkage.html)(Z)
  - Convierte una _linkage matrix_ a una MATLAB (TM) compatible.
```

#### Notas de _dendrogram_

[dendrogram](https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.dendrogram.html): Grafica el agrupamiento jerárquico. Es necesario usar `plt.show()`.
```python
# Sintaxis de llamada
hierarchy.dendrogram(Z, p=30, truncate_mode=None, color_threshold=None, get_leaves=True, 
                     orientation='top', labels=None, count_sort=False, distance_sort=False, 
                     show_leaf_counts=True, no_plot=False, no_labels=False, leaf_font_size=None, 
                     leaf_rotation=None, leaf_label_func=None, show_contracted=False, 
                     link_color_func=None, ax=None, above_threshold_color='C0')
```
- **Parámetros:**
    - **Z** - `ndarray `: Objeto retornado de la función `scipy.cluster.hierachy.linkage`.
- **Retorna:**
    - **R**: `dict`.

**Uso**:

```python
# Importar funciones
import seaborn as sns
from scipy.cluster.hierarchy import linkage, dendrogram
from scipy.cluster.vq import whiten
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# Cargar dataset
iris = sns.load_dataset('iris')

# Extraer features y labels
X = iris.iloc[:, :4].values
y=iris.species.values
X_train, _, y_train, _ = train_test_split(X, y, test_size=0.3, random_state=21, stratify=y)

# Normalizar datos
X_scaled = whiten(X_train)

# Calcular mergings
Z = linkage(X_scaled, method='complete')

# Graficar dendrograma
plt.figure(figsize=(10, 6))
dendrogram(Z,
           labels=y_train,
           leaf_rotation=90,
           leaf_font_size=6,
)

plt.show()
```

**Ejemplo**:

En este ejemplo se crea un dendrograma del _dataset_ _iris_. Notar que para una mejor visualización se tomó solo una muestra de los datos y además de normalizaron con la función `whiten()`.

:::{attention}
En este ejemplo se está usando un _dataset_ que ya tiene etiquetas, por lo que de antemano ya se conoce la etiqueta real de cada _datapoint_, sin embargo en _unsupervised learning_ se trabaja con datos no etiquetados. Este ejemplo es solo con fines ilustrativos de cómo usar la función, pero lo común es no conocer la etiqueta real de los datos.
:::

```{code-cell} ipython3
# Importar funciones
import seaborn as sns
from scipy.cluster.hierarchy import linkage, dendrogram
from scipy.cluster.vq import whiten
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# Cargar dataset
iris = sns.load_dataset('iris')

# Extraer features y labels
X = iris.iloc[:, :4].values
y=iris.species.values
X_train, _, y_train, _ = train_test_split(X, y, test_size=0.3, random_state=21, stratify=y)

# Normalizar datos
X_scaled = whiten(X_train)

# Calcular mergings
Z = linkage(X_scaled, method='complete')

# Graficar dendrograma
plt.figure(figsize=(10, 6))
dendrogram(Z,
           labels=y_train,
           leaf_rotation=90,
           leaf_font_size=6,
)

plt.show()
```
- Notar que la gráfica se lee de abajo hacia arriba, empezando desde abajo cada punto es su propio _cluster_ y eventualmente comienzan a agruparse para formar _clusters_ más amplios.
- El eje _y_ indica la distancias entre las agrupaciones de los _clusters_.

<br/>

#### Notas de _fcluster_

[fcluster](https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.fcluster.html): Crea la estiquetas sobre a cuál _cluster_ pertenece cada dato desde el agrupamiento jeráquico definido en la matriz _linkage_.
```python
# Sintaxis de llamada
hierarchy.fcluster(Z, t, criterion='inconsistent', depth=2, R=None, monocrit=None)
```
- **Parámetros:**
    - **Z** - `ndarray `: Objeto retornado por `scipy.cluster.hierachy.linkage`.
    - **t** - `scalar`: .
        - Si _criterion_ = {'inconsistent', 'distance', 'monocrit'}: Un _threshold_ a aplicar cuando se formen los _clusters_ planos.
        - Si _criterion_ = {'maxclust', 'max_monocrit'}: Número máximo de _clusters_.
    - **criterion** - {'inconsistent', 'distance', 'maxclust', 'monocrit', 'maxclust_monocrit'}: Criterio a usar para formar los _clusters_ planos.
    - **depth** - `int`: Profundidad máxima para calcular la inconsistencia.
    - **R** - `ndarray`: Matriz de inconsistencias a usar cundo `criterion='inconsistent'`.
- **Retorna:**
    - **f_cluster**: `ndarray`.

**Uso**:

```python
# Importar funciones
from scipy.cluster.hierarchy import fcluster
import seaborn as sns

# Generar cluster para cada datapoint
df['cluster_labels'] = fcluster(Z, t, criterion)

# Graficar datos y el cluster
sns.scatterplot(x='x_coordinate', 
                y='y_coordinate',
                hue='cluster_labels', 
                data = df)
plt.show()
```
- Previamente se tuvo que haber generado la matriz _Z_ con `linkage()`.
- No necesariamente se tiene que generar una columna nueva, se puede asignar un objeto y hacer las manipulaciones correspondientes, pero esta es una forma muy fácil de indentificar el _cluster_ de cada punto, además que es útil para visualizar los datos.

**Ejemplo**:

En este ejemplo se crean 3 _clusters_ y se gráfica un diagrama de dispersión que indica el _cluster_ asignado y su etiqueta real.

:::{attention}
En este ejemplo se está usando un _dataset_ que ya tiene etiquetas, por lo que de antemano ya se conoce la etiqueta real de cada _datapoint_, sin embargo en _unsupervised learning_ se trabaja con datos no etiquetados. Este ejemplo es solo con fines ilustrativos de cómo usar la función, pero lo común es no conocer la etiqueta real de los datos.
:::

```python
# Importaciones
from scipy.cluster.hierarchy import fcluster
import pandas as pd

# Asignar etiquetas a cada punto
cluster_labels = fcluster(Z, t=3, criterion='maxclust')

# Añadir el cluster al dataset
iris['cluster'] = cluster_labels

# Crear diagrama de dispersión
plt.figure(figsize=(8, 6))
sns.scatterplot(x='sepal_length', y='petal_length', hue='cluster', 
                style='species', data=iris, palette='Dark2', s=70)
plt.title('Clusters vs Actual Species')
plt.show()

# Opcionalmente crear crosstab de cluster vs species
print(pd.crosstab(iris['cluster'], iris['species']))
```

<br/>

#### Notas de _linkage_

[linkage](https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.linkage.html): Realiza una agrupamiento jerárquico o aglomerativo. Calcula las distancias entre los _clusters_ en cada _stage_ y va agrupando los _clusers_ con base a esas distancias entre los puntos.

:::{caution}
Esta función puede ser computacionalmente costosa en _datasets_ grandes. En ese caso se recomienda usar `kmeans()`.
:::

```python
# Sintaxis de llamada
hierarchy.linkage(y, method='single', metric='euclidean', optimal_ordering=False)
```
- **Parámetros:**
    - **y** - `ndarray` o `DataFrame`: Matriz de distancia condensada. Alternativamente una matriz de _m_ vectores de observaciones en _n_ dimensiones, _shape (m, n)_. Debe de contener únicamente valores numéricos y finitos.
    - **method** - `str`: Algoritmo de _linkage_ a usar.
        - 'single': Calcula la proximidad de los _clusters_ basado en los dos objetos más cercanos.
        - 'complete': Calcula la proximidad de los _clusters_ basado en los dos objetos más alejados.
        - 'mean': Calcula la proximidad de los _clusters_ basado en la media aritmética de todos los objetos.
        - 'centroid: Calcula la proximidad de los _clusters_ basado en la media geométrica de todos los objetos.
        - 'median': Utiliza la media de los objetos cluster.
        - 'ward': Calcula la proximidad de los _clusters_ usando la diferencia entre la suma de los cuadrados de los _joint clusters_ menos la suma de los cuadrados individuales.
    - **metric** - `str` o `function`: Métrica de distancia a usar en caso de de y sea una colección de vectores de observaciones.
    - **optimal_ordering** - `bool`: La matriz linkage será reordenada de manera que distancia entre 'hojas' consecutivas sea mínima.
- **Retorna:**
    - **Z**: `ndarray`.

**Uso**:

:::{attention}
Es recomendado que _y_ esté normalizado de alguna manera. Una opción es usar la función `scipy.cluster.vq.whiten()`, pero se podrían usar otras funciones de normalización.
:::

```python
# Importar función
from scipy.cluster.hierarchy import linkage

# Generar matriz Z
Z = linkage(df, method)
```