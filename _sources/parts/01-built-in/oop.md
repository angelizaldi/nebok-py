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

# Programación orientada a objetos

En esta sección se presentan algunas acciones comunes en _POO_ como crear clases, definir atributos, métodos, etc.

```{warning} En esta sección no se explican conceptos relacionados con la _POO_, se da por hecho que ya se conocen.
```

---
## Clases

Son una representación abstracta de un objeto.

### Crear una clase

Para crear una clase se usa: 
```python
# Crear una clase nueva
class ClassName:
    # Class body
```
- _ClassName_ es el nombre que tendrá la clase. El nombre por convención se pone en "CamelCase" (primer letra de cada palabra en mayúsculas, sin espacios entre palabras).
- Todo el código indentado será parte de la clase.
- Se puede crear una clase "vacía" usando la palabra reservada `pass`.

```{caution} Si se van a usar funciones de otros módulos/librerías dentro del cuerpo de la clase, se debe de importar afuera de la definición de la clase.
```

<br/>

### Crear instancias

Una **instancia** es un objeto específico creado de una clase particular. Para inicializar una instancia de una clase usar:
```python
# Crear instancia de la clase ClassName
obj = ClassName([args])
```
- _obj_ será una instancia de la clase _ClassName_.
- _args_ por lo general, son los argumentos del método `__init__()`, pero no necesariamente tiene que ser así. Se deben de proveer al menos los argumentos obligatorios, es decir, los que no tienen un valor por default.


<br/>

### Clases hijas

Las clases hijas son clases que heredan los métodos y atributos de su clase padre. Para definir una clase hija que heredará los atributos y métodos de la clase padre se utiliza:
```python
# Definir una clase hija
class ChildClass(ParentClass):
    # Class body
```
- _ChildClass_ es el nombre que tendrá la clase hija, que hereda atributos y métodos de _ParentClass_.
- _ParentClass_ es el nombre de la clase padre. Ya tuvo que haber sido definida, antes que la clase hija.

Para utilizar los métodos o el constructor de la clase padre dentro de la clase hija usar:
```python
# Usar un método de ParentClass en ChildClass
class ChildClass(ParentClass):
    # Class body
    ...
    ParentClass.method_name(self, [params])
```
- No estrictamente el primer argumento debe ser _self_, pero sí un objeto. Puede ser otro objeto que tenga sentido con el método al que se está llamando.

Para utilizar los atributos o métodos de la clase padre en una instancia de la clase hija en el _script_ usar:
```python
# Usar métodos/atributos de la clase padre en una instancia de la clase hija
child_obj.attr_name
child_obj.method_name(args)
```
- _child_obj_ es una instancia de la clase hija.
- En este caso _attr_name_ y _method_name_ son atributos y métodos de la clase padre, no de la hija.

<br/>

---
## Atributos

Los atributos son las propiedades que tendrán las instancias (objetos) de la clase o la clase misma.


### Atributos de instancias
Los atributos de instancia son atributos propios de los objetos y cuyos valores pueden diferir de una objeto a otro. Los atributos de instancias normalmente se definen en el método `.__init__()` (ver {ref}`oop-init`), pero no necesariamente:
```python
# Definir una clase
class ClassName:
    
    # Definir atributos de instancia en el método init
    def __init__(self, [params])
        self.attribute_name = expression
        ...
```
- De esta manera _attribute_name_ será un atributo de la instancia al momento de inicializar el objeto.
- El método puede reciber otros parámetros expresados como _params_ en este ejemplo, pero son opcionales. 
- _expression_ puede ser un escalar o una expresión que utilice uno o más argumentos del método y retorne un objeto.

<br/>

#### Atributos en métodos

Se pueden definir atributos de instancia dentro de un método diferente a `.__init__()`, el cual debe de asignar un valor al atributo. Estos atributos se inicializan si y solo si el método es llamado.
```python
# Definir la clase
class ClassName:
        
    # Definir atributos de instancia dentro de un método
    def method_name(self, [params]):
        self.attribute_name = expression
```
- _attribute_name_ será un atributo de instancia, solo si _method_name_ es llamado.
- _expression_ puede ser un escalar o una expresión que utilice uno o más argumentos del método y retorne un objeto.
- En general es recomendado inicializar los atributos de instancias en el método `__init__()` y no en otros métodos.

