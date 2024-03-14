# CSV

Este módulo implementa clases para leer archivos _.csv_ y escribir datos tabulares en archivos ._csv_. Es necesario importar el módulo.

```python
import csv
```

:::{attention}
En esta sección solo se revisan las funciones `csv.reader()` y `csv.writer()`. Para un tratado más completo de este módulo visitar la [documentación](https://docs.python.org/3/library/csv.html#module-csv) de Python.
:::

<br>

---
## Lectura

Para leer un archivo _.csv_ utilizar la siguiente función. Esta función retorna un objeto `csvreader`.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [reader](https://docs.python.org/3/library/csv.html#csv.reader)(csvfile, dialect='excel', **fmtparams)
  - Retorna un objeto `reader` sobre el cual se puede iterar sobre líneas en el archivo _.csv_ dado.
```

<br>

---
### Métodos

A continuación se presenta una lista de métodos públicos del objeto `csvreader`. Aquí no se presentan todos los métodos y atributos de la clase `csvreader`, consultar la [documentación](https://docs.python.org/3/library/csv.html#reader-objects) para más información.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [\_\_next\_\_](https://docs.python.org/3/library/csv.html#csv.csvreader.__next__)()
  - Devuelve la siguiente fila del objeto iterable `reader` como una lista.
```

<br>

### Plantilla de uso

A continuación se presenta una forma general de cómo trabajar con los objetos `csvreader`.

```python
# Importar el módulo
import csv

# Crear conexión con el archivo
with open(filename, 'r') as csvfile:
    # Crear objeto csvreader
    reader = csv.reader(csvfile, delimiter=',')
    
    # Opcional - Omitir la fila de encabezados
    next(reader)
    
    # Iterar sobre el resto de las filas
    for row in reader:
        ...
```
- _filename_ \- `str`: Es la ruta al archivo, incluyendo nombre y la extensión `.csv` o la correspondiente al delimitador.
- En la iteración `row` es `list`, cuyos elementos son los valores de una fila del archivo csv.

<br><br>

---
## Escritura

Para escribir desde Python a un archivo _.csv_ utilizar la siguiente función. Esta función retorna un objeto `csvwriter`.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [writer](https://docs.python.org/3/library/csv.html#csv.writer)(csvfile, dialect='excel', **fmtparams)
  - Retorna un objeto `writer` responsable de convertir los datos del usuario en cadenas delimitadas en el objeto `file-like` dado.
```

<br>

### Métodos

A continuación se presenta una lista de métodos públicos del objeto `csvwriter`. Aquí no se presentan todos los métodos y atributos de la clase `csvwriter`, consultar la [documentación](https://docs.python.org/3/library/csv.html#writer-objects) para más información.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [writerow](https://docs.python.org/3/library/csv.html#csv.csvwriter.writerow)(row)
  - Escribe el parámetro `row` en el objeto de archivo `writer`.
* - [writerows](https://docs.python.org/3/library/csv.html#csv.csvwriter.writerows)(rows)
  - Escribe todos los elementos en `rows` (un `iterable`) en el objeto de archivo `writer`.
```

<br>

---
### Plantilla de uso

A continuación se presenta una forma general de cómo trabajar con los objetos `csvwriter`

```python
# Importar el módulo
import csv

# Crear conexción con el archivo
with open(filename, 'w') as csvfile:
    # Crear objeto csvreader
    writer = csv.writer(csvfile, delimiter=',')
    
    # Opcional - Escribir una línea
    writer.writerow(iterable)
    
    # Opcional - Escribir múltiples líneas
    writer.writerows(iterable_of_iterable)
```
- _filename_ \- `str`: Es la ruta al archivo, incluyendo nombre y la extensión `.csv` o la correspondiente al delimitador.
- Si solo se escribirá una línea se debe pasar una `iterable`, por ejemplo, un objeto `list`, donde cada elemento se escribirá separado por comas.
- Si se escribirán múltiples líneas al mismo tiempo se debe pasar un `iterable` de `iterable`, por ejemplo un objeto `list` anidado.