# os

Este módulo provee de funcionalidades para interactuar con el sistema operativo. Es necesario importar el módulo
```python
import os
```

:::{warning}
En esta sección solo se presentan algunas de las funciones del módulo `os`, para un tratado completo de este módulo visitar la [documentación](https://docs.python.org/3/library/os.html#module-os) de Python.
:::

<br>

---
## Crear directorios

Lista de funciones para crear directorios.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [makedirs](https://docs.python.org/3/library/os.html#os.makedirs)(name, mode=0o777, exist_ok=False)
  - Función recursiva de creación de directorios (un directorio con subdirectorios).
* - [mkdir](https://docs.python.org/3/library/os.html#os.mkdir)(path, mode=0o777, *, dir_fd=None)
  - Crea un directorio llamado `path`.
```

<br>

---
## Cambiar o recuperar ruta actual

Lista de funciones para recuperar o modificar la ruta del directorio actual. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [chdir](https://docs.python.org/3/library/os.html#os.chdir)(path)
  - Cambia el directorio de trabajo actual a `path`.
* - [chroot](https://docs.python.org/3/library/os.html#os.chroot)(path)
  - Cambiar el directorio "root" del proceso actual a `path`.
* - [getcwd](https://docs.python.org/3/library/os.html#os.getcwd)()
  - Devuelve una cadena que representa el directorio de trabajo actual.
```

<br>

---
## Eliminar archivos y directorios

Lista de funciones para eliminar archivos o directorios.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [remove](https://docs.python.org/3/library/os.html#os.remove)(path, *, dir_fd=None)
  - Elimina el archivo `path`. Si `path` es un directorio, se genera `OSError`.
* - [removedirs](https://docs.python.org/3/library/os.html#os.removedirs)(name)
  - Elimina directorios recursivamente. Por ejemplo, `os.removedirs('foo/bar/baz')` eliminará primero el directorio 'foo/bar/baz', y luego elimina 'foo/bar' y 'foo' si están vacíos.
* - [rmdir](https://docs.python.org/3/library/os.html#os.rmdir)(path, *, dir_fd=None)
  - Elimina el directorio `path`. Si el directorio no existe o no está vacío, se genera un `FileNotFoundError` o un `OSError` respectivamente.
```

<br>

---
## Enlistar

Función para enlistar el contenido de un directorio.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [listdir](https://docs.python.org/3/library/os.html#os.listdir)(path='.')
  - Retorna una lista que contiene los nombres de los archivos y directorios en el directorio dado por `path`.
```

<br>

---
## Renombrar archivos y directorios

Funciones para renombrar archivos o directorios.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [rename](https://docs.python.org/3/library/os.html#os.rename)(src, dst, *, src_dir_fd=None, dst_dir_fd=None)
  - Cambia el nombre de un archivo o directorio de `src` a `dst`. Si `dts` ya existe se produce un error `OSError`.
* - [renames](https://docs.python.org/3/library/os.html#os.renames)(old, new)
  - Función recursiva de cambio de nombre de directorio o archivo.
* - [replace](https://docs.python.org/3/library/os.html#os.replace)(src, dst, *, src_dir_fd=None, dst_dir_fd=None)
  - Cambia el nombre de un archivo o directorio de `src` a `dst`. Si `dst` es un directorio no vacío, se generará `OSError`. Si `dst` existe y es un archivo se reemplazará el archivo.
```

