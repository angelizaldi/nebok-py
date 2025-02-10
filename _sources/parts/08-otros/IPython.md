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
## Shorcuts

A continución se enlistan algunos shorcuts del teclado al trabajar con IPython.

```{list-table}
:header-rows: 1
:name: ipython-shorcuts

* - Shortcut
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
* - `Ctrl + T`
  - Transpone dos caracteres
* - `Ctrl + F / Flecha-derecha`
  - Mueve el cursor una posición a la derecha
* - `Ctrl + B / Flecha-Izquierda`
  - Mueve el cursor una posición a la izquierda
```

<br>

---
## Obtener ayuda

Mientras se programa en IPython se puede obtener ayuda sobre los módulos, funciones y clases son los que se está trabajando

**Obtener ayuda de un objeto**: Si se quiere obtener ayuda de un objeto o sobre una función/método utilizar un signo de integorración `?` al final del nombre del objeto/método/función.

```{code-cell} ipython3
# Obtener ayuda sobre la clase list
list?
```

<br>

**Recuperar información de una función**: Para recuperar la sintaxis, el docstring, el código, entre otros datos de una función se pueden utilizar dos signos de interrogación `??` al final del nombre de la función:

```{code-cell} ipython3
# Recuperar información de una función
print??
```

**Buscar funciones, clases, métodos constantes**: Se puede utiliza un signo de interrogación `?` y _wildcards_ para enlistar todos los objetos que cumplan determinado patrón, para ello se utiliza el _wildcard_ `*` que representa cualquier caracter una o más veces:

```{code-cell} ipython3
# Enlistar todas las funciones que llevan `mean` en numpy
np.*mean*?
```

<br>

---
## Impresión (display)

IPython cuenta con la función `display()` que permite imprimir objetos con un mejor formato de lo que lo haría `print()`, así como también permite renderizar fórmulas de _LaTeX_ y elementos HTML.

```{note}
Por default en IPython utiliza display para imprimir objetos por lo que no es necesario usarlo explícitamente.
```

Algunos objetos que tienen un mejor formato al ser imprimidos por `display()` son los `DataFrame` de `pandas` y las gráficas de `Matplotlib.pyplot`:

**Ejemplo**: A continuación veremos la diferencia entre `print()` y `display()` al imprimir un `DataFrame`. Primero crearemos el `DataFrame`

```{code-cell} ipython3
# importar libreria
import pandas as pd

# Crear objeto
df = pd.DataFrame({'col1': [1, 2], 'col2': ['a', 'b']})
```

Ahora imprimiremos el objeto con `print()`
```{code-cell} ipython3
# Imprimir df
print(df)
```

Ahora imprimiremos el objeto con `display()`
```{code-cell} ipython3
# Imprimir df
display(df)
```
<br>

### Renderizar LaTeX

Para poder imprimir fórmulas de LaTeX es necesario importar de `IPython.display` la función `Math` y utilizar esta función dentro de `display()`. 

```{code-cell} ipython3
# Renderizar fórmulas de LaTeX
from IPython.display import Math

# fomurla de LaTeX
latex_formula = r'\frac{1}{2} \cdot \sqrt{3x-1} + \left( y^2 + 1 \right)'

display(Math(latex_formula))
```
- Notar que la cadena que contenga la fórmula de LaTeX debe de ser una cadena cruda (_raw string_).

<br>

### Renderizar HTML

Para poder imprimir contenido de HTML es necesario importar de `IPython.display` la función `HTML` y utilizar esta función dentro de `display()`. 

```{code-cell} ipython3
# Renderizar elementos HTML
from IPython.display import HTML

# Contenido HTML
html_content = "<h1>Hello, IPython!</h1>"

display(HTML(html_content))
```

<br>

---
## In y Out

Al trabajar con IPython cada sentencia escrita en la consola y cada resultado se almacenan en los objetos `In` del tipo `list` y `Out` del tipo `dict`. Como se muestra en la siguiente imagen:

```{image} ../images/In-Out.png
:name: IPython-in-and-out
:align: center
```

Tener en cuenta las siguientes características:
- **In**: En `In` se almacena las sentencias utilizadas en IPython como `str`. Para acceder a una sentencia basta con utilizar el índice de _In_.

```{image} ../images/In.png
:name: IPython-in
:align: center
```

- **Out**: En `Out` se almacena los resultados de los `In` (en caso de que haya). Es un diccionario cuyas llaves son el índice del _Out_ y cuyos valores son el resultado del _Out_. Se puede utilizar este objeto para manipular los resultados posteriormente.

```{image} ../images/Out.png
:name: IPython-out
:align: center
```

```{note}
Se puede acceder a los últimos tres resultados de `Out` con guiones bajos:
- '_': Último valor en `Out`.
- '__': Penúltimo valor en `Out`.
- '___': Antepenúltimo valor en `Out`.

Alternativamente se puede indicar un _Out_ específico con un guión bajo y el índice del _Out_: <br> `__Ind_`
```

<br/>

---
## Utilizar _conda_ o _pip_ desde IPython

Para poder utilizar _conda_ o _pip_ desde IPython es recomendado primero importar la librería `sys` y cada comando debe ir precedido por un `!`:

```{code-cell} ipython3
# Importar sys
import sys

# Mostrar información de pandas 
!pip show pandas
```

<br>

---
## Comandos mágicos

Los comandos mágicos, son comandos especiales precedidos por _%_ que permiten realizar diversas acciones, a continuación se enlistan algunos comandos y su descripción.

