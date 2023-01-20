# JSON

Protocolos para la serialización y deserialización de objetos de Python en JSON's. Es necesario importarlo.
```python
import json
```

## Exportar

Para exportar un objeto de Python como un archivo `.json` se puede usar:

```python
# Crear conexión, exportar y cerrar conexión
with open(filename, "w") as outfile:
    json.dump(X, outfile)
```
- _filename_ \- `path`, `str`: Es la ruta donde se exportará el archivo, incluyendo nombre y la extensión `.json`.
- X `dict`: Objeto que se va a serializar.
- _outfile_ es un nombre opcional.

## Importar

Para importar un archivo `.json` y convertirlo a un objeto de Python, usar:

```python
with open(filename, ‘r’) as json_file:
    X = json.load(json_file)
```
- _filename_ \- `path`, `str`: Es la ruta donde se exportará el archivo, incluyendo nombre y la extensión `.json`.
- _X_ objeto en el que se almacenará el JSON.
- _json_file_ es un nombre opcional.
