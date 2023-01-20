#!/usr/bin/env python
# coding: utf-8

# # Cadenas
# 
# El tipo de dato `str` almacenan una secuencia de caracteres encerrados en comillas dobles o simples. `str` es considerado una secuencia. Sus principales características son:
# - Es inmutable: No se puede modificar una vez creada.
# - Está indexado: Sus elementos están ordenados.
# - Es un iterable: Se puede iterar por sus elementos y se puede utilizar la palabra reservada `in` para verificar membresía.
# - Se puede hacer _subsetting_ y _slicing_ de sus caracteres.
# - Se puede concatenar con otras cadenas.

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

# ### Unicode
# 
# Se utiliza para poder ingresar letras con acentos como á, ä, à, ñ u otros símbolos etc. Se utilizan los códigos unicode, que se pueden consultar en [códigos unicode](https://unicode-table.com/es/#basic-latin).
# 
# Para insertar códigos unicode se debe de poner el código dentro de una cadena con prefijo `u` y el código se pone como `\u_code_`, donde `_code_` es el código de unicode:

# In[1]:


# Ingresando un espacio en blanco y el signo ! con códigos unicode:
print(u"Hello\u0020World\u0021") 


# ### Raw strings
# 
# Son cadenas “crudas”, que ignoran _caracteres ilegales_ como `\n` y los imprime tal cual. Para crear una cadena cruda se utiliza una `r` como prefijo de la cadena.

# In[2]:


# Una cadena normal
print("text1 \ttext2")

# Una cadena cruda
print(r"text1 \ttext2")


# Los caracteres ilegales son:
# - `\’`: Comilla simple.
# - `\”`: Comilla doble.
# - `\n`: Salto de línea.
# - `\t`: Tabulación.
# - `\\`: Diagonal inversa.
# - `\b`: Un espacio en blanco para atrás.
# - `\xhh`: Valor hexadecimal.
# 

# ---
# ## Concatenar cadenas:
# Para concatenar cadenas se usa el operador `+`. Usar únicamente con objetos de tipo `str`:

# In[3]:


x = "Hello"
y = "World!"
print(x + " " + y)


# `str` tiene además el método `join`para concatenar que se ve con más profundidad en "ref".

# Para concatenar una misma cadena `n ` veces usar el operador de multiplicación `*` con la cadena:

# In[4]:


"text " * 5


# ---
# ## Verificar membresía
# 
# Se puede verificar que un patrón esté dentro de una cadena con los operadores `in` y `not in`, retornando un valor lógico. El patrón no tiene porque ser una palabra exacta, pueden ser partes de palabras, palabras o frases.
# ```python
# "pattern" in "string"
# "pattern" not in "string"
# ```
# Ejemplos:

# In[5]:


text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
print("amet" in text)
print("minim" in text)


# ---
# ## Iteración
# 
# Las cadenas son una secuencia, esto permite que se puede usar una cadena como el rango en un `for loop`, iterando caracter por caracter:
# ```python
# for i in string:
#     expression
# ```
# 
# Ejemplo:

# In[6]:


for char in "abc":
    print(char)


# ---
# ## Selección de elementos: 
# 
# ### Subsetting:
# Si `X` es `str` e `i` es un número entero, entonces para seleccionar caracyeres de una cadenas tener en cuenta las siguientes características: 
# - Se utilizan corchetes `[]` para acceder a los elementos, junto con el nombre de la variable y el índice del elemento: <br/>
# `X[i]`
# - Los índices comienza en cero (0), esto quiere decir que si quiere acceder al elemento `i`, se debe de usar `[i-1]`.
# - Se puede utilizar números negativos, de manera que se comience por el último elemento. Se puede acceder al último caracter con `[-1]`, al penúltimo caracters `[-2]`, etc.
# 
# ---
# ### Slicing:
# Si `X` es `str` e `i`, `j` y `k` son números entonces, entonces:
# - Para seleccionar un rango de caracteres consecutivos se utiliza dos puntos: <br/> `X[i:j]`
# - La selección por rango, tienen la característica que el primer elemento es inclusivo y el último es exclusivo, esto quiere decir que no se incluirá en el rango, si se usa el rango `[i:j]`, en realidad solo se accederá a `[i:j-1]`.
# - Desde el índice `i` hasta el `j`, sin incluir el `j`: <br> `X[i:j]`
# - Desde el inicio hasta el `j`, sin incluir el `j`: <br> `X[:j]`
# - Desde la posición `i` hasta el final de la cadena: <br>`X[i:]`
# - Toda la cadena: <br> `X[:]`
# - Desde el índice `i` hasta el `j`, sin incluir el `j`, cada `k` caracteres: <br> `X[i:j:k]`
# 
# Algunos patrones útiles:
# - El primer caracter: <br> `X[0]`
# - El último caracter: <br> `X[-1]`
# - Toda la cadena cada `k` caracteres: <br> `X[::k]`
# - Toda la cadena al revés: <br> `X[::-1]`
# 
# 

# In[7]:


# Ejemplos
X = "aeiou"

# Primer caracter
print(X[0])

# Penúltimo caracter
print(X[-2])

# Del ínidice 0 al 2
print(X[0:3])

# La cadena al revés cada 2 caracteres
print(X[::-2])


# ---
# ## Convertir otro tipo de secuencia:
# 
# Se puede convertir una cadena a cualquier otro tipo de secuencia, donde cada elemento de la secuencia será cada caracter de la cadena con las funciones `list()` y `tuple()`.
# ```python
# list(X)
# tuple(X)
# ```
# - `X` \- `str`.
# 
# 
