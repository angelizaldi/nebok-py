# Funciones

En esta sección se enlistan las funciones de la librería `numpy`.

:::{warning}
No se enlistan todas las funciones de la librería numpy, solo algunas de las más importante. Para una lista completa de funciones visitar la [documentación](https://numpy.org/doc/stable/reference/routines.html#routines) de `numpy`.
:::

## Argumento `axis`

En las funciones que tienen el parámetro `axis` significa que la función se puede aplicar únicamente en un eje determinado, dando como resultado un arreglo de una dimensión menor con respecto al número de dimensiones del array original. Tomar como referencia la imagen para conceptualizar cómo se aplica la función dependiendo del eje indicado en un array 2D.

```{image} ../images/2d-func-axis.png
:name: axis-2D-func
:width: 300px
:align: center
```
Independientemente del eje indicado el array retornado será un array 1D.
- `axis=0`: En este caso se aplica la función a cada colummna.
- `axis=1`: En este caso se aplica la función a cada fila.

En arrays 3D, tomar como referencia la siguiente imagen

```{image} ../images/3d-func-axis.png
:name: axis-3D-func
:width: 300px
:align: center
```
Independientemente del eje indicado el array retornado será un array 2D.
- `axis=0`: En este caso se aplica la función a cada colummna de cada "rebanada". 
- `axis=1`: En este caso se aplica la función a cada fila de cada "rebanada".
- `axis=2`: En este caso se aplica la función a todas las "rebanadas" para cada fila y columna.

:::{tip}
Es posible aplicar la función en dos ejes al mismo tiempo, por ejemplo en lugar de usar `a.sum(axis=2).sum(axis=0)`, se puede usar `axis=(0, 2)` o `axis=(2, 0)`, el orden en el que se pongan los ejes no importa.

Si se quiere aplicar la función en todos los ejes se puede omitir el parámetro `axis` o explícitamente se puede usar `axis=None`.
:::

## Tabla de contenido


```{tableofcontents}
````