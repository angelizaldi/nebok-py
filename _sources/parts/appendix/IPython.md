---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# IPython

IPython es un ambiente computacional interactivo para Python. En esta sección se explica brevemente algunas funcionalidades de IPython.

:::{note}
Para más información visitar la [documentación](https://ipython.readthedocs.io/en/stable/index.html) de IPython.
:::

IPython forma parte de manera nativa en {doc}`./jupyter`.

---
## Autocompletar

Al utilizar IPython o JupyterNotebooks se puede autocompletar el código mientras se escribe utilizando la tecla <kbd> tab </kbd>.
- `pattern<tab>`: Si se utiliza mientras se está escribiendo un nombre sugirirá nombres de variables, palabras reservadas o funciones disponibles que empiecen por el patrón `pattern` en el ambiente global.
- `object.<tab>`: Al utilizarse con objetos sugirirá atributos y métodos del objeto `object`.
- `module.tab>`: Al utilizarse con modulos sugerirá clases, funciones y constantes del módulo `module`.
- `funtion(patttern<tab>)`: Al utilizar dentro de una función y un patrón sugerirá argumentos de `function` que empiecen con `pattern`.
- `from library import patttern<tab>`: Al utilizar mientras se importa una librería sugerirá funciones, clases o módulos que empiezan por el patrón `pattern`.
- `import <tab>`: Al utilizar con la palabra reserva `import`, mostrará todas las librerías disponibles para importar.

<br>

---
## Obtener ayuda

Mientras se programa en IPython se puede obtener ayuda sobre los módulos, funciones y clases con los que se está trabajando

**Obtener ayuda de comando mágico**: Si se quiere obtener ayuda de {ref}`magic-commands` utilizar un signo de integorración `?` al final del comando.

```{code-cell} ipython3
# Obtener ayuda sobre la clase list
%command_name?
```
- _command_name_ es el nombre del comando mágico.

<br>

**Obtener ayuda de un objeto**: Si se quiere obtener ayuda de un objeto o sobre un objeto utilizar un signo de integorración `?` al final del nombre del objeto.

```{code-cell} ipython3
# Obtener ayuda sobre la clase list
list?
```

<br>

**Recuperar información de una función**: Para recuperar la definición, el _docstring_, los parámetros, entre otros datos de una función se pueden utilizar dos signos de interrogación `??` al final del nombre de la función:

```{code-cell} ipython3
# Recuperar información de una función
print??
```

**Buscar funciones, clases, métodos, constantes, etc.**: Se puede utiliza un signo de interrogación `?` y _wildcards_ para enlistar todos los objetos que cumplan determinado patrón, para ello se utiliza el _wildcard_ `*` que representa cualquier caracter una o más veces:

```{code-cell} ipython3
# Enlistar todas las funciones que llevan `mean` en numpy
np.*mean*?
```

<br>

---
## Impresión (display)

IPython cuenta con la función `display()` que permite imprimir objetos con un mejor formato de lo que lo haría `print()`, así como también permite renderizar fórmulas de _LaTeX_ y elementos _HTML_.

```{note}
Por default en IPython se utiliza `display()` para imprimir objetos por lo que no es necesario usarlo explícitamente.
```

Algunos objetos que tienen un mejor formato al ser imprimidos por `display()` son los `DataFrame` de `pandas` y las gráficas de `Matplotlib.pyplot`.

**Ejemplo**: A continuación veremos la diferencia entre `print()` y `display()` al imprimir un `DataFrame`.

```{code-cell} ipython3
# importar libreria
import pandas as pd

# Crear objeto
df = pd.DataFrame({'col1': [1, 2], 'col2': ['a', 'b']})
```

Imprimir objeto con `print()`
```{code-cell} ipython3
# Imprimir df
print(df)
```

Imprimir con `display()`
```{code-cell} ipython3
# Imprimir df
display(df)
```
<br>

### Renderizar LaTeX

Para poder imprimir fórmulas de _LaTeX_ es necesario importar de `IPython.display` la función `Math()` y utilizar esta función dentro de `display()`. 

```{code-cell} ipython3
# Importar función
from IPython.display import Math

# fórmula de LaTeX
latex_formula = r'\frac{1}{2} \cdot \sqrt{3x-1} + \left( y^2 + 1 \right)'

# Renderizar fórmulas de LaTeX
display(Math(latex_formula))
```
- **Importante**: Notar que la cadena que contenga la fórmula de _LaTeX_ debe de ser una cadena cruda (_raw string_).

<br>

### Renderizar HTML

Para poder imprimir contenido de _HTML_ es necesario importar de `IPython.display` la función `HTML()` y utilizar esta función dentro de `display()`. 

```{code-cell} ipython3
# Importar función
from IPython.display import HTML

# Contenido HTML
html_content = "<h1>Hello, IPython!</h1>"

# Renderizar elementos HTML
display(HTML(html_content))
```

<br>

---
## In y Out

Al trabajar con IPython cada sentencia escrita en la consola y cada resultado se almacenan en los objetos _In_ del tipo `list` y _Out_ del tipo `dict`. Como se muestra en la siguiente imagen:

```{image} ../images/In-Out.png
:name: IPython-in-and-out
:align: center
```

Tener en cuenta las siguientes características:
- **In**: En _In_ se almacena las sentencias utilizadas en IPython como `str`. Para acceder a una sentencia basta con utilizar el índice de _In_.

```{image} ../images/In.png
:name: IPython-in
:align: center
```

- **Out**: En _Out_ se almacena los resultados de los _In_ (en caso de que haya). Es un diccionario cuyas llaves son el índice del _Out_ y cuyos valores son el resultado del _Out_. Se puede utilizar este objeto para manipular los resultados posteriormente.

```{image} ../images/Out.png
:name: IPython-out
:align: center
```

```{note}
Se puede acceder a los últimos tres resultados de _Out_ con guiones bajos:
- '_': Último valor en _Out_.
- '__': Penúltimo valor en _Out_.
- '___': Antepenúltimo valor en _Out_.

Alternativamente se puede indicar un _Out_ específico con un guión bajo y el índice del _Out_: <br> `__Ind_`
```

<br/>

---
## Utilizar comandos de _shell_, __conda_ o _pip_

Para poder utilizar comandos de _shell_ _conda_ o _pip_ desde IPython es recomendado primero importar la librería `sys` y cada comando debe ir precedido por un `!`.

:::{caution}
El altamente recomendado importar la librería _sys_ antes de ejecutar un comando de terminal en IPython.
:::

:::{tip}
Muchos comandos _shell_ tienen comandos mágicos equivalente. Revisar {ref}`magic-commands-files` y {ref}`magic-commands-shell`.
:::

```sh
# Importar sys
import sys

# Comando de shell
!ls

# Comando de pip
!pip install pandas

# Comando de conda
!conda install pandas
```

<br/>

**Ejemplo**:

En este ejemplo se imprime información de la librería _pandas_ con _pip_.

```{code-cell} ipython3
# Importar sys
import sys

# Mostrar información de pandas 
!pip show pandas
```

<br>

---
(magic-commands)=
## Comandos mágicos

Los comandos mágicos, son comandos especiales precedidos por _%_ que permiten realizar diversas acciones, a continuación se enlistan algunos comandos y su descripción.

:::{note}
Para una lista completa y más información sobre los comandos mágicos usar el comando mágico `%magic` y `%lsmagic` Además visitar la [documentación](https://ipython.readthedocs.io/en/stable/interactive/magics.html) de IPython.
:::

<br/>

### Gestión del Entorno y Configuración

Comandos para configurar el comportamiento de IPython y su entorno.

| Comando          | Descripción |
|-----------------|------------|
| [%autoawait](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-autoawait)    | Habilita o deshabilita la espera automática en async. |
| [%autocall](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-autocall)     | Controla si las llamadas a funciones se ejecutan automáticamente. |
| [%automagic](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-automagic)    | Permite ejecutar comandos mágicos sin el prefijo `%`. |
| `%autosave`     | Configura el guardado automático de notebooks. |
| [%config](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-config)       | Muestra y configura opciones de IPython. |
| [%colors](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-colors)       | Cambia el esquema de colores de IPython. |
| [%gui](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-gui)          | Configura la integración con interfaces gráficas. |
| [%matplotlib](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-matplotlib)   | Configura la integración con Matplotlib. |
| [%pylab](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-pylab)        | Importa NumPy y Matplotlib en el espacio de nombres. |
| [%precision](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-precision)    | Establece la precisión de los números flotantes en la salida. |
| [%quickref](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-quickref)     | Muestra una referencia rápida de IPython. |
| [%xmode](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-xmode)        | Configura el nivel de detalle de los rastreos de errores. |

<br/>

(magic-commands-files)=
### Manejo de Archivos y Directorios

Comandos para navegar y gestionar archivos y directorios.

:::{note}
La mayoría de los comandos de esta sección los _alias_ de comandos de _cmd_ que pueden variar dependiendo del sistema operativo. Para más información consultar `%alias?`
:::

| Comando   | Descripción |
|----------|------------|
| [%bookmark](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-bookmark) | Gestiona accesos directos a directorios. |
| `%cat`      | Muestra el contenido de un archivo. |
| [%cd](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-cd)       | Cambia de directorio. |
| `%cp`       | Copia archivos o directorios. |
| `%dirs`     | Muestra el historial de directorios. |
| `%ldir`     | Lista archivos en formato detallado. |
| `%less`     | Muestra el contenido de un archivo de manera paginada. |
| `%lf`       | Lista funciones en un archivo. |
| `%lk`       | Lista variables en un archivo. |
| `%ll`       | Lista el código de una función o clase en detalle. |
| `%ls`       | Lista archivos en el directorio actual. |
| `%mkdir`    | Crea un directorio. |
| `%mv`       | Mueve archivos o directorios. |
| [%pwd](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-pwd)      | Muestra el directorio actual. |
| [%pycat](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-pycat)    | Muestra el contenido de un archivo con resaltado de sintaxis. |
| `%rm`       | Elimina archivos. |
| `%rmdir`    | Elimina directorios. |

<br/>

### Historial y Macros

Comandos para gestionar y reutilizar comandos previos.

| Comando          | Descripción |
|-----------------|------------|
| [%dirs](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-dirs)        | Muestra el historial de directorios. |
| `%hist`         | Muestra el historial de comandos. |
| [%history](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-history)      | Similar a `%hist`, pero con más opciones. |
| [%macro](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-macro)        | Define una macro a partir de comandos previos. |
| [%recall](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-recall)      | Recupera un comando previo. |
| `%rep`          | Repite el último comando ingresado. Igual que `%recall` |
| [%rerun](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-rerun)        | Reejecuta un comando del historial. |
| [%save](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-save)         | Guarda comandos en un archivo. |
| `%store`        | Guarda variables en un almacenamiento persistente. |

<br/>

#### Comando _%history_

[%history](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-history) permite imprimir _n_ cantidad de elementos de los objetos _In_ y _Out_:
```shell
# Sintaxis de llamada
%history [-n] [-o] [-p] [-t] [-f FILENAME] [-g [PATTERN ...]]
             [-l [LIMIT]] [-u]
             [range ...]
```
- \-n: Para indicar que se impriman los _In_.
- \-o: Para indicar que se impriman los _Out_.
- range: Indica cuál línea o cuál rango de líneas imprimir, si es un rango se debe definir como `n-m`.

Ejemplos:
```shell
# Fila 4 de In
%history -n 4

# Fila 4 a 6 de In
%history -n 4-6

# Fila 4 a 6 de In y Out
%history -n -o 4-
```

<br/>

### Depuración y Perfilado de Código

Comandos para depurar y analizar el rendimiento del código.

| Comando    | Descripción |
|-----------|------------|
| [%debug](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-debug)  | Inicia el depurador en la última excepción. |
| [%doctest_mode](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-doctest_mode) | Ajusta la salida para pruebas con doctest. |
| [%pdb](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-pdb)    | Activa el depurador en caso de error. |
| [%prun](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-prun)   | Perfila la ejecución de una función o script. |
| [%tb](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-tb)     | Muestra el traceback de la última excepción. |
| [%time](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-time)   | Mide el tiempo de ejecución de una línea de código. |
| [%timeit](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-timeit) | Mide el tiempo de ejecución repetida de una línea. |

<br/>

(magic-command-debug)=
#### Comando _%debug_

[%debug](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-debug) activa el depurador de errores interactivo al ocurrir un error o una excepción. Para ello se utiliza el comando `%debug`, inmediatamente después de que occura un error. Al ejecutar el comando se iniciará una sesión _ipdb_ (se puede identificar por que al inicio de cada línea aparece `ipdb>`) que permitirá de manera interactiva analizar el código para encontrar el error.
```shell
# Sintaxis de llamada
%debug [--breakpoint FILE:LINE] [statement ...]
```
:::{tip}
Se puede indicar que se inicialice _ipdb_ automáticamente al suceder un error usando `%pdb on`.
:::

Existen algunas instrucciones especiales para interactuar en _ipdb_ (estas instrucciones son las mismas que las del depurador _pdb_):
```shell
# Reanuda la ejecución del programa hasta el próximo breakpoint
ipdb> continue

# Ejecuta la siguiente línea sin entrar en llamadas a funciones
ipdb> next

# Imprimir el contenido de una variable o expresión
ipdb> pp expression 	

# Salir de la sesión de debugging
ipdb> quit 	
```

<br/>

#### Timing

Se refiere al proceo de identificar el tiempo de ejecución de una línea o un bloque de líneas. Existen diversos comandos mágicos que pueden ayudar a realizar dichas tareas:
- [%time expression](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-time): Tiempo de la ejecución de una sola sentencia. Ideal para comandos que duran más tiempo en ejecurse y que realizar la operación de manera iterativa no sesgue los resultados, como con ordenar.
- [%timeit expression](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-timeit): Tiempo de ejecución de una sola línea de manera iterativa.
- [%%timeit expression](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-timeit): Tiempo de ejecución de un bloque de código, por ejemplo, una celda de un _Jupyter Notebook_. Debe ser la primer sentencia en la celda.

**Uso de `%timeit` y `%%timeit`**:

Ambos se utilizan para calcular el tiempo de ejecución de una línea (`%timeit`) o de un bloque de líneas (`%%timeit`), la manera como lo calcula es que ejecuta la misma línea o bloque de línea en varias ejecuciones y en cada ejecución corre el código de manera iterativa para estimar los tiempos de ejecución.
```shell
# Sintaxis de llamada
%timeit [-n<N> -r<R> [-t|-c] -q -p<P> -o] statement

%%timeit [-n<N> -r<R> [-t|-c] -q -p<P> -o] setup_code
```
- _-n\<N\>_: Especifica el número de iteraciones (cúantas veces será ejecutado el código en cada ejecución).
- _-r\<R\>_: Especifica el número de ejecuciones/_runs_.
- _-o_: Para indicar que se retorne un objeto `TimeitResult`, el cual se puede almacenar en una variable.

Para almacenar los resultados en un `TimeitResult` se puede hacer de la siguiente manera:
```python
# Almecenar resultado en variable
list_comp = %timeit -o [i**2 for i in range(1000)]
```
- Posteriormente se puede acceder a las propiedades de `TimeitResult`:
    - `TimeitResult.timings` - `list`: Lista de los tiempos de cada ejecución (run).
    - `TimeitResult.best` - `float`: Mejor tiempo.
    - `TimeitResult.worst` - `float`: Peor tiempo.

<br/>

#### Profiling

Se refiere al proceo de identificar las áreas que se pueden optimizar en una línea o un bloque de líneas, como la memoria consumida o el tiempo de ejecución. Existen diversos comandos mágicos que pueden ayudar a realizar dichas tareas:
- [%prun expression](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-prun): Ejecuta código con el profiler.
- `%lprun`: Ejcuta línea por línea con el profiler. Es más completo que `%prun`. Forma parte de la extensión [line_profiler](https://kernprof.readthedocs.io/en/latest/). **Importante**: Es necesario instalarlo.
- `%mprun`: Ejecuta código con el profiler de memoria línea por línea. Forma parte de la extensión `memory_profiler`. **Importante**: Es necesario instalarlo.

Las extensiones externas a IPython se tienen que cargar antes de poder usarlas.

```python
# Cargar extensión
%load_ext line_profiler
%load_ext memory_profiler

# Utilizar comando
%lprun -f function_name function_name(args)
%mprun -f function_name function_name(args)
```
- La _flag_ _-f_ se utiliza para indicar que se perfilará una función.
- Es necesario primero poner solo el nombre de la función y después la llamada a la función.

<br/>

### Gestión de Extensiones y Módulos

Comandos para cargar, descargar y recargar extensiones en IPython.

| Comando         | Descripción |
|---------------|------------|
| [%load_ext](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-load_ext)   | Carga una extensión en IPython. |
| [%reload_ext](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-reload_ext) | Recarga una extensión ya cargada. |
| [%unload_ext](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-unload_ext) | Descarga una extensión de IPython. |

<br/>

### Ejecución de Código y Scripts

Comandos para ejecutar scripts y código desde IPython.

| Comando      | Descripción |
|------------|------------|
| [%code_wrap](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-code_wrap) | Envuelve código para mejor visualización. |
| `%ed`       | Edita una celda o archivo en un editor externo. |
| [%edit](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-edit)     | Similar a `%ed`, pero más flexible. |
| [%load](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-load)     | Carga código desde un archivo o URL. |
| [%loadpy](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-loadpy)   | Carga y ejecuta un archivo Python. |
| [%notebook](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-notebook) | Exporta el historial a un notebook. |
| [%page](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-page)     | Muestra la salida en formato paginado. |
| [%pastebin](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-pastebin) | Sube código a un pastebin. |
| [%psource](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-psource)  | Muestra el código fuente de un objeto. |
| [%run](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-run)      | Ejecuta un script en IPython. |

#### Comando _%run_

Ejecuta un _script_ de Python en IPython, ya sea en la consola o en una celda de _Jupyter_.

```shell
# Sintaxis de llamada
%run [-n -i -e -G]
     [( -t [-N<N>] | -d [-b<N>] | -p [profile options] )]
     ( -m mod | filename ) [args]
```

**Patrones comunes**:

```shell
# Ejecución básica
%run path/to/my_script.py

# Ejecución en debug mode
%run -d path/to/my_script.py

# Ejecución y mantener el namespace después de la ejecución
%run -i path/to/my_script.py
```
- Se debe indicar la ruta al archivo en relación con el directorio actual en IPython.
- Al ejecutar un _script_ en modo _debug_ se abrirá una sesión de _ipdb_. Ver {ref}`magic-command-debug` para más información.

:::{note}
La ejecución en _debug mode_ permite ejecutar el código línea por línea. Para ello es recomendado añadir _breakpoints_ al _script_ con la función `breakpoint()` (función _built-in_):

<code>
# Añadir breakpoints
def add(a, b):
    result = a + b
    breakpoint()
    return result
</code>

Al ejecutar el _script_, la ejecución se dentendrá después del _breakpoint_ y se entrará a la sesión _ipdb_ donde se podrá ejecutar el código línea por línea e interactuar con los variables.
:::

<br/>

(magic-commands-shell)=
### Sistema y Shell

Comandos para interactuar con el sistema operativo.

| Comando     | Descripción |
|-----------|------------|
| [%alias](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-alias)   | Define un alias para un comando del sistema. |
| [%alias_magic](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-alias_magic) | Define un alias para un comando mágico. |
| [%conda](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-conda)     | Ejecuta comandos de _conda_ dentro de IPython. |
| [%killbgscripts](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-killbgscripts) | Mata procesos en segundo plano. |
| [%lsmagic](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-lsmagic) | Muestra la lista de comandos mágicos disponibles. |
| `%man`     | Muestra el manual de un comando. |
| [%magic](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-magic) | Muestra información sobre los comandos mágicos disponibles. |
| [%mamba](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-mamba)   | Usa Mamba para gestionar paquetes. |
| [%micromamba](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-micromamba) | Usa Micromamba para gestionar paquetes. |
| [%pip](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-pip)     | Ejecuta comandos de _pip_ dentro de IPython. |
| [%rehashx](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-rehashx) | Recarga los comandos del sistema en IPython. |
| [%sc](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-sc)    | Ejecuta comandos del sistema y almacena la salida en una variable. OBSOLETO. Usar `!` |
| [%set_env](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-set_env) | Define variables de entorno. |
| [%sx](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-sx)    | Similar a `%sc`, pero devuelve la salida como lista de líneas. Equivale a usar `!!` |
| [%system](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-system)  | Ejecuta comandos del sistema. |
| [%unalias](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-unalias) | Elimina un alias definido. |
| [%uv](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-uv) | Corre el paquete _uv_ para admnistrar paquetes dentro del _kernel_ actual. |

<br/>

### Inspección de Variables y Objetos

Comandos para ver información sobre variables y objetos en el entorno.

| Comando    | Descripción |
|-----------|------------|
| [%env](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-env)    | Muestra las variables de entorno. |
| [%pdef](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-pdef)   | Muestra la firma de una función. |
| [%pdoc](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-pdoc)   | Muestra la documentación de un objeto. |
| [%pfile](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-pfile)  | Muestra el archivo fuente de un objeto. |
| [%pinfo](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-pinfo)  | Muestra información sobre un objeto. |
| [%pinfo2](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-pinfo2) | Similar a `%pinfo`, pero más detallado. |
| [%pprint](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-pprint) | Muestra la representación de un objeto con formato. |
| [%psearch](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-psearch) | Busca objetos en el entorno. |
| [%who](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-who)    | Lista las variables definidas en el entorno. |
| [%who_ls](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-who_ls) | Similar a `%who`, pero en formato de lista. |
| [%whos](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-whos)   | Muestra información detallada sobre las variables. |

<br/>

### Limpieza y Reinicio del Entorno

Comandos para limpiar variables, sesiones y resetear IPython.

| Comando             | Descripción |
|--------------------|------------|
| `%clear`          | Limpia la pantalla de IPython. |
| [%logoff](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-logoff)         | Desactiva el registro de comandos. |
| [%logon](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-logon)          | Activa el registro de comandos. |
| [%logstart](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-logstart)       | Inicia el registro en un archivo. |
| [%logstate](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-logstate)       | Muestra el estado del registro. |
| [%logstop](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-logstop)        | Detiene el registro. |
| [%popd](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-popd)          | Regresa al directorio anterior. |
| [%pushd](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-pushd)         | Guarda el directorio actual y cambia a otro. |
| [%reset](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-reset)         | Borra todas las variables del entorno. |
| [%reset_selective](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-reset_selective) | Borra variables específicas. |
| [%xdel](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-xdel)          | Elimina una variable del entorno. |




<br>

---
## Shorcuts

A continución se enlistan algunos _shortcuts_ del teclado al trabajar con IPython.

```{list-table}
:header-rows: 1
:name: ipython-shorcuts

* - Atajo
  - Descripción
* - `Crtl + P / flecha-arriba`
  - Busca los comandos anteriores en el historial
* - `Crtl + N / flecha-abajo`
  - Busca los comandos posteriores en el historial
* - `Crtl + R`
  - Permite buscar en el historial escribiendo texto
* - `Crtl + C`
  - Interrumpe la ejecución actual
* - `Ctrl + A`
  - Mueve el cursor al inicio de la línea
* - `Ctrl + E`
  - Mueve el cursos al final de la línea
* - `Ctrl + K`
  - Elimina desde donde está el cursor hasta el final de la línea
* - `Ctrl + U`
  - Elimina el texto desde el inicio de la línea hasta el cursor
* - `Ctrl + L`
  - Limpia la pantalla (no elimina el historial)
* - `Ctrl + D`
  - Elimina el caracter inmediato a la derecha respecto al cursor.
* - `Ctrl + T`
  - Transpone dos caracteres
* - `Ctrl + F / Flecha-derecha`
  - Mueve el cursor una posición a la derecha
* - `Ctrl + B / Flecha-Izquierda`
  - Mueve el cursor una posición a la izquierda
```

## Anexos

A continuación se enlistan los comandos del depurador _ipdb_.

:::{note}
Algunos comandos se pueden llamar por una sola letra o por una palabra, para identificar estos comandos vendrá entre paréntesis el resto de la palabra, por ejemplo _q(uit)_, se puede llamar tanto por _q_ como por _quit_.
:::

:::{caution}
La clasificación en esta lista puede estar incompleta. Se clasificaron solo los comandos más importantes, pero es posible que haya comandos que entren en alguna categoría específica pero se hayan colocado en la categoría "Otros".
:::

```{list-table}
:header-rows: 1

* - Comando
  - Descripción
* - **Control de ejecución**
  -
* - [c(ont(inue))](https://docs.python.org/3/library/pdb.html#pdbcommand-continue)
  - Reanuda la ejecución del programa hasta el próximo _breakpoint_.
* - [n(ext)](https://docs.python.org/3/library/pdb.html#pdbcommand-next)
  - Ejecuta la siguiente línea sin entrar en llamadas a funciones.
* - [q(uit)](https://docs.python.org/3/library/pdb.html#pdbcommand-quit)
  - Sale del depurador y termina la ejecución del programa.
* - [r(eturn)](https://docs.python.org/3/library/pdb.html#pdbcommand-return)
  - Continúa la ejecución hasta que la función actual retorne.
* - [s(tep)](https://docs.python.org/3/library/pdb.html#pdbcommand-step)
  - Ejecuta la siguiente línea, entrando en funciones si es necesario.
* - **Inspección del código**
  -
* - [l(ist)](https://docs.python.org/3/library/pdb.html#pdbcommand-list)` [first[, last]]`
  - Muestra el código fuente de la función actual.
* - [p](https://docs.python.org/3/library/pdb.html#pdbcommand-p)` expression`
  - Imprime el valor de una variable o expresión.
* - [pp](https://docs.python.org/3/library/pdb.html#pdbcommand-pp)` expression`
  - Imprime una variable con formato legible (`pprint`).
* - [whatis](https://docs.python.org/3/library/pdb.html#pdbcommand-whatis)` expression`
  - Muestra el tipo de una variable u objeto.
* - [w(here)](https://docs.python.org/3/library/pdb.html#pdbcommand-where)
  - Muestra el stack trace actual.
* - **Manejo de breakpoints**
  -
* - [b(reak)](https://docs.python.org/3/library/pdb.html#pdbcommand-break)` [([filename:]lineno | function) [, condition]]`
  - Con un argumento de _lineno_, establece un _breakpoint_ en la línea _lineno_ o en una función en el archivo actual.
* - [cl(ear)](https://docs.python.org/3/library/pdb.html#pdbcommand-clear)` [filename:lineno | bpnumber ...]`
  - Elimina uno o más breakpoints en el archivo _lineno_.
* - [tbreak](https://docs.python.org/3/library/pdb.html#pdbcommand-tbreak)` [([filename:]lineno | function) [, condition]]`
  - Crea un breakpoint temporal que se elimina después de ser alcanzado.
* - **Manejo de breakpoints**
  -
* - [d(own)](https://docs.python.org/3/library/pdb.html#pdbcommand-down)` [count]`
  - Se mueve un nivel (default) hacia abajo en la pila de llamadas.
* - [u(p)](https://docs.python.org/3/library/pdb.html#pdbcommand-up)` [count]`
  - Se mueve un nivel hacia arriba en la pila de llamadas.
* - **Otros**
  -
* - [!](https://docs.python.org/3/library/pdb.html#pdbcommand-0)` statement`
  - Ejecuta la declaración (una línea) en el contexto del depurador.
* - [a(rgs)](https://docs.python.org/3/library/pdb.html#pdbcommand-args)
  - Imprime los argumentos de la función actual y sus valores actuales.
* - [alias](https://docs.python.org/3/library/pdb.html#pdbcommand-alias)` [name [command]]`
  - Crea un alias llamado _name_ que ejecuta un comando.
* - [commands](https://docs.python.org/3/library/pdb.html#pdbcommand-commands)` [bpnumber]`
  - Define una serie de comandos a ejecutar cuando se alcanza un _breakpoint_.
* - [condition](https://docs.python.org/3/library/pdb.html#pdbcommand-condition)` bpnumber [condition]`
  - Asigna una condición a un _breakpoint_ para que solo se active bajo ciertas circunstancias. 
* - [debug](https://docs.python.org/3/library/pdb.html#pdbcommand-debug)` code`
  - Inicia una sesión de depuración anidada en la línea actual.
* - [disable](https://docs.python.org/3/library/pdb.html#pdbcommand-disable)` bpnumber [bpnumber ...]`
  - Deshabilita un _breakpoint_ sin eliminarlo.
* - [display](https://docs.python.org/3/library/pdb.html#pdbcommand-display)` [expression]`
  - Muestra automáticamente el valor de una expresión cuando se detiene el programa.
* - [enable](https://docs.python.org/3/library/pdb.html#pdbcommand-enable)` bpnumber [bpnumber ...]`
  - Habilita un _breakpoint_ previamente deshabilitado.
* - [exceptions](https://docs.python.org/3/library/pdb.html#pdbcommand-exceptions)` [excnumber]`
  - Configura cómo manejar excepciones en el depurador.
* - [h(elp)](https://docs.python.org/3/library/pdb.html#pdbcommand-help)` [command]`
  - Muestra ayuda sobre los comandos de `pdb`.
* - [ignore](https://docs.python.org/3/library/pdb.html#pdbcommand-ignore)` bpnumber [count]`
  - Configura cuántas veces se ignorará un _breakpoint_ antes de activarse.
* - [interact](https://docs.python.org/3/library/pdb.html#pdbcommand-interact)
  - Inicia una sesión interactiva en el contexto actual.
* - [j(ump)](https://docs.python.org/3/library/pdb.html#pdbcommand-jump)` lineno`
  - Cambia la ejecución a otra línea dentro de la misma función.
* - [ll | longlist](https://docs.python.org/3/library/pdb.html#pdbcommand-ll)
  - Lista el código completo de la función actual.
* - [retval](https://docs.python.org/3/library/pdb.html#pdbcommand-retval)
  - Muestra el valor de retorno de la última función terminada.
* - [run](https://docs.python.org/3/library/pdb.html#pdbcommand-run)` [args ...]`
  - Ejecuta un script dentro del depurador. 
* - [source](https://docs.python.org/3/library/pdb.html#pdbcommand-source)` expression`
  - Muestra el código fuente de un objeto o función.
* - [unalias](https://docs.python.org/3/library/pdb.html#pdbcommand-unalias)` name`
  - Elimina un alias previamente definido.
* - [undisplay](https://docs.python.org/3/library/pdb.html#pdbcommand-undisplay)` [expression]`
  - Deja de mostrar una expresión previamente registrada con `display`.
* - [unt(il)](https://docs.python.org/3/library/pdb.html#pdbcommand-until)` [lineno]`
  - Continúa la ejecución hasta alcanzar una línea mayor que la actual.
```