<br/>

#### Acceder los atributos de instancia dentro de la clase

Si se quiere obtener al valor un atributo de instancia dentro la misma de la clase se usa _self.attribute_name_:

```python
# Definir una clase nueva
class ClassName:
    
    # Definir un atributo de instancia
    def __init__(self)
        self.attribute_name = value
    
    # Acceder al atributo desde otro método    
    def method_name(self):
        return self.attribute_name
```
- En este ejemplo _method_name_ recupera el valor de _attribute_name_ para retornarlo. Cabe destacar que no es necesario definir métodos para recuperar los valores de los atributos de instancia.

<br/>

#### Acceder a los atributos de instancia en una instancia
Una vez definido una instancia (objeto) de la clase se puede acceder los valores de sus atributos de instancia con _obj.attribute_name_:
```python
# Crear un instancia
obj = ClassName(args)

# Recuperar el valor de un atributo
obj.attribute_name
```
- _obj_ es un objeto de una clase.

<br/>

### Atributos de clase

Los atributos de clase son atributos que todos los objetos de una misma clase tendrán en común y con el mismo valor. Para definir un atributo de clase se realiza en el cuerpo de la clase, afuera de cualquier método:
```python
# Definir una clase nueva
class ClassName:
    
    # Definir un atributo de clase
    ATTRIBUTE_NAME = val

    # Class body
    ...
```
- Por convencion los nombres de atributos a nivel de clase se ponen en mayúsculas, pero no es obligatorio.
- Los atributos de clase usualmente se usan para definir valor mínimos o máximos de otros atributos o definir constantes dentro de la clase.

<br/>

#### Acceder a atributos de clase dentro de la clase

Si se quiere obtener el valor de un atributo de clase dentro la misma de la clase usar _ClassName.ATTRIBUTE_NAME_ o _self.ATTRIBUTE_NAME_:
```python
# Definir una clase nueva
class ClassName:
    
    # Definir un atributo de clase
    ATTRIBUTE_NAME = val
    
    # Acceder al atributo un método    
        def method_name(self):
            return ClassName.ATTRIBUTE_NAME
           # o return self.ATTRIBUTE_NAME
```
- _ClassName_ es un nombre arbitrario de la clase.
- _attribute_name_ es un nombre arbitrario del atributo de clase.
- _method_name_ es un nombre arbitrario de un método.
- Se recomienda usar _ClassName.ATTRIBUTE_NAME_, para identificar que es un atributo a nivel de clase.
- En este ejemplo _method_name_ recupera el valor de _ATTRIBUTE_NAME_ para retornarlo. Cabe destacar que no es necesario definir métodos para recuperar los valores de los atributos de clase.

<br/>

#### Acceder a atributos de clase en una instancia

Una vez definido una instancia (objeto) de la clase se puede acceder a los valores de sus atributos de clase desde un _script_ o desde la consola con _obj.\_\_class\_\_.ATTRIBUTE_NAME_ o _obj.ATTRIBUTE_NAME_:
```python
# Crear un instancia
obj = ClassName(args)

# Recuperar valores de atributos de clase fuera de la clase
obj.__class__.ATTRIBUTE_NAME
obj.ATTRIBUTE_NAME
```
- _ClassName_ es un nombre arbitrario de la clase.
- _ATTRIBUTE_NAME_ es un nombre arbitrario del atributo de clase.
- _obj_ es una instacia de _ClassName_.
- Se recomienda usar _obj.__class__.ATTRIBUTE_NAME_, para identificar que es un atributo a nivel de clase.

```{attention} Modificaciones en el valor de un atributo de clase en una instancia **no** modifica el valor de ese atributo para toda la clase, en cambio se reemplaza por un nuevo atributo en la instancia con el mismo nombre que el atributo a nivel de clase.
```

