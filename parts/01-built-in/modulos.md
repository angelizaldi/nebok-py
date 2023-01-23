# Paquetes y Módulos.

Un **módulo** es un archivo de Python, con extensión _.py_, que contiene una seríe de funciones, variables y/o contantes. Un **paquete** es un conjunto de módulos. Es posible importar módulos y paquetes a un script para tener acceso a todo el contenido del módulo o paquete.

```{attention} Antes de importar un módulo/paquete externo se tuvo que haber instalado.
```

Para importar un paquete se usa la palabra reservada `import`.
```python
# Importar paquete
import package_name
```
- _package_name_ es el nombre del paquete.

Se puede importar el módulo/paquete con un nombre distinto usando `as`.
```python
# Importar paquete con alias
import package_name as alias
```
- _package_name_ es el nombre del módulo.
- _alias_ es un nombre arbitrario.

Se puede importar un módulo específico de un paquete
```python
# Importar módulo de un paquete con un alias
import package_name.module_name as alias
```
- _package_name_ es el nombre del paquete.
- _module_name_ es el nombre del módulo.
- _alias_ es un nombre arbitrario opcional.

Se puede importar una o más funciones en específico de la siguiente manera:
```python
# Importar funciones especificas de un paquete
from package_name import function_name_1, function_name_1, ... 

# Importar funciones especificas de un módulo de un paquete
from package_name.module_name import function_name_1, function_name_1, ...
```
- _package_name_ es el nombre del paquete.
- _module_name_ es el nombre del módulo.
- _function_name_i_ es el nombre de la función i. Se pueden importar otra clase de objetos aparte de funciones.
- Si se importa una función de esta forma no es necesario usar la notación _package_name.function_name()_, se usa directamente el nombre de la función.

Se pueden importar todas las definiciones (funciones, variables, constantes, etc.) de un paquete o módulo, de manera que no sea necesario poner el nombre del módulo antes de llamar la función usando:
```python
# Importar todo de un paquete
from package_name import *

# Importar todo de un módulo
from package_name.module_name import *
```
- No es una buena practica importar de esta manera.

---
## Utilizar las funciones, variables y/o constantes de un módulo:

Para utilizar las funciones, variables y/o constantes de un módulo o paquete importado se tiene que usar el nombre del paquete/módulo o aquel que se le asignó con `as`, seguido de un punto ‘.’, seguido del nombre de la función con sus respectivos argumentos (si existen).
```python
# Usando funciones u otros objetos importados
package_name.module_name.function_name(args)
package_name.module_name.variable_name
```
- Este es un ejemplo general, la sintaxis dependerá de cómo se importó el paquete, módulo o función/objeto.
   
---
## Módulos locales:

Se puede importar un archivo de python (_.py_) local a la sesión para poder utilizar las constantes, funciones, etc. definidas en el archivo. Para ello el archivo debe de estar en el directorio de la sesión y simplemente importarlo como un módulo.
```python
# Ejemplos de importación de un script local
import script
import script as alias
from script import obj1, obj2, ...
```
- _script_ es el nombre del archivo .py en el mismo directorio.
- _obji_ son funciones, constantes, etc. en el archivo.
