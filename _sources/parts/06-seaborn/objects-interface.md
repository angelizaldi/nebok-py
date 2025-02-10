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

# Interface por objetos

```{code-cell} ipython3
:tags: ["remove-input"]

import matplotlib.pyplot as plt
import seaborn as sns
import seaborn.objects as so
import numpy as np

azul="#30adb9"
cafe="#ba6a30"
cafe_claro="#cf9975"
```

Es una interfaz que permite mayor flexibilidad y personalización de las gráficas, sin tener que recurrir a utilizar las funciones de _matplotlib_, aunque sigue siendo posible hacerlo si es necesario. Para utilizarlo se recomienda importar el módulo:

```python
# Importar módulo
import seaborn.objects as so
```
- _so_ es el nombre por convención.

Existen 4 clases bases las cuales se explican a continuación:
- [objects.Mark](https://seaborn.pydata.org/generated/seaborn.objects.Mark.html): Clase base para objetos que representan datos visualmente.
- [objects.Move](https://seaborn.pydata.org/generated/seaborn.objects.Move.html): Clase base para objetos que aplican transformaciones posicionales simples.
- [objects.Scale](https://seaborn.pydata.org/generated/seaborn.objects.Scale.html): Clase base para objetos que mapean valores de datos a propiedades visuales.
- [objects.Stat](https://seaborn.pydata.org/generated/seaborn.objects.Stat.html): Clase base para objetos que aplican transformaciones estadísticas.

Para algunos ejemplos de esta sección se utilizarán los siguientes objetos:
```{code-cell} ipython3
# Cargar el dataset
flights = sns.load_dataset("flights")

# Agrupar datos por año
yearly_data = flights.groupby('year')['passengers'].sum().reset_index()

# Filtrar datos para 1950 y 1960
sub_flights = flights[(flights['year'] == 1950) | (flights['year'] == 1960)]
```

## Uso

Para utilizar la interfaz por objeto se utilizan las clases definidas en este módulo, la clase principal sería `Plot` que permite especificar los datos y los elementos que tendrá la gráfica, incluyendo el tipo de gráfica. Para especificar los elementos de utilizarán otras clases como `Line`, `Dot`, etc. Cada clase tiene a su vez atributos y métodos para añadir más elementos a la gráfica o personalizarla.

**Ejemplo un eje**:

```{code-cell} ipython3
# Importar interfaz
import seaborn.objects as so

# Crear gráfica
plot = (
    so.Plot(yearly_data, x='year', y='passengers')
    .add(so.Line(color=azul))
    .add(so.Dot(color=azul))
    .label(x='Año', y='Total de Pasajeros', title='Tendencia de total de pasajeros')
)

# Mostrar gráfica
plot.show()
```

**Ejemplo múltiples ejes**:

```{code-cell} ipython3
# Importar interfaz
import seaborn.objects as so

# Crear gráfica
plot = (
    so.Plot(sub_flights, x='month', y='passengers')
    .add(so.Bar(color=azul))
    .facet(col='year')
    .layout(size=(10, 6))
)

# Mostrar gráfica
plot.show()
```

<br/>

---
## Clase _Plot_

Es la clase principal para definir gráficas. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [objects.Plot](https://seaborn.pydata.org/generated/seaborn.objects.Plot.html)(*args, ...)
  - Una interfaz para especificar de forma declarativa gráficas estadísticas.
```

### Métodos

Métodos de las `Plot`. 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - Especificación:
  -
* - [add](https://seaborn.pydata.org/generated/seaborn.objects.Plot.add.html)(mark, *transforms, orient=None, legend=True, label=None, data=None, **variables)
  - Especifica una capa de la visualización en términos de marcas y transformaciones de datos.
* - [scale](https://seaborn.pydata.org/generated/seaborn.objects.Plot.scale.html)(**scales)
  - Especifica mapeos de unidades de datos a propiedades visuales.
* - Subplots*:
  -
* - [facet](https://seaborn.pydata.org/generated/seaborn.objects.Plot.facet.html)(col=None, row=None, order=None, wrap=None)
  - Produce _subplots_ con subconjuntos condicionales de los datos.
* - [pair](https://seaborn.pydata.org/generated/seaborn.objects.Plot.pair.html)(x=None, y=None, wrap=None, cross=True)
  - Produce _subplots_ al emparejar ´x´ y/o ´y´.
* - Personalización:
  -
* - [label](https://seaborn.pydata.org/generated/seaborn.objects.Plot.label.html)(*, title=None, legend=None, **variables)
  - Controla las etiquetas y títulos de ejes, leyendas y _subplots_.
* - [layout](https://seaborn.pydata.org/generated/seaborn.objects.Plot.layout.html)(*, size=<default>, engine=<default>, extent=<default>)
  - Controla el tamaño y el diseño de la figura.
* - [limit](https://seaborn.pydata.org/generated/seaborn.objects.Plot.limit.html)(**limits)
  - Controla el rango de datos visibles.
* - [share](https://seaborn.pydata.org/generated/seaborn.objects.Plot.share.html)(**shares)
  - Controla el uso compartido de los límites de los ejes y las marcas en los _subplots_.
* - [theme](https://seaborn.pydata.org/generated/seaborn.objects.Plot.theme.html)(config, /)
  - Controla la apariencia de los elementos en la gráfica.
* - Integración:
  -
* - [on](https://seaborn.pydata.org/generated/seaborn.objects.Plot.on.html)(target)
  - Proporciona _figures_ o _axes_ de `Matplotlib` existentes para dibujar el gráfico.
* - Output:
  -
* - [plot](https://seaborn.pydata.org/generated/seaborn.objects.Plot.plot.html)(pyplot=False)
  - Compila la especificación del gráfico y devuelve el objeto `Plotter`.
* - [save](https://seaborn.pydata.org/generated/seaborn.objects.Plot.save.html)(loc, **kwargs)
  - Compila el gráfico y lo escribe en un búfer o archivo localmente.
* - [show](https://seaborn.pydata.org/generated/seaborn.objects.Plot.show.html)(**kwargs)
  - Compila la gráfica y la imprime.

```

<br/>

---
## Objetos de tipo _Mark_

Los objetos de tipo _Mark_ representan datos visualmente, son los principales objetos ya que con estos se definen el tipo de gráfica que se realizará, entre las cuales se incluyen gráficas de líneas, puntos, barras, áreas y texto.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - **Áreas**
  - 
* - [objects.Area](https://seaborn.pydata.org/generated/seaborn.objects.Area.html)([artist_kws, color, alpha, ...])
  - Una marca de área graficada desde la base hasta los valores de datos.
* - [objects.Band](https://seaborn.pydata.org/generated/seaborn.objects.Band.html)([artist_kws, color, alpha, ...])
  - Una marca de área que representa un intervalo entre valores.
* - **Barras**
  - 
* - [objects.Bar](https://seaborn.pydata.org/generated/seaborn.objects.Bar.html)([artist_kws, color, alpha, ...])
  - Una marca de barra graficada entre la base y y los valores de datos.
* - [objects.Bars](https://seaborn.pydata.org/generated/seaborn.objects.Bars.html)([artist_kws, color, alpha, ...])
  - Una marca de barra más eficiente con valores predeterminados, más adecuados para histogramas.
* - **Puntos**
  - 
* - [objects.Dot](https://seaborn.pydata.org/generated/seaborn.objects.Dot.html)([artist_kws, marker, pointsize, ...])
  - Una marca punto adecuada para diagramas de puntos o diagramas de dispersión menos densos.
* - [objects.Dots](https://seaborn.pydata.org/generated/seaborn.objects.Dots.html)([artist_kws, marker, pointsize, ...])
  - Una marca de punto definida por trazos para manejar mejor las marcas superpuestas.
* - **Líneas**
  - 
* - [objects.Dash](https://seaborn.pydata.org/generated/seaborn.objects.Dash.html)([artist_kws, color, alpha, ...])
  - Una marca de línea graficada como un segmento orientado para cada punto de datos.
* - [objects.Line](https://seaborn.pydata.org/generated/seaborn.objects.Line.html)([artist_kws, color, alpha, ...])
  - Una marca de línea que conecta puntos de datos con orden a lo largo de la orientación del eje.
* - [objects.Lines](https://seaborn.pydata.org/generated/seaborn.objects.Lines.html)([artist_kws, color, alpha, ...])
  - Una marca de línea más eficiente pero menos flexible para graficar muchas líneas.
* - [objects.Path](https://seaborn.pydata.org/generated/seaborn.objects.Path.html)([artist_kws, color, alpha, ...])
  - Una marca de _path_ que conecta puntos de datos en el orden en que aparecen.
* - [objects.Paths](https://seaborn.pydata.org/generated/seaborn.objects.Paths.html)([artist_kws, color, alpha, ...])
  - Una marca más eficiente pero menos flexible para graficar muchos _paths_.
* - [objects.Range](https://seaborn.pydata.org/generated/seaborn.objects.Range.html)([artist_kws, color, alpha, ...])
  - Una marca de línea orientada graficada entre los valores mínimo/máximo.
* - **Texto**
  - 
* - [objects.Text](https://seaborn.pydata.org/generated/seaborn.objects.Text.html)([artist_kws, text, color, ...])
  - Una marca de texto para anotar o representar valores de datos.
```

### Ejemplo de _Bar_

En este ejemplo de gráfica la media de _bill_length_mm_ para cada _species_. Si no se agregará `so.Agg()`, entonces se graficaría el valor _y_ para cada _x_. `so.Agg()` se agregó para replicar el comportamiento de `sns.barplot()`.

```{code-cell} ipython3
# Importar el dataset
penguins = sns.load_dataset("penguins")

# Crear gráfica de barras con agregación de la media
p = (
    so.Plot(penguins, x="species", y="bill_length_mm")
    .add(so.Bar(), so.Agg())
)

# Mostrar gráfica
p.show()
```

### Ejemplo de _Dot_

En este ejemplo se crea un diagrama de dispersión entre _bill_length_mm_ y _bill_depth_mm_, además se crea una leyenda por _sex_ y se modifica el estilo del marcador por _species_.

```{code-cell} ipython3
# Crear gráfica
p = (
    so.Plot(penguins, x='bill_length_mm', y='bill_depth_mm')
    .add(sns.objects.Dot(), color='sex', marker='species')
    .scale(color={'Male': azul, 'Female': cafe}) 
)

# Imprimir gráfica
p.show()
```

### Ejemplo de _Line_

En este ejemplo se grafica el _tip_ para los días, con la leyenda por _smoker_.

```{code-cell} ipython3
# Crear gráfica
p = (
    so.Plot(yearly_data, x='year', y='passengers')
    .add(so.Line(color=azul))
)

# Show plot
p.show()
```

<br/>

---
## Objetos de tipo _Move_

Los objetos de tipo _Move_ aplican transformaciones posicionales simples.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [objects.Dodge](https://seaborn.pydata.org/generated/seaborn.objects.Dodge.html)(empty='keep', gap=0, by=None)
  - Desplazamiento y estrechamiento de marcas superpuestas a lo largo del eje de orientación.
* - [objects.Jitter](https://seaborn.pydata.org/generated/seaborn.objects.Jitter.html)(width=<default>, x=0, y=0, seed=None)
  - Desplazamiento aleatorio a lo largo de uno o ambos ejes para reducir marcas superpuestas.
* - [objects.Norm](https://seaborn.pydata.org/generated/seaborn.objects.Norm.html)(func='max', where=None, by=None, percent=False)
  - Escalamiento divisivo en el eje de valores después de calcular _aggregates_ por grupos.
* - [objects.Shift](https://seaborn.pydata.org/generated/seaborn.objects.Shift.html)(x=0, y=0)
  - Desplazamiento de todas las marcas con la misma magnitud/dirección.
* - [objects.Stack](https://seaborn.pydata.org/generated/seaborn.objects.Stack.html)()
  - Desplazamiento de barras superpuestas o marcas de área a lo largo del eje de valores, para que se apilen entre ellas, en lugar de sobre encimarse.
```

<br/>

---
## Objetos de tipo _Scale_

Los objectos de tipo _Scale_ mapean valores de datos a propiedades visuales.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [objects.Boolean](https://seaborn.pydata.org/generated/seaborn.objects.Boolean.html)(values=None)
  - Una escala con un dominio discreto de valores ´True´ y ´False´.
* - [objects.Continuous](https://seaborn.pydata.org/generated/seaborn.objects.Continuous.html)(values=None, norm=None, trans=None)
  - Una escala numérica que soporta normas y transformaciones funcionales.
* - [objects.Nominal](https://seaborn.pydata.org/generated/seaborn.objects.Nominal.html)(values=None, order=None)
  - Una escala categórica sin importancia/magnitud relativa.
* - [objects.Temporal](https://seaborn.pydata.org/generated/seaborn.objects.Temporal.html)(values=None, norm=None)
  - Una escala para datos de fecha/hora.
```

<br/>

---
## Objetos de tipo _Stat_

Los objetos de tipo _Stat_ aplican transformaciones estadísticas.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [objects.Agg](https://seaborn.pydata.org/generated/seaborn.objects.Agg.html)(func='mean')
  - Calcula _aggregates_ de los datos a lo largo del eje de valores utilizando el método dado.
* - [objects.Count](https://seaborn.pydata.org/generated/seaborn.objects.Count.html)(). 
  - Cuenta el número de observaciones distintas dentro cada grupo.
* - [objects.Est](https://seaborn.pydata.org/generated/seaborn.objects.Est.html)(func='mean', errorbar=('ci', 95), n_boot=1000, seed=None)
  - Calcula una estimación puntual y un intervalo como una barra de error.
* - [objects.Hist](https://seaborn.pydata.org/generated/seaborn.objects.Hist.html)(stat='count', bins='auto', ...)
  - Agrupa las observaciones en _bins_, realiza el conteo de cada _bin_ y, opcionalmente, las normaliza o acumula.
* - [objects.KDE](https://seaborn.pydata.org/generated/seaborn.objects.KDE.html)(bw_adjust=1, bw_method='scott', common_norm=True, common_grid=True, gridsize=200, cut=3, cumulative=False)
  - Calcula una estimación univariada de la densidad del _kernel_.
* - [objects.Perc](https://seaborn.pydata.org/generated/seaborn.objects.Perc.html)(k=5, method='linear')
  - Calcula los percentiles de las observaciones.
* - [objects.PolyFit](https://seaborn.pydata.org/generated/seaborn.objects.PolyFit.html)(order=2, gridsize=100)
  - Ajusta un polinomio del orden dado y muestrea los datos en la curva estimada.
```