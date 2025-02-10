# Pickle

Módulo con protocolos para la serialización y deserialización de objetos de Python en `pickles` (únicamente se pueden usar dentro de Python). Es necesario importar el módulo.

```python
# Importar el módulo
import pickle
```

:::{attention}
En esta sección solo se revisan las funciones `pickle.dump()` y `pickle.load()`. Para un tratado más completo de este módulo visitar la [documentación](https://docs.python.org/3/library/pickle.html) de Python.
:::


<br>

---
## Exportar

La función `pickle.dump()` es útil para exportar objetos de Python a _pickles_.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [dump](https://docs.python.org/3/library/pickle.html#pickle.dump)(obj, file, protocol=None, *, fix_imports=True, buffer_callback=None)
  - Exporta una representación en _pickle_ de un objeto de Python.
```

<br>

Plantilla para exportar un objeto a _pickle_ usando un administrador de contextos.

```python
# Importar módulo
import pickle

# Crear conexión, exportar y cerrar conexión
with open(filename, 'wb') as outfile:
    pickle.dump(X, outfile)
```
- _filename_ \- `str`, `path-like`: Es la ruta donde se exportará el archivo, incluyendo nombre y la extensión _.pkl_.
- _X_ \- `object`: Objeto se que se va a serializar como _pickle_.
- _outfile_ es un nombre opcional.

<br>

---
## Importar

La función `pickle.load()` es útil  para importar _pickles_ en objetos de Python.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [load](https://docs.python.org/3/library/pickle.html#pickle.load)(file, *, fix_imports=True, encoding='ASCII', errors='strict', buffers=None)
  - Importa un _pickle_ como un objeto de Python.
```

<br>

Plantilla para importar un _pickle_ en un objeto de Python usando un administrador de contextos.

```python
# Importar módulo
import pickle

# Crear conexión, importar y cerrar conexión
with open(filename, 'rb') as infile:
    X = pickle.load(infile)
```
- _filename_ \- `str`, `path-like`: Es la ruta donde está el pickle, incluyendo nombre y la extensión _.pkl_.
- _X_ \- `object`: Objeto donde se almacenará el pickle.
- _infile_ es un nombre opcional.