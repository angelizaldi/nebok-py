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

# Cluster

Incluye algoritmos de _clustering_, como _K-Means_ y _DBSCAN_, para agrupar datos en conjuntos basados en similitudes. Para importar este módulo o una clase o función específica usar:

```python
# Importar módulo
from sklearn import cluster

# Importar clase específica
from sklearn.cluster import ClassName

# Importar función específica
from sklearn.cluster import func_name
```
- _ClassName_ o _func_name_ es el nombre de la clase o función respectivamente.

:::{note}
Para más información de esta librería visitar la [documentación](https://scikit-learn.org/stable/api/sklearn.cluster.html) de `sklearn`.
:::

<br/>

(cluster-classes)=
## Clases

Clases implementadas en el módulo `cluster`.

```{list-table}
:header-rows: 1

* - Clase
  - Descripción
* - [AffinityPropagation](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AffinityPropagation.html)(...)
  - Realiza el _clusterin_ por _Affinity Propagation_ de los datos.
* - [AgglomerativeClustering](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html)(n_clusters=2, ...)
  - Agrupación aglomerativa.
* - [Birch](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.Birch.html)(...)
  - Implementa el algoritmo de agrupación BIRCH.
* - [BisectingKMeans](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.BisectingKMeans.html)(n_clusters=8, ...)
  - Agrupación en bisectriz de _K-Means_.
* - [DBSCAN](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html)(eps=0.5, ...)
  - Realiza el _clusterin_ DBSCAN a partir de una matriz de vectores o una matriz de distancias.
* - [FeatureAgglomeration](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.FeatureAgglomeration.html)(n_clusters=2, ...)
  - _Features_ aglomerados.
* - [HDBSCAN](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.HDBSCAN.html)(min_cluster_size=5, ...)
  - Agrupación de datos mediante agrupación jerárquica basada en la densidad.
* - [KMeans](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html)(n_clusters=8, ...)
  - Agrupación _K-Means_.
* - [MeanShift](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MeanShift.html)(...)
  - Agrupación por desplazamiento de la media utilizando un _kernel_ plano.
* - [MiniBatchKMeans](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MiniBatchKMeans.html)(n_clusters=8, ...)
  - _Mini-Batch K-Means_.
* - [OPTICS](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.OPTICS.html)(...)
  - Estimación de la estructura de agrupación a partir de la matriz de vectores.
* - [SpectralBiclustering](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralBiclustering.html)(n_clusters=3, ...)
  - _Biclustering_ espectral _(Kluger, 2003)_.
* - [SpectralClustering](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralClustering.html)(n_clusters=8, ...)
  - Aplica el _clusterin_ a una proyección del laplaciano normalizado.
* - [SpectralCoclustering](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralCoclustering.html)(n_clusters=3, ...)
  - Algoritmo _Spectral Co-Clustering (Dhillon, 2001)_.
```

<br/>

### KMeans

`sklearn.cluster.Kmeans()`: Implementa el algoritmo de _clustering K-Means_, que agrupa datos en _k clusters_ basándose en la distancia euclidiana. Es útil para segmentación de clientes, agrupamiento de imágenes, reducción de dimensionalidad visual.
```python
# Sintaxis de llamada
Kmeans(n_clusters=8, *, init='k-means++', n_init='auto', max_iter=300, tol=0.0001, 
       verbose=0, random_state=None, copy_x=True, algorithm='lloyd')
```
**Parámetros:**
- **n_cluster** - `int`: El número de clasificaciones que hará el modelo, así como el número de _centroides_ a generar.
- **n_init** - `int`: Número de veces que el algoritmo se ejecutará con diferente semilla para los _centroides_. El resultado final será el que tenga mejor _output_ en términos de la _inertia_.

:::{tip}
Alternativamente revisar {ref}`hierarchy-functions`, particularmente `linkage()` y `fclusters()`.
:::

#### Uso

La forma básica de usar este clase es la siguiente:

```python
# Importar clase
from sklearn.cluster import Kmeans

# Inicializar modelo
model = KMeans(n_clusters)

# Ajustar modelo
model.fit(X)

# Predecir clusters
labels = model.predict(X) # o new_X

# Ajustar y predecir al mismo tiempo
labels = model.fit_predict(samples)

# Evaluar calidad de clusters
model.inertia_
```

<br/>

Patrones útiles:
```python
# Graficar centroides
plt.scatter(xs, ys, c = labels, alpha = 0.5) # labels son etiquetas reales de cada punto
centroids = model.cluster_centers_
centroids_x = centroids[:,0]
centroids_y = centroids[:,1]
plt.scatter(centroids_x, centroids_y, marker = 'D', s=50)
plt.show()

# Graficar inercia
ks = range(1, 6)
inertias = []
for k in ks:
    model = KMeans(n_clusters = k)
    model.fit(samples)
    inertias.append(model.inertia_)
    
plt.plot(ks, inertias, '-o')
plt.xlabel('number of clusters, k')
plt.ylabel('inertia')
plt.xticks(ks)
plt.show()

# Crear crosstab de predicciones vs labels reales
model = KMeans(n_clusters = 3)
labels = model.fit_predict(samples)
df = pd.DataFrame({'labels': labels, 'real_labels': real_labels})
ct = pd.crosstab(df['labels'], df['real_labels'])
print(ct)
```
- Para elegir el mejor número de clusters se pueden graficar la _inercía_ para varíos números de clusters y cuando la inercia empiece a decaer más lentamente puede ser una buena opción (gráfica con forma de "codo").

<br/>

**Ejemplo**

En este ejemplo se crean 3 _clusters_ y se gráfica un diagrama de dispersión que indica el _cluster_ asignado y su etiqueta real.

```{code-cell} ipython3
# Importaciones
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.cluster import KMeans

# Cargar dataset
iris = sns.load_dataset('iris')
X = iris.iloc[:, :4].values 

# Aplicar Kmean con 3 clusters
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
cluster_labels = kmeans.fit_predict(X)

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

#### Atributos

Atributos de la clase `KMeans`.

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - **cluster_centers_**
  - Coordenadas de los centros de los _clusters_. Si el algoritmo se detiene antes de converger completamente (ver _tol_ y _max_iter_), estas no serán consistentes con _labels\__.
* - **feature_names_in_**
  - Nombres de los _features_ observados durante el ajuste. Definido sólo cuando _X_ tiene nombres que son todos cadenas.
* - **inertia_**
  - Suma de las distancias al cuadrado de las muestras a su centro de _cluster_ más cercano, ponderada por los pesos de la muestra si se han proporcionado.
* - **labels_**
  - Etiquetas de cada punto.
* - **n_features_in_**
  - Número de _features_ vistos durante el ajuste.
* - **n_iter_**
  - Número de iteraciones realizadas.
```

#### Métodos

Métodos de la clase `KMeans`.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [fit](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans.fit)(X,  y=None,  sample_weight=None)
  - Calcula el _clusterin K-means_.
* - [fit_predict](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans.fit_predict)(X,  y=None,  sample_weight=None)
  - Calcula los centros de _clusters_ y predice el índice de _clusters_ para cada muestra.
* - [fit_transform](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans.fit_transform)(X,  y=None,  sample_weight=None)
  - Calcula el _clusterin_ y transforma _X_ en un espacio de distancia de agrupación.
* - [predict](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans.predict)(X)
  - Predice el _cluster_ más cercano al que pertenece cada muestra de _X_.
* - [score](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans.score)(X,  y=None,  sample_weight=None)
  - Opuesto al valor de _X_ en el objetivo _K-means_.
* - [transform](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans.transform)(X)
  - Transforma _X_ en un espacio de distancia de _clusters_.
```

<br/>

## Funciones

Funciones implementadas en el módulo `cluster`.

```{list-table}
:header-rows: 1

* - Clase
  - Descripción
* - [affinity_propagation](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.affinity_propagation.html)(S, ...)
  - Realiza el _clusterin_ por _Affinity Propagation_ de los datos.
* - [cluster_optics_dbscan](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.cluster_optics_dbscan.html)(...)
  - Realiza la extracción DBSCAN para una épsilon arbitrario.
* - [cluster_optics_xi](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.cluster_optics_xi.html)(...)
  - Extrae automáticamente los _clusters_ según el método _Xi-steep_.
* - [compute_optics_graph](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.compute_optics_graph.html)(X, ...)
  - Calcula el grafo de alcanzabilidad OPTICS.
* - [dbscan](https://scikit-learn.org/stable/modules/generated/dbscan-function.html)()
  - Realiza el _clusterin_ DBSCAN a partir de una matriz de vectores o una matriz de distancias.
* - [estimate_bandwidth](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.estimate_bandwidth.html)(X, ...)
  - Calcula el _bandwidth_ que se utilizará con el algoritmo de desplazamiento medio.
* - [k_means](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.k_means.html)(X, n_clusters, ...)
  - Ejecutar el algoritmo de agrupación _K-Means_.
* - [kmeans_plusplus](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.kmeans_plusplus.html)(X, n_clusters, ...)
  - Inicializa semillas _n_clusters_ según _K-Means++_.
* - [mean_shift](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.mean_shift.html)(X, ...)
  - Realiza el _clusterin_ por desplazamiento medio de los datos utilizando un kernel plano.
* - [spectral_clustering](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.spectral_clustering.html)(affinity, ...)
  - Aplica el _clusterin_ a una proyección del laplaciano normalizado.
* - [ward_tree](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.ward_tree.html)(X, ...)
  - Agrupación de _Ward_ basada en una matriz de _features_.
```