Si se desea modificar el valor de un atributo de clase para todos los objetos usar:
```python
# Modificar el valor de ATTRIBUTE_NAME para toda la clase
ClassName.ATTRIBUTE_NAME = new_val
```
- _ClassName_ es un nombre arbitrario de la clase.
- _ATTRIBUTE_NAME_ es un nombre arbitrario del atributo de clase.

<br/>

#### Definir atributos de clase de forma dinámica

Se puede crear un atributo de clase de manera dinámina (_on-demand_) desde un _script_ o desde la consola usando:
```python
# Craer el atributo de clase NEW_ATTRIBUTE_NAME
ClassName.NEW_ATTRIBUTE_NAME = value
```
- Se creará el atributo _NEW_ATTRIBUTE_NAME_ y la clase y todos las instancias tendrán ese nuevo atributo.

<br/>

---
## Métodos

Los métodos son acciones que pueden realizar las instancias o las clases mismas. Existen diversos tipos de métodos


(oop-init)=
### Metodo `__init__`

Es un método el cual es llamado automáticamente cuando una instancia de la clase es creada. Generalmente se usa para definir los atributos de instancia.
```python
# Definir una clase nueva
class ClassName:

    # Definir el método __init__
    def __init__(self, [params]):
        self.attribute1 = expression
        ...
```
- El primer parámetro del método debe de ser _self_, incluso cuando no hay más parámetros. El nombre _self_ es por convención pero se puede llamar de cualquier otra forma.
- _params_ son otros posibles parámetros de la función, pero son opcionales.
- _expression_ puede ser un escalar o una expresión que utilice uno o más argumentos del método y retorne un objeto.
- El método `__init__()` puede o no reciber otros parámetros adicionales los cuales pueden o no tener valores por default. Si no tienen valores por default, los valores de esos parámetros se deben de indicar al momento de crear el objeto.

<br/>

### Métodos de instancia

Los métodos de instancia son las acciones asociadas a una instancia de una clase. Para crear métodos de instancia se utiliza una función, cuyo primer argumento debe de ser _self_.
```python
# Definir una clase nueva
class ClassName:
    
    # Definir un método de instancia
    def method_name(self, [params]):
        # method body
```
- El primer parámetro del método debe de ser _self_, incluso cuando no hay más parámetros. El nombre _self_ es por convención pero se puede llamar de cualquier otra forma.
- _params_ son otros posibles parámetros de la función, pero son opcionales.
- Es altamente recomendado poner {ref}`func-docstrings` para indicar qué hace cada método.

<br/>

#### Usar un método

Para llamar a un método de una instancia, se utiliza el nombre del objeto, un punto y el nombre del método con sus argumentos, en caso de que tenga.
```python
# Crear una instancia
obj = ClassName(args)

# Usar un método de una instancia
obj.method_name(args)
```
- _obj_ es un objeto de una clase _ClassName_.
- No se pone el argumento self, porque la sintaxis anterior equivale a: <br/> `ClassName.method_name(obj, args)`

<br/>

### Definir métodos de manera dinámica

Se pueden crear **métodos de instancia** fuera de la definición de la clase de forma dinámica (_on-demand_), para ello se define una función y posteriormente se asigna el nuevo método a la clase
```python
# Definir una función
def method_name(self, [params]):
    # method body

# Asignar el método a una clase
ClassName.method_name = method_name
```
- _method_name_ será un nuevo método de _ClassName_.

<br/>

### Métodos de clase

Existen métodos que se pueden definir a nivel de clase y no puede usar información de las instancias. Para definir este tipo de métodos se utiliza el decorator `@classmethod`. Un caso de uso de este tipo de métodos es para crear instancias sin llamar al constructor, como solo puede haber un constructor este método permite modificar la forma como se llama al constructor permitiendo tener diferentes formas de inicializar un objeto.
```python
# Crear una clase nueva
class ClassName:
    
    # Definir un método de clase
    @classmethod
    def method_name(cls, [params]):
        # method body
        return cls([args])
```
- El primer parámetro debe de ser `cls`, se utiliza ese nombre por convención, pero se puede llamar de cualquier otra forma. `cls` es un objeto que hace referencia a la clase misma. `csl` es equivalente a usar la clase como tal _ClassName_.
- En el cuerpo de la función se puede hacer cualquier modificación a los valores de los parámetros.
- En el `return`, `cls()` llamará a `__init__(args])`, es decir `return cls([args])` equivale a `__init__([args])` o `ClassName([args])` (que en todo caso lo que hace es llamar al método `__init__()`).

