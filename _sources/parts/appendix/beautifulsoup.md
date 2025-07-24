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

# BeautifulSoup

En esta sección se cubre lo esencial para hacer _web scraping_ en Python usando la librería `BeautifulSoup`, en conjunto con otros módulos como `requests` y `urllib.request`.

Para utilizar `BeautifulSoup` es necesario instalarlo. Desde la terminal usar:
```
# Con pip
pip install beautifulsoup4

# Con conda
conda install beautifulsoup4
```

Una vez instalado se debe de importar
```python
# Importar BeautifulSoup
from bs4 import BeautifulSoup
```

:::{warning}
- En este sitio no se explica ningún concepto relacionado con documentos HTML o XML.
- En este sitio únicamente se explorarán documentos HTML.
- En este sitio únicamente se explorará métodos para navegar, buscar y acceder a partes de documentos HTML, pero no a modificaciones de los documentos.
:::

---

(bs4-jerarquia-clases)=
## Principales clases de `BeautifulSoup`

A continuación se muestra la jerarquía de las principales clases en `bs4`. Tener en cuenta que las clases están ordenadas de acuerdo a las clases padres y las clases hijas.

- `bs4.element.PageElement`: Representa la posición actual de una parte de un documento HTML o XML y en la que se puede seguir explorando.
    - `bs4.element.Tag`: Representa un elemento de un documento HTML o XML, junto con sus atributos y contenido.
        - `bs4.BeautifulSoup`: Es una estructura de datos que representa un documento HTML o XML completo.
    - `bs4.element.NavigableString`: Representa una cadena unicode que es el contenido de un elemento HTML o XML. Esta clase también es una subclase de `str`.
        - `bs4.Stylesheet`: Representa cadenas dentro de la etiqueta `<style>`.
        - `bs4.Script`: Representa cadenas dentro de la etiqueta `<script>`.
  
:::{note}
Tener en cuenta lo siguiente:
- La clase `BeautifulSoup` es una clase hija de la clase `Tag`. Para fines prácticos se puede considerar a los objetos de tipo `BeautifulSoup` como objetos de tipo `Tag`
- La clase `Tag` es una clase hija de la clase `PageElement`. Para fines prácticos esto no es relevante, ya que no se trabajarán con instancias de `PageElement`. Basta con saber que la mayoría de métodos de `Tag` son heredados de `PageElement`.
:::

La clase `PageElement` contiene los siguientes métodos y atirbutos que la mayoría se pueden encontrar en sus clases hijas. **Importante**, esto no es una lista completa de los atributos y métodos de `PageElement`:

:::{caution}
El uso de métodos cuyos nombres están en _CamelCase_ está desaconsejado, se recomienda utilizar sus versiones más recientes que se pueden identificar porque las palabras de sus nombres están separados por guiones bajos (_method_name_).
:::

- findAllNext
- findAllPrevious
- findNext
- findNextSibling
- findNextSiblings
- findParent
- findParents
- findPrevious
- findPreviousSibling
- findPreviousSiblings
- find_all_next
- find_all_previous
- find_next
- find_next_sibling
- find_next_siblings
- find_parent
- find_parents
- find_previous
- find_previous_sibling
- find_previous_siblings
- getText
- get_text
- next
- nextSibling
- next_elements
- next_siblings
- parents
- previous
- previousSibling
- previous_elements
- previous_siblings
- text

Por su parte, la clase `Tag` incorpora los siguientes métodos y atributos. **Importante**, esto no es una lista completa de los atributos y métodos propios de `Tag`:
- name 
- attrs
- find_all
- find
- prettify

---
## Conexión y lectura de una página web

Para leer el contenido de una página web primero es necesario conectarse con ella. Para ello se puede utilizar las siguientes opciones:

:::{warning}
Es necesario instalar e importar la librería `requests`. En cambio `urllib.request` es un módulo _built-in_ de Python y por lo tanto no es necesario instalarlo, únicamente importarlo.
:::

```python
# Usando la librería urllib.request
from urllib.request import urlopen
page = urlopen(url)
html = page.read()

# Usando la librería request
import requests
page = requests.get(url)
html = page.content
```
- _url_ es una cadena con el url de la página web.
- El objeto _html_ es el que se podrá pasar al constructor `BeautifulSoup()` para  inicializar el objeto _soup_ y poder navegar por el documento.

