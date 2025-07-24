# Linear Algebra

Es un módulo que provee de funciones útiles para trabajar con matrices y otras estructuras y operaciones de álgebra lineal. Es posible importar solo el módulo o una función específica. Para usar este submódulo es necesario importarlo:

```python
# Importar linalg
from scipy import linalg

# Importar función específica
from scipy.linalg import function_name
```
- _function_name_ es el nombre de la función que se desea importar.

:::{note}
Para más información visitar la [documentación](https://docs.scipy.org/doc/scipy/reference/linalg.html) de _scipy_.
:::

:::{note}
Alternativamente revisar el módulo {doc}`../03-numpy/algebra-lineal` de _numpy_.
:::

A continuación se presenta un resumen de cada sección:
- **Basicos**: Funciones básicas para operaciones lineales, como multiplicación de matrices, inversión, normas y solución de sistemas lineales.
- **Descomposiciones** : Implementa descomposiciones matriciales, como LU, QR, Cholesky y SVD.
- **Eigenvalores y Eigenvectores**: Resuelve problemas de valores y vectores propios para matrices cuadradas.
- **Ecuaciones matriciales**: Resuelve ecuaciones matriciales como ecuaciones de Sylvester/Lyapunov y de Riccati.
- **Funciones de matrices**: Aplica funciones a matrices, como exponencial, logaritmo y raíz cuadrada matricial.
- **Matrices especialess**: Genera matrices especiales, como matrices de Toeplitz, Hankel, circulantes y de Vandermonde.
- **Proyecciones**: Incluye métodos para proyecciones aleatorias y esbozos (sketches) de matrices.
- **Rutinas de bajo nivel** : Contiene funciones de bajo nivel para operaciones específicas, como wrappers de LAPACK/BLAS.

<br/>

## Basicos

Funciones básicas para operaciones lineales, como multiplicación de matrices, inversión, normas y solución de sistemas lineales.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - **Principales funciones**
  - 
* - [det](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.det.html)(a, ...)
  - Calcula el determinante de una matriz.
* - [inv](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.inv.html)(a, ...)
  - Calcula el inverso de una matriz.
* - [ishermitian](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.ishermitian.html)(a, ...)
  - Comprueba si una matriz 2D cuadrada es hermitiana.
* - [issymmetric](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.issymmetric.html)(a, ...)
  - Comprueba si una matriz 2D cuadrada es simétrica.
* - [norm](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.norm.html)(a, ...)
  - Norma vectorial o matricial.
* - [solve](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.solve.html)(a, b, ...)
  - Resuelve el conjunto de ecuaciones lineales `a @ x == b` para la incógnita _x_.
* - **Otras funciones**
  - 
* - [bandwidth](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.bandwidth.html)(a)
  - Retorna el _bandwidth_ inferior y superior de una matriz numérica 2D.
* - [khatri_rao](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.khatri_rao.html)(a, b)
  - Producto Khatri-Rao.
* - [kron](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.kron.html)(a, b)
  - Producto de Kronecker.
* - [lstsq](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.lstsq.html)(a, b, ...)
  - Calcula la solución de mínimos cuadrados a la ecuación $Ax = b$.
* - [matmul_toeplitz](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.matmul_toeplitz.html)(c_or_cr, x, ...)
  - Multiplicación eficiente de matriz-matriz de Toeplitz usando FFT.
* - [matrix_balance](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.matrix_balance.html)(A, ...)
  - Calcula una transformación de similitud diagonal para el balance de fila/columna.
* - [orthogonal_procrustes](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.orthogonal_procrustes.html)(A, B, ...)
  - Calcula la solución del problema ortogonal (o unitario) de Procrustes de una matriz.
* - [pinv](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.pinv.html)(a, ...)
  - Calcula la pseudo-inversa (Moore-Penrose) de una matriz.
* - [pinvh](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.pinvh.html)(a, ...)
  - Calcula l pseudo-inversa (Moore-Penrose) de una matriz hermitiana.
* - [solve_banded](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.solve_banded.html)(l_and_u, ab, b, ...)
  - Resuelve la ecuación $Ax = b$ para _x_, suponiendo que _A_ es una matriz _banded_.
* - [solve_circulant](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.solve_circulant.html)(c, b, ...)
  - Resuelve $Cx = b$ para _x_, donde _C_ es una matriz circulante.
* - [solve_toeplitz](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.solve_toeplitz.html)(c_or_cr, b, ...)
  - Resuelve un sistema de Toeplitz utilizando la recursión de Levinson.
* - [solve_triangular](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.solve_triangular.html)(a, b, ...)
  - Resuelve la ecuación $Ax = b$ Para _x_, suponiendo que _A_ es una matriz triangular.
* - [solveh_banded](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.solveh_banded.html)(ab, b, ...)
  - Resuelve la ecuación $Ax = b$.
* - [subspace_angles](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.subspace_angles.html)(A, B)
  - Calcula los ángulos del subespacio entre dos matrices.
```

<br/>

## Descomposiciones

Implementa descomposiciones matriciales, como LU, QR, Cholesky y SVD.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - **Principales funciones**
  -
* - [cholesky](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.cholesky.html)(a, ...)
  - Calcula la descomposición de Cholesky de una matriz.
* - [lu](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.lu.html)(a, ...)
  - Calcula la descomposición de Lu de una matriz con pivote parcial.
* - [qr](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.qr.html)(a, ...)
  - Calcula la descomposición QR de una matriz.
* - [svd](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.svd.html)(a, ...)
  - Descomposición del valor singular.
* - **Otras funciones**
  - 
* - [cdf2rdf](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.cdf2rdf.html)(w, v)
  - Convierte eigenvectores `v` y eigenvalores `w` complejos en eigenvalores reales en un bloque diagonal `wr` y el eigenvector real asociado `vr`
* - [cho_factor](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.cho_factor.html)(a, ...)
  - Calcula la descomposición de Cholesky de una matriz, para usar en `cho_solve()`.
* - [cho_solve](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.cho_solve.html)(c_and_lower, b, ...)
  - Resuelve las ecuaciones lineales $Ax = b$, dada la factorización de Cholesky de _A_.
* - [cho_solve_banded](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.cho_solve_banded.html)(cb_and_lower, b, ...)
  - Resuelve las ecuaciones lineales $Ax = b$, dada la factorización de Cholesky del hermitiano con bandas _A_.
* - [cholesky_banded](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.cholesky_banded.html)(ab, ...)
  - Factorización Cholesky de una matriz definida positiva hermitiana con bandas.
* - [cossin](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.cossin.html)(X, ...)
  - Calcula la descomposición coseno-seno (CS) de una matriz ortogonal/unitaria.
* - [diagsvd](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.diagsvd.html)(s, M, N)
  - Construye la matriz sigma en SVD a partir de valores singulares y tamaño _M_, _N_.
* - [hessenberg](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.hessenberg.html)(a, ...)
  - Calcula la forma de Hessenberg de una matriz.
* - [ldl](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.ldl.html)(A, ...)
  - Calcula la factorización LDLT o Bunch-Kaufman de una matriz simétrica/ hermitiana.
* - [lu_factor](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.lu_factor.html)(a, ...)
  - Calcula la descomposición de Lu de una matriz.
* - [lu_solve](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.lu_solve.html)(lu_and_piv, b, ...)
  - Resuelve un sistema de ecuación, $Ax = b$, dada la factorización LU de _A_.
* - [null_space](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.null_space.html)(A, ...)
  - Construye una base ortonormal para el espacio nulo de _A_ usando SVD.
* - [ordqz](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.ordqz.html)(A, B, ...)
  - Descomposición de QZ para un par de matrices con reordenamiento.
* - [orth](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.orth.html)(A, ...)
  - Construye una base ortonormal para el rango de _A_ usando SVD.
* - [polar](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.polar.html)(a, ...)
  - Calcula la descomposición polar.
* - [qr_delete](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.qr_delete.html)(Q, R, k, int p=1, ...)
  - _QR Downdate_ en las eliminaciones de fila o columna.
* - [qr_insert](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.qr_insert.html)(Q, R, u, k, ...)
  - Actualización de QR en las inserciones de fila o columna.
* - [qr_multiply](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.qr_multiply.html)(a, c, ...)
  - Calcula la descomposición QR y multiplica _Q_ con una matriz.
* - [qr_update](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.qr_update.html)(Q, R, u, v, ...)
  - Actualización de Rank-K QR.
* - [qz](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.qz.html)(A, B, ...)
  - Descomposición de QZ para valores propios generalizados de un par de matrices.
* - [rq](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.rq.html)(a, ...)
  - Calcula la descomposición RQ de una matriz.
* - [rsf2csf](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.rsf2csf.html)(T, Z, ...)
  - Convierte la forma real de Schur en forma compleja de Schur.
* - [schur](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.schur.html)(a, ...)
  - Calcula la descomposición de Schur de una matriz.
* - [svdvals](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.svdvals.html)(a, ...)
  - Calcula los valores singulares de una matriz.
```

<br/>

## Eigenvalores y Eigenvectores

Resuelve problemas de valores y vectores propios para matrices cuadradas.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [eig](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.eig.html)(a, ...)
  - Resuelve un problema de valor propio ordinario o generalizado de una matriz cuadrada.
* - [eig_banded](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.eig_banded.html)(a_band, ...)
  - Resuelve un problema de valor propio de una matiz simétrica real o compleja hermitiana con bandas.
* - [eigh](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.eigh.html)(a, ...)
  - Resuelve un problema de valor propio estándar o generalizado para una matriz compleja hermética o simétrica real.
* - [eigh_tridiagonal](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.eigh_tridiagonal.html)(d, e, ...)
  - Resuelve el problema de valor propio para una matriz tridiagonal simétrica real.
* - [eigvals](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.eigvals.html)(a, ...)
  - Calcula los valores propios de un problema de valor propio ordinario o generalizado.
* - [eigvals_banded](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.eigvals_banded.html)(a_band, ...)
  - Resuelve un problema de valor propio dde una matiz simétrica real o compleja hermitiana con bandas.
* - [eigvalsh](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.eigvalsh.html)(a, ...)
  - Resuelve un problema de valor propio estándar o generalizado para una matiz simétrica real o compleja hermitiana con bandas. 
* - [eigvalsh_tridiagonal](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.eigvalsh_tridiagonal.html)(d, e, ...)
  - Resuelve el problema de valor propio para una matriz tridiagonal simétrica real.
```

<br/>

## Ecuaciones matriciales

Resuelve ecuaciones matriciales como ecuaciones de _Sylvester/Lyapunov_ y de _Riccati_.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [solve_continuous_are](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.solve_continuous_are.html)(a, b, q, r, ...)
  - Resuelve la ecuación de Riccati algebraico de tiempo continuo (CARE).
* - [solve_continuous_lyapunov](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.solve_continuous_lyapunov.html)(a, q)
  - Resuelve la ecuación continua de Lyapunov $AX + XA^H = Q$.
* - [solve_discrete_are](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.solve_discrete_are.html)(a, b, q, r, ...)
  - Resuelve la ecuación de Riccati algebraico de tiempo discreto (DARE).
* - [solve_discrete_lyapunov](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.solve_discrete_lyapunov.html)(a, q, ...)
  - Resuelve la ecuación discreta de Lyapunov $AXA^H - X + Q = 0$.
* - [solve_sylvester](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.solve_sylvester.html)(a, b, q)
  - Calcula una solución (_X_) a la ecuación de Sylvester $AX + XB = Q$.
```

<br/>

## Funciones de matrices

Aplica funciones a matrices, como exponencial, logaritmo y raíz cuadrada matricial.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [coshm](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.coshm.html)(A)
  - Calcula el coseno hiperbólico de una matriz.
* - [cosm](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.cosm.html)(A)
  - Calcula el coseno de una matriz.
* - [expm](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.expm.html)(A)
  - Calcula la matriz exponencial de un arreglo.
* - [expm_cond](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.expm_cond.html)(A, ...)
  - Número de condición relativa del exponencial de la matriz en la norma Frobenius.
* - [expm_frechet](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.expm_frechet.html)(A, E, ...)
  - Derivada de Frechet de la matriz exponencial de A en la dirección E.
* - [fractional_matrix_power](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.fractional_matrix_power.html)(A, t)
  - Calcula el potenciación fraccional de una matriz.
* - [funm](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.funm.html)(A, func, ...)
  - Evalua una función de matriz especificada por un `callable`.
* - [logm](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.logm.html)(A, ...)
  - Calcula el logatirmo de una matriz.
* - [signm](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.signm.html)(A, ...)
  - Función de signo de una matriz.
* - [sinhm](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.sinhm.html)(A)
  - Calcula el seno hiperbólico de una matriz.
* - [sinm](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.sinm.html)(A)
  - Calcula el seno de una matriz.
* - [sqrtm](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.sqrtm.html)(A, ...)
  - Calcula la raíz cuadrada de una matriz.
* - [tanhm](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.tanhm.html)(A)
  - Calcula la tangente hiperbólica de una matriz.
* - [tanm](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.tanm.html)(A)
  - Calcula la tangente de una matriz.
```
<br/>

## Matrices especiales

Genera matrices especiales, como matrices de Toeplitz, Hankel, circulantes y de Vandermonde.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [block_diag](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.block_diag.html)(*arrs)
  - Crea una matriz diagonal de bloque a partir de arrelgos proporcionados.
* - [circulant](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.circulant.html)(c)
  - Construye una matriz circulante.
* - [companion](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.companion.html)(a)
  - Crea una matriz complementaria.
* - [convolution_matrix](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.convolution_matrix.html)(a, n, ...)
  - Construye una matriz de convolución.
* - [dft](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.dft.html)(n, ...)
  - Matriz de transformación discreta de Fourier.
* - [fiedler](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.fiedler.html)(a)
  - Retorna una matriz simétrica de Fiedler.
* - [fiedler_companion](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.fiedler_companion.html)(a)
  - Retorna una matriz complementaria de Fiedler.
* - [hadamard](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.hadamard.html)(n, ...)
  - Construye una matriz de Hadamard.
* - [hankel](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.hankel.html)(c, ...)
  - Construye una matriz de Hankel.
* - [helmert](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.helmert.html)(n, ...)
  - Crea una matriz de Helmert de orden _n_.
* - [hilbert](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.hilbert.html)(n)
  - Crea una matriz de Hilbert de orden _n_.
* - [invhilbert](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.invhilbert.html)(n, ...)
  - Calcula el inverso de la matriz de Hilbert de orden _n_.
* - [invpascal](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.invpascal.html)(n, ...)
  - Retorna el inverso de la matriz Pascal _n x n_.
* - [leslie](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.leslie.html)(f, s)
  - Crea una matriz Leslie.
* - [pascal](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.pascal.html)(n, ...)
  - Retorna la matriz Pascal _n x n_.
* - [toeplitz](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.toeplitz.html)(c, ...)
  - Construye una matriz de Toeplitz.
```
<br/>

## Proyecciones

Incluye métodos para proyecciones aleatorias y esbozos (sketches) de matrices.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [clarkson_woodruff_transform](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.clarkson_woodruff_transform.html)(input_matrix, ...)
  - Aplica una transformación/_sketch_ Clarkson-WoodRuff a la matriz de entrada.
```

<br/>

## Rutinas de bajo nivel

Contiene funciones de bajo nivel para operaciones específicas, como wrappers de LAPACK/BLAS.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [find_best_blas_type](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.find_best_blas_type.html)([arrays, dtype])
  - Encuentra el mejor tipo de BLAS/LAPACK.
* - [get_blas_funcs](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.get_blas_funcs.html)(names, ...)
  - Retorna los objetos de función BLAS disponibles en _names_.
* - [get_lapack_funcs](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.get_lapack_funcs.html)(names, ...)
  - Retorna los objetos de función LAPACK disponibles en _names_.
```