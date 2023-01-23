# Numpy

`numpy` es una librería que se utiliza principalmente para computo científico en Python. Contiene el objeto `ndarray` que permite trabajar con arrays multidimensionales, con los cuales se pueden hacer calculos vectorizados (elemento con elemento) de manera similar a los vectores en R. Además contiene una gran cantidad de funciones para operaciones matemáticas, álgebra lineal, estádistica, manipulación de arrays entre muchos otros. 

Para utilizar `numpy` es necesario instalarlo. Desde la terminal usar:
```
# Con pip
pip install numpy

# Con conda
conda install numpy
```

Una vez instalado se debe de importar
```python
import numpy as np
```
- `np` es el nombre por convención.
- En todo el documento se utilizará `np` para hacer referencia a numpy.

Para conocer la versión de `numpy` instalada usar:
```python
np.__version__ 
```

## Creación de arrays

Los arrays son objetos que pueden almacenar distintos valores del mismo tipo de dato en _n_ dimensiones. Existen diversas formas de crear arrays. 
1. Convertir secuencias de Python a `ndarray`.
2. Funciones especiales de `numpy` para crear `ndarray`.
3. Concatenando otros `ndarray`.
4. Impotar datos desde un sitio externo o la computadora con funciones especiales
5. Creación de matrices a partir de bytes sin procesar mediante el uso de cadenas o búferes
6. Otras funciones especiales para crear arrays.

En esta sección solo se presentará la opción 1. usando la función `np.array()`. Para más información visitar la [Guía de usuario](https://numpy.org/doc/stable/user/basics.creation.html#array-creation) de `numpy`.


Cualquier objeto de Python que sea una secuencia (`list`, `tuple`, `set`, `str`, `range`, entre otros) se puede convertir a un objeto `numpy.ndarray` con la función :

```python
a = np.array(X)
```
- _X_ \- `sequence`: Cualquier objeto de python que sea una secuncia (`list`, `tuple`, `set`, `str`, `range`, entre otros). Si _X_ es un objeto anidado el array también estará anidado. Por ejemplo, una lista cuyos elementos sean otras listas, todas del mismo tamaño, resultará en un `ndarray` de dos dimensiones, donde cada lista será

```{note}
Para más opciones de creación de arrays visitar la sección de Funciones para la creación de arrays.
```

## Selección de elementos

---
## Selección de elementos: 

### Subsetting:
Para seleccionar elementos de una `narray` tener en cuenta las siguientes características:
- Se utilizan corchetes `[]` para acceder a los elementos, junto con el nombre del array y el índice del elemento: <br/>
`X[i]`
- Los índices comienza en cero (0), esto quiere decir que si quiere acceder al elemento `i`, se debe de usar `[i-1]`.
- Se puede utilizar números negativos, de manera que se comience por el último elemento. Se puede acceder al último con `[-1]`, al penúltimo elemento `[-2]`, etc.
- Para arrays de dos dimensiones o más se separar cada dimensión con coma, donde el primer elemento corresponde a la dimensión 1, el segundo a la dimensión 2, etc. <br/>
`X[i, j, ...]`

---
### Slicing:
- Para seleccionar un rango de elementos consecutivos se utiliza dos puntos: <br/> `X[i:j]`
- La selección por rango, tienen la característica que el primer elemento es inclusivo y el último es exclusivo, esto quiere decir que no se incluirá en el rango, si se usa el rango `[i:j]`, en realidad solo se accederá a `[i:j-1]`.
- Desde el índice `i` hasta el `j`, sin incluir el `j`: <br> `X[i:j]`
- Desde el inicio hasta el `j`, sin incluir el `j`: <br> `X[:j]`
- Desde la posición `i` hasta el final de la cadena: <br>`X[i:]`
- Toda la lista: <br> `X[:]`
- Desde el índice `i` hasta el `j`, sin incluir el `j`, cada `k` elementos: <br> `X[i:j:k]`

Algunos patrones útiles:
- El primer elemento: <br> `X[0]`
- El último elemento: <br> `X[-1]`
- Toda la lista cada `k` elementos: <br> `X[::k]`
- Toda la lista al revés: <br> `X[::-1]`

---
### Fancy Indexing