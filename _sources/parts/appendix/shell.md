# Shell

Un _shell_ es un programa que sirve como interfaz entre el usuario y un sistema operativo. Permite ejecutar comandos, administrar archivos y automatizar tareas. Existen diferentes tipos de _shell_, como _Bash_, _Zsh_, _Fish_ y _PowerShell_, cada uno con sus propias características. En esencia, cuando se escribe un comando en la terminal y se presiona <kbd>Enter</kbd>, el _shell_ lo interpreta y le dice al sistema qué hacer.

:::{caution}
Este sitio está enfocado más en funcionalidades de _Bash_, que es el principal intérprete para sistemas operativos tipo Unix, aunque igualmente puede ser útil para otros intérpretes como _Zsh_.

Todos los links relacionados con documentación en este sitio llevarán a la documentación de _Bash_ y en el caso de algunos comandos a la documentación de _man pages_.
:::

:::{warning}
En este sitio únicamente se revisa lo básico de _Bash_. Para más información consultar la [documentación](https://www.gnu.org/software/bash/manual/bash.html) de _Bash_
:::


Los dos principales intérpretes para sistemas Unix son lo siguientes:
- _Bash_ (_Bourne Again Shell_) es un intérprete de comandos y un lenguaje de _scripting_ para sistemas operativos tipo Unix, como Linux y macOS. Es una evolución del _shell Bourne_ (sh), con características mejoradas como historial de comandos, expansiones de variables y compatibilidad con programación estructurada. Es el _shell_ por defecto en muchas distribuciones de Linux.
- _Zsh_ es otro intérprete de comandos, similar a _Bash_, pero con características adicionales como autocompletado avanzado, corrección de errores tipográficos y mayor personalización. _Zsh_ es el _shell_ predeterminado en lugar de _Bash_ en _macOS_ (desde Catalina en adelante).

:::{tip}
Para saber que _shell_ es el predeterminado usar `echo $SHELL` en la terminal, lo cual en Unix usualmente retornará `bin/bash` o `bin/zsh` dependiendo del intérprete predeterminado. 
:::

Para verificar información relacionada al _shell_ instalado o realizar algunas acciones básicas usar los siguientes comandos.

```sh
# Imprimir shell predeterminado
echo $SHELL

# Imprimir versión de bash
bash -- version

# Imprimir versión de zsh
zsh -- version

# Imprimir ubicación del ejecutable (bash)
which bash

# Imprimir ubicación del ejecutable (zsh)
which zsh

# Activar bash (en caso que no sea el predeterminado)
bash # para salir usar: exit

# Activar zsh (en caso que no sea el predeterminado)
zsh # para salir usar: exit

# Cambiar permanentemente a bash
chsh -s /bin/bash

# Cambiar parmanentemente a zsh
chsh -s /bin/zsh
```

<br/>

## Conceptos básicos

A continuación se enlistan algunos conceptos básicos útiles para esta sección.

:::{note}
Para otros conceptos visitar la [documentación](https://www.gnu.org/software/bash/manual/bash.html#Concept-Index) de _Bash_.
:::

**General**:
- **Shell**: Interfaz que permite ejecutar comandos en un sistema operativo.
- **Terminal**: Aplicación que proporciona acceso a la línea de comandos.
- **Prompt**: Símbolo o texto que indica que el _shell_ está listo para recibir comandos.
- **Comando**: Instrucción que se ejecuta en el _shell_.
- **Argumento**: Parámetro que se pasa a un comando para modificar su comportamiento.
- **Flag (opción)**: Modificadores que cambian el comportamiento de un comando (ejemplo: `ls -l`).
- **Scripts de shell**: Archivos con secuencias de comandos ejecutables (`.sh`).

**Directorios y Rutas**:
- **Directorio**: Ubicación en el sistema de archivos que puede contener archivos y otros directorios (subdirectorios). Funciona como una carpeta en un sistema operativo gráfico.
    - **Directorio raíz (_Root Directory_)**: Es el directorio principal del sistema de archivos, representado por `/` en sistemas Unix/Linux. Contiene todos los demás directorios y archivos del sistema.
    - **Directorio de Inicio (_Home Directory_)**: Es el directorio personal de un usuario en el sistema, donde se almacenan archivos de configuración y documentos. Se representa con `~` en el shell.
    - **Directorio padre**: Es el directorio que contiene a otro directorio. Se puede referenciar usando `..` en comandos del shell.
    - **Directorio actual**: Es el directorio activo. Se puede referenciar usando `.` en comandos del shell.
- **Rutas absolutas y relativas**: Formas de referirse a archivos y directorios en el sistema.
    - **Ruta absoluta**: Especifica la ubicación de un archivo o directorio desde el directorio raíz `/`. Siempre comienza con `/`. Ejemplo: `/home/usuario/documentos/archivo.txt`.
    - **Ruta relativa**: Especifica la ubicación de un archivo o directorio en relación con el directorio actual. No comienza con `/`. Ejemplo: `documentos/archivo.txt` (si se está en `/home/usuario/`).

**Funcionalidades de _shell_**:
- **Redirección (`>`, `>>`, `<`)**: Mecanismo para enviar o recibir datos desde archivos.
- **Pipes (`|`)**: Permiten conectar la salida de un comando con la entrada de otro.
- **Variables de entorno**: Variables globales que afectan el comportamiento del shell (ejemplo: `$HOME`, `$PATH`).
- **Expansión de variables**: Uso de variables dentro del shell (ejemplo: `echo $USER`).
- **Globbing (`*`, `?`, `[]`)**: Uso de comodines para hacer coincidencias en nombres de archivos.
- **Expresiones regulares**: Patrones utilizados para buscar y manipular texto en comandos como `grep` y `sed`.
- **Permisos de archivos (`r`, `w`, `x`)**: Control de acceso a archivos y directorios.
- **Usuarios y grupos**: Gestión de cuentas en el sistema (`whoami`, `groups`, `id`).
- **Procesos (`ps`, `top`, `kill`)**: Administración de tareas en ejecución.
- **Gestión de trabajos (`jobs`, `fg`, `bg`, `&`)**: Control de procesos en segundo plano y foreground.
- **Aliases**: Atajos personalizados para comandos (`alias ll='ls -la'`).
- **Historial de comandos (`history`)**: Registro de comandos ejecutados en el shell.
- **Shebang (`#!`)**: Línea que define qué intérprete debe ejecutar un script (`#!/bin/bash`).
- **Subshells (`$(command)`, `` `command` ``)**: Ejecución de comandos dentro de otro comando.
- **Condiciones y estructuras de control (`if`, `case`, `for`, `while`)**: Lógica de programación en scripts.
- **Funciones en shell**: Bloques reutilizables de código dentro de un script.
- **Gestión de paquetes**: Instalación y actualización de software (`apt`, `yum`, `brew`).
- **Configuración del shell (`.bashrc`, `.zshrc`)**: Archivos que personalizan el entorno de trabajo.
- **Tareas programadas (`cron`, `at`)**: Ejecución automática de comandos en horarios específicos.

<br/>

## Atajos de navegación

Son atajos relacionados con la navegación por el sistema de archivos. El _shell_ toma estos patrones y los expande o reemplaza por la ruta real del directorio al que hacen referencia antes de ejecutar el comando, se utilizan para simplificar la especificación de rutas en el sistema de archivos.

| Atajo    | Descripción                                  | Ejemplo de uso                     |
|----------|----------------------------------------------|------------------------------------|
| `.`      | Directorio actual                            | `cp archivo.txt ./subdir/`         |
| `..`     | Directorio padre                             | `cd ..` (sube un nivel)            |
| `~`      | Directorio _home_ del usuario actual           | `cd ~` o `ls ~/Documentos`         |
| `-`      | Directorio anterior (_OLDPWD_)                 | `cd -` (alterna entre directorios) |
| `../..`  | Subir dos niveles en la jerarquía            | `cd ../../`                        |
| `~usuario`| Directorio _home_ del usuario especificado     | `ls ~otrousuario/Downloads`        |

<br/>

## Operadores

A continuación se enlistan los operadores de _Bash_ por categorías.

### Archivos

Verifican propiedades de archivos y directorios, como existencia, permisos o tipo.

| Operador | Descripción | Ejemplo |
|----------|------------|---------|
| `-f` | Verifica si un archivo existe y es un archivo normal. | `[ -f archivo.txt ] && echo "Existe"` |
| `-d` | Verifica si un directorio existe. | `[ -d carpeta ] && echo "Existe"` |
| `-r` | Verifica si un archivo es legible. | `[ -r archivo.txt ] && echo "Legible"` |
| `-w` | Verifica si un archivo es escribible. | `[ -w archivo.txt ] && echo "Escribible"` |
| `-x` | Verifica si un archivo es ejecutable. | `[ -x script.sh ] && echo "Ejecutable"` |

(sh-operadores-cadenas)=
### Cadenas

Estos operadores se utilizan para comparar cadenas o retornar información sobre el contenido de una cadena.

| Operador | Descripción | Ejemplo |
|----------|------------|---------|
| `=` | Comparación de cadenas: igual. | `[ "abc" = "abc" ] && echo "Iguales"` |
| `!=` | Comparación de cadenas: diferente. | `[ "abc" != "xyz" ] && echo "Diferentes"` |
| `-z` | Verifica si una cadena está vacía. | `[ -z "" ] && echo "Vacía"` |
| `-n` | Verifica si una cadena no está vacía. | `[ -n "Hola" ] && echo "No vacía"` |

:::{caution}
Para comparaciones de cadenas lexicográficas en evaluaciones condicionales usando `[ ]` se deben de escapar lo operadores `<`, `>`, `<=` y `>=` con `\`, por ejemplo `\>` para "mayor que". Esto no es necesario al usar las evaluaciones condicionales mejoradas `[[ ]]`. Para más información consultar {ref}`shell-conditional-expressions`.
:::

### Comparación

Estos operadores comparan valores y devuelven un resultado booleano (`true`/`false`). Se usan principalmente en estructuras condicionales (`if`, `while`, etc.).

:::{note}
Para comparaciones entre cadenas ver {ref}`sh-operadores-cadenas`.
:::

| Operador | Descripción | Ejemplo |
|----------|------------|---------|
| `-eq` | Comparación numérica: igual. | `[ 5 -eq 5 ] && echo "Iguales"` |
| `-ne` | Comparación numérica: no igual. | `[ 5 -ne 3 ] && echo "Diferentes"` |
| `-lt` | Comparación numérica: menor que. | `[ 3 -lt 5 ] && echo "Menor"` |
| `-le` | Comparación numérica: menor o igual. | `[ 3 -le 3 ] && echo "Menor o igual"` |
| `-gt` | Comparación numérica: mayor que. | `[ 5 -gt 3 ] && echo "Mayor"` |
| `-ge` | Comparación numérica: mayor o igual. | `[ 5 -ge 5 ] && echo "Mayor o igual"` |

### Control de Flujo

Estos operadores permiten controlar cómo se ejecutan los comandos en secuencia, en paralelo o condicionalmente. Determinan si un comando se ejecuta dependiendo del éxito o fracaso de otro, o si se ejecuta en segundo plano.

| Operador | Descripción | Ejemplo |
|----------|------------|---------|
| `&&` | Ejecuta el segundo comando solo si el primero tiene éxito. | `mkdir nueva_carpeta && cd nueva_carpeta` |
| `||` | Ejecuta el segundo comando solo si el primero falla. | `ls archivo.txt \|\| echo "No existe"` |
| `;` | Separa y ejecuta múltiples comandos secuencialmente. | `echo "Hola"; echo "Mundo"` |
| `&` | Ejecuta un comando en segundo plano. | `sleep 10 &` |

### Evaluación condicional

Los constructores `[ ]` y `[[ ]]` se usan para evaluar condiciones en _scripts_ (expresiones que retornan `true` o `false`). `[[ ]]` es una versión más potente que admite operadores adicionales y es preferible en _bash_ moderno.

:::{note}
Para más información de estos operadores consultar {ref}`shell-conditional-expressions`.
:::

:::{note}
Los operadores `-a` y `-o` solo se usan con `[ ]` (corchetes simples), en corchetes dobles se puede usar `&&` y `||`. Para más información consultar {ref}`shell-conditional-expressions`.
:::

| Operador | Descripción | Ejemplo |
|----------|------------|---------|
| `[ ]` | Evaluación condicional (test). | `[ -f archivo.txt ] && echo "Existe"` |
| `[[ ]]` | Evaluación condicional mejorada. | `[[ "abc" == "abc" ]] && echo "Iguales"` |
| `!` | Niega una condición. | `[ ! -f archivo.txt ] && echo "No existe"` |
| `-a` -| Operador _AND_ solo con `[ ]` | `[ -f archivo.txt -a -r archivo.txt ] && echo "No existe y no es legible"` |
| `-o` -| Operador _OR_ solo con `[ ]` | `[ -d directorio -o -f archivo.txt ] && echo "Existe el directorio o existe el archivo"` |

### Redirección de Entrada/Salida

Estos operadores gestionan cómo se manejan los flujos de datos (_input/output_) entre comandos y archivos. Permiten enviar la salida de un comando a un archivo, leer datos desde un archivo o encadenar comandos mediante tuberías (`|`).

| Operador | Descripción | Ejemplo |
|----------|------------|---------|
| `|` | Pasa la salida de un comando como entrada de otro. | `ls -l \| grep "txt"` |
| `>` | Redirige la salida a un archivo (sobrescribe). | `echo "Hola" > archivo.txt` |
| `>>` | Redirige la salida a un archivo (añade sin sobrescribir). | `echo "Mundo" >> archivo.txt` |
| `<` | Usa un archivo como entrada de un comando. | `sort < lista.txt` |
| `<<` | Redirección de entrada con heredoc. | `cat << EOF` |
| `<<<` | Redirección de entrada con una cadena. | `grep foo <<< "foo bar"` |

### Sustitución y evaluación

Estos operadores permiten incrustar la salida de un comando dentro de otro (`$(cmd)` o `cmd`) o realizar cálculos aritméticos (`$((expr))`). Son útiles para dinamizar comandos y _scripts_.

| Operador | Descripción | Ejemplo |
|----------|------------|---------|
| `$(cmd)` | Sustitución de comandos. | `echo "Hoy es $(date)"` |
| `` `cmd` `` | Sustitución de comandos (forma antigua). | `` echo "Hoy es `date`" `` |
| `$((expr))` | Evaluación aritmética. | `echo $((3 + 2))` |

:::{note}
Para más información sobre la evaluación aritmética ver {ref}`sh-evaluacion-aritmetica`. Las evaluaciones aritméticas tienen sus propios operadores.
:::

<br/>

## Palabras reservadas

Las palabras reservadas en shell son términos con un significado especial predefinido dentro de la sintaxis del lenguaje del shell (como Bash).

:::{note}
Para más información consultar la [documentación](https://www.gnu.org/software/bash/manual/bash.html#Reserved-Words) de _bash_.
:::

:::{warning}
No se puede usar palabras reservadas como nombres para variables, funciones o alias.
:::

| Palabra Reservada (Keyword) | Descripción                                                                 |
|-----------------------------|-----------------------------------------------------------------------------|
| `if`                        | Inicia una estructura de control condicional.                                |
| `then`                      | Se usa junto con `if` para definir el bloque de código a ejecutar si la condición es verdadera. |
| `else`                      | Se usa para definir el bloque de código a ejecutar si la condición de `if` es falsa. |
| `elif`                      | Expresión condicional adicional, que se coloca entre `if` y `else`.         |
| `fi`                        | Finaliza una estructura condicional `if`.                                    |
| `for`                       | Define un bucle que recorre una lista de valores.                           |
| `in`                        | Se usa dentro de los bucles `for` para iterar sobre elementos.               |
| `do`                        | Inicia el bloque de código que se ejecutará dentro de un bucle `for` o `while`. |
| `done`                      | Finaliza el bloque de código dentro de un bucle `for` o `while`.             |
| `while`                     | Define un bucle que ejecuta un bloque de código mientras se cumpla una condición. |
| `until`                     | Define un bucle que ejecuta un bloque de código hasta que se cumpla una condición. |
| `break`                     | Sale de un bucle prematuramente.                                             |
| `continue`                  | Salta a la siguiente iteración del bucle.                                    |
| `case`                       | Inicia una estructura de selección múltiple, similar a `switch` en otros lenguajes. |
| `esac`                       | Finaliza una estructura `case`.                                             |
| `select`                     | Crea un menú de selección basado en las entradas del usuario.               |
| `function`                   | Define una función en un script de bash.                                    |
| `return`                     | Sale de una función y opcionalmente devuelve un valor.                      |
| `exit`                       | Finaliza el script o cierra la sesión actual con un código de salida.       |
| `trap`                       | Establece una acción a ejecutar cuando se recibe una señal.                 |
| `test`                       | Realiza una prueba condicional, como verificar si un archivo existe.       |
| `[[`                         | Inicia una prueba condicional extendida (usada generalmente para comparar cadenas y otros valores). |
| `]]`                         | Finaliza una prueba condicional extendida.                                 |
| `[[`                         | Inicia una condición extendida para evaluaciones más complejas.             |
| `alias`                      | Define un alias para un comando o conjunto de comandos.                     |
| `unalias`                    | Elimina un alias previamente definido.                                      |
| `exec`                       | Reemplaza el proceso actual con el especificado.                            |
| `local`                      | Define una variable local dentro de una función.                           |
| `readonly`                   | Marca una variable como de solo lectura, impidiendo su modificación.       |

<br/>

## Variables

Las variables permiten almacenar valores son un nombre en particular y poder hacer referencia a esos valores posteriormente en un _script_. Para definir variables en _bash_ basta con asignar un valor con el operador `=`.

:::{caution}
No debe haber espacios ni antes ni después del signo igual.
:::

```sh
# Definir una variable
var_name=val
```
- El nombre de la variable debe de satisfacer los siguientes puntos:
    - Puede contener letras (mayúsculas y minúsculas), números y el guion bajo (_).
    - Debe comenzar con una letra o un guion bajo.
    - Es sensible a mayúsculas y minúsculas.
- Los valores pueden ser cadenas de texto, números o el resultado de comandos.
    - Si el valor contiene espacios u otros caracteres especiales, es recomendable encerrarlo entre comillas simples o dobles.
    - Las comillas dobles permiten la expansión de variables (`$variable`) y la sustitución de comandos (`$(comando)` o `comando`) dentro de la cadena. 

:::{note}
Las variables que se definen de esta manera son variables de entorno locales al _shell_ actual o al _script_ en el que se definen.
:::

Para poder acceder al valor de una variable en un comando o _script_ se debe preceder el nombre de la variable con el signo de dólar (`$`).

```sh
# Imprimir valor de una variable
echo "$var_name"

# Imprimir cadena y valor de una variable
echo "El valor de mi variable es $var_name"

# Usar variable en expresión condicional
if [ "$var_name" = "my_value" ]; then
  echo "$var_name"
fi
```

Para que una variable esté disponible en otros subprocesos (como otros _scripts_ que llaman desde un _script_), se debe usar el comando `export`:

```sh
# Exportar variable
export MI_VARIABLE="valor"
```

<br/>

## Variables de Ambiente

Las variables de ambiente en _shell_ son valores dinámicos con nombre que están disponibles para el _shell_ y todos los procesos (programas y _scripts_) que se ejecutan dentro de él.

:::{tip}
Cuando se quiera usar o imprimir el valor de una variable se tiene que usar `$` antes del nombre (`$VAR_NAME`) para efectivametne recuperar el contenido de la misma.
:::

:::{note}
Para una lista completa vistar la documentación de _bash_, particularmente la sección de [Shell Variables](https://www.gnu.org/software/bash/manual/bash.html#Shell-Variables).
:::

| Variable          | Descripción                                                                 |
|-------------------|-----------------------------------------------------------------------------|
| `HOME`            | Ruta del directorio personal del usuario actual.                           |
| `PATH`            | Lista de directorios donde el sistema busca ejecutables, separados por `:`.|
| `USER` / `LOGNAME`| Nombre del usuario actual.                                                 |
| `SHELL`           | Ruta al intérprete de comandos del usuario.                                |
| `PWD`             | Directorio de trabajo actual (Present Working Directory).                  |
| `OLDPWD`          | Directorio de trabajo anterior.                                            |
| `TERM`            | Tipo de terminal en uso (ej. `xterm-256color`).                            |
| `LANG` / `LC_*`   | Configuración de idioma y localización (ej. `en_US.UTF-8`).                |
| `EDITOR`          | Editor de texto preferido (ej. `vim`, `nano`).                             |
| `VISUAL`          | Editor visual preferido (similar a `EDITOR`).                              |
| `PS1`             | Cadena de prompt primaria del shell.                                       |
| `PS2`             | Cadena de prompt secundaria (para comandos multilínea).                    |
| `HOSTNAME`        | Nombre del sistema host.                                                   |
| `TMPDIR`          | Directorio para archivos temporales (alternativo a `/tmp`).                |
| `DISPLAY`         | Identificador de pantalla para servidores X11 (ej. `:0`).                  |
| `XDG_*`           | Variables de configuración para entornos de escritorio (estándar XDG).     |
| `SSH_*`           | Variables relacionadas con conexiones SSH (ej. `SSH_CLIENT`).              |
| `HTTP_PROXY`      | URL del proxy para conexiones HTTP.                                        |
| `HTTPS_PROXY`     | URL del proxy para conexiones HTTPS.                                       |
| `NO_PROXY`        | Lista de dominios excluidos del proxy.                                     |
| `MANPATH`         | Lista de directorios donde buscar páginas de manual.                       |
| `LD_LIBRARY_PATH` | Lista de directorios para buscar bibliotecas compartidas en tiempo de ejecución.|

<br/>

## Comandos

Un comando en _Bash_ es una instrucción que le das al intérprete de comandos (Bash) para que realice una acción específica. Puede ser desde ejecutar un programa, manipular archivos, mostrar información del sistema, hasta controlar el flujo de un script. Existen tres tipos principales de comandos:
- Comandos _Builtin_: Son comandos que están implementados directamente dentro del propio shell de Bash. Unos son heredados de _shell_ y otros son nativos de _Bash_.
- Comandos del sistema: Son programas ejecutables que residen en el sistema de archivos (generalmente en directorios como `/bin`, `/usr/bin`, `/usr/local/bin`).

:::{warning}
En esta sección no se enlistan todos los comandos de _bash_. Para más información consultar la [documentación](https://www.gnu.org/software/bash/manual/bash.html#Builtin-Index) de _Bash_.
:::

**Comandos de Shell Builtin**

Comandos heredados de _Bourne Shell_.

```{list-table}
:header-rows: 1

* - Comando
  - Descripción
* - [. (a period)](https://www.gnu.org/software/bash/manual/bash.html#index-_002e)
  - Comando nulo. No hace nada; útil como placeholder o para evaluaciones.
* - [: (a colon)](https://www.gnu.org/software/bash/manual/bash.html#index-_003a)
  - Ejecuta un script en el contexto actual del shell (igual que `source`).
* - [break](https://www.gnu.org/software/bash/manual/bash.html#index-break)
  - Sale de un bucle `for`, `while` o `until`.
* - [cd](https://www.gnu.org/software/bash/manual/bash.html#index-cd)
  - Cambia el directorio actual.
* - [continue](https://www.gnu.org/software/bash/manual/bash.html#index-continue)
  - Salta a la siguiente iteración de un bucle.
* - [eval](https://www.gnu.org/software/bash/manual/bash.html#index-eval)
  - Ejecuta una cadena como si fuera un comando del shell.
* - [exec](https://www.gnu.org/software/bash/manual/bash.html#index-exec)
  - Reemplaza el proceso del shell con otro comando.
* - [exit](https://www.gnu.org/software/bash/manual/bash.html#index-exit)
  - Termina el script o shell actual, con un código de salida.
* - [export](https://www.gnu.org/software/bash/manual/bash.html#index-export)
  - Define variables de entorno disponibles para subprocesos.
* - [getopts](https://www.gnu.org/software/bash/manual/bash.html#index-getopts)
  - Procesa argumentos pasados al script (estilo POSIX).
* - [hash](https://www.gnu.org/software/bash/manual/bash.html#index-hash)
  - Muestra o gestiona el hash interno de comandos usados por el shell.
* - [pwd](https://www.gnu.org/software/bash/manual/bash.html#index-pwd)
  - Muestra el directorio de trabajo actual.
* - [readonly](https://www.gnu.org/software/bash/manual/bash.html#index-readonly)
  - Marca una variable como de solo lectura.
* - [return](https://www.gnu.org/software/bash/manual/bash.html#index-return)
  - Termina una función y opcionalmente establece un código de retorno.
* - [shift](https://www.gnu.org/software/bash/manual/bash.html#index-shift)
  - Desplaza los parámetros posicionales ($1, $2, ...) hacia la izquierda.
* - [test](https://www.gnu.org/software/bash/manual/bash.html#index-test)
  - Evalúa una condición (igual que `[ ... ]`).
* - [times](https://www.gnu.org/software/bash/manual/bash.html#index-times)
  - Muestra el tiempo de CPU usado por el shell y procesos hijos.
* - [trap](https://www.gnu.org/software/bash/manual/bash.html#index-trap)
  - Ejecuta un comando cuando se recibe una señal (por ejemplo, al salir del script).
* - [umask](https://www.gnu.org/software/bash/manual/bash.html#index-umask)
  - Muestra o establece los permisos por defecto para nuevos archivos/directorios.
* - [unset](https://www.gnu.org/software/bash/manual/bash.html#index-unset)
  - Elimina variables o funciones del entorno.
```

**Comandos de Bash Builtin**

Comandos que son exclusivos o que se han ampliado en _Bash_.

```{list-table}
:header-rows: 1

* - Comando
  - Descripción
* - [alias](https://www.gnu.org/software/bash/manual/bash.html#index-alias)
  - Crea un atajo o reemplazo para un comando.
* - [bind](https://www.gnu.org/software/bash/manual/bash.html#index-bind)
  - Muestra o modifica las asignaciones de teclas del readline.
* - [builtin](https://www.gnu.org/software/bash/manual/bash.html#index-builtin)
  - Ejecuta un comando interno del shell, incluso si hay uno externo con el mismo nombre.
* - [caller](https://www.gnu.org/software/bash/manual/bash.html#index-caller)
  - Muestra información sobre la pila de llamadas (funciones) del shell.
* - [command](https://www.gnu.org/software/bash/manual/bash.html#index-command)
  - Ejecuta un comando, ignorando alias y funciones con el mismo nombre.
* - [declare](https://www.gnu.org/software/bash/manual/bash.html#index-declare)
  - Declara variables y da atributos (como tipo de dato, solo lectura, etc.).
* - [echo](https://www.gnu.org/software/bash/manual/bash.html#index-echo)
  - Imprime texto en la salida estándar.
* - [enable](https://www.gnu.org/software/bash/manual/bash.html#index-enable)
  - Habilita o deshabilita comandos internos del shell.
* - [help](https://www.gnu.org/software/bash/manual/bash.html#index-help)
  - Muestra ayuda sobre los comandos internos de Bash.
* - [let](https://www.gnu.org/software/bash/manual/bash.html#index-let)
  - Realiza operaciones aritméticas.
* - [local](https://www.gnu.org/software/bash/manual/bash.html#index-local)
  - Declara variables locales dentro de funciones.
* - [logout](https://www.gnu.org/software/bash/manual/bash.html#index-logout)
  - Cierra una sesión interactiva de shell de login.
* - [mapfile](https://www.gnu.org/software/bash/manual/bash.html#index-mapfile)
  - Lee líneas desde la entrada estándar y las guarda en un array.
* - [printf](https://www.gnu.org/software/bash/manual/bash.html#index-printf)
  - Imprime texto con formato (más control que `echo`).
* - [read](https://www.gnu.org/software/bash/manual/bash.html#index-read)
  - Lee una línea desde la entrada estándar y la asigna a una o más variables.
* - [readarray](https://www.gnu.org/software/bash/manual/bash.html#index-readarray)
  - Similar a `mapfile`; lee líneas en un array.
* - [source](https://www.gnu.org/software/bash/manual/bash.html#index-source)
  - Ejecuta un script en el contexto actual del shell (igual que `.`).
* - [type](https://www.gnu.org/software/bash/manual/bash.html#index-type)
  - Muestra cómo se resolverá un comando (función, alias, builtin, etc.).
* - [typeset](https://www.gnu.org/software/bash/manual/bash.html#index-typeset)
  - Alias de `declare` en muchas versiones de Bash.
* - [ulimit](https://www.gnu.org/software/bash/manual/bash.html#index-ulimit)
  - Muestra o establece límites de recursos del sistema para el shell actual.
* - [unalias](https://www.gnu.org/software/bash/manual/bash.html#index-unalias)
  - Elimina alias previamente definidos.
```

**Comandos del sistema**

Se conocen como comandos externos o utilidades del sistema. Se encuentran en directorios como `/bin`, `/usr/bin`, etc. _Bash_ (o cualquier _shell_) los ejecuta invocando programas externos.

:::{note}
Los links de la siguiente tabla llevan a la [documentación](https://man7.org/linux/man-pages/dir_all_alphabetic.html) de _man pages_. Alternativamente se puede buscar información sobre estos comandos en las siguientes páginas:
- [tldr](https://tldr.inbrowser.app/): Descripción amigable de comandos para múltiples plataformas.
- [explainshell](https://explainshell.com/): Explicación de comandos línea por línea.
:::

:::{warning}
La siguiente lista solo presenta una pequeña fracción de comandos comunes en sistemas Unix. Para una lista más completa visitar la [documentación](https://man7.org/linux/man-pages/dir_all_alphabetic.html) de _man pages_.
:::

| Comando   | Descripción breve                                                   |
|-----------|---------------------------------------------------------------------|
| [cat](https://man7.org/linux/man-pages/man1/cat.1.html) | Muestra el contenido de un archivo.|
| [chmod](https://man7.org/linux/man-pages/man1/chmod.1p.html) | Cambia los permisos de archivos o directorios.|
| [chown](https://man7.org/linux/man-pages/man1/chown.1.html) | Cambia el propietario o grupo de archivos/directorios.|
| [cp](https://man7.org/linux/man-pages/man1/cp.1.html) | Copia archivos o directorios.|
| [cut](https://man7.org/linux/man-pages/man1/cut.1.html) | Extrae secciones de texto por delimitadores o posiciones.|
| [date](https://man7.org/linux/man-pages/man1/date.1.html) | Muestra o ajusta la fecha y hora del sistema.|
| [df](https://man7.org/linux/man-pages/man1/df.1.html) | Muestra el uso del espacio en disco.|
| [du](https://man7.org/linux/man-pages/man1/du.1.html) | Muestra el uso del espacio por archivos y directorios.|
| [find](https://man7.org/linux/man-pages/man1/find.1.html) | Busca archivos y directorios en una jerarquía.|
| [grep](https://man7.org/linux/man-pages/man1/grep.1.html) | Busca texto dentro de archivos usando expresiones regulares.|
| [head](https://man7.org/linux/man-pages/man1/head.1.html) | Muestra las primeras líneas de un archivo.|
| [kill](https://man7.org/linux/man-pages/man1/kill.1.html) | Envía señales (como finalizar) a procesos.|
| [less](https://man7.org/linux/man-pages/man1/less.1.html) | Muestra contenido de archivos página por página (modo lectura).|
| [ls](https://man7.org/linux/man-pages/man1/ls.1.html) | Lista el contenido de un directorio.|
| [man](https://man7.org/linux/man-pages/man1/man.1p.html) | Muestra el manual de ayuda de comandos.|
| [mkdir](https://man7.org/linux/man-pages/man1/mkdir.1.html) | Crea un nuevo directorio.|
| [more](https://man7.org/linux/man-pages/man1/more.1.html) | Similar a `less`, pero con menos funcionalidades.|
| [mv](https://man7.org/linux/man-pages/man1/git-mv.1.html) | Mueve o renombra archivos o directorios.|
| [paste](https://man7.org/linux/man-pages/man1/paste.1.html) | Fusiona líneas de archivos.|
| [ping](https://man7.org/linux/man-pages/man8/ping.8.html) | Envía paquetes ICMP a una dirección para probar conectividad.|
| [ps](https://man7.org/linux/man-pages/man1/ps.1.html) | Muestra información de procesos en ejecución.|
| [rm](https://man7.org/linux/man-pages/man1/rm.1.html) | Elimina archivos o directorios.|
| [rmdir](https://man7.org/linux/man-pages/man1/rmdir.1.html) | Elimina directorios vacíos.|
| [tail](https://man7.org/linux/man-pages/man1/tail.1.html) | Muestra las últimas líneas de un archivo.|
| [sort](https://man7.org/linux/man-pages/man1/sort.1.html) | Ordena las líneas de un archivo de texto.|
| [top](https://man7.org/linux/man-pages/man1/top.1.html) | Muestra procesos activos en tiempo real.|
| [touch](https://man7.org/linux/man-pages/man1/touch.1.html) | Crea archivos vacíos o actualiza marcas de tiempo.|
| [uname](https://man7.org/linux/man-pages/man1/uname.1.html) | Muestra información del sistema.|
| [uniq](https://man7.org/linux/man-pages/man1/uniq.1.html) | Reporta u omite líneas repetidas.|
| [wc](https://man7.org/linux/man-pages/man1/wc.1.html) | Cuenta líneas, palabras y caracteres en archivos.|
| [whoami](https://man7.org/linux/man-pages/man1/whoami.1.html) | Muestra el nombre del usuario actual.|

<br/>

### Ayuda

#### _man_

[man](https://man7.org/linux/man-pages/man1/man.1p.html) - (Comando del sistema): Muestra el manual de ayuda de comandos.

:::{note}
Llama automáticamente a `less` de manera que se tuebe que usar espacio para pasar a la siguiente página y <kbd>q</kbd> para salir. 
:::

:::{warning}
No se explican todas las opciones. Para más información ir a la documentación de _man pages_ siguiendo el link o usar `man man`.
:::

```sh
# Sintaxis de llamada (tiene múltiples sintaxis de llamadas)
 man [-adho] [-t | -w] [-M manpath] [-P pager] [-S mansect]
     [-m arch[:machine]] [-p [eprtv]] [mansect] page ...

 man -f [-d] [-M manpath] [-P pager] [-S mansect] keyword ...
 whatis [-d] [-s mansect] keyword ...

 man -k [-d] [-M manpath] [-P pager] [-S mansect] keyword ...
 apropos [-d] [-s mansect] keyword ...
```
**Argumentos**:
- _page ..._: Muestra la página de manual del comando dado.
- _mansect_: Muestra la página del comando en una sección (número) específica del manual.
- _keyword ..._: Muestra la página de manual del comando dado.
**Opciones**:
- `-k <keyword>`: Busca en las descripciones cortas de todas las páginas de manual.
- `-f <keyword>`: Muestra una lista de páginas de manual disponibles para el comando dado (sinopsis).
- `-a <page>`: Muestra todas las páginas de manual que coincidan con el comando, una tras otra.
- `-M <manpath>`: Usa una ruta personalizada para buscar las páginas de manual.
- `-w <page>`: Muestra la ruta del archivo de manual sin abrirlo.
- `-P <pager>`: Usa un programa diferente para mostrar la página (por ejemplo, `-P cat`).

**Patrones útiles**:

A continuación se presentan algunos casos de uso comunes.

```sh
# Ver la página de manual del comando `command`
man command

# Buscar en todas las páginas de manual el término "pattern"
man -k pattern

# Mostrar la página de manual de una sección específica (por ejemplo, la sección 2 de `command`)
man 2 command

# Buscar páginas de manual que coincidan con un patrón (similar a buscar en títulos)
man -f pattern

# Ver el manual usando un localizador alternativo de páginas
man -M /ruta/a/manpages pattern

# Mostrar la página de ayuda de man
man man
```

### Archivos y directorios

#### _cd - Change Directory_

[cd](https://www.gnu.org/software/bash/manual/bash.html#index-cd) - (_Shell Builtin_): Cambia el directorio actual.

```sh
# Sintaxis de llamada
cd [-L|[-P [-e]] [-@] [directory]
```
**Argumentos**:
- `[directory]`: La ruta al directorio al que se desea cambiar. Puede ser absoluta (`/home/user`) o relativa (`../otro_directorio`). Por defailt es la variable `$HOME`.
**Opciones**:
- `-L`: Sigue enlaces simbólicos al cambiar de directorio. Es el comportamiento por defecto.
- `-P`: No sigue enlaces simbólicos; navega al directorio físico real en el sistema de archivos.
- `-e`: Usado junto con `-P`, causa que `cd` devuelva un error si el directorio físico no existe.
- `-@`: Muestra atributos extendidos del directorio si el sistema de archivos los admite.

**Patrones útiles**:

A continuación se presentan algunos casos de uso comunes.

```sh
# Ir al directorio home del usuario actual
cd

# Ir a un directorio específico
cd /ruta/al/directorio

# Ir al directorio anterior
cd -

# Ir al directorio padre (subir un nivel)
cd ..

# Usar una ruta relativa para navegar a un subdirectorio
cd carpeta/subcarpeta

# Ir al home de otro usuario (si se tiene permiso)
cd ~usuario

# Seguir enlaces simbólicos al cambiar de directorio (comportamiento por defecto)
cd -L /ruta/simbolica

# No seguir enlaces simbólicos (ir al directorio físico real)
cd -P /ruta/simbolica

# Usar -e con -P para devolver un error si el directorio físico no existe
cd -Pe /ruta/simbolica

# Mostrar atributos extendidos del directorio si está habilitado
cd -@ /ruta

```

#### _cp - Copy_

[cp](https://man7.org/linux/man-pages/man1/cp.1.html) - (Comando del sistema): Copia archivos o directorios.

:::{warning}
No se explican todas las opciones. Para más información ir a la documentación de _man pages_ siguiendo el link o usar `man cp`.
:::

```sh
# Sintaxis de llamada (tiene múltiples sintaxis de llamadas)
cp [-R [-H | -L | -P]] [-fi | -n] [-alpSsvXx] source_file target_file

cp [-R [-H | -L | -P]] [-fi | -n] [-alpSsvXx]
    source_file ... target_directory
    
cp [-f | -i | -n] [-alPpSsvx] source_file target_file

cp [-f | -i | -n] [-alPpSsvx] source_file ... target_directory
```
**Argumentos**
- _source_file ..._: Ruta, nombre y extensión de uno o más archivo de origen. Puede ser una ruta absoluta o relativa.
- _target_file_: Ruta, nombre y extensión del archivo destino. Ver opciones y patrones útiles para el manejo de la sobreescritura.
- _target_directory_: El directorio donde se colocarán los archivos copiados.. Puede ser una ruta absoluta o relativa.
**Opciones**:
- `-R`: Copia directorios de forma recursiva.
- `-H`: Con `-R`, sigue solo los enlaces simbólicos del nivel superior.
- `-L`: Con `-R`, sigue todos los enlaces simbólicos encontrados (deep follow).
- `-P`: Con `-R`, no sigue enlaces simbólicos (comportamiento por defecto).
- `-f`: Fuerza la sobrescritura de archivos de destino sin preguntar.
- `-i`: Pregunta antes de sobrescribir archivos existentes.
- `-n`: No sobrescribe archivos de destino existentes.
- `-a`: Equivalente a `-R -p -P`; copia recursiva conservando enlaces, atributos y sin seguir symlinks.
- `-l`: Crea enlaces duros en lugar de copiar (si es posible).
- `-p`: Conserva los atributos del archivo original (permisos, timestamps, etc.).
- `-S`: Hace copias seguras usando archivos temporales.
- `-s`: Crea enlaces simbólicos en lugar de copiar los archivos.
- `-v`: Muestra el nombre de cada archivo a medida que se copia.
- `-X`: No copia archivos con atributos extendidos.
- `-x`: No cruza sistemas de archivos.
- `source_file`: El archivo o archivos a copiar.
- `target_file`: El nombre del archivo destino.
- `target_directory`: El directorio donde se colocarán los archivos copiados.

**Patrones útiles**:

A continuación se presentan algunos casos de uso comunes.

```sh
# Copiar un archivo a otro con un nuevo nombre
cp archivo.txt copia.txt

# Copiar un archivo a un directorio
cp archivo.txt /ruta/destino/

# Copiar varios archivos a un directorio
cp archivo1.txt archivo2.txt /ruta/destino/

# Copiar un directorio recursivamente (incluyendo su contenido)
cp -R carpeta_origen carpeta_destino

# Copiar un directorio y seguir los enlaces simbólicos (como si fueran archivos/directorios reales)
cp -RL carpeta_origen carpeta_destino

# Copiar un directorio y no seguir enlaces simbólicos
cp -RP carpeta_origen carpeta_destino

# Forzar la sobrescritura sin preguntar
cp -f archivo.txt /ruta/destino/

# Preguntar antes de sobrescribir un archivo existente
cp -i archivo.txt /ruta/destino/

# No sobrescribir archivos existentes
cp -n archivo.txt /ruta/destino/

# Mostrar el progreso mientras copia
cp -v archivo.txt /ruta/destino/

# Copiar conservando atributos como permisos, timestamps, etc.
cp -p archivo.txt /ruta/destino/
```

#### _ls - List_

[ls](https://man7.org/linux/man-pages/man1/ls.1.html) - (Comando del sistema): Lista el contenido de un directorio.

:::{warning}
No se explican todas las opciones. Para más información ir a la documentación de _man pages_ siguiendo el link o usar `man ls`.
:::

```sh
# Sintaxis de llamada
ls [-@ABCFGHILOPRSTUWabcdefghiklmnopqrstuvwxy1%,] [--color=when]
        [-D format] [file ...]
```
**Argumentos**
- _file ..._: Ruta a uno o más directorios para listar el contenido del mismo. En caso de que sea un archivo solo imprimirá el nombre y extensión del mismo.
**Opciones**:
- `-a, --all`: Muestra todos los archivos, incluidos los ocultos (que comienzan con `.`).
- `-l`: Usa un formato largo que muestra permisos, propietarios, tamaño y fecha.
- `-h, --human-readable`: Muestra tamaños en formato legible (KB, MB, GB). Se usa junto con `-l`.
- `-R, --recursive`: Lista archivos en subdirectorios de manera recursiva.
- `-S`: Ordena los archivos por tamaño, de mayor a menor.
- `-F`: Agrega un `/` al final del nombre de cada carpeta y un `*` al final del nombre de cada programa ejecutable. 
- `-t`: Ordena por fecha de modificación, del más reciente al más antiguo.
- `-r, --reverse`: Invierte el orden de la lista (por ejemplo, con `-t` muestra los más antiguos primero).
- `-d`: Muestra los nombres de los directorios sin listar su contenido (útil con `*/`).
- `-1`: Muestra un archivo por línea (útil para scripts o conteos).
- `--color`: Colorea la salida según el tipo de archivo (por defecto en muchas distros).

**Patrones útiles**:

A continuación se presentan algunos casos de uso comunes.

```sh
# Listar archivos en el directorio actual
ls

# Listar archivos incluyendo los ocultos (que comienzan con .)
ls -a

# Listar archivos con detalles (permisos, propietario, tamaño, fecha)
ls -l

# Listar archivos con detalles, incluyendo archivos ocultos
ls -la

# Ordenar archivos por fecha de modificación (más reciente al final)
ls -lt

# Ordenar archivos por tamaño (más grandes al principio)
ls -lS

# Mostrar el tamaño de los archivos en formato legible (KB, MB...)
ls -lh

# Listar archivos en todos los subdirectorios de forma recursiva
ls -R

# Listar solo los directorios
ls -d */

# Listar archivos, pero mostrando solo los nombres (sin colores, sin formatos)
ls -1
```

#### _mkdir - Make Directory_

[mkdir](https://man7.org/linux/man-pages/man1/mkdir.1.html) - (Comando del sistema): Crea un nuevo directorio.

```sh
# Sintaxis de llamada
mkdir [-pv] [-m mode] directory_name ...
```
**Argumentos**
- _directory_name_: Nombre de el o los directorios que se van a crear.
**Opciones**:
- `-m mode`: Establece los _bits_ de permiso del archivo del directorio final creado en el modo especificado.
- `-p`: Crea directorios intermedios según sea necesario.
- `-v`: Enumera los directorios a medida que se crean.

**Patrones útiles**:

A continuación se presentan algunos casos de uso comunes.

```sh
# Crear un directorio
mkdir directorio

# Crear un directorio en el modo especificado
mkdir -m 700 directorio

# Crear los directorios indicados (incluyendo foo y bar)
mkdir -p foo/bar/baz
```

#### _mv - Move_

[mv](https://man7.org/linux/man-pages/man1/git-mv.1.html) - (Comando del sistema): Mueve o renombra archivos o directorios.

:::{warning}
No se explican todas las opciones. Para más información ir a la documentación de _man pages_ siguiendo el link o usar `man mv`.
:::

```sh
# Sintaxis de llamada (tiene múltiples sintaxis de llamadas)
mv [-f | -i | -n] [-hv] source target

mv [-f | -i | -n] [-v] source ... directory
```
**Argumentos**
- _source ..._: Archivo o archivos de origen que deseas mover o renombrar, se debe indicar la entensión.
- _target_: Nuevo nombre o ruta de destino para un solo archivo, se debe indicar la extensión. Si ya existe el archivo lo va a reemplazar.
- _directory_: Directorio donde se desea mover múltiples archivos.
**Opciones**:
- `-f`: Fuerza el movimiento sin pedir confirmación, incluso si sobrescribe archivos existentes.
- `-i`: Solicita confirmación antes de sobrescribir archivos existentes.
- `-n`: No sobrescribe archivos existentes en el destino.
- `-v`: Muestra el nombre de cada archivo a medida que se mueve.

**Patrones útiles**:

A continuación se presentan algunos casos de uso comunes.

```sh
# Renombrar un archivo
mv viejo_nombre.txt nuevo_nombre.txt

# Mover un archivo a otro directorio
mv archivo.txt /ruta/destino/

# Mover varios archivos a un directorio
mv archivo1.txt archivo2.txt /ruta/destino/

# Sobrescribir archivos de destino sin pedir confirmación
mv -f archivo.txt /ruta/destino/

# Pedir confirmación antes de sobrescribir
mv -i archivo.txt /ruta/destino/

# No sobrescribir si el archivo ya existe
mv -n archivo.txt /ruta/destino/

# Mostrar el progreso mientras se mueven archivos
mv -v archivo.txt /ruta/destino/
```

#### _paste - Merge_

[paste](https://man7.org/linux/man-pages/man1/paste.1.html) - (Comando del sistema): Fusiona líneas de archivos horizontalmente, para que el _output_ sea correcto ambos archivos deben de tener el mismo número de filas.

```sh
# Sintaxis de llamada
paste [-s] [-d list] file ...
```
**Argumentos**
- _file ..._: Uno o más archivos que se fusionarán.
**Opciones**:
- `-d list`: Usa uno o más de los caracteres proporcionados para reemplazar los caracteres _newline_ en lugar de _tab_ (default). Usar `$'\t'`para tabulaciones, `$'\n'` para saltos de líneas, `$'\\'` para barras invertidas.
- `-s`: Concatena todas las líneas de cada archivo de entrada separado en el orden de línea de comando.

**Patrones útiles**:

A continuación se presentan algunos casos de uso comunes.

```sh
#!/bin/bash

# Combinar dos archivos línea por línea (columnas separadas por tabulador)
paste archivo1.txt archivo2.txt

# Combinar archivos con delimitador específico (ej. coma)
paste -d ',' archivo1.txt archivo2.txt

# Combinar líneas de un solo archivo en una sola línea
paste -s archivo.txt

# Combinar líneas con delimitador personalizado y serializar
paste -s -d ':' archivo.txt  # Usa ':' como separador

# Combinar datos en columnas desde la entrada estándar
ls | paste - -  # Muestra el listado en 2 columnas

# Combinar en 3 columnas con delimitador personalizado
ls | paste -d '|' - - -  # Tres columnas separadas por |

# Pegar datos de múltiples archivos con numeración de líneas
paste -n archivo1.txt archivo2.txt  # Muestra número de línea al inicio

# Combinar archivos con separación por tabulador y mostrar en pantalla
paste -t $'\t' archivo1.txt archivo2.txt  # Fuerza separación por tab

# Pegar datos ignorando líneas en blanco
paste -d ',' -s --delimiters archivo.txt  # Útil para CSV

# Combinar con secuencia de delimitadores diferente para cada par de columnas
paste -d ':,.' archivo1.txt archivo2.txt archivo3.txt
# Usa : entre 1y2, , entre 2y3, . entre 3y1

# Pegar datos desde múltiples procesos (process substitution)
paste <(cmd1) <(cmd2)  # Combina salidas de dos comandos

# Crear una tabla CSV simple desde múltiples archivos
paste -d ',' archivo1.txt archivo2.txt > tabla.csv

# Transponer filas a columnas
paste -s archivo.txt | tr '\t' '\n'  # Convierte filas a columna única

# Combinar con delimitador de nueva línea (útil para procesamiento posterior)
paste -d '\n' archivo1.txt archivo2.txt

# Pegar versiones serializadas con numeración
seq 1 5 | paste -d ' ' - - -  # Produce: 1 2 3\n4 5 \n
```

#### _pwd - Path Working Directory_

[pwd](https://www.gnu.org/software/bash/manual/bash.html#index-pwd) - (_Shell Builtin_): Muestra el directorio de trabajo actual.

```sh
# Sintaxis de llamada
pwd [-LP]
```
**Opciones**:
- `-L`: La ruta impresa puede contener enlaces simbólicos.
- `-P`: La ruta impresa no contendrá enlaces simbólicos.

**Patrones útiles**:

A continuación se presentan algunos casos de uso comunes.

```sh
# Mostrar el directorio de trabajo actual
pwd
```

#### _rm - Remove_

[rm](https://man7.org/linux/man-pages/man1/rm.1.html) - (Comando del sistema): Elimina archivos o directorios.

:::{warning}
_Shell_ no tiene un "basurero", el archivo se eliminará completamente.
:::

:::{warning}
No se explican todas las opciones. Para más información ir a la documentación de _man pages_ siguiendo el link o usar `man rm`.
:::

```sh
# Sintaxis de llamada
rm [-f | -i] [-dIRrvWx] file ...
unlink [--] file
```
**Argumentos**
- `file ...`: Uno o más archivos o directorios a eliminar.
**Opciones**:
- `-f`: Forzar la eliminación sin pedir confirmación y sin mostrar errores si el archivo no existe.
- `-i`: Solicita confirmación antes de eliminar cada archivo.
- `-I`: Solicita confirmación una sola vez si se van a eliminar muchos archivos o un directorio.
- `-d`: Elimina directorios vacíos.
- `-r` o `-R`: Elimina directorios y su contenido de forma recursiva.
- `-v`: Muestra información detallada de lo que se está eliminando.
- `-W`: No elimina los archivos, sino que los escribe en el archivo de historial de eliminación (si soportado).
- `-x`: No atraviesa sistemas de archivos montados.

**Patrones útiles**:

A continuación se presentan algunos casos de uso comunes.

```sh
# Eliminar un solo archivo
rm archivo.txt

# Eliminar varios archivos
rm archivo1.txt archivo2.txt

# Eliminar un archivo sin pedir confirmación, incluso si no existe
rm -f archivo.txt

# Pedir confirmación antes de eliminar cada archivo
rm -i archivo1.txt archivo2.txt

# Eliminar un directorio vacío
rm -d directorio_vacio

# Eliminar recursivamente un directorio y su contenido
rm -r directorio_con_archivos

# Eliminar recursivamente y forzadamente (sin confirmación)
rm -rf directorio

# Mostrar los archivos a medida que se eliminan
rm -v archivo1.txt archivo2.txt

# Confirmar de forma interactiva antes de eliminar todo un directorio
rm -I -r directorio
```

#### _rmdir - Remove Directory_

[rmdir](https://man7.org/linux/man-pages/man1/rmdir.1.html) - (Comando del sistema): Elimina directorios vacíos.

```sh
# Sintaxis de llamada
rmdir [-pv] directory ...
```
**Argumentos**
- _directory_: Uno o más directorios vacíos que se van a eliminar.
**Opciones**:
- `-p`: Cada argumento del directorio se trata como un nombre de ruta del cual se eliminarán todos los componentes, si están vacíos, comenzando con el componente más profundo.
- `-v`: Enumera cada directorio a medida que se elimina.

**Patrones útiles**:

A continuación se presentan algunos casos de uso comunes.

```sh
# Eliminar un directorio
rmdir directorio

# Elimina todos los directorios involucrados (incluyendo foo y bar)
rmdir -p foo/bar/baz
```

<br/>

### Exploración de Archivos

#### _cat - Concatenate_

[cat](https://man7.org/linux/man-pages/man1/cat.1.html) - (Comando del sistema): Muestra el contenido de un archivo.

```sh
# Sintaxis de llamada
cat [-belnstuv] [file ...]
```
**Argumentos**
- `file ...`: Uno o más archivos o directorios a utilizar.
**Opciones**:
- `-b`: Numera las líneas no vacías.
- `-e`: Equivalente a `-vE`, muestra caracteres no imprimibles y marca el final de cada línea con `$`.
- `-l`: (No estándar) No tiene un uso común en `cat`.
- `-n`: Numera todas las líneas.
- `-s`: Comprime múltiples líneas en blanco en una sola.
- `-t`: Equivalente a `-vT`, muestra caracteres no imprimibles y tabulaciones como `^I`.
- `-u`: (No estándar) No tiene un uso común en `cat`.
- `-v`: Muestra caracteres no imprimibles, excepto tabulaciones y saltos de línea.

**Patrones útiles**:

A continuación se presentan algunos casos de uso comunes.

```sh
# Mostrar el contenido de un archivo
cat archivo.txt

# Concatenar y mostrar el contenido de varios archivos
cat archivo1.txt archivo2.txt

# Crear un nuevo archivo a partir de la concatenación de varios archivos
cat archivo1.txt archivo2.txt > nuevo_archivo.txt

# Añadir el contenido de un archivo al final de otro archivo
cat archivo1.txt >> archivo2.txt

# Mostrar el contenido de un archivo con números de línea
cat -n archivo.txt

# Mostrar el contenido de un archivo con caracteres no imprimibles visibles
cat -v archivo.txt

# Mostrar el contenido de un archivo con el final de cada línea marcado con un $
cat -e archivo.txt

# Mostrar el contenido de un archivo con tabulaciones visibles como ^I
cat -t archivo.txt

# Mostrar el contenido de un archivo con múltiples espacios en blanco comprimidos en uno solo
cat -s archivo.txt
```

<br/>

#### _cut_

[cut](https://man7.org/linux/man-pages/man1/cut.1.html) - (Comando del sistema): Extrae secciones de texto por delimitadores o posiciones.

```sh
# Sintaxis de llamada (tiene múltiples sintaxis de llamadas)
cut -b list [-n] [file ...]

cut -c list [file ...]

cut -f list [-w | -d delim] [-s] [file ...]

```
**Argumentos**

- _file ..._: Uno o más archivos de entrada.
**Opciones**:
- `-b list`: Selecciona solo los bytes en `list`.
- `-c list`: Selecciona solo los caracteres en `list`.
- `-f list`: Selecciona solo los campos en `list` (número separados por espacios) o rangos de números separados por guión (_n-m_).
- `-d delim`: Usa `delim` como delimitador de campo en lugar de la tabulación.
- `-s`: Suprime las líneas que no contienen el delimitador de campo.
- `-n`: No divide caracteres multibyte (solo con `-b`).

**Patrones útiles**:

A continuación se presentan algunos casos de uso comunes.

```sh
# Cortar los bytes especificados (por ejemplo, los bytes 1-5) de cada línea de un archivo
cut -b 1-5 archivo.txt

# Cortar los caracteres especificados (por ejemplo, los caracteres 1-5) de cada línea de un archivo
cut -c 1-5 archivo.txt

# Cortar los campos especificados (por ejemplo, los campos 1 y 3) de cada línea de un archivo delimitado por tabulaciones
cut -f 1,3 archivo.txt

# Cortar los campos especificados (por ejemplo, los campos 1 y 3) de cada línea de un archivo delimitado por comas
cut -f 1,3 -d ',' archivo.csv

# Cortar los campos especificados (por ejemplo, los campos 1 y 3) de cada línea de un archivo delimitado por comas, sin mostrar líneas que no contienen el delimitador
cut -f 1,3 -d ',' -s archivo.csv

# Cortar los bytes especificados (por ejemplo, los bytes 1-5) de cada línea de un archivo, sin dividir caracteres multibyte
cut -b 1-5 -n archivo.txt
```

<br/>

#### _grep_

[grep](https://man7.org/linux/man-pages/man1/grep.1.html) - (Comando del sistema): Busca texto dentro de archivos usando expresiones regulares. Devuelve las líneas que satisfacen los patrones.

```sh
# Sintaxis de llamada
grep [-abcdDEFGHhIiJLlMmnOopqRSsUVvwXxZz] [-A num] [-B num] [-C num]
      [-e pattern] [-f file] [--binary-files=value] [--color[=when]]
      [--colour[=when]] [--context=num] [--label] [--line-buffered] [--null]
      [pattern] [file ...]
```
**Argumentos**
- `pattern`: El patrón a buscar.
- `file ...`: Uno o más archivos de entrada
**Opciones**:
- `-a`: Trata los archivos binarios como texto.
- `-b`: Muestra la posición de byte de cada coincidencia.
- `-c`: Muestra solo el número de coincidencias por archivo.
- `-d action`: Especifica la acción a tomar con directorios (por ejemplo, `read`, `recurse`).
- `-E`: Usa expresiones regulares extendidas.
- `-F`: Usa patrones fijos (sin expresiones regulares).
- `-G`: Usa expresiones regulares básicas.
- `-H`: Muestra el nombre del archivo para cada coincidencia.
- `-h`: No muestra el nombre del archivo para cada coincidencia.
- `-i`: Ignora mayúsculas y minúsculas.
- `-L`: Muestra los archivos que no contienen coincidencias.
- `-l`: Muestra solo los nombres de los archivos con coincidencias.
- `-m num`: Detiene la búsqueda después de `num` coincidencias.
- `-n`: Muestra el número de línea de cada coincidencia.
- `-o`: Muestra solo la parte de la línea que coincide.
- `-q`: No muestra salida, solo devuelve el código de estado.
- `-R`, `-r`: Busca recursivamente en directorios.
- `-s`: Suprime los mensajes de error sobre archivos inexistentes o ilegibles.
- `-v`: Muestra las líneas que no coinciden con el patrón.
- `-w`: Coincide solo palabras completas.
- `-x`: Coincide solo líneas completas.
- `-Z`, `-z`: Trata la entrada como datos terminados en NUL.
- `-A num`: Muestra `num` líneas después de cada coincidencia.
- `-B num`: Muestra `num` líneas antes de cada coincidencia.
- `-C num`: Muestra `num` líneas antes y después de cada coincidencia.
- `-e pattern`: Especifica el patrón a buscar.
- `-f file`: Toma los patrones del archivo especificado.
- `--binary-files=value`: Controla cómo se tratan los archivos binarios (`binary`, `text`, `without-match`).
- `--color[=when]`, `--colour[=when]`: Resalta las coincidencias en color (`auto`, `always`, `never`).
- `--context=num`: Muestra `num` líneas antes y después de cada coincidencia.
- `--label`: Usa la etiqueta especificada en lugar del nombre del archivo.
- `--line-buffered`: Usa el buffer de línea.
- `--null`: Termina cada nombre de archivo con NUL.

**Patrones útiles**:

A continuación se presentan algunos casos de uso comunes.

```sh
# Buscar un patrón en un archivo
grep "patrón" archivo.txt

# Buscar un patrón en varios archivos
grep "patrón" archivo1.txt archivo2.txt

# Buscar un patrón de forma recursiva en un directorio
grep -r "patrón" directorio/

# Buscar un patrón ignorando mayúsculas y minúsculas
grep -i "patrón" archivo.txt

# Mostrar las líneas que no coinciden con el patrón
grep -v "patrón" archivo.txt

# Mostrar el número de línea donde se encuentra el patrón
grep -n "patrón" archivo.txt

# Mostrar el contexto de 3 líneas alrededor de cada coincidencia
grep -C 3 "patrón" archivo.txt

# Buscar un patrón y mostrar solo el número de coincidencias
grep -c "patrón" archivo.txt

# Buscar múltiples patrones especificados en un archivo
grep -f patrones.txt archivo.txt

# Buscar un patrón y resaltar las coincidencias en color
grep --color=auto "patrón" archivo.txt
```

<br/>

#### _head_

[head](https://man7.org/linux/man-pages/man1/head.1.html) - (Comando del sistema): Muestra las primeras líneas de un archivo.

```sh
# Sintaxis de llamada
head [-n count | -c bytes] [file ...]
```
**Argumentos**
- `file ...`: Uno o más archivos de entrada.
**Opciones**:
- `-n count`: Muestra las primeras `count` líneas de cada archivo.
- `-c bytes`: Muestra los primeros `bytes` bytes de cada archivo.

**Patrones útiles**:

A continuación se presentan algunos casos de uso comunes.

```sh
# Mostrar las primeras 10 líneas de un archivo (por defecto)
head archivo.txt

# Mostrar las primeras 5 líneas de un archivo
head -n 5 archivo.txt

# Mostrar las primeras 20 líneas de varios archivos
head -n 20 archivo1.txt archivo2.txt

# Mostrar los primeros 100 bytes de un archivo
head -c 100 archivo.txt

# Mostrar los primeros 50 bytes de varios archivos
head -c 50 archivo1.txt archivo2.txt
```

<br/>

#### _less_

[less](https://man7.org/linux/man-pages/man1/less.1.html) - (Comando del sistema): Muestra contenido de archivos página por página (modo lectura).

:::{note}
Usar  espacio para pasar a la siguiente página. Usar los suiguientes _shortcuts_ para navegar por los archivos:
- <kbd>q</kbd> para salir.
- <kbd>p</kbd> para el archivo previo (en caso de abrir múltiples archivos).
- <kbd>n</kbd> para el siguiente archivo (en caso de abrir múltiples archivos).
:::

```sh
# Sintaxis de llamada
less -?
less --help
less -V
less --version

less [-[+]aABcCdeEfFgGiIJKLmMnNqQrRsSuUVwWX~]
      [-b space] [-h lines] [-j line] [-k keyfile]
      [-{oO} logfile] [-p pattern] [-P prompt] [-t tag]
      [-T tagsfile] [-x tab,...] [-y lines] [-[z] lines]
      [-# shift] [+[+]cmd] [--] [filename]...
```
**Argumentos**
- _filename_: Uno o más archivos de entrada.
**Opciones**:
- `-g`: Resalta solo la última coincidencia de búsqueda.
- `-i`: Ignora mayúsculas y minúsculas en las búsquedas.
- `-j line`: Posiciona la línea `line` en la parte superior de la pantalla.
- `-m`: Muestra un mensaje de porcentaje en lugar de la línea de estado.
- `-N`: Muestra los números de línea.
- `-p pattern`: Busca el `pattern` al iniciar.
- `-q`: No usa la campana.
- `-s`: Comprime múltiples líneas en blanco.
- `-u`: No muestra subrayados.
- `-x tab,...`: Define las posiciones de tabulación.
- `-y lines`: Define el número de líneas de desplazamiento.
- `-z lines`: Define el número de líneas de pantalla.
- `--`: Finaliza las opciones.

**Patrones útiles**:

A continuación se presentan algunos casos de uso comunes.

```sh
# Mostrar el contenido de un archivo
less archivo.txt

# Navegar por el contenido de varios archivos
less archivo1.txt archivo2.txt

# Buscar un patrón dentro del archivo
less archivo.txt
/patrón

# Mostrar el contenido de un archivo y resaltar las coincidencias de un patrón
less -p "patrón" archivo.txt

# Mostrar el contenido de un archivo con un número específico de líneas de historial
less -b 100 archivo.txt

# Mostrar el contenido de un archivo con un número específico de líneas de pantalla
less -z 20 archivo.txt

# Mostrar el contenido de un archivo y comenzar en una línea específica
less +10 archivo.txt
```

<br/>

#### _sort_

[sort](https://man7.org/linux/man-pages/man1/sort.1.html) - (Comando del sistema): Ordena las líneas de un archivo de texto.

```sh
# Sintaxis de llamada
sort [-bcCdfghiRMmnrsuVz] [-k field1[,field2]] [-S memsize] [-T dir] [-t
      	char] [-o output] [file ...]

sort --help
sort --version

```
**Argumentos**
- `file ...`: Uno o más archivos de entrada
**Opciones**:
- `-b`: Ignora los espacios en blanco iniciales.
- `-c`: Verifica si el archivo ya está ordenado.
- `-C`: Verifica si el archivo ya está ordenado y muestra un mensaje.
- `-d`: Usa el orden de diccionario (solo letras, dígitos y espacios).
- `-f`: Ignora las diferencias entre mayúsculas y minúsculas.
- `-g`: Usa la comparación numérica general.
- `-h`: Ordena por tamaño humano (por ejemplo, 2K, 1G).
- `-i`: Ignora caracteres no imprimibles.
- `-M`: Ordena por mes.
- `-n`: Usa la comparación numérica.
- `-r`: Ordena en orden inverso (descendente).
- `-s`: Estabiliza el orden (no mezcla líneas con claves iguales).
- `-u`: Elimina líneas duplicadas.
- `-V`: Ordena por versión (por ejemplo, `file-1`, `file-2`).
- `-z`: Usa NUL como delimitador de línea.
- `-k field1[,field2]`: Ordena por la clave de campo especificada.
- `-S memsize`: Usa `memsize` de memoria para la ordenación.
- `-T dir`: Usa `dir` para archivos temporales.
- `-t char`: Usa `char` como delimitador de campo.
- `-o output`: Especifica el archivo de salida.

**Patrones útiles**:

A continuación se presentan algunos casos de uso comunes.

```sh
# Ordenar un archivo alfabéticamente
sort archivo.txt

# Ordenar un archivo numéricamente
sort -n archivo.txt

# Ordenar un archivo en orden inverso
sort -r archivo.txt

# Ordenar un archivo y eliminar líneas duplicadas
sort -u archivo.txt

# Ordenar un archivo por una columna específica (por ejemplo, la segunda columna)
sort -k 2 archivo.txt

# Ordenar un archivo delimitado por comas por una columna específica (por ejemplo, la tercera columna)
sort -t ',' -k 3 archivo.csv

# Ordenar un archivo y guardar el resultado en un archivo de salida
sort -o salida.txt archivo.txt

# Ordenar varios archivos y mostrar el resultado combinado
sort archivo1.txt archivo2.txt
```

<br/>

#### _tail_

[tail](https://man7.org/linux/man-pages/man1/tail.1.html) - (Comando del sistema): Muestra las últimas líneas de un archivo.

```sh
# Sintaxis de llamada
tail [-F | -f | -r] [-qv] [-b number | -c number | -n number] [file ...]
```
**Argumentos**
- `file ...`: Uno o más archivos de entrada
**Opciones**:
- `-F`: Sigue el archivo y reinicia si se reemplaza.
- `-f`: Sigue el crecimiento del archivo en tiempo real.
- `-r`: Muestra las líneas en orden inverso.
- `-q`: No muestra el nombre del archivo.
- `-v`: Muestra el nombre del archivo.
- `-b number`: Muestra los últimos `number` bloques de 512 bytes.
- `-c number`: Muestra los últimos `number` bytes.
- `-n number`: Muestra las últimas `number` líneas. Si se agrega un `+` antes del número filas entonces es para indicar que se muestren todas las filas excepto las primeras `number` filas. 

**Patrones útiles**:

A continuación se presentan algunos casos de uso comunes.

```sh
# Mostrar las últimas 10 líneas de un archivo (por defecto)
tail archivo.txt

# Mostrar las últimas 20 líneas de un archivo
tail -n 20 archivo.txt

# Mostrar los últimos 100 bytes de un archivo
tail -c 100 archivo.txt

# Mostrar las últimas 50 líneas de varios archivos
tail -n 50 archivo1.txt archivo2.txt

# Seguir el crecimiento de un archivo en tiempo real
tail -f archivo.txt

# Seguir el crecimiento de un archivo en tiempo real y reiniciar si el archivo se reemplaza
tail -F archivo.txt

# Mostrar las últimas 10 líneas de un archivo en orden inverso
tail -r archivo.txt

# Mostrar las últimas 20 bloques de 512 bytes de un archivo
tail -b 20 archivo.txt

# Mostrar las últimas 10 líneas de un archivo sin mostrar el nombre del archivo
tail -q archivo.txt
```

<br/>

#### _uniq_

[uniq](https://man7.org/linux/man-pages/man1/uniq.1.html) - (Comando del sistema): Reporta u omite líneas repetidas consecutivas.

```sh
# Sintaxis de llamada
uniq [-c | -d | -D | -u] [-i] [-f num] [-s chars] [input_file [output_file]]
```
**Argumentos**
- `input_file`: Archivo de entrada.
- `output_file`: Archivo de salida (opcional).
**Opciones**:
- `-c`: Muestra el número de veces que cada línea se repite.
- `-d`: Muestra solo las líneas duplicadas.
- `-D`: Muestra todas las líneas duplicadas y sus repeticiones.
- `-u`: Muestra solo las líneas únicas.
- `-i`: Ignora diferencias entre mayúsculas y minúsculas.
- `-f num`: Ignora los primeros `num` campos al comparar líneas.
- `-s chars`: Ignora los primeros `chars` caracteres al comparar líneas.

**Patrones útiles**:

A continuación se presentan algunos casos de uso comunes.

```sh
# Eliminar líneas duplicadas consecutivas de un archivo
uniq archivo.txt

# Mostrar el número de veces que cada línea se repite
uniq -c archivo.txt

# Mostrar solo las líneas duplicadas
uniq -d archivo.txt

# Mostrar todas las líneas duplicadas y sus repeticiones
uniq -D archivo.txt

# Mostrar solo las líneas únicas
uniq -u archivo.txt

# Ignorar diferencias entre mayúsculas y minúsculas
uniq -i archivo.txt

# Ignorar los primeros 2 campos al comparar líneas
uniq -f 2 archivo.txt

# Ignorar los primeros 3 caracteres al comparar líneas
uniq -s 3 archivo.txt

# Eliminar líneas duplicadas consecutivas y guardar el resultado en un archivo de salida
uniq archivo.txt salida.txt

```

<br/>

#### _wc_

[wc](https://man7.org/linux/man-pages/man1/wc.1.html) - (Comando del sistema): Cuenta líneas, palabras y caracteres en archivos.

```sh
# Sintaxis de llamada
wc [--libxo] [-Lclmw] [file ...]
```
**Argumentos**
- `file ...`: Uno o más archivos de entrada.
**Opciones**:
- `-L`: Muestra la longitud de la línea más larga.
- `-c`: Muestra el número de bytes.
- `-l`: Muestra el número de líneas.
- `-m`: Muestra el número de caracteres.
- `-w`: Muestra el número de palabras.
- `--libxo`: Produce la salida en formato libxo

**Patrones útiles**:

A continuación se presentan algunos casos de uso comunes.

```sh
# Contar las líneas, palabras y caracteres de un archivo
wc archivo.txt

# Contar solo las líneas de un archivo
wc -l archivo.txt

# Contar solo las palabras de un archivo
wc -w archivo.txt

# Contar solo los caracteres de un archivo
wc -m archivo.txt

# Contar solo la longitud de la línea más larga de un archivo
wc -L archivo.txt

# Contar las líneas, palabras y caracteres de varios archivos
wc archivo1.txt archivo2.txt

# Contar las líneas, palabras y caracteres de un archivo y mostrar el total
wc archivo.txt archivo2.txt
```

<br/>

### Historial

[history](https://www.gnu.org/software/bash/manual/bash.html#index-history) - (Bash History Builtins): Muestra el historial con los números de línea. Las líneas marcadas con un asterisco (*) han sido modificadas.

:::{tip}
Al mostrar el historial se mostrará un número de serie tal que si se usa `!num_serie` entonces se rejecutará ese comando.
:::

```sh
# Sintaxis de llamada
history [-c] [-d offset] [n]

history -awrn [filename]

history -ps arg [arg...]
```
**Argumentos**
- `filename`: Archivo de historial (opcional).
**Opciones**:
- `-c`: Borra todo el historial de comandos.
- `-d offset`: Elimina el comando en la posición `offset` del historial.
- `n`: Muestra los últimos `n` comandos del historial.
- `-a`: Añade el historial de comandos actual al archivo de historial.
- `-w`: Guarda el historial de comandos en un archivo.
- `-r`: Lee el historial de comandos desde un archivo.
- `-n`: Reemplaza el historial actual con el contenido del archivo de historial.
- `-p`: Ejecuta un comando sin guardarlo en el historial.
- `-s arg`: Guarda `arg` en el historial como si fuera un comando.

**Patrones útiles**:

A continuación se presentan algunos casos de uso comunes.

```sh
# Mostrar el historial de comandos
history

# Mostrar los últimos 10 comandos del historial
history 10

# Borrar todo el historial de comandos
history -c

# Eliminar un comando específico del historial (por ejemplo, el comando en la posición 5)
history -d 5

# Guardar el historial de comandos en un archivo
history -w historial.txt

# Leer el historial de comandos desde un archivo
history -r historial.txt

# Añadir el historial de comandos actual al archivo de historial
history -a

# Reemplazar el historial actual con el contenido del archivo de historial
history -n

# Ejecutar un comando sin guardarlo en el historial
history -s "comando"
```

<br/>

### Ingeso y salida de datos

#### _echo_

[echo](https://www.gnu.org/software/bash/manual/bash.html#index-echo) - (Comando del sistema): Imprime texto en la salida estándar.

```sh
# Sintaxis de llamada
echo [-neE] [arg …]
```
**Argumentos**
- `arg ...`: Uno o más argumentos a imprimir.
**Opciones**:
- `-n`: No imprime el salto de línea al final.
- `-e`: Habilita la interpretación de secuencias de escape.
- `-E`: Deshabilita la interpretación de secuencias de escape (por defecto).

**Patrones útiles**:

A continuación se presentan algunos casos de uso comunes.

```sh
# Imprimir un mensaje en la terminal
echo "Hola, mundo"

# Imprimir un mensaje sin el salto de línea al final
echo -n "Hola, mundo"

# Imprimir un mensaje con secuencias de escape interpretadas
echo -e "Hola,\nmundo"

# Imprimir un mensaje sin interpretar secuencias de escape (por defecto)
echo -E "Hola,\nmundo"

# Imprimir el valor de una variable
mi_variable="Hola, mundo"
echo $mi_variable

# Imprimir el resultado de un comando
echo "La fecha y hora actual es: $(date)"
```

<br/>

#### _read_

[read](https://www.gnu.org/software/bash/manual/bash.html#index-read) - (Comando del sistema): Lee una línea desde la entrada estándar y la asigna a una o más variables.

```sh
# Sintaxis de llamada
read [-ers] [-u fd] [-t timeout] [-p prompt] [-a array] [-n nchars] [-d delim] [name ...]
```
**Argumentos**
- `name ...`: Uno o más nombres de variables para almacenar la entrada.
**Opciones**:
- `-e`: Habilita la edición de línea.
- `-r`: No permite caracteres de escape.
- `-s`: Oculta la entrada (útil para contraseñas).
- `-u fd`: Lee desde el descriptor de archivo `fd`.
- `-t timeout`: Establece un tiempo de espera para la entrada.
- `-p prompt`: Muestra un mensaje de aviso.
- `-a array`: Almacena las palabras leídas en un array.
- `-n nchars`: Lee `nchars` caracteres.
- `-d delim`: Usa `delim` como delimitador de entrada.

**Patrones útiles**:

A continuación se presentan algunos casos de uso comunes.

```sh
# Leer una línea de entrada y almacenarla en una variable
read nombre
echo "Hola, $nombre"

# Leer una línea de entrada con un mensaje de aviso
read -p "Introduce tu nombre: " nombre
echo "Hola, $nombre"

# Leer una línea de entrada con un límite de tiempo de 5 segundos
read -t 5 -p "Introduce tu nombre (tienes 5 segundos): " nombre
echo "Hola, $nombre"

# Leer una línea de entrada y almacenarla en un array
read -a nombres
echo "Hola, ${nombres[0]} y ${nombres[1]}"

# Leer una línea de entrada sin permitir caracteres de escape
read -r nombre
echo "Hola, $nombre"

# Leer una línea de entrada desde un descriptor de archivo específico
exec 3< archivo.txt
read -u 3 linea
echo "La línea leída es: $linea"
exec 3<&-

# Leer una cantidad específica de caracteres
read -n 5 -p "Introduce 5 caracteres: " entrada
echo "Has introducido: $entrada"

# Leer una línea de entrada hasta un delimitador específico
read -d ':' -p "Introduce una cadena terminada en ':': " cadena
echo "La cadena introducida es: $cadena"
```

<br/>

### Otros

Otros comandos.

:::{warning}
Estos comandos no forman parte del sistema ni _bash_, son necesarios instalarlos. Consultar cada comando para más información.
:::

#### _curl_

[curl](https://curl.se/docs/manpage.html): Principalmente utilizado para transferir datos desde o hacia un servidor, usando varios protocolos (HTTP, HTTPS, FTP, etc.). Es muy versátil para realizar peticiones web.  

:::{tip}
Para verificar que se tiene instalado `curl` usar: `curl --version`
:::

```sh
# Sintaxis de llamada
curl [options / URLs]
```
**Argumentos**
- `URL`: La URL o URLs a las que se hace la solicitud. Puede llevar _wildcards_, en caso de que existan muchas direcciones similares, servirá para acceder a todos esos archivos en esas direcciones. 
**Opciones**:
- `-o file.ext`: Guarda la salida en `file.ext`.
- `-O`: Guarda la salida en un archivo con el mismo nombre que en la URL.
- `-L`: Sigue redirecciones.
- `-d data`: Envía datos en una solicitud POST.
- `-X method`: Especifica el método HTTP a usar (por ejemplo, `POST`, `GET`).
- `-H header`: Añade un encabezado a la solicitud.
- `-u user:password`: Usa autenticación básica con `user` y `password`.
- `-I`: Muestra solo los encabezados de la respuesta.
- `-A agent`: Especifica un agente de usuario personalizado.

**Patrones útiles**:

A continuación se presentan algunos casos de uso comunes.

```sh
# Descargar el contenido de una URL y mostrarlo en la terminal
curl http://example.com

# Descargar el contenido de una URL y guardarlo en un archivo
curl -o archivo.html http://example.com

# Descargar el contenido de una URL y guardarlo en un archivo con el mismo nombre que en la URL
curl -O http://example.com/archivo.html

# Descargar varios archivos con URLs similares
curl -O http://example.com/archivo1.html -O http://example.com/archivo2.html

# Seguir redirecciones
curl -L http://example.com

# Enviar datos en una solicitud POST
curl -d "param1=valor1&param2=valor2" -X POST http://example.com/formulario

# Enviar datos en una solicitud POST desde un archivo
curl -d @datos.json -H "Content-Type: application/json" -X POST http://example.com/api

# Descargar un archivo con autenticación básica
curl -u usuario:contraseña -O http://example.com/archivo_protegido.html

# Mostrar los encabezados de la respuesta
curl -I http://example.com

# Especificar un agente de usuario personalizado
curl -A "MiAgenteDeUsuario" http://example.com
```

<br/>

#### _wget_

[wget](https://www.gnu.org/software/wget/manual/wget.html): Diseñado principalmente para descargar archivos de la web de forma no interactiva. Su fortaleza radica en la descarga robusta y en segundo plano.

:::{tip}
Para verificar que se tiene instalado `wget` usar: `wget --version`
:::

```sh
# Sintaxis de llamada
wget [option]... [URL]...
```
**Argumentos**
- `URL`: La URL o URLs desde las que se hace la descarga.
**Opciones**:
- `-O file`: Guarda la salida en `file`.
- `-b`: Ejecuta la descarga en segundo plano.
- `--user=user`: Especifica el nombre de usuario para autenticación.
- `--password=password`: Especifica la contraseña para autenticación.
- `--progress=type`: Muestra el progreso de la descarga (`dot`, `bar`).
- `--limit-rate=rate`: Limita la velocidad de descarga.
- `-c`: Continúa una descarga interrumpida. Para que se mantenga el archivo parcial (la parte que se descargó) en caso de que haya ocurrido un error en la descarga.
- `-r`: Descarga de manera recursiva.
- `-k`: Convierte los enlaces para navegación local.
- `-q`: Desactiva el _output_. 
- `--user-agent=agent`: Especifica un agente de usuario personalizado.
- `-i`: Para indicar que el/los URLs que se van a leer, están en un archivo en la computadora local, en ese caso en lugar de poner URL poner el nombre y extensión del archivo.

**Patrones útiles**:

A continuación se presentan algunos casos de uso comunes.

```sh
# Descargar un archivo desde una URL
wget http://example.com/archivo.txt

# Descargar un archivo y guardarlo con un nombre específico
wget -O nuevo_nombre.txt http://example.com/archivo.txt

# Descargar un archivo en segundo plano
wget -b http://example.com/archivo.txt

# Descargar un archivo con autenticación básica
wget --user=usuario --password=contraseña http://example.com/archivo_protegido.txt

# Descargar un archivo y mostrar el progreso en formato de barra
wget --progress=bar http://example.com/archivo.txt

# Descargar un archivo y limitar la velocidad de descarga
wget --limit-rate=200k http://example.com/archivo.txt

# Descargar un archivo y continuar una descarga interrumpida
wget -c http://example.com/archivo.txt

# Descargar un sitio web completo de manera recursiva
wget -r http://example.com

# Descargar un sitio web completo y convertir los enlaces para navegación local
wget -r -k http://example.com

# Descargar un archivo y especificar el agente de usuario
wget --user-agent="MiAgenteDeUsuario" http://example.com/archivo.txt
```

<br/>

## Entrada de datos

Es posible solicitar al usuario que ingrese información, para ello se usa el comando `read`:

```sh
read VAR
```
- En _VAR_ se almacenará el texto ingresado.

<br/>

(sh-evaluacion-aritmetica)=
## Expansión aritmética

La expansión aritmética es un mecanismo que permite evaluar expresiones matemáticas directamente dentro del _shell_ y reemplazar la expresión por su resultado numérico. Para ello se utiliza `$(( ... ))` y `(( ... ))`:

:::{caution}
En ambas expresiones es recomendado (mas no obligatorio) dejar especios entre los paréntesis y las expresiones, como se verá en los ejemplos posteriores.
:::

:::{important}
Las expresiones aritméticas están diseñadas para trabajar únicamente con números enteros, no para números de punto flotante.
:::

```sh
# Sintaxis básica
$((expresión_aritmética))

# Sintaxis básica
((expresión_aritmética))
```
- Las expresiones deben de tener solo valores numéricos.
- `$((expresión_aritmética))`: Evalúa y devuelve el resultado (para imprimir o asignar).
    - Se usa cuando quieres usar el resultado de una expresión.
    - Se puede almacenar en una variable o imprimir directamente.
- `((expresión_aritmética))`: Solo evalúa (para asignaciones, condiciones, contadores).
    - Se usa para realizar operaciones, cambiar valores, o en condiciones.
    - No imprime nada a menos que se indique.
    - En condiciones retorna 0 si la expresión es verdadera, y 1 si es falsa.

:::{tip}
Para saber si una expresión debe de ir entre `$(( ... ))` o `(( ... ))` revisar los tipos de operadores y los ejemplos enlistados, estos indicarán el uso más común para ese tipo de expresiones. Pero lo más fundamental es si se quiere asignar o imprimir usar `$(( ... ))`, si solo se quiere evaluar usar `(( ... ))`.
:::

### Operadores

#### Aritméticos

:::{note}
Se pueden usar parétesis para agrupar expresiones que deben de ser evaluadas en conjunto y previo al resto de las expresiones (conforme a la jerarquía de operaciones).
:::

| Operador | Descripción | Ejemplo |
| --- | --- | --- |
| + | `Suma` | $(( 5 + 3 )) |
| - | `Resta` | $(( 5 - 2 )) |
| * | `Multiplicación` | $(( 4 * 2 )) |
| / | `División entera` | $(( 10 / 3 )) |
| % | `Módulo (residuo)` | $(( 10 % 3 )) |
| ** | `Exponenciación` | $(( 2 ** 3 )) |

**Ejemplo**

```sh
# Calcular el total de productos con precio fijo
precio_unitario=20
cantidad=3
total=$(( precio_unitario * cantidad ))
echo "Total: $total"  # Total: 60
```

#### Incremento/Decremento

| Operador | Descripción | Ejemplo |
| --- | --- | --- |
| ++ | `Incremento (pre o post)` | (( ++a )), (( a++ )) |
| -- | `Decremento (pre o post)` | (( --b )), (( b-- )) |

**Ejemplo**

```sh
# Contador simple
contador=0
(( contador++ ))
(( contador++ ))
echo "Contador: $contador"  # Contador: 2
```

#### Asignación

| Operador | Descripción | Ejemplo |
| --- | --- | --- |
| = | `Asignación simple` | (( a=5 )) |
| += | `Suma y asigna` | (( a+=3 )) |
| -= | `Resta y asigna` | (( a-=2 )) |
| *= | `Multiplica y asigna` | (( a*=4 )) |
| /= | `Divide y asigna` | (( a/=2 )) |
| %= | `Módulo y asigna` | (( a%=3 )) |
| **= | `Exponencia y asigna` | (( a**=2 )) |

**Ejemplo**

```sh
# Acumular puntos en un juego
puntos=10
(( puntos += 5 ))  # gana 5 puntos
(( puntos *= 2 ))  # se duplican los puntos
echo "Puntos: $puntos"  # Puntos: 30

```

#### Comparación

| Operador | Descripción | Ejemplo |
| --- | --- | --- |
| == | `Igual a` | $(( a == b )) |
| != | `Distinto de` | $(( a != b )) |
| < | `Menor que` | $(( a < b )) |
| <= | `Menor o igual que` | $(( a <= b )) |
| > | `Mayor que` | $(( a > b )) |
| >= | `Mayor o igual que` | $(( a >= b )) |

**Ejemplo**

:::{note}
En este ejemplo se usa `(( ... ))` en lugar de `$(( ... ))`, esto es así porque no se pretende imprimir ni asignar la expresión a ningún lado, solo evaluarla.
:::

```sh
# Verificar si un número es mayor que otro
a=10
b=5
if (( a > b )); then
  echo "$a es mayor que $b" # Output: 10 es mayor que 5
fi


```

#### Bitwise

| Operador | Descripción | Ejemplo |
| --- | --- | --- |
| & | `AND bit a bit` | $(( a & b )) |
| ` | ``` | OR bit a bit |
| ^ | `XOR bit a bit` | $(( a ^ b )) |
| ~ | `NOT bit a bit (unario)` | $(( ~a )) |
| << | `Desplazamiento a la izquierda` | $(( a << 1 )) |
| >> | `Desplazamiento a la derecha` | $(( b >> 2 )) |

**Ejemplo**

```sh
# Usar bits para controlar flags (modo binario)
flag1=1      # 0001
flag2=2      # 0010
combined=$(( flag1 | flag2 ))  # 0011 = 3
echo "Flags combinados: $combined"  # Flags combinados: 3
```

#### Operador ternario

El operador ternario permite hacer una evaluación `if ... then ... else ...` de manera simplificada:

```sh
# Sintaxis del operador ternario
condición ? valor_si_verdadero : valor_si_falso
```

**Ejemplo**

```sh
# Definir el número mayor entre dos números
num1=10
num2=5
mayor=$(( num1 > num2 ? num1 : num2 ))
echo "El mayor entre $num1 y $num2 es: $mayor"
```

<br/>

## Estructuras condicionales

(shell-conditional-expressions)=
### Expresiones condicionales

Una condición en el contexto de un _shell_ es una expresión que se evalúa como verdadera o falsa. El resultado de esta evaluación determina el flujo de ejecución del _script_. En _Bash_ se utilizan principalmente `[ ]` (corchetes simples) y `[[ ]]` (corchetes dobles) para evaluar condiciones dentro de estructuras de control como `if`, `while`, `until`, etc. Las diferencias entre estos operadores son las siguientes:
- `[ ]`: Corchetes simples.
    - Requiere espacios después del corchete de apertura y antes del corchete de cierre. Los operadores como `-eq`, `-gt`, `=`, `!=` deben estar separados por espacios.
    - Realiza la expansión de palabras y la división de campos después de la expansión. Esto puede llevar a errores si las variables contienen espacios o caracteres especiales que no están entre comillas.
    - Utiliza operadores como `-eq`, `-ne`, `-gt`, `-lt`, `-ge`, `-le` para comparaciones numéricas y `=` y `!=` para comparaciones de cadenas. Para combinar condiciones usa `-a` (_AND_) y `-o` (_OR_).
    - Ejemplo: `[ 10 -le 10 ]` <br/> `[ "$string2" \> "$string1" ]`
- `[[ ]]`: Corchetes dobles.
    - Es más flexible con los espacios. Permite operadores como `==`, `!=`, `<`, `>` directamente para comparación de cadenas (sin necesidad de escapar los caracteres `<` y `>`).
    - No realiza la división de campos y realiza menos expansiones, lo que lo hace más seguro y predecible, especialmente al trabajar con variables que pueden contener espacios.
    - Soporta los operadores de `[ ]` pero además introduce operadores más intuitivos como `&&` (_AND_), `||` (_OR_), `=~` (para expresiones regulares), `<` y `>` para comparación lexicográfica de cadenas.
    - Ejemplo: `[[ "$string2" > "$string1" ]]`

<br/>

### If

Es estructura condicional, usa las palabras reservadas `if`, `else` y `fi`. Ejecuta un bloque de código si una condición es verdadera, también permite ejecutar otro bloque diferente si la condición es falsa. Se puede usar `elif` para evaluar condiciones múltiples. Se pueden escribir en múltiples líneas (_scripts_) o en una sola linea (directo en la terminal):

```sh
# Condición simple if ... then
if [ condición ]; then
    # Código a ejecutar si la condición es verdadera
fi

# Condición simple if ... then en una sola línea
if [ condición ]; then comando; fi

# ---------------------------------------------------

# Condición compleja: if ... then ... else ...
if [ condición ]; then
    # Código si la condición es verdadera
else
    # Código si la condición es falsa
fi

# Condición compleja: if ... then ... else ... en una sola línea
if [ condición ]; then comando_si_verdadero; else comando_si_falso; fi

# ---------------------------------------------------

# Evaluar condiciones múltiples
if [ condición1 ]; then
    # Código si condición1 es verdadera
elif [ condición2 ]; then
    # Código si condición2 es verdadera
else
    # Código si ninguna de las condiciones anteriores es verdadera
fi

# Evaluar condiciones múltiples en una sola línea
if [ condición1 ]; then comando1; elif [ condición2 ]; then comando2; else comando_si_ninguna; fi
```

**Ejemplo**

En este ejemplo se hace uso de una evalución de múltiples condiciones, para verificar el valor de una variable:

```sh
# Múltiples líneas
if [ "$VAR" -eq 1 ]; then 
    echo "Uno"
elif [ "$VAR" -eq 2 ]; then 
    echo "Dos"
else 
    echo "Otro"
fi

# Una sola línea
if [ "$VAR" -eq 1 ]; then echo "Uno"; elif [ "$VAR" -eq 2 ]; then echo "Dos"; else echo "Otro"; fi
```

<br/>

### Case

Permite ejecutar diferentes bloques de código basados en el valor de una variable o expresión. Es útil cuando tienes múltiples valores discretos a comparar. Se puede escribir en múltiples líneas (_scripts_) o en una sola linea (directo en la terminal):

```sh
# Uso de case
case "$variable" in
    patron1)
        # Código a ejecutar si $variable coincide con patron1
        ;;
    patron2)
        # Código a ejecutar si $variable coincide con patron2
        ;;
    *) # Patrón por defecto (opcional)
        # Código a ejecutar si no coincide con ningún patrón anterior
        ;;
esac

# Uso de case en una sola línea
case "$variable" in patrón1) comando1 ;; patrón2) comando2 ;; *) comando_default ;; esac
```

**Ejemplo**

En este ejemplo se hace uso de una evalución de múltiples condiciones, para verificar el valor de una variable:

```sh
# Múltiples líneas
VALOR="b"
case "$VALOR" in 
    a) 
        echo "Es a" 
        ;; 
    b) 
        echo "Es b" 
        ;; 
    *) 
        echo "Otro valor" 
        ;; 
esac

# Una sola línea
VALOR="b"; case "$VALOR" in a) echo "Es a" ;; b) echo "Es b" ;; *) echo "Otro valor" ;; esac
```

<br/>

## Estructuras cíclicas

### For

Permite iterar sobre una lista de elementos (palabras, archivos, etc.) o un rango numérico. Tiene tres estructoras principales como se puede definir y que a su vez se pueden escribir en múltiples líneas (_scripts_) o en una sola linea (directo en la terminal):

```sh
# Iterar sobre una lista
for variable in item1 item2 item3 ...; do
    # Código a ejecutar para cada item
    echo "Elemento: $variable"
done

# Iterar sobre una lista en una sola línea
for variable in item1 item2 item3; do comando; done

# ---------------------------------------------------

# Iterar sobre un rango numérico
for i in $(seq 1 5); do
    echo "Número: $i"
done

# Iterar sobre un rango numérico en una sola línea
for i in $(seq 1 5); do echo "Número: $i"; done

# ---------------------------------------------------

# Iteración estilo C
for (( i=1; i<=5; i++ )); do
    echo "Número: $i"
done

# Iteración estilo C en una sola línea
for (( i=1; i<=5; i++ )); do echo "Índice: $i"; done
```
**Notas**
- En la secuencia ambos números son inclusivos. La sintaxis general es `seq [PRIMERO [INCREMENTO]] ÚLTIMO`:
    - _PRIMERO_: El primer número de la secuencia (opcional, por defecto es 1).
    - _INCREMENTO_: El valor que se añade (o resta si es negativo) en cada paso (opcional, por defecto es 1).
    - _ÚLTIMO_: El último número de la secuencia (obligatorio).
- En el estilo de _C_. La sintaxis general es `(( inicialización ; condición ; actualización ))`:
    - _inicialización_: El primer valor se la secuencia, se debe indicar con una variable y el símbolo `=`, ejemplo: `i=0`.
    - _condición_: Es una condición que debe cumplir la variable definida en _inicialización_, usualmente se usarán los operadores `<`, `<=`, `>` y `>=`, ejemplo: `i<5`.
    - _actualización_: Indica el incremento/decremento de la variable definida en _inicialización_, usualmente se usan operadores de incremento/decremento (`i++` y `i--`) u operadores de asignación recursivos (`i+=2`, `i-=2`, etc.).

<br/>

**Ejemplo**.

En los siguientes ejemplo se itera por los tres primeros números naturales de manera inversa, como lista, secuencia y en estilo _C_.

```sh
# Como lista
for i in 3 2 1; do 
    echo "Número: $i"
done

# Como secuencia
for i in $(seq 3 -1 1); do 
    echo "Número: $i"
done

# Estilo C
for i in (( i=3; i>=1; i-- )); do 
    echo "Número: $i"
done
```

<br/>

### Until

Ejecuta un bloque de código hasta que una condición sea verdadera. La condición se evalúa al final de cada iteración. Esto significa que el bloque de código se ejecutará al menos una vez. Se puede escribir en múltiples líneas (_scripts_) o en una sola linea (directo en la terminal):

```sh
# Iteración hasta que se cumpla la condición
until [ condición ]; do
    # Código a ejecutar hasta que la condición sea verdadera
    # Asegúrate de que algo cambie dentro del bucle para que la condición eventualmente sea verdadera
done

# Iteración hasta que se cumpla la condición en una sola línea
until [ condición ]; do comando; done
```

**Ejemplo**.

En este ejemplo se pregunta iterativamente al usuario que ingrese un texto, el cíclo se detiene hasta que se ingresa "si".

```sh
# Múltiples líneas
ESTADO="no"
until [ "$ESTADO" = "si" ]; do 
    echo "¿Ya?"
    read RESPUESTA
    if [ "$RESPUESTA" = "si" ]; then 
        ESTADO="si"
    fi
done

# Una sola línea
ESTADO="no"; until [ "$ESTADO" = "si" ]; do echo "¿Ya?"; read RESPUESTA; if [ "$RESPUESTA" = "si" ]; then ESTADO="si"; fi; done
```

### While

Ejecuta un bloque de código mientras una condición sea verdadera. La condición se evalúa al principio de cada iteración. Se puede escribir en múltiples líneas (_scripts_) o en una sola linea (directo en la terminal):

```sh
# Iteración hasta que se cumpla la condición
while [ condición ]; do
    # Código a ejecutar mientras la condición sea verdadera
    # Asegúrate de que algo cambie dentro del bucle para evitar un bucle infinito
done

# Iteración hasta que se cumpla la condición en una sola línea
while [ condición ]; do comando; done
```

**Ejemplo**.

En este ejemplo se itera hasta que un contador alcanza el valor de 3.

```sh
# Múltiples líneas
CONTADOR=0
while [ "$CONTADOR" -lt 3 ]; do 
    echo "Contador: $CONTADOR"
    ((CONTADOR++))
done

# Una sola línea
CONTADOR=0; while [ "$CONTADOR" -lt 3 ]; do echo "Contador: $CONTADOR"; ((CONTADOR++)); done
```

<br/>

## Funciones (UDF)

Es un bloque de código que se define dentro de un _script_ o directamente en la línea de comandos, al cual se le asigna un nombre. Posteriormente se puede llamar a esta función por su nombre para ejecutar el código que contiene, potencialmente con diferentes argumentos. A continuaciónse presentan cómo definir una función en _bash_.

:::{important}
En un script las funciones se deben de definir al inicio.
:::

:::{important}
Todos los argumentos en _Bash_ se definen por posición, en caso de que se quiera omitir un parámetro y éste tenga un valor por default se debe de pasar una cadena vacía `""`.
:::

:::{caution}
La palabra `return` no retorna valores, se usa para retornar el estatus de la ejecución _0_ para éxitoso y otros valores para errores (entre 1 y 255). Para retornar valores usar `echo $( ... )`
:::

```sh
# Definir función estilo tradicional
mi_funcion() {
    # Definición de los parámetros
    local param1="$1"  # Primer parámetro
    local param2="${2:-default}"  # Segundo parámetro (con valor por defaut)
    ...
    
    # Cuerpo de la función
    # Usar parámetros en el cuerpo de la función
    local result=$((param1 + param2))

    # Retornar estatus de ejecución
    return $result
    # Retornar valor: echo "$result"
}

# Definir función con palabra reservada
function mi_funcion {
    # Definición de los parámetros
    local param1="$1"  # Primer parámetro
    local param2="${2:-default}"  # Segundo parámetro (con valor por default)
    ...
    
    # Cuerpo de la función
    ...

    # Retornar valor
    return $resultado # $resultado se tuvo que haber definido en algún momento
}
```
- Se recomienda que el nombre esté en minúsculas, con las palabras separadas por guiones bajos.
- Si el parámetro tiene un valor por default se debe de indicar con `"${n:-default}"`, donde _n_ es el número del parámetro y _default_ es el valor por default.
- Estrictamente hablando los valores de los parámetros se almacenan en `$1`, `$2`, etc. pero es recomendado crear variables locales con nombres descriptivos de los parámetros.
    - `$0` almacena el nombre de la función.
    - `$@` o `$*` se utilizan para acceder a todos los parámetros
- Es recomendado usar `local` al definir las variables para evitar conflictos con variables globales.
- Por default se retorna el estatus de ejecución donde 0 es éxitoso y cualquier otro número es un error. Se puede usar `echo` para retornar un valor específico.

Para llamar a una función únicamente utilizar su nombre y los parámetros separados por espacios.

```sh
# Llamar a una función
my_funcion arg1 arg2 ...
```

En caso de que la función retorne un valor se puede asignar a una variable o también se puede almacenar automáticamente en `$?`:

```sh
# Llamar a función
mi_funcion arg1 arg2 ...
echo "$?"  # $? contiene el valor de retorno

# Llamar función y almacenar valor en variable
result=$(mi_funcion arg1 arg2 ...)
echo "$result"
```

<br/>

## Nano

Nano es un editor de texto simple y fácil de usar que se ejecuta en la terminal. Permite crear, editar y guardar archivos directamente desde la línea de comandos. Es una alternativa más amigable a editores como _vi_ o _vim_, ya que muestra los atajos de teclado en la parte inferior de la pantalla. Se usa comúnmente en sistemas Linux y macOS para editar archivos de configuración o escribir _scripts_ rápidamente.

:::{note}
En la mayoría de las distribuciones de Linux (como Ubuntu, Debian y Fedora) y macOS, _Nano_ viene instalado por defecto.
:::

```sh
# Verificar versión de nano
nano --version

# Abrir nano
nano

# Abrir o crear archivo
nano filename.ext
```
- Si _filename.ext_ no existe, entonces se creará el archivo y se abrirá.

Una vez abierto el archivo, en la terminal se puede modificar el contenido y desplazarse sobre el documento. Existen los siguientes _shorcuts_ (hay otros que aparecerán ahí mismo en la terminal):
- `Ctrl+K`: Corta una línea y la almacena en el portapapeles.
- `Ctrl+U`: Pega lo que esté en el portapapeles.
- `Ctrl+O`: Guarda un archivo, es necesario presionar <kbd>enter</kbd> para confirmar.
- `Ctrl+X`: Salir del editor de texto.

<br/>

## Scripts

Un _script_ en _Bash_ es un archivo de texto plano que contiene una secuencia de comandos que el intérprete de comandos _Bash_ puede leer y ejecutar automáticamente, línea por línea (o bloque por bloque en estructuras de control).

### Crear/editar un _script_

Existen múltiples formas de crear un _script_, por ejemplo usando cualquier editor como _VS Code_, el archivo debe de tener la extensión `.sh`. Otra alternativa es usar _nano_, como se explicará a continuación.

:::{tip}
Para agregar comentarios en un _script_ usar `#`, por ejemplo: `# Un comentario`.
:::

```sh
# Crear el archivo
nano mi_script.sh
```

Una vez abierto escribir el contenido del _script_. Asegurarse de que la primera línea sea `#!/bin/bash`, para indicar que el _script_ debe ejecutarse con _Bash_:

```sh
#!/bin/bash
echo "Hola, Mundo"
```
- Para guardar utilizar <kbd>Ctrl + O</kbd> para guardar el archivo y <kbd>Enter</kbd> para confirmar el nombre del archivo y guardarlo.
- Para salir de _nano_ usar <kbd>Ctrl + X</kbd>.


Para editar un _script_ existente simplemente abrir el _script_ en un editor y modificar el contenido del mismo como sea necesario. En nano para abrir un archivo existente usar el siguiente comando (el archivo debe estar en el directorio actual, en caso contrario se debe indicar su ruta)

```sh
# Abrir el archivo
nano mi_script.sh
```

### Ejecutar un _script_

Para ejecutar un _script_ de _Bash_ seguir lo siguientes pasos:

**1. Dar permisos de ejecución al _script_**: Antes de poder ejecutar el _script_, es necesario darle permisos de ejecución. Usa el siguiente comando:

```sh
# Dar permisos al script
chmod +x mi_script.sh
```

**2. Ejecutar el script desde la terminal**: Después de otorgar los permisos simplemente llamar al _script_:

```sh
# Ejecutar script
./mi_script.sh
```

### _Scripts_ con parámetros

Si se espera que un _script_ reciba parámetros se debe hacer referencia a los valores de esos parámetros en el cuerpo del _script_ con `$1`, `$2`, etc. Ejemplo de un _script_ que recibe parámetros:

```sh
#!/bin/bash

# Mostrar el nombre del script
echo "Nombre del script: $0"

# Mostrar el número de parámetros
echo "Número de parámetros recibidos: $#"

# Mostrar todos los parámetros en una línea
echo "Parámetros recibidos: $@"

# Mostrar parámetros individuales
echo "Primer parámetro: $1"
echo "Segundo parámetro: $2"
echo "Tercer parámetro: $3"
```
- En este ejemplo se hace uso de las principales formas de usar los parámetros:
    - `$0`: Contiene el nombre del _script_.
    - `$#`: Contiene el número de parámetros.
    - `$@`: Contiene todos los parámetros.
    - `$1`, `$2`, ...: Contienen cada uno de los parámetros posicionales.

Para ejecutar un _script_ que recibe parámetros usar alguna de las siguientes opciones:

:::{caution}
Recordar que antes de ejecutar un _script_ se tuvo que haber otorgado permisos con `chmod +x mi_script.sh`.
:::

```sh
# Parámetros posicionales
./mi_script.sh valor1 valor2 "valor 3" ...

# Parámetros especiales
./mi_script.sh -a -b --opcion=valor
```
- Si _valor_i_ tiene espacios debe de ir entre comillas

<br/>

## Wildcards (Globbing)

Los _globbing_ en _Bash_ son mecanismos de coincidencia de patrones que permiten usar comodines o _wildcards_ en cadenas.

:::{caution}
Por default, los comodines no coinciden con archivos o directorios que comienzan con un punto (`.`) (archivos ocultos). Para incluirlos, el patrón debe comenzar explícitamente con un punto, por ejemplo: `ls .*`.
:::

| Atajo    | Descripción                                  | Ejemplo de uso                     |
|----------|----------------------------------------------|------------------------------------|
| `*`      | Comodín para cualquier número de caracteres  | Listar todos los archivos PDF: `ls *.pdf` |
| `?`      | Comodín para un único carácter               | `ls documento?.doc`                |
| `[ ]`    | Comodín para rangos o conjuntos de caracteres| `ls [abc]*.log`                    |

<br/>

## Shortcuts

A continuación se enlistan algunos atajos de teclado al trabajar en _bash_ desde la terminal.

:::{caution}
En macOS usar <kbd>Command</kbd> en lugar de <kbd>Ctrl</kbd>.
:::

| Atajo                  | Descripción                                              | 
|------------------------|----------------------------------------------------------|
| `Ctrl + A`             | Mover el cursor al principio de la línea.                |
| `Ctrl + E`             | Mover el cursor al final de la línea.                    |
| `Ctrl + U`             | Eliminar desde el cursor hasta el principio de la línea. |
| `Ctrl + K`             | Eliminar desde el cursor hasta el final de la línea.     |
| `Ctrl + W`             | Eliminar la palabra anterior al cursor.                  |
| `Ctrl + L`             | Limpiar la pantalla (equivalente a `clear`).             |
| `Ctrl + C`             | Interrumpir el comando en ejecución.                     |
| `Ctrl + Z`             | Suspender el proceso en ejecución (en segundo plano).    |
| `Tab`                   | Autocompletar el comando o archivo.                     |
| `Ctrl + R`             | Buscar en el historial de comandos.                      |
| `!!`                    | Ejecutar el último comando.                             |
| `!n`                    | Ejecutar el comando con el número _n_ del historial.    |
| `Arrow Up`             | Buscar el comando anterior en el historial.              |
| `Arrow Down`           | Buscar el comando siguiente en el historial.             |
| `Ctrl + D`             | Cerrar la sesión o terminar la terminal (logout).        |

<br/>

## Patrones útiles

A continuación se presentan algunas acciones comunes en _shell_.

### Almacenar _output_ de un comando en un archivo

Para almacenar el _output_ de un comando de _Bash_ en un archivo, se puede utilizar el operador de redirección (`>`) o el operador de anexado (`>>`).
- `>`: Crea o sobrescribe el archivo, es decir, si el archivo ya existe, su contenido anterior será reemplazado por el nuevo output.
- `>>`: Anexa el output al final del archivo, sin borrar el contenido previo del archivo.

```sh
# Crear o sobrescribir archivo
ls > listado_de_archivos.txt

# Anexar al archivo
echo "Nuevo texto" >> archivo.txt
```

### Operador _pipe_

El operador _pipe_ en _Bash_ se utiliza para conectar la salida estándar (_stdout_) de un comando con la entrada estándar (_stdin_) de otro comando. En esencia se ejecutan los siguientes pasos:
1. Ejecuta el primer comando.
2. Captura la salida estándar (lo que normalmente se verá en la pantalla) de ese comando.
3. Envía esa salida directamente como la entrada estándar al segundo comando.
4. El segundo comando procesa esa entrada y produce su propia salida.

```sh
# Sintaxis básica
comando1 | comando2

# Sintaxis encadenada
comando1 | comando2 | comando3 | ...
```

**Ejemplo**:

En este ejemplo se desea encontrar todas las líneas de una archivo que contengan la palabra "error".

```sh
# Uso de pipe
cat mi_archivo.txt | grep "error"
```