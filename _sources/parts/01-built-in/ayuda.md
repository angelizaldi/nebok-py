# Obtener ayuda

Para obtener ayuda sobre algún objeto usar la función `help()` o desde {doc}`../appendix/IPython` también se puede usar el operador `?`. 

Se puede consultar ayuda sobre diversos objetos y elementos:
- Paquetes y Módulos.
- Clases.
- Funciones.
- Métodos y atributos de clases.
- Instancias de clases.
- Métodos y atributos de instancias de clases.
- _Keywords_, como por ejemplo `'if'`, `'for'`, `'def'`, etc. Notar que se deben de poner como una cadena.
- Excepciones.
- Documentación interactiva: Existe ayuda para determinados temas (notar que se deben de poner como una cadena) enlistando los distintos elementos del tema, que a su vez se puede obtener más información sobre cada uno de los elementos ya sea llamando de nuevo a la función o si se está en una sesión interactiva escribiendo directamente el elemento (ver tip):
    - _'keywords'_: Enlistará las palabras reservadas en Python.
    - _'topics'_: Enlistará algunos temas de interés como _Assertion_, _Looping_, _Types_, entre muchos otros.
    - _'modules'_: Enlistará los módulos disponibles en la sesión actual.
    - _'builtins'_: Enlistará y mostrará información sobre funciones, exepciones y otros objetos integrados en Python.
    - _'types'_: Enlistará y mostrará información sobre los tipos de datos de Python.
 
:::{tip}
Si se usa en la consola la función sin argumentos se iniciará una sesión interactiva de la ayuda de Python, que permitirá explorar los diversos temas anteriormente enlistados de una manera más interactiva y sin necesidad de tener que estar escribiendo `help()` en cada ocasión.

<code> help() </code> </br>
- Para salir de la sesión escribir `quit`.
:::

**Ejemplos**:
```python
# Importar algunos paquetes y módulos
import math
import pandas as pd
from numpy import random

# Obtener ayuda de un paquete importado
help(math) # En IPython ?math

# Obtener ayuda de de un paquete importado con un alias
help(pd) # ?pd

# Obtener ayuda de un módulo importado de una librería
help(random) # ?random

# Obtener ayuda de una clase built-in
help(str) # ?str

# Obtener ayuda de una clase importada.
help(pd.Series) #pd.Series

# Obtener ayuda de una instancia.
x = list([0, 1, 2, 3, 4, 5])
help(x) # ?x

# Obtener ayuda de una función built-in.
help(zip) # ?zip

# Obtener ayuda de una función importada.
help(math.cos) # ?math.cos

# Ayuda sobre una palabra reservada
help('for')

# Ayuda sobre los tipos de datos
help('types')
```


---
## Enlistar métodos y atributos de clases

Para conocer todos las funciones y constantes que tiene una librería o todos los métodos y atributos que tiene una clase o una instancia de clase usar la función `dir()`. Algunos ejemplos:

```python
# Importar algunas librerias
import math
import pandas as pd
from numpy import random

# Enlistar todas las funciones y clases de un paquete importado
dir(math)

# Enlistar todas las funciones y clases de un paquete importado con un alias:
dir(pd)

# Enlistar todas las funciones y clases de un módulo importado
dir(random)

# Enlistar todos los métodos y atributos de una clase built-in
dir(str)

# Enlistar todos los métodos y atributos de una clase importada.
dir(pd.Series)

# Enlistar todos los métodos y atributos de una instancia
x = list([0, 1, 2, 3, 4, 5])
dir(x)
```