:::{note}
Para una lista completa y más información sobre los comandos mágicos visitar la [documentación](https://ipython.readthedocs.io/en/stable/interactive/magics.html) de IPython.
:::

```{list-table}
:header-rows: 1
:name: ipython-comandos-magicos

* - Comando
  - Descripción
* - **Ayuda**
  -
* - `%command?`
  - Retorna ayuda del comando mágico _command_ (sustitur _command_ por el nombre comando)
* - [%history](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-history)
  - Imprime el historial de entrada. Con el más reciente al último.
* - [%lsmagic](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-lsmagic)
  - Retorna el nombre de todos los comandos mágicos
* - [%magic](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-magic)
  - Retorna ayuda sobre los comandos mágicos de IPython
* - **Debugging**
  -
* - [%debug](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-debug)
  - Activa el depurador de errores interactivo.
* - [%pdb mode](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-pdb)
  - Controla la llamada automática del depurador de errores _pdb_.
* - **Profiling y Timing**
  -
* - [%prun expression](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-prun)
  - Ejecuta una expresión en el perfilador de Python.
* - [%time expression](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-time)
  - Reporta el tiempo de ejecución de una sentencia
* - [%timeit expression](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-timeit)
  - Reporta el tiempo promedio de ejecución de un un bloque (celda), a través de un ciclo. Importante, si se usa en una celda de _JupyterNotebook_ se debe poner soble `%`: `%%timeit`.
* - **Matplotlib**
  -
* - [%matplotlib](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-matplotlib)
  - Establece la integración de `matplotlib` con IPython, de manera que se puedan crear múltiples ventanas de gráficas sin interferir con la sesión de la consola
* - `%matplotlib inline`
  - (Solo _Jupyter Notebook_) Para establecer que las gráficas se muestren como una imagen estática dentro de los notebook
* - `%matplotlib notebook`
  - (Solo _Jupyter Notebook_) Para establecer que las gráficas se muestren como una imagen interactiva dentro del notebook, que nos permite hacer zoom, desplazarse por la gráfica, entre otras opciones. Para convertir la imagen interactiva en una estática, utilizar el botón azul de la esquina superior derecha
* - **Sistema**
  -
* - `%ls`
  - Retorna nombre y extensión de los archivos en el directorio actual
* - [%pwd](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-pwd)
  - Retorna el directorio actual. Se puede asignar a una variable
* - **Scripts**
  -
* - [%load script.py](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-load)
  - (Solo Jupyter Notebooks) Importa un script a un _cell_ de un notebook
* - [%run filename.py](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-run)
  - Ejecuta un script directamente en el shell de IPython. El archivo debe de estar en el directorio actual o indicar su ruta.
* - **Variables**
  -
* - [%reset](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-reset)
  - Elimina todas las variables/nombres definidas en el _namespace_ interactivo. Más información abajo
* - [%who](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-who)
  - Retorna las variables definidas en la sesión
* - [%whos](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-whos)
  - Retorna información de las variables definidas en la sesión, como el nombre, tipo de dato, tamaño o valor, entre otros
* - [%who_ls](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-who_ls)
  - Retorna un objeto `list` de las variables definidas en la sesión
* - [%xdel variable](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-xdel)
  - Elimina una variable de la sesión actual
* - **Otros**
  -
* - [%page OBJECT`](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-page)
  - Imprime un objeto de una manera más ordenada y limpia
* - [%xmode mode](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-xmode)
  - Controla cómo mostrar los errores cuando ocurre uno. Se debe de indicar _mode_, del más simple al más informativo: Plain, Context (default) y Verbose
```

### Comando _%history_

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

### Debugging

[%debug](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-debug) activa el depurador de errores interactivo al ocurrir un error o una excepción. Para ello se utiliza el comando `%debug` inmediatamente después de que occura un error. Al ejecutar el comando se iniciará una sesión `ipdb` (se puede identificar por que al inicio de cada línea aparece `ipdb>`) que permitirá de manera interactiva analizar el código para encontrar el error.
```shell
# Sintaxis de llamada
%debug [--breakpoint FILE:LINE] [statement ...]
```
:::{note}
Para salir de la sesión utilizar el comando `quit`.
:::

### Timing

Se refiere al proceo de identificar el tiempo de ejecución de una línea o un bloque de líneas. Existen diversos comandos mágicos que pueden ayudar a realizar dichas tareas:
- [%time expression](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-time): Tiempo de la ejecución de una sola sentencia. Ideal para comandos que duran más tiempo en ejecurse y que realizar la operación de manera iterativa no sesgue los resultados, como con ordenar.
- [%timeit expression](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-timeit): Tiempo de ejecución de una sola línea de manera iterativa.
- [%%timeit expression](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-timeit): Tiempo de ejecución de un bloque de código, por ejemplo, una celda de un _Jupyter Notebook_. Debe ser la primer sentencia en la celda.

Uso de `%timeit` y `%%timeit`:
Ambos se utilizan para calcular el tiempo de ejecución de una línea (`%timeit`) o de un bloque de líneas (`%%timeit`), la manera como lo cálcula es que ejecuta la misma línea o bloque de línea en varias ejecuciones y en cada ejecución corre el código de manera iterativa para estimar los tiempos de ejecución.
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

### Profiling

Se refiere al proceo de identificar las áreas que se pueden optimizar en una línea o un bloque de líneas, como la memoria consumida o el tiempo de ejecución. Existen diversos comandos mágicos que pueden ayudar a realizar dichas tareas:
- [%prun expression](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-prun): Ejecuta código con el profiler.
- `%lprun`: Ejcuta línea por línea con el profiler. Es más completo que `%prun`. Forma parte de la extensión [line_profiler](https://kernprof.readthedocs.io/en/latest/), es necesario instalarlo.
- `%mprun`: Ejecuta código con el profiler de memoria línea por línea. Forma parte de la extensión `memory_profiler`, es necesario instalarlo.

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


