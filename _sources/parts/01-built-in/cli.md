# _Command Line Interface_

El _Command Line Interface_ (CLI) de Python es la forma en que se puede interactuar con Python desde la terminal o línea de comandos. Permite ejecutar _scripts_, probar fragmentos de código, administrar módulos, etc.

El _command line_ está disponible posterior a instalar Python. Para utilizar _CLI_ basta con ejecutar el comando `python3` en una terminal.

:::{caution}
Para que el comando funcione correctamente se debe añadir la ruta al ejecutable de Python en la variable _PATH_ del sistema, en caso contrario será necesario indicar explicitamente la ruta al ejecutable. 
:::

Para saber cuál copia de Python se está usando usar el siguiente comando:

```sh
# Ver copia de Python usada
which python3
```
- Con copia se refiere a que se pueden tener múltiples versiones de Python en una misma computadora, para saber cuál versión se usa de forma nativa se utiliza ese comando.

A continuación se presenta la sintaxis de llamada del comando `python3`:

:::{caution}
`pyhon3` no necesarimente será el comando, dependerá del sistema operativo y la manera en la que se instaló, alternativamente se podría intentar usar simplemente `python` o incluso especificar su versión `python3.MAJOR`, por ejemplo `python3.11`, esto es particularme útil si se tienen múltiples versiones de Python instaladas.
:::

```sh
# Sintaxis de llamada
python3 [option] ... [-c cmd | -m mod | file | -] [arg] ...

# Ejecutar comando indicando su ubicación
path/to/python3 [option] ... [-c cmd | -m mod | file | -] [arg] ...
```
- **Argumentos**:
    - `option ...`: Opciones pasadas al comando. Ver tabla más abajo.
    - Solo uno de los siguientes
        - `-c cmd `: Programa pasado como cadena. Ver {ref}`cli-cmd`.
        - `-m mod `: Ejecuta un módulo de la librería como un _script_. Ver {ref}`cli-mod`.
        - `file`: Programa leído desde un archivo _script_, debe tener una extensión _.py_. En caso de que no esté en el directoria actual se debe indicar su ruta relativa o absoluta. Ver {ref}`cli-file`.
        - `-`: Programa leído desde _stdin_ (Default; Modo interactivo si un _tty_). 
    - `arg ...`: Argumentos pasados al programa en `sys.argv[1:]`.
- **Opciones**:
    - `-b`: Emite advertencias sobre `str(bytes_instance)`, `str(bytearray_instance)` y comparaciones de bytes/bytearray con str. (`-bb`: Emite errores).
    - `-B`: No escribe archivos _.pyc_ al importar.
    - `-d`: Activa la salida de depuración de analizador (solo para expertos).
    - `-E`: Ignorar las variables de entorno _PYTHON*_ (como Pythonpath).
    - `-h`: Imprime este mensaje de ayuda (equivale a `-?` o `--help`).
    - `-i`: Permite inspeccionar interactivamente después de ejecutar un _script_; Fuerza un _prompt_ incluso si _stdin_ no parece ser una terminal.
    - `-I`: Aisla Python del entorno del usuario (implica `-E` y `-s`).
    - `-O`: Elimina declaraciones `assert` y dependientes de `__debug__`.|
    - `-OO`: Igual que `-O` y también descarta _docstrings_.
    - `-P`: No agrega un _path_ potencialmente inseguro al _sys.path_.
    - `-q`: No imprime la versión y los mensajes de derechos de autor en el inicio interactivo.
    - `-s`: No agregua el directorio del sitio de usuario al _sys.path_ |
    - `-S`: No implica '_import site_' en la inicialización.
    - `-u`: Fuerza los _streams_ de _stdout_ y _stderr_ a ser _unbuffered_.
    - `-v`: Verbose.
    - `-V`: Imprime el número de versión de Python (Equivale `--version`).
    - `-W arg`: Control de advertencias; _arg_ puedes ser {_action_, _message_, _category_, _module_, _lineno_}.|
    - `-x`: Omite la primera línea de fuente, permitiendo el uso de formas no Unix de _#!cmd_.
    - `-X opt`: Establece una opción específica de implementación.
    - `--check-hash-based-pycs always:default:never`: Controla cómo Python invalida los archivos _.pyc_ basados en _hash_.
    - `--help-env`: Imprime ayuda sobre las variables de entorno de Python.
    - `--help-xoptions`: Imprime ayuda sobre las opciones de implementación `-X` específicas.
    - `--help-all`: Imprima la información de ayuda completa.

Patrones comunes:

```sh
# Mostrar la versión de Python instalada
python3 --version

# Ejecutar un archivo Python
python3 script.py

# Iniciar el intérprete interactivo de Python
python3

# Ejecutar una línea de código Python directamente desde la terminal
python3 -c "print('Hola, mundo')"

# Ejecutar un módulo como script (por ejemplo, iniciar un servidor HTTP)
python3 -m http.server

# Ejecutar un archivo Python con argumentos desde la terminal
python3 script.py arg1 arg2

# Ejecutar un entorno virtual (si ya ha sido creado)
python3 -m venv entorno
source entorno/bin/activate

# Instalar paquetes con pip (usando el módulo -m)
python3 -m pip install nombre_paquete

# Comprobar si una expresión es válida sin ejecutar el código
python3 -m py_compile archivo.py

# Ejecutar un archivo Jupyter Notebook convertido a script
python3 notebook_convertido.py
```

<br/>

---
(cli-repl)=
## REPL (Intérprete - modo interactivo)

Es posible iniciar una sesión interactiva para ejecutar código línea por línea. Para ello simplemente usar el comando `python3` sin ningún argumento desde la terminal:

```sh
# Activar REPL
python3
```

Es posible identificar que ingresó al modo interactivo porque aparecerá `>>>` al inicio de cada línea:

```
$ python3
Python 3.13 (default, April 4 2023, 09:25:04)
[GCC 10.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Al iniciar un bloque que implique múltiples líneas indentadas, automáticamente se harán los saltos de línea y en ese caso cada línea comenzará por `...`. Para ejecutar el bloque dar <kbd>enter</kbd> dos veces. Ejemplo con un bloque _if_:

```
>>> the_world_is_flat = True
>>> if the_world_is_flat:
...    print("Be careful not to fall off!")
... 
Be careful not to fall off!
```

Para salir de la sesión interactiva usar la función `quit()`:

```
>>> quit()
```

:::{tip}
También se puede salir con las teclas <kbd>Ctrl + D</kbd> en Unix y <kbd>Ctrl + Z</kbd> en Windows.
:::

<br/>

---
(cli-file)=
## Ejecutar _script_

La forma más sencilla de ejecutar un _script_ desde la terminal es usando el comando `python3` y el nombre del archivo.

```sh
# Ejecutar script
python3 filename.py

# Ejecutar script en otro directorio
python3 path/to/filename.py

# Ejecutar y entrar a modo interactivo para inspección
python3 -i filename.py

