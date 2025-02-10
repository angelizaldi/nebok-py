# Módulo linalg

`numpy.linalg` es un módulo que provee de funciones útiles para trabajar con matrices y otras estructuras y operaciones de álgebra lineal. Es posible importar solo el módulo o una función específica.

```python
# Importar el módulo
from numpy import linalg

# Importar una función específica
from numpy.linalg import function_name
```
- _function_name_ es el nombre de la función que se desea importar.
- Si se importa todo el módulo es necesario usar `linalg.function_name()` cada vez que se llame a una función el módulo.
- Si se usa `import numpy as np` y se desea usar una función del módulo `linalg`, entonces se debe usar `np.linalg.function_name()`.


:::{attention}
Para más información de este módulo visitar la [documentación](https://numpy.org/doc/stable/reference/routines.linalg.html#linear-algebra-numpy-linalg) de `numpy`.
:::

<br>

---
## Operador @

El operador `@` es un operador especial de `numpy` que permite realizar multiplicaciones entre matrices. 

```python
# Uso del operador @
array1 @ array2
```
- La multiplacación se debe realizar entre arrays 2D.
- Los arrays deben de satisfacer que el número de columnas de _array1_ debe ser igual al número de filas de _array2_, es decir, si _array1_ tiene shape _(m, k)_, entonces _array2_ debe tener shape _(k, n)_, donde $m$, $k$ y $n$ son cualquier número entero.
- Si _array1_ tiene shape _(m, k)_ y _array2_ tiene shape _(k, n)_, entonces `array1 @ array2` tiene shape _(m, n)_.

<br>


---
## Eigenvalores

Funciones para cálculos de eigenvalores y eigenvectores ([valores propios y vectores propios](https://es.wikipedia.org/wiki/Vector,_valor_y_espacio_propios)). 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [linalg.eig](https://numpy.org/doc/stable/reference/generated/numpy.linalg.eig.html)(a)
  - Calcula los valores propios y los vectores propios de una matriz cuadrada.
* - [linalg.eigh](https://numpy.org/doc/stable/reference/generated/numpy.linalg.eigh.html)(a[, UPLO])
  - Devuelve los valores propios y los vectores propios de una [matriz hermitiana compleja](https://en.wikipedia.org/wiki/Hermitian_matrix) (simétrica conjugada) o una [matriz simétrica real](https://en.wikipedia.org/wiki/Symmetric_matrix).
* - [linalg.eigvals](https://numpy.org/doc/stable/reference/generated/numpy.linalg.eigvals.html)(a)
  - Calcula los valores propios de una matriz general.
* - [linalg.eigvalsh](https://numpy.org/doc/stable/reference/generated/numpy.linalg.eigvalsh.html)(a[, UPLO])
  - Calcula los valores propios de una [matriz hermitiana compleja](https://en.wikipedia.org/wiki/Hermitian_matrix) o [matriz simétrica real](https://en.wikipedia.org/wiki/Symmetric_matrix).
```

<br>

## Factorizaciones

Funciones para factorizaciones (descomposiciones) de matrices. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [linalg.cholesky](https://numpy.org/doc/stable/reference/generated/numpy.linalg.cholesky.html)(a)
  - [Descomposición de Cholesky](https://es.wikipedia.org/wiki/Factorizaci%C3%B3n_de_Cholesky).
* - [linalg.qr](https://numpy.org/doc/stable/reference/generated/numpy.linalg.qr.html)(a[, mode])
  - Calcula la [factorización QR](https://es.wikipedia.org/wiki/Factorizaci%C3%B3n_QR) de una matriz.
* - [linalg.svd](https://numpy.org/doc/stable/reference/generated/numpy.linalg.svd.html)(a[, full_matrices, compute_uv, ...])
  - Descomposición en valores singulares.
```

<br>

## Inversas y sistemas

Funciones para cálculo de [inversas](https://en.wikipedia.org/wiki/Invertible_matrix) y para solución de sistemas de ecuaciones lineales. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [linalg.inv](https://numpy.org/doc/stable/reference/generated/numpy.linalg.inv.html)(a)
  - Calcular la inversa de una matriz.
* - [linalg.lstsq](https://numpy.org/doc/stable/reference/generated/numpy.linalg.lstsq.html)(a, b[, rcond])
  - Devuelve la solución de mínimos cuadrados a una ecuación matricial lineal.
* - [linalg.pinv](https://numpy.org/doc/stable/reference/generated/numpy.linalg.pinv.html)(a[, rcond, hermitian])
  - Calcula la pseudo-inversa ([Moore-Penrose](https://en.wikipedia.org/wiki/Moore%E2%80%93Penrose_inverse)) de una matriz.
* - [linalg.solve](https://numpy.org/doc/stable/reference/generated/numpy.linalg.solve.html)(a, b)
  - Resuelve una ecuación matricial lineal o un sistema de ecuaciones escalares lineales.
* - [linalg.tensorinv](https://numpy.org/doc/stable/reference/generated/numpy.linalg.tensorinv.html)(a[, ind])
  - Calcula la inversa de una arreglo N-dimensional.
* - [linalg.tensorsolve](https://numpy.org/doc/stable/reference/generated/numpy.linalg.tensorsolve.html)(a, b[, axes])
  - Resuelve la ecuación tensorial `a x = b` para `x`.
```

<br>

## Normas, determinantes y trazas

Funciones para cálculo de [normas](https://en.wikipedia.org/wiki/Matrix_norm) y otros cálculos como [determinantes](https://en.wikipedia.org/wiki/Determinant), [trazas](https://en.wikipedia.org/wiki/Trace_(linear_algebra)) y [rango](https://en.wikipedia.org/wiki/Row_and_column_spaces). 


:::{note}
Notar que la función `trace()` no pertenece al módulo `linalg`.
:::

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [linalg.det](https://numpy.org/doc/stable/reference/generated/numpy.linalg.det.html)(a)
  - Calcula el determinante de una matriz.
* - [linalg.matrix_rank](https://numpy.org/doc/stable/reference/generated/numpy.linalg.matrix_rank.html)(A[, tol, hermitian])
  - Devuelve el rango de matriz de la matriz usando el método SVD.
* - [linalg.norm](https://numpy.org/doc/stable/reference/generated/numpy.linalg.norm.html)(x[, ord, axis, keepdims])
  - Calcula la norma matricial o vectorial.
* - [linalg.slogdet](https://numpy.org/doc/stable/reference/generated/numpy.linalg.slogdet.html)(a)
  - Calcula el signo y el logaritmo (natural) del determinante de una matriz.
* - [trace](https://numpy.org/doc/stable/reference/generated/numpy.trace.html)(a[, offset, axis1, axis2, dtype, out])
  - Devuelve la suma a lo largo de las diagonales de la matriz.
```

<br>

## Productos

Funciones para cálculos de productos entre matrices y vectores, como el [producto punto](https://en.wikipedia.org/wiki/Dot_product), [productos matriciales](https://en.wikipedia.org/wiki/Matrix_multiplication) y el [producto cruz](https://en.wikipedia.org/wiki/Cross_product), entre otros. 

:::{note}
Notar que no todas las funciones enlistadas a continuación pertenecen al módulo `linalg`, únicamente aquellas cuyo nombre están de la forma `linalg.func_name`.
:::


```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [cross](https://numpy.org/doc/stable/reference/generated/numpy.cross.html)(a, b[, axisa, axisb, axisc, axis])
  - Devuelve el producto cruz de dos vectores.
* - [dot](https://numpy.org/doc/stable/reference/generated/numpy.dot.html)(a, b[, out])
  - Producto escalar de dos matrices.
* - [inner](https://numpy.org/doc/stable/reference/generated/numpy.inner.html)(a, b, /)
  - Producto interno de dos arreglos.
* - [kron](https://numpy.org/doc/stable/reference/generated/numpy.kron.html)(a, b)
  - Producto de [Kronecker](https://en.wikipedia.org/wiki/Kronecker_product) de dos matrices.
* - [linalg.matrix_power](https://numpy.org/doc/stable/reference/generated/numpy.linalg.matrix_power.html)(a, n)
  - Eleva una matriz cuadrada a la potencia (entera) n.
* - [linalg.multi_dot](https://numpy.org/doc/stable/reference/generated/numpy.linalg.multi_dot.html)(arrays, *[, out])
  - Calcule el producto punto de dos o más matrices en una sola llamada de función.
* - [matmul](https://numpy.org/doc/stable/reference/generated/numpy.matmul.html)(x1, x2, /[, out, casting, order, ...])
  - Producto matricial de dos arreglos.
* - [outer](https://numpy.org/doc/stable/reference/generated/numpy.outer.html)(a, b[, out])
  - Calcular el producto externo de dos vectores. El producto externo es igual al producto de cada par ordenado del producto cartesiano de dos vectores.
* - [tensordot](https://numpy.org/doc/stable/reference/generated/numpy.tensordot.html)(a, b[, axes])
  - Calcula el producto escalar del tensor a lo largo de los ejes especificados.
* - [vdot](https://numpy.org/doc/stable/reference/generated/numpy.vdot.html)(a, b, /)
  - Devuelve el producto escalar de dos vectores.
```
