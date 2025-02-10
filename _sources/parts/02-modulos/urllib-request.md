# urllib.request

Es un módulo con funcionalidades para abrir _URL_s.

```python
# Importar el módulo
import urllib.request
```

:::{warning}
En esta sección solo se presentan algunas de las funciones del módulo `urllib.request`, para un tratado completo de este módulo visitar la [documentación](https://docs.python.org/3/library/urllib.request.html#module-urllib.request) de Python.
:::

## Leer URL

Para leer el contenido de una _url_ (solicitud _GET_ simple) usar la función `urlopen()`:

```python
# Importar función
from urllib.request import urlopen

# Crear conexión con la página
page = urlopen(url)

# Leer contenido HTML de la página
html = page.read()

# Cerrar conexión con la página
page.close()
```
- _url_ es la dirección de la página web que se quiere leer.
- Si se quiere leer para usar con `BeautifulSoup` entonces usar: `soup = BeautifulSoup(page.read())`.

Alternativamente se podría usar la clase `Request` para una solicitud _GET_, de esta manera se podrían indicar _headers_ adicionales y además se puede personalizar la solicitud _HTTP_ después de enviarla:
```python
# Importaciones
from urllib.request import urlopen, Request

# Crear conexión con la página
request = Request(url)
response = urlopen(request)

# Leer contenido HTML de la página
html = response.read()

# Cerrar conexión con la página
response.close()
```
- Para añadir encabezados adicioanles usar un diccionario junto con el parámetro _headers_ del constructor `Request()`, ejemplo: `Request(url, headers={'User-Agent': 'Mozilla/5.0'})`

## Guardar archivo en línea localmente

Para guardar un archivo en línea de manera local usar la función `urlretrieve()`:

```python
# Importar función
from urllib.request import urlretrieve

# Definir url del archivo
url = 'http://www.webpage.com/files/winequality-white.csv'

# Almacenar archivo localmene
urlretrieve(url, 'my_file.csv')
```
- La _URL_ debe de incluir la extensión del archivo (_.csv_, _.txt_, _.xlsx_, etc.)
- El archivo se guardará en el directorio activo a menos de que se indique la ruta (absoluta o relativa) completa donde se quiere almacenar.

## Funciones

Funciones de la librería `urllib.request`.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [build_opener](https://docs.python.org/3/library/urllib.request.html#urllib.request.build_opener)([handler,  ...])
  - Devuelve una instancia de `OpenerDirector`, que encadena los controladores en el orden dado. Los controladores pueden ser instancias de `BaseHandler` o subclases de `BaseHandler` (en cuyo caso debe ser posible llamar al constructor sin ningún parámetro). 
* - [getproxies](https://docs.python.org/3/library/urllib.request.html#urllib.request.getproxies)()
  - Esta función auxiliar devuelve un diccionario de asignaciones de URL de esquema a un servidor proxy. 
* - [install_opener](https://docs.python.org/3/library/urllib.request.html#urllib.request.install_opener)(opener)
  - Instala una instancia de `OpenerDirector` como el _opener_ global predeterminado. 
* - [pathname2url](https://docs.python.org/3/library/urllib.request.html#urllib.request.pathname2url)(path)
  - Convierte la ruta local indicada en una URL de archivo.
* - [url2pathname](https://docs.python.org/3/library/urllib.request.html#urllib.request.url2pathname)(url)
  - Convierte la URL del archivo indicada en una ruta local. 
* - [urlcleanup](https://docs.python.org/3/library/urllib.request.html#urllib.request.urlcleanup)()
  - Limpia archivos temporales que puedan haber quedado atrás en llamadas anteriores a `urlretrieve()`.
* - [urlopen](https://docs.python.org/3/library/urllib.request.html#urllib.request.urlopen)(url,  data=None,  [timeout,  ]*,  context=None)
  - Abre una URL que puede ser una cadena que contiene una URL válida y correctamente codificada, o un objeto `Request`.
* - [urlretrieve](https://docs.python.org/3/library/urllib.request.html#urllib.request.urlretrieve)(url,  filename=None,  reporthook=None,  data=None)
  - Almacena un archivo en la red indicado por una URL a un archivo local. Si la URL apunta a un archivo local, el objeto no se copiará a menos que se proporcione _filename_. Retorna una tupla (_filename, headers_) donde _filename_ es el nombre del archivo local bajo el cual se puede encontrar el objeto y _headers_ es lo que el método `info()` retorne del objeto devuelto por `urlopen()`.
```

## Clase _Request_

Esta clase es una abstracción de una solicitud de URL. 

:::{note}
Para más información visitar la [documentación](https://docs.python.org/3/library/urllib.request.html#urllib.request.Request) de Python.
:::

---
### Atributos de _Request_

Atributos de la clase `Request`. 

```{list-table}
:header-rows: 1

* - Atributo
  - Descripción
* - [Request.data](https://docs.python.org/3/library/urllib.request.html#urllib.request.Request.data)
  - El cuerpo de la entidad para el _request_, o `None` si no se especifica.
* - [Request.full_url](https://docs.python.org/3/library/urllib.request.html#urllib.request.Request.full_url)
  - La URL original pasada al constructor.
* - [Request.host](https://docs.python.org/3/library/urllib.request.html#urllib.request.Request.host)
  - La autoridad URI, normalmente un host, pero también puede contener un puerto separado por dos puntos.
* - [Request.method](https://docs.python.org/3/library/urllib.request.html#urllib.request.Request.method)
  - El método de solicitud HTTP que se utilizará. De forma predeterminada, su valor es `None`, lo que significa que `get_method()` realizará el cálculo normal del método que se utilizará.
* - [Request.origin_req_host](https://docs.python.org/3/library/urllib.request.html#urllib.request.Request.origin_req_host)
  - El host original de la solicitud, sin puerto.
* - [Request.selector](https://docs.python.org/3/library/urllib.request.html#urllib.request.Request.selector)
  - La ruta URI. Si la solicitud utiliza un proxy, el selector será la URL completa que se pasa al proxy.
* - [Request.type](https://docs.python.org/3/library/urllib.request.html#urllib.request.Request.type)
  - El esquema URI.
* - [Request.unverifiable](https://docs.python.org/3/library/urllib.request.html#urllib.request.Request.unverifiable)
  - Indica si la solicitud no es verificable según lo define _RFC 2965_.
```

<br/>

---
### Métodos de _Request_

Métodos de la clase `Request`. 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [Request.add_header](https://docs.python.org/3/library/urllib.request.html#urllib.request.Request.add_header)(key,  val)
  - Agrega otro _header_ a la solicitud. Actualmente, todos los controladores ignoran los encabezados, excepto los controladores HTTP, donde se agregan a la lista de encabezados enviados al servidor.
* - [Request.add_unredirected_header](https://docs.python.org/3/library/urllib.request.html#urllib.request.Request.add_unredirected_header)(key,  header)
  - Agrega un encabezado que no se agregará a una solicitud redirigida.
* - [Request.get_full_url](https://docs.python.org/3/library/urllib.request.html#urllib.request.Request.get_full_url)()
  - Devuelve la URL dada en el constructor.
* - [Request.get_header](https://docs.python.org/3/library/urllib.request.html#urllib.request.Request.get_header)(header_name,  default=None)
  - Devuelve el valor del encabezado indicado. Si el encabezado no está presente, devuelve el valor predeterminado.
* - [Request.get_method](https://docs.python.org/3/library/urllib.request.html#urllib.request.Request.get_method)()
  - Devuelve una cadena que indica el método de solicitud HTTP. Si `Request.method` no es `None`, devuelve su valor; de lo contrario, devuelve _'GET'_ si `Request.data` es `None` o _'POST'_ si no lo es. Esto solo tiene sentido para solicitudes _HTTP_.
* - [Request.has_header](https://docs.python.org/3/library/urllib.request.html#urllib.request.Request.has_header)(header)
  - Devuelve si la instancia tiene el encabezado nombrado (verifica tanto los regulares como los no redirigidos).
* - [Request.header_items](https://docs.python.org/3/library/urllib.request.html#urllib.request.Request.header_items)()
  - Devuelve una lista de tuplas (_header_name, header_value_) de los encabezados de la solicitud.
* - [Request.remove_header](https://docs.python.org/3/library/urllib.request.html#urllib.request.Request.remove_header)(header)
  - Elimina el encabezado con nombre de la instancia de solicitud (tanto de los encabezados regulares como de los no redirigidos).
* - [Request.set_proxy](https://docs.python.org/3/library/urllib.request.html#urllib.request.Request.set_proxy)(host,  type)
  - Prepara la solicitud conectándose a un servidor proxy. El host y el tipo reemplazarán a los de la instancia, y el selector de la instancia será la URL original proporcionada en el constructor.
```