# Ejecutar script con argumentos
python3 filename.py arg1 arg2
```

<br/>

---
(cli-cmd)=
## Ejecutar código en línea

Es posible ejecutar sentencias de Python sin entrar em modo interactivo directamente con `python3`, para ello se usa el argumento `-c cmd`:

```sh
# Ejecutar líneas
python3 -c "print('Hola, mundo')"
```

<br/>

---
(cli-mod)=
## Usar módulos _script_

Es posible ejecuta módulos estándar como si fuera un _script_, para ello se usa el argumento `-m mod`:

```sh
# Ejecutar un módulo como script
python3 -m mod [args]
```
- _mod_: Es el nombre del módulo.
- _args_: Son argumentos de los comandos del módulo.

A continuación se revisarán algunos módulos comúnes de usar con `python3`.

<br/>

### _venv_

Crea entornos virtuales de Python en uno o más directorios de destino.

:::{note}
Para más información de este módulo visitar la [documentación](https://docs.python.org/3/library/venv.html) de Python.
:::

:::{important}
Es altamente recomendado crear un entorno virtual por cada proyecto de Python. Esto con el fin de evitar conflictos al instalar librerías.
:::

```sh
# Sintaxis de llamada
venv [-h] [--system-site-packages] [--symlinks | --copies] [--clear] [--upgrade] 
    [--without-pip] [--prompt PROMPT] [--upgrade-deps] ENV_DIR [ENV_DIR ...]
```
- **Argumentos**:
    - `ENV_DIR`: Uno o más directorios en los que se creará el entorno. Si no se indica se crea en el directorio actual.
- **Opciones**
    - `-h, --help`: Muestra ayuda del módulo.
    - `--system-site-packages`: Proporciona al entorno virtual acceso a los paquetes de sitio _dir_ del sistema.
    - `--symlinks`: Intenta usar _symlinks_ en lugar de copias, cuando _symlinks_ no son el valor predeterminado para la plataforma.
    - `--copies`: Intenta usar copias en lugar de _symlinks_, incluso cuando _symlinks_ son el valor predeterminado para la plataforma.
    - `--clear`: Elimina el contenido del directorio del entorno si ya existe, antes de la creación del entorno.
    - `--upgrade`: Actualiza el directorio del entorno para usar esta versión de Python, suponiendo que Python se haya actualizado _in-place_.
    - `--without-pip`: Omite la instalación o actualización de _pip_ en el entorno virtual (_pip_ es _bootstrapped_ de forma predeterminada).
    - `--prompt PROMPT`: Proporciona un prefijo del _prompt_ alternativo para este entorno.
    - `--upgrade-deps`: Actualiza las dependencias del _core_.

**Patrones útiles**:
```sh
# Crear entorno (directorio actual)
python3 -m venv env_name

# Crear entorno en versión de Python específica (ejm 10)
python3.10 -m venv env_name

# Entrar al entorno virtual (Unix)
source env_name/bin/activate

# Entrar al entorno virtual (Windows)
env_name/bin/activate

# Salir del entorno virtual
deactivate
```
- _env_name_ es el nombre del entorno virtual.
- Si se quiere usar una versión de Python específica se debe de tener instalada esa versión.
- Para entrar al entorno virtual se debe estar en la carpeta donde se encuenta el entorno, no se debe estar dentro de él.

<br/>

### _csvkit_

Es un paquete que incluye comandos para trabajar con archivos _csv_, convertir archivos a _csv_, entre otros. Es necesario instalarlo.

```python
# Instalar csvkit
pip install csvkit

# Actualizar csvkit
pip install --upgrade csvkit
```

#### Opciones comunes

Las herramientas de `csvkit` comparten un conjunto común de argumentos de línea de comandos. 

:::{caution}
No todos los argumentos son compatibles con todas las herramientas, comprobar cuáles son compatibles con el indicador `--help`.
:::

- `-d DELIMITER`, `--delimiter DELIMITER`: Carácter delimitador del archivo CSV de entrada.
- `-t`, `--tabs`: Especifica que el archivo CSV de entrada está delimitado por tabulaciones. Sobrescribe `-d`.
- `-q QUOTECHAR`, `--quotechar QUOTECHAR`: Carácter utilizado para encerrar entre comillas las cadenas en el archivo CSV de entrada.
- `-u {0,1,2,3}`, `--quoting {0,1,2,3}`: Estilo de comillas utilizado en el archivo CSV de entrada:  
    - `0` comillas mínimas,  
    - `1` comillas en todo,  
    - `2` comillas en valores no numéricos,  
    - `3` sin comillas.
- `-b`, `--no-doublequote`: Indica si las comillas dobles se duplican o no en el archivo CSV de entrada.
- `-p ESCAPECHAR`, `--escapechar ESCAPECHAR`: Carácter utilizado para escapar el delimitador si se usa `--quoting 3` (sin comillas) y para escapar el carácter de comillas si se usa `--no-doublequote`.
- `-z FIELD_SIZE_LIMIT`, `--maxfieldsize FIELD_SIZE_LIMIT`: Longitud máxima permitida de un campo en el archivo CSV de entrada.
- `-e ENCODING`, `--encoding ENCODING`: Especifica la codificación del archivo CSV de entrada.
- `-L LOCALE`, `--locale LOCALE`: Especifica la configuración regional (por ejemplo, `en_US`) para números con formato.
- `-S`, `--skipinitialspace`: Ignora los espacios en blanco inmediatamente después del delimitador.
- `--blanks`: No convierte los valores `""`, `"na"`, `"n/a"`, `"none"`, `"null"` o `"."` en valores `NULL`.
- `--null-value NULL_VALUES [NULL_VALUES ...]`: Convierte este/estos valores en `NULL`. Se puede usar múltiples veces.
- `--date-format DATE_FORMAT`: Especifica un formato de fecha estilo `strptime`, como `"%m/%d/%Y"`.
- `--datetime-format DATETIME_FORMAT`: Especifica un formato de fecha y hora estilo `strptime`, como `"%m/%d/%Y %I:%M %p"`.
- `--no-leading-zeroes`: No convierte los valores numéricos con ceros a la izquierda en números.
- `-H`, `--no-header-row`: Especifica que el archivo CSV de entrada no tiene fila de encabezado. Se crearán encabezados por defecto (`a`, `b`, `c`, ...).
- `-K SKIP_LINES`, `--skip-lines SKIP_LINES`: Especifica el número de líneas iniciales a omitir antes de la fila de encabezado (por ejemplo, comentarios, avisos de derechos de autor, filas vacías).
- `-v`, `--verbose`: Muestra trazas detalladas cuando ocurren errores.
- `-l`, `--linenumbers`: Inserta una columna con números de línea al principio de la salida. Útil al usar `grep` o como clave primaria simple.
- `--zero`: Usa numeración basada en cero para columnas en lugar de la numeración por defecto basada en uno.
- `-V`, `--version`: Muestra la información de versión y termina.

<br/>

#### Comandos

A continuación se presenta una lista de comandos disponibles en _csvkit_.

| Comando | Descripción |
|---------|-------------|
| [csvclean](https://csvkit.readthedocs.io/en/latest/scripts/csvclean.html) | Limpia archivos CSV con errores de formato comunes y reporta los problemas. |
| [csvcut](https://csvkit.readthedocs.io/en/latest/scripts/csvcut.html) | Extrae columnas específicas de un archivo CSV. |
| [csvformat](https://csvkit.readthedocs.io/en/latest/scripts/csvformat.html) | Cambia el formato de un archivo CSV (por ejemplo, delimitador, comillas, etc.). |
| [csvgrep](https://csvkit.readthedocs.io/en/latest/scripts/csvgrep.html) | Filtra filas de un archivo CSV que coincidan (o no) con una expresión regular o valor específico. |
| [csvjoin](https://csvkit.readthedocs.io/en/latest/scripts/csvjoin.html) | Realiza una unión (_join_) entre dos archivos CSV usando una clave común. |
| [csvjson](https://csvkit.readthedocs.io/en/latest/scripts/csvjson.html) | Convierte un archivo CSV a formato JSON. |
| [csvlook](https://csvkit.readthedocs.io/en/latest/scripts/csvlook.html) | Muestra un archivo CSV en formato tabular estilo consola, con bordes y alineación. |
| [csvpy](https://csvkit.readthedocs.io/en/latest/scripts/csvpy.html) | Abre un archivo CSV en un entorno interactivo de Python para exploración y análisis. |
| [csvsort](https://csvkit.readthedocs.io/en/latest/scripts/csvsort.html) | Ordena las filas de un archivo CSV según una o más columnas. |
| [csvsql](https://csvkit.readthedocs.io/en/latest/scripts/csvsql.html) | Ejecuta sentencias SQL sobre archivos CSV como si fueran tablas de base de datos. |
| [csvstack](https://csvkit.readthedocs.io/en/latest/scripts/csvstack.html) | Apila múltiples archivos CSV que tienen columnas similares en un solo archivo. |
| [csvstat](https://csvkit.readthedocs.io/en/latest/scripts/csvstat.html) | Genera estadísticas descriptivas para columnas de un archivo CSV. |
| [in2csv](https://csvkit.readthedocs.io/en/latest/scripts/in2csv.html) | Convierte varios formatos de datos tabulares a CSV. |
| [sql2csv](https://csvkit.readthedocs.io/en/latest/scripts/sql2csv.html) | Ejecuta una consulta SQL sobre un archivo CSV y exporta los resultados como CSV. |

:::{caution}
A continuación se explicarán más a profundidad algunos de los comandos, pero no todos, para más información de cada uno seguir su correspondiente link.
:::

<br/>

##### _csvcut_

[csvcut](https://csvkit.readthedocs.io/en/latest/scripts/csvcut.html): Extrae columnas específicas de un archivo CSV.

```sh
# Sintaxis de llamada
csvcut [-h] [-d DELIMITER] [-t] [-q QUOTECHAR] [-u {0,1,2,3}] [-b]
              [-p ESCAPECHAR] [-z FIELD_SIZE_LIMIT] [-e ENCODING] [-S] [-H]
              [-K SKIP_LINES] [-v] [-l] [--zero] [-V] [-n] [-c COLUMNS]
              [-C NOT_COLUMNS] [-x]
              [FILE]
