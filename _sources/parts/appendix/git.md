# git

Git es un sistema de control de versiones distribuido que permite rastrear cambios en el código fuente, coordinar el trabajo entre múltiples desarrolladores y gestionar diferentes versiones de un proyecto de manera eficiente.  Para poder utilizar _git_ se debe instalar, aunque en MacOS ya viene instalado de fábrica. 

:::{note}
Para más información consultar la [documentación](https://git-scm.com/docs) de _git_.
:::

Para verificar que se tiene _git_ instalado utilizar el siguiente comando.

```sh
# Verificar que se tenga _Git_ instalado
git --version
```

Conceptos importantes al trabajar con _git_:

- **Repositorio**: Estructura que contiene todos los archivos, historial de cambios y configuraciones de un proyecto gestionado con _Git_. Puede ser local o remoto.
- **_Working Directory_**: Espacio de trabajo donde se encuentran los archivos del proyecto en su estado actual, permitiendo modificaciones antes de ser confirmadas en el historial. A los archivos en general no se les da seguimiento, primero se deben de pasar al _staging area_.
- **_Staging Area_**: Espacio intermedio donde se preparan los cambios antes de confirmarlos en el historial del repositorio. Permite seleccionar qué modificaciones incluir en el próximo _commit_.
- **_.git Directory_**: Carpeta oculta dentro de un repositorio que almacena toda la información de Git, incluyendo historial de cambios, configuraciones y referencias a los _commits_. Este directorio nunca se debe de editar o eliminar.
- **_Committing_**: Proceso de guardar cambios en el historial del repositorio, creando un nuevo registro con una descripción y un identificador único.
- **_Hash_**: Código único generado por _Git_ para identificar cada commit, basado en el contenido y metadatos del cambio. Normalmente es una cadena hexadecimal de 40 caracteres, sin embargo, es posible solo indicar los primero 6 u 8 caracteres para poder identificar un _commit_.
- **_Branch_**: Rama del desarrollo que permite trabajar en cambios independientes sin afectar la versión principal del código. Por default cada repositorio de _Git_ tiene una _branch_ por default llamada "_master_" o "_main_". Cada _branch_ es independiente por lo que modificaciones en una no afectan a otra, hasta que se unen (_merge_) ambas _branch_.
- **_Merging_**: Proceso de combinar los cambios de una rama en otra, integrando el historial de ambas para unificar el desarrollo.
- **_Remote_**: Repositorio alojado en un servidor o plataforma externa que permite compartir cambios y colaborar con otros desarrolladores. Cuando se clona un repositorio de una _url_, se almacena información sobre ese repositorio original, a ese repositorio original se le llama "remote" (como nombre conceptual, no como tal el nombre del remote, cada remote tiene su propio nombre, por ejemplo, es común que su nombre sea "_origin_").
- **_Pull_**: Acción de descargar y fusionar los cambios más recientes de un repositorio remoto en el repositorio local.
- **_Push_**: Acción de enviar los _commits_ del repositorio local a un repositorio remoto, actualizando la versión compartida del proyecto.

En el proceso de realizar un _commit_ _Git_ utiliza una estructura de tres niveles para almacenar la información relacionada con el _commit_:

- **_Commit_** - Información del _commit_: Aquí se almacena información como el autor, el mensaje, la hora a la que ocurrió el _commit_, etc.
- **_Tree_** - Información de los archivos: Es un objeto que actúa como un directorio en _Git_. Contiene referencias a otros _trees_ (subdirectorios) y _blobs_ (archivos). Almacena la estructura de los archivos y directorios en un commit, asociando cada archivo a su correspondiente _blob_.
- **_Blob_** - Contenido de los archivos: Para cada archivo en el _tree_ existe un _blob_. Un _blob_ contiene un _snapshot_ comprimido del contenido del archivo cuando ocurrió el _commit_. Si en un _commit_ particular no ocurrió un cambio en un archivo en particular, entonces como _blob_ para ese archivo se utilizará el uno anterior (de un _tree_ pasado). Cada _blob_ tiene un identificador _hash SHA-1_.

A continuación se presenta la sintaxis de llamada del comando `git`:

:::{attention}
Para más información consultar la [documentación](https://git-scm.com/docs/git) de _git_.
:::

```sh
git [-v | --version] [-h | --help] [-C <path>] [-c <name>=<value>]
           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
           [-p | --paginate | -P | --no-pager] [--no-replace-objects] [--bare]
           [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]
           [--super-prefix=<path>] [--config-env=<name>=<envvar>]
           <command> [<args>]
```
- **Comandos**
    - Ver {ref}`git-commands`.
- **Opciones**
    - `-v, --version`: Imprime la versión _Git suite_ de la que proviene el programa _git_.
    - `-h, --help`: Imprime ayuda sobre el comando y una lista de los comandos más utilizados.
    - `-C <path>`: Ejecuta como si _Git_ se iniciara en _\<path>_ en lugar del directorio de trabajo actual.
    - `-c <name>=<value>`: Pasa un parámetro de configuración al comando.
    - `--config-env=<name>=<envvar>`: Como `-c <name>=<value>`, proporcionea la variable de configuración _\<name>_ un valor, donde _\<envvar>_ es el nombre de una variable de entorno para recuperar el valor.
    - `--exec-path[=<path>]`: Ruta a donde sea están instalados los programas de _core Git_.
    - `--html-path`: Imprime la ruta, sin desarraigar, donde se instala la documentación HTML de _Git_.
    - `--man-path`: Imprime el _manpath_ (ver `man(1)`) para las páginas del manual para esta versión de _Git_.
    - `--info-path`: Imprime la ruta donde se instalan los archivos de información que documentan esta versión de _Git_.
    - `-p, --paginate`: Concatena (_pipe_) todos los resultados en _less_ (o si se establece, _$PAGER_) si la salida estándar es un terminal.
    - `-P, --no-pager`: No concatena (_pipe_) la salida de _git_ en un _pager_.
    - `--git-dir=<path>`: Establece la ruta al directorio del repositorio (directorio ".git").
    - `--work-tree=<path>`: Establece la ruta a la rama de trabajo. Puede ser una ruta absoluta o una ruta en relación con el directorio de trabajo actual.
    - `--namespace=<path>`: Establezce el espacio de nombres de _Git_.
    - `--super-prefix=<path>`: Actualmente solo para uso interno. Establece un prefijo que proporcione una ruta desde arriba de un repositorio hasta su raíz.
    - `--bare`: Trata el repositorio como un repositorio _bare_. Si el entorno _GIT_DIR_ no está configurado, se establece en el directorio de trabajo actual.
    - `--no-replace-objects`: No usa _refs_ de reemplazo para reemplazar los objetos _Git_.
    - `--literal-pathspecs`: Trata las _pathspecs_ literalmente (es decir, sin _globbing_, sin _pathspec magi_).
    - `--glob-pathspecs`: Agrega _"glob" magic_ a todos los _pathspec_.
    - `--noglob-pathspecs`: Agrega _"literal" magic_ a todos los _pathspec_.
    - `--icase-pathspecs`: Agrega _"icase" magic_ a todos los _pathspec_.
    - `--no-optional-locks`: No realiza operaciones opcionales que requieran bloqueos.
    - `--list-cmds=group[,group...]`: Lista de comandos por grupo. Esta es una opción interna/experimental y puede cambiar o eliminarse en el futuro.

<br/>

---
(git-commands)=
## Comandos

:::{warning}
En la siguiente tabla no se enlistan todos los comandos. Consultar la [documentación](https://git-scm.com/docs) de _git_.
:::

| Comando | Descripción |
| --- | --- |
| **Iniciar un área de trabajo** | Ver `git help tutorial` |
| [clone](https://git-scm.com/docs/git-clone) | Clonar un repositorio en un nuevo directorio. |
| [config](https://git-scm.com/docs/git-config) | Configurar opciones de usuario y repositorio en _Git_. |
| [init](https://git-scm.com/docs/git-init) | Crear un repositorio _Git_ vacío o reinicializar uno existente. |
| **Trabajar en los cambios actuales** | Ver `git help everyday` |
| [add](https://git-scm.com/docs/git-add) | Agrega el contenido de archivos al _staging area_. |
| [clean](https://git-scm.com/docs/git-clean) | Elimina archivos no rastreados del árbol de trabajo. |
| [mv](https://git-scm.com/docs/git-mv) | Mover o renombrar un archivo, un directorio o un enlace simbólico. |
| [restore](https://git-scm.com/docs/git-restore) | Restaurar archivos en el árbol de trabajo. |
| [rm](https://git-scm.com/docs/git-rm) | Elimina archivos del árbol de trabajo y del _staging area_. |
| **Examinar el historial y el estado** | Ver `git help revisions` |
| [bisect](https://git-scm.com/docs/git-bisect) | Usar búsqueda binaria para encontrar el _commit_ que introdujo un error. |
| [diff](https://git-scm.com/docs/git-diff) | Muestra diferencias entre _commits_, entre un _commit_ y el árbol de trabajo, etc. |
| [grep](https://git-scm.com/docs/git-grep) | Imprimir líneas que coincidan con un patrón. |
| [log](https://git-scm.com/docs/git-log) | Muestra los registros de _commits_. |
| [show](https://git-scm.com/docs/git-show) | Muestra varios tipos de objetos. |
| [status](https://git-scm.com/docs/git-status) | Muestra el estado del árbol de trabajo. |
| **Gestionar, marcar y ajustar el historial** |  |
| [annotate](https://git-scm.com/docs/git-annotate) | Muestra quién cambió cada línea en un archivo. |
| [branch](https://git-scm.com/docs/git-branch) | Listar, crear o eliminar ramas. |
| [checkout](https://git-scm.com/docs/git-checkout) | Cambiar ramas o restaurar archivos del árbol de trabajo. |
| [commit](https://git-scm.com/docs/git-commit) | Registra cambios en el repositorio. |
| [merge](https://git-scm.com/docs/git-merge) | Une dos o más historiales de desarrollo. |
| [rebase](https://git-scm.com/docs/git-rebase) | Reaplicar _commits_ sobre otra base. |
| [reset](https://git-scm.com/docs/git-reset) | Restablece el `HEAD` actual al estado especificado. |
| [switch](https://git-scm.com/docs/git-switch) | Cambiar entre ramas. |
| [tag](https://git-scm.com/docs/git-tag) | Crear, listar, eliminar o verificar una etiqueta firmada con GPG. |
| **Colaborar con otros** | Ver `git help workflows` |
| [fetch](https://git-scm.com/docs/git-fetch) | Descargar objetos y referencias de otro repositorio. |
| [pull](https://git-scm.com/docs/git-pull) | Descargar e integrar cambios desde otro repositorio o rama local. |
| [push](https://git-scm.com/docs/git-push) | Actualizar referencias remotas junto con los objetos asociados. |
| [remote](https://git-scm.com/docs/git-remote) | Gestionar repositorios remotos. |

<br/>

### _add_

[add](https://git-scm.com/docs/git-add): Agrega el contenido de archivos al índice (_staging area_).

```sh
# Sintaxis de llamada
git add [<options>] [--] <pathspec>...
```
**Argumentos**
- `<pathspec>`: Archivos para agregar contenido. Se puede indicar `.` para indicar que todo el directorio activo (incluyendo subdirectorios).
**Opciones**
- `-n, --dry-run`: En modo _dry run_. Esto significa que el comando se ejecutará simulando los efectos que tendría, pero sin realizar cambios reales en el repositorio.
- `-v, --verbose`: Muestra más detalles sobre el proceso de `add`.
- `-i, --interactive`: Selección interactiva.
- `-p, --patch`: Selecciona _hunks_ de manera interactiva.
- `-e, --edit`: Edita _diff_ actual y aplica.
- `-f, --force`: Permite agregar archivos ignorados de otra manera.
- `-u, --update`: Actualiza archivos rastreados.
- `--renormalize`: Renormaliza la _EOL_ de los archivos rastreados (implica -u).
- `-N, --intent-to-add`: Registra solo el hecho de que la ruta se agregará más tarde.
- `-A, --all`: Agrega cambios de todos los archivos rastreados y sin seguimiento.
- `--ignore-removal`: Ignora las rutas eliminadas en el árbol de trabajo (igual que `--no-all`).
- `--refresh`: No agrega, solo actualiza el _staging area_.
- `--ignore-errors`: Simplemente omite los archivos que no se pueden agregar debido a errores.
- `--ignore-missing`: Compruebe si, ilos archivos _- even missing -_ se ignoran en _dry run_.
- `--sparse`: Permite entradas de actualización fuera del cono _parse-checkout_.
- `--chmod (+|-)x`: Sobreescribe el bit ejecutable de los archivos enumerados.
- `--pathspec-from-file <file>`: Lee _pathspec_ desde un archivo.
- `--pathspec-file-nul`: Con `--pathspec-from-file`, los elementos _pathspec_ se separan con el carácter de _NUL_.

Patrones útiles:

```sh
# Agregar todo el directorio actual
git add .

# Agregar de un directorio específico
git add path/to/dir

# Agregar archivos con extensión específica en un directorio
git add path/to/dir\*.ext # Usar . para todo el directorio

# Agregar archivos con patrón específico en un directorio
git add path/to/dir\pattern*.ext # Ejm pattern al inicio
```
- `*` funcionar como un _wildcard_ y se puede combinar con cualquier patrón para buscar archivos/directorios que tengan determinados patrones en sus nombres.

<br/>

### _annotate_

[annotate](https://git-scm.com/docs/git-annotate): Muestra quién insertó/cambió cada línea en un archivo. Este comando no muestra las lineas que se eliminaron ya que su objetivo es mostrar el autor de cada línea en el estado actual del archivo.

```sh
# Sintaxis de llamada
git annotate [<options>] [<rev-opts>] [<rev>] [--] <file>
```
**Argumentos**
- `<file>`: Archivo a analizar.
**Opciones**
- `--[no-]incremental`: Muestra entradas _blame_ mientras se encuentran, incrementalmente.
- `-b`: No muestra los nombres de objetos _boundary commits_ (predeterminado: _off_).
- `--[no-]root`: No trata los _ root commits_ como _boundaries_ (predeterminado: _off_).
- `--[no-]show-stats`: Muestra estadísticas de costos de trabajo.
- `--[no-]progress`: Fuerza informes de progreso.
- `--[no-]score-debug`: Muestra la puntuación de salida para las entradas _blame_.
- `-f, --[no-]show-name`: Muestra nombre de archivo original (predeterminado: _auto_).
- `-n, --[no-]show-number`: Muestra el número de _lino_ original (predeterminado: _off_).
- `-p, --[no-]porcelain`: Muestra en un formato diseñado para el consumo de la máquina.
- `--[no-]line-porcelain`: Muestra formato _porcelain_ con información de confirmación por línea.
- `-c`: Usa el mismo modo de salida que _git-annotate_ (predeterminado: _off_).
- `-t`: Muestra marca de tiempo cruda (predeterminado: _off_).
- `-l`: Muestra el _SHA1_ largo del _commit_ (predeterminado: _off_).
- `-s`: Suprime el nombre del autor y la marca de tiempo (predeterminado: _off_).
- `-e, --[no-]show-email`: Muestra correo electrónico del autor en lugar del nombre (predeterminado: _off_).
- `-w`: Ignora las diferencias de espacios blancos.
- `--[no-]ignore-rev <rev>`: Ignorar _\<rev>_ al _blaming_.
- `--[no-]ignore-revs-file <file>`: Ignorar las revisiones de _\<file>_.
- `--[no-]color-lines`: Metadatos redundantes de color de la línea anterior diferente.
- `--[no-]color-by-age`: Líneas de color por edad.
- `--[no-]minimal`: Gastar ciclos adicionales para encontrar una mejor coincidencia.
- `-S <file>`: Usa revisiones de  _\<file>_ en lugar de llamar a _git-rev-list_.
- `--[no-]contents <file>`: Usa el contenido de _\<file>_ como la imagen final.
- `-C[<score>]`: Encuentra copias de línea dentro y a través de archivos.
- `-M[<score>]`: Encuentra movimientos de línea dentro y a través de archivos.
- `-L <range>`: Procesa solo rangos de líneas definidos por \<star>, \<end> o la función: \<funcname>.
- `--[no-]abbrev[=<n>]`: Utiliza \<n> dígitos para mostrar los nombres de objetos.

Patrones útiles:

```sh
# Mostrar quién modificó cada línea de un archivo y en qué commit
git annotate <file>

# Ver la anotación de un archivo en un commit específico
git annotate <commit-hash> <file>

# Mostrar anotaciones ignorando espacios en blanco
git annotate -w <file>

# Anotar un archivo en una rama específica
git annotate <branch_name> -- <file>

# Mostrar anotaciones junto con el contenido del archivo
git annotate -p <file>
```

La salida de este comando es similar al siguiente (ejm de archivo con 5 líneas):

```
<commit_hash>        (<username>  <datetime utc>       1)file content
<commit_hash>        (<username>  <datetime utc>       2)file content
<commit_hash>        (<username>  <datetime utc>       3)file content
<commit_hash>        (<username>  <datetime utc>       4)file content
<commit_hash>        (<username>  <datetime utc>       5)file content
```
Cada fila tiene 5 componentes, los componentes 2 al 4 están entre paréntesis:
1. El primer componente son los primeros 8 caracteres del _hash_ del _commit_.
2. El segundo es el autor.
3. El tercero es la fecha y hora.
4. El cuarto es el número de línea donde del archivo.
5. El quinto es el contenido actual de la línea en el archivo.


<br/>

### _branch_

[branch](https://git-scm.com/docs/git-branch): Listar, crear o eliminar ramas.

:::{warning}
No se explican todas las opciones. Para más información ir a la documentación de _git branch_ siguiendo el link o usar `git branch -h` en la terminal.
:::

```sh
# Sintaxis de llamada (existen diversar formas de llamar el comando)
git branch [<options>] [-r | -a] [--merged] [--no-merged]
git branch [<options>] [-f] [--recurse-submodules] <branch-name> [<start-point>]
git branch [<options>] [-l] [<pattern>...]
git branch [<options>] [-r] (-d | -D) <branch-name>...
git branch [<options>] (-m | -M) [<old-branch>] <new-branch>
git branch [<options>] (-c | -C) [<old-branch>] <new-branch>
git branch [<options>] [-r | -a] [--points-at]
git branch [<options>] [-r | -a] [--format]
```
**Argumentos**
- `<start-point>`: Punto de inicio para la nueva rama, puede ser un nombre de rama, un _commit hash_ o una referencia como _HEAD_.
- `<branch-name>`: Nombre de la rama que se va a crear, eliminar o modificar.
- `<pattern>`: Patrón utilizado para filtrar ramas en los comandos que listan o buscan ramas.
- `<new-branch>`: Nombre de la nueva rama cuando se está renombrando una rama existente.
**Opciones**
- `-a, --all`: Listar todas las ramas, incluyendo las remotas.
- `-d, --delete`: Eliminar una rama local.
- `-D`: Forzar la eliminación de una rama local, incluso si no está fusionada.
- `-m, --move`: Renombrar una rama.
- `-v, --verbose`: Mostrar más información sobre cada rama.
- `-vv`: Mostrar información detallada sobre la rama y su seguimiento remoto.
- `--merged`: Listar ramas que han sido fusionadas en la actual.
- `--no-merged`: Listar ramas que no han sido fusionadas en la actual.
- `--set-upstream-to=<remoto>/<rama>`: Establecer la rama de seguimiento para la actual.

Patrones útiles:

```sh
# Listar todas las ramas locales
git branch

# Listar todas las ramas, incluyendo las remotas
git branch -a

# Crear una nueva rama sin cambiar a ella
git branch <nombre_rama>

# Crear una nueva rama basada en un commit específico
git branch <nombre_rama> <commit>

# Renombrar una rama existente
git branch -m <nombre_antiguo> <nombre_nuevo>

# Eliminar una rama local
git branch -d <nombre_rama>

# Forzar la eliminación de una rama local (si no está fusionada)
git branch -D <nombre_rama>

# Listar las ramas con su último commit asociado
git branch -v

# Ver qué ramas ya han sido fusionadas con la actual
git branch --merged

# Ver qué ramas aún no han sido fusionadas con la actual
git branch --no-merged

# Establecer la rama actual como la rama principal (upstream) de un remoto
git branch --set-upstream-to=<remoto>/<rama>

# Mostrar información detallada sobre una rama
git branch -vv
```

<br/>

### _checkout_

[checkout](https://git-scm.com/docs/git-checkout): Cambiar ramas o restaurar archivos del árbol de trabajo. Es un comando que funciona para descartar cambios que se han hecho a archivos, pero que no han sido _staged_ (para ello revisa los tutoriales).

:::{warning}
Una vez descartados los cambios no se puede deshacer esta acción.
:::

:::{warning}
No se explican todas las opciones. Para más información ir a la documentación de _git checkout_ siguiendo el link o usar `git checkout -h` en la terminal.
:::

```sh
# Sintaxis de llamada (existen diversar formas de llamar el comando)
git checkout [<options>] <branch>
git checkout [<options>] [<branch>] -- <file>...
```
**Argumentos**
- `-- <file>`: Restaurar un archivo específico a su última versión confirmada. Puede se un directorio para descartar los cambios de todos los archivos del directorio.
- `<branch>`: Cambiar a la rama especificada.
**Opciones**
- `-b <new-branch>`: Crear y cambiar a una nueva rama.
- `<commit-hash> -- <file>`: Restaurar un archivo desde un _commit_ específico.
- `-f, --force`: Forzar el cambio de rama incluso si hay cambios sin confirmar.

Patrones útiles:

```sh
# Cambiar a una rama existente
git checkout <branch>

# Crear y cambiar a una nueva rama
git checkout -b <new-branch>

# Restaurar un archivo a su última versión en el HEAD
git checkout -- <file>

# Restaurar un archivo a su versión en un commit específico
git checkout <commit-hash> -- <file>

# Cambiar a la última versión de un archivo en otra rama
git checkout <branch> -- <file>
```

<br/>

### _clean_

[clean](https://git-scm.com/docs/git-clean): Elimina archivos no rastreados (_untracked_) del árbol de trabajo. Estos son archivos que _git_ no está llevando control de su historial de cambios.

```sh
# Sintaxis de llamada
 git clean [-d] [-f] [-i] [-n] [-q] [-e <pattern>] [-x | -X] [--] [<pathspec>...]
```
**Argumentos**
- `<pathspec>`: Si se proporciona algún argumento \<pathspec>... opcional, solo se verán afectadas aquellas rutas que coincidan con _pathspec_.
**Opciones**
- `-q, --[no-]quiet`: No imprime los nombres de los archivos eliminados.
- `-n, --[no-]dry-run`: En modo _dry run_. Esto significa que el comando se ejecutará simulando los efectos que tendría, pero sin realizar cambios reales en el repositorio. En este caso enlistará los archivos _untracked_.
- `-f, --[no-]force`: Forzar la eliminación. Tener cuidado al utilizar esta opción porque una vez eliminados los archivos ya no se podrán recuperar.
- `-i, --[no-]interactive`: Limpieza interactiva.
- `-d`: Elimina directorios completos.
- `-e, --exclude <pattern>`: Agrega \<pattern> para ignorar las reglas.
- `-x`: Elimina los archivos ignorados también.
- `-X`: Elimina solo archivos ignorados.

Patrones útiles:

```sh
# Mostrar qué archivos sin seguimiento serían eliminados sin borrarlos realmente
git clean -n

# Eliminar archivos sin seguimiento en el directorio de trabajo
git clean -f

# Eliminar tanto archivos sin seguimiento como directorios sin seguimiento
git clean -fd

# Eliminar archivos sin seguimiento pero mantener los archivos ignorados
git clean -fx

# Eliminar archivos sin seguimiento, incluidos los archivos ignorados
git clean -fxd
```

<br/>

### _clone_

[clone](https://git-scm.com/docs/git-clone): Clona un repositorio en un nuevo directorio.

:::{note}
Automáticamente se creará un "_remote_" llamado "_origin_". Un _remote_ almacena información sobre el repositorio original.
:::

:::{warning}
No se explican todas las opciones. Para más información ir a la documentación de _git clone_ siguiendo el link o usar `git clone -h` en la terminal.
:::

```sh
# Sintaxis de llamada
git clone [<options>] [--] <repo> [<dir>]
```
**Argumentos Posicionales**
- `<repo>`: El repositorio (posiblemente remoto) a clonar.
- `<dir>`: Nombre del directorio donde se va a clonar.
**Opciones**
- `-v, --verbose`: Muestra más detalles sobre el proceso de `clone`.
- `--quiet`: Suprimir la salida del progreso.
- `--progress`: Forzar la visualización del progreso incluso si la salida no es un terminal.
- `--bare`: Clonar el repositorio sin un directorio de trabajo.
- `--mirror`: Clonar el repositorio como un espejo exacto, incluyendo todas las referencias.
- `-l, --local`: Usar enlaces en lugar de copiar los archivos cuando se clona en el mismo sistema de archivos.
- `--no-hardlinks`: No usar enlaces duros cuando se clona localmente.
- `--recurse-submodules[=<path>]`: Clonar también los submódulos del repositorio.
- `--depth <depth>`: Crear un clon superficial con un historial truncado a `<depth>` commits.
- `--shallow-since <date>`: Clonar un historial limitado hasta una fecha específica.
- `--shallow-exclude <revision>`: Omitir los commits alcanzables desde una revisión dada.
- `--single-branch`: Solo obtener la rama activa en el remoto.
- `--branch <name>`: Especificar una rama específica para clonar.
- `--origin <name>`: Usar un nombre personalizado en lugar de "origin" para el remoto.
- `--separate-git-dir <git-dir>`: Colocar el directorio `.git` en una ubicación diferente.
- `-o, --origin <name>`: Especificar el nombre del remoto en el repositorio clonado.
- `--filter=<filter-spec>`: Filtrar qué objetos se incluyen en la clonación para reducir el tamaño.


Patrones útiles:

```sh
# Clonar desde un remoto
git clone git://example.com/git.git/ my-dir

# Clonar local a otro directorio
git clone -l . ../copy # Directorio actual a ../copy
```

<br/>

### _commit_

[commit](https://git-scm.com/docs/git-commit): Registra cambios en el repositorio.

```sh
# Sintaxis de llamada
git commit [-a | --interactive | --patch] [-s] [-v] [-u<mode>] [--amend]
                  [--dry-run] [(-c | -C | --squash) <commit> | --fixup [(amend|reword):]<commit>)]
                  [-F <file> | -m <msg>] [--reset-author] [--allow-empty]
                  [--allow-empty-message] [--no-verify] [-e] [--author=<author>]
                  [--date=<date>] [--cleanup=<mode>] [--[no-]status]
                  [-i | -o] [--pathspec-from-file=<file> [--pathspec-file-nul]]
                  [(--trailer <token>[(=|:)<value>])...] [-S[<keyid>]]
                  [--] [<pathspec>...]
```
- **Argumentos**:
    - `<pathspec>`: Cuando se proporciona `<pathspec>` en la línea de comando, _commits_ el contenido de los archivos que coinciden con _pathspec_ sin registrar los cambios ya agregados al _staging area_.
- **Opciones Generales**:
    - `-q, --quiet`: Suprimir la salida de progreso.
    - `-v, --verbose`: Muestra más detalles sobre el proceso de `pull`.
- **Opciones del mensaje**:
    - `-F, --file <file>`: Lee el mensaje del archivo.
    - `--author <author>`: Sobreescribe el autor del _commit_.
    - `--date <date>`: Fecha de anulación del _commit_.
    - `-m, --message <message>`: Mensaje del _commit_.
    - `-c, --reedit-message <commit>`: Reutiliza y edita el mensaje del _commit_ especificado.
    - `-C, --reuse-message <commit>`: Reutiliza el mensaje del _commit_ especificado.
    - `--fixup [(amend|reword):]commit`: Utiliza el mensaje formateado de _autosquash_ para arreglar o enmendar/volver el _commit_ especificado.
    - `--squash <commit>`: Utiliza el mensaje formateado de _autosquash_ para _squash_ el _commit_ especificado.
    - `--reset-author`: El _commit_ es escrito por mí ahora (utilizado con _-C/-c/--amend_).
    - `--trailer <trailer>`: Agrega trailer personalizado(s).
    - `-s, --signoff`: Agregs un trailer firmado.
    - `-t, --template <file>`: Utiliza el archivo de plantilla especificado.
    - `-e, --edit`: Forza la edición del _commit_.
    - `--cleanup <mode>`: Indica cómo quitar los espacios y comentarios del mensaje.
    - `--status`: Incluye estado en la plantilla de mensaje de confirmación.
    - `-S, --gpg-sign[=<key-id>]`: _GPG sign commit_.
- **Opciones del contenido**:
    - `-a, --all`: _Commit_ todos los archivos cambiados.
    - `-i, --include`: Agrega archivos especificados al _staging area_ para _commit_.
    - `--interactive`: Agrega archivos interactivamente.
    - `-p, --patch`: Agrega cambios interactivos.
    - `-o, --only`: _Commit_ solo archivos especificados.
    - `-n, --no-verify`: Omite _hooks pre-commit_ y _commit-msg_.
    - `--dry-run`: Muestra lo que se hará _commit_.
    - `--short`: Muestra el estado de manera concisa.
    - `--branch`: Mostrar información de la _branch_.
    - `--ahead-behind`: Calcula valores _full ahead/behind_.
    - `--porcelain`: Salida legible por máquina.
    - `--long`: Muestra estado en formato largo (predeterminado).
    - `-z, --null`: Terminar entradas con NUL.
    - `--amend`: Corrige el _commit_ anterior. Se debe de usar inmediatamente después de haber usado hecho _commit_ en que el que cometió un error. El nuevo _commit_ debe enmendar los errores.
    - `--no-post-rewrite`: Omite _hooks post-rewrite_.
    - `-u, --untracked-files[=<mode>]`: Mostrar archivos no seguidos, modos opcionales: todos, normales, no. (Predeterminado: todo).
    - `--pathspec-from-file <file>`: Lee _pathspec_ desde un archivo.
    - `--pathspec-file-nul`: Con `--pathspec-from-file`, los elementos _pathspec_ se separan con el carácter de _NUL_.


Patrones útiles:

```sh
# Hacer commit de todo en el staging area
commit -m "my message"

# Hacer commit de todo (aunque no esté en el staging area)
git commit -a -m "my message"

# Modificar el último commit (ejm con nuevo mensaje)
git commit --amend -m "my new message"
```

<br/>

### _config_

[config](https://git-scm.com/docs/git-config): Configurar opciones de usuario y repositorio en _Git_.

:::{warning}
No se explican todas las opciones. Para más información ir a la documentación de _git config_ siguiendo el link o usar `git config -h` en la terminal.
:::

```sh
# Sintaxis de llamada (este comando tiene varios subcomandos)
git config list [<file-option>] [<display-option>] [--includes]
git config get [<file-option>] [<display-option>] [--includes] [--all] [--regexp] [--value=<value>] [--fixed-value] [--default=<default>] <name>
git config set [<file-option>] [--type=<type>] [--all] [--value=<value>] [--fixed-value] <name> <value>
git config unset [<file-option>] [--all] [--value=<value>] [--fixed-value] <name>
git config rename-section [<file-option>] <old-name> <new-name>
git config remove-section [<file-option>] <name>
git config edit [<file-option>]
git config [<file-option>] --get-colorbool <name> [<stdout-is-tty>]
```
**Argumentos**
- `<file-option>`: Representa una opción relacionada con el archivo. Puede hacer referencia a un archivo específico dentro de un comando, como al aplicar cambios en un archivo o especificar archivos para su manipulación.
- `<display-option>`: Hace referencia a una opción que controla cómo se muestra la salida o la información en la terminal. Esto puede incluir opciones como colores, formato o el tipo de visualización de los datos.
- `<name>`: Es un marcador de posición que representa un nombre en los comandos. Puede referirse a un nombre de usuario, nombre de una rama, nombre de un archivo, o cualquier otro identificador relevante para el comando.
- `<value>`: Representa un valor asociado con una configuración o argumento. El valor puede ser un dato específico que se asigna a una clave, como un correo electrónico, un número o un texto.
- `<old-name>`: Se refiere al nombre original o antiguo de un archivo, una rama o cualquier entidad que esté siendo modificada o renombrada en un comando.
- `<new-name>`: Hace referencia al nuevo nombre que se asignará a un archivo, rama u otra entidad cuando se cambie o renombre.
- `<stdout-is-tty>`: Indica una opción o argumento relacionada con la salida estándar de la terminal (stdout). Este argumento suele usarse para controlar si la salida está o no formateada para una terminal interactiva.
**Opciones**
- `--global`: Aplica la configuración a nivel global para el usuario.
- `--local`: Aplica la configuración solo al repositorio actual.
- `--system`: Aplica la configuración a nivel de sistema para todos los usuarios.
- `--list`: Muestra todas las configuraciones actuales.
- `--unset <key>`: Elimina una configuración específica.
- `--get <key>`: Obtiene el valor de una configuración específica.
- `--replace-all <key> <value>`: Reemplaza todas las ocurrencias de una clave con un nuevo valor.
- `--add <key> <value>`: Añade una nueva configuración sin sobrescribir valores existentes.
- `--edit`: Abre el archivo de configuración en un editor de texto.

Patrones útiles:

```sh
# Configurar el nombre de usuario globalmente
git config --global user.name "Tu Nombre"

# Configurar el correo electrónico globalmente
git config --global user.email "tu@email.com"

# Ver todas las configuraciones actuales
git config --list

# Obtener un valor específico de configuración
git config user.name

# Establecer un editor de texto predeterminado para los mensajes de commit
git config --global core.editor "vim"

# Configurar la rama predeterminada al clonar un repositorio
git config --global init.defaultBranch main

# Habilitar colores en la salida de Git
git config --global color.ui auto

# Configurar credenciales para no pedir autenticación cada vez
git config --global credential.helper cache

# Configurar un alias para un comando más corto
git config --global alias.st status

# Eliminar una configuración específica
git config --global --unset user.name
```

<br/>

### _diff_

[diff](https://git-scm.com/docs/git-diff): Muestra diferencias entre _commits_, entre un _commit_ y el árbol de trabajo, etc.

:::{warning}
No se explican todas las opciones. Para más información ir a la documentación de _git pull_ siguiendo el link o usar `git pull -h` en la terminal.
:::

```sh
# Sintaxis de llamada
git diff --no-index [<options>] <path> <path>
```
**Argumentos**
- `<path>`: Cuando se indica, se utiliza para limitar la diferencia a las rutas indicadas (ya sean archivos o directorios).
**Opciones**
- `--cached, --staged`: Comparar los cambios preparados para _commit_con el último commit.
- `--stat`: Mostrar un resumen de las diferencias en lugar del contenido completo.
- `--name-only`: Listar solo los nombres de los archivos modificados.
- `--name-status`: Mostrar los archivos modificados junto con su estado (`A`=Added, `M`=Modified, `D`=Deleted).
- `--word-diff`: Mostrar diferencias palabra por palabra en lugar de línea por línea.
- `--color`: Mostrar diferencias con colores.
- `--no-color`: Deshabilitar los colores en la salida.
- `--ignore-space-change, -b`: Ignorar cambios en espacios en blanco.
- `--ignore-all-space, -w`: Ignorar todos los cambios en espacios en blanco.
- `--ignore-blank-lines`: Ignorar líneas en blanco en la comparación.
- `--diff-filter=[ACDMRTUXB]`: Filtrar por tipo de cambio (A=Added, C=Copied, D=Deleted, M=Modified, etc.).
- `-U<n>`: Mostrar `n` líneas de contexto alrededor de los cambios.

Patrones útiles:

```sh
# Ver cambios en el área de trabajo
git diff

# Comparar cambios preparados para commit con el último commit
git diff --staged

# Ver solo los nombres de los archivos modificados
git diff --name-only

# Ignorar cambios en espacios en blanco
git diff -w

# Ver cambios en un directorio/archivo específico
git diff path/to/filename.ext

# Comparar cambios entre dos ramas específicas
git diff main feature-branch

# Comparar cambios entre dos commits especificos
git diff hash1 hash2
git diff HEAD HEAD~1
```
- Si se van a comparar dos _commits_ pueden ser los primeros caracteres del _hash_ o _shorcuts_ como _HEAD_. Al usar _HEAD_ tener en cuenta:
    - _HEAD_ Último _commit_/_commit_ actual.
    - _HEAD^_ o _HEAD~1_: _Commit_ anterior a _HEAD_, penúltimo _commit_.
    - _HEAD~2_: _Commit_ anterior a _HEAD~1_, antepenúltimo _commit_.
    - _HEAD~n_: _n_ commits atrás, en relación con el _commit_ actual (_HEAD_).
    - _HEAD^n_: _n-ésimo_ padre de _HEAD_.

Ejemplo:

Si se tiene un repositorio de _git_, con un único archivo `my_triangle.yml`, al cual previamente ya se le hizo _commit_. Si el contenido del archivo es el siguiente:

```yaml
name: triangle
sides: 3
kinds_by_sides:
    - equilateral
    - isoceles
    - scalene
    - acute
```

Y posteriormente se elimina la línea _- acute_ y se usa el comando `git diff`. Entonces la salida del comando sería similar a la siguiente:
```sh
diff --git a/my_triangle.yml b/my_triangle.yml
index <hash_del_commit>..<hash_actual> <modo_del_archivo>
--- a/my_triangle.yml
+++ b/my_triangle.yml
@@ -4,4 +4,3 @@ kinds_by_sides:
     - equilateral
     - isoceles
     - scalene
-    - acute
```
- `diff --git a/tu_archivo.yml b/tu_archivo.yml`: Indica que se está viendo las diferencias entre dos versiones del archivo "my_triangle". "a" representa la versión original (_commit_) y "b" representa la versión modificada.
- `index <hash_del_commit>..<hash_actual> <modo_del_archivo>`: Muestra los _hashes_ (identificadores únicos) de las versiones del archivo y el modo del archivo (permisos).
- `--- a/tu_archivo.yml`: Indica el inicio de la sección de diferencias para la versión original.
- `+++ b/tu_archivo.yml`: Indica el inicio de la sección de diferencias para la versión modificada.
- `@@ -4,4 +4,3 @@`: Es el "_hunk header_". Significa:
    - `-4,4`: En la versión original, la sección de cambios comienza en la línea 4 y abarca 4 líneas.
    - `+4,3`: En la versión modificada, la sección de cambios comienza en la línea 4 y abarca 3 líneas.
- `- - acute`: La línea que se ha eliminado está precedida por un signo menos (-). En caso de que se hubiera agregado una línea aparecía con un `+`.

<br/>

### _init_

[init](https://git-scm.com/docs/git-init): Crea un repositorio _Git_ vacío o reinicializa uno existente.

:::{warning}
No se debe de crear un repositorio dentro de otro repositorio.
:::

```sh
# Sintaxis de llamada
git init [-q | --quiet] [--bare] [--template=<template-directory>]
                [--separate-git-dir <git-dir>] [--object-format=<format>]
                [-b <branch-name> | --initial-branch=<branch-name>]
                [--shared[=<permissions>]] [<directory>]
```
**Argumentos**
- `<directory>`: Nombre del directorio. Si no se indica se utiliza el directorio actual como repositorio.
**Opciones**
- `--template <template-directory>`: Directorio desde el cual se utilizarán las plantillas.
- `--bare`: Crear un repositorio _bare_.
- `--shared[=<permissions>]`: Especifica que el repositorio de _git_ se comparta entre varios usuarios.
- `-q, --quiet`: Modo silencioso.
- `--separate-git-dir <gitdir>`: directorio de git separado del árbol de trabajo.
- `-b, --initial-branch <name>`: Sobreescribe el nombre de la rama inicial.
- `--object-format <hash>`: Especifica el algoritmo hash para usar.

Patrones útiles:

```sh
# Inicializar un repositorio de git
git init
```

<br/>

### _log_

[log](https://git-scm.com/docs/git-log): Muestra el historial de los registros de _commits_. Muestra los _commits_ más recientes primero, para navegar en el _output_ usar espacio para ir más abajo o _q_ para salir.

```sh
# Sintaxis de llamada
git log [<options>] [<revision-range>] [[--] <path>...]
```
**Argumentos**
- `<path>`: Directorio o archivo específico. En caso de que se un directorio solo mostrará el historial del directorio como tal, no de sus archivos. Se pueden especificar más de uno.
**Opciones**
- `-q, --quiet`: Suprimir la salida DIFF.
- `--source`: Muestra la fuente.
- `--use-mailmap`: Usa archivo _mail map_.
- `--mailmap`: Alias de `--use-mailmap`.
- `--clear-decorations`: Borra todos los filtros de decoración previamente definidos.
- `--decorate-refs <pattern>`: Solo decora las referencias que coinciden con _\<pattern>_.
- `--decorate-refs-exclude <pattern>`: No decora las referencias que coincidan con _\<pattern>_.
- `--decorate[=...]`: Decorar opciones.
- `-L <range:file>`: Rastrea la evolución del rango de línea _\<star>, \<End>_ o _function_: _\<funcname> en \<file>_.

Patrones útiles:

```sh
# Ver log de 
git log

# Ver log de directorio/archivo
git log path/to/dir

# Limitar a n commits
git log -n # n es un número, no la letra n

# Mostrar historial desde determinada fecha
git log --since=<date>
```
- En `--since` _\<date>_ puede ser una fecha como _YYYY/MM/DDD_ o también se pueden usar cadenas como "2 weeks ago".

El resultado de este comando es similar al siguiente (uno por cada _commit_):
```
commit <hash> (<commit> -> <branch>)
Author: <username> <user email>
Date:   <date time utc>

    <commit message>
```
- La primer línea contiene el _hash_ e información del _commit_.
- La siguiente línea contiene información de quién hizo el _commit_.
- Posteriormente se muestra información sobre cuándo se hizo el _commit_.
- Finalmente se muestra el mensaje que se agregó al realizar el _commit_.


<br/>

### _merge_

[merge](https://git-scm.com/docs/git-merge): Une dos o más historiales de desarrollo. Comando utilizado para hacer _merge_ de _branches_. Los cambios de _source_ los aplicará a _destination_. El resultado es un _commit_ en _destination_ que incluye todo de _source_.

:::{warning}
No se explican todas las opciones. Para más información ir a la documentación de _git merge_ siguiendo el link o usar `git merge -h` en la terminal.
:::

```sh
# Sintaxis de llamada
git merge [<options>] [<commit>...]
git merge --abort
git merge --continue
```
**Argumentos**
- `<commit>`: Representa el identificador de una o varias ramas o commits específicos que se desean fusionar en la rama actual.
**Opciones**
- `--no-ff`: Forzar un _commit_ de fusión incluso si se puede hacer fast-forward.  
- `--ff-only`: Solo permitir una fusión si se puede hacer fast-forward; de lo contrario, abortar.  
- `--no-commit`: No hacer un _commit_ automático después de la fusión.  
- `--abort`: Cancelar la fusión y restaurar el estado anterior.  
- `--continue`: Continuar el proceso de fusión después de resolver conflictos.  
- `--squash`: Combinar los cambios sin crear un _commit_ de fusión automático.  
- `--strategy=<estrategia>`: Especificar la estrategia de fusión (ej. `recursive`, `ort`).  
- `--strategy-option=<opción>`: Pasar opciones a la estrategia de fusión (ej. `ours`, `theirs`).  
- `-m <mensaje>`: Especificar un mensaje de _commit_ personalizado para la fusión.  
- `--log`: Incluir mensajes de _commit_ en el _commit_ de fusión.  
- `--quiet`: Suprimir la salida de información durante la fusión.  
- `--verbose`: Mostrar detalles adicionales durante la fusión.  
- `--verify-signatures`: Verificar firmas GPG de los commits antes de fusionar.  
- `--allow-unrelated-histories`: Permitir fusionar repositorios sin historial común. 

:::{caution}
Si la misma línea del mismo archivo se modificó en dos _branches_ distintos que posteriormente se trantan se unir, entonces se creará un conflicto y no se podrá hacer el _merge_. Si ocurre un conflicto y posterioremente  se utiliza `git status` se indicarará cuáles archivos están en conflicto.
:::

Patrones útiles:

```sh
# Fusionar una rama en la actual
git merge <branch_destination>

# Fusionar una rama en una rama específica
git merge <branch_source> <branch_destination>

# Fusionar una rama en la actual sin hacer un commit automático
git merge --no-commit <branch>

# Fusionar una rama en la actual sin hacer un merge commit (fast-forward si es posible)
git merge --ff-only <branch>

# Fusionar una rama en la actual con un commit de combinación incluso si se puede hacer fast-forward
git merge --no-ff <branch>

# Abortar un merge en caso de conflictos
git merge --abort

# Continuar un merge después de resolver conflictos
git merge --continue
```

### _pull_

[pull](https://git-scm.com/docs/git-pull): Descarga e integra cambios desde otro repositorio o rama local y los une al _branch_ actual (activo) del repositorio.

:::{warning}
No se explican todas las opciones. Para más información ir a la documentación de _git pull_ siguiendo el link o usar `git pull -h` en la terminal.
:::

```sh
# Sintaxis de llamada
git pull [<options>] [<repository> [<refspec>...]]
```
**Argumentos**
- `<repository>`: El repositorio "remoto" que es la fuente de una operación de búsqueda o extracción.
- `<refspec>`: Especifica qué referencias buscar y qué referencias locales actualizar.
**Opciones**
- `--rebase[=<mode>]`: En lugar de hacer un merge, aplicar los commits en la parte superior de la rama actual. `<mode>` puede ser `false`, `true`, `interactive`, etc.
- `--no-rebase`: Deshabilitar la rebase automática al hacer `pull`.
- `--ff-only`: Solo avanzar si se puede hacer un fast-forward, sin crear commits de merge.
- `--no-ff`: Forzar un _commit_ de merge incluso si es posible un fast-forward.
- `--commit`: Crear un _commit_ automáticamente después de la fusión (por defecto).
- `--no-commit`: No crear un _commit_ automáticamente después de la fusión.
- `--squash`: Fusionar cambios remotos en un solo _commit_ en lugar de múltiples commits.
- `--no-squash`: Deshabilitar la fusión en un solo commit.
- `-q, --quiet`: Suprimir la salida de progreso.
- `-v, --verbose`: Muestra más detalles sobre el proceso de `pull`.
- `--all`: Recuperar y fusionar cambios de todos los remotos configurados.
- `--tags`: Incluir etiquetas en la actualización desde el remoto.
- `-f, --force`: Forzar la actualización del contenido local incluso si hay cambios locales.
- `--depth <depth>`: Hacer una descarga superficial con un historial truncado a `<depth>` commits.
- `--update-shallow`: Actualizar un repositorio superficial con más historial.
- `--allow-unrelated-histories`: Permitir fusionar historiales no relacionados.
- `-r, --recurse-submodules[=<mode>]`: Actualizar también los submódulos al hacer `pull`. `<mode>` puede ser `yes`, `no`, `on-demand`.

Patrones útiles:

```sh
# Actualizar branches desde el repositorio remoto
git pull

# Merge actualización con en el branch actual
git pull origin
```

<br/>

### _push_

[push](https://git-scm.com/docs/git-push): Actualizar referencias remotas junto con los objetos asociados.

:::{warning}
Para prevenir sobreescibir archivos en el repositorio remoto, primero se debe de hacer _pull_ y después _push- (es decir, si ocurrieron cambios en el remoto, mientras se hacían cambios localmente y después se trata de hacer _push_ de esos cambios no se podrá, hasta que se actualice el repositorio con _pull_).
:::

:::{warning}
No se explican todas las opciones. Para más información ir a la documentación de _git pull_ siguiendo el link o usar `git pull -h` en la terminal.
:::

```sh
# Sintaxis de llamada
git push [<options>] [<repository> [<refspec>...]]
```
**Argumentos**
- `<repository>`: El repositorio "remoto" que es la fuente de una operación de búsqueda o extracción.
- `<refspec>`: Especifica qué referencias buscar y qué referencias locales actualizar.
**Opciones**
- `--rebase[=<mode>]`: En lugar de hacer un merge, aplicar los commits en la parte superior de la rama actual. `<mode>` puede ser `false`, `true`, `interactive`, etc.
- `--no-rebase`: Deshabilitar la rebase automática al hacer `pull`.
- `--ff-only`: Solo avanzar si se puede hacer un fast-forward, sin crear commits de merge.
- `--no-ff`: Forzar un _commit_ de merge incluso si es posible un fast-forward.
- `--commit`: Crear un _commit_ automáticamente después de la fusión (por defecto).
- `--no-commit`: No crear un _commit_ automáticamente después de la fusión.
- `--squash`: Fusionar cambios remotos en un solo _commit_ en lugar de múltiples commits.
- `--no-squash`: Deshabilitar la fusión en un solo commit.
- `-q, --quiet`: Suprimir la salida de progreso.
- `-v, --verbose`: Muestra más detalles sobre el proceso de `pull`.
- `--all`: Recuperar y fusionar cambios de todos los remotos configurados.
- `--tags`: Incluir etiquetas en la actualización desde el remoto.
- `-f, --force`: Forzar la actualización del contenido local incluso si hay cambios locales.
- `--depth <depth>`: Hacer una descarga superficial con un historial truncado a `<depth>` commits.
- `--update-shallow`: Actualizar un repositorio superficial con más historial.
- `--allow-unrelated-histories`: Permitir fusionar historiales no relacionados.
- `-r, --recurse-submodules[=<mode>]`: Actualizar también los submódulos al hacer `pull`. `<mode>` puede ser `yes`, `no`, `on-demand`.

Patrones útiles:

```sh
# Subir cambios al remoto de la rama actual
git push

# Subir cambios a un remoto origin y rama específica
git push origin main

# Subir cambios a la rama del mismo nombre que la actual en el remoto
git push origin HEAD
```

<br/>

### _remote_

[remote](https://git-scm.com/docs/git-remote): Gestionar repositorios remotos.

:::{warning}
No se explican todas las opciones ni subcomandos. Para más información ir a la documentación de _git remote_ siguiendo el link o usar `git remote -h` en la terminal.
:::

```sh
# Sintaxis de llamada (Existen varios subcomandos)
git remote [-v | --verbose]
git remote add [-t <branch>] [-m <master>] [-f] [--tags | --no-tags] [--mirror=<fetch|push>] <name> <url>
git remote rename [--[no-]progress] <old> <new>
git remote remove <name>
git remote set-head <name> (-a | --auto | -d | --delete | <branch>)
git remote [-v | --verbose] show [-n] <name>
git remote prune [-n | --dry-run] <name>
git remote [-v | --verbose] update [-p | --prune] [(<group> | <remote>)...]
git remote set-branches [--add] <name> <branch>...
git remote get-url [--push] [--all] <name>
git remote set-url [--push] <name> <newurl> [<oldurl>]
git remote set-url --add <name> <newurl>
git remote set-url --delete <name> <url>
```
**Argumentos**
- `-v, --verbose`: Ser más detallado.

Patrones útiles:

```sh
# Enlistar remotos
git remote

# Agrega remote
git remote add remote_name git://example.com/git.git/

# Imitar clone, pero hacer track de ramas específicas
git remote add -f -t branch_name -m master_name remote_name git://example.com/git.git/

# Remover remote
git remote remove remote_name
```

<br/>

### _reset_

[reset](https://git-scm.com/docs/git-reset): Restablece el `HEAD` actual al estado especificado. Deshace la acción de agregar un archivo al _staging area_ (_unstaged_), es decir elimina el archivo del _staging area_.

```sh
# Sintaxis de llamada (existen varias)
git reset [--mixed | --soft | --hard | --merge | --keep] [-q] [<commit>]
git reset [-q] [<tree-ish>] [--] <pathspec>...
git reset [-q] [--pathspec-from-file [--pathspec-file-nul]] [<tree-ish>]
git reset --patch [<tree-ish>] [--] [<pathspec>...]
```
**Argumentos**
En las últimas tres formas, copia las entradas de `<tree-ish>` al _staging ara_. En la primer froma, establece la cabecera de la rama actual (_HEAD_) a `<commit>`, modificando opcionalmente el _staging area_ y el árbol de trabajo para que coincidan. El valor predeterminado de `<tree-ish>`/`<commit>` es _HEAD_ en todas las formas.
**Opciones**
- `-q, --quiet`: Suprimir la salida de progreso.
- `--no-refresh`: Omite refrescarse el _staging area_ después del reinicio.
- `--mixed`: Restablece _HEAD_ y el _staging area_.
- `--soft`: Restablece solo _HEAD_.
- `--hard`: Restablece _HEAD_, el _staging area_ y el árbol de trabajo.
- `--merge`: Restablece _HEAD_, el _staging area_ y el árbol de trabajo.
- `--keep`: Restablece _HEAD_, pero mantiene los cambios locales.
- `--recurse-submodules[=<reset>]`: Controla la actualización recursiva de submódulos.
- `-p, --patch`: Selecciona _hunks_ de manera interactiva.
- `-N, --intent-to-add`: Registra solo la intención de que se agregarán rutas eliminadas más tarde.
- `--pathspec-from-file <file>`: Lee _pathspec_ desde un archivo.
- `--pathspec-file-nul`: Con `--pathspec-from-file`, los elementos _pathspec_ se separan con el carácter de _NUL_.

Patrones útiles:

```sh
# Deshacer todos los últimos cambios en el staging area
git reset HEAD

# Deshacer los últimos cambios en un archivo específico
git reset HEAD path/to/file.ext

# Deshacer último commit pero mantener cambios en el staging area
git reset --soft HEAD~1

# Deshacer último commit y deshacer cambios en el staging area
git reset --mixed HEAD~1

# Retornar a un commit específico (deshaciendo cambios posteriores)
git reset --hard <hash_del_commit>
```
- Al usar _HEAD_ tener en cuenta:
    - _HEAD_ último _commit_, último _commit_/_commit_ actual.
    - _HEAD^_ o _HEAD~1_: _Commit_ anterior a _HEAD_, penúltimo _commit_.
    - _HEAD~2_: _Commit_ anterior a _HEAD~1_, antepenúltimo _commit_.
    - _HEAD~n_: _n_ commits atrás, en relación con el _commit_ actual (_HEAD_).
    - _HEAD^n_: _n-ésimo_ padre de _HEAD_.

<br/>

### _rm_

[rm](https://git-scm.com/docs/git-rm): Elimina archivos del árbol de trabajo y del _staging area_.

```sh
git rm [-f | --force] [-n] [-r] [--cached] [--ignore-unmatch]
              [--quiet] [--pathspec-from-file=<file> [--pathspec-file-nul]]
              [--] [<pathspec>...]
```
**Argumentos**
- `<pathspec>`: Si se proporciona algún argumento \<pathspec>... opcional, solo se verán afectadas aquellas rutas que coincidan con _pathspec_.
**Opciones**
- `-n, --[no-]dry-run`: carrera seca.
- `-q, --[no-]quiet`: No enumera archivos eliminados.
- `--[no-]cached`: Solo elimina del _staging area_.
- `-f, --[no-]force`: Anula la verificación actualizada.
- `-r`: Permitir la eliminación recursiva.
- `--[no-]ignore-unmatch`: Salir con un estado cero incluso si no coincide con nada.
- `--[no-]sparse`: Permitir entradas de actualización fuera del cono de verificación escasa.
- `--[no-]pathspec-from-file <file>`: Leer _pathspec_ desde el archivo.
- `--[no-]pathspec-file-nul`: Con `--pathspec-from-file`, los elementos de _pathspec_ se separan con el carácter de _NUL_.

Patrones útiles:

```sh
# Eliminar un archivo del repositorio y del sistema de archivos
git rm <file>

# Eliminar varios archivos a la vez
git rm <file1> <file2> ...

# Eliminar un directorio y todo su contenido del repositorio y del sistema de archivos
git rm -r <directory>

# Eliminar un archivo solo del repositorio pero mantenerlo en el sistema de archivos
git rm --cached <file>

# Eliminar todos los archivos que coincidan con un patrón (ej. eliminar todos los archivos .log)
git rm *.log

# Forzar la eliminación de un archivo que ha sido modificado sin hacer commit
git rm -f <file>
```
- `*` funcionar como un _wildcard_ y se puede combinar con cualquier patrón para buscar archivos/directorios que tengan determinados patrones en sus nombres.

Al mostrar la información de un _commit_, el resultado de este comando es similar una combinación de `git log` y `git diff` (ver cada comando para entender el _output_):
```
commit <hash> (<commit> -> <branch>)
Author: <username> <user email>
Date:   <date time utc>

    <commit message>

diff --git a/my_triangle.yml b/my_triangle.yml
index <hash_del_commit>..<hash_actual> <modo_del_archivo>
--- a/my_triangle.yml
+++ b/my_triangle.yml
@@ -4,4 +4,3 @@ kinds_by_sides:
     - equilateral
     - isoceles
     - scalene
-    - acute
```
- La primer línea contiene el _hash_ e información del _commit_.
- La siguiente línea contiene información de quién hizo el _commit_.
- Posteriormente se muestra información sobre cuándo se hizo el _commit_.
- Finalmente se muestra el mensaje que se agregó al realizar el _commit_.
- `diff --git a/tu_archivo.yml b/tu_archivo.yml`: Indica que se está viendo las diferencias entre dos versiones del archivo "my_triangle". "a" representa la versión original (_commit_) y "b" representa la versión modificada.
- `index <hash_del_commit>..<hash_actual> <modo_del_archivo>`: Muestra los _hashes_ (identificadores únicos) de las versiones del archivo y el modo del archivo (permisos).
- `--- a/tu_archivo.yml`: Indica el inicio de la sección de diferencias para la versión original.
- `+++ b/tu_archivo.yml`: Indica el inicio de la sección de diferencias para la versión modificada.
- `@@ -4,4 +4,3 @@`: Es el "_hunk header_". Significa:
    - `-4,4`: En la versión original, la sección de cambios comienza en la línea 4 y abarca 4 líneas.
    - `+4,3`: En la versión modificada, la sección de cambios comienza en la línea 4 y abarca 3 líneas.
- `- - acute`: La línea que se ha eliminado está precedida por un signo menos (-). En caso de que se hubiera agregado una línea aparecía con un `+`.

<br/>

### _show_

[show](https://git-scm.com/docs/git-show): Muestra información de varios tipos de objetos.

```sh
# Sintaxis de llamada
git show [<options>] <object>...
```
**Argumentos**
- `<object>`: Los nombres de los objetos a mostrar (predeterminado _HEAD_).
**Opciones**
- `--pretty[=<format>], --format=<format>`: Imprime, en formato _pretty_, el contenido de los registros de confirmación en un formato dado, donde _\<format>_ puede ser uno _oneline, short, medium, full, fuller, reference, email, raw, format:\<string>_ y _tformat_.
- `--abbrev-commit`: En lugar de mostrar el nombre completo hexadecimal de 40 bytes del objeto _commit_, muestra un prefijo que nombra al objeto de manera única.
- `--no-abbrev-commit`: Muestra el nombre completo hexadecimal de 40 bytes del objeto _commit_.
- `--oneline`: Es es un _shorthand_ para `--pretty=oneline --abbrev-commit`, cuando se utilizan juntos.
- `--encoding=<encoding>`: Los objetos de _commit_ registran la codificación de caracteres utilizada para el mensaje de registro en su encabezado de codificación.
- `--expand-tabs=<n>, --expand-tabs, --no-expand-tabs`: Realiza una expansión de tabulación (reemplaza cada tabulación con suficientes espacios para completar la siguiente columna de visualización que sea un múltiplo de \<n>) en el mensaje de registro antes de mostrarlo en la salida
- `--notes[=<ref>]`: Muestra las notas que anotan la confirmación al mostrar el mensaje de registro de confirmación.
- `--no-notes`: No muestra notas.
- `--show-notes-by-default`: Muestra las notas predeterminadas a menos que se dan opciones para mostrar notas específicas.
- `--show-signature`: Verifica la validez de un objeto _commit_ firmado pasando la firma a `gpg --verify` y mostrar la salida.

Patrones útiles:

```sh
# Mostrar los cambios y metadatos del último commit
git show

# Mostrar los cambios de un commit específico
git show <commit-hash>

# Ver los cambios de un archivo específico en un commit
git show <commit-hash> -- <archivo>

# Mostrar información de una etiqueta
git show <tag-name>

# Ver la diferencia entre dos commits
git show <commit-hash1>..<commit-hash2>
```


<br/>

### _status_

[status](https://git-scm.com/docs/git-status): Muestra el estado del árbol de trabajo. Entre la información que retorna está:
- "_Changes to be commited_": Archivos en el _staging area_ que se han modificado desde la última vez.
- "_Changes not staged for commit_": Archivos que se han modificado, pero no están en el _staging area_.
- "_Untracked files_": Archivos a los cuales _git_ no les está dando un seguimiento. Para darle un seguimiento a un archivo se debe de Agrega al _staging area_, con el comando `git add`.

```sh
# Sintaxis de llamada
git status [<options>] [--] [<pathspec>...]
```
**Argumentos**
- `<pathspec>`: Si se proporciona algún argumento \<pathspec>... opcional, solo se verán afectadas aquellas rutas que coincidan con _pathspec_.
**Opciones**
- `-v, --verbose`: Ser detallado.
- `-s, --short`: Muestra el estado de manera concisa.
- `-b, --branch`: Muestra información de la _branch_.
- `--show-stash`: Muestra información de _stash_.
- `--ahead-behind`: Calcula por adelantado/detrás de los valores.
- `--porcelain[=<version>]`: Salida legible por máquina.
- `--long`: Muestra estado en formato largo (predeterminado).
- `-z, --null`: Termina entradas con NUL.
- `-u, --untracked-files[=<mode>]`: Muestra archivos no seguidos, modos opcionales: _all, normal, no_. (Default: _all_)
- `--ignored[=<mode>]`: Muestra archivos ignorados, modos opcionales: _traditional, matching, no_. (Default: _traditional_)
- `--ignore-submodules[=<when>]`: Ignora los cambios en los submódulos, opcional cuando: _all, dirty, untracked_. (Default: _all_)
- `--column[=<style>]`: Enumera archivos sin seguimiento en columnas.
- `--no-renames`: No detecta renombes.
- `-M, --find-renames[=<n>]`: Detectar renombes, opcionalmente establece un índice de similitud.

Patrones útiles:

```sh
# Imprimir estatus del repositorio
git status
```

<br/>

## HEAD

_HEAD_ en _Git_ es un puntero especial que indica cuál es el _commit_ actual. Es esencialmente un marcador que apunta a la última confirmación en la rama actual en la que se está trabajando. Características principales:
- _HEAD_ normalmente apunta al último _commit_ de la rama actual.
- Cuando se cambia de rama con `git checkout`, _HEAD_ se mueve para apuntar al último _commit_ de la nueva rama.
- _HEAD_ es la referencia que _Git_ usa para saber qué archivos mostrar en el directorio de trabajo

Al utilizar _HEAD_ se puede hacer referencia a _commits_ anteriores en relación con el último _commit_:
- _HEAD_: El útlimo _commit_ en la rama actual.
- _HEAD~1_ o _HEAD~_: El _commit_ anterior a _HEAD_.
- _HEAD~2_: Dos _commits_ antes de _HEAD_.
- _HEAD~n_: _n commits_ antes de _HEAD_.
- _HEAD^_: El primer padre de _HEAD_ (útil en fusiones que tienen múltiples padres)
- _HEAD^2_: El segundo padre de _HEAD_ (en una fusión)
- _HEAD^n_: El n-ésimo padre de _HEAD_ (en una fusión)

Algunos ejemplos de comandos con los que se pueden usar _HEAD_:
```sh
# Ver a qué commit apunta HEAD
git show HEAD

# Ver los cambios entre el directorio de trabajo y HEAD
git diff HEAD

# Deshacer cambios en el directorio de trabajo y volver al estado de HEAD
git reset --hard HEAD

# Mover HEAD a un commit específico (detached HEAD)
git checkout abc123def

# Revertir el último commit manteniendo los cambios en el directorio de trabajo
git reset HEAD~1
```

A continuacion se enlistan algunos casos de usos común de _HEAD_:

```sh
# Comparar cambios
git diff HEAD              # Diferencias entre directorio de trabajo y último commit
git diff HEAD~1 HEAD       # Diferencias entre penúltimo y último commit

# Revertir cambios
git reset --soft HEAD~1    # Deshacer último commit manteniendo cambios preparados
git reset --mixed HEAD~1   # Deshacer último commit manteniendo cambios sin preparar
git reset --hard HEAD~1    # Deshacer último commit descartando cambios

# Examinar versiones antiguas
git checkout HEAD~3        # Ir a un estado anterior (detached HEAD)
git checkout -             # Volver a donde estabas

# Guardar referencia a un commit
git tag v1.0 HEAD          # Crear una etiqueta en el commit actual

# Recuperar archivos eliminados
git checkout HEAD -- archivo_eliminado.txt

# Descartar cambios en un archivo específico
git checkout HEAD -- archivo_modificado.txt
```

<br/>

## _README_

Es un documento que se puede poner en un repositorio de _GitHub_ para indicar a otras personas las características del proyecto y cualquier otra cosa que se quiera compartir. Generalemnte es un archivo _markdown_ (`.md`). Algunas secciones que podría tener un archivo _README_ son:
- Información del proyecto. Una explicación específica del proyecto.
- Indicar cómo instalar (si aplica).
- Indicar los requisitos (si aplica).
- Indicar cómo usarlo (si aplica). Solo indicar los más indispensable.
- Indicar ejemplos (si aplica).
- Licencias.
- Indicar cómo contruibuir con el proyecto.

<br/>

---
## _.gitignore_

Es un archivo especial que se coloca en el _root directory_ del repositorio para indicar patrones con _wildcards_ que representen nombres de archivos que _git_ debe de ignorar. Por ejemplo si _.gitignore_ contiene:

```yaml
build
*.mpl
```

Entonces _git_ ignorará todos los archivos y carpetas que se llamen estrictamente "_build_" o que tengan la extensión "_.mpl_". Si el nombre de un directorio coincide con un patrón entonces se ignorará todo el contenido de este.

<br/>

## Tutoriales

### Deshacer el último cambio hecho a un archivo que ya ha sido _staged_

Es necesario usar dos comandos:

```sh
# Deshacer cambios de archivo staged
git reset HEAD path/filename
git checkout -- path/filename
```
- Se debe de usar `--` para separar el comando _checkout_ del nombre del archivos o archivos.

### Crear un un _.gitignore_

_.gitignore_ es un archivo que se puede crear para indicar archivos que _git_ debe de ignorar, dentro del archivo se deben de poner los nombres de los archivos que _git_ debe de ignorar.
- Una forma de crear el archivo es usando el comando: <br/> `echo file_name >> .gitignore`
- De estar forma el archivo se creará y además añadirá el archivo _file_name_. En lugar de un archivo puede ser un directorio.
- Para añadir más archivos se utiliza el mismo comando: <br/> `echo file_name >> .gitignore`

### Hacer carpeta un repositorio y hacer _push_ a un repositorio remoto

1. Primero se debe de convertir el poyecto en repositorio con el comando `git init`, para ello se debe estar dentro de la carpeta principal del proyecto en la terminal.
2. Opcionalmente se puede excluir archivos indicándolos en un archivo _.gitignore_.
3. Se puede revisar el estatus de _git_ con `git status`.
4. Poner los archivos en el _staging area_ con `git add `.
5. Opcionalmente se puede remover archivos del _staging area_ con `git rm filename`.
6. Hacer _commit_ de los archivos en el _staging area_ para hacer version control en ellos usando `git commit -m "message"`.
7. Usar los siguientes comandos:
    - `git remote add origin https://github.com/username/repository_name.git`
    - `git branch -M main`
    - `git push -u origin main`

