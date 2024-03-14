# Lectura y escritura de datos

En esta sección se enlistan las funciones relacionadas con la lectura de datos en arrays o almacenar arrays en archivos locales .

:::{warning}
Para una lista completa visitar la [documentación](https://numpy.org/doc/stable/reference/routines.io.html#input-and-output) de `numpy`.
:::

---
## Archivos binarios

Funciones relacionadas con la lectura y escritura de _pickles_. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [load](https://numpy.org/doc/stable/reference/generated/numpy.load.html)(file[, mmap_mode, allow_pickle, ...])
  - Carga arreglos u objetos _pickle_ desde archivos `.npy`, `.npz` o `.pkl`.
* - [save](https://numpy.org/doc/stable/reference/generated/numpy.save.html)(file, arr[, allow_pickle, fix_imports])
  - Almacena un arreglo en un archivo binario en formato numpy `.npy`.
```

<br>

## Archivos binarios crudos

Funciones relacionadas con la lectura de archivos binarios crudos. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [fromfile](https://numpy.org/doc/stable/reference/generated/numpy.fromfile.html)(file[, dtype, count, sep, offset, like])
  - Construye un arreglo a partir de datos en un archivo de texto o binario.
```

<br>

## Archivos texto

Funciones relaciones con la lectura y escritura de archivos de texto. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [genfromtxt](https://numpy.org/doc/stable/reference/generated/numpy.genfromtxt.html)(fname[, dtype, comments, ...])
  - Carga datos desde un archivo de texto, con los valores faltantes manejados como se especifica.
* - [loadtxt](https://numpy.org/doc/stable/reference/generated/numpy.loadtxt.html)(fname[, dtype, comments, delimiter, ...])
  - Carga datos desde un archivo de texto.
* - [savetxt](https://numpy.org/doc/stable/reference/generated/numpy.savetxt.html)(fname, X[, fmt, delimiter, newline, ...])
  - Guarda un arreglo en un archivo de texto.
```

<br>