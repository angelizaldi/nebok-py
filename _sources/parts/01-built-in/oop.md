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

```{warning} En esta sección no se explican detallamente conceptos relacionados con la POO, se da por hecho que ya se conocen. Simplemente se presentan algunas acciones comunes en POO como crear clases, definir atributos, métodos, etc.
```

---
## Clases

Son una representación abstracta de un objeto.

### Crear una clase

Para crear una clase se usa: 
```python
# Crear una clase nueva
class ClassName:
    # Definición de la clase
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
obj = ClassName([args])
```
- _obj_ será una instancia de la clase `ClassName`.
- _args_ por lo general, son los argumentos del método __init__(), pero no necesariamente tiene que ser así. Se deben de proveer al menos los argumentos obligatorios, es decir, los que no tienen un valor por default.


<br/>

### Clases hijas

Las clases hijas son clases que heredan los métodos y atributos de otra clase. Para definir una clase hija que heredará los atributos y métodos de la clase padre se utiliza:
```python
# Definir una clase hija
class ChildClass(ParentClass):
    # Definición de la clase
```
- _ChildClass_ es el nombre que tendrá la clase hija, que hereda atributos y métodos de _ParentClass_.
- _ParentClass_ es el nombre de la clase padre. Ya tuvo que haber sido definida, antes que la clase hija.

Para utilizar los métodos o el constructor de la clase padre dentro de la clase hija usar:
```python
class ChildClass(ParentClass):
    
    ClassParent.method_name(self, [args])
```
- No estrictamente el primer argumento debe ser `self`, pero sí un objeto. Puede ser otro objeto que tenga sentido con el método al que se está llamando.

Para utilizar los atributos o métodos de la clase padre en una instancia de la clase hija en el programa usar:
```python
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
Los atributos de instancia son atributos propios de los objetos y cuyos valores pueden diferir de una objeto a otro. Los atributos de instancias normalmente se definen en el método `__init__()` (ver {ref}`init`), pero no necesariamente:
```python
# Crear una clase nueva
class ClassName:
    
    # Definir atributos de instancia en el método init
    def __init__(self, [args])
        self.attribute_name = expression
        ...
```
- automáticamente _attribute_name_ será un atributo de la clase al momento de inicializar el objeto.
- El constructor puede reciber otros parámetros expresados como _args_ en este ejemplo, pero son opcionales. 
- _expression_ puede ser un escalar o una expresión que utilice uno o más argumentos del método.

<br/>

---
#### Atributos en métodos

Se pueden definir atributos de instancia dentro de un método diferente a `__init__()`, el cual debe de asignar un valor al atributo. Estos atributos se inicializan si y solo si el método es llamado.
```python
# Crear una clase nueva
class ClassName:
        
    # Definir atributos de instancia dentro de un método
    def method_name(self, [args]):
        self.attribute_name = expression
```
- _attribute_name_ será un atributo de instancia, solo si _method_name_ es llamado.
- _expression_ puede ser un esclar o una expresión que utilice uno o más argumentos del método.
- En general es recomendado inicializar los atributos de instancias en el método `__init__()` y no en otros métodos.

<br/>

---
#### Recuperar valores de atributos de instancia dentro de la clase

Si se quiere obtener al valor un atributo de instancia dentro la misma de la clase se usa `self.attribute_name`:

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
- En este ejemplo `method_name` recupera el valor de `attribute_name` para retornarlo. Cabe destacar que no es necesario definir métodos para recuperar los valores de los atributos de instancia.

<br/>

---
#### Acceder a valores de atributos de instancia de una instancia
Una vez definido una instancia (objeto) de la clase se puede acceder los valores de sus atributos de instancia con `obj.attribute_name`:
```python
# Crear un instancia
obj = ClassName(args)

# Recuperar el valor de un atributo
obj.attribute_name
```
- _obj_ es un objeto de una clase.

<br/>

---
### Atributos de clase

Los atributos de clase son atributos que todos los objetos de una misma clase tendrán en común y con el mismo valor. Para definir un atributo de clase se realiza en el cuerpo de la clase, afuera de cualquier método:
```python
# Definir una clase nueva
class ClassName:
    
    # Definir un atributo de clase
    ATTRIBUTE_NAME = val
    
    
```
- Por convencion los nombres de atributos a nivel de clase se ponen en mayúsculas, pero no es obligatorio.

<br/>

---
#### Recuperar valores de atributos de clase dentro de la clase

Si se quiere obtener el valor de un atributo de clase dentro la misma de la clase usar `ClassName.ATTRIBUTE_NAME` o `self.ATTRIBUTE_NAME`:
```python
# Definir una clase nueva
class ClassName:
    
    # Definir un atributo de clase
    ATTRIBUTE_NAME = val
    
    # Acceder al atributo un método    
        def method_name(self):
            return ClassName.ATTRIBUTE_NAME
           #return self.ATTRIBUTE_NAME
```
- `ClassName` es un nombre arbitrario de la clase.
- `ATTRIBUTE_NAME` es un nombre arbitrario del atributo de clase.
- `method_name` es un nombre arbitrario de un método.
- Se recomienda usar `ClassName.ATTRIBUTE_NAME`, para identificar que es un atributo a nivel de clase.
- En este ejemplo `method_name` recupera el valor de `ATTRIBUTE_NAME` para retornarlo. Cabe destacar que no es necesario definir métodos para recuperar los valores de los atributos de clase.

<br/>

---
#### Recuperar valores de atributos de clase de una instancia

Una vez definido una instancia (objeto) de la clase se puede acceder a los valores de sus atributos de clase desde un script o desde la consola con `obj.__class__.ATTRIBUTE_NAME` o `obj.ATTRIBUTE_NAME`:
```python
# Crear un instancia
obj = ClassName(args)

# Recuperar valores de atributos de clase fuera de la clase
obj.__class__.ATTRIBUTE_NAME
obj.ATTRIBUTE_NAME
```
- `ClassName` es un nombre arbitrario de la clase.
- `ATTRIBUTE_NAME` es un nombre arbitrario del atributo de clase.
- _obj_ es una instacia de `ClassName` .

```{attention} Modificaciones en el valor de un atributo de clase en una instancia **no** modifica el valor de ese atributo para toda la clase, en cambio se reemplaza por un nuevo atributo en la instancia con el mismo nombre que el atributo a nivel de clase.
```

Si se desea modificar el valor de un atributo de clase para todos los objetos usar:
```python
# Modificar el valor de ATTRIBUTE_NAME para toda la clase
ClassName.ATTRIBUTE_NAME = new_val
```
- `ClassName` es un nombre arbitrario de la clase.

<br/>

----
#### Atributos de clase de forma dinámica

Se puede crear un atributo de clase de manera dinámina desde un script o desde la consola usando:
```python
# Craer el atributo de clase NEW_ATTRIBUTE_NAME
ClassName.NEW_ATTRIBUTE_NAME = value
```
- Se creará el atributo _NEW_ATTRIBUTE_NAME_ y todos las instancias tendrán ese nuevo atributo.

<br/>

---
## Métodos

Los métodos son acciones que pueden realizar las instancias o las clases mismas. Existen diversos tipos de métodos


(init)=
### Metodo __init__

Es un método el cual es llamado automáticamente cuando una instancia de la clase es creada. Generalmente se usa para definir los atributos de instancia.
```python
# Crear una clase nueva
class ClassName:

    # Definir el método __init__
    def __init__(self, [params]):
        self.attribute1 = expression
```
- El primer parámetro del método debe de ser `self`, incluso cuando no hay más parámetros.
- _expression_ puede ser un escalar o una expresión que utilice uno o más argumentos del método.
- El método `__init__()` puede o no reciber otros parámetros adicionales los cuales pueden o no tener valores por default. Si no tienen valores por default, los valores de esos parámetros se deben de indicar al momento de crear el objeto.

<br/>

---
### Métodos de instancia

Los métodos de instancia son las acciones asociadas a una instancia de una clase. Para crear métodos de instancia se utiliza una función, cuyo primer argumento debe de ser `self`.
```python
# Crear una clase nueva
class ClassName:
    
    # Definir un método de instancia
    def method_name(self, [params]):
        body
```
- El primer parámetro del método debe de ser `self`, incluso cuando no hay más parámetros.
- _params_ son otros posibles parámetros de la función, pero son opcionales.
- Es altamente recomendado poner docstrings para indicar qué hace cada método.

<br/>

#### Usar un método

Para llamar a un método de una clase, se utiliza el nombre del objeto, un punto y el nombre del método con sus argumentos, si tiene.
```python
# Crear un instancia
obj = ClassName(args)

