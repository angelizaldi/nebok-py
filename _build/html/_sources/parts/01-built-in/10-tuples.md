# Tuples

Corresponde al tipo de dato `tuple`. Son sequencias para almacener múltiples elementos en una sola variable. Algunas caractacterísticas de:
- Se Puede almacenar diferentes tipos de datos en un `tuple`.
- Están indexados: Los elementos están ordenados (indexados)
- Es inmutable: No se pueden modificar una vez creado el `tuple`.
- Permiten valores duplicados.
- Es un iterable: Se puede iterar por sus elementos y se puede usar la palabra reservada `in` para verificar memebresía.

---
## Creación de un tuple

Para crear un tuple existen distintas formas:
1. Poner los elementos, separados por coma directamente
2. Poner los elementos, separados por coma de paréntesis `()`.
3. Utilizar el constructor `tuple()`, con los elementos separados por coma
```python
# Todas las siguientes expresiones son equivalentes
X = x1, x2, ...
X = (x1, x2, ...)
X = tuple(x1, x2, ...)
```
- Los elementos pueden ser otros tuples.

```{warning} Si se quiere crear un tuple de solo un elemento usando paréntesis, se tienen que poner una coma ‘,’ después del elemento.
<code>
X = (x,)
</code>
```

---
## Selección de elementos: 

### Subsetting:
Para seleccionar elementos de una tupla tener en cuenta las siguientes características:
- Se utilizan corchetes `[]` para acceder a los elementos, junto con el nombre de la tupla y el índice del elemento: <br/>
`X[i]`
- Los índices comienza en cero (0), esto quiere decir que si quiere acceder al elemento `i`, se debe de usar `[i-1]`.
- Se puede utilizar números negativos, de manera que se comience por el último elemento. Se puede acceder al último con `[-1]`, al penúltimo elemento `[-2]`, etc.
- Para tupls dentro de otras tuplas, considerar que en esencia usar `X[i]` devolverá otra tupla, entonces para acceder a los elementos de esa otra tupla usar otro `[]`, esto es: <br/> `X[N1][N2]`
- Lo anterior se puede generalizar para cualquier número de tuplas anidadas.


### Slicing:
- Para seleccionar un rango de elementos consecutivos se utiliza dos puntos: <br/> `X[i:j]`
- La selección por rango, tienen la característica que el primer elemento es inclusivo y el último es exclusivo, esto quiere decir que no se incluirá en el rango, si se usa el rango `[i:j]`, en realidad solo se accederá a `[i:j-1]`.
- Desde el índice `i` hasta el `j`, sin incluir el `j`: <br> `X[i:j]`
- Desde el inicio hasta el `j`, sin incluir el `j`: <br> `X[:j]`
- Desde la posición `i` hasta el final de la cadena: <br>`X[i:]`
- Toda la lista: <br> `X[:]`
- Desde el índice `i` hasta el `j`, sin incluir el `j`, cada `k` elementos: <br> `X[i:j:k]`

Algunos patrones útiles:
- El primer elemento: <br> `X[0]`
- El último elemento: <br> `X[-1]`
- Toda la lista cada `k` elementos: <br> `X[::k]`
- Toda la lista al revés: <br> `X[::-1]`

---
##  Concatenar y multiplicar:

El operador `+` sirve para concatenar tuples, los elementos se agrega al final del primer tuple.
```python
# Si X y Y son tuples, entonces W es la concatenacion de X y Y:
W = X + Y
```

El operador `*` sirve para repetir `n` veces un tuple y concatenarlos.
```python
# Si X es un tuple y n un número entero, entonces Y es X concatenado n veces
Y = X * n 
```

##  Modificar:
Los tuples no se pueden modificar una vez creados. Un truco para modificar una tupla es convertir la tupla en una lista y después volverla a convertir en una tupla:
```python
# Un tuple
X = (...)
# Convertir a lista
Y = list(X)
# modificar
...
# Convertir a tuple de vuelta
X = tuple(Y)
```

Para eliminar todo el tuple se puede usar la palabra reservada `del`:
```python
# Si X es un tuple
del X
```

---
## Unpack de tuples:

Se refiere a asignar a varias variables los elementos de un objeto iterable como un `tuple`:
```python
# Si X es una tupla de longitud n:
x1, x2, ... , xn  = X
```

Si el número de variables es menor que el número de elementos se puede usar un asterisco `*`, para indicar que en esa variable se almacenen el resto de los elementos:
```python
# Si X es una tupla:
x1, x2, ... , *xi  = X
```
- En ese caso la varible `xi` almacenará todos lo valores restantes en la tupla.
- El asterisco no tiene porque ir en la última variable, puede ir antes, en ese caso python asignará el número de elementos que sea necesario, para que el resto de las variables que vienen después tengan un elemento.

---
## Iteración:

Para interar sobre todos los elementos de un tuple se puede usar un `for loop`. Algunas opciones de iteración son:
```python
# Iterar sobre los elementos del tuple X:
for ele in X:
    ...
        
# Iterar sobre los índices del tuple X:
for i in range(len(X)):
    ...
    
# Iterar sobre los elementos y los índices del tuple X:
for i, ele in enumerate(X):
    ...
```
- En todos los ejemplos anteriores `i`y `ele` son nombres opcionales.

---
## Métodos de tuple

En esta sección se verán los métodos del tipo `tuple`.

---
### Información

Métodos que retornan información sobre el `tuple` o sus elementos.

---
**count**:

`tuple.count()`: Devuelve el número de veces que hay un elemento específico en el `tuple`.
```python
X.count(Y)
```

**Parámetros:**
- **`X`** \- `tuple`: Un `tuple`.
- **`Y`** \- `object`: Un número, una cadena, etc.

**Retorna:**
-  `int`.

---
**index**:

`tuple.index()`: Devuelve la posición en la que se encuentra un elemento. El elemento es tal cual el objeto que se quiere buscar.
```python
X.index(Y)
```

**Parámetros:**
- **`X`** \- `tuple`: Un `tuple`.
- **`Y`** \- `object`: Un número, una cadena, etc.

**Retorna:**
-  `int`.