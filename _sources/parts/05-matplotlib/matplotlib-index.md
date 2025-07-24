---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Matplotlib

```{code-cell} ipython3
:tags: ["remove-input"]

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
```

`matplotlib` es una librería que se utiliza principalmente para crear visualizaciones estáticas y dinámicas. La mayoría de las funcionalidades que se verán en esta sección están en el módulo `pyplot` que es útil para crear una variedad amplia de gráficas. Lo más común es importar la librería y el módulo `pyplot`, ya que este módulo provee de todo lo necesario para crear, personalizar y manipular gráficas.

Para utilizar `matplotlib` es necesario instalarlo. Desde la terminal usar:
```
# Con pip
pip install matplotlib

# Con conda
conda install matplotlib
```

Una vez instalado se debe de importar:
```python
# Importar módulo
import matplotlib.pyplot as plt
```
- _plt_ es el nombre por convención, en este sitio se utilizará _plt_ para refererirse a `matplotlib.pyplot`.

:::{note}
Para más información de esta librería visitar la [documentación](https://matplotlib.org/stable/api/index.html) y [guía de usuario](https://matplotlib.org/stable/users/index.html#) de `matplotlib`.
:::

<br/>

---
## Figuras y _Axes_

En `matplotlib` se trabaja principalmente con dos clases que sirven para hacer las gráficas:
- `Figure`: Es el objeto que contendrá la gráfica o las gráficas, ya que una sola figura puede contener múltiples gráficas. En una figura con múltiples gráficas, a cada gráfica se le denomina _subplot_.
    - Por convención se le llama a este objeto _fig_.
    - Algunas formas para crear el objeto _fig_ son (más adelante se explicará mejor cada una): 
        - `plt.figure()`: Crea un objeto `Figure`.
        - `plt.subplots()`: Crea una objeto `Figure` y un objeto `Axes`.
- `Axes`: Representa todos los elementos de la gráfica, incluyendo la gráfica como tal (datos), ejes, títulos, etiquetas, leyendas, etc. Hay un `Axes` por cada gráfica, por lo que una sola `Figure` puede tener múltiples `Axes`.
    - Por convención se le llama a este objeto _ax_.
    - Algunas formas para crear el objeto _ax_ son (más adelante se explicará mejor cada una): 
        - `plt.axes()`: Crea un objeto `Axes`.
        - `plt.subplots()`: Crea una objeto `Figure` y un objeto `Axes`.

```{note}
Se puede trabajar directamente con esos objetos (_fig_ y _ax_), cada objeto tiene distintos métodos para ir agregando elementos a la gráfica. También es posible trabajar de manera implicíta con estos objetos, sin necesidad de declararlos, algunas funciones (Ver {doc}`./pyplot`) crean automáticamente esos objetos.
```

Algunos elementos de los objetos `Figure` y `Axes`:

<br/>

![anatomia-figura](https://matplotlib.org/stable/_images/anatomy.png)

<br/>

---
## Interfaces

En `matplotlib` existen dos interfaces principales para crear gráficas
- **Interfaz orienta a objetos**: Utiliza directamente los objetos _fig_ y _ax_ y sus métodos para agregar o modificar elementos a la gráfica. Se recomienda esta interfaz si se quiere un mayor control en la personalización de las gráficas.
- **Interfaz basada en Matlab**: Utiliza funciones del módulo `pyplot` y lleva un control de manera implícita de los últimos objetos _fig_ y _ax_ activos para agregar o modificar elementos en la gráfica. Se recomienda esta interfaz si se quiere crear gráficas de manera rápida con menos opciones de personalización.

Para los ejemplos de esta sección se utilizará el _dataset_ "flights" de la librería {doc}`../06-seaborn/seaborn-index`, además se agrupan los datos por año para las visualizaciones de un solo _axes_. Para las figuras con más de un _axes_ se crean dos _datasets_ uno para el años 1950 y otro para 1960.

```{code-cell} ipython3
# Cargar el dataset
flights = sns.load_dataset("flights")

# Agrupar datos por año
yearly_data = flights.groupby('year')['passengers'].sum().reset_index()

# Filtrar datos para 1950 y 1960
data_1950 = flights[flights['year'] == 1950]
data_1960 = flights[flights['year'] == 1960]
```

<br/>

### Interfaz Orienta a Objetos

En esta Interfaz se crean dos objetos _fig_ y _ax_. Hay dos formas principales de crear estos objetos.

#### 1. Usar las funciones _plt.figure()_ y _plt.axes()_

Se pueden crear los objetos directamente con las funciones `plt.figure()` y `plt.axes()` y utilizar los métodos de estos objetos para conformar las gráficas:

```python
# Importar módulo
import matplotlib.pyplot as plt

# Crear objetos
fig = plt.figure()
ax = plt.axes()

# Utilizar métodos de ax y/o fig para agregar elementos a la gráfica
ax.method_name()
...
ax.method_name ()
...

# Imprimir la gráfica
plt.show()
```
**Notas**:
- _fig_ será una instancia de la clase {doc}`./figure`.
- _ax_ será una instancia de la clase {doc}`./axes`.
- Las grafícas se crean usando los objetos _fig_ y  _ax_ y sus métodos, ver {ref}`Métodos de Figure <matplotlib-figure-metodos>` y {ref}`Métodos de Axes <matplotlib-axes-metodos>`.
- Se pueden agregar tantos métodos como sean necesarios para personalizar las gráficas.
- Al finalizar para mostrar la gráfica usar `plt.show()`.

<br/>

**Ejemplo**:
En este ejemplo se utiliza las funciones `plt.figure()` y `plt.axes()` para crear una figura con un _axes_.

```{code-cell} ipython3
# Crear objetos
fig = plt.figure()
ax = plt.axes()

# Graficar los datos
ax.plot(yearly_data['year'], yearly_data['passengers'], label='Passengers', marker='o', c='#30adb9')

# Añadir elementos a la gráfica
ax.set_xlabel('Año')
ax.set_ylabel('Total de pasajeros')
ax.set_title('Tendencia de total de pasajeros')
ax.legend()

# Show the plot
plt.show()
```

<br/>

#### 2. Usar la función _plt.subplots()_ 

Se recomienda utilizar este método porque es más simple y versátil. En este caso la función `plt.subplots()` retorna un objeto _fig_ y un objecto _ax_ y posteriormente se pueden utilizar los métodos de estos objetos para conformar las gráficas:

```python
# Importar módulo
import matplotlib.pyplot as plt

# Crear objetos
fig, ax = plt.subplots(nrows=1, ncols=1, [sharey], [sharex])

# Utilizar métodos de ax y/o fig para agregar elementos a la gráfica
ax.method_name()
...
ax. method_name ()
...

# Imprimir la gráfica
plt.show()
```
**Notas**:
- Se puede indicar cuántas filas y columnas de gráficas tendrá la figura, si no se indican se utilizan los valores por default que es 1 en ambos casos, es decir, una figura con una sola gráfica (un solo _axes_).
- _fig_ será una instancia de la clase {doc}`./figure`
- Dependiendo de los argumentos _n_ y _m_, el objeto _ax_ puede ser:
    - Una instancia de la clase {doc}`./axes` (`n=1` y `m=1`, default)
    - Un `ndarray` de instancias de la clase {doc}`./axes` (`n>1` o `m>1`).
    - **IMPORTANTE**: En lugar de definir _ax_ como _array_, se podrían definir tantos _ax_i_ dentro de un tuple, como sean necesarios (_unpacking_). <br> `fig, (ax0, ax1) = plt.subplots(nrows=1, ncols=2) # ejm. 2 axes`
- Las grafícas se crean usando los objetos _fig_ y  _ax_ y sus métodos, {ref}`Métodos de Figure <matplotlib-figure-metodos>` y {ref}`Métodos de Axes <matplotlib-axes-metodos>`.
- **IMPORTANTE**: En caso de que _ax_ sea _ndarray_, para utilizar los métodos propios de la clase `Axes` se tiene que indicar el índice del elemento usando `ax[i]` o `ax[i, j]`, dependiendo de las dimensiones del _array_, donde _i_ es el índice de las filas y _j_ es el índice de las columnas, ambos empienzan en cero.
- Se pueden agregar tantos métodos como sean necesarios para personalizar las gráficas.
- Al finalizar para mostrar la gráfica usar `plt.show()`.

<br/>

**Ejemplo 1**:
En este ejemplo se utiliza la función `plt.subplots()` con los argumentos _nrows=1_ y _ncols=1_ para crear una figura con un _axes_.

```{code-cell} ipython3
# Crear figura y axes
fig, ax = plt.subplots(1, 1)

# Graficar datos
ax.plot(yearly_data['year'], yearly_data['passengers'], label='Passengers', marker='o', c='#30adb9')

# Añadir elementos a la gráfica
ax.set_xlabel('Año')
ax.set_ylabel('Total de pasajeros')
ax.set_title('Tendencia de total de pasajeros')
ax.legend()

# Show the plot
plt.show()
```

<br/>

**Ejemplo 2**:
En este ejemplo se utiliza la función `plt.subplots()` con los argumentos _nrows=1_ y _ncols=2_ para crear una figura con dos _axes_.

```{code-cell} ipython3
# Crear figura y axes
fig, axes = plt.subplots(1, 2, figsize=(12, 5), sharey=True)

# Graficar datos de 1950
axes[0].bar(data_1950['month'], data_1950['passengers'], color='#30adb9')
axes[0].set_title('Pasajeros en 1950')
axes[0].set_xlabel('Mes')
axes[0].set_ylabel('Números de Pasajeros')
axes[0].tick_params(axis='x', rotation=45)

# Graficar datos de 1960
axes[1].bar(data_1960['month'], data_1960['passengers'], color='#ba6a30')
axes[1].set_title('Pasajeros en 1960')
axes[1].set_xlabel('Mes')
axes[1].tick_params(axis='x', rotation=45)

# Ajustar el layout
plt.tight_layout()

# Imprimir la figura
plt.show()
```

<br/>

---
### Interfaz basada en Matlab

Para crear gráficas en un interfaz basada en _Matlab_ se utiliza las funciones del módulo {doc}`./pyplot`, lo que permite llevar un control implícito de los objetos _ax_ y _figure_, es decir, no es necesario declararlos. Las figuras pueden tener un _axes_ o múltiples _axes_ como se verá a continuación.

#### Figura con un solo _axes_

Para crear una figura con un único axes basta con llamar a cualquiera de las {ref}`pyplot-funciones`. 

```python
# Llamar a alguna función de pyplot para crear una gráfica.
plt.plot() # Ejemplo con plt.plot()
# Llamar a alguna función de pyplot para personalizar gráficas.
plt.tile() # Ejemplo con plt.title()
...

# Imprimir la gráfica
plt.show()
```
**Notas**:
- Hacer llamadas de las funciones de `matplotlib.pyplot` para agregar {ref}`pyplot-funciones` o {ref}`pyplot-personalizacion`.
- Este estilo mantiene un seguimiento de los _fig_ y _ax_ actuales de manera implícita.
- Al finalizar para mostrar la gráfica usar `plt.show()`.

<br/>

**Ejemplo**:
En este ejemplo se utiliza directamente la función `plt.plot()` para crear una figura con un _axes_, además se hacen llamadas a las funciones `plt.xlabel()`, `plt.ylabel()`, `plt.title()` y `plt.legend()` para añadir elementos a la gráfica.

```{code-cell} ipython3
# Crear nueva figura (opcional)
plt.figure()

# Graficar los datos
plt.plot(yearly_data['year'], yearly_data['passengers'], label='Passengers', marker='o', c='#30adb9')

# Agregar elementos
plt.xlabel('Año')
plt.ylabel('Total de pasajeros')
plt.title('Tendencia de total de pasajeros')
plt.legend()

# Imprimir la figura
plt.show()
```

<br/>

#### Figura con múltiples _axes_

Para crear una figura con múltiples axes, se usa la función `plt.subplot()`, en cada llamada se debe de indicar el número total de filas y columnas que tendrá la figura y el indice del _axes_ con el que se estará trabajando en cada llamada.

```python
# Opcionalmente llamar a la función plt.figure()
[plt.figure()]

# Llamar a la función plt.subplot()
plt.subplot(n, m, i1)
# Llamar a alguna función de pyplot para crear una gráfica.
plt.plot() # Ejemplo con plt.plot()
# Llamar a alguna función de pyplot para personalizar gráficas.
plt.tile() # Ejemplo con plt.title()

# Llamar a la función plt.subplot()
plt.subplot(n, m, i2)
# Llamar a alguna función de pyplot para crear una gráfica.
plt.plot() # Ejemplo con plt.plot()
# Llamar a alguna función de pyplot para personalizar gráficas.
plt.tile() # Ejemplo con plt.title()

# Hacer tantas llamadas a las funciones como sea necesario
...

# Imprimir la gráfica
plt.show()
```
**Notas**:
- Para trabajar con una gráfica en particular hacer una llamada a la función `plt.subplot()` indicando el índice y el número total de filas y columnas.
- Una vez se haya llamado a la función `plt.subplot()` indicando el índice, hacer llamadas de las funciones de `matplotlib.pyplot` para agregar {ref}`pyplot-funciones` o para {ref}`pyplot-personalizacion`.
- Este estilo mantiene un seguimiento de los _fig_ y _ax_ actuales de manera implícita.
- Al finalizar para mostrar la gráfica usar `plt.show()`.

<br/>

**Ejemplo**:
En este ejemplo se llama a la función `plt.subplot()` para cada _axes_ en la figura, en este caso se hacen dos llamadas.  

```{code-cell} ipython3
# Crear nueva figura (opcional)
plt.figure(figsize=(12, 5))

# Graficar datos de 1950
ax1 = plt.subplot(1, 2, 1)
plt.bar(data_1950['month'], data_1950['passengers'], color='#30adb9')
plt.title('Pasajeros en 1950')
plt.xlabel('Mes')
plt.ylabel('Número de Pasajeros')
plt.xticks(rotation=45)

# Graficar datos de 1960
plt.subplot(1, 2, 2, sharey=ax1)
plt.bar(data_1960['month'], data_1960['passengers'], color='#ba6a30')
plt.title('Pasajeros en 1960')
plt.xlabel('Mes')
plt.xticks(rotation=45)

# Ajustar el layout
plt.tight_layout()

# Imprimir la figura
plt.show()
```

<br/>

---
## Tabla de contenido


```{tableofcontents}
````