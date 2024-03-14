# Pandas

`pandas` es una librería que se utiliza principalmente para analizar, limpiar, explorar y manipular datos tabulares. Sus principales clases son `DataFrame`, `Series` e `Index` pero tiene una variedad de clases más.

Para utilizar `pandas` es necesario instalarlo. Desde la terminal usar:
```
# Con pip
pip install pandas

# Con conda
conda install pandas
```

Una vez instalado se debe de importar
```python
import pandas as pd
```
- `pd` es el alias por convención.
- En el sitio se utilizará `pd` para hacer referencia a pandas.

Para conocer la versión de `pandas` instalada usar:
```python
pd.__version__ 
```

En pandas existen tres objetos que son con los que se estará trabajando principalmente:
- `Index`: Es un array inmutable, funje el papel de identificar por medio de etiquetas cada fila o columna. Puede ser visto como un `set` ordenado o un multi set ordenado, aunque `index` puede tener valores repetidos.
- `Series`: Es como una columna en una tabla. Es un `ndarray` unidimensional (un vector columna) que puede ser de cualquier tipo de dato, pero todos los elementos del mismo tipo. Además las filas tienen un `Index` para identificar a cada fila.
- `DataFrame`: Es una estructura de datos de dos dimensiones, como una tabla, que tiene filas y columnas. Las columnas pueden ser de diferentes tipos, pero cada columna debe de ser del mismo tipo. Tanto las filas como las columna tiene etiquetas mediante `Index`.

Las tres clases anteriores funcionan de manera similar a como funcionan los arrays de `numpy`, por ejemplo, las operaciones entre estos objetos están vectorizadas y muchas funciones de `numpy` también se pueden usar con estas clases.

<br><br>

