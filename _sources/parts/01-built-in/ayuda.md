# Obtener ayuda

Para obtener ayuda sobre algún objeto usar la función `help()` o el operador `?`. Ejemplos:
```python
# Importar algunas librerias
import math
import pandas as pd
from numpy import random

# Obtener ayuda de una librería importada
help(math)

# Obtener ayuda de de una librería importada con un alias
help(pd)

# Obtener ayuda de un módulo importado de una librería
help(random)

# Obtener ayuda de una clase built-in
help(str)

# Obtener ayuda de una clase importada.
help(pd.Series)

# Obtener ayuda de un objeto.
x = list([0, 1, 2, 3, 4, 5])
help(x)

# Obtener ayuda de una función built-in.
help(zip)

# Obtener ayuda de una función importada.
help(math.cos)
```
- `object` es la instancia, clase, función, método, etc.

---
## Enlistar métodos y atributos de clases

Para conocer todos las funciones y constantes que tiene una librería o todos los métodos y atributos que tiene una clase usar la función `dir()`. Algunos ejemplos:

```python
# Importar algunas librerias
import math
import pandas as pd
from numpy import random

# Enlistar todas las funciones y clases de una librería importada
dir(math)

# Enlistar todas las funciones y clases de una librería importada 
# con un alias:
dir(pd)

# Enlistar todas las funciones y clases de un módulo importado de 
# una librería
dir(random)

# Enlistar todos los métodos y atributos de una clase built-in
dir(str)

# Enlistar todos los métodos y atributos de una clase importada.
dir(pd.Series)

# Enlistar todos los métodos y atributos de un objeto
x = list([0, 1, 2, 3, 4, 5])
dir(x)
```
