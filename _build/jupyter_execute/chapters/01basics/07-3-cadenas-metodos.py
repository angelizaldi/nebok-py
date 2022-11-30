#!/usr/bin/env python
# coding: utf-8

# # Métodos de cadenas
# 
# En esta sección se explicarán algunos de los métodos de `str`, con ejemplos. Para información más detallada de todos los métodos visitar la [página](https://docs.python.org/3.8/library/stdtypes.html#string-methods) oficial.
# 
# Los ejemplos suponen que el método se aplica directamente sobre un objeto que es `str`, pero es posible usar el objeto como argumento usando x, por ejemplo, en lugar de usar `X.upper()` se puede usar:
# ```python
# str.upper(X)
# ```
# - `X` \- `str`.
# - En ese caso el primer argumento debe de ser la cadena.

# ---
# ## Buscar patrones:
# 
# Métodos para buscar
# 
# **find**
# 
# `str.find()`: Retorna la primer posición de la cadena donde se encuentra un patrón, pero si no encuentra el patrón retorna -1.
# ```python
# str.find(sub, [start=0], [end=-1])
# ```
# **Parámetros:**
# - **`sub`** \- `str`: Es el patrón a buscar.
# - **`start`**, **`end`** \- `int`: Para indicar desde cuál y hasta cuál elemento buscar el patrón, `end` es exclusivo. Por default es desde el inicio hasta el final.
# - Existe un método similar pero para devolver la última coincidencia es `str.rfind()`.
# 
# **Retorna:**
# - `int`.
# 
# **Ejemplo:**

# In[1]:


X = "Lorem ipsum dolor sit amet, consectetur sit adipiscing elit"
print(X.find("sit"))

#Retorna -1
print(X.find("totam"))


# ---
# **index**
# 
# `str.index()`: Retorna la primer posición de la cadena donde se encuentra un patrón. Si no encuentra el patrón retorna un error `ValueError`. 
# ```python
# str.index(sub, [start=0], [end=-1])
# ```
# **Parámetros:**
# - **`sub`** \- `str`: Es el patrón a buscar.
# - **`start`**, **`end`** \- `int`: Para indicar desde cuál y hasta cuál elemento buscar el patrón, `end` es exclusivo. Por default es desde el inicio hasta el final.
# 
# **Retorna:**
# - `int` o `ValueError`.
# 
# **Ejemplo:**

# In[2]:


X = "Lorem ipsum dolor sit amet, consectetur sit adipiscing elit"
print(X.index("sit"))


# ```{note}
# Otros métodos para conocer información sobre búsqueda de patrones no cubiertos aquí.
# - `str.rfind()`: Como `str.find` pero retorna información de la última coincidencia.
# - `str.rindex()`: Como `str.index` pero retorna información de la última coincidencia.
# ```

# ---
# ## Información de la cadena:

# **count**
# 
# `str.count()`: Retorna el número de veces que hay un patrón en una cadena.
# ```python
# str.count(sub="pattern", [start=0], [end=-1])
# ```
# **Parámetros:**
# - **`sub`**\- `str`: Es el patrón a buscar.
# - **`star`**, **`end`**\- `int`: Para indicar desde cuál y hasta cuál elemento buscar el patrón. Por default es desde el inicio hasta el final.
# 
# **Retorna:**
# - `int`.
# 
# **Ejemplo:**

# In[3]:


X = "Lorem ipsum dolor sit amet, consectetur sit adipiscing elit"
X.count("sit")


# ---
# **endswith**
# 
# `str.endswith()`: Retorna `True` si la cadena termina con algún patron en específic, `False` en caso contrario.
# ```python
# str.endswith(suffix="pattern", [start=0], [end=-1])
# ```
# **Parámetros:**
# - **`suffix`** \- `str`: Es el sufijo a buscar.
# - **`star`**, **`end`**\- `int`: Para indicar desde cuál y hasta cuál elemento buscar el patrón. Por default es desde el inicio hasta el final.
# 
# **Retorna:**
# - `bool`.
# 
# **Ejemplo:**

