# _Sparse_

El módulo sparse proporciona estructuras de datos y funciones para crear, manipular y operar con matrices dispersas de manera eficiente. Al trabajar con matrices dispersas, se ahorra memoria y se mejora el rendimiento, ya que solo se almacenan los elementos no nulos.

Para usar este submódulo es necesario importarlo:

```python
# Importar sparse
from scipy import sparse

# Importar clase específica
from scipy.sparse import ClassName

# Importar función específica
from scipy.sparse import function_name
```
- _function_name_/_ClassName_ es el nombre de la función o clase, respectivamente, que se desea importar.

:::{note}
Para más información visitar la [documentación](https://docs.scipy.org/doc/scipy/reference/sparse.html) de _scipy_.
:::

:::{warning}
En este sitio no se documentan todas las clases y funciones del módulo _sparse_. Tampoco se documentan los submódulos [csgraph](https://docs.scipy.org/doc/scipy/reference/sparse.csgraph.html#module-scipy.sparse.csgraph) y [lianlg](https://docs.scipy.org/doc/scipy/reference/sparse.linalg.html#module-scipy.sparse.linalg), este último es similar a {doc}`./linalg`, pero especial para arreglos dispersos.


Principalmente se documenta los arreglos de tipo _sparse_, que son la sustitución de las matrices de tipo _sparse_. Esto como parte de la migración de [spmatrix a sparray](https://docs.scipy.org/doc/scipy/reference/sparse.migration_to_sparray.html#migration-to-sparray).
:::


## Clases

Clases impementadas en el módulo _sparse_ del tipo _sparse array_.

```{list-table}
:header-rows: 1

* - Clase
  - Descripción
* - [bsr_array](https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.bsr_array.html)(arg1[,  shape,  dtype,  copy,  ...])
  - Una matriz dispersa de formato _Block Sparse Row_.
* - [coo_array](https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.coo_array.html)(arg1[,  shape,  dtype,  copy,  maxprint])
  - Una matriz dispersa en formato de coordenada.
* - [csc_array](https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.csc_array.html)(arg1[,  shape,  dtype,  copy,  maxprint])
  - Matriz de columna dispersa comprimida.
* - [csr_array](https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.csr_array.html)(arg1[,  shape,  dtype,  copy,  maxprint])
  - Matriz de fila dispersa comprimida.
* - [dia_array](https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.dia_array.html)(arg1[,  shape,  dtype,  copy,  maxprint])
  - Matriz dispersa con almacenamiento diagonal.
* - [dok_array](https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.dok_array.html)(arg1[,  shape,  dtype,  copy,  maxprint])
  - Diccionario de matrices dispersas basadas en llaves.
* - [lil_array](https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.lil_array.html)(arg1[,  shape,  dtype,  copy,  maxprint])
  - Matriz de fila dispersa Lista de listas.
* - [sparray](https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.sparray.html)()
  - Esta clase proporciona una clase base para todas las matrices dispersas.
```

<br/>

## Funciones

Funciones impementadas en el módulo _sparse_ del tipo _sparse array_.

### Construcción de matrices dispersas

Funciones para crear matrices dispersas a partir de datos densos, listas de coordenadas u otros formatos.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [block_array](https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.block_array.html)(blocks,  *[,  format,  dtype])
  - Construye una matriz dispersa a partir de _sub-blocks_ dispersos.
* - [diags_array](https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.diags_array.html)(diagonals,  /,  *[,  offsets,  ...])
  - Construye una matriz dispersa a partir de diagonales.
* - [eye_array](https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.eye_array.html)(m[,  n,  k,  dtype,  format])
  - Matriz de identidad en formato de matriz dispersa.
* - [random_array](https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.random_array.html)(shape,  *[,  density,  format,  ...])
  - Retorna una matriz dispersa de números uniformemente aleatorios en [0, 1).
```

<br/>

### Combinación de matrices

Funciones para combinar matrices dispersas, como concatenación horizontal, vertical o apilamiento. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [block_diag](https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.block_diag.html)(mats[,  format,  dtype])
  - Construye una matriz dispersa diagonal de bloque o una matriz a partir de las matrices proporcionadas.
* - [hstack](https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.hstack.html)(blocks[,  format,  dtype])
  - Apila matrices dispersas horizontalmente (_column wise_).
* - [kron](https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.kron.html)(A,  B[,  format])
  - Producto de Kronecker de matrices dispersas A y B.
* - [kronsum](https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.kronsum.html)(A,  B[,  format])
  - Suma Kronecker de matrices dispersas cuadradas A y B.
* - [tril](https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.tril.html)(A[,  k,  format])
  - Retorna la porción triangular inferior de una matriz o matriz dispersa.
* - [triu](https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.triu.html)(A[,  k,  format])
  - Retorna la porción triangular superior de una matriz o matriz dispersa.
* - [vstack](https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.vstack.html)(blocks[,  format,  dtype])
  - Apila matrices dispersas verticalmente (_row wise_).
```

<br/>

### Identificación de matrices dispersas

Funciones para verificar matrices dispersas.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [issparse](https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.issparse.html)(x)
  - ¿Es X de una matriz dispersa o tipo de matriz dispersa?.
```

<br/>

### Herramientas para matrices dispersas

Funciones de utilidad para manipular y operar con matrices dispersas.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [find](https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.find.html)(A)
  - Retorna los índices y valores de los elementos distintos de una matriz.
* - [get_index_dtype](https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.get_index_dtype.html)([arrays,  maxval,  check_contents])
  - Según las matrices de entrada (entero) _A_, determina un tipo de datos de índice adecuado que pueda contener los datos en las matrices.
* - [load_npz](https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.load_npz.html)(file)
  - Carga una matriz/matriz dispersa desde un archivo usando formato `.npz`.
* - [safely_cast_index_arrays](https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.safely_cast_index_arrays.html)(A[,  idx_dtype,  msg])
  - Convierte de forma segura índices de matriz dispersos a _idx_dtype_.
* - [save_npz](https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.save_npz.html)(file,  matrix[,  compressed])
  - Guarda una matriz o una matriz dispersa en un archivo usando formato `.npz`.
```