<br>

Para inicializar un objeto a través de un método de clase se usa:
```python
# Crear instancia con un método de clase
obj = ClassName.method_name([args])
```
- _method_name_ es un método a nivel de la clase _ClassName_.

<br>

**Ejemplo**: En este ejemplo se define una clase que crea una fecha indicando el año, mes y día individualemente. Posteriormente se define un método de clase que permite crear la fecha desde una cadena {ref}`datetime-iso` en lugar de los elementos individuales.

```{code-cell} ipython3
# Definir la clase
class Fecha:    
    # Definir el constructor
    def __init__(self, year, month, day):
      # Asignar los atributos de año, mes y dia.
      self.year, self.month, self.day = year, month, day
    
    # Se definie el método a nivel de clase "desde_str"
    @classmethod
    def desde_str(cls, str_date):
        year, month, day = map(int, str_date.split("-"))
        return cls(year, month, day) # Equivale a: Fecha.__init__(year, month, day)

# Crear instancia desde el metodo de clase
fecha = Fecha.desde_str('2023-01-01')   

# Imprimir los atributos de fecha
print(fecha.year)
print(fecha.month)
print(fecha.day)
```
- El método de clase _desde_str_ permite inicializar un objeto con base a una cadena que contiene una fecha en lugar de pasar individualmente cada atributo.

<br/>

### Métodos estáticos

Son un tipo de método de clase, el método se asocia con la clase, no con las instancias de la clase. Para crear métodos estáticos se usa el decorator `@staticmethod`:
```python
# Crear una clase nueva
class ClassName:
    
    # Definir un método estático
    @staticmethod
    def method_name([params]):
        # method body
```
- Los métodos estáticos no tienen el parámetros _self_ porque _self_ se asocia a las instancias.
- Los métodos estáticos no pueden acceder a los atributos de instancia o métodos de instancias.

Para usar un método estático usar:
```python
# Usar un método estático
ClassName.method_name([params])
```

<br/>

**Ejemplo**: A continuación se define un método estático simple que suma dos números.
```{code-cell} ipython3
# Definir la clase
class MyClass:
    
    # Definir el método estático
    @staticmethod
    def my_static_method(arg1, arg2):
        return arg1 + arg2

# Utilizar el método estático    
result = MyClass.my_static_method(1, 2)
print(result)
```

<br/>

### Atributos y Métodos privados

Es posible restringir el acceso a atributos y métodos para prevenir modificación de datos. Para ello existen diversas estrategias.

#### Convenciones de nombres

:::{warning}
Las convenciones no convierten a los atributos como privados, únicamente es para indicar que no se debe de interactuar con esos atributos.
:::

Existen ciertas convenciones para trabajar con atributos/métodos privados (todos los atributos/métodos de todas las clases en Python son públicas por default).
- **Atributos/métodos internos**: Se utiliza un guión bajo al principio del nombre, para indicar que es un atributo/método el cual no se debe de utilizar ni modificar (aunque sí se puede hacer), no deben de formar parte de la _API_ pública: <br/> `_attr_name` <br/> `_method_name`
- **Atributos/métodos pseudo-privados**: Se utilizan dos guión bajos la principio del nombre para indicar que no se deben heredar a las clases hijas: <br/> `__attr_name` <br/> `__method_name`

### Atributos restringidos y de solo lectura

Son atributos especiales que tienen un control de acceso y son particularmente útiles cuando se quiere asignar valores a un atributo: La forma de crear una propiedad es:
1.	Definir el atributo como “protegido” (usando un guión bajo en el nombre).
2.	Crear un método con el decorador `@property` que tiene el mismo nombre que el atributo (sin el guión bajo) y retorne el atributo.
3.	Crear un método con el decorador `@attr_name.setter` que tiene el mismo nombre que el atributo (sin el guión bajo) y que será llamado cuando se trate de usar `obj.attr=val`, cuyo argumento será el valor que se está tratando de asignar.

