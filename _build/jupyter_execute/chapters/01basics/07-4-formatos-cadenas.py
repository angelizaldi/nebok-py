#!/usr/bin/env python
# coding: utf-8

# # Formatos de cadenas.
# 
# En esta sección se explica el método `str.format()` y las "f-strings" que permiten darle un formato personalizado a las cadenas e incluir de manera dinámica variables en la cadena.
# 
# ```{attention} Existen otros métodos para hacer lo mismo como los `string.Template` o usando el operador `%`, pero no se cubrirán en esta página.
# ```

# ## str.format

# Es un método que sirve para imprimir valores de variables en algún formato en específico. Para ello en la cadena se deben especificar campos delimitados por corchetes `{}` donde irán los valores.
# 
# `str.format()`: Da formato a una cadena.
# ```python
# X.format(*args, **kwargs)
# ```
# **Parámetros:**:
# - `*args`: Valores o variables a reemplazar en la cadena. Se puede incluir cualquier tipo de objeto que se pueda imprimir, el valor mostrado será el mismo que el del método `__str__()` o `__repr__()` de la clase del objeto.
# 
# **Retorna:**
# - `str`.
# 
# **Ejemplo:**

# In[1]:


x = "World!"
print("Hello {0}".format(x))


# ---
# ### Uso
# 
# Existen tres formas principales de usar este método:
# 
# **índices**
# 
# - Dentro de la cadena se puede usar `{0}`, `{1}`, `{2}`, …, que serviría para indicar que se empaten por el índice correspondiente con los argumentos de `str.format()`. 
# - Se puede poner más de una vez algún índice `{i}`, de manera que lo imprima más de una vez en una misma cadena. - - Los índice comienzan en cero.
# - Si no se indican los índices se empatan por posición los argumentos y los campos `{}`, pero el número de corchetes debe ser igual al número de argumentos.
# 
# Ejemplos:

# In[2]:


x1 = "texto"
x2 = 10.0
x3 = True
cadena = "Una cadena: {}\nun número: {}\nun valor booleano: {}"
print(cadena.format(x1, x2, x3))


# ---
# **nombres**
# 
# - En la cadena, los campos `{}` deben de tener nombres los cuales se deben especificar en `str.format()` como par  `name=val`.
# 
# Ejemplo:

# In[3]:


x1 = "texto"
x2 = 10.0
x3 = True
cadena = "Una cadena: {string}\nun número: {number}\nun valor booleano: {boolean}"
print(cadena.format(string=x1, number=x2, boolean=x3))


# ---
# **diccionario**
# 
# - El argumento de `str.format()` es un diccionario y en los campos `{}` se accede a los valores del diccionario recuperando el valor con los nombres de las llaves del diccionario. 
# - Los nombres de las llaves dentro de la cadena no se deben de poner entre comillas.
# 
# Ejemplo:

# In[4]:


my_dict = {"string": "texto", "number": 10.0, "boolean": True}
cadena = "Una cadena: {x[string]}\nun número: {x[number]}\nun valor booleano: {x[boolean]}"
print(cadena.format(x=my_dict))


# ---
# ## f-strings
# 
# Es una alternativa al método `str.format()`, está disponible en Python 3.6+. Requiere una sintaxis más sencilla y es más rápida, para ello se agrega el prefijo `f` a una cadena:
# 
# **Sintaxis**:
# ```python
#     f"text ... {expression} .."
# ```
# 
# **Parámetros:**
# - <code><i>expression</i></code>: Es un valor, un objeto o incluso funciones y/o métodos que retornen un objeto imprimible. El valor mostrado será el mismo que el del método `__str__()` o `__repr__()` de la clase del objeto.
# 
# **Ejemplo:**

# In[5]:


x=10.0
y=True
f"Esto es un número {x} y esto un valor booleano {y}"


# Se puede relaizar una conversión en la cadena, algunas conversiones disponibles son:
# - `!s`: Version en cadena.
# - `!r`: Cadena en versión imprimible, es decir, entre comillas, (solo funciona si la expresión es `str`).
# - `!a`: Como `!r` pero ignora los caracteres non-ASCII.
# 
# **Ejemplos:**

# In[6]:


x = 10
y = "texto"
print(f"Convertir a cadena {x!s}")
print(f"Texto entre comillas: {y!r}")


# **Formatos**
# 
# Para dar formatos, se utiliza dos puntos y el formato que se quiere dar:
# ```python
# 	f"text ... {expression:format}"
# ```
# - <code><i> format </i></code>: Es el formato que se quiere dar. Revisar formatos de cadenas.
# 
# **Ejemplo**:

# In[7]:


x = 1897.9876
print(f"Sin formato: {x}")
print(f"Separar los miles: {x:,}")
print(f"Notación científica con 1 décimal: {x:.1e}")
print(f"Con tres décimales (redondea) {x:.3f}")
print(f"Combinación de separación de miles y 2 décimales:{x:,.2f}")


# In[ ]:




