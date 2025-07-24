# pip

Pip es el gestor de paquetes de Python que permite instalar, actualizar y administrar bibliotecas y dependencias desde el _Python Package Index_ (PyPI). Para poder utilizar _pip_, Python debe estar instalado. Usualmente pip ya viene instalado si se descargó Python desde _python.org_ o se está trabajando en un ambiente virtual. 

Para verificar que se tiene _pip_ instalado utilizar el siguiente comando.

:::{note}
Para más información consultar la [documentación](https://pip.pypa.io/en/stable/) de _pip_.
:::

```sh
# Verificar que se tenga Python instalado
python --version

# Verificar que se tenga pip instalado
python -m pip --version
```

:::{attention}
En caso de que no se tenga _pip_ instalado consultar [esta guía](https://pip.pypa.io/en/stable/installation/) de _pip_.
:::

A continuación se presenta la sintaxis de llamada del comando `pip`:

:::{attention}
Para más información consultar la [documentación](https://pip.pypa.io/en/stable/cli/pip/) de _pip_.
:::

:::{warning}
Es posible que sea necesario usar el comando `python3` para ejecutar _pip_. Incluso se podría indicar una versión específica o un entorno virtual. Esto aplica para todos los comandos presentados en esta sección.
:::

```sh
# Sintaxis de llamada
pip <command> [options]

# Sintaxis de llamada con Python
python3 -m pip <command> [options] # o solo python o versión concreta

# Sintaxis de llamada con entorno virtual
env_name/bin/python -m pip <command> [options]
```
- **Comandos**:
    - Ver tabla más abajo.
- **Opciones**:
  - `-h, --help`: Mostrar ayuda.
    - `--debug`: Deja que las excepciones no controladas se propagen fuera de la subrutina principal, en lugar de registrarlas en _stderr._.
    - `--isolated`: Ejecuta _pip_ en modo aislado, ignorando las variables de entorno y la configuración del usuario.
    - `--require-virtualenv`: Permite que _pip_ solo se ejecute en un entorno virtual; Sale con un error de lo contrario.
    - `--python <python>`: Ejecuta _pip_ con el intérprete Python especificado.
    - `-v, --verbose`: Da más salida. La opción es aditiva y se puede usar hasta 3 veces.
    - `-V, --version`: Muestra la versión.
    - `-q, --quiet`: Dar menos salida. La opción es aditiva y se puede usar hasta 3 veces (correspondiente a la advertencia, error y niveles de registro críticos).
    - `--log <path>`: Ruta hacia un _log_ de agregado detallado (_verbose_).
    - `--no-input`: Desactivar la solicitud de entrada.
    - `--keyring-provider <keyring_provider>`: Habilita la búsqueda de credenciales a través del _keyring_ si se permite la entrada del usuario. Es necesario especificar el mecanismo a usar: {_auto, disabled, import, subprocess_}. (predeterminado: _auto_).
    - `--proxy <proxy>`: Especifica un proxy en el formulario del esquema: `scheme://[user:passwd@]proxy.server:port`.
    - `--retries <retries>`: Número máximo de reintentos que cada conexión debe intentar (predeterminada 5 veces).
    - `--timeout <sec>`: Establece el tiempo de espera del _socket_ (predeterminado 15 segundos).
    - `--exists-action <action>`: Acción predeterminada cuando ya existe una ruta: {_(s)witch, (i)gnore, (w)ipe, (b)ackup, (a)bort_}.
    - `--trusted-host <hostname>`: Marca este _host_ o _host:part_ como confiable, a pesar de que no tenga _https_ válido o ningún _https_.
    - `--cert <path>`: Ruta al paquete de certificado CA codificado por PEM. Si se proporciona, anula el valor predeterminado.
    - `--client-cert <path>`: Ruta al certificado de cliente SSL, un solo archivo que contiene la clave privada y el certificado en formato PEM.
    - `--cache-dir <dir>`: Almacena los datos de caché en _\<dir>_.
    - `--no-cache-dir`: Deshabilita el caché.
    - `--disable-pip-version-check`: No verifica periódicamente _PyPI_ para determinar si hay una nueva versión de PIP disponible para descargar. Implícito con `--no-index`.
    - `--no-color`: Suprimir la salida con color.
    - `--no-python-version-warning`: Sinlenciar advertencias de deprecación para las próximas Pythons no compatibles.
    - `--use-feature <feature>`: Habilita una nueva funcionalidad, que puede ser incompatible hacia atrás.
    - `--use-deprecated <feature>`: Habilita una funcionalidad obsoleta, que se eliminará en el futuro.

La tabla de comandos disponibles es la siguiente:

| Comando      | Descripción |
|-------------|------------|
| [cache](https://pip.pypa.io/en/stable/cli/pip_cache/)    | Inspecciona y administra el caché del _wheel_ de _pip_. |
| [check](https://pip.pypa.io/en/stable/cli/pip_check/)    | Verifica si los paquetes instalados tienen dependencias compatibles. |
| `completion` | Un comando de ayuda utilizado para la finalización del comando. |
| [config](https://pip.pypa.io/en/stable/cli/pip_config/)   | Administra la configuración local y global. |
| [debug](https://pip.pypa.io/en/stable/cli/pip_debug/)    | Muestra información útil para la depuración. |
| [download](https://pip.pypa.io/en/stable/cli/pip_download/) | Descarga paquetes. |
| [freeze](https://pip.pypa.io/en/stable/cli/pip_freeze/)   | Imprime los paquetes instalados en formato de requisitos. |
| [hash](https://pip.pypa.io/en/stable/cli/pip_hash/)     | Calcula los _hash_ de los archivos de los paquetes. |
| `help`     | Muestra ayuda para los comandos. |
| `index`    | Inspecciona la información disponible de los índices de paquetes. |
| [inspect](https://pip.pypa.io/en/stable/cli/pip_inspect/)  | Inspecciona el entorno de Python. |
| [install](https://pip.pypa.io/en/stable/cli/pip_install/)  | Instala y actualiza paquetes. |
| [list](https://pip.pypa.io/en/stable/cli/pip_list/)     | Lista los paquetes instalados. |
| [show](https://pip.pypa.io/en/stable/cli/pip_show/)     | Muestra información sobre los paquetes instalados. |
| [uninstall](https://pip.pypa.io/en/stable/cli/pip_uninstall/) | Desinstala paquetes. |
| [wheel](https://pip.pypa.io/en/stable/cli/pip_wheel/)    | Construye _wheels_ a partir de sus requisitos. |


:::{warning}
En las secciones siguientes se revisarán algunos comandos, pero no todos. Para más información de cada comando seguir el link de cada comando para revisar su documentación.
:::

<br/>

## _freeze_

[freeze](https://pip.pypa.io/en/stable/cli/pip_freeze/): Imprime los paquetes instalados en formato de archivo de requisitos.

:::{note}
Este comando se usa para generar el archivo de requisitos que posteriormente se puede usar para instalar paquetes en otro entorno.
:::

```sh
# Sintaxis de llamanda
pip freeze [options]
```
**Opciones**
- `-r, --requirement <file>`: Usa el orden en el archivo de requisitos dados y sus comentarios al generar salida. Esta opción se puede usar varias veces.
- `-l, --local`: Si en un _virtualenv_ que tiene acceso global, no imprime los paquetes instalados a nivel global.
- `--user`: Solo imprimr paquetes instalados en el sitio del usuario (_user-site_).
- `--path <path>`: Restringe a la ruta de instalación especificada para el listados de paquetes (se puede usar varias veces).
- `--all`: No omite estos paquetes en la salida: _pip, wheel, distribute, setuptools_.
- `--exclude-editable`: Excluye el paquete _editable_ de la salida.
- `--exclude <package>`: Excluye el paquete especificado de la salida.

**Patrones útiles**:

A continuación se presentan algunos casos de uso comunes.

```sh
# Generar archivo de requisitos
pip freeze > requirements.txt
```

<br/>

## _help_

`help`: Muestra ayuda para los comandos.

```sh
# Sintaxis de llamanda
pip help <command>
```
- _\<command>_: Es el nombre del comando del cual se desea retornar ayuda.

<br/>

## _install_

[install](https://pip.pypa.io/en/stable/cli/pip_install/): Instala y actualiza paquetes de:
- _PyPi_ (y otros _indexes_) usando especificadores de requisitos.
- URLs de proyectos _VCS_
- Directorios de proyectos locales.
- Archivos _source_ locales o remotos.

:::{attention}
Para más información consultar la documentación de _pip_ o usar `pip install -h` o `pip help install`.
:::

:::{tip}
Es posible instalar paquetes desde un archivo de requisitos que contiene un listado de paquetes con sus respectivas versiones mínimas.
:::

```sh
# Sintaxis de llamadas
pip install [options] <requirement specifier> [package-index-options] ...
pip install [options] -r <requirements file> [package-index-options] ...
pip install [options] [-e] <vcs project url> ...
pip install [options] [-e] <local project path> ...
pip install [options] <archive url/path> ...
```
- **Opciones del índice de Paquetes**:
    - `-i, --index-url <url>`: URL base del índice de paquetes de Python (default: https://pypi.org/simple).
    - `--extra-index-url <url>`: URL adicionales de índices de paquetes para usar además de `--index-url`.
    - `--no-index`: Ignora el índice de paquetes (solo mira las URL de `--find-links` en su lugar).
    - `-f, --find-links <url>`: Si es una URL o ruta a un archivo HTML, analiza los enlaces a archivos como los archivos _sdist_ (_.tar.gz_) o _wheel_ (_.whl_). 
- **Opciones**
    - `-r, --requirement <file>`: Instalar desde el archivo de requisitos especificado.
    - `-c, --constraint <file>`: Restringir versiones usando el archivo de restricciones especificado.
    - `--no-deps`: No instalar dependencias del paquete.
    - `--pre`: Incluir versiones preliminares y de desarrollo. Por defecto, pip solo encuentra versiones estables.
    - `-e, --editable <path/url>`: Instalar un proyecto en modo editable (modo "develop" de setuptools) desde una ruta de proyecto local o una URL de VCS.
    - `--dry-run`: No instalar nada, solo imprimir lo que se haría. Puede usarse junto con `--ignore-installed` para "resolver" los requisitos.
    - `-t, --target <dir>`: Instalar paquetes en `<dir>`. No reemplaza archivos/carpetas existentes a menos que se use `--upgrade`.
    - `--platform <platform>`: Usar solo _wheels_ compatibles con `<platform>`. Por defecto, usa la plataforma del sistema en ejecución.
    - `--python-version <python_version>`: Versión de Python a usar para comprobaciones de compatibilidad con _wheels_ y _Requires-Python_.
    - `--implementation <implementation>`: Usar solo _wheels_ compatibles con la implementación de Python `<implementation>` (ej. 'pp', 'jy', 'cp', 'ip').
    - `--abi <abi>`: Usar solo _wheels_ compatibles con el ABI de Python `<abi>` (ej. 'pypy_41'). Si no se especifica, se usa el ABI del intérprete actual.
    - `--user`: Instalar en el directorio de usuario de Python en lugar del sistema.
    - `--root <dir>`: Instalar todo en un directorio raíz alternativo.
    - `--prefix <dir>`: Prefijo de instalación donde se colocan `lib`, `bin` y otras carpetas de nivel superior.
    - `--src <dir>`: Directorio donde se almacenan proyectos editables.
    - `-U, --upgrade`: Actualizar todos los paquetes especificados a la versión más reciente disponible.
    - `--upgrade-strategy <upgrade_strategy>`: Determina cómo se maneja la actualización de dependencias (por defecto: `only-if-needed`).
    - `--force-reinstall`: Reinstalar todos los paquetes, incluso si ya están actualizados.
    - `-I, --ignore-installed`: Ignorar paquetes instalados y sobrescribirlos.
    - `--ignore-requires-python`: Ignorar la información de _Requires-Python_.
    - `--no-build-isolation`: Deshabilitar la construcción en un entorno aislado para distribuciones modernas.
    - `--use-pep517`: Usar PEP 517 para construir distribuciones desde código fuente (usar `--no-use-pep517` para forzar el comportamiento heredado).
    - `--check-build-dependencies`: Verificar dependencias de compilación cuando se usa PEP 517.
    - `--break-system-packages`: Permitir que pip modifique una instalación de Python marcada como `EXTERNALLY-MANAGED`.
    - `-C, --config-settings <settings>`: Configuraciones a pasar al _backend_ de compilación PEP 517.
    - `--global-option <options>`: Opciones globales adicionales para `setup.py` antes de ejecutar `install` o `bdist_wheel`.
    - `--compile`: Compilar archivos de código fuente de Python a bytecode.
    - `--no-compile`: No compilar archivos de código fuente de Python a bytecode.
    - `--no-warn-script-location`: No advertir cuando se instalan scripts fuera del `PATH`.
    - `--no-warn-conflicts`: No advertir sobre dependencias en conflicto.
    - `--no-binary <format_control>`: No usar paquetes binarios (_wheels_).
    - `--only-binary <format_control>`: No usar paquetes fuente (_source distributions_).
    - `--prefer-binary`: Preferir paquetes binarios sobre paquetes fuente, incluso si los paquetes fuente son más recientes.
    - `--require-hashes`: Requerir un _hash_ para verificar cada requisito, asegurando instalaciones repetibles.
    - `--progress-bar <progress_bar>`: Especifica si se debe usar la barra de progreso \[`on`, `off`, `raw`] (por defecto: `on`).
    - `--root-user-action <root_user_action>`: Acción si pip se ejecuta como usuario root \[`warn`, `ignore`] (por defecto: `warn`).
    - `--report <file>`: Generar un archivo JSON que describa lo que pip hizo para instalar los requisitos.
    - `--no-clean`: No limpiar los directorios de compilación.

**Patrones útiles**:

A continuación se presentan algunos casos de uso comunes.

```sh
# Instalar paquete por su nombre
pip install pkg_name

# Instalar más de un paquete por su nombre
pip install pkg_name1, pkg_name2, ...

# Instalar paquete con versión específica
pip instal pkg_name=='MAJOR.MINOR.PATCH'

# Instalar paquete con versión mínima
pip instal pkg_name>='MAJOR.MINOR.PATCH'

# Instalar paquete con un archivo de requisitos
pip install -r requirements.txt

# Actualizar un paquete
pip install --upgrade pkg_name

# Actualizar pip
pip install --upgrade pip

# Instalar paquete de GitHub
pip install git+https://github.com/pypa/sampleproject.git@main

# Instalar paquete de un archivo de distribución
python -m pip install sampleproject-1.0.tar.gz
python -m pip install sampleproject-1.0-py3-none-any.whl
```
- _pkg_name_ es el nombre del paquete como _numpy_, _pandas_, _scipy_, etc.
- Para más ejemplos consultar la [documentación](https://pip.pypa.io/en/stable/cli/pip_install/#examples) de _pip_.

<br/>

## _list_

[list](https://pip.pypa.io/en/stable/cli/pip_list/): Lista los paquetes instalados. Los paquete se enlistan en orden alfabético.

```sh
# Sintaxis de llamadas
pip list [options]
```
**Opciones**
- `-o, --outdated`: Lista de paquetes obsoletos.
- `-u, --uptodate`: Lista de paquetes actualizados.
- `-e, --editable`: Lista de proyectos editables.
- `-l, --local`: Si en un _virtualenv_ que tiene acceso global, indica que no se enlisten paquetes de instalación global.
- `--user`: Solo imprime paquetes instalados en el sitio del usuario (_user-site_).
- `--path <path>`: Restringe a la ruta de instalación especificada para el listado de los paquetes.
- `--pre`: Incluye versiones _pre-release_ y desarrollo. Por default, _pip_ solo encuentra versiones estables.
- `--format <list_format>`: Selecciona el formato de salida entre: _columns_ (default), _freeze_ o _json_.
- `--not-required`: Lista de paquetes que no son dependencias de los paquetes instalados.
- `--exclude-editable`: Excluye el paquete editable de la salida.
- `--include-editable`: Incluye un paquete editable en la salida.
- `--exclude <package>`: Excluye el paquete especificado de la salida.

**Patrones útiles**:

A continuación se presentan algunos casos de uso comunes.

```sh
# Enlistar paquetes instalados
pip list

# Enlistar paquetes obsoletos como columnas
pip list --outdated --format columns
```

<br/>

## _uninstall_

[uninstall](https://pip.pypa.io/en/stable/cli/pip_uninstall/): Desinstala paquetes.

```sh
# Sintaxis de llamada
pip uninstall [options] <package> ...
pip uninstall [options] -r <requirements file> ...
```
**Opciones**
- `-r, --requirement <file>`: Desinstala todos los paquetes enlistados en el archivo de requisitos dado.
- `-y, --yes`: No solicita la confirmación de las eliminaciones de desinstalación.
- `--root-user-action <root_user_action>`: Acción si _pip_ se ejecuta como un _root user_ \[_warn, ignore_] (default: _warn_).
- `--break-system-packages`: Permite que _pip_ modifique una instalación de Python administrada externamente.

**Patrones útiles**:

A continuación se presentan algunos casos de uso comunes.

```sh
# Desinstalar un paquete
pip uninstall pkg_name
```
- _pkg_name_ es el nombre del paquete como _numpy_, _pandas_, _scipy_, etc.