```python
class ClassName:
    def__init__(self, attr_val):
        # Definir atributo como protegido
        self._attr = attr_val

@property
def attr(self):
    return self._attr

@attr.setter
def attr(self, new_value):
    # method body
    self._attr = new_value
```
- El método con el decorador `@attr.setter` debe de validar en qué casos si se puede modificar el atributo.
- Existe posibilidad de no modificar un atributo si no se agrega el método `@attr.setter`.
- Existen otros decoradores como `@attr.getter` y `@attr.deleter` para indicar qué hacer en caso de que se trate de acceder al valor del atributo o eliminar el valor del atributo.

<br/>

---
## Métodos especiales

Al utilizar instancias de clases y {doc}`./operadores-palabras` por default se ejecutan ciertos métodos, a continuación se enlistan los principales métodos de este tipo para definir como se debe de operar con las instancias de las clases, así como otros métodos especiales:

:::{note}
Para más información y una lista completa de métodos especiales visitar la [documentación](https://docs.python.org/3/reference/datamodel.html#special-method-names) de Python.
:::

### Aritméticos

Métodos que se ejecutan al utilizar operadores aritméticos entre dos objetos. 

:::{warning}
Todos estos métodos deben de retornar una instancia de la misma clase o `NotImplemented`.
:::

:::{caution}
Es altamente recomendado verificar que la operación se está haciendo entre instancias de la misma clase o clases compatibles, aunque también se debe de poder manejar las operaciones entre instancias de clases diferentes para evitar que se arroje una excepción. Ver el ejemplo.
:::

:::{note}
Para más información de estos métodos especiales visitar la [documentación](https://docs.python.org/3/reference/datamodel.html#emulating-numeric-types) de Python.
:::

| Método                | Operador |
|-----------------------|----------|
| `__add__(self, other)`    | `+`  |
| `__sub__(self, other)`    | `-`  |
| `__mul__(self, other)`    | `*`  |
| `__truediv__(self, other)` | `/`  |
| `__floordiv__(self, other)` | `//` |
| `__mod__(self, other)`    | `%`  |
| `__pow__(self, other)`    | `**` |

Ejemplo de implementación con el operador `+`:

```python
# Definir clase
class Numero:
    def __init__(self, valor):
        self.valor = valor

    # Sobreescribir operador
    def __add__(self, other):
        if isinstance(other, (int, float, Numero)):
            return Numero(self.valor + (other.valor if isinstance(other, Numero) else other))
        return NotImplemented
```

### Bitwise

Métodos que se ejecutan al utilizar operadores bitwise entre dos objetos. 

:::{warning}
Estos métodos solo deben implementarse con enteros o tipos compatibles (si el objeto tiene sentido bit a bit).
:::

:::{warning}
Todos estos métodos deben de retornar una instancia de la misma clase o `NotImplemented`.
:::

:::{caution}
Es altamente recomendado verificar que los operandos son enteros, aunque también se debe de poder manejar operandos de otras clases para evitar que se arroje una excepción. Ver el ejemplo.
:::

:::{note}
Para más información de estos métodos especiales visitar la [documentación](https://docs.python.org/3/reference/datamodel.html#emulating-numeric-types) de Python.
:::

| Método                | Operador |
|-----------------------|----------|
| `__and__(self, other)`    | `&`  |
| `__or__(self, other)`     | `\|`  |
| `__xor__(self, other)`    | `^`  |
| `__lshift__(self, other)` | `<<` |
| `__rshift__(self, other)` | `>>` |

Ejemplo de implementación con el operador `&`:

```python
# Definir clase
class BitwiseNumero:
    def __init__(self, valor):
        if not isinstance(valor, int):
            raise TypeError("Solo se permiten enteros para operaciones bitwise")
        self.valor = valor

    # Sobreescribir operador
    def __and__(self, other):
        if isinstance(other, BitwiseNumero):
            return BitwiseNumero(self.valor & other.valor)
        elif isinstance(other, int):
            return BitwiseNumero(self.valor & other)
        return NotImplemented
```

### Comparación

Métodos que se ejecutan al utilizar operadores de comparación entre dos objetos. 

:::{warning}
Todos estos métodos deben de retornar `bool` o `NotImplemented`.
:::

:::{caution}
Es altamente recomendado verificar que la comparación se está haciendo entre instancias de la misma clase, aunque también se debe de poder manejar las comparaciones entre instancias de clases diferentes para evitar que se arroje una excepción. Ver el ejemplo.
:::

:::{note}
Por default estos operadores retornar la comparación del valor retornado por la función `id()`, es decir, retorna la comparación de la ubicación en memoria.
:::

:::{note}
Para más información de estos métodos especiales visitar la [documentación](https://docs.python.org/3/reference/datamodel.html#object.__lt__) de Python.
:::

|Método|Operador|
|:----------|:----------:|
|`__eq__(self, other)`|`==`|
|`__ne__(self, other)`|`!=`|
|`__lt__(self, other)`|`<`|
|`__gt__(self, other)`|`>`|
|`__le__(self, other)`|`<=`|
|`__ge__(self, other)`|`>=`|

Ejemplo de implementación con el operador `==`:

```python
# Definir clase
class ClassName:
    def __init__(self, value):
        self.value = value

    # Sobreescribir operador
    def __eq__(self, other):
        if isinstance(other, ClassName):
            return self.value == other.value
        return NotImplemented
```

### Hash

Método para retornar identificadores únicos de instancias. Este identificador se define y se retorna en este método. Estos identificadores se utilizan para poder utilizar las instancias como llaves de diccionarios y añadirse en `sets`. Si dos objetos tienen el mismo _hash_ entonces se considera que son iguales.

:::{caution}
Este método debe de retornar `int`.
:::

:::{note}
Para más información de este método especial visitar la [documentación](https://docs.python.org/3/reference/datamodel.html#object.__hash__) de Python.
:::

```python
# Definir clase
class ClassName:
    # Class body

    # Definir método hash
    def __hash__(self):
        # method body
        ...
        return hash_value
```

:::{warning}
Las instancias con la propiedad _hash_ deben de tener las siguientes características:
1. Deben de ser _inmutables_ (ver {doc}`./tipos-datos`) y sus valores _hash_ no pueden modificarse durante su tiempo de vida.
2. Si dos objetos retornan `True` al usar el operador `==`, entonces sus valores _hash_ deben de ser los mismos.
3. Si se sobreescribe el operador `==`, también se debe de sobreescribir `__hash__()`. Si solo se sobreescribir el operador `==` entonces las instancias si volverán _unhashable_, y no podrán usarse como llaves en diccionarios ni añadirse a `sets`.
:::


### Representación en cadena

Existen dos métodos para imprimir la representanción en cadena de un objeto los cuales se explican a continuación:

:::{tip}
Se debe definir al menos el método `__repr__()`.
:::

:::{note}
Al usar la función `print()` con un objeto automáticamente se llama al método `__str__()` y si este método no existe entonces se llama a `__repr__()`. En caso de que tampoco exista entonces se imprime información sobre la clase y su ubicación en memoria.
:::

:::{caution}
Ambos métodos deben de retornar `str`.
:::

|Método|Descripción|
|:----------|:----------|
|[\_\_str__(self)](https://docs.python.org/3/reference/datamodel.html#object.__str__)|Debe imprimir el objeto de una manera que sea amigable con el usuario. Debe ser una representación en cadena del objeto. Para invocarlo usar la función `str()` o `print()`.|
|[\_\_repr__(self)](https://docs.python.org/3/reference/datamodel.html#object.__repr__)|Debe de imprimir la manera tal cual de construir el objeto en cuestión (evaluando la expresión retornada debe retornar el mismo objeto). Está más orientada a desarrolladores. Para invocarlo usar la función `repr()`.|

<br>

---
## Excepciones

Las excepciones son clases, la mayoría de las excepciones heredan sus características de `Exception`. Es posible crear una excepción personaliza. Para ello se debe de crear una clase cuya clase padre sea `Exception`, aunque se podría usar otras excepciones como clase padre. 

Las excepciones personalizadas son útiles para personalizar el nombre de la excepción y de esta forma ser más explícitos respecto al error ocurrido cuando se muestre el _traceback_.

```python
# Definir clase
MyException(Exception):
    pass
```
- Lo más común es que la clase esté vacía.
- También es posible definir un constructor con el método `__init__()` para definir un mensaje (una propiedad heredada de `Exception`): <br/> `def __init__(self, message):` <br/><pre><code>       self.message = message</code></pre>
- No estrictamente la clase padre tiene que ser `Exception`, puede ser cualquiera de sus subclases.

:::{note}
Para más información de las excepciones revisar {doc}`./exceptions`.
:::

<br/>

---
## Data Classes

Son clases especiales que utilizan el decorator `@dataclass`. Estas clases agregan de manera automática métodos como `__init__()` y `__repr__()`. Es recomendado para clases pequeñas con pocos atributos y detalles.
```python
# Plantilla general de una Data Class

# Importar el decorator
from dataclasses import dataclass

# Definir la clase
@dataclass(*, init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False)
class ClassName:

    # Sintaxis para atributos de instancia
    attr1: type1
    attr2: type2
    ...
    
    # Sintaxis de los métodos
    def method_name([params]):
        # Definición del método

    ...
```
- Se pueden indicar atributos de clase e instancia. _type_i_ son los tipos de datos  de los atributos.
- Los métodos se definen de la misma manera que en las clases normales.

<br>

**Ejemplo**: A continuación se crea una clase sencilla con `dataclass`,
```{code-cell} ipython3
# Importar el decorator
from dataclasses import dataclass

# Definir la clase
@dataclass
class Point:
    x: int
    y: int

# Crear una instancia
p = Point(1, 2)
print(p)
```

<br/>

---
## Buenas prácticas

Al trabajar con clases es aconsejable seguir las siguientes recomendaciones:
1. Inicializar los atributos en el método `.__init__()`.
2. Nombrar a la clase en _CamelCase_ y a los atributos y métodos separados por guión bajo (_attibute_name_ y _method_name_).
3. Usar _docstring_ para indicar qué hacen las clases y los métodos.

<br/>

---
## Métodos útiles

Algunos métodos de clases que existen para todas las clases son:
- `ClassName.mro()`: Muestra el "method resolution order", que en esencia es el orden en el que, las clases buscarán los metodos y atributos, es decir primero buscan dentro de la misma clase y después en las clases padres, si son más de una muestra en que orden se buscan.

<br/>

---
## Funciones útiles

Algunas funciones útiles al trabajar con objetos y clases son:
- `type()`: Retorna la clase a la que pertenece un objeto.
- `dir()`: Enlista todos los atributos y métodos de la clase de un objeto.
- `isinstance()`: Verifica que un objeto pertenezca a una clase. Tener en cuenta que los objetos de las clases hijas, también son instancias de las clases padres.
- `super()`: Determina la siguiente clase en el _MRO_ de `type` y permite llamar a métodos de esa clase.

:::{note}
Para más información de estas funciones visitar la sección de funciones de {ref}`func-objetos-clases`.
:::

### Uso de _super()_

En el siguiente ejemplo vemos cómo se puede usar la función `super()` para poder acceder a métodos de una clase padre.

```{code-cell} ipython3
# Definir una clase
class Figura:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

# Definir una clase hija
class Cuadrado(Figura):
    def __init__(self, lado):
        # Llamar al constructor de la clase base (Figura) usando super()
        super().__init__(lado, lado)

    def area(self):
        # Llama al método area de la clase base (Figura) usando super()
        return super().area()


# Crear una instancia de la clase Cuadrado
c = Cuadrado(lado=2)

# Acceder a los atributos de la clase Figura
print(f"Base: {c.base}")
print(f"Altura: {c.altura}")

# Llamar al método area de la clase Cuadrado
print(f"Area: {c.area()}")
```

