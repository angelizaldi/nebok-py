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


## Autocompletar

Al utilizar IPython o JupyterNotebooks se puede autocompletar el código mientras se escribe utilizando la tecla <span style="background-color:LightGray"> tab </span>.
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

## In y Out

Al trabajar con IPython cada sentencia escrita en la consola y cada resultado de almacenan en los objetos `In` del tipo `list` y `Out` del tipo `dict`. Como se muestra en la siguiente imagen:

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

Alternativamente se puede indicar un _Out_ especíco con un guión bajo y el índice del _Out_: <br> `_Ind`
```

## Utilizar _conda_ o _pip_ desde IPython

Para poder utilizar _conda_ o _pip_ desde IPython es recomendado primero importar la librería `sys` y cada comando debe ir precedido por un '!':

```{code-cell} ipython3
# Importar sys
import sys

# Mostrar información de pandas 
!pip show pandas
```

<br>

## Comandos mágicos

Los comandos mágicos, son comandos especiales precedidos por _%_ que permiten realizar diversas acciones, a continuación se enlistan algunos comandos y su descripción.

```{list-table}
:header-rows: 1
:name: ipython-comandos-magicos

* - Comando
  - Descripción
* - `%run script.py`
  - Ejecuta un script directamente en el shell de IPython. El archivo debe de estar en el directorio actual
* - `%reset`
  - Elimina todas las variables/nombres definidas en el _namespace_ interactivo. Más información abajo
* - `%time statement`
  - Reporta el tiempo de ejecución de una sentencia
* - `%%timeit statement`
  - Reporta el tiempo promedio de ejecución de un un bloque (celda), a través de un ciclo. Más información abajo
* - `%who`
  - Retorna las variables definidas en la sesión
* - `%who_ls`
  - Retorna un objeto `list` de las variables definidas en la sesión
* - `%whos`
  - Retorna información de las variables definidas en la sesión, como el nombre, tipo de dato, tamaño o valor, entre otros
* - `%page OBJECT`
  - Imprime un objeto de una manera más ordenada y limpia
* - `%xdel variable`
  - Elimina una variable de la sesión actual
* - `%pwd`
  - Retorna el directorio actual. Se puede asignar a una variable
* - `%ls`
  - Retorna nombre y extensión de los archivos en el directorio actual
* - `%lsmagic`
  - Retorna el nombre de todos los comandos mágicos
* - `%magic`
  - Retorna ayuda sobre los comandos mágicos de IPython
* - `%command?`
  - Retorna ayuda del comando mágico _command_ (sustitur _command_ por el nombre comando)
* - `%load script.py`
  - (Solo Jupyter Notebooks) Importa un script a un _cell_ de un notebook
* - `%paste`
  - Pega código del portapales al shell, respetando la identación y ejecuta el código al pegarlo
* - `%xmode mode`
  - Controla cómo mostrar los errores cuando ocurre uno. Se debe de indicar _mode_, del más simple al más informativo: Plain, Context (default) y Verbose
```

### Comando _%history_

Permite imprimir _n_ cantidad de elementos de los objetos _In_ y _Out_:
```shell
%history [-n] [-o] [range [range ...]]
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

Permite hacer _debugging_ del código al ocurrir un error o una excepción. Al ejecutar el comando se iniciará una sesión `ipdb` (se puede identificar por que al inicio de cada línea aparece `ipdb>`) que permitirá de manera interactiva analizar el código para encontrar el error. 

Para salir de la sesión utilizar el comando `quit`.

### Timing y profiling

Se refiere al proceo de identificar el tiempo de ejecución de una línea o un bloque de línea, así la memoria utilizada por una línea o un bloque de líneas. Existen diversos comandos mágicos que pueden ayudar a realizar dichas tareas:
- `%time`: Tiempo de la ejecución de una sola sentencia. Ideal para comandos que duran más tiempo en ejecurse y que realizar la operación de manera iterativa no sesgue los resultados, como con ordenar.
- `%timeit`: Tiempo de ejecución de una sola línea de manera iterativa.
- `%%timeit`: Tiempo de ejecución de un bloque de código, por ejemplo, una celda de un _Jupyter Notebook_. Debe ser la primer sentencia en la celda.
- `%pru`n: Ejecuta código con el profiler.
- `%lprun`: Ejcuta línea por línea con el profiler.
- `%mprun`: Ejecuta código con el profiler de memoria línea por línea.


Uso de `%timeit` y `%%timeit`:
Ambos se utilizan para calcular el tiempo de ejecución de una línea (`%timeit`) o de un bloque de líneas (`%%timeit`), la manera como lo cálcula es que ejecuta la misma línea o bloque de línea en varias ejecuciones y en cada ejecución corre el código de manera iterativa para estimar los tiempos de ejecución.
```shell
%timeit [-n<N> -r<R> [-t|-c] -q -p<P> -o] statement

%%timeit [-n<N> -r<R> [-t|-c] -q -p<P> -o] setup_code
```
- \-n\<N\>: Especifica el número de iteraciones (cúantas veces será ejecutado el código en cada ejecución).
- \-r\<R\>: Especifica el número de ejecuciones/runs.
- \-o: Para indicar que se retorne un objeto `TimeitResult`, el cual se puede almacenar en una variable.

Para almacenar los resultados en un `TimeitResult` se puede hacer de la siguiente manera:
```shell
list_comp = %timeit -o [i**2 for i in range(1000)]
```
- Posteriormente se puede acceder a las propiedades de `TimeitResult`:
    - `TimeitResult.timings` - `list`: Lista de los tiempos de cada ejecución (run).
    - `TimeitResult.best` - `float`: Mejor tiempo.
    - `TimeitResult.worst` - `float`: Peor tiempo.


## Matplotlib

Al utilizar la librería `matplotlib` en IPython no es necesario usar `plt.show()`. Sin embargo existen unos comandos mágicos que mejoran la experiencia: 

```{list-table}
:header-rows: 1
:name: ipython-matplotlib

* - Comando
  - Descripción
* - `%matplotlib`
  - Establece la integración de `matplotli` con IPython, de manera que se puedan crear múltiples ventanas de gráficas sin interferir con la sesión de la consola
* - `%matplotlib inline`
  - (Solo _Jupyter Notebook_) Para establecer que las gráficas se muestren como una imagen estática dentro de los notebook
* - `%matplotlib notebook`
  - (Solo _Jupyter Notebook_) Para establecer que las gráficas se muestren como una imagen interactiva dentro del notebook, que nos permite hacer zoom, desplazarse por la gráfica, entre otras opciones. Para convertir la imagen interactiva en una estática, presiona en botón azul de la esquina superior derecha
```