```
- **Argumentos**
    - `FILE`: Archivo de entrada.
- **Opciones**:
    - `-h`: Muestra la ayuda.
    - `-d DELIMITER`: Especifica el delimitador de campo.
    - `-t`: Usa tabulaciones como delimitador de campo.
    - `-q QUOTECHAR`: Especifica el carácter de comillas.
    - `-u {0,1,2,3}`: Controla el manejo de caracteres Unicode.
    - `-b`: Desactiva el buffer de salida.
    - `-p ESCAPECHAR`: Especificifica el carácter de escape.
    - `-z FIELD_SIZE_LIMIT`: Establece el límite de tamaño de campo.
    - `-e ENCODING`: Especifica la codificación de entrada.
    - `-S`: Desactiva la detección de encabezados.
    - `-H`: Omite la primera línea.
    - `-K SKIP_LINES`: Omite las primeras _SKIP_LINES_ líneas.
    - `-v`: Muestra la versión.
    - `-l`: Muestra la lista de hojas.
    - `--zero`: Usa índices de hoja basados en cero.
    - `-V`: Muestra la versión.
    - `-n`: No muestra encabezados.
    - `-c COLUMNS`: Especifica las columnas a seleccionar.
    - `-C NOT_COLUMNS`: Especifica las columnas a excluir.
    - `-x`: Habilita la detección automática de delimitadores.

**Patrones útiles**:

A continuación se presentan algunos casos de uso comunes.

```sh
# Seleccionar una columna específica (por ejemplo, la tercera columna) de un archivo CSV
csvcut -c 3 archivo.csv

# Seleccionar varias columnas específicas (por ejemplo, la primera y tercera columna) de un archivo CSV
csvcut -c 1,3 archivo.csv

# Seleccionar columnas por nombre en lugar de por número
csvcut -c "Nombre,Edad" archivo.csv

# Excluir una columna específica (por ejemplo, la segunda columna) de un archivo CSV
csvcut -C 2 archivo.csv

# Excluir varias columnas específicas (por ejemplo, la primera y tercera columna) de un archivo CSV
csvcut -C 1,3 archivo.csv

# Seleccionar una columna específica de un archivo CSV delimitado por punto y coma
csvcut -d ';' -c 2 archivo.csv

# Seleccionar una columna específica de un archivo CSV con un carácter de comillas específico
csvcut -q '"' -c 2 archivo.csv

# Seleccionar una columna específica de un archivo CSV con una codificación específica
csvcut -e utf-8 -c 2 archivo.csv

# Seleccionar una columna específica de un archivo CSV y omitir las primeras 2 líneas
csvcut -K 2 -c 2 archivo.csv

# Seleccionar una columna específica de un archivo CSV y tratar los valores en blanco como nulos
csvcut --blanks -c 2 archivo.csv
```

<br/>

##### _csvgrep_

[csvgrep](https://csvkit.readthedocs.io/en/latest/scripts/csvgrep.html): Filtra filas de un archivo CSV que coincidan (o no) con una expresión regular o valor específico.

```sh
# Sintaxis de llamada
csvgrep [-h] [-d DELIMITER] [-t] [-q QUOTECHAR] [-u {0,1,2,3}] [-b]
               [-p ESCAPECHAR] [-z FIELD_SIZE_LIMIT] [-e ENCODING] [-S] [-H]
               [-K SKIP_LINES] [-v] [-l] [--zero] [-V] [-n] [-c COLUMNS]
               [-m PATTERN] [-r REGEX] [-f MATCHFILE] [-i] [-a]
               [FILE]
