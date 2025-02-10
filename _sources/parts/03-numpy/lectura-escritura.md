# Lectura y escritura de datos

En esta sección se enlistan las funciones relacionadas con la lectura de datos en _arrays_ o almacenar _arrays_ en archivos locales.

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

Funciones relaciones con la lectura y escritura de archivos de texto (_.txt_, _.csv_, etc.). 

:::{caution}
Tener en cuenta los siguiente al trabajar con estas funciones:
- Se debe especificar el separador del archivo con el parámetro _delimiter_
- Es recomendado que los archivos tengan solo datos numéricos, en caso de que tenga otra clase de datos se debe de especificar el tipo con el parámetro _dtype_.
:::

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [genfromtxt](https://numpy.org/doc/stable/reference/generated/numpy.genfromtxt.html)(fname[, dtype, comments, ...])
  - Carga datos desde un archivo de texto, con los valores faltantes manejados como se especifica.
* - [loadtxt](https://numpy.org/doc/stable/reference/generated/numpy.loadtxt.html)(fname[, dtype, comments, delimiter, ...])
  - Carga datos desde un archivo de texto.
* - [savetxt](https://numpy.org/doc/stable/reference/generated/numpy.savetxt.html)(fname, X[, fmt, delimiter, newline, ...])
  - Guarda un arreglo en un archivo de texto. Por default la función espera que los datos sean numéricos, para almacenar otro tipo de datos o en diferentes formatos usar el parámetro _fmt_.
```

<br>