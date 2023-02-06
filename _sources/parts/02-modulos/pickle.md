# Pickle

Protocolos para la serialización y deserialización de objetos de Python en `pickles` (únicamente se pueden usar dentro de Python). Es necesario importar el módulo.
```python
import pickle
```

<br>

---
## Exportar

Función para exportar objetos a pickles.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [dump](https://docs.python.org/3/library/pickle.html#pickle.dump)(obj, file, protocol=None, *, fix_imports=True, buffer_callback=None)
  - Exporta una representación en `pickle` de un objeto de Python.
```

<br>

Plantilla para exportar un objeto a `pickle` usando un administrador de contextos.

```python
with open(filename, 'wb') as outfile:
    pickle.dump(X, outfile)
```
- _filename_ \- `str`, `path-like`: Es la ruta donde se exportará el archivo, incluyendo nombre y la extensión `.pkl`.
- _X_ \- `object`: Objeto se que se va a serializar como `pickle`.
- _outfile_ es un nombre opcional.

<br><br>

---
## Importar

Función para importar pickles en objetos de Python.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [load](https://docs.python.org/3/library/pickle.html#pickle.load)(file, *, fix_imports=True, encoding='ASCII', errors='strict', buffers=None)
  - Importa un `pickle` como un objeto de Python.
```

<br>

Plantilla para importar un `pickle` en un objeto de Python usando un administrador de contextos.

```python
with open(filename, 'rb') as infile:
    X = pickle.load(infile)
```
- _filename_ \- `str`, `path-like`: Es la ruta donde está el pickle, incluyendo nombre y la extensión `.pkl`.
- _X_ \- `object`: Objeto donde se almacenará el pickle.
- _infile_ es un nombre opcional.