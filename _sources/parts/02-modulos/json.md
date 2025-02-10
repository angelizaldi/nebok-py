# JSON

Es un módulo con protocolos para la serialización y deserialización de objetos de Python en _JSONs_. Es necesario importar el módulo.
```python
# Importar el módulo
import json
```

:::{attention}
En esta sección solo se revisan las funciones `json.dump()` y `json.load()`. Para un tratado más completo de este módulo visitar la [documentación](https://docs.python.org/3/library/json.html) de Python.
:::


<br>

---
## Exportar

La función `json.dump()` es útil para exportar objetos a _JSON_.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [dump](https://docs.python.org/3/library/json.html#json.dump)(obj, fp, ...)
  - Serialiaza _obj_ a JSON usando esta [tabla de conversión](https://docs.python.org/3/library/json.html#py-to-json-table).
```

<br>

Plantilla para exportar un objeto a _JSON_ usando un administrador de contextos.

```python
# Crear conexión, exportar y cerrar conexión
with open(filename, "w") as outfile:
    json.dump(X, outfile)
```
- _filename_ \- `path`, `str`: Es la ruta donde se exportará el archivo, incluyendo nombre y la extensión _.json_.
- _X_ \- `dict`: Objeto que se va a serializar.
- _outfile_ es un nombre opcional.

<br>

---
## Importar

La función `json.load()` es útil para importar archivos JSON como objetos de Python, generalmente como `dict`.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [load](https://docs.python.org/3/library/json.html#json.load)(fp, ...)
  - Deserializa _fp_ a un objeto de Python usando esta [tabla de conversión](https://docs.python.org/3/library/json.html#py-to-json-table, pero por default como `dict`.
```

<br>

Plantilla para importar un JSON en un objeto de Python usando un administrador de contextos.

```python
# Crear conexión, importar y cerrar conexión
with open(filename, "r") as json_file:
    X = json.load(json_file)
```
- _filename_ \- `path`, `str`: Es la ruta donde se exportará el archivo, incluyendo nombre y la extensión _.json_.
- _X_: objeto en el que se almacenará el JSON.
- _json_file_: Es un nombre opcional.