```
- **Argumentos**
    - `FILE`: Archivo de entrada.
- **Opciones**:
    - `-h`: Muestra la ayuda.
    - `-d DELIMITER`: Especifica el delimitador de campo.
    - `-t`: Usa tabulaciones como delimitador de campo.
    - `-q QUOTECHAR`: Especifica el carácter de comillas.
    - `-u {0,1,2,3}`: Controla el manejo de caracteres Unicode.
    - `-b`: Desactiva el buffer de salida.
    - `-p ESCAPECHAR`: Especifica el carácter de escape.
    - `-z FIELD_SIZE_LIMIT`: Establece el límite de tamaño de campo.
    - `-e ENCODING`: Especifica la codificación de entrada.
    - `-S`: Desactiva la detección de encabezados.
    - `-H`: Omite la primera línea.
    - `-K SKIP_LINES`: Omite las primeras _SKIP_LINES_ líneas.
    - `-v`: Muestra la versión.
    - `-l`: Muestra la lista de hojas.
    - `--zero`: Usa índices de hoja basados en cero.
    - `-V`: Muestra la versión.
    - `-n`: No muestra encabezados.
    - `-c COLUMNS`: Especifica las columnas para filtrar.
    - `-m PATTERN`: Especifica el patrón a buscar.
    - `-r REGEX`: Especifica la expresión regular a buscar.
    - `-f MATCHFILE`: Especifica el archivo con patrones a buscar.
    - `-i`: Muestra solo las filas que no coinciden.
    - `-a`: Muestra todas las filas que coinciden.

**Patrones útiles**:

A continuación se presentan algunos casos de uso comunes.

```sh
# Filtrar filas que contienen un patrón específico en una columna (por ejemplo, la tercera columna)
csvgrep -c 3 -m "patrón" archivo.csv

# Filtrar filas que contienen un patrón específico en varias columnas (por ejemplo, la primera y tercera columna)
csvgrep -c 1,3 -m "patrón" archivo.csv

# Filtrar filas que coinciden con una expresión regular en una columna específica
csvgrep -c 2 -r "^patrón" archivo.csv

# Filtrar filas que contienen un patrón específico en una columna de un archivo CSV delimitado por punto y coma
csvgrep -d ';' -c 2 -m "patrón" archivo.csv

# Filtrar filas que contienen un patrón específico en una columna de un archivo CSV con un carácter de comillas específico
csvgrep -q '"' -c 2 -m "patrón" archivo.csv

# Filtrar filas que contienen un patrón específico en una columna de un archivo CSV con una codificación específica
csvgrep -e utf-8 -c 2 -m "patrón" archivo.csv

# Filtrar filas que contienen un patrón específico en una columna y omitir las primeras 2 líneas
csvgrep -K 2 -c 2 -m "patrón" archivo.csv

# Filtrar filas que contienen un patrón específico en una columna y tratar los valores en blanco como nulos
csvgrep --blanks -c 2 -m "patrón" archivo.csv

# Filtrar filas que contienen un patrón específico en una columna y usar índices de columna basados en cero
csvgrep --zero -c 2 -m "patrón" archivo.csv

# Filtrar filas que contienen un patrón específico en una columna y mostrar solo las filas que no coinciden
csvgrep -c 2 -m "patrón" -i archivo.csv
```

<br/>

##### _csvlook_

[csvlook](https://csvkit.readthedocs.io/en/latest/scripts/csvlook.html): Muestra un archivo CSV en formato tabular estilo consola, con bordes y alineación. 

```sh
# Sintaxis de llamada
csvlook [-h] [-d DELIMITER] [-t] [-q QUOTECHAR] [-u {0,1,2,3}] [-b]
        [-p ESCAPECHAR] [-z FIELD_SIZE_LIMIT] [-e ENCODING] [-L LOCALE]
        [-S] [--blanks] [--null-value NULL_VALUES [NULL_VALUES ...]]
        [--date-format DATE_FORMAT] [--datetime-format DATETIME_FORMAT]
        [-H] [-K SKIP_LINES] [-v] [-l] [--zero] [-V]
        [--max-rows MAX_ROWS] [--max-columns MAX_COLUMNS]
        [--max-column-width MAX_COLUMN_WIDTH]
        [--max-precision MAX_PRECISION] [--no-number-ellipsis]
        [-y SNIFF_LIMIT] [-I]
        [FILE]
```
- **Argumentos**
    - `FILE`: Archivo de entrada.
- **Opciones**:
    - `-h`: Muestra la ayuda.
    - `-d DELIMITER`: Especifica el delimitador de campo.
    - `-t`: Usa tabulaciones como delimitador de campo.
    - `-q QUOTECHAR`: Especifica el carácter de comillas.
    - `-u {0,1,2,3}`: Controla el manejo de caracteres Unicode.
    - `-b`: Desactiva el buffer de salida.
    - `-p ESCAPECHAR`: Especifica el carácter de escape.
    - `-z FIELD_SIZE_LIMIT`: Establece el límite de tamaño de campo.
    - `-e ENCODING`: Especifica la codificación de entrada.
    - `-L LOCALE`: Especifica la configuración regional.
    - `-S`: Desactiva la detección de encabezados.
    - `--blanks`: Trata los valores en blanco como nulos.
    - `--null-value NULL_VALUES`: Especifica los valores nulos.
    - `--date-format DATE_FORMAT`: Especifica el formato de fecha.
    - `--datetime-format DATETIME_FORMAT`: Especifica el formato de fecha y hora.
    - `-H`: Omite la primera línea.
    - `-K SKIP_LINES`: Omite las primeras _SKIP_LINES_ líneas.
    - `-v`: Muestra la versión.
    - `-l`: Muestra la lista de hojas.
    - `--zero`: Usa índices de hoja basados en cero.
    - `-V`: Muestra la versión.
    - `--max-rows MAX_ROWS`: Limita el número de filas mostradas.
    - `--max-columns MAX_COLUMNS`: Limita el número de columnas mostradas.
    - `--max-column-width MAX_COLUMN_WIDTH`: Limita el ancho de las columnas.
    - `--max-precision MAX_PRECISION`: Limita la precisión de los números.
    - `--no-number-ellipsis`: No usa puntos suspensivos para números largos.
    - `-y SNIFF_LIMIT`: Establece el límite de detección.
    - `-I`: Desactiva la detección de tipos.

**Patrones útiles**:

A continuación se presentan algunos casos de uso comunes.

```sh
# Mostrar el contenido de un archivo CSV en formato de tabla
csvlook archivo.csv

# Mostrar el contenido de un archivo CSV delimitado por punto y coma en formato de tabla
csvlook -d ';' archivo.csv

# Mostrar el contenido de un archivo CSV con un carácter de comillas específico
csvlook -q '"' archivo.csv

# Mostrar el contenido de un archivo CSV con una codificación específica
csvlook -e utf-8 archivo.csv

# Mostrar el contenido de un archivo CSV y omitir las primeras 2 líneas
csvlook -K 2 archivo.csv

# Mostrar el contenido de un archivo CSV y tratar los valores en blanco como nulos
csvlook --blanks archivo.csv

# Mostrar el contenido de un archivo CSV con un formato de fecha específico
csvlook --date-format "%Y-%m-%d" archivo.csv

