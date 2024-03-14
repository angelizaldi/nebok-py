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
- Los arrays deben de satisfacer que el número de columnas de `array1` debe ser igual al número de filas de `array2`, es decir, si `array1` tiene shape `(m, k)`, entonces `array2` debe tener shape `(k, n)`, donde $m$, $k$ y $n$ son cualquier número entero.
- Si `array1` tiene shape `(m, k)` y `array2` tiene shape `(k, n)`, entonces `array1 @ array2` tiene shape `(m, n)`.

<br>


---
## Eigenvalores

Funciones para cálculos de eigenvalores y eigenvectores (valores propios y vectores propios). 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [linalg.eig](https://numpy.org/doc/stable/reference/generated/numpy.linalg.eig.html)(a)
  - Calcula los valores propios y los vectores propios de una matriz cuadrada.
* - [linalg.eigh](https://numpy.org/doc/stable/reference/generated/numpy.linalg.eigh.html)(a[, UPLO])
  - Devuelve los valores propios y los vectores propios de una matriz hermitiana compleja (simétrica conjugada) o una matriz simétrica real.
* - [linalg.eigvals](https://numpy.org/doc/stable/reference/generated/numpy.linalg.eigvals.html)(a)
  - Calcula los valores propios de una matriz general.
* - [linalg.eigvalsh](https://numpy.org/doc/stable/reference/generated/numpy.linalg.eigvalsh.html)(a[, UPLO])
  - Calcula los valores propios de una matriz hermitiana compleja o simétrica real.
```

<br>

## Factorizaciones

Funciones para factorizaciones (descomposiciones) de matrices. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [linalg.cholesky](https://numpy.org/doc/stable/reference/generated/numpy.linalg.cholesky.html)(a)
  - Descomposición de Cholesky.
* - [linalg.qr](https://numpy.org/doc/stable/reference/generated/numpy.linalg.qr.html)(a[, mode])
  - Calcula la factorización qr de una matriz.
* - [linalg.svd](https://numpy.org/doc/stable/reference/generated/numpy.linalg.svd.html)(a[, full_matrices, compute_uv, ...])
  - Descomposición en valores singulares.
```

<br>

## Inversas y sistemas

Funciones para cálculo de inversas y para solución de sistemas de ecuaciones lineales. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [linalg.inv](https://numpy.org/doc/stable/reference/generated/numpy.linalg.inv.html)(a)
  - Calcular la inversa de una matriz.
* - [linalg.lstsq](https://numpy.org/doc/stable/reference/generated/numpy.linalg.lstsq.html)(a, b[, rcond])
  - Devuelve la solución de mínimos cuadrados a una ecuación matricial lineal.
* - [linalg.pinv](https://numpy.org/doc/stable/reference/generated/numpy.linalg.pinv.html)(a[, rcond, hermitian])
  - Calcula la pseudo-inversa (Moore-Penrose) de una matriz.
* - [linalg.solve](https://numpy.org/doc/stable/reference/generated/numpy.linalg.solve.html)(a, b)
  - Resuelve una ecuación matricial lineal o un sistema de ecuaciones escalares lineales.
* - [linalg.tensorinv](https://numpy.org/doc/stable/reference/generated/numpy.linalg.tensorinv.html)(a[, ind])
  - Calcula la inversa de una arreglo N-dimensional.
* - [linalg.tensorsolve](https://numpy.org/doc/stable/reference/generated/numpy.linalg.tensorsolve.html)(a, b[, axes])
  - Resuelve la ecuación tensorial `a x = b` para `x`.
```

<br>

## Normas, determinantes y trazas

Funciones para cálculo de normas y otros cálculos como determinantes, trazas y rango. 

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
- Notar que la función `trace()` no pertenece al módulo `linalg`.

<br>

## Productos

Funciones para cálculos de productos entre matrices y vectores, como el producto punto, productos matriciales y el producto cruz, entre otros. 

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
  - Producto de Kronecker de dos matrices.
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
