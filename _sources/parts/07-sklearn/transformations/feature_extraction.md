# Feature Extraction

Proporciona métodos para extraer _features_ de datos no estructurados, como texto o imágenes, utilizando técnicas como _Bag of Words_ o _TF-IDF_. Para importar este módulo o una clase o función específica usar:

```python
# Importar módulo
from sklearn import feature_extraction

# Importar clase específica
from sklearn.feature_extraction import ClassName

# Importar función específica
from sklearn.feature_extraction import func_name
```
- _ClassName_ o _func_name_ es el nombre de la clase o función respectivamente.

:::{note}
Para más información de esta librería visitar la [documentación](https://scikit-learn.org/stable/api/sklearn.feature_extraction.html) de `sklearn`.
:::

<br/>

## Clases

Clases implementadas en el módulo `feature_extraction`.

```{list-table}
:header-rows: 1

* - Clase
  - Descripción
* - [DictVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.DictVectorizer.html)(...)
  - Transforma listas de valores de _features_ en vectores.
* - [FeatureHasher](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.FeatureHasher.html)(n_features=1048576, ...)
  - Implementa el _hashing_ de _features_, también conocido como el truco del _hashing_.
```

### DictVectorizer

[DictVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.DictVectorizer.html): Convierte diccionarios de _features_ (formato _clave-valor_) en una matriz numérica, útil para trabajar con datos categóricos o mixtos. Cada elemento de la lista es `dict` con el nombre del _feature_ `str` como llaves y el valor del _feature_ como valores (cada elemento de la lista es una muestra). Es útil para hacer _dummy variables_, porque los _feature_ con valores categóricos los convierte tipo `OneHotEncoder`. Es útil para preparación de datos categóricos para modelos de _machine learning_, como regresión lineal o árboles de decisión.
```python
# Sintaxis de llamada
DictVectorizer(*, dtype=numpy.float64, separator='=', sparse=True, sort=True)
```
**Parámetros:**
- **dtype** - `dtype`: El tipo de datos de los valores de los _feature_.
- **separator** - `str`: Cadena de separación usada al crear los nuevos _feature_ para los _one-hot-enconder_.
- **sparse** - `bool`: Para indicar si el método de trasformar debe de retornar _sparse matrix_.
- **sort** - `bool`: Para indicar que los atributos _feature_names\__ y _vocabulary\__ sean ordenados al momento de ajustar.

#### Atributos

Atributos de la clase `DictVectorizer`.

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - **feature_names_**
  - Un `list` de longitud _n_features_ que contiene los nombres de los _features_ (por ejemplo, _"f=ham"_ y _"f=spam"_).
* - **vocabulary_**
  - Un diccionario que asigna nombres de _features_ a índices de _features_.
```

#### Métodos

Métodos de la clase `DictVectorizer`.


```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [fit](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.DictVectorizer.html#sklearn.feature_extraction.DictVectorizer.fit)(X,  y=None)
  - Aprende un `list` de nombres de _features_ -> mapeos de índices.
* - [fit_transform](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.DictVectorizer.html#sklearn.feature_extraction.DictVectorizer.fit_transform)(X,  y=None)
  - Aprende un `list` de nombres de _features_ -> mapeos índices y transforma _X_.
* - [inverse_transform](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.DictVectorizer.html#sklearn.feature_extraction.DictVectorizer.inverse_transform)(X,  dict_type=<class 'dict'>)
  - Transforma una matriz o matriz dispersa _X_, a mapeos de _features_.
* - [restrict](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.DictVectorizer.html#sklearn.feature_extraction.DictVectorizer.restrict)(support,  indices=False)
  - Restringe los _features_ a aquellos en el soporte mediante la selección de _features_.
* - [transform](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.DictVectorizer.html#sklearn.feature_extraction.DictVectorizer.transform)(X)
  - Transforma los dicts _features_->valor en matrices o matrices dispersas.
```

<br/>

### Imágenes

Estas clases se enfocan en la extracción de _features_ a partir de imágenes.

```{list-table}
:header-rows: 1

* - Clase
  - Descripción
* - [image.PatchExtractor](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.image.PatchExtractor.html)(...)
  - Extrae parches de una colección de imágenes.
```

<br/>

### Texto

Estas clases se enfocan en la extracción de _features_ a partir de texto, convirtiendo documentos de texto en representaciones numéricas que pueden ser utilizadas por modelos de _machine learning_.

```{list-table}
:header-rows: 1

* - Clase
  - Descripción
* - [text.CountVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html)(...)
  - Convierte una colección de documentos de texto en una matriz de recuento de _tokens_.
* - [text.HashingVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.HashingVectorizer.html)(...)
  - Convierte una colección de documentos de texto en una matriz de ocurrencias de _tokens_.
* - [text.TfidfTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfTransformer.html)(...)
  - Transforma una matriz de recuento en una representación normalizada _TF_ o _TF-IDF_.
* - [text.TfidfVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html)(...)
  - Convierte una colección de documentos en bruto en una matriz de _features TF-IDF_.
```

<br/>

#### CountVectorizer

[text.CountVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html): Convierte una colección de documentos de texto en una matriz de conteos de palabras (_Bag of Words_). Cada fila representa un documento y cada columna una palabra.
```python
# Sintaxis de llamada
CountVectorizer(*, input='content', encoding='utf-8', decode_error='strict', 
                strip_accents=None, lowercase=True, preprocessor=None, tokenizer=None, 
                stop_words=None, token_pattern='(?u)\\b\\w\\w+\\b', ngram_range=(1, 1), 
                analyzer='word', max_df=1.0, min_df=1, max_features=None, vocabulary=None, 
                binary=False, dtype=numpy.int64)
```
**Parámetros:**
- **stop_words** - {`list`, 'english'}: Para indicar un conjunto de palabras a excluir del vocabulario, normalmente palabras comunes con poca trascendencia para los modelos como _'the', 'me', 'this'_, etc.
- **token_pattern** - `str` o `None`: Expresión regular que denota lo que constituye un “_token_”, solo se utiliza si `analyzer == 'word'`.
- **ngram_range** - `2-tuple`: Valores minimos y máximos para extraer _n-grams_.
- **max_df** - `float: (0.0, 1.0)` o `int`: Para indicar el número máximo de documentos en las que debe de aparecer una palabra para ser considerada en el vocabulario. Si es `float` entonces representa una proporción de documentos.
- **min_df** - `float: (0.0, 1.0)` o `int`: Para indicar el número minimo de documentos en las que debe de aparecer una palabra para ser considerada en el vocabulario. Si es `float` entonces representa una proporción de documentos.



##### Atributos

Atributos de la clase `CountVectorizer`.

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - **fixed_vocabulary_**
  - `True` si el usuario proporciona un vocabulario fijo de mapeos de términos a índices.
* - **vocabulary_**
  - Mapeo de términos a índices de _features_.
```

##### Métodos

Métodos de la clase `CountVectorizer`.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [build_analyzer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html#sklearn.feature_extraction.text.CountVectorizer.build_analyzer)()
  - Retorna un `callable` para procesar los datos de entrada.
* - [build_preprocessor](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html#sklearn.feature_extraction.text.CountVectorizer.build_preprocessor)()
  - Retorna una función para preprocesar el texto antes de la tokenización.
* - [build_tokenizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html#sklearn.feature_extraction.text.CountVectorizer.build_tokenizer)()
  - Retorna una función que divide una cadena en una secuencia de _tokens_.
* - [decode](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html#sklearn.feature_extraction.text.CountVectorizer.decode)(doc)
  - Decodifica la entrada en una cadena de símbolos unicode.
* - [fit](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html#sklearn.feature_extraction.text.CountVectorizer.fit)(raw_documents,  y=None)
  - Aprende un diccionario de vocabulario de todos los _tokens_ de los documentos sin procesar.
* - [fit_transform](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html#sklearn.feature_extraction.text.CountVectorizer.fit_transform)(raw_documents,  y=None)
  - Aprende el diccionario de vocabulario y devuelve la matriz documento-término.
* - [inverse_transform](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html#sklearn.feature_extraction.text.CountVectorizer.inverse_transform)(X)
  - Retorna términos por documento con entradas no nulas en _X_.
* - [transform](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html#sklearn.feature_extraction.text.CountVectorizer.transform)(raw_documents)
  - Transforma documentos en matriz documento-término.
```

<br/>

#### TfidfVectorizer

[text.TfidfVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html): Transforma una lista de documentos en una matriz de frecuencias de las palabras. Es similar a `CountVectorizer()` pero este en lugar del conteo, retorna una ponderación del conteo de las palabras dependiendo de qué tan seguido aparece una palabra (_token_). Existen una clase similar que toma como argumento el _bag-of-words_ de `CountVectorizer()` llamada `TfidTranformer()` y el _output_ es el similar que el de `TfidVectorizer()`.
```python
# Sintaxis de llamada
TfidfVectorizer(*, input='content', encoding='utf-8', decode_error='strict', 
                strip_accents=None, lowercase=True, preprocessor=None, tokenizer=None, 
                analyzer='word', stop_words=None, token_pattern='(?u)\\b\\w\\w+\\b', 
                ngram_range=(1, 1), max_df=1.0, min_df=1, max_features=None, vocabulary=None, 
                binary=False, dtype=numpy.float64, norm='l2', use_idf=True, 
                smooth_idf=True, sublinear_tf=False)
```

**Uso**

La forma básica de usar este clase es la siguiente:

```python
# Importar clase
from sklearn.feature_extraction.text import TfidfVectorizer

# Inicializar el vectorizador
vectorizer = TfidfVectorizer(stop_words)

# Ajustar el vectorizador
vectorizer.fit(X)  # X es una lista o array de textos

# Ajustar el vectorizador y transformar los datos de texto
X_tfidf = vectorizer.fit_transform(X)  # X es una lista o array de textos

# Transformar datos de texto
X_tfidf = vectorizer.transform(X) # X es una lista o array de textos

# Obtener los nombres de las características (palabras)
feature_names = vectorizer.get_feature_names_out()
```
- _X_tfidf_ será una matriz donde las filas representan documentos y las columnas representan palabras.

##### Atributos

Atributos de la clase `TfidfVectorizer`.

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - **fixed_vocabulary_**
  - `True` si el usuario proporciona un vocabulario fijo de correspondencias entre términos e índices.
* - **idf_**
  - Vector de frecuencia inversa de documentos, sólo definido si `use_idf=True`.
* - **vocabulary_**
  - Mapeo de términos a índices de _features_.
```

##### Métodos

Métodos de la clase `TfidfVectorizer`.

:::{note}
Al ajustar este modelo lo común es proporcionar un `iterable` de `str` o `file-object`, es decir, en esencia un `array-like` de textos y retornará una matriz _csr_ donde se indica para cada documento el _Tfidf_ de cada palabra (recuento de la palabra en el documentos por logaritmo del inverso de la frecuencia de la palabra, todo normalizado).
:::

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [build_analyzer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html#sklearn.feature_extraction.text.TfidfVectorizer.build_analyzer)()
  - Retorna un `callable` para procesar los datos de entrada.
* - [build_preprocessor](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html#sklearn.feature_extraction.text.TfidfVectorizer.build_preprocessor)()
  - Retorna una función para preprocesar el texto antes de la tokenización.
* - [build_tokenizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html#sklearn.feature_extraction.text.TfidfVectorizer.build_tokenizer)()
  - Retorna una función que divide una cadena en una secuencia de _tokens_.
* - [decode](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html#sklearn.feature_extraction.text.TfidfVectorizer.decode)(doc)
  - Decodifica la entrada en una cadena de símbolos unicode.
* - [fit](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html#sklearn.feature_extraction.text.TfidfVectorizer.fit)(raw_documents,  y=None)
  - Aprende vocabulario e _idf_ a partir del conjunto de entrenamiento.
* - [fit_transform](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html#sklearn.feature_extraction.text.TfidfVectorizer.fit_transform)(raw_documents,  y=None)
  - Aprende vocabulario e _idf_, retorna una matriz documento-término.
* - [inverse_transform](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html#sklearn.feature_extraction.text.TfidfVectorizer.inverse_transform)(X)
  - Retorna términos por documento con entradas no nulas en _X_.
* - [transform](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html#sklearn.feature_extraction.text.TfidfVectorizer.transform)(raw_documents)
  - Transforma documentos en una matriz documento-término.
```

<br/>

## Funciones - Imágenes

Funciones implementadas en el módulo `feature_extraction`. Estas funciones se enfocan en la extracción de _features_ a partir de imágenes.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [image.extract_patches_2d](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.image.extract_patches_2d.html)(image, patch_size, ...)
  - Transforma una imagen 2D en una colección de parches.
* - [image.grid_to_graph](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.image.grid_to_graph.html)(n_x, n_y, n_z=1, ...)
  - Gráfico de las conexiones píxel a píxel.
* - [image.img_to_graph](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.image.img_to_graph.html)(img, ...)
  - Gráfico de las conexiones de gradiente píxel a píxel.
* - [image.reconstruct_from_patches_2d](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.image.reconstruct_from_patches_2d.html)(patches, image_size)
  - Reconstruye la imagen a partir de todos sus parches.
```