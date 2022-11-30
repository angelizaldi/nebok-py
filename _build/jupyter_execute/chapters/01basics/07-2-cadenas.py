#!/usr/bin/env python
# coding: utf-8

# # Cadenas
# 
# El tipo de dato es `str`, almacenan cadenas de caracteres.
# - Sus elementos están ordenados (indexados).
# - No se puede modificar una vez creada.
# 
# 
# 
# Existen unas cadenas especiales:
# ```python
# #Unicode
# X = u'text'
# #Raw string
# X = r'text'
# #Bytes string
# X = b'text'
# ```
# 
# **Unicode**
# Es para poder ingresar letras con acentos como á, ä, à, ñ u otros símbolos etc. Se utilizan los códigos unicode, que se pueden consultar en [códigos unicode](https://unicode-table.com/es/#basic-latin).
# 
# Para insertar códigos unicode se debe de poner el código dentro de una cadena con prefijo `u` y el código se pone como `\u_code_`, donde `_code_` es el código de unicode:

# In[1]:


# Ingresando un espacio en blanco y el signo ! con códigos unicode:
print(u"Hello\u0020World\u0021") 


# **Raw string** Son cadenas “crudas”, que ignoran caracteres especiales como `\n` y los imprime tal cual. Para saber más sobre caracteres especiales consulta 

# In[2]:


# Una cadena normal
print("text1 \ntext2")


# In[3]:


# Una cadena cruda
print(r"text1 \ntext2")


# ---
# ## Crear una cadena
# 
# Para crear una variable de tipo de cadena usar comillas dobles o comillas simples para abrir y cerrar la cadena:
# ```python
# x = "text"
# x = 'text'
# ```
# 
# Para crear una cadena de mútiples líneas usar tres comillas dobles o tres comillas simples para abrir y cerrar la cadena:
# ```python
# x = """
#     text
#     more text
#     """
#      
# x = '''
#     text
#     more text
#     '''
# ```
# - Los saltos de línea (`\n`) se respetarán en la cadena.

# ---
# ## Concatenar cadenas:
# Para concatenar cadenas se usa el operador `+`. Ya sea que se ponga la cadena tal cual o una variable de tipo `str`:

# In[4]:


x = "Hello"
y = "World!"
print(x+" "+y)


# `str` tiene además el método `join`para concatenar que se ve con más profundidad en "ref".

# ---
# ## Repetir cadenas:
# 
# Para repetir una cadena `n ` veces usar el operador de multiplicación `*` con la cadena:

# In[5]:


"text " * 5


# ---
# ## Verificar membresía de patrones
# 
# Se puede verificar que un patrón esté dentro de una cadena con los operadores `in` y `not in`, retornando un valor lógico. El patrón no tiene porque ser una palabra exacta, pueden ser partes de palabras o más de un palabra.
# ```python
# "pattern" in "string"
# "pattern" not in "string"
# ```
# Ejemplos:

# In[6]:


text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
print("amet" in text)
print("minim" in text)


# ---
# ## Iterar sobre una cadena.
# 
# Las cadenas se pueden manipular como una secuencia. Esto permite que se puede usar una cadena como el rango en un `for loop`, iterando caracter por caracter:
# ```python
# for i in string:
#     expression
# ```
# 
# Ejemplo:

# In[7]:


for char in "abc":
    print(char)


# ---
# ## Subsetting y slicing.
# 
# Al ser `str` una secuencia se pueden extraer elementos y rangos de una cadena usando corchetes. La idexación comienza en 0 y termina en `N-1`, siendo `N` la longitud de la cadena. También es posible usar números negativos ,siendo -1 igual a la última posición, -2 la penúltima posición, etc.
# 
# Si `text` es un objeto de tipo `str` entonces, para hacer subsetting y slicing se usa:
# - Un caracter específico: <br> `text[i]`
# - Un caracter específico, empezado desde el final, de derecha a izquierda: <br> `text[-i]`
# - Desde el índice `i` hasta el `j`, sin incluir el `j`: <br> `text[i:j]`
# - Desde el inicio hasta el `j`, sin incluir el `j`: <br> `text[:j]`
# - Desde la posición `i` hasta el final de la cadena: <br>`text[i:]`
# - Toda la cadena: <br> `text[:]`
# - Desde el índice `i` hasta el `j`, sin incluir el `j`, cada `k` caracteres: <br> `text[i:j:k]`
# 
# Algunos patrones útiles:
# - El primer caracter: <br> `text[0]`
# - El último caracter: <br> `text[-1]`
# - Toda la cadena cada `k` elementos: <br> `text[::k]`
# - Toda la cadena al revés: <br> `text[::-1]`
# 

# ---
# ## Convertir una cadena a una secuencia:
# Se puede convertir una cadena en una secuencia, donde cada elemento de la secuencia será cada caracter de la cadena con las funciones `list()` y `tuple()`.
# ```python
# list(X)
# tuple(X)
# ```
# - `X` \- `str`.
# 
# 

# In[ ]:




