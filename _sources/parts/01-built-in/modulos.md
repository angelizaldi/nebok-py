# Paquetes y Módulos

Un **módulo** es un archivo de Python, con extensión _.py_, que contiene una seríe de funciones, variables y/o contantes. Un **paquete** es un conjunto de módulos. Es posible importar módulos y paquetes a un script para tener acceso a todo el contenido del módulo o paquete.

```{attention} Antes de importar un módulo/paquete externo se tuvo que haber instalado.
```

Para importar un paquete se usa la palabra reservada `import`:
```python
# Importar paquete
import package_name
```
- _package_name_ es el nombre del paquete.
- Al importar un paquete de esta forma, para usar los objetos es necesario poner el nombre del paquete antes del nombre del objeto: <br/> `package_name.object_name`.

<br/>

## Opciones de importación

A continuación se presentan algunas opciones a la hora de importar un módulo/paquete.

**1**. Se puede importar el módulo/paquete con un nombre distinto usando `as`:
```python
# Importar paquete con alias
import package_name as alias
```
- _package_name_ es el nombre del módulo.
- _alias_ es un nombre arbitrario.
- Al importar un paquete de esta forma, para usar los objetos es necesario poner el alias del paquete antes del nombre del objeto: <br/> `alias.object_name`.

<br/>

**2**. Se puede importar un módulo específico de un paquete:
```python
# Importar módulo de un paquete
import package_name.module_name

# Importar módulo de un paquete con un alias
import package_name.module_name as alias
```
- _package_name_ es el nombre del paquete.
- _module_name_ es el nombre del módulo.
- _alias_ es un nombre arbitrario opcional.
- Al importar un paquete de esta forma, para usar los objetos del módulo es necesario poner el nombre del paquete y módulo o alias del módulo antes del nombre del objeto: <br/> `package_name.module_name.object_name`  <br/> `alias.object_name`


<br/>

**3**. Se puede importar uno o más objetos en específico de la siguiente manera:
```python
# Importar objetos especificos de un paquete
from package_name import obj1, obj2, ...

# Importar objetos especificos de un módulo de un paquete
from package_name.module_name import obj1, obj2, ...
```
- _package_name_ es el nombre del paquete.
- _module_name_ es el nombre del módulo.
- _obji_ es el nombre del objeto _i_. 
- Si se importa un objeto de esta forma se puede usar directamente en el _script_ únicamente con el nombre del objeto, sin hacer referencia al paquete/módulo: <br/> `obj_name`

<br/>

**4**. Se pueden importar todos los objetos (funciones, constantes, etc.) de un paquete o módulo:
```python
# Importar todo de un paquete
from package_name import *

# Importar todo de un módulo
from package_name.module_name import *
```
- No es una buena practica importar de esta manera.
- Si se importa el contenido de un paquete/módulo de esta forma se pueden usar los objetos directamente en el _script_ únicamente con el nombre de los mismos, sin hacer referencia al paquete/módulo. <br/> `obj_name`

<br/>

---
## Módulos locales

Se puede importar un archivo de python (_.py_) local a la sesión para poder utilizar las constantes, funciones, etc. definidas en el archivo. Para ello el archivo debe de estar en el directorio de la sesión y simplemente importarlo como un módulo.
```python
# Ejemplos de importación de un script local
import script
import script as alias
from script import obj1, obj2, ...
```
- _script_ es el nombre del archivo _.py_ en el mismo directorio.
- _obji_ son funciones, constantes, etc. en el archivo.
