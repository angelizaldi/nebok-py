# Jupyter

_Jupyter_ es un proyecto que abarca diferentes softwares que ofrecen diversas herramientas, entre los que destacan _Jupyter Notebooks_ y _Jupyter Lab_. En esta sección se presenta brevemente la interacción con estos softwares como _shortcuts_ y comandos de consola, entro otros.

:::{note}
Para más información consultar la [documentación](https://docs.jupyter.org/en/latest/) de _Jupyter_.
:::

Para usar _Jupyter_ es necesario instarlo:

:::{note}
_Jupyter Notebooks_ se instala automáticamente al instalarse _Anaconda_, por lo que no es necesario instalarlo manualmente.
:::

```shell
# Instalar Jupyter Notebook con pip
pip install jupyter

# Instalar Jupyter Lab con pip
pip install jupyterlab

# Instalar Jupyter Lab con conda
conda install -c conda-forge jupyterlab
```

Una vez instalada para abrir los software utilizar:

:::{caution}
Asegurarse de entrar primero al ambiente virtual en caso de que se haya instalado los _softwares_ en algún ambiente virtual específico (de _conda_ o de _python_).
:::

:::{caution}
En caso de usar _conda_ es posible que sea necesario primero activar _conda_, ya sea el _environment_ base o alguno en particular. Esto va a depender de cómo se instaló el _software_ de _Jupyter_ y _conda_.
:::

:::{warning}
Dependiendo del directorio desde donde se haya ejecutado el comando en la terminal, será el directorio base de _Jupyter_ (en cada sesión).
:::

```shell
## Jupyter Notebook
# Si se instaló con pip
jupyter notebook

# Si se instaló con conda
conda activate # Opcionalmente primero activar conda (ejm con base)
jupyter notebook

#-------------------------
## Jupyter Lab
# Si se instaló con pip
jupyter lab

# Si se instaló con conda
conda activate # Opcionalmente primero activar conda (ejm con base)
jupyter lab
```

<br/>

## Comandos

El comando `jupyer` es el comando principal para ejecutar aplicaciones del proyecto _Jupyter_. Este comando se ejecuta desde la terminal:

```shell
# Sintaxis de llamada
jupyter [-h] [--version] [--config-dir] [--data-dir] [--runtime-dir]
               [--paths] [--json] [--debug]
               [subcommand]
```

A continuación se enlistan las opciones del comando:

| Opción | Descripción |
| --- | --- |
| `jupyter -h, --help` | Muestra información y ayuda de los comandos. |
| `jupyter --version` | Muestra la versión de los paquetes _core_ de Jupyter. |
| `jupyter --config-dir` | Muestra la locación de la carpeta _config_ |
| `jupyter --data-dir` | Muestra la locación de la carpeta _data_ |
| `jupyter --runtime-dir` | Muestra la locación de la carpeta _runtime_ |
| `jupyter --paths` | Muestra todas las _search paths_. Opcionalmente añadir `--json` |
| `jupyter --json` | Imprime las _search paths_ en formato de JSON. |
| `jupyter --debug` | Imprime información de depuración sobre las _paths_. |

<br/>

### Subcomandos

Los subcomandos son comandos secundarios de _Jupyter_ asociados con alguna funcionalidad específica de _Jupyter_ como _notebooks_, _lab_ o _console_, a continuación se enlistas todos los subcomandos:

:::{caution}
Algunos subcomandos son necesarios instalarlos manualmente, mientras que otros suelen venir incluidos al instalar _Jupyter_ o _Jupyter Lab_.
:::

| Subcomando        | Descripción breve |
|-------------------|------------------|
| `book`           | Crea y gestiona libros Jupyter usando Jupyter Book. |
| `console`        | Inicia una consola interactiva de Jupyter. |
| `dejavu`         | Herramienta experimental para depuración y reproducción de sesiones. |
| `events`         | Muestra eventos registrados en Jupyter. |
| `execute`        | Ejecuta un _notebook_ Jupyter desde la línea de comandos. |
| `kernel`         | Administra procesos de kernel de Jupyter. |
| `kernelspec`     | Gestiona las especificaciones de los kernels de Jupyter. |
| `lab`            | Inicia JupyterLab, la interfaz de usuario basada en web. |
| `labextension`   | Gestiona extensiones para JupyterLab. |
| `labhub`         | Inicia JupyterHub en modo JupyterLab. |
| `migrate`        | Migra configuraciones y datos entre versiones de Jupyter. |
| `nbconvert`      | Convierte _notebooks_ Jupyter a diferentes formatos (HTML, PDF, etc.). |
| `notebook`       | Inicia la interfaz clásica de Jupyter Notebook. |
| `qtconsole`      | Inicia una consola basada en Qt para Jupyter. |
| `run`            | Ejecuta scripts y notebooks Jupyter desde la línea de comandos. |
| `server`         | Gestiona servidores de Jupyter. |
| `troubleshoot`   | Proporciona información para diagnosticar problemas en Jupyter. |
| `trust`          | Firma _notebooks_ Jupyter para ejecutar celdas sin advertencias. |

<br/>

#### _jupyter-book_

Construye y administra libros de _Jupyter_.

```shell
# Sintaxis de llamada
jupyter-book [OPTIONS] COMMAND [ARGS]...

# Alternativamente se puede usar solo jb
jb [OPTIONS] COMMAND [ARGS]...
```
**Opciones**:
- `--version`: Muestra la versión.
- `-h`, `--help`: Muestra ayuda de este subcomando.

**Comandos**

| Comando | Descripción |
| --- | --- |
| `build` | Convierte el contenido del libro o página a HTML o un PDF. |
| `clean` | Elimina el directorio _\_build_ excepto _jupyter_cache_. |
| `config` | Inspecciona el archivo _\_config.yml_. |
| `create` | Crea una plantilla de libro Jupyter que pueda personalizar. |
| `myst` | Manipula los archivos de _Myst markdown_. |
| `toc` | Línea de comandos para _sphinx-external-toc_. |

<br/>

#### _jupyter lab_

Inicia JupyterLab, la interfaz de usuario basada en web.

JupyterLab tiene tres modos de ejecución diferentes:
- Modo principal (`--core-mode`): En este modo, JupyterLab se ejecutará utilizando los recursos de JavaScript contenidos en el paquete Python `jupyterlab` instalado. En el modo principal, no se habilitan extensiones. Este es el valor predeterminado en una versión estable de JupyterLab si no tiene extensiones instaladas.
- Modo de desarrollo (`--dev-mode`): utiliza los paquetes de JavaScript locales no publicados en la carpeta `dev_mode`. En este caso, JupyterLab mostrará una franja roja en la parte superior de la página. Solo se puede utilizar si JupyterLab está instalado como `pip install -e .`.
- Modo de aplicación: JupyterLab permite que el usuario cree varias "aplicaciones" de JupyterLab con diferentes combinaciones de extensiones. El `--app-dir` se puede utilizar para establecer un directorio para diferentes aplicaciones. La ruta de la aplicación predeterminada se puede encontrar usando `jupyter lab path`.

:::{warning}
El comando `jupyter lab` tiene subcomandos los cuales no se documentan aquí. Consultar `jupyter lab --help`.
:::

```shell
# Sintaxis de llamada
jupyter lab [OPTIONS]...
```
Listado de opciones:

:::{note}
Para más información sobre cada opción consultar `jupyter lab --help`.
:::

| Opción | Descripción |
| --- | --- |
| `--debug` | Establece el nivel de depuración para la extensión y las aplicaciones del servidor subyacente. |
| `--show-config` | Muestra la configuración de la aplicación (formato legible por humanos). |
| `--show-config-json` | Muestra la configuración de la aplicación (formato JSON). |
| `--generate-config` | Genera el archivo _config_ predeterminado. |
| `-y` | Responde sí a cualquier pregunta en lugar de solicitar. |
| `--allow-root` | Permite que el servidor se ejecute desde _Root User_. |
| `--no-browser` | Evita la apertura de la URL predeterminada en el navegador. |
| `--autoreload` | Auto recarga la aplicación web. |
| `--script` | Obsoleto, ignorado. |
| `--no-script` | Obsoleto, ignorado. |
| `--core-mode` | Inicia la aplicación en modo _core_. |
| `--dev-mode` | Inicia la aplicación en modo _dev_ para que se ejecute desde la fuente. |
| `--skip-dev-build` | Omite la instalación inicial y la compilación JS de la aplicación en modo _dev_. |
| `--watch` | Inicia la aplicación en modo _watch_. |
| `--splice-source` | Empalma los paquetes fuente en el directorio de la aplicación. |
| `--expose-app-in-browser` | Exponga la instancia de la aplicación global al navegador a través de _window.jupyterapp_. |
| `--extensions-in-dev-mode` | Carga extensiones pre-construidas en el modo _dev_. |
| `--collaborative` | Para habilitar la colaboración en tiempo real, debe instalar la extensión `jupyter_collaboration`. |
| `--custom-css` | Carga CSS personalizados en los archivos HTML de plantilla. El valor predeterminado es falso. |
| `--log-level=<Enum>` | Establece el nivel de registro por valor o nombre. |
| `--config=<Unicode>` | Ruta completa del archivo _config_. |
| `--ip=<Unicode>` | La dirección IP del servidor Jupyter. |
| `--port=<Int>` | El puerto del servidor (env: jupyter_port). |
| `--port-retries=<Int>` | El número de puertos adicionales para probar si el puerto especificado no está disponible. |
| `--keyfile=<Unicode>` | La ruta completa a un archivo _key_ privado para su uso con SSL/TLS. |
| `--certfile=<Unicode>` | La ruta completa a un archivo de certificado SSL/TLS. |
| `--client-ca=<Unicode>` | La ruta completa a un certificado de autoridad de certificado para la autenticación del cliente SSL/TLS. |
| `--notebook-dir=<Unicode>` | El directorio para usar para _notebooks_ y _kernels_. |
| `--browser=<Unicode>` | Especifica qué comando usar para invocar un navegador web al iniciar el servidor. |
| `--pylab=<Unicode>` | Obsoleto: use `%pylab` o `%matplotlib` en el _notebook_ para habilitar _matplotlib_. |
| `--watch=<Bool>` | Indica si el servidor de la aplicación está en modo de _watch_. |
| `--app-dir=<Unicode>` | El directorio de aplicaciones para desde el cual iniciar JupyterLab. |

<br/>

#### _jupyter nbconvert_

Convierte _notebooks_ Jupyter a diferentes formatos (HTML, PDF, etc.).

```shell
# Sintaxis de llamada
jupyter nbconvert [OPTIONS]...

# A HTML
jupyter nbconvert mynotebook.ipynb --to html

# A markdown
jupyter nbconvert mynotebook.ipynb --to markdown

# A PDF
jupyter nbconvert mynotebook.ipynb --to pdf
```
Listado de opciones:

:::{note}
Para más información sobre cada opción consultar `jupyter nbconvert --help`.
:::

| Comando | Descripción |
| --- | --- |
| `--debug` | Establezca el nivel de registro en _logging.DEBUG_ (maximiza la salida de registro). |
| `--show-config` | Muestra la configuración de la aplicación (formato legible por humanos). |
| `--show-config-json` | Muestra la configuración de la aplicación (formato JSON). |
| `--generate-config` | Genera el archivo _config_ predeterminado. |
| `--execute` | Ejecuta el _notebook_ antes de la exportación. |
| `--allow-errors` | Continua la ejecución del _notebook_ incluso si una de las celdas arroja un error e incluye el mensaje de error en la salida de la celda (el comportamiento predeterminado es abortar la conversión). Esta bandera solo es relevante si `--execute` también se especificó. |
| `--stdin` | Lee un solo archivo de _notebook_ de _stdin_. Escribe el _notebook_ resultante con el nombre predeterminado 'notebook.*'. |
| `--stdout` | Escribe la salida de _notebook_ a _stdout_ en lugar de los archivos. |
| `--inplace` | Ejecuta _nbconvert_ _in-place_, sobrescribiendo el _notebook_ existente (solo relevante al convertir en formato de _notebook_). |
| `--clear-output` | Borra la salida del archivo actual y guarda _in-place_, sobrescribiendo el _notebook_ existente. |
| `--coalesce-streams` | Fusiona los resultados consecutivos de _stdout_ y _stderr_ en un _stream_ (dentro de cada celda). |
| `--no-prompt` | Excluye las indicaciones de entrada y salida del documento convertido. |
| `--no-input` | Excluye celdas de entrada e indicaciones de salida del documento convertido. |
| `--allow-chromium-download` | Indica si permitir la descarga de _chromium_ si no se encuentra una versión adecuada en el sistema. |
| `--disable-chromium-sandbox` | Deshabilita el _sandbox_ de seguridad de _chromium_ al convertir a PDF. |
| `--show-input` | Muestra la entrada del código. Esta bandera solo es útil para los usuarios de _dejavu_. |
| `--embed-images` | Incrusta las imágenes como _base64 dataurls_ en la salida. Este indicador solo es útil para las exportaciones HTML/WebPDF/Slides. |
| `--sanitize-html` | Indica si el HTML en las células de Markdown y las salidas de las celdas debe "sanitizarse". |
| `--log-level=<Enum>` | Establece el nivel de registro por valor o nombre. |
| `--config=<Unicode>` | Ruta completa del archivo _path_. |
| `--to=<Unicode>` | El formato de exportación que se utilizará: 'asciidoc', 'personalizado', 'html', 'latex', 'markdown', 'notebook', 'pdf', 'python', 'qtpdf', 'qtpng', 'rst', 'script', y 'webpdf'. |
| `--template=<Unicode>` | Nombre de la plantilla para usar. |
| `--template-file=<Unicode>` | Nombre del archivo de plantilla para usar. |
| `--theme=<Unicode>` | Tema específico de la plantilla (por ejemplo, el nombre de un tema Jupyterlab CSS distribuido como extensión _prebuilt_ para la plantilla de _lab_). |
| `--sanitize_html=<Bool>` | Indica si se debe "sanitizar" el HTML en las células de Markdown y las salidas de las células. Esto debe ser establecido en _True_ por _nbviewer_ o herramientas similares. |
| `--writer=<DottedObjectName>` | Clase _Writer_ usada para escribir los resultados de la conversión. |
| `--post=<DottedOrNone>` | Clase _PostProcessor_ utilizada para escribir los resultados de la conversión. |
| `--output=<Unicode>` | Sobrescribe el uso del nombre base para los archivos de salida. Admite reemplazos de patrones '{notebook_name}'. |
| `--output-dir=<Unicode>` | Directorio a utilizar para escribir salidas. El valor predeterminado se emite al directorio de cada _notebook_. |
| `--reveal-prefix=<Unicode>` | El prefijo de URL para _reveal.js_ (versión 3.x). |
| `--nbformat=<Enum>` | La versión _nbformat_ para escribir. |

<br/>

#### _jupyter notebook_

Inicia la interfaz clásica de Jupyter Notebook.

```shell
# Sintaxis de llamada
jupyter notebook [OPTIONS]...
```
Listado de opciones:

:::{note}
Para más información sobre cada opción consultar `jupyter notebook --help`.
:::

| Opción | Descripción |
| --- | --- |
| `--debug` | Establece el nivel de depuración para la extensión y las aplicaciones del servidor subyacente. |
| `--show-config` | Muestra la configuración de la aplicación (formato legible por humanos). |
| `--show-config-json` | Muestra la configuración de la aplicación (formato JSON). |
| `--generate-config` | Genera el archivo _config_ predeterminado. |
| `-y` | Responde sí a cualquier pregunta en lugar de solicitar. |
| `--allow-root` | Permite que el servidor se ejecute desde _Root User_. |
| `--no-browser` | Evita la apertura de la URL predeterminada en el navegador. |
| `--autoreload` | Auto recarga la aplicación web. |
| `--script` | Obsoleto, ignorado. |
| `--no-script` | Obsoleto, ignorado. |
| `--expose-app-in-browser` | Exponga la instancia de la aplicación global al navegador a través de _window.jupyterapp_. |
| `--custom-css` | Carga CSS personalizados en los archivos HTML de plantilla. El valor predeterminado es falso. |
| `--log-level=<Enum>` | Establece el nivel de registro por valor o nombre. |
| `--config=<Unicode>` | Ruta completa del archivo _config_. |

<br/>

---
## Shortcuts

Atajos disponibles en _jupyter notebooks_ y _jupyter lab_. 

:::{tip}
Se pueden consultar los atajos directamente en _Jupyter_ con el atajo `Shift + Cmd + H`.
:::

<br/>

### Archivos y Guardado

Comandos para guardar, imprimir y cerrar notebooks.

| Acción | Atajo |
| --- | --- |
| Guardar notebook | `Cmd + S` |
| Guardar notebook como | `Shift + Cmd + S` |
| Imprimir | `Cmd + P` |
| Cerrar y apagar notebook | `Ctrl + Shift + Q` |

<br/>

### Búsqueda y Comandos

Atajos para buscar texto, activar la paleta de comandos y ver los atajos de teclado.

| Acción | Atajo |
| --- | --- |
| Buscar | `Cmd + F` |
| Buscar siguiente | `Cmd + G` |
| Buscar anterior | `Shift + Cmd + G` |
| Finalizar búsqueda | `Escape` |
| Activar Command Palette | `Shift + Cmd + C` |
| Mostrar atajos de teclado | `Shift + Cmd + H` |

<br/>

### Cambio de Tipo de Celda

Atajos para cambiar entre celdas de código, _Markdown_, _Raw_ y encabezados.

:::{caution}
En la mayoría de estos atajos se debe estar en _select mode_.
:::

| Acción | Atajo |
| --- | --- |
| Cambiar de _edit mode_ a _select mode_ | `Escape` |
| Cambiar de _select mode_ a _edit mode_ | `Enter` |
| Cambiar a celda de código | `Y` |
| Cambiar a celda de código | `Y` |
| Cambiar a celda de Markdown | `M` |
| Cambiar a celda de texto sin formato (Raw) | `R` |
| Cambiar a encabezado nivel 1 | `1` |
| Cambiar a encabezado nivel 2 | `2` |
| Cambiar a encabezado nivel 3 | `3` |
| Cambiar a encabezado nivel 4 | `4` |
| Cambiar a encabezado nivel 5 | `5` |
| Cambiar a encabezado nivel 6 | `6` |

<br/>

### Control del Kernel

Comandos para interrumpir, reiniciar o gestionar el _kernel_.

| Acción | Atajo |
| --- | --- |
| Interrumpir kernel | `I + I` |
| Reiniciar kernel | `0 + 0` |

<br/>

### Depuración

Atajos específicos para el depurador de código en _JupyterLab_.

| Acción | Atajo |
| --- | --- |
| Panel de Depuración | `Shift + Cmd + E` |
| Pausar | `F9` |
| Siguiente | `F10` |
| Entrar en función (Step In) | `F11` |
| Salir de función (Step Out) | `Shift + F11` |
| Terminar | `Shift + F9` |

<br/>

### Edición y Control de Celdas

Atajos para modificar, copiar, cortar, eliminar, fusionar y deshacer cambios en celdas.

:::{caution}
En estos atajos se debe estar en _select mode_.
:::

| Acción | Atajo |
| --- | --- |
| Redo | `Shift + Cmd + Z` |
| Undo | `Cmd + Z` |
| Copiar celda | `C` |
| Cortar celda | `X` |
| Eliminar celda | `D + D` |
| Pegar celda debajo | `V` |
| Insertar celda arriba | `A` |
| Insertar celda debajo | `B` |
| Fusionar celda arriba | `Ctrl + Backspace` |
| Fusionar celda debajo | `Ctrl + Shift + M` |
| Fusionar celdas seleccionadas | `Shift + M` |

<br/>

### Ejecutar Celdas

Comandos para ejecutar una celda y definir cómo avanzar después de la ejecución.

:::{caution}
En estos atajos se debe estar en _select mode_.
:::

| Acción | Atajo |
| --- | --- |
| Ejecutar celda y avanzar | `Shift + Enter` |
| Ejecutar celda sin avanzar | `Ctrl + Enter / Cmd + Enter` |
| Ejecutar celda e insertar debajo | `Alt + Enter` |

<br/>

### Encabezados y Colapsado de Contenidos

Atajos para manejar encabezados y estructurar el contenido del notebook.

:::{caution}
En estos atajos se debe estar en _select mode_.
:::

| Acción | Atajo |
| --- | --- |
| Insertar encabezado arriba | `Shift + A` |
| Insertar encabezado abajo | `Shift + B` |
| Colapsar todos los encabezados | `Ctrl + Shift + ArrowLeft` |
| Expandir todos los encabezados | `Ctrl + Shift + ArrowRight` |
| Seleccionar encabezado arriba / colapsar | `ArrowLeft` |
| Seleccionar encabezado abajo / expandir | `ArrowRight` |

<br/>

### Interfaz y Configuración

Controles para administrar la interfaz, extensiones, configuraciones y paneles auxiliares.

| Acción | Atajo |
| --- | --- |
| Mostrar barra lateral izquierda | `Cmd + B` |
| Alternar interfaz simple | `Shift + Cmd + D` |
| Mostrar Administrador de Extensiones | `Shift + Cmd + X` |
| Abrir Explorador de Archivos | `Shift + Cmd + F` |
| Mostrar Ayuda Contextual | `Cmd + I` |
| Abrir nuevo Launcher | `Shift + Cmd + L` |
| Abrir Inspector de Propiedades | `Shift + Cmd + U` |
| Abrir Sesiones y Pestañas | `Shift + Cmd + B` |
| Abrir Editor de Configuración | `Cmd + ,` |
| Mostrar Tabla de Contenidos | `Shift + Cmd + K` |

<br/>

### Navegación en JupyterLab

Comandos para cambiar entre pestañas y administrar la interfaz de JupyterLab.

| Acción | Atajo |
| --- | --- |
| Cerrar pestaña | `Alt + W` |
| Activar siguiente pestaña | `Ctrl + Shift + ]` |
| Activar pestaña anterior | `Ctrl + Shift + [` |
| Activar siguiente barra de pestañas | `Ctrl + Shift + .` |
| Activar barra de pestañas anterior | `Ctrl + Shift + ,` |
| Activar pestaña usada previamente | `Shift + Cmd + '` |

<br/>

### Selección y Navegación de Celdas

Permite moverse entre celdas, seleccionar múltiples celdas y reorganizarlas.

:::{caution}
En estos atajos se debe estar en _select mode_.
:::

| Acción | Atajo |
| --- | --- |
| Seleccionar celda abajo | `ArrowDown / J` |
| Seleccionar celda arriba | `ArrowUp / K` |
| Extender selección arriba | `Shift + ArrowUp / Shift + K` |
| Extender selección abajo | `Shift + ArrowDown / Shift + J` |
| Extender selección hasta arriba | `Shift + Home` |
| Extender selección hasta abajo | `Shift + End` |
| Seleccionar todas las celdas | `Cmd + A` |
| Mover celda arriba | `Ctrl + Shift + ArrowUp` |
| Mover celda abajo | `Ctrl + Shift + ArrowDown` |