# Mostrar el contenido de un archivo CSV con un formato de fecha y hora específico
csvlook --datetime-format "%Y-%m-%d %H:%M:%S" archivo.csv

# Mostrar el contenido de un archivo CSV y limitar el número de filas mostradas
csvlook --max-rows 10 archivo.csv

# Mostrar el contenido de un archivo CSV y limitar el número de columnas mostradas
csvlook --max-columns 5 archivo.csv

# Mostrar el contenido de un archivo CSV y limitar el ancho de las columnas
csvlook --max-column-width 20 archivo.csv
```

<br/>

##### _csvsort_

[csvsort](https://csvkit.readthedocs.io/en/latest/scripts/csvsort.html): Ordena las filas de un archivo CSV según una o más columnas.

```sh
# Sintaxis de llamada
csvsort [-h] [-d DELIMITER] [-t] [-q QUOTECHAR] [-u {0,1,2,3}] [-b]
               [-p ESCAPECHAR] [-z FIELD_SIZE_LIMIT] [-e ENCODING] [-L LOCALE]
               [-S] [--blanks] [--null-value NULL_VALUES [NULL_VALUES ...]]
               [--date-format DATE_FORMAT] [--datetime-format DATETIME_FORMAT]
               [-H] [-K SKIP_LINES] [-v] [-l] [--zero] [-V] [-n] [-c COLUMNS]
               [-r] [-i] [-y SNIFF_LIMIT] [-I]
               [FILE]
```
- **Argumentos**
    - `FILE`: Archivo de entrada.
- **Opciones**:
    - `-h`: Muestra la ayuda.
    - `-d DELIMITER`: Especifica el delimitador de campo.
    - `-t`: Usa tabulaciones como delimitador de campo.
    - `-q QUOTECHAR`: Especifica el carácter de comillas.
    - `-u {0,1,2,3}`: Controla el manejo de caracteres Unicode.
    - `-b`: Desactiva el buffer de salida.
    - `-p ESCAPECHAR`: Especifica el carácter de escape.
    - `-z FIELD_SIZE_LIMIT`: Establece el límite de tamaño de campo.
    - `-e ENCODING`: Especifica la codificación de entrada.
    - `-L LOCALE`: Especifica la configuración regional.
    - `-S`: Desactiva la detección de encabezados.
    - `--blanks`: Trata los valores en blanco como nulos.
    - `--null-value NULL_VALUES`: Especifica los valores nulos.
    - `--date-format DATE_FORMAT`: Especifica el formato de fecha.
    - `--datetime-format DATETIME_FORMAT`: Especifica el formato de fecha y hora.
    - `-H`: Omite la primera línea.
    - `-K SKIP_LINES`: Omite las primeras _SKIP_LINES_ líneas.
    - `-v`: Muestra la versión.
    - `-l`: Muestra la lista de hojas.
    - `--zero`: Usa índices de hoja basados en cero.
    - `-V`: Muestra la versión.
    - `-n`: No muestra encabezados.
    - `-c COLUMNS`: Especifica las columnas por las que ordenar.
    - `-r`: Ordena en orden inverso.
    - `-i`: Ignora diferencias entre mayúsculas y minúsculas.
    - `-y SNIFF_LIMIT`: Establece el límite de detección.
    - `-I`: Desactiva la detección de tipos.

**Patrones útiles**:

A continuación se presentan algunos casos de uso comunes.

```sh
# Ordenar un archivo CSV por la primera columna
csvsort -c 1 archivo.csv

# Ordenar un archivo CSV por una columna específica (por ejemplo, la tercera columna)
csvsort -c 3 archivo.csv

# Ordenar un archivo CSV por varias columnas (por ejemplo, la segunda y tercera columna)
csvsort -c 2,3 archivo.csv

# Ordenar un archivo CSV por una columna específica en orden inverso
csvsort -c 2 -r archivo.csv

# Ordenar un archivo CSV delimitado por punto y coma por una columna específica
csvsort -d ';' -c 2 archivo.csv

# Ordenar un archivo CSV con un carácter de comillas específico
csvsort -q '"' -c 2 archivo.csv

# Ordenar un archivo CSV con una codificación específica
csvsort -e utf-8 -c 2 archivo.csv

# Ordenar un archivo CSV y omitir las primeras 2 líneas
csvsort -K 2 -c 2 archivo.csv

# Ordenar un archivo CSV y tratar los valores en blanco como nulos
csvsort --blanks -c 2 archivo.csv

# Ordenar un archivo CSV con un formato de fecha específico
csvsort --date-format "%Y-%m-%d" -c 2 archivo.csv

# Ordenar un archivo CSV con un formato de fecha y hora específico
csvsort --datetime-format "%Y-%m-%d %H:%M:%S" -c 2 archivo.csv
```

<br/>

##### _csvsql_

[csvsql](https://csvkit.readthedocs.io/en/latest/scripts/csvsql.html): Ejecuta sentencias SQL sobre archivos CSV como si fueran tablas de base de datos.

```sh
# Sintaxis de llamada
csvsql [-h] [-d DELIMITER] [-t] [-q QUOTECHAR] [-u {0,1,2,3}] [-b]
              [-p ESCAPECHAR] [-z FIELD_SIZE_LIMIT] [-e ENCODING] [-L LOCALE]
              [-S] [--blanks] [--null-value NULL_VALUES [NULL_VALUES ...]]
              [--date-format DATE_FORMAT] [--datetime-format DATETIME_FORMAT]
              [-H] [-K SKIP_LINES] [-v] [-l] [--zero] [-V]
              [-i {firebird,mssql,mysql,oracle,postgresql,sqlite,sybase}]
              [--db CONNECTION_STRING] [--query QUERIES] [--insert]
              [--prefix PREFIX] [--before-insert BEFORE_INSERT]
              [--after-insert AFTER_INSERT] [--tables TABLE_NAMES]
              [--no-constraints] [--unique-constraint UNIQUE_CONSTRAINT]
              [--no-create] [--create-if-not-exists] [--overwrite]
              [--db-schema DB_SCHEMA] [-y SNIFF_LIMIT] [-I]
              [--chunk-size CHUNK_SIZE]
              [FILE [FILE ...]]