# In[4]:


X = "Lorem ipsum dolor sit amet, consectetur sit adipiscing elit"
X.startswith("Lor")


# ---
# **isalnum**
# 
# `str.isalnum()` \- `bool`: Retorna `True` si todos los caracteres de la cadena son alfanuméricos, `False` en caso contrario.
# ```python
# str.isalnum()
# ```
# **Parámetros:**
# - No tiene parámetros
# 
# **Retorna:**
# - `bool`.
# 
# **Ejemplo:**

# In[5]:


X = "abc123"
Y = "abc.123"

print(X.isalnum())
print(Y.isalnum())


# ---
# **isnumeric**
# 
# `str.isnumeric()` \- `bool`: Retorna `True` si todos los caracteres de la cadena son numéricos.
# ```python
# str.isnumeric()
# ```
# **Parámetros:**
# - No tiene parámetros
# 
# **Retorna:**
# - `bool`.
# 
# **Ejemplo:**

# In[6]:


X = "123456"
Y = "99.00"
Z = "123abc"

print(X.isnumeric())
print(Y.isnumeric())
print(Y.isnumeric())


# ---
# **isupper**
# 
# `str.isupper()` \- `bool`: Retorna `True` si todos los caracteres son mayúsculas y hay al menos un caracter alfabético en mayúsculas, si no, retorna `False`.
# ```python
# str.isupper() 
# ```
# **Parámetros:**
# - No tiene parámetros
# 
# **Retorna:**
# - `bool`.
# 
# **Ejemplo:**

# In[7]:


X = "ABC123"
Y = "ABc123"

print(X.isupper())
print(Y.isupper())


# ```{note}
# Otros métodos para conocer información sobre las cadenas no cubiertos aquí.
# - `str.startswith()`: Para verificar que una cadena comienza con un patrón en específico.
# - `str.isdecimal()`: Para verificar que una cadena represente una valor número décimal.
# - `str.isdigit()`: Para verificar que una cadena represente un número.
# - `str.isidentifier()`.
# - `str.islower()`: Para verificar que todos los caracteres de una cadena sean minúsculas.
# - `str.isprintable()`: Para verificar que todos los caracteres de una cadena sean imprimibles.
# - `str.isspace()`.
# - `str.istitle()`.
# ```

# ## Formato de la cadena:

# **zfill**
# 
# `str.zfill()` \- `str`: Retorna una cadena agregando ceros al principio de la cadena (si es necesario), para que tenga una longitud específica.
# ```python
# str.zfill(width)
# ```
# **Parámetros:**
# - `witdh` \- `int`: Es la longitud que se desea que tenga la cadena.
# 
# **Retorna:**
# - `str`.
# 
# **Ejemplo:**

# In[8]:


X = "Lorep"
X.zfill(10)


# ---
# **center**
# 
# `str.center()` \- `str`: Retorna una cadena agregando caracteres al princio y al final, para que tenga una longitud determinada y la cadena original esté al centro.
# ```python
# str.center(width, [fillchar = " "])
# ```
# **Parámetros:**
# - `witdh` \- `int`: Es la longitud que se desea que tenga la cadena.
# - `fillchar` \- `str`: Es el carácter que se desea agregar al principio y al final. Por default son espacios en blanco.
# 
# **Retorna:**
# - `str`.
# 
# **Ejemplo:**

# In[9]:


X = "Lorep"
print(X.center(10))
print(X.center(10, "."))


# ---
# **ljust**
# 
# `str.ljust()` \- `str`: Justifica el texto a la izquierda, agregando caracteres al final de la cadena para que tenga una longitud determinada.
# ```python
# str.ljust(width, [fillchar = " "])
# ```
# **Parámetros:**
# - `witdh` \- `int`: Es la longitud que se desea que tenga la cadena.
# - `fillchar` \- `str`: Es el carácter que se desea agregar al final. Por default son espacios en blanco.
# 
# **Retorna:**
# - `str`.
# 
# **Ejemplo:**