<br/>

---
## Creación de objeto `BeautifulSoup`

El objeto `BeautifulSoup` representa una documento HTML o XML completo que permite explorar el contenido del mismo de manera simple. Para crear un objeto `BeautifulSoup` se utiliza el constructor, es posible pasarle una cadena que represente un documento HTML o XML, o pasar un objeto `file-like` que represente el documento.

:::{note}
La clase `BeautifulSoup` es una clase hija de la clase `Tag`, por lo que a grandes rasgos se puede entender a un objeto `BeautifulSoup` como un objeto `Tag`.
:::

```python

BeautifulSoup(markup='', features=None)
```
- markup \- `str`, `file-like`: Cadena o archivo que represente un documento HTML o XML.
- features \- `str`, `{"html.parser", "lxml", "lxml-xml", "xml", "html5lib"}` o `{"html", "html5", "xml"}`: Indica el tipo de _parser_ o el tipo del _markup_. Es recomendado indicar el _parser_. Algunos _parsers_ requieren instalar otras librerías externas. Para más información consultar la [documentación](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-a-parser) de `BeautifulSoup`. Por default se trata de usar el mejor _parser_ instalado.
- **Importante**: Existen más parámetros, para más información utilizar `help(BeautifulSoup)` o `help(bs4.BeautifulSoup)`, dependiendo de cómo se haya importado.

<br/>

**Ejemplo**:
Ejemplo básico de creación de un objeto `BeautifulSoup` desde una _url_:

```{code-cell} ipython3
# Importar librerías
from bs4 import BeautifulSoup
import requests

# Definir URL
url = "https://docs.python.org/3/library/stdtypes.html"

# Conexión y lectura de la url
page = requests.get(url)
soup = BeautifulSoup(page.content)

# Imprimir el tipo del objeto soup
print(type(soup))
```
- Alternativamente se podría usar `page.text` en lugar de `page.content`.

Para evitar errores en caso de que no sea posible conectarse con la página se puede usar un manejador de errores:
```python
# Importar librerías
from bs4 import BeautifulSoup
import requests

# Definir URL
url = "https://docs.python.org/3/library/stdtypes.html"

# Conexión y lectura de la url
try:
    page = requests.get(url)
except HTTPError as e:
    # except body
else:
    soup = BeautifulSoup(page.content)
```

<br/>

---
## Imprimir el contenido del documento HTML

Por default si se imprime un objeto `Tag`/`BeautifulSoup` se retornará una representación en cadena de la etiqueta/documento HTML. Es posible imprimir el contenido del documento HTML desde un objeto `Tag`/`BeautifulSoup` con un formato organizado y jerarquizado con el método `.prettify()`

```python
# Imprimir contenido del documento HTML
tag.prettify()
```
- tag – `Tag`, `BeautifulSoup`: Una instancia de la clase `Tag` o `BeautifulSoup`.

**Ejemplo**:

En este ejemplo se imprimirá el contenido de un elemento `<p>` con un _id_ específico.
.
```{code-cell} ipython3
# Imprimir contenido de un tag
paragraph = soup.find('p', {'id': 'index-1'})
print(paragraph.prettify())
```

<br/>

---
## Navegación por un documento HTML

En un objeto `BeautifulSoup` o `Tag` se puede navegar a través del documento de diversas maneras. Para entender la navegación en un documento HTML, conceptualizar a un documento HTML como una estructura jerarquizada, como se muestra en la siguiente imagen.