```
- **Argumentos**
    - `FILE [FILE ...]`: Uno o más archivos CSV de entrada.
- **Opciones**:
    - `-h`: Mostrar ayuda y salir.
    - `-d DELIMITER`: Especificar el delimitador de campo.
    - `-t`: Utilizar tabulaciones como delimitador.
    - `-q QUOTECHAR`: Especificar el carácter de comillas.
    - `-u {0,1,2,3}`: Especificar el modo de manejo de Unicode.
    - `-b`: Desactivar el manejo de comillas.
    - `-p ESCAPECHAR`: Especificar el carácter de escape.
    - `-z FIELD_SIZE_LIMIT`: Especificar el límite de tamaño de campo.
    - `-e ENCODING`: Especificar la codificación del archivo.
    - `-L LOCALE`: Especificar la configuración regional.
    - `-S`: Desactivar el análisis de encabezados.
    - `--blanks`: Tratar los valores en blanco como nulos.
    - `--null-value NULL_VALUES [NULL_VALUES ...]`: Especificar los valores nulos.
    - `--date-format DATE_FORMAT`: Especificar el formato de fecha.
    - `--datetime-format DATETIME_FORMAT`: Especificar el formato de fecha y hora.
    - `-H`: Desactivar el encabezado de columna.
    - `-K SKIP_LINES`: Especificar el número de líneas a omitir.
    - `-v`: Mostrar información detallada.
    - `-l`: Mostrar la lista de tablas.
    - `--zero`: Permitir valores cero.
    - `-V`: Mostrar la versión y salir.
    - `-i {firebird,mssql,mysql,oracle,postgresql,sqlite,sybase}`: Especificar el tipo de base de datos.
    - `--db CONNECTION_STRING`: Especificar la cadena de conexión a la base de datos.
    - `--query QUERIES`: Especificar las consultas SQL.
    - `--insert`: Insertar datos en la tabla.
    - `--prefix PREFIX`: Especificar el prefijo de la tabla.
    - `--before-insert BEFORE_INSERT`: Comando a ejecutar antes de insertar datos.
    - `--after-insert AFTER_INSERT`: Comando a ejecutar después de insertar datos.
    - `--tables TABLE_NAMES`: Especificar los nombres de las tablas.
    - `--no-constraints`: Desactivar las restricciones.
    - `--unique-constraint UNIQUE_CONSTRAINT`: Especificar la restricción única.
    - `--no-create`: No crear la tabla si no existe.
    - `--create-if-not-exists`: Crear la tabla si no existe.
    - `--overwrite`: Sobrescribir la tabla existente.
    - `--db-schema DB_SCHEMA`: Especificar el esquema de la base de datos.
    - `-y SNIFF_LIMIT`: Especificar el límite de detección.
    - `-I`: Desactivar el análisis de encabezados.
    - `--chunk-size CHUNK_SIZE`: Especificar el tamaño del fragmento

**Patrones útiles**:

A continuación se presentan algunos casos de uso comunes.

:::{note}
Para especificar la cadena de conexión con `--db` usar alguna de las siguientes opciones:
- **PostgreSQL**: _csvsql --db postgresql://usuario:contraseña@host:puerto/nombre_base_datos archivo.csv_.
- **MySQL**: _csvsql --db mysql://usuario:contraseña@host:puerto/nombre_base_datos archivo.csv_
- **SQLite**: _csvsql --db sqlite:///ruta/al/archivo.db archivo.csv_.

Notar que no necesariamente todos los campos son obligatorios.
:::

```sh
# Generar una declaración CREATE TABLE a partir de un archivo CSV
csvsql datos.csv

# Crear una tabla en SQLite a partir de un archivo CSV
csvsql --db sqlite:///base.db --insert datos.csv

# Ejecutar una consulta SQL directamente sobre uno o más archivos CSV
csvsql --query "SELECT columna1, columna2 FROM datos WHERE columna3 > 10" datos.csv

# Combinar varios archivos CSV y aplicar una consulta SQL
csvstack archivo1.csv archivo2.csv | csvsql --query "SELECT * FROM stdin WHERE columna = 'valor'"

# Especificar el tipo de base de datos para que genere el SQL compatible (por ejemplo, PostgreSQL)
csvsql --dialect postgresql datos.csv

# Crear tabla si no existe, e insertar los datos
csvsql --db sqlite:///base.db --insert --create-if-not-exists datos.csv

# Generar SQL sin restricciones como claves únicas o foráneas
csvsql --no-constraints datos.csv

# Crear una tabla SQL a partir de un archivo CSV sin insertar datos
csvsql --db sqlite:///mydatabase.db --no-insert myfile.csv

# Crear una tabla SQL con un nombre específico
csvsql --db sqlite:///mydatabase.db --tables mytable myfile.csv

# Crear una tabla SQL con un esquema específico
csvsql --db sqlite:///mydatabase.db --db-schema myschema --insert myfile.csv

# Convertir múltiples archivos CSV a una tabla SQL
csvsql --db sqlite:///mydatabase.db --insert file1.csv file2.csv
```

<br/>

##### _csvstack_

[csvstack](https://csvkit.readthedocs.io/en/latest/scripts/csvstack.html): Apila múltiples archivos CSV que tienen columnas similares en un solo archivo.

```sh
# Sintaxis de llamada
csvstack [-h] [-d DELIMITER] [-t] [-q QUOTECHAR] [-u {0,1,2,3}] [-b]
                [-p ESCAPECHAR] [-z FIELD_SIZE_LIMIT] [-e ENCODING] [-S] [-H]
                [-K SKIP_LINES] [-v] [-l] [--zero] [-V] [-g GROUPS]
                [-n GROUP_NAME] [--filenames]
                [FILE [FILE ...]]
```
- **Argumentos**
    - `FILE [FILE ...]`: Uno o más archivos de entrada.
- **Opciones**:
    - `-h`: Muestra la ayuda.
    - `-d DELIMITER`: Especifica el delimitador de campo.
    - `-t`: Usa tabulaciones como delimitador de campo.
    - `-q QUOTECHAR`: Especifica el carácter de comillas.
    - `-u {0,1,2,3}`: Controla el manejo de caracteres Unicode.
    - `-b`: Desactiva el buffer de salida.
    - `-p ESCAPECHAR`: Especifica el carácter de escape.
    - `-z FIELD_SIZE_LIMIT`: Establece el límite de tamaño de campo.
    - `-e ENCODING`: Especifica la codificación de entrada.
    - `-S`: Desactiva la detección de encabezados.
    - `-H`: Omite la primera línea.
    - `-K SKIP_LINES`: Omite las primeras _SKIP_LINES_ líneas.
    - `-v`: Muestra la versión.
    - `-l`: Muestra la lista de hojas.
    - `--zero`: Usa índices de hoja basados en cero.
    - `-V`: Muestra la versión.
    - `-g GROUPS`: Especifica los nombres de los grupos.
    - `-n GROUP_NAME`: Especifica el nombre de la columna de grupo.
    - `--filenames`: Añade una columna de grupo con nombres de archivo.

**Patrones útiles**:

A continuación se presentan algunos casos de uso comunes.

```sh
# Combinar varios archivos CSV en uno solo
csvstack archivo1.csv archivo2.csv > combinado.csv

# Combinar varios archivos CSV y añadir una columna de grupo con nombres de archivo
csvstack --filenames archivo1.csv archivo2.csv > combinado.csv

# Combinar varios archivos CSV y añadir una columna de grupo con nombres personalizados
csvstack -g "Grupo1,Grupo2" archivo1.csv archivo2.csv > combinado.csv

# Combinar varios archivos CSV delimitados por punto y coma
csvstack -d ';' archivo1.csv archivo2.csv > combinado.csv

# Combinar varios archivos CSV con un carácter de comillas específico
csvstack -q '"' archivo1.csv archivo2.csv > combinado.csv

