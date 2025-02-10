# Os.path

Este módulo provee de funcionalidades para trabajar con "_paths_". Es necesario importar el módulo
```python
# Importar el módulo
import os.path
```

:::{warning}
En esta sección solo se presentan algunas de las funciones del módulo `os.path`, para un tratado completo de este módulo visitar la [documentación](https://docs.python.org/3/library/os.path.html#module-os.path) de Python.
:::

<br>

---
## Concatenar paths

Función para concatenar _paths_. Basícamente concatena todos los argumentos con `/` como separador.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [join](https://docs.python.org/3/library/os.path.html#os.path.join)(path, *paths)
  - Concatena uno o más paths de manera inteligente.
```

<br>

## Información

Funciones que retornan información sobre el _path_. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [exists](https://docs.python.org/3/library/os.path.html#os.path.exists)(path)
  - Retorna `True` si _path_ se refiere a una ruta existente.
* - [isabs](https://docs.python.org/3/library/os.path.html#os.path.isabs)(path)
  - Retorna `True` si _path_ es una ruta de acceso absoluta.
* - [isdir](https://docs.python.org/3/library/os.path.html#os.path.isdir)(path)
  - Retorna `True` si _path_ es un directorio existente.
* - [isfile](https://docs.python.org/3/library/os.path.html#os.path.isfile)(path)
  - Retorna `True` si la ruta es un archivo regular existente.
* - [lexists](https://docs.python.org/3/library/os.path.html#os.path.lexists)(path)
  - Retorna `True` si _path_ hace referencia a una ruta existente.
* - [samefile](https://docs.python.org/3/library/os.path.html#os.path.samefile)(path1, path2)
  - Retorna `True` si ambos argumentos se refieren al mismo archivo o directorio.
```

<br>

## Partes de path

Funciones que retornan partes de un _path_.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [basename](https://docs.python.org/3/library/os.path.html#os.path.basename)(path)
  - Devuelve el nombre base de la ruta _path_. Por ejemplo, `basename('/foo/bar/')` retorna "bar".
* - [dirname](https://docs.python.org/3/library/os.path.html#os.path.dirname)(path)
  - Devuelve el nombre del directorio la ruta _path_. Por ejemplo, `dirname('foo/bar/baz')` retorna "foo/bar".
* - [split](https://docs.python.org/3/library/os.path.html#os.path.split)(path)
  - Divide _path_ en un par, _(head, tail)_ donde la cola es el el último componente de la ruta y el encabezado es todo lo que conduce a ese último componente. Por ejemplo, `split('foo/bar/bar/')` retorna `('foo/bar', 'baz')`.
```

