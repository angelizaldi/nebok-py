# Pickle

Protocolos para la serialización y deserialización de objetos de Python en `pickles` (únicamente se pueden usar dentro de Python). Es necesario importarlo.
```python
import pickle
```

---
## Exportar

Para convertir un objeto a un `pickle` usar:

```python
with open(filename, 'wb') as outfile:
    pickle.dump(X, outfile)
```
- _filename_ \- `str`, `path-like`: Es la ruta donde se exportará el archivo, incluyendo nombre y la extensión pkl.
- _X_ \- `object`: Objeto se que se va a serializar como `pickle`.
- _outfile_ es un nombre opcional.

---
## Importar
    
Para importar un `pickle` a Python usar:

```python
with open(filename, 'rb') as infile:
    X = pickle.load(infile)
```
- _filename_ \- `str`, `path-like`: Es la ruta donde está el pickle, incluyendo nombre y la extensión pkl.
- _X_ \- `object`: Objeto donde se almacenará el pickle.
- _infile_ es un nombre opcional.