![](https://www.bu.edu/lernet/artemis/years/2020/projects/FinalPresentations/HTML/hierarchy.jpg)

:::{caution}
La posición en el documento donde se realizará la navegación/búsqueda depende del tipo de objeto:
- `BeautiufulSoup`: La posición es al inicio del documento.
- `Tag`: La posición será la posición de la etiqueta en cuestión.
:::

- **Navegar a niveles inferiores**.
    - **Navegar usando nombres de etiquetas**: Es posible navegar _hacia abajo_ usando nombres de etiquetas con métodos como `.find()` y `.find_all()`. Ver métodos de búsqueda {ref}`bs4-tag-metodo-busqueda-abajo`.
    - **Hijos de etiquetas**: Para acceder a los hijos de elementos usar atributos como:
        - `.contents`: Retorna una lista de los hijos directos de un elemento.
        - `.children`: Retorna un `generator` de los hijos directos de un elemento.
        - `.descendants`: Retorna un `generator` de todos los hijos de un elemento.
        - `.string`: Retorna un `NavigableString` del hijo un elemento.
        - `.strings`: Retorna un `generator` de los `NavigableString` de los hijos de un elemento.
        - `.strippedstrings`: Retorna un `generator` de los `NavigableString` removiendo espacios en blanco extras o saltos de línea de los hijos de un elemento.
- **Navegar a niveles superiores**:
    - **Navegar usando nombres de etiquetas**: Es posible navegar _hacia arriba_ usando nombres de etiquetas con métodos como `.find_parent()` y `.find_parents()`. Ver métodos de búsqueda {ref}`bs4-tag-metodo-busqueda-arriba`.
    - **Padres de etiquetas**: Para acceder a los padres de elementos usar atributos como:
        - `.parent`: Retorna el elemento padre de un elemento.
        - `.parents`: Retorna un `generator` de todos los elementos padres de un elemento.
- **Navegar en el mismo nivel**:
    - **Navegar usando nombres de etiquetas**: Es posible navegar _en el mismo nivel_ usando nombres de etiquetas con métodos como `.next_sibling()` y `.previous_sibling()` o  sus equivalentes en plural. Ver métodos de búsqueda {ref}`bs4-tag-metodo-busqueda-mismo`. 
    - **Hermanos de etiquetas**: Para acceder a los hermanos de elementos usar atributos como:
        - `.next_sibling`: Retorna el próximo elemento en el mismo nivel de un elemento.
        - `.next_siblings`: Retorna un `generator` de todos los próximos elementos en el mismo nivel de un elemento.
        - `.previous_sibling`: Retorna el elemento anterior en el mismo nivel de un elemento.
        - `.previous_siblings`: Retorna un `generator` de todos los elementos anteriores en el mismo nivel de un elemento.
- **Navegación lineal**:
    - **Navegar usando nombres de etiquetas**: Es posible navegar _independiente del nivel_ usando nombres de etiquetas con métodos como `.next_sibling()` y `.previous_sibling()` o  sus equivalentes en plural. Ver métodos de búsqueda {ref}`bs4-tag-metodo-busqueda-lineal`.
    - **Ascendientes y descendientes**: Se puede navegar _linealmente_ por orden de aparición, independiente del nivel, con atributos como:
        - `.next_element`: Retorna el próximo elemento independiente del nivel de un elemento.
        - `.next_elements`: Retorna un `generator` de todos los próximos elementos independiente del nivel de un elemento.
        - `.previous_element`: Retorna el elemento anterior independiente del nivel de un elemento.
        - `.previous_elements`: Retorna un `generator` de todos los elementos anteriores independiente del nivel de un elemento.

En las siguientes secciones se profundiza más en algunos de estos métodos para navegar en un documento HTML o buscar contenido específico.

<br/>

### Acceder a un único _tag_ por su nombre

:::{caution}
En esta sección se explica la búsqueda hacia niveles inferiores, pero los mismos procedimientos aplican para cualquier dirección con los métodos apropiados. Consultar métodos de {ref}`bs4-tag-metodo-busqueda`.
:::

Se puede acceder a _tags_ únicos específicos, esto es particulamente útil si sabe que solo hay una etiqueta en el documento o si solo se quiere recuperar la primer coincidencia. Para acceder a _tags_ de HTML concretos por su nombre se puede hacer principal de dos formas, tener en cuenta que `soup` es una instancia de `Tag` o `BeautifulSoup` y `tag_name` es el nombre de una etiqueta HTML válida:
1. Utilizando el método `.find()`: <br/> `soup.find('tag_name')`.
2. Utilizando la notación punto: <br/> `soup.tag_name`

:::{note}
Las dos formas explicadas anteriormente en esencia son la misma, ya que internamente al utilizar la _notación punto_ se llama al método `.__getattr__(tag_name)` y este método retorna `self.find('tag_name')`.
:::

Al acceder a elementos únicos por su nombre tener en cuenta lo siguiente:
- Se accede únicamente a la primer coincidencia encontrada.
- Es posible omitir algunas etiquetas padres como `.html` correspondientes a `<html> ... </html>`, `.head` correspondiente `<head> ... </head>`, `.body` correspondiente `<body> ... </body>`, `.div` correspondiente `<div> ... </div>`, etc. Recordar que se accede a la primer etiqueta encontrada, independientemente de las etiquetas padres. 
- El objeto retornado generalmente será una instancia de `bs4.element.Tag`, de ahí que se pueda encadenar el acceso a etiquetas más internas.

```python
# Acceder a la etiqueta 'tag_name' con el método .find()
soup.find('tag_name')

# Acceder a etiquetas más internas con el método .find()
soup.find('parent_tag').find('child_tag')

# Acceder a la etiqueta 'tag_name' con notación punto
soup.tag_name

# Acceder a etiquetas más internas con notación punto
soup.parent_tag.child_tag
```
- _soup_ – `Tag`, `BeautifulSoup`: Una instancia de la clase `Tag` o `BeautifulSoup`.
- _tag_name_ es una etiqueta válida de HTML.

:::{tip}
Un comportamiento similar se puede conseguir con el método `.findall()` usando: <br/> `soup.find('tag_name', limit=1)`
:::

<br/>

**Ejemplo**

```{code-cell} ipython3
# Acceder a primer etiqueta <h1> con método find
print(soup.find("h1"))

# Acceder a primer etiqueta <h1> con notación punto
print(soup.h1) # equivale a soup.html.body.h1
```

<br/>

### Acceder a todos los elementos de un _tag_ específico

:::{caution}
En esta sección se explica la búsqueda hacia niveles inferiores, pero los mismos procedimientos aplican para cualquier dirección con los métodos apropiados. Consultar métodos de {ref}`bs4-tag-metodo-busqueda`.
:::

Se puede acceder a todos los elementos de algún _tag_ específico, retornando una lista, para ello se utiliza el método `.find_all()`

```python
# Acceder a todas los elementos de una etiqueta específica
soup.find_all('tag_name')

# Lo anterior equivale a:
soup('tag_name')
```
- _soup_ – `Tag`, `BeautifulSoup`: Una instancia de la clase `Tag` o `BeautifulSoup`.
- _tag_name_ es una etiqueta válida de HTML. También es posible poner un `iterable` de `str` para buscar múltiples elementos de HTML al mismo tiempo: <br>`soup.find_all(['tag_name_1', 'tag_name_2', ...])`
- Notar que hacer una llamada directamente en un objeto equivale a utilizar el método `.find_all()`

:::{tip}
Alternativamente se puede usar el método `tag.findAll()`
:::

<br/>

### Acceder a _tags_ por nombre y atributos específicos

:::{caution}
En esta sección se explica la búsqueda hacia niveles inferiores, pero los mismos procedimientos aplican para cualquier dirección con los métodos apropiados. Consultar métodos de {ref}`bs4-tag-metodo-busqueda`.
:::

En los métodos `.find()` y `.findall()` existe el parámetro `attrs` que permite especificar valores de atributos concretos que el elemento HTML debe de tener. Este parámetro se debe especificar como un diccionario donde los _keys_ son el nombre del atributo y los _values_ son el valor que debe de tener el atributo:

```python
# Especificar atributos al buscar etiquetas
soup.find_all('tag_name', attrs={'attr_name': 'val', ...})

# Alternativamente se pueden especificar por key=value
soup.find_all('tag_name', attr_name='val', ...)
```
- _soup_ – `Tag`, `BeautifulSoup`: Una instancia de la clase `Tag` o `BeautifulSoup`.
- _tag_name_ es una etiqueta válida de HTML.
- **Importante**: Un mismo atributo se puede repetir múltiples veces con diferentes valores para especificar múltiples posibles valores que puede tomar ese atributo.
- **Importante**: Si los atributos se definen como _keywords_ en lugar de un diccionario se debe verificar que el nombre de atributo no entre en conflicto con otros nombres de Python. Por ejemplo, no es posible utilizar el _keyword_ `class`, para ello utilizar `class_`.

Entre los atributos más importantes que se pueden especificar están:
- `class`: Clase del elemento.
- `id`: Id del elemento.

<br/>

### Acceder a valores de atributos de _tags_

Se puede acceder a los valores de los atributos de un objeto `Tag` utilizando el atributo `.attrs`, este atributo retorna un `dict` con los pares de atributos y valor, por lo que posteriormente se pueden seleccionar atributos específicos:

```python
# Acceder a todos los atributos
tag.attrs

# Acceder a un atributo en concreto, ejemplo con class
tag.attrs['class']
```

<br/>

**Ejemplo**

```{code-cell} ipython3
# Acceder al url del primer link 
print(soup.find('section', {'id': 'comparisons'}).find('a').attrs['href'])
``` 

### Selectores CSS

Es posible acceder a selectores de CSS con la propiedad `.css` junto con los método `.select()` y `.select_one()` que retornan todas y una, respectivamente, las etiquetas que satisfacen los selectores de _CSS_ especificados.

:::{note}
El acceso a elementos de un documento HTML por medio de los selectores CSS es manejado por la librería [Soup Sieve](https://facelessuser.github.io/soupsieve/) e implementada a través de _BeautifulSoup_. Para ver más métodos de está librería consultar la [documentación](https://facelessuser.github.io/soupsieve/api/) de `Soup Sieve`.
:::

Los selectores se pueden especificar por:
- Nombre: `soup.css.selec('tagname')`
- Id: `soup.css.selec('#id')` <br/> `soup.css.selec('tagname#id')`
- Etiquetas anidadas (ejemplo de 2, pero pueden ser más): `soup.css.selec('ParentTagname ChildTagname')`

:::{note}
Para más información consultar la [documentación](https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.html#css-selectors-through-the-css-property) de `BeautifulSoup`.
:::

<br/>

---
## Objeto `Tag`

El objeto `Tag` es un objeto que representa una etiqueta de HTML o XML que forma parte de un documento HTML o XML, según sea el caso, junto a sus atributos y contenido. Este objeto es retornado cuando se accede a un _tag_ específico de un objeto `BeautifulSoup` o cuando se acceden a etiquetas más internas de otros objetos `Tag`. Algunos métodos y atributos que retornan instancias de `Tag` son:
- `Tag.find()`.
- `Tag.find_all()` (retorna una lista de instancias de `Tag`).
- `Tag.select()` (retorna una lista de instancias de `Tag`).
- `Tag.children` (retorna un iterator de instancias de `Tag`).
- `Tag.parent`.
- `Tag.descendants`.

### Atributos

Atributos de la clase `Tag`.

:::{warning}
Esta no es una lista completa de los atributos de `Tag`.
:::

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - `attrs`
  - Retorna los atributos del _tag_ como `dict`. 
* - `get_text`
  - Retorna el texto del _tag_ como `str`.  
* - `name`
  - Retorna el nombre del _tag_ como `str`.

```

### Métodos

Métodos de instancia de la clase `Tag`.

#### Parámetros comunes

A continuación se enlistan parámetros comúnes en los métodos de `Tag` y se explica su funcionalidad. También se indica cómo se debe de especificar los argumentos de estos parámetros, tener en cuenta que _name_ y _string_ tienen múltiples formas de definirlos que se explican más detalladamente en {ref}`bs4-metodos-parametros-tipos-filtros`.

- [name](https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.html#the-name-argument) \- ver {ref}`bs4-metodos-parametros-tipos-filtros`: El parámetro `name` se utiliza para especificar la o las etiquetas por las cuales se quiere filtrar.
- _attrs_ \- `dict`: Un diccionario cuyos _keys_ son atributos del elemento HTML y cuyos _values_ son los valores concretos que deben tener esos atributos. Un mismo atributo se puede repetir múltiples veces en el diccionario con diferentes valores.
    - [keyword](https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.html#the-keyword-arguments): En lugar de definir un diccionario para definir valores de atributos, se puede pasar directamente pares `key=value` como argumento a modo de `keyword`. En caso de que el atributo sea `"class"`, se debe de pasar como `class_=value`.
- [string](https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.html#the-string-argument) \- ver {ref}`bs4-metodos-parametros-tipos-filtros`: El parámetro `string` se utiliza en lugar de _name_ para que la búsqueda se realice con base al contenido en cadena de las etiquetas en lugar del nombre de las etiquetas. Algunas etiquetas de HTML pueden tener contenido en cadena que se encuentra entre las etiquetas de apertura y cierre (`<tagname> content </tagname>`). Algunos ejemplos de etiquetas con este tipo de contenido son: `<p>`, `<span>`, `<h1>`, ..., `<h6>`, `<dt>`, `<dl>`, `<li>`, entre muchos otros. En versiones anteriores a '4.4.0' este parámetro se denomina `text`.
- [limit](https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.html#the-limit-argument) \- `int`: Limita el número de elementos en la búsuqueda.
- [recursive](https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.html#the-recursive-argument) \- `bool`: Indica si se debe de realizar la búsqueda en todos los hijos del elementos (`True`) o solo en los hijos directos (`False`).

(bs4-metodos-parametros-tipos-filtros)=
#### Tipos de filtros

Los parámetros _name_ y _string_ se pueden especificar de diversas formas que incluyen:

- [str](https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.html#a-string): Una cadena con el nombre de la etiqueta o el contenido de cadena del elemento.
- [regular expression](https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.html#a-regular-expression): Una cadena que represente una expresión regular para filtrar los _match_ usando el método `.search()`. La expresión regular se tiene que pasar como argumento de la función `compile()`: <br/> `re.compile(r'pattern')`
- [function](https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.html#a-function): Una función que reciba un único elemento (de tipo `Tag`) y retorne valores `True` o `False` dependiendo de si el elemento en cuestión satisface las condiciones por las que se quiera filtrar.
- [list](https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.html#a-list) de `str` o `function`: Una lista de cadenas, expresiones regulares o funciones para verificar múltiples opciones al mismo tiempo. 
- [True](https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.html#true): El valor `True` equivale a no filtrar los resultados, y acceder a todas los elementos en el objeto.

(bs4-tag-metodo-busqueda)=
#### Buscar elementos

:::{warning}
Esta no es una lista completa de los atributos de instancia de `Tag`.
:::

(bs4-tag-metodo-busqueda-abajo)=
##### Niveles abajo

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [find](https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.html#find)(name, attrs, recursive, string, **kwargs)
  - Busca en los hijos de este elemento y retorna la primer coincidencia que satisfaga los criterios. Retorna `bs4.element.Tag` o `bs4.element.NavigableString`, si no se encuentra ningún hijo que satisfaga los criterios retorna `None`.
* - [find_all](https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.html#find-all)(name, attrs, recursive, string, limit, **kwargs)
  - Busca en los hijos de este elemento y retorna todas las coincidencias que satisfagan los criterios. Retorna `list` de `bs4.element.Tag` o `bs4.element.NavigableString`, si no se encuentra ningún hijo que satisfaga los criterios retorna una lista vacía. Es un alias del método `findAll()`.
```

(bs4-tag-metodo-busqueda-arriba)=
##### Niveles arriba

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [find_parent](https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.html#find-parents-and-find-parent)(name, attrs, string, **kwargs)
  - Busca en los padres de este elemento y retorna la primer coincidencia que satisfaga los criterios. Retorna `bs4.element.Tag` o `bs4.element.NavigableString`, si no se encuentra ningún padre que satisfaga los criterios retorna `None`.
* - [find_parents](https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.html#find-parents-and-find-parent)(name, attrs, string, limit, **kwargs)
  - Busca en los padres de este elemento y retorna todas las coincidencias que satisfagan los criterios. Retorna `list` de `bs4.element.Tag` o `bs4.element.NavigableString`, si no se encuentra ningún padre que satisfaga los criterios retorna una lista vacía.
```

(bs4-tag-metodo-busqueda-mismo)=
##### Mismo nivel

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [find_next_sibling](https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.html#find-next-siblings-and-find-next-sibling)(name, attrs, string, **kwargs)
  - Busca en los hermanos (elementos en el mismo nivel) posteriores de este elemento y retorna la primer coincidencia que satisfaga los criterios. Retorna `bs4.element.Tag` o `bs4.element.NavigableString`, si no se encuentra ningún hermano posterior que satisfaga los criterios retorna `None`.
* - [find_next_siblings](https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.html#find-next-siblings-and-find-next-sibling)(name, attrs, string, limit, **kwargs)
  - Busca en los hermanos (elementos en el mismo nivel) posteriores de este elemento y retorna todas las coincidencias que satisfagan los criterios. Retorna `list` de `bs4.element.Tag` o `bs4.element.NavigableString`, si no se encuentra ningún hermano posterior que satisfaga los criterios retorna una lista vacía.
* - [find_previous_sibling](https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.html#find-previous-siblings-and-find-previous-sibling)(name, attrs, string, **kwargs)
  - Busca en los hermanos (elementos en el mismo nivel) anteriores de este elemento y retorna la primer coincidencia que satisfaga los criterios. Retorna `bs4.element.Tag` o `bs4.element.NavigableString`, si no se encuentra ningún hermano anterior que satisfaga los criterios retorna `None`.
* - [find_previous_siblings](https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.html#find-previous-siblings-and-find-previous-sibling)(name, attrs, string, limit, **kwargs)
  - Busca en los hermanos (elementos en el mismo nivel) anteriores de este elemento y retorna todas las coincidencias que satisfagan los criterios. Retorna `list` de `bs4.element.Tag` o `bs4.element.NavigableString`, si no se encuentra ningún hermano anterior que satisfaga los criterios retorna una lista vacía.
```

(bs4-tag-metodo-busqueda-lineal)=
##### Niveles por orden de aparición

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [find_next](https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.html#find-all-next-and-find-next)(name, attrs, string, **kwargs)
  - Busca en los elementos posteriores de este elemento, independientemente del nivel y retorna la primer coincidencia que satisfaga los criterios. Retorna `bs4.element.Tag` o `bs4.element.NavigableString`, si no se encuentra ningún hermano elemento que satisfaga los criterios retorna `None`.
* - [find_all_next](https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.html#find-all-next-and-find-next)(name, attrs, string, limit, **kwargs)
  - Busca en los elementos posteriores de este elemento, independientemente del nivel y retorna todas las coincidencias que satisfagan los criterios. Retorna `list` de `bs4.element.Tag` o `bs4.element.NavigableString`, si no se encuentra ningún elemento posterior que satisfaga los criterios retorna una lista vacía.
* - [find_previous](https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.html#find-all-previous-and-find-previous)(name, attrs, string, **kwargs)
  - Busca en los elementos anteriores de este elemento, independientemente del nivel y retorna la primer coincidencia que satisfaga los criterios. Retorna `bs4.element.Tag` o `bs4.element.NavigableString`, si no se encuentra ningún elemento anterior que satisfaga los criterios retorna `None`.
* - [find_all_previous](https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.html#find-all-previous-and-find-previous)(name, attrs, string, limit, **kwargs)
  - Busca en los elementos anteriores de este elemento, independientemente del nivel y retorna todas las coincidencias que satisfagan los criterios. Retorna `list` de `bs4.element.Tag` o `bs4.element.NavigableString`, si no se encuentra ningún elemento anterior que satisfaga los criterios retorna una lista vacía.
```

#### Acceder a contenido

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - `get`(key, default=None)
  - Retorna el valor de '_key_' de la etiqueta, o el valor dado por default si la etiqueta no existe.
* - [get_text](https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.html#get-text)(separator="", strip=False)
  - Retorna una cadena `str` que resulta de la concatenación de todas las cadenas hijas de este elemento. Las cadenas hijas son el contenido de los elementos internos eliminando las etiquetas de apertura y cierre. Se puede indicar el delimitador para la concatenación e indicar que se eliminen los espacios en blanco en los extremos de cada cadena interna.
```

**Ejemplo**

```{code-cell} ipython3
# Definir el markup
markup = '<a href="http://example.com/">\nI linked to <i>example.com</i>\n</a>'

# Crear objeto soup
soup = BeautifulSoup(markup, 'html.parser')

# Imprimer el texto
soup.get_text()
```