# In[10]:


X = "Lorep"
print(X.ljust(10))
print(X.ljust(10, "."))


# ---
# **rjust**
# 
# `str.rjust()` \- `str`: Justifica el texto a la derecha, agregando caracteres al principio de la cadena para que tenga una longitud determinada.
# ```python
# str.rjust(width, [fillchar = " "])
# ```
# **Parámetros:**
# - `witdh` \- `int`: Es la longitud que se desea que tenga la cadena.
# - `fillchar` \- `str`: Es el carácter que se desea agregar al principio. Por default son espacios en blanco.
# 
# **Retorna:**
# - `str`.
# 
# **Ejemplo:**

# In[11]:


X = "Lorep"
print(X.rjust(10))
print(X.rjust(10, "."))


# ---
# **capitalize**
# 
# `str.capitalize()` \- `str`: Convierte la cadena para que tenga la primer letra en mayúsculas y el resto en minúsculas.
# ```python
# str.capitalize()
# ```
# **Parametros:**
# - No tiene parámetros
# 
# **Retorna:**
# - `str`.
# 
# **Ejemplo:**

# In[12]:


X = "lorem ipsum dolor sit amet"
X.capitalize()


# ---
# **title**
# 
# `str.title()` \- `str`: Convierte la cadena para que tenga la primer letra de cada palabra en mayúsculas.
# ```python
# str.title()
# ```
# **Parametros:**
# - No tiene parámetros
# 
# **Retorna:**
# - `str`.
# 
# **Ejemplo:**

# In[13]:


X = "lorem ipsum dolor sit amet"
X.title()


# ---
# **lower**
# 
# `str.lower()` \- `str`: Convierte una cadena en minúsculas.
# ```python
# str.lower()
# ```
# **Parametros:**
# - No tiene parámetros
# 
# **Retorna:**
# - `str`.
# 
# **Ejemplo:**

# In[14]:


X = "LOREM IPSUM DOLOR SIT AMET"
X.lower()


# ---
# **upper**
# 
# `str.upper()` \- `str`: Convierte una cadena en mayúsculas.
# ```python
# str.upper()
# ```
# **Parametros:**
# - No tiene parámetros
# 
# **Retorna:**
# - `str`.
# 
# **Ejemplo:**

# In[15]:


X = "lorem ipsum dolor sit amet"
X.upper()


# ```{note} 
# Otros métodos para modificar el formato de las cadenas no cubiertos aquí.
# - `str.swapcase()`
# - `str.casefold()`
# ```

# ## Reemplazar patrones

# **replace**
# 
# `str.replace()` \- `str`: Sustituye un patrón por uno nuevo.
# ```python
# str.replace(old, new, [count = -1])
# ```
# **Parámetros:**
# - `old`, `new` \- `str`: Son los patrones.
# - `count` \- `int`: Indica cuántas coincidencias remplazar. Por default son todas.
# 
# **Retorna:**
# - `str`.
# 
# **Ejemplo:**

# In[16]:


X = "Lorem ipsum dolor sit amet, consectetur sit adipiscing elit"
X.replace("sit", "magni")


# ---
# **maketrans**
# 
# `str.maketrans()` \- `dict`: Mapea caracteres por otros caracteres. El objeto retornato se utiliza como argumento de `str.translate()`.
# ```python
# str.maketrans(x, [y], [z])
# ```
# **Parámetros:**
# - `x` \- `str`: Cadena con los caracteres a reemplazar.
# - `y` \- `str`: Cadena con los caracteres que reemplazarán a `x`, debe tener la misma longitud que `x`. Los caracteres se empatan por posición.
# 
# **Retorna:**
# - `dict`.
# 
# ```{attention}
# Existen otras formas de utilizar este método, pero no son cubiertas en esta página.
# ```

# ---
# **translate**
# 
# `str.translate()` \- `str`: Remplaza caracteres de acuerdo al mapeo indicado en `str.maketrans()`.
# ```python	
# str.translate(table)
# ```
# **Parámetros:**
# - `table` \- `dict`: Objeto creado con `str.maketrans`.
# 
# **Retorna:**
# - `str`.
# 
# **Ejemplo:**

# In[17]:


X = "Lorem ipsum dolor sit amet"
table = X.maketrans("aeio", "4310")
X.translate(table)


# ## Separar y Unir:

# **join**
# 
# `str.join()`: Retorna los elementos de un iterable concatenados como cadena, separados por una expresión. Es exactamente lo contrario a split().
# ```python
# "exp".join(X)
# ```
# **Parámetros:**
# - `X` \- `iterable` de `str`: Se unirá cada elemento de X con <code><i>exp</i></code>.
# - <code><i>exp</i></code> \- `str`: Es la expresión que habrá en la cadena entre cada elemento.
# 
# **Retorna:**
# - `str`.
# 
# **Ejemplo:**

# In[18]:


X = ["Hello", "World!", "from", "python"]
print(" ".join(X))
print(".".join(X))


# ---
# **split**
# 
# `str.split()`: Separa una cadena de acuerdo a un patrón y retorna una lista con las subcadenas. 
# ```python
# str.split(sep=" ", maxsplit=-1)
# ```
# **Parámetros:**
# - `sep` \- `str`: Indica el separador. Por default son espacios en blanco.
# - `maxspli` \- `int`: Indica cuántas separaciones máximas hacer, por default son todas.
# 
# **Retorna:**
# - `list`
# 
# **Ejemplo:**

# In[19]:


X = "Lorem ipsum dolor sit amet, consectetur sit adipiscing elit"
X.split()


# ```{note}
# Otro método para hacer split:
# - `str.rsplit(sep=" ", maxSplit=-1)` \- `list`: Caso especial de `split()` para que la separación se inicie desde la derecha. Si no se especifica `maxSplit` es lo mismo que `split()`.
# ```

# ## Eliminar caracteres:

# **lstrip**
# 
# `str.lstrip()` [str] `str`: Elimina los espacios en blanco o un conjunto de caracteres en específico al principio de la cadena.
# ```python
# X.lstrip([chars = ‘ ’])
# ```
# **Parámetros:**
# - `chars` \- `str`: Los caracteres a eliminar, por default son espacios en blanco. No es un patrón, se eliminan todos los caracteres que estén dentro.
# 
# **Retorna:**
# - `str`.
# 
# **Ejemplo:**

# In[20]:


X = "...Lorem ipsum dolor sit amet, consectetur sit adipiscing elit..."
X.lstrip(".")


# ---
# **rstrip**
# 
# `str.rstrip()` [str] `str`: Elimina los espacios en blanco o un conjunto de caracteres en específico al final de la cadena.
# ```python
# X.rstrip([chars = ‘ ’])
# ```
# **Parámetros:**
# - `chars` \- `str`: Los caracteres a eliminar, por default son espacios en blanco. No es un patrón, se eliminan todos los caracteres que estén dentro.
# 
# **Retorna:**
# - `str`.
# 
# **Ejemplo:**

# In[21]:


X = "...Lorem ipsum dolor sit amet, consectetur sit adipiscing elit..."
X.rstrip(".")


# ---
# **strip**
# 
# `str.strip()` [str] `str`: Elimina los espacios en blanco o un conjunto de caracteres, al principio y final de una cadena.
# ```python
# X.strip([chars = ‘ ’])
# ```
# **Parámetros:**
# - `chars` \- `str`: Los caracteres a eliminar, por default son espacios en blanco. No es un patrón, se eliminan todos los caracteres que estén dentro.
# 
# **Retorna:**
# - `str`.
# 
# **Ejemplo:**

# In[22]:


X = "...Lorem ipsum dolor sit amet, consectetur sit adipiscing elit..."
X.strip(".")


# ## Otros:
# 
# Otros métodos de cadenas no cubiertos aquí:
# - `str.encode()`.
# - `str.expandtabs()`.
# - `str.format_map()`.
# - `str.partition()`.
# - `str.rpartition()`.
# 
