# Manipulación de arrays

En esta sección se enlistan las funciones relacionadas con la manipulación de arrays como, cambiar el _shape_, agregar o eliminar elementos, concatenar o apilar arrays, etc.

:::{warning}
Para una lista completa visitar la [documentación](https://numpy.org/doc/stable/reference/routines.array-manipulation.html#array-manipulation-routines) de `numpy`.
:::

---
## Agregar y eliminar elementos

Funciones para agregar y eliminar elementos a un array. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [append](https://numpy.org/doc/stable/reference/generated/numpy.append.html)(arr, values[, axis])
  - Agrega valores al final de un arreglo.
* - [delete](https://numpy.org/doc/stable/reference/generated/numpy.delete.html)(arr, obj[, axis])
  - Devuelve un nuevo arreglo con sub-arreglos a lo largo de un eje eliminado.
* - [insert](https://numpy.org/doc/stable/reference/generated/numpy.insert.html)(arr, obj, values[, axis])
  - Inserta valores a lo largo del eje dado antes de los índices dados.
* - [trim_zeros](https://numpy.org/doc/stable/reference/generated/numpy.trim_zeros.html)(filt[, trim])
  - Elimina los ceros iniciales y/o finales de un arreglo 1D.
```

<br>

## Concatenación y apilación

Funciones para concatenar y apilar arrays. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [block](https://numpy.org/doc/stable/reference/generated/numpy.block.html)(arrays)
  - Ensambla un arreglo a partir de listas anidadas de bloques.
* - [column_stack](https://numpy.org/doc/stable/reference/generated/numpy.column_stack.html)(tup)
  - Apila arreglos 1D como columnas en un arreglo 2D.
* - [concatenate](https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html)([axis, out, dtype, casting])
  - Concatena una secuencia de arreglos a lo largo de un eje existente.
* - [dstack](https://numpy.org/doc/stable/reference/generated/numpy.dstack.html)(tup)
  - Apila arreglos a lo largo del tercer eje.
* - [hstack](https://numpy.org/doc/stable/reference/generated/numpy.hstack.html)(tup, *[, dtype, casting])
  - Apila los arreglos horizontalmente.
* - [row_stack](https://numpy.org/doc/stable/reference/generated/numpy.row_stack.html)(tup, *[, dtype, casting])
  - Apila los arreglos verticalmente.
* - [stack](https://numpy.org/doc/stable/reference/generated/numpy.stack.html)(arrays[, axis, out, dtype, casting])
  - Apila una secuencia de arreglos a lo largo de un nuevo eje.
* - [vstack](https://numpy.org/doc/stable/reference/generated/numpy.vstack.html)(tup, *[, dtype, casting])
  - Apila los arreglos verticalmente.
```

<br>

## Manipulación del shape

Funciones para modificar el _shape_ de un array. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [broadcast_arrays](https://numpy.org/doc/stable/reference/generated/numpy.broadcast_arrays.html)(*args[, subok])
  - Realiza _broadcasting_ entre un conjunto de arreglos entre sí.
* - [broadcast_to](https://numpy.org/doc/stable/reference/generated/numpy.broadcast_to.html)(array, shape[, subok])
  - Modifica el _shape_ de un array a un shape específico.
* - [expand_dims](https://numpy.org/doc/stable/reference/generated/numpy.expand_dims.html)(a, axis)
  - Expande el _shape_ de un arreglo.
* - [ravel](https://numpy.org/doc/stable/reference/generated/numpy.ravel.html)(a[, order])
  - Devuelve el arreglo convertido a 1D.
* - [reshape](https://numpy.org/doc/stable/reference/generated/numpy.reshape.html)(a, newshape[, order])
  - Modifica el _shape_ de un arreglo sin cambiar sus datos.
* - [resize](https://numpy.org/doc/stable/reference/generated/numpy.resize.html)(a, new_shape)
  - Devuelve un arreglo nuevo con un nuevo _shape_ especificado.
* - [squeeze](https://numpy.org/doc/stable/reference/generated/numpy.squeeze.html)(a[, axis])
  - Elimina los ejes de longitud uno de `a`.
```

<br>

## Reacomodar elementos

Funciones para modificar el orden de los elementos de un array, únicamente para revertir el orden, recorrer o girar elementos. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [flip](https://numpy.org/doc/stable/reference/generated/numpy.flip.html)(m[, axis])
  - Invierte el orden de los elementos en un arreglo a lo largo del eje dado.
* - [fliplr](https://numpy.org/doc/stable/reference/generated/numpy.fliplr.html)(m)
  - Invierte el orden de los elementos a lo largo del eje 1 (izquierda/derecha).
* - [flipud](https://numpy.org/doc/stable/reference/generated/numpy.flipud.html)(m)
  - Invierte el orden de los elementos a lo largo del eje 0 (arriba/abajo).
* - [roll](https://numpy.org/doc/stable/reference/generated/numpy.roll.html)(a, shift[, axis])
  - Recorre los elementos de el arreglo a lo largo de un eje dado.
* - [rot90](https://numpy.org/doc/stable/reference/generated/numpy.rot90.html)(m[, k, axes])
  - Gira un arreglo 90 grados en el plano especificado por los ejes.
```

<br>

## Repetir arreglos o elementos

Funciones para repetir y concatenar elementos de arreglos o arreglos completos. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [repeat](https://numpy.org/doc/stable/reference/generated/numpy.repeat.html)(a, repeats[, axis])
  - Repite elementos de un arreglo.
* - [tile](https://numpy.org/doc/stable/reference/generated/numpy.tile.html)(A, reps)
  - Construye una matriz repitiendo `A` la cantidad de veces dada por `reps`.
```

<br>

## Splitting

Funciones para separar (split) arrays. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [array_split](https://numpy.org/doc/stable/reference/generated/numpy.array_split.html)(ary, indices_or_sections[, axis])
  - Divide un arreglo en múltiples sub-arreglos.
* - [dsplit](https://numpy.org/doc/stable/reference/generated/numpy.dsplit.html)(ary, indices_or_sections)
  - Divide un arreglo en múltiples sub-arreglos a lo largo del tercer eje (profundidad).
* - [hsplit](https://numpy.org/doc/stable/reference/generated/numpy.hsplit.html)(ary, indices_or_sections)
  - Divide un arreglo en múltiples sub-arreglos horizontalmente.
* - [split](https://numpy.org/doc/stable/reference/generated/numpy.split.html)(ary, indices_or_sections[, axis])
  - Divide un arreglo en múltiples sub-arreglos como _views_.
* - [vsplit](https://numpy.org/doc/stable/reference/generated/numpy.vsplit.html)(ary, indices_or_sections)
  - Divide un arreglo en múltiples sub-arreglos verticalmente.
```

<br>

---
## Transponer

Funciones para transponer arreglos o acciones similares a transponer. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [moveaxis](https://numpy.org/doc/stable/reference/generated/numpy.moveaxis.html)(a, source, destination)
  - Mueve los ejes de un arreglo a nuevas posiciones.
* - [swapaxes](https://numpy.org/doc/stable/reference/generated/numpy.swapaxes.html)(a, axis1, axis2)
  - Intercambia dos ejes de un arreglo.
* - [transpose](https://numpy.org/doc/stable/reference/generated/numpy.transpose.html)(a[, axes])
  - Devuelve un arreglo con ejes transpuestos.
```