# Usar un método de una instancia
obj.method_name(args)
```
- _obj_ es un objeto de una clase `ClassName`.
- No se pone el argumento self, porque la sintaxis anterior equivale a:

```python
ClassName.method_name(obj, args)
```
- El mismo objeto será el primer argumento, del método _method_name_ de la clase _ClassName_.

<br/>

---
### Métodos on-demand

Se pueden crear métodos fuera de la definición de clase de forma dinámica, para ello se define una función y posteriormente se asigna el nuevo método de la clase
```python
# Definir una función
def method_name(self, [args]):
    # Definición del metodo
    body

# Asignar el método a una clase
ClassName.method_name = method_name
```
- _method_name_ será un nuevo método de `ClassName`.

<br/>

---
### Métodos de clase

Existen métodos que se pueden declarar a nivel de clase. Para declarar este tipo de métodos se utiliza el decorator `@classmethod`. Este tipo de métodos se usan para crear objetos sin llamar al constructor, como solo puede haber un constructor esté método permite modificar la forma como se llama al constructor permitiendo tener diferentes formas de inicializar un objeto.
```python
# Crear una clase nueva
class ClassName:
    
    # Definir un método de clase
    @classmethod
    def method_name(cls, [params]):
        # Definición del método
        ...
        return cls([params])
```
- El primer argumento debe de ser `cls` por convención. `cls` es un objeto que hace referencia a la clase misma. `csl` es equivalente a usar la clase como tal `ClassName`.
- En el cuerpo de la función se puede hacer cualquier modificación a los valores de los parámetros.
- En el `return` `cls()` llamará a `__init__([params])`, es decir `return(cls)` equivale a `__init__([args])` o `ClassName([args])` (que en todo caso lo que hace es llamar al método `__init__()`).

<br>

Para inicializar un objeto a través de un método de clase se usa:
```python
# Crear instancia con un método de clase
obj = ClassName.method_name([args])
```
- _method_name_ es un método a nivel de la clase `ClassName`.

<br>

**Ejemplo**: En este ejemplo se define una clase que crea una fecha indicando el año, mes y día individualemente. Posteriormente se define un método de clase que permite crear la fecha desde una cadena en lugar de los elementos individuales.
```{code-cell} ipython3
# Definir la clase
class Fecha:    
    # Definir el constructor
    def __init__(self, year, month, day):
      # Asignar los atributos de año, mes y dia.
      self.year, self.month, self.day = year, month, day
    
    # Se definie el método a nivel de clase desde_str.
    @classmethod
    def desde_str(cls, datestr):
        year, month, day = map(int, datestr.split("-"))
        # Equivale a: Fecha.__init__(year, month, day)
        return cls(year, month, day)

# Crear instancia desde el metodo de clase
fecha = Fecha.desde_str('2023-01-01')   

# Imprimir los atributos de fecha
print(fecha.year)
print(fecha.month)
print(fecha.day)
```
- El método de clase `desde_str` permite inicializar un objeto con base a una cadena que contiene una fecha en lugar de pasar individualmente cada atributo.

<br/>

---
### Métodos estáticos

Son un tipo de método de clase, el método se asocia con la clase, no con las instancias de la clase. Para crear métodos estáticos se usa el decorator `@staticmethod`:
```python
# Crear una clase nueva
class ClassName:
    
    # Definir un método estático
    @staticmethod
    def method_name([params]):
        # Definición del método
```
- Los métodos estáticos no tienen el parámetros `self` porque `self` se asocia a las instancias.
- Los métodos estáticos no pueden acceder a los atributos de instancia o métodos de instancias.

Para usar un método estático usar:
```
ClassName.method_name([params])
```

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

    # Sintaxis para atributos de instancia:
    attr1: type1
    attr2: type2
    ...
    
    # Definición de los métodos
    def method_name([params]):
        # Definición del método
```
- Se pueden indicar atributos de clase e instancia. `type_i` son los tipos de datos  de los atributos.
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
## Funciones útiles
Algunas funciones útiles al trabajar con objetos y clases son:
- `type()`: Retorna la clase a la que pertenece un objeto.
- `dir()`: Elista todos los atributos y métodos de la clase de un objeto.
- `isinstance()`: Verifica que un objeto pertenezca a una clase. Tener en cuenta que los objetos de las clases hijas, también son instancias de las clases padres.

<br/>

---
## Métodos útiles
Algunos métodos de clases que existen para todas las clases son:
- _ClassName_`.mro()`: Muestra el "method resolution order", que en esencia es el orden en el que, las clases buscarán los metodos y atributos, es decir primero buscan dentro de la misma clase y después en las clases padres, si son más de una muestra en que orden se buscan.