# Combinar varios archivos CSV con una codificación específica
csvstack -e utf-8 archivo1.csv archivo2.csv > combinado.csv

# Combinar varios archivos CSV y omitir las primeras 2 líneas de cada archivo
csvstack -K 2 archivo1.csv archivo2.csv > combinado.csv

# Combinar varios archivos CSV y tratar los valores en blanco como nulos
csvstack --blanks archivo1.csv archivo2.csv > combinado.csv

# Combinar varios archivos CSV y usar índices de columna basados en cero
csvstack --zero archivo1.csv archivo2.csv > combinado.csv
```

<br/>

##### _csvstat_

[csvstack](https://csvkit.readthedocs.io/en/latest/scripts/csvstack.html): Apila múltiples archivos CSV que tienen columnas similares en un solo archivo.

```sh
# Sintaxis de llamada
csvstat [-h] [-d DELIMITER] [-t] [-q QUOTECHAR] [-u {0,1,2,3}] [-b]
               [-p ESCAPECHAR] [-z FIELD_SIZE_LIMIT] [-e ENCODING] [-L LOCALE]
               [-S] [--blanks] [--null-value NULL_VALUES [NULL_VALUES ...]]
               [--date-format DATE_FORMAT] [--datetime-format DATETIME_FORMAT]
               [-H] [-K SKIP_LINES] [-v] [-l] [--zero] [-V] [--csv] [--json]
               [-i INDENT] [-n] [-c COLUMNS] [--type] [--nulls] [--non-nulls]
               [--unique] [--min] [--max] [--sum] [--mean] [--median]
               [--stdev] [--len] [--max-precision] [--freq]
               [--freq-count FREQ_COUNT] [--count]
               [--decimal-format DECIMAL_FORMAT] [-G] [-y SNIFF_LIMIT] [-I]
               [FILE]
```
- **Argumentos**
    - `FILE`: Archivo de entrada.
- **Opciones**:
    - `-h`: Muestra la ayuda.
    - `-d DELIMITER`: Especifica el delimitador de campo.
    - `-t`: Usa tabulaciones como delimitador de campo.
    - `-q QUOTECHAR`: Especifica el carácter de comillas.
    - `-u {0,1,2,3}`: Controla el manejo de caracteres Unicode.
    - `-b`: Desactiva el buffer de salida.
    - `-p ESCAPECHAR`: Especifica el carácter de escape.
    - `-z FIELD_SIZE_LIMIT`: Establece el límite de tamaño de campo.
    - `-e ENCODING`: Especifica la codificación de entrada.
    - `-L LOCALE`: Especifica la configuración regional.
    - `-S`: Desactiva la detección de encabezados.
    - `--blanks`: Trata los valores en blanco como nulos.
    - `--null-value NULL_VALUES`: Especifica los valores nulos.
    - `--date-format DATE_FORMAT`: Especifica el formato de fecha.
    - `--datetime-format DATETIME_FORMAT`: Especifica el formato de fecha y hora.
    - `-H`: Omite la primera línea.
    - `-K SKIP_LINES`: Omite las primeras _SKIP_LINES_ líneas.
    - `-v`: Muestra la versión.
    - `-l`: Muestra la lista de hojas.
    - `--zero`: Usa índices de hoja basados en cero.
    - `-V`: Muestra la versión.
    - `--csv`: Muestra las estadísticas en formato CSV.
    - `--json`: Muestra las estadísticas en formato JSON.
    - `-i INDENT`: Especifica la indentación para JSON.
    - `-n`: No muestra encabezados.
    - `-c COLUMNS`: Especifica las columnas para las que mostrar estadísticas.
    - `--type`: Muestra el tipo de datos de cada columna.
    - `--nulls`: Muestra el número de valores nulos en cada columna.
    - `--non-nulls`: Muestra el número de valores no nulos en cada columna.
    - `--unique`: Muestra el número de valores únicos en cada columna.
    - `--min`: Muestra el valor mínimo de cada columna.
    - `--max`: Muestra el valor máximo de cada columna.
    - `--sum`: Muestra la suma de los valores de cada columna.
    - `--mean`: Muestra la media de los valores de cada columna.
    - `--median`: Muestra la mediana de los valores de cada columna.
    - `--stdev`: Muestra la desviación estándar de los valores de cada columna.
    - `--len`: Muestra la longitud de los valores de cada columna.
    - `--freq`: Muestra la frecuencia de los valores de cada columna.
    - `--freq-count FREQ_COUNT`: Especifica el número de frecuencias a mostrar.
    - `--count`: Muestra el número de filas.
    - `--decimal-format DECIMAL_FORMAT`: Especifica el formato decimal.
    - `-G`: Usa el formato de salida de Google BigQuery.
    - `-y SNIFF_LIMIT`: Establece el límite de detección.
    - `-I`: Desactiva la detección de tipos.

**Patrones útiles**:

A continuación se presentan algunos casos de uso comunes.

```sh
# Mostrar estadísticas generales de un archivo CSV
csvstat archivo.csv

# Mostrar estadísticas de una columna específica (por ejemplo, la tercera columna)
csvstat -c 3 archivo.csv

# Mostrar el tipo de datos de cada columna
csvstat --type archivo.csv

# Mostrar el número de valores nulos en cada columna
csvstat --nulls archivo.csv

# Mostrar el número de valores no nulos en cada columna
csvstat --non-nulls archivo.csv

# Mostrar el número de valores únicos en cada columna
csvstat --unique archivo.csv

# Mostrar el valor mínimo de cada columna
csvstat --min archivo.csv

# Mostrar el valor máximo de cada columna
csvstat --max archivo.csv

# Mostrar la suma de los valores de cada columna
csvstat --sum archivo.csv

# Mostrar la media de los valores de cada columna
csvstat --mean archivo.csv

# Mostrar la mediana de los valores de cada columna
csvstat --median archivo.csv

# Mostrar la desviación estándar de los valores de cada columna
csvstat --stdev archivo.csv

# Mostrar la longitud de los valores de cada columna
csvstat --len archivo.csv

# Mostrar la frecuencia de los valores de cada columna
csvstat --freq archivo.csv

# Mostrar estadísticas en formato JSON
csvstat --json archivo.csv

# Mostrar estadísticas en formato CSV
csvstat --csv archivo.csv
```

<br/>

##### _in2csv_

[in2csv](https://csvkit.readthedocs.io/en/latest/scripts/in2csv.html): Convierte varios formatos de datos tabulares a CSV.

```sh
# Sintaxis de llamada
in2csv [-h] [-d DELIMITER] [-t] [-q QUOTECHAR] [-u {0,1,2,3}] [-b]
        [-p ESCAPECHAR] [-z FIELD_SIZE_LIMIT] [-e ENCODING] [-L LOCALE]
        [-S] [--blanks] [--null-value NULL_VALUES [NULL_VALUES ...]]
        [--date-format DATE_FORMAT] [--datetime-format DATETIME_FORMAT]
        [-H] [-K SKIP_LINES] [-v] [-l] [--zero] [-V]
        [-f {csv,dbf,fixed,geojson,json,ndjson,xls,xlsx}] [-s SCHEMA]
        [-k KEY] [-n] [--sheet SHEET] [--write-sheets WRITE_SHEETS]
        [--use-sheet-names] [--reset-dimensions]
        [--encoding-xls ENCODING_XLS] [-y SNIFF_LIMIT] [-I]
        [FILE]
