# _conda_

Conda es un gestor de paquetes y entornos que permite instalar, actualizar y administrar dependencias de software de manera eficiente, especialmente en proyectos de ciencia de datos y desarrollo. Funciona con múltiples lenguajes de programación, incluyendo Python y R, y facilita la creación de entornos aislados para evitar conflictos entre paquetes. Usualmente _conda_ se instala al instalar [Anaconda](https://www.anaconda.com/docs/main), [Miniconda](https://www.anaconda.com/docs/getting-started/miniconda/main) o [Miniforge](https://conda-forge.org/docs/):

Para esta sección tener en cuenta las siguientes definiciones:
- **Channels**: Los paquetes se instalan desde un _Channel_, que es como una liga a la nube de _Anaconda_ donde se almacenan los paquetes, por default es el channel ‘_main’_, pero existen muchos otros, los usuarios pueden crear sus propios _channels_ y distribuir sus propios paquetes. Al momento de instalar o buscar paquetes es posible especificar un _channel_ específico.
- **Enviroments**: Permiten que para cada entorno se pueda utilizar distintas versiones de los paquetes y evitan que haya conflictos de compabilidad entre paquetes. Además, es posible especificar versiones específicas de Python. Normalmente por default será el _base _o _root_. La mayoría de los comandos permiten especificar un entorno específico. 
Algunas acciones:
    - Crear un enviroment: Usa el comando `conda create`
    - Enlistar, eliminar exportar, entre otros usa: `conda env`
    - Otra forma de enlistar es con: `conda info -e`
    - Cambiar de un enviroment a otro: `conda activate` o `source activate`
- **Semantic versioning**: Es la forma como se pone la versión de un sofware/paquete (_MAJOR.MINOR.PATCH_).
    1. _MAJOR_ cuando se hacen cambios incompatibles de _API_.
    2. _MINOR_ cuando se agrega una funcionalidad de una manera compatible con versiones anteriores.
    3. _PATCH_ cuando se arreglan _bugs_ compatibles con versiones anteriores.

Para verificar que se tiene _conda_ instalado utilizar el siguiente comando.

:::{note}
Para más información consultar la [documentación](https://docs.conda.io/projects/conda/en/stable/user-guide/index.html) de _conda_.
:::

```sh
# Verificar que se tenga conda instalado
conda --version
conda -V

# Verificar que se tenga conda instalado
conda info
```

A continuación se presenta la sintaxis de llamada del comando `conda`:

:::{important}
Es altamente recomendado crear un entorno virtual por cada proyecto en _conda_. Esto con el fin de evitar conflictos al instalar librerías.
:::

```sh
# Sintaxis de llamada
conda [-h] [-v] [--no-plugins] [-V] COMMAND ...
```
- **Opciones**:
    - `-h, --help`: Muestra ayuda sobre _conda_.
    - `-v, --verbose`: Se puede usar varias veces. Una vez para una salida detallada, dos veces para el registro de _INFO_, tres veces para el registro de _DEBUG_, cuatro veces para el registro de _TRACE_.
    - `--no-plugins`: Deshabilita todos los complementos que no están integrados en _conda_.
    - `-V, --version`: Muestra el número de versión de conda.
- **Comandos**:
    -  Consultar la siguiente tabla:

Patrones útiles:

```sh
# Activar entorno base
conda activate

# Activar entorno específico
conda activate env_name

# Desactivar conda
conda deactivate
```

:::{note}
Para saber que se activó un entorno éxitosamente su nombre debe aparecer al inicio cada línea de la terminal entre paréntesis.
:::

<br/>

## Comandos

A continuación se enlistan algunos de los principales comandos de _conda_.

:::{warning}
En las secciones siguientes se revisarán algunos comandos, pero no todos. Para más información de cada comando seguir el link de cada comando o revisar la [documentación](https://docs.conda.io/projects/conda/en/stable/commands/index.html).
:::

| Comando    | Descripción |
|-----------------------|------------|
| activate | Activa un entorno de conda. |
| [clean](https://docs.conda.io/projects/conda/en/stable/commands/clean.html) | Elimina paquetes y cachés no utilizados. |
| commands | Lista todos los subcomandos de conda disponibles (incluidos los de complementos). Generalmente solo se usa para la autocompletación de comandos. |
| [compare](https://docs.conda.io/projects/conda/en/stable/commands/compare.html)  | Compara paquetes entre entornos de conda. |
| [config](https://docs.conda.io/projects/conda/en/stable/commands/config.html) | Modifica los valores de configuración en `.condarc`. |
| content-trust | Herramientas de firma y verificación para Conda. |
| [create](https://docs.conda.io/projects/conda/en/stable/commands/create.html) | Crea un nuevo entorno de conda a partir de una lista de paquetes especificados. |
| deactivate | Desactiva el entorno de conda actualmente activo. |
| [doctor](https://docs.conda.io/projects/conda/en/stable/commands/doctor.html) | Muestra un informe de estado del entorno. |
| [env](https://docs.conda.io/projects/conda/en/stable/commands/env/index.html)   | Administra entornos virtuales. |
| export   | Exporta un entorno determinado. |
| [info](https://docs.conda.io/projects/conda/en/stable/commands/info.html) | Muestra información sobre la instalación actual de conda. |
| [init](https://docs.conda.io/projects/conda/en/stable/commands/init.html) | Inicializa conda para la interacción con la terminal. |
| [install](https://docs.conda.io/projects/conda/en/stable/commands/install.html)  | Instala una lista de paquetes en un entorno de conda especificado. |
| [list](https://docs.conda.io/projects/conda/en/stable/commands/list.html)     | Lista los paquetes instalados en un entorno de conda. |
| [notices](https://docs.conda.io/projects/conda/en/stable/commands/notices.html)  | Recupera las últimas notificaciones del canal. |
| [package](https://docs.conda.io/projects/conda/en/stable/commands/package.html)  | Crea paquetes de bajo nivel para conda. (EXPERIMENTAL) |
| [remove (uninstall)](https://docs.conda.io/projects/conda/en/stable/commands/remove.html)  | Elimina una lista de paquetes de un entorno de conda especificado. |
| [rename](https://docs.conda.io/projects/conda/en/stable/commands/rename.html)   | Cambia el nombre de un entorno existente. |
| repoquery | Búsqueda avanzada en los metadatos de los paquetes. |
| [run](https://docs.conda.io/projects/conda/en/stable/commands/run.html) | Ejecuta un programa en un entorno de conda. |
| [search](https://docs.conda.io/projects/conda/en/stable/commands/search.html)   | Busca paquetes y muestra información asociada usando el formato `MatchSpec`. |
| [update (upgrade)](https://docs.conda.io/projects/conda/en/stable/commands/update.html).   | Actualiza los paquetes de conda a la última versión compatible. |

<br/>

(conda-create)=
### _create_

[create](https://docs.conda.io/projects/conda/en/stable/commands/create.html): Crea un nuevo entorno de conda a partir de una lista de paquetes especificados. Es necesario usar la opción `-n NAME` o `-p PREFIX`.

:::{important}
_conda_ permite crear entornos diferentes a Python, como por ejemplo _R_ o _sqlite_, etc. Por lo que es necesario especificar que se trata de de un entorno de Python indicando como paquete al menos a _python_.
:::

:::{warning}
No se explican todas las opciones. Para más información ir a la documentación de _conda_ siguiendo el link o usar `conda create -h`.
:::

```sh
# Sintaxis de llamada
conda create [-h] [--clone ENV] [-n ENVIRONMENT | -p PATH] [-c CHANNEL] [--use-local]
                    [--override-channels] [--repodata-fn REPODATA_FNS] [--experimental {jlap,lock}]
                    [--no-lock] [--repodata-use-zst | --no-repodata-use-zst] [--strict-channel-priority]
                    [--no-channel-priority] [--no-deps | --only-deps] [--no-pin] [--copy]
                    [--no-shortcuts] [--shortcuts-only SHORTCUTS_ONLY] [-C] [-k] [--offline] [--json]
                    [--console CONSOLE] [-v] [-q] [-d] [-y] [--download-only] [--show-channel-urls]
                    [--file FILE] [--no-default-packages] [--subdir SUBDIR] [--solver {classic,libmamba}]
                    [-m] [--dev]
                    [package_spec ...]
```
- **Argumentos posicionales**
    - `package_spec`: Lista en paquete a instalar o actualizar en el entorno. Cada paquete se separa por espacios.
- **Opciones**
    - `-h, --help`: Muestra ayuda sobre este comando.
    - `--clone ENV`: Crea un nuevo entorno como una copia de un entorno local existente.
    - `--file FILE`: Lee las versiones de los paquetes del archivo dado.
    - `--dev`: Usa `sys.executable -m conda` en _wrapper scripts_ en lugar de _CONDA_EXE_.
- **Especificación del entorno**
    - `-n ENVIRONMENT, --name ENVIRONMENT`: Nombre del entorno.
    - `-p PATH, --prefix PATH`: Ruta completa a la ubicación del entorno (es decir, _path/to/myenv_).
- **Personalización del _channel_**
    - `-c CHANNEL, --channel CHANNEL`: Canal adicional para buscar paquetes.
    - `--use-local`: Usa paquetes construidos localmente. Idéntico a '-c local'.
    - `--override-channels`: No busca canales predeterminados o _.condarc_. Requiere `--channel`.
    - `--repodata-fn REPODATA_FNS`: Especifiqca el nombre del archivo de _repodata_ en el servidor remoto donde se configuran los canales o dentro de las copias de seguridad locales.
    - `--experimental {jlap,lock}`:
        - _jlap_: Descarca datos de índice de paquetes incrementales de _repodata.jlap_; implica 'lock'.
        - _lock_: Usa el bloqueo al leer, actualizar el caché del índice (_repodata.json_). Ahora habilitado.
    - `--no-lock`: Desactiva el bloqueo al leer, actualizar el caché del índice (_repodata.json_).
    - `--repodata-use-zst, --no-repodata-use-zst`: Verifica/no verifica para _repodata.json_. Habilitado por defecto.
    - `--subdir SUBDIR, --platform SUBDIR`: Usa paquetes creados para esta plataforma.

**Patrones útiles**:

A continuación se presentan algunos casos de uso comunes.

:::{note}
Para especificar versiones de los paquetes usar _=_ para versiones específicas y _>=_ para versiones mínimas.
:::

```sh
# Crear entorno nuevo
conda create -n myenv

# Crear entorno nuevo con un paquete 
conda create -n myenv pkg_name

# Crear entorno nuevo con múltiples paquetes
conda create -n myenv pkg_name1 pkg_name2 ... # Separados por espacios

# Crear entorno nuevo con un archivo de requitos
conda create -n myenv --file filename.yml # Ver ejm de filename más abajo

# Crear entorno nuevo con una versión de Python específica
conda create -m myenv python=MAJOR.MINOR # aplica lo mismo para cualquier otro paquete

# Crear entorno que sea un clon de otro
conda create -n env2 --clone path/to/env1
```

A continuación se presenta un ejemplo de un archivo de definición del entorno:

:::{important}
El archivo debe de tener extensión `.yml` o `.yaml`. Y debe seguir la siguiente estrutura:

<code>
name: env_name
channels:
    - conda-forge
    - ...
dependencies:
    - pkg_name1
    - ...
</code>

También puede ser usado un archivo `.txt` creado con `conda list --explicit` o `conda list --export`
:::

:::{note}
Existe también el comando `conda env create` para crear entornos desde archivos de definición de entornos.
:::

Ejemplo de un archivo:

```yaml
name: myproject
channels:
  - defaults
dependencies:
  - python=3.6
  - pandas>=0.21
  - scikit-learn
  - statsmodels
```

<br/>

### _env_

[env](https://docs.conda.io/projects/conda/en/stable/commands/env/index.html): Administra entornos virtuales. Muchos de estos subcomandos utilizan directamente un archivo de definición del entorno, que especifica la definición del entorno por medio de una archivo `.yml` o `.yaml`.

```sh
# Sintaxis de llamada
conda env [-h] command ...
```
- **Opciones**
    - `-h`: Muestra ayuda sobre este comando.
- **Comandos**: Es un argumento posicional, debe ir al final.
    - [config](https://docs.conda.io/projects/conda/en/stable/commands/env/config/index.html): Configura un entorno de _conda_.
    - [create](https://docs.conda.io/projects/conda/en/stable/commands/env/create.html): Crea un entorno basado en un archivo de definición del entorno.
    - [export](https://docs.conda.io/projects/conda/en/stable/commands/env/export.html): Exporta un entorno determinado.
    - [list](https://docs.conda.io/projects/conda/en/stable/commands/env/list.html): Un alias para `conda info --envs`. Enlista todos los entornos de conda.
    - [remove](https://docs.conda.io/projects/conda/en/stable/commands/env/remove.html): Elimina un entorno.
    - [update](https://docs.conda.io/projects/conda/en/stable/commands/env/update.html): Actualiza el entorno actual en función del archivo de entorno.

#### _env create_

[create](https://docs.conda.io/projects/conda/en/stable/commands/env/create.html): Crea un entorno basado en un archivo de definición del entorno. Para crear entornos directamente en la línea de comandos revisar `ref`{conda-create}

:::{important}
_conda_ permite crear entornos diferentes a Python, como por ejemplo _R_ o _sqlite_, etc. Por lo que es necesario especificar que se trata de de un entorno de Python indicando como paquete al menos a _python_.
:::

:::{warning}
No se explican todas las opciones. Para más información ir a la documentación de _conda_ siguiendo el link o usar `conda env create -h`.
:::

```sh
# Sintaxis de llamada
conda env create [-h] [-f FILE] [-n ENVIRONMENT | -p PATH] [-C] [-k] [--offline]
                        [--no-default-packages] [--json] [--console CONSOLE] [-v] [-q] [-d] [-y]
                        [--solver {classic,libmamba}] [--subdir SUBDIR]
                        [remote_definition]
```
- **Opciones**
    - `-h, --help`: Muestra ayuda sobre este comando.
    - `-f FILE, --file FILE`: Archivo de definición del entorno (default: _environment.yml_).
    - `--no-default-packages`: Ignora _create_default_packages_ en el archivo _.condarc_.
    - `--solver {classic,libmamba}`: Elige qué _solver backend_ usar.
    - `--subdir SUBDIR, --platform SUBDIR`: Usa paquetes creados para esta plataforma.
- **Especificación del entorno**
    - `-n ENVIRONMENT, --name ENVIRONMENT`: Nombre del entorno.
    - `-p PATH, --prefix PATH`: Ruta completa a la ubicación del entorno (es decir, _path/to/myenv_).

**Patrones útiles**:

A continuación se presentan algunos casos de uso comunes.

:::{note}
Para especificar versiones de los paquetes usar _=_ para versiones específicas y _>=_ para versiones mínimas.
:::

```sh
# Crear entorno nuevo
conda env create -f /path/to/environment.yml

# Crear entorno nuevo sobreescribiendo el nombre
conda env create -f /path/to/requirements.txt -n path/to/envname
```
- Notar que el entorno se puede crear en un directorio diferente al actual.

A continuación se presenta un ejemplo de un archivo de definición del entorno:

:::{important}
El archivo debe de tener extensión `.yml` o `.yaml`. Y debe seguir la siguiente estrutura:

<code>
name: env_name
channels:
    - conda-forge
    - ...
dependencies:
    - pkg_name1
    - ...
</code>
:::

Ejemplo de un archivo:

```yaml
name: myproject
channels:
  - defaults
dependencies:
  - python=3.6
  - pandas>=0.21
  - scikit-learn
  - statsmodels
```

<br/>

#### _env export_

[export](https://docs.conda.io/projects/conda/en/stable/commands/env/export.html): Exporta un entorno determinado.

```sh
# Sintaxis de llamada
conda env export [-h] [-c CHANNEL] [--override-channels] [-n ENVIRONMENT | -p PATH] [-f FILE]
                        [--no-builds] [--ignore-channels] [--json] [--console CONSOLE] [-v] [-q]
                        [--from-history]
```
**Opciones**
- `-h, --help`: Muestra ayuda de este comando.
- `-c CHANNEL, --channel CHANNEL`: Canal adicional para incluir en la exportación.
- `--override-channels`: No incluye canales de _.condarc_.
- `-f FILE, --file FILE`: Nombre o ruta del archivo para el entorno exportado.
- `--no-builds`: Elimina la especificación de compilación de las dependencias.
- `--ignore-channels`: No incluye nombres de canales con nombres de paquetes.
- `--from-history`: Construye especificaciones de entorno a partir de especificaciones explícitas en el historial.
- `-n ENVIRONMENT, --name ENVIRONMENT`: Nombre del entorno.
- `-p PATH, --prefix PATH`: Ruta completa a la ubicación del entorno (es decir, _path/to/myenv_).
- `--json`: Informa todo el resultado como JSON. Adecuado para usar _conda_ programáticamente.
- `--console CONSOLE`: Selecciona el _backend_ para usar para la representación de salida normal.
- `-v, --verbose`: Se puede usar varias veces. Una vez para una salida detallada, dos veces para el registro de información, tres veces para el registro de depuración, cuatro veces para el registro de rastreo.
- `-q, --quiet`: No muestra la barra de progreso.

**Patrones útiles**:

A continuación se presentan algunos casos de uso comunes.

```sh
# Exportar entorno en un archivo
conda env export --file path/to/filename.yml
```
- _filename_ es el archivo donde se exportará el entorno, debe tener extensión `.yml` o `.yaml`.

<br/>

#### _env list_

[list](https://docs.conda.io/projects/conda/en/stable/commands/env/list.html): Enlista todos los entornos de conda.

:::{note}
Es un alias para `conda info --envs`.
:::

```sh
# Sintaxis de llamada
conda env list [-h] [--json] [--console CONSOLE] [-v] [-q]
```
**Opciones**:
- `-h, --help`: Muestra ayuda de este comando.
- `--json`: Informa todo el resultado como JSON. Adecuado para usar _conda_ programáticamente.
- `--console CONSOLE`: Selecciona el _backend_ para usar para la representación de salida normal.
- `-v, --verbose`: Se puede usar varias veces. Una vez para una salida detallada, dos veces para el registro de información, tres veces para el registro de depuración, cuatro veces para el registro de rastreo.
- `-q, --quiet`: No muestra la barra de progreso.

**Patrones útiles**:

A continuación se presentan algunos casos de uso comunes.

```sh
# Enlistar entornos
conda env list
```

<br/>

#### _env remove_

[remove](https://docs.conda.io/projects/conda/en/stable/commands/env/remove.html): Elimina un entorno.

```sh
# Sintaxis de llamada
conda env remove [-h] [-n ENVIRONMENT | -p PATH] [--solver {classic,libmamba}] [--json]
                        [--console CONSOLE] [-v] [-q] [-d] [-y]
```
**Opciones**:
- `-h, --help`: Muestra ayuda de este comando.
- `--solver {classic,libmamba}`: Elige qué _solver backend_ usar.
- `-n ENVIRONMENT, --name ENVIRONMENT`: Nombre del entorno.
- `-p PATH, --prefix PATH`: Ruta completa a la ubicación del entorno (es decir, _path/to/myenv_).
- `--json`: Informa todo el resultado como JSON. Adecuado para usar _conda_ programáticamente.
- `--console CONSOLE`: Selecciona el _backend_ para usar para la representación de salida normal.
- `-v, --verbose`: Se puede usar varias veces. Una vez para una salida detallada, dos veces para el registro de información, tres veces para el registro de depuración, cuatro veces para el registro de rastreo.
- `-q, --quiet`: No muestra la barra de progreso.
- `-d, --dry-run`: Solo muestra lo que se habría hecho.
- `-y, --yes`: Establece cualquier valor de confirmación en 'Sí' automáticamente. No se les pedirá a los usuarios que confirmaran ninguna adición, eliminación, copias de seguridad, etc.

**Patrones útiles**:

A continuación se presentan algunos casos de uso comunes.

```sh
# Remover un entorno
conda env remove --name envname
```
- _envname_ es el nombre del entorno que se removerá.

#### _env update_

[update](https://docs.conda.io/projects/conda/en/stable/commands/env/update.html): Actualiza el entorno actual en función del archivo de entorno.

```sh
# Sintaxis de llamada
conda env update [-h] [-n ENVIRONMENT | -p PATH] [-f FILE] [--prune] [--json] [--console CONSOLE]
                        [-v] [-q] [--solver {classic,libmamba}]
```
**Opciones**:
- `-h, --help`: Muestra ayuda de este comando.
- `-f FILE, --file FILE`: Nombre o ruta del archivo para el entorno exportado.
- `--prune`: Remueve paquetes instalados no definidos en `environment.yml`.
- `--solver {classic,libmamba}`: Elige qué _solver backend_ usar.
- `-n ENVIRONMENT, --name ENVIRONMENT`: Nombre del entorno.
- `-p PATH, --prefix PATH`: Ruta completa a la ubicación del entorno (es decir, _path/to/myenv_).
- `--json`: Informa todo el resultado como JSON. Adecuado para usar _conda_ programáticamente.
- `--console CONSOLE`: Selecciona el _backend_ para usar para la representación de salida normal.
- `-v, --verbose`: Se puede usar varias veces. Una vez para una salida detallada, dos veces para el registro de información, tres veces para el registro de depuración, cuatro veces para el registro de rastreo.
- `-q, --quiet`: No muestra la barra de progreso.

**Patrones útiles**:

A continuación se presentan algunos casos de uso comunes.

```sh
# Actualizar entorno con base a un archivo un entorno
conda env update --name=envname --file=path/to/filename.yml
```
- _envname_ es el nombre del entorno que se actualizará.
- _filename_ es el archivo sobre el cual se basará la actualización, debe tener extensión `.yml` o `.yaml`.

<br/>

### _info_

[info](https://docs.conda.io/projects/conda/en/stable/commands/info.html) | Muestra información sobre la instalación actual de conda.

```sh
# Sintaxis de llamada
conda info [-h] [--json] [--console CONSOLE] [-v] [-q] [-a] [--base] [-e] [-s] [--unsafe-channels]
```
**Opciones**
- `-h, --help`: Muestra ayuda sobre este comando.
- `-a, --all`: Muestra toda la información.
- `--base`: Muestra la ruta del entorno base.
- `-e, --envs`: Enumera todos los entornos de _conda_ conocidos.
- `-s, --system`: Lista de variables de entorno.
- `--unsafe-channels`: Muestra lista de canales con _tokens_ expuestos.
- `--json`: Informa todo el resultado como JSON. Adecuado para usar _conda_ programáticamente.
- `--console CONSOLE`: Selecciona el _backend_ para usar para la representación de salida normal.
- `-v, --verbose`: Se puede usar varias veces. Una vez para una salida detallada, dos veces para el registro de información, tres veces para el registro de depuración, cuatro veces para el registro de rastreo.
- `-q, --quiet`: No muestra la barra de progreso.

<br/>

### _install_

[install](https://docs.conda.io/projects/conda/en/stable/commands/install.html)  | Instala una lista de paquetes en un entorno de conda especificado.

:::{note}
En el proceso de installar un paquete se verificará la compatibilidad de la versión de Python y la del paquete en sí mismo, así como de todas las dependencias (paquetes extras necesarios). A esto se le llama _satisfiability_.
:::

:::{warning}
No se explican todas las opciones. Para más información ir a la documentación de _conda_ siguiendo el link o usar `conda install -h`.
:::

```sh
# Sintaxis de llamada
conda install [-h] [--revision REVISION] [-n ENVIRONMENT | -p PATH] [-c CHANNEL] [--use-local]
                     [--override-channels] [--repodata-fn REPODATA_FNS] [--experimental {jlap,lock}]
                     [--no-lock] [--repodata-use-zst | --no-repodata-use-zst] [--strict-channel-priority]
                     [--no-channel-priority] [--no-deps | --only-deps] [--no-pin] [--copy] [--no-shortcuts]
                     [--shortcuts-only SHORTCUTS_ONLY] [-C] [-k] [--offline] [--json] [--console CONSOLE]
                     [-v] [-q] [-d] [-y] [--download-only] [--show-channel-urls] [--file FILE]
                     [--solver {classic,libmamba}] [--force-reinstall]
                     [--freeze-installed | --update-deps | -S | --update-all | --update-specs] [-m]
                     [--clobber] [--dev]
                     [package_spec ...]
```
- **Argumentos posicionales**
    - `package_spec`: Lista en paquete a instalar o actualizar en el entorno. Cada paquete se separa por espacios.
- **Opciones**
    - `-h, --help`: Muestra ayuda sobre este comando.
    - `--revision REVISION`: Revierte a la _REVISION_ especificada.
    - `--file FILE`: Lee las versiones de los paquetes del archivo dado.
    - `--dev`: Usa `sys.executable -m conda` en _wrapper scripts_ en lugar de _CONDA_EXE_.
- **Especificación del entorno**
    - `-n ENVIRONMENT, --name ENVIRONMENT`: Nombre del entorno.
    - `-p PATH, --prefix PATH`: Ruta completa a la ubicación del entorno (es decir, _path/to/myenv_).
- **Personalización del _channel_**
    - `-c CHANNEL, --channel CHANNEL`: Canal adicional para buscar paquetes.
    - `--use-local`: Usa paquetes construidos localmente. Idéntico a '-c local'.
    - `--override-channels`: No busca canales predeterminados o _.condarc_. Requiere `--channel`.
    - `--repodata-fn REPODATA_FNS`: Especifiqca el nombre del archivo de _repodata_ en el servidor remoto donde se configuran los canales o dentro de las copias de seguridad locales.
    - `--experimental {jlap,lock}`:
        - _jlap_: Descarca datos de índice de paquetes incrementales de _repodata.jlap_; implica 'lock'.
        - _lock_: Usa el bloqueo al leer, actualizar el caché del índice (_repodata.json_). Ahora habilitado.
    - `--no-lock`: Desactiva el bloqueo al leer, actualizar el caché del índice (_repodata.json_).
    - `--repodata-use-zst, --no-repodata-use-zst`: Verifica/no verifica para _repodata.json_. Habilitado por defecto.
- **Modificadores del modo del _solver_**
    - `--strict-channel-priority`: Los paquetes en canales de menor prioridad no se consideran si un paquete con el mismo nombre aparece en un canal de mayor prioridad.
    - `--no-channel-priority`: La versión del paquete tiene prioridad sobre la prioridad del canal.
    - `--no-deps`: No instala, actualiza, elimina ni cambia las dependencias.
    - `--only-deps`: Solo instala dependencias.
    - `--no-pin`: Ignora el archivo _pinned_.
    - `--solver {classic,libmamba}`: Elige qué _solver backend_ usar.
    - `--force-reinstall`: Se asegura de que cualquier paquete requerido por el usuario para la operación actual esté desinstalado y reinstalado, incluso si ese paquete ya existe en el entorno.
    - `--freeze-installed, --no-update-deps`: No actualiza ni cambia las dependencias ya instaladas.
    - `--update-deps`: Actualiza dependencias que tienen actualizaciones disponibles.
    - `-S, --satisfied-skip-solve`: Salida temprana y no ejecuta el _solver_ si las especificaciones solicitadas están satisfechas.
    - `--update-all, --all`: Actualiza todos los paquetes instalados en el entorno.
    - `--update-specs`: Actualización basada en especificaciones proporcionadas.

**Patrones útiles**:

A continuación se presentan algunos casos de uso comunes.

:::{note}
Para especificar versiones de los paquetes usar _=_ para versiones específicas y _>=_ para versiones mínimas.
:::

```sh
# Instalar un paquete
conda install pkg_name

# Instalar múltiples paquetes
conda install pkg_name1 pkg_name2 ... # Separar por espacios

# Instalar un archivo de requitos
conda install --file filename.yml # Ver ejm de filename más abajo

# Instalar versión específica
conda create -m myenv python=MAJOR.MINOR # aplica lo mismo para cualquier otro paquete

# Instalar versión específica parcialmente
conda create -m myenv python=MAJOR.* # aplica lo mismo para cualquier otro paquete

# Instalar alguna de las versiones especificadas
conda create -m myenv 'pkg_name=1.0|1.4' # Separar con |

# Instalar versiones que satisfaga condiciones
conda create -m myenv 'pkg_name>1.0,pkg_name<1.4' # Separar con |
```
- _myenv_ es el nombre del entorno.

<br/>

### _list_

[list](https://docs.conda.io/projects/conda/en/stable/commands/list.html): Lista los paquetes instalados en un entorno de conda.

```sh
# Sintaxis de llamada
conda list [-h] [-n ENVIRONMENT | -p PATH] [--json] [--console CONSOLE] [-v] [-q]
                  [--show-channel-urls] [--reverse] [-c] [-f] [--explicit] [--md5] [--sha256] [-e] [-r]
                  [--no-pip] [--auth]
                  [regex]
```
- **Argumentos posicionales**
    - `regex`: enlista solo paquetes que coinciden con esta expresión regular.
- **Opciones**
    - `-h, --help`: Muestra ayuda de este comando.
    - `--show-channel-urls`: Muestra URL de canales. Anula el valor dado por `conda config --show show_channel_urls`.
    - `--reverse`: Lista de paquetes instalados en orden inverso.
    - `-c, --canonical`: Imprime solamente nombres canónicos de los paquetes.
    - `-f, --full-name`: Solo busca nombres completos, es decir, `^<regex>$`. `--full-name NAME` es idéntico a la expresión regular `'^NAME$'`.
    - `--explicit`: Lista explícitamente todos los paquetes de _conda_ instalados con URL (la salida puede ser utilizada por `conda create --file`).
    - `--md5`: Agrega _MD5 hashsum_ cuando se usa `--explicit`.
    - `--sha256`: Agrega _SHA256 hashsum_ cuando se usa `--explicit`.
    - `-e, --export`: Imprime cadenas de requisitos legibles por máquina en lugar de listas de paquetes legibles por humanos de manera explícita. Esta salida puede ser utilizada por `conda create --file`.
    - `-r, --revisions`: Enumera el historial de revisión.
    - `--no-pip`: No incluye paquetes instalados _pip-only_.
    - `--auth`: En modo explícito, deja los detalles de autenticación en los URL de paquete. Se eliminan de otra manera por defecto.
- **Especificación del entorno**
    - `-n ENVIRONMENT, --name ENVIRONMENT`: Nombre del entorno.
    - `-p PATH, --prefix PATH`: Ruta completa a la ubicación del entorno (es decir, _path/to/myenv_).
- **Salida y Opciones del control del flujo**
    - `--json`: Informa todo el resultado como JSON. Adecuado para usar _conda_ programáticamente.
    - `--console CONSOLE`: Selecciona el _backend_ para usar para la representación de salida normal.
    - `-v, --verbose`: Se puede usar varias veces. Una vez para una salida detallada, dos veces para el registro de información, tres veces para el registro de depuración, cuatro veces para el registro de rastreo.
    - `-q, --quiet`: No muestra la barra de progreso.

**Patrones útiles**:

A continuación se presentan algunos casos de uso comunes.

```sh
# Enlistar paquetes
conda list

# Enlistar paquete en entorno específico
conda list -n myenv

# Enlistar paquetes que cumplen un regex
conda list ^py # Ejm con 'empieza por "py"'

# Almacenar paquetes para usar con otros comandos
conda list --export > path/to/filename.txt
```

<br/>

### _remove_

[remove](https://docs.conda.io/projects/conda/en/stable/commands/remove.html): Elimina una lista de paquetes de un entorno de conda especificado. Usar la _flag_ `--all` para remover todos los paquetes y el entorno en sí mismo. Este comando también removerá todas las dependencias

:::{warning}
No se explican todas las opciones. Para más información ir a la documentación de _conda_ siguiendo el link o usar `conda remove -h`.
:::

```sh
# Sintaxis de llamada
conda remove [-h] [-n ENVIRONMENT | -p PATH] [-c CHANNEL] [--use-local] [--override-channels]
                    [--repodata-fn REPODATA_FNS] [--experimental {jlap,lock}] [--no-lock]
                    [--repodata-use-zst | --no-repodata-use-zst] [--features] [--force-remove] [--no-pin]
                    [--solver {classic,libmamba}] [-C] [-k] [--offline] [--json] [--console CONSOLE] [-v]
                    [-q] [-d] [-y] [--all] [--keep-env] [--dev]
                    [package_name ...]
```
- **Argumentos posicionales**
    - `package_spec`: Lista en paquete a instalar o actualizar en el entorno. Cada paquete se separa por espacios.
- **Opciones**
    - `-h, --help`: Muestra ayuda sobre este comando.
    - `--all`: Elimina todos los paquetes, es decir, todo el entorno.
    - `--keep-env`: Utilizado con `--all`, elimine todos los paquetes pero mantiene el entorno.
    - `--dev`: Usa `sys.executable -m conda` en _wrapper scripts_ en lugar de _CONDA_EXE_.
- **Personalización del _channel_**
    - `-c CHANNEL, --channel CHANNEL`: Canal adicional para buscar paquetes.
    - `--use-local`: Usa paquetes construidos localmente. Idéntico a '-c local'.
    - `--override-channels`: No busca canales predeterminados o _.condarc_. Requiere `--channel`.
    - `--repodata-fn REPODATA_FNS`: Especifiqca el nombre del archivo de _repodata_ en el servidor remoto donde se configuran los canales o dentro de las copias de seguridad locales.
    - `--experimental {jlap,lock}`:
        - _jlap_: Descarca datos de índice de paquetes incrementales de _repodata.jlap_; implica 'lock'.
        - _lock_: Usa el bloqueo al leer, actualizar el caché del índice (_repodata.json_). Ahora habilitado.
    - `--no-lock`: Desactiva el bloqueo al leer, actualizar el caché del índice (_repodata.json_).
    - `--repodata-use-zst, --no-repodata-use-zst`: Verifica/no verifica para _repodata.json_. Habilitado por defecto.
- **Modificadores del modo del _solver_**
    - `--features`: Elimina características (en lugar de paquetes).
    - `--force-remove, --force`: Fuerza la eliminación de un paquete sin eliminar paquetes que dependen de él. El uso de esta opción generalmente dejará el entorno en un estado roto e inconsistente.
    - `--no-pin`: Ignora paquetes _pinned_ que se aplican a la operación actual.
    - `--solver {classic,libmamba}`: Elige qué _solver backend_ usar.

**Patrones útiles**:

A continuación se presentan algunos casos de uso comunes.

```sh
# Remover un paquete
conda remove pkg_name

# Remover múltiples paquetes
conda remove pkg_name1 pkg_name2 ... # Separar por espacios

# Remover todos los paquetes y el entorno
conda remove -n myenv --all

# Remover todos los paquetes pero mantener el entorno
conda remove -n myenv --all --keep-env
```
- _myenv_ es el nombre del entorno.

<br/>

### _run_

[run](https://docs.conda.io/projects/conda/en/stable/commands/run.html): Ejecuta un programa en un entorno de conda. Permite ejecutar comandos de terminal usando conda.

```sh
# Sintaxis de llamada
conda run [-h] [-n ENVIRONMENT | -p PATH] [-v] [--dev] [--debug-wrapper-scripts] [--cwd CWD]
                 [--no-capture-output]
                 ...
```
- **Argumentos posicionales**
    - `executable_call`: Nombre ejecutable, con argumentos adicionales que se pasarán al ejecutable en invocación.
- **Opciones**
    - `-h, --help`: Muestra ayuda de este comando.
    - `-v, --verbose`: Se puede usar varias veces. Una vez para una salida detallada, dos veces para el registro de información, tres veces para el registro de depuración, cuatro veces para el registro de rastreo.
    - `--dev`: Establece `CONDA_EXE` a `python -m conda`, suponiendo que el directorio de trabajo actual contiene la raíz de las fuentes de desarrollo de conda.
    - `--debug-wrapper-scripts`: Cuando esto se establece, donde se implementa, el _scriptswill_ de _shell wrapper_ usa el comando `echo` para imprimir información de depuración en _stderr_ (error estándar).
    - `--cwd CWD`: Directorio de trabajo actual para que el comando se ejecute. El valor predeterminado es el directorio de trabajo actual del usuario si no se especifica ningún directorio.
    - `--no-capture-output, --live-stream`: No captura _stdout/stderr_ (Salida estándar/Error estándar).
- **Especificación del entorno**
    - `-n ENVIRONMENT, --name ENVIRONMENT`: Nombre del entorno.
    - `-p PATH, --prefix PATH`: Ruta completa a la ubicación del entorno (es decir, _path/to/myenv_).

**Patrones útiles**:

A continuación se presentan algunos casos de uso comunes.

```sh
# Ejecutar comando desde conda
conda run -n my-python-env python --version
```
- En este ejemplo se imprime la versión de Python, desde conda, usando el comando `python`.

<br/>

### _search_

[search](https://docs.conda.io/projects/conda/en/stable/commands/search.html): Busca paquetes y muestra información asociada usando el formato `MatchSpec` (lenguaje de consultas para paquetes de _conda_).

:::{warning}
No se explican todas las opciones. Para más información ir a la documentación de _conda_ siguiendo el link o usar `conda search -h`.
:::

```sh
# Sintaxis de llamada
conda search [-h] [--envs] [-i] [--subdir SUBDIR] [--skip-flexible-search] [-c CHANNEL]
                    [--use-local] [--override-channels] [--repodata-fn REPODATA_FNS]
                    [--experimental {jlap,lock}] [--no-lock] [--repodata-use-zst | --no-repodata-use-zst]
                    [-C] [-k] [--offline] [--json] [--console CONSOLE] [-v] [-q]
```
- **Opciones**
    - `-h, --help`: Muestra ayuda sobre este comando.
    - `--envs`: Busca en todos los entornos del usuario actual. Si se ejecuta como administrador (en Windows) o UID 0 (en UNIX), busca en todos los entornos conocidos en el sistema.
    - `-i, --info`: Proporciona información detallada sobre cada paquete.
    - `--subdir SUBDIR, --platform SUBDIR`: Busca el _subdir_ dado (sistema operativo). Debe formatearse como 'osx-64', 'linux-32', 'win-64', etc. El valor predeterminado es buscar la plataforma actual.
    - `--skip-flexible-search`: No realiza una búsqueda flexible si la búsqueda inicial falla.
- **Personalización del _channel_**
    - `-c CHANNEL, --channel CHANNEL`: Canal adicional para buscar paquetes.
    - `--use-local`: Usa paquetes construidos localmente. Idéntico a '-c local'.
    - `--override-channels`: No busca canales predeterminados o _.condarc_. Requiere `--channel`.
    - `--repodata-fn REPODATA_FNS`: Especifiqca el nombre del archivo de _repodata_ en el servidor remoto donde se configuran los canales o dentro de las copias de seguridad locales.
    - `--experimental {jlap,lock}`:
        - _jlap_: Descarca datos de índice de paquetes incrementales de _repodata.jlap_; implica 'lock'.
        - _lock_: Usa el bloqueo al leer, actualizar el caché del índice (_repodata.json_). Ahora habilitado.
    - `--no-lock`: Desactiva el bloqueo al leer, actualizar el caché del índice (_repodata.json_).
    - `--repodata-use-zst, --no-repodata-use-zst`: Verifica/no verifica para _repodata.json_. Habilitado por defecto.

**Patrones útiles**:

A continuación se presentan algunos casos de uso comunes.

:::{note}
Para especificar versiones de los paquetes usar _=_ para versiones específicas y _>=_ para versiones mínimas.
:::

```sh
# Buscar un paquete
conda search pkg_name

# Buscar un paquete que contiene una palabra
conda search '*pattern*'

# Buscar paquete con una versión específica
conda search 'pkg_name>=MAJOR.MINOR'

# Buscar paquete en un channel concreto
conda search conda-forge::pkg_name # Ejm con conda-forge
```

<br/>

### _update_

[update (upgrade)](https://docs.conda.io/projects/conda/en/stable/commands/update.html): Actualiza los paquetes de conda a la última versión compatible.

:::{warning}
No se explican todas las opciones. Para más información ir a la documentación de _conda_ siguiendo el link o usar `conda install -h`.
:::

```sh
# Sintaxis de llamada
conda update [-h] [-n ENVIRONMENT | -p PATH] [-c CHANNEL] [--use-local] [--override-channels]
                    [--repodata-fn REPODATA_FNS] [--experimental {jlap,lock}] [--no-lock]
                    [--repodata-use-zst | --no-repodata-use-zst] [--strict-channel-priority]
                    [--no-channel-priority] [--no-deps | --only-deps] [--no-pin] [--copy] [--no-shortcuts]
                    [--shortcuts-only SHORTCUTS_ONLY] [-C] [-k] [--offline] [--json] [--console CONSOLE]
                    [-v] [-q] [-d] [-y] [--download-only] [--show-channel-urls] [--file FILE]
                    [--solver {classic,libmamba}] [--force-reinstall]
                    [--freeze-installed | --update-deps | -S | --update-all | --update-specs] [--clobber]
                    [package_spec ...]
```
- **Argumentos posicionales**
    - `package_spec`: Lista en paquete a instalar o actualizar en el entorno. Cada paquete se separa por espacios.
- **Opciones**
    - `-h, --help`: Muestra ayuda sobre este comando.
    - `--file FILE`: Lee las versiones de los paquetes del archivo dado.
- **Especificación del entorno**
    - `-n ENVIRONMENT, --name ENVIRONMENT`: Nombre del entorno.
    - `-p PATH, --prefix PATH`: Ruta completa a la ubicación del entorno (es decir, _path/to/myenv_).
- **Personalización del _channel_**
    - `-c CHANNEL, --channel CHANNEL`: Canal adicional para buscar paquetes.
    - `--use-local`: Usa paquetes construidos localmente. Idéntico a '-c local'.
    - `--override-channels`: No busca canales predeterminados o _.condarc_. Requiere `--channel`.
    - `--repodata-fn REPODATA_FNS`: Especifiqca el nombre del archivo de _repodata_ en el servidor remoto donde se configuran los canales o dentro de las copias de seguridad locales.
    - `--experimental {jlap,lock}`:
        - _jlap_: Descarca datos de índice de paquetes incrementales de _repodata.jlap_; implica 'lock'.
        - _lock_: Usa el bloqueo al leer, actualizar el caché del índice (_repodata.json_). Ahora habilitado.
    - `--no-lock`: Desactiva el bloqueo al leer, actualizar el caché del índice (_repodata.json_).
    - `--repodata-use-zst, --no-repodata-use-zst`: Verifica/no verifica para _repodata.json_. Habilitado por defecto. 
- **Modificadores del modo del _solver_**
    - `--strict-channel-priority`: Los paquetes en canales de menor prioridad no se consideran si un paquete con el mismo nombre aparece en un canal de mayor prioridad.
    - `--no-channel-priority`: La versión del paquete tiene prioridad sobre la prioridad del canal.
    - `--no-deps`: No instala, actualiza, elimina ni cambia las dependencias.
    - `--only-deps`: Solo instala dependencias.
    - `--no-pin`: Ignora el archivo _pinned_.
    - `--solver {classic,libmamba}`: Elige qué _solver backend_ usar.
    - `--force-reinstall`: Se asegura de que cualquier paquete requerido por el usuario para la operación actual esté desinstalado y reinstalado, incluso si ese paquete ya existe en el entorno.
    - `--freeze-installed, --no-update-deps`: No actualiza ni cambia las dependencias ya instaladas.
    - `--update-deps`: Actualiza dependencias que tienen actualizaciones disponibles.
    - `-S, --satisfied-skip-solve`: Salida temprana y no ejecuta el _solver_ si las especificaciones solicitadas están satisfechas.
    - `--update-all, --all`: Actualiza todos los paquetes instalados en el entorno.
    - `--update-specs`: Actualización basada en especificaciones proporcionadas.

**Patrones útiles**:

A continuación se presentan algunos casos de uso comunes.

```sh
# Actualizar paquete específico
conda update -n myenv pkg_name
```
- _myenv_ es el nombre del entorno.