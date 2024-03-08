# Lectura y escritura de archivos

Se refiere a importar datos desde una fuente externa para poder trabajar con esos datos directamente desde python. Existen diversas formas de importar archivos a Python, pero en esta sección solo se explicará la función `open()`.

<br>

---
## Función open

Es la función principal para trabajar con archivos en Python, permite leer, crear y modificar archivos de texto y archivos binarios.


[open](https://docs.python.org/3/library/functions.html#open)(): Lee un archivo ubicado en `file` y retorna un `file object` correspondiente. Si el archivo no se puede leer, se genera un `OSError`.
```python
open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
```
**Notas:**

- El argumento **`mode`** (`str`) es para indicar qué tipo de conexión, existen caracteres para indicar la acción a realizar en el archivo y otros para indicar el tipo de archivo. Al momento de definir el `mode` los caracteres se deben de poner en el siguiente orden y con las siguientes opciones:
    1. Tipo de acción. 
        - `r`: Abre un archivo solo para su lectura. Arroja un error si el archivo no existe.
        - `a`: Abre un archivo para agregar contenido. Si no existe el archivo lo crea en la ruta determinada. Si ya existe, agregará el contenido nuevo al final del documento.
        - `w`: Abre un archivo para escribir en él. Si no existe el archivo lo crea en la ruta determinada. Si ya existe sobreescribirá el archivo, borrando todo lo que había anteriormente.
        - `x`: Crea el archivo en la ruta determinada, retorna un error si el archivo ya existe.
    2. Lectura y escritura.
        - `+`: Independientemente del caracter elegido en _tipo de acción_, permite abrir un archivo para lectura y escritura. Tener en cuenta las siguientes características al momento de "escribir" dependiendo del primer caracter elegido:
            - `r+`: El archivo debe existir y el cursor se ubicará al inicio del documento, con el riesgo de sobreescribir contenido.
            - `a+`: Crea archivo si no existe. El cursor se ubicará al final del documento.
            - `w+`: Crea el archivo si no existe, o elimina contenido si ya existe. El cursor se ubicará al inicio del documento.
            - `x+`: Crea el archivo o arroja error si ya existe. El cursos se ubicará al inicio del documento.
    3.  Tipo de _I/O_.
        - `t`: Modo texto (default). Retorna contenido en forma de `str`. No es necesario indicar este modo ya que es el modo por default.
        - `b`: Modo binario. Retorna contenido en forma de `bytes`.


:::{warning} Es necesario cerrar la conexión cuando ya no se necesite, ello se puede hacer con el método `.close()`. También se puede utilizar un _context manager_, en ese caso no es necesario cerrar la conexión ya que el administrador lo hará automáticamente.
:::

<br>

---
## Uso

Para usar la función `open()` se puede hacer de dos formas principales.

**1. Sin administrador de contextos**. En esta caso se establece una conexión con un archivo, y se almacenará en una variable esa conexión, con ese objeto se puede usar los métodos de `file`.
```python
# Establecer conexión
file = open("path/to/file.ext")

# Usar métodos, por ejempo .read()
lines = file.read()

# Cerrar conexión cuando ya no se necesite
file.close()
```

**2. Con administrador de contextos**: En este caso se utiliza un administrador de contextos el cual creará la conexión con el archivo y cerrará la conexión automáticamente:
```python
# Establecer conexión
with open("path/to/file.ext") as file:
    # Usar métodos, por ejempo .read()
    lines = file.read()
```

<br>

---
## Métodos del objeto file

En esta parte se enlistas los métodos de los objetos `IOBase` y `TextIOBase`. Para más información de cada uno visitar el link presionando en el nombre del método.

<br>

### Cerrar conexión

Método para cerrar una conexión con un archivo.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [close](https://docs.python.org/3/library/io.html#io.IOBase.close)()
  - Cierra la conexión con un archivo.
```

<br>

### Escritura

Métodos para escibir en un archivo.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [writelines](https://docs.python.org/3/library/io.html#io.IOBase.writelines)(lines, /)
  - Escribe una lista de textos en un archivo.
* - [write](https://docs.python.org/3/library/io.html#io.TextIOBase.write)(s, /)
  - Escriba la cadena `s` en un archivo y devuelva la cantidad de caracteres escritos.
```

<br>

### Información

Métodos sobre el archivo o la conexión.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [tell](https://docs.python.org/3/library/io.html#io.TextIOBase.tell)()
  - Retorna la ubicación actual (en número de caracteres anteriores) que se está leyendo.
* - [seekable](https://docs.python.org/3/library/io.html#io.IOBase.seekable)()
  - Retorna `True` si el _stream_ admite el acceso aleatorio.
* - [writable](https://docs.python.org/3/library/io.html#io.IOBase.writable)()
  - Retorna un valor booleano si se puede escribir en el archivo.
* - [readable](https://docs.python.org/3/library/io.html#io.IOBase.readable)()
  - Retorna `True` si el archivo se puede leer.
```

<br>

### Lectura

Métodos para leer archivos.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [read](https://docs.python.org/3/library/io.html#io.TextIOBase.read)(size=- 1, /)
  - Permite leer e imprimir el contenido de un archivo de texto.
* - [readlines](https://docs.python.org/3/library/io.html#io.IOBase.readlines)(hint=- 1, /)
  - Devuelve todas las líneas de un texto, en formato de lista, donde cada línea es un elemento de la lista.
* - [readline](https://docs.python.org/3/library/io.html#io.TextIOBase.readline)(size=- 1, /)
  - Devuelve línea por línea de un archivo. Es necesario ejecutarlo una vez por cada línea, retorna una sola `str`.
```

<br>

### Navegacion

Método para moverse en un archivo.

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [seek](https://docs.python.org/3/library/io.html#io.TextIOBase.seek)(offset, whence=SEEK_SET, /)
  - Se mueve a la posición indicada del archivo.
```