```
- **Argumentos**
    - `FILE`: Archivo de entrada.
- **Opciones**:
    - `-h`: Muestra la ayuda.
    - `-d DELIMITER`: Especifica el delimitador de campo.
    - `-t`: Usa tabulaciones como delimitador de campo.
    - `-q QUOTECHAR`: Especifica el carácter de comillas.
    - `-u {0,1,2,3}`: Controla el manejo de caracteres Unicode.
    - `-b`: Desactiva el buffer de salida.
    - `-p ESCAPECHAR`: Especifica el carácter de escape.
    - `-z FIELD_SIZE_LIMIT`: Establece el límite de tamaño de campo.
    - `-e ENCODING`: Especifica la codificación de entrada.
    - `-L LOCALE`: Especifica la configuración regional.
    - `-S`: Desactiva la detección de encabezados.
    - `--blanks`: Trata los valores en blanco como nulos.
    - `--null-value NULL_VALUES`: Especifica los valores nulos.
    - `--date-format DATE_FORMAT`: Especifica el formato de fecha.
    - `--datetime-format DATETIME_FORMAT`: Especifica el formato de fecha y hora.
    - `-H`: Omite la primera línea.
    - `-K SKIP_LINES`: Omite las primeras _SKIP_LINES_ líneas.
    - `-v`: Muestra la versión.
    - `-l`: Muestra la lista de hojas.
    - `--zero`: Usa índices de hoja basados en cero.
    - `-V`: Muestra la versión.
    - `-f FORMAT`: Especifica el formato de entrada (`csv`, `dbf`, `fixed`, `geojson`, `json`, `ndjson`, `xls`, `xlsx`).
    - `-s SCHEMA`: Especifica el esquema.
    - `-k KEY`: Especifica la clave.
    - `-n`: No muestra encabezados.
    - `--sheet SHEET`: Especifica la hoja.
    - `--write-sheets WRITE_SHEETS`: Especifica las hojas a escribir.
    - `--use-sheet-names`: Usa nombres de hojas como nombres de archivos.
    - `--reset-dimensions`: Restablece las dimensiones.
    - `--encoding-xls ENCODING_XLS`: Especifica la codificación de archivos Excel.
    - `-y SNIFF_LIMIT`: Establece el límite de detección.
    - `-I`: Desactiva la detección de tipos.

**Patrones útiles**:

A continuación se presentan algunos casos de uso comunes.

```sh
# Convertir un archivo Excel (.xlsx) a CSV
in2csv archivo.xlsx > archivo.csv

# Convertir una hoja específica de un archivo Excel a CSV
in2csv --sheet "Hoja1" archivo.xlsx > hoja1.csv

# Convertir un archivo JSON a CSV
in2csv archivo.json > archivo.csv

# Convertir un archivo DBF a CSV
in2csv archivo.dbf > archivo.csv

# Convertir un archivo GeoJSON a CSV
in2csv archivo.geojson > archivo.csv

# Convertir un archivo CSV delimitado por punto y coma a CSV estándar
in2csv -d ';' archivo.csv > archivo_estandar.csv

# Convertir un archivo Excel a CSV especificando la codificación
in2csv --encoding-xls latin1 archivo.xlsx > archivo.csv

# Convertir un archivo Excel a CSV y omitir las primeras 2 líneas
in2csv -K 2 archivo.xlsx > archivo.csv

# Convertir un archivo Excel a CSV y usar nombres de hojas como nombres de archivos
in2csv --use-sheet-names archivo.xlsx
```

<br/>

##### _sql2csv_

[sql2csv](https://csvkit.readthedocs.io/en/latest/scripts/sql2csv.html): Ejecuta una consulta SQL sobre un archivo CSV y exporta los resultados como CSV.

```sh
# Sintaxis de llamada
sql2csv [-h] [-v] [-l] [-V] [--db CONNECTION_STRING] [--query QUERY]
               [-e ENCODING] [-H]
               [FILE]
```
- **Argumentos**
    - `FILE`: Archivo de entrada (opcional).
- **Opciones**:
    - `-h`: Muestra la ayuda.
    - `-v`: Muestra la consulta ejecutada.
    - `-l`: Lista las tablas disponibles en la base de datos.
    - `-V`: Muestra la versión.
    - `--db CONNECTION_STRING`: Especifica la cadena de conexión a la base de datos.
    - `--query QUERY`: Especifica la consulta SQL a ejecutar.
    - `-e ENCODING`: Especifica la codificación de salida.
    - `-H`: No incluye encabezados en la salida.


**Patrones útiles**:

A continuación se presentan algunos casos de uso comunes.

:::{note}
Para especificar la cadena de conexión con `--db` usar alguna de las siguientes opciones:
- **PostgreSQL**: _sql2csv --db "postgresql://usuario:contraseña@host:puerto/nombre_base_datos"_.
- **MySQL**: _sql2csv --db "mysql://usuario:contraseña@host:puerto/nombre_base_datos"_.
- **SQLite**: _sql2csv --db "sqlite:///ruta/al/archivo.db"_.

Notar que no necesariamente todos los campos son obligatorios.
:::

```sh
# Ejecutar una consulta SQL en una base de datos y exportar el resultado a CSV
sql2csv --db "sqlite:///mi_base_de_datos.db" --query "SELECT * FROM mi_tabla" > resultado.csv

# Ejecutar una consulta SQL en una base de datos PostgreSQL y exportar el resultado a CSV
sql2csv --db "postgresql://usuario:contraseña@localhost/mi_base_de_datos" --query "SELECT * FROM mi_tabla" > resultado.csv

# Ejecutar una consulta SQL en una base de datos MySQL y exportar el resultado a CSV
sql2csv --db "mysql://usuario:contraseña@localhost/mi_base_de_datos" --query "SELECT * FROM mi_tabla" > resultado.csv

# Ejecutar una consulta SQL en una base de datos y exportar el resultado a CSV con una codificación específica
sql2csv --db "sqlite:///mi_base_de_datos.db" --query "SELECT * FROM mi_tabla" -e utf-8 > resultado.csv

# Ejecutar una consulta SQL en una base de datos y exportar el resultado a CSV sin encabezados
sql2csv --db "sqlite:///mi_base_de_datos.db" --query "SELECT * FROM mi_tabla" -H > resultado.csv

# Ejecutar una consulta SQL en una base de datos y mostrar la consulta ejecutada
sql2csv --db "sqlite:///mi_base_de_datos.db" --query "SELECT * FROM mi_tabla" -v > resultado.csv

# Ejecutar una consulta SQL en una base de datos y listar las tablas disponibles
sql2csv --db "sqlite:///mi_base_de_datos.db" -l
```