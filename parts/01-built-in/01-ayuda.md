# Obtener ayuda

Para obtener ayuda sobre algún objeto usar la función `help()` o el operador `?`:
```python
# Obtener ayuda de "object".
help(object) # Esto equivale a usar: object?
```
- `object` es la instancia, clase, función, método, etc.

---
## Clases:

Al consultar la ayuda de una clase se retorna una descripción, los atributos, métodos, etc. La forma como se indique la clase depende si es built-in o es importada. Si es importada se debe de poner tal cual como fue importada. Ejemplos:

```python
import pandas as pd

# Una clase built-in
help(str)

# Una clase de un módulo importado con un alias
help(pd.DataFrame)
```

---
## Funciones

Al consultar la ayuda de una función se retorna el "docstring", los parámetros, el objeto retornado, etc. Se pone el nombre de la función sin paréntesis. Si es importada se debe de poner la librería o módulo o el alías con la que se importó la librería o módulo. Ejemplos:

```python
import pandas as pd
from numpy import random

# Función built-in
help(print)

# Función de una librería importada con un alias
help(pd.read_csv)

# Función de un módulo importado de una librería
help(random.choice)
```

---
## Métodos y atributos

Retorna información sobre los métodos, sus argumentos y valores retornados o información sobre el atributo. Se pone la clase, punto y el nombre del atributo o método, este último sin paréntesis. Ejemplos:

```python
import pandas as pd

# Método de una clase built-in
help(str.upper)

# Atributo de una clase importada
help(pd.Series.size)

# Método de una clase importada:
help(pd.Series.to_numpy)
```

---
## Enlistar métodos y atributos de clases:

Para conocer todos las funciones que tiene una librería o todos los métodos y atributos que tiene una clase usar la función `dir()`. Algunos ejemplos:
```python
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
```
