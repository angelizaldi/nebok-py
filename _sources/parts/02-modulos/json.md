# JSON

Protocolos para la serialización y deserialización de objetos de Python en JSONs. Es necesario importar el módulo.
```python
import json
```

<br>

---
## Exportar

Función para exportar objetos a JSON.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [dump](https://docs.python.org/3/library/json.html#json.dump)(obj, fp, *, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw)
  - Serialiaza `obj` a JSON usando esta [tabla de conversión](https://docs.python.org/3/library/json.html#py-to-json-table).
```

<br>

Plantilla para exportar un objeto a JSON usando un administrador de contextos.

```python
# Crear conexión, exportar y cerrar conexión
with open(filename, "w") as outfile:
    json.dump(X, outfile)
```
- _filename_ \- `path`, `str`: Es la ruta donde se exportará el archivo, incluyendo nombre y la extensión `.json`.
- X \- `dict`: Objeto que se va a serializar.
- _outfile_ es un nombre opcional.

<br>

---
## Importar

Función para importar archivos JSON a objetos de Python.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [load](https://docs.python.org/3/library/json.html#json.load)(fp, *, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)
  - Deserializa `fp` a un objeto de Python usando esta [tabla de conversión](https://docs.python.org/3/library/json.html#py-to-json-table).
```

<br>

Plantilla para importar un JSON en un objeto de Python usando un administrador de contextos.

```python
# Crear conexión, importar y cerrar conexión
with open(filename, "r") as json_file:
    X = json.load(json_file)
```
- _filename_ \- `path`, `str`: Es la ruta donde se exportará el archivo, incluyendo nombre y la extensión `.json`.
- _X_: objeto en el que se almacenará el JSON.
- _json_file_: Es un nombre opcional.



