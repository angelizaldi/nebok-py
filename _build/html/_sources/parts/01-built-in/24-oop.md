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

```{warning} Esta sección no pretende explicar la programación orientada a objeto ni el uso de clases en python, sino simplemente presentar brevemente algunas acciones comunes con las clases, métodos, atributos e instancias en python.
```

---
## Clases

Son una representación abstracta de un objeto.

### Definición de una clase

Para crear una clase se usa: 
```python
# Crear una clase nueva
class ClassName:
    # Definición de la clase
    ...
```
- _ClassName_ es el nombre que tendrá la clase. El nombre por convención se pone en "CamelCase" (primer letra de cada palabra en mayúsculas, sin espacios entre palabras).
- Todo el código indentado será parte de la clase.
- Se puede crear una clase "vacía" usando la palabra reservada `pass`.

```{caution} Si se van a usar funciones de otros módulos/librerías dentro del cuerpo de la clase, se debe de importar afuera de la definición de la clase.
```

### Declaración de objetos:

Para inicializar un objeto/instancia de una clase usar:
```
obj = ClassName([args])
```
- _obj_ será un objeto de la clase ClassName.
- _args_ son los argumentos del método __init__(), si tiene, particularmente se deben poner los que no tienen valores por default.


### Clases hijas

Las clases hijas son clases que heredan los métodos y atributos de otra clase. Para definir una clase hija que heredará los atributos y métodos de la clase padre se utiliza:
```python
class ChildClass(ParentClass):
    # Definición de la clase
    ...
```
- _ChildClass_ es el nombre que tendrá la clase hija, que hereda atributos y métodos de _ParentClass_.
- _ParentClass_ es el nombre de la clase padre, ya tuvo que haber sido definida, antes que la clase hija.

Para utilizar los métodos o el constructor de la clase padre dentro de la clase hija usar:
```python
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

---
## Atributos

Los atributos son las propiedades que tendrán las instancias (objetos) de la clase.

---
### Atributos de instancias
Los atributos de instancia son atributos propios de los objetos y cuyos valores pueden diferir de una objeto a otro. Los atributos de instancias normalmente se definen en el constructor (método `__init__()`):
```python
# Definir atributos de instancia dentro del constructor
def __init__(self, [args])
    self.attribute_name = expression
    ...
```
- automáticamente _attribute_name_ será un atributo de la clase al momento de inicializar el objeto.
- El constructor puede reciber otros parámetros expresados como _args_ en este ejemplo, pero son opcionales. 
- _expression_ puede ser un `scalar` o una expresión que utilice uno o más argumentos del método.

---
#### Atributos en métodos:

Se pueden definir atributos de instancia dentro de un método, el cual debe de asignar un valor al atributo. Estos atributos se inicilizan si y solo si el método es llamado:
```python
# Definir atributos de instancia dentro de un método
def method_name(self, [args]):
    self.attribute_name = expression
    ...
```
- _attribute_name_ será un atributo de la clase, solo si _method_name_ es llamado.
- _expression_ puede ser un `scalar` o una expresión que utilice uno o más argumentos del método.
- En general es recomendado inicializar los atributos de instancias en el método __init__() y no en otros métodos.

---
#### Acceder a valores de atributos de instancia dentro de la clase

Si se quiere obtener al valor un atributo de instancia dentro la misma de la clase usar usar:
```python
# Recuperar valores de atributos de instancia dentro de la clase
self.attribute_name
```

---
#### Acceder a valores de atributos de instancia fuera de la clase:

Una vez definido una instancia (objeto) de la clase se puede acceder los valores de sus atributos de instancia con:
```python
# Recuperar valores de atributos de instancia fuera de la clase
obj.attribute_name
```
- _obj_ es un objeto de una clase.

---
### Atributos de clase.

Los atributos de clase son atributos que todos los objetos de una misma clase tendrán en común. Para definir un atributo de clase se realiza en el cuerpo de la clase, afuera de cualquier método:
```python
# Definir valores de atributos de clase dentro de la clase
class ClassName:
    ATTRIBUTE_NAME = val
    ...
```
- Por convencion los nombres de atributos a nivel de clase se ponen en mayúsculas, pero no es obligatorio.

---
#### Acceder a valores de atributos de clase dentro de la clase

Si se quiere obtener al valor un atributo de clase dentro la misma de la clase usar cualquiera de los siguientes métodos, pero se recomienda el primero, para identificar que es un atributo a nivel de clase:
```python
# Recuperar valores de atributos de clase dentro de la clase
# Los dos son equivalente.
ClassName.ATTRIBUTE_NAME
self.ATTRIBUTE_NAME
```

---
#### Acceder a valores de atributos de clase fuera de la clase

Una vez definido una instancia (objeto) de la clase se puede acceder a los valores de sus atributos de clase desde un script o desde la consola con cualquiera de las siguientes opciones:
```python
# Recuperar valores de atributos de clase fuera de la clase
# Las dos son equivalentes
obj.__class__.ATTRIBUTE_NAME
obj.ATTRIBUTE_NAME
```
- _obj_ es un objeto de una clase.

```{attention} Modificaciones en el valor de un atributo a nivel de clase en una instancia NO modifica el valor de ese atributo a nivel de clase, en cambio se reemplaza por un nuevo atributo en la instancia con el mismo nombre que el atributo a nivel de clase.
```

Si se desea modificar un atributo a nivel de clase para todos los objetos usar:
```python
# Modificar el valor de ATTRIBUTE_NAME para toda la clase
ClassName.ATTRIBUTE_NAME = new_val
```

----
#### Crear atributos de clase de forma dinámica

Se puede crear un atributo de clase de manera dinámina desde un script o desde la consola usando:
```python
# Craer el atributo de clase NEW_ATTRIBUTE_NAME
ClassName.NEW_ATTRIBUTE_NAME = value
```
- Se creará el atributo _NEW_ATTRIBUTE_NAME_ y todos las instancias tendrán ese nuevo atributo.

---
## Métodos

Los métodos son "acciones" que pueden realizar los objetos. Existen diversos tipos de métodos

---
### Constructor (__init__)
Es un método el cual es llamado automáticamente cuando un objeto de la clase es creado.
```python
# Definir el método __init__
def __init__(self, [args]):
    self.attribute1 = expression
    self.attribute2 = expression
    ...
```
- _expression_ puede ser un `scala` o una expresión que utilice uno o más argumentos del método.
- El método `__init__()` puede o no reciber otros argumentos adicionales los cuales pueden o no tener valores por default. Si no tienen valores por default los valores de esos parámetros se deben de indicar al momento de crear el objeto.

---
### Métodos generales

Para crear métodos se utiliza una función, cuyo primer argumento debe de ser self:
```python
def method_name(self, [args]):
    # Definición del método
    ...
```
- `self` debe de ser el primer argumento de todos los métodos en la clase, incluso cuando no hay más argumentos.
- _args_ son otros posibles argumentos de la función, pero no son obligatorios.
- Es altamente recomendado poner docstrings para indicar qué hace cada método.

---
#### Usar un método

Para llamar a un método de una clase, se utiliza el nombre del objeto, un punto y el nombre del método con sus argumentos, si tiene:
```
obj.method_name([args])
```
- _obj_ es un objeto de una clase.
- No se pone el argumento self, porque la sintaxis anterior equivale a:
```
ClassName.method_name(obj, [args])
```
- El mismo objeto será el primer argumento, del método _method_name_ de la clase _ClassName_.

---
### Métodos on-demand

Se pueden crear métodos fuera de la definición de clase de forma dinámica, para ello se define una función y posteriormete se asigna el nuevo método de la clase
```python
# Definir una función
def method_name(self, [args]):
    # Definición del metodo
    ...

# Asignar el método a una clase
ClassName.method_name = method_name
```

---
### Métodos de clase

Existen métodos que se pueden declarar a nivel de clase. Para declarar este tipo de métodos se utiliza el decorator `@classmethod`. Este tipo de métodos se usan para crear objetos sin llamar al constructor, como solo puede haber un constructor esté método permite modificar la forma como se llama al constructor permitiendo tener diferentes formas de inicializar un objeto.
```python
# Definir un método de clase
@classmethod
def method_name(cls, [args]):
    # Definición del método
    ...
    return cls([args])
```
- El primer argumento debe de ser `cls` por convención. `cls` es un objeto que hace referencia a la clase misma. `csl` es equivalente a usar la clase como tal `ClassName`.
- En el cuerpo de la función se puede hacer cualquier modificación a los valores de los parámetros.
- En el `return` `cls()` llamará a `__init__([args])`, es decir `return(cls)` equivale a `__init__([args])` o `ClassName([args])` (que en todo caso lo que hace es llamar al método `__init__()`).

Para inicializar un objeto a través de un método de clase se usa:
```python
obj = ClassName.method_name([args])
```
- _method_name_ es un método a nivel de clase.

Ejemplo
```{code-cell} ipython3
#Se definie la clase
class Fecha:    
    # Constructor
    def __init__(self, year, month, day):
      # Asignar los atributos de año, mes y dia.
      self.year, self.month, self.day = year, month, day
    
    # Se definie el método a nivel de clase from_str.
    # Este método permite inicializar un objeto con base a una cadena 
    # que contiene una fecha en lugar de pasar individualmente cada atributo.
    @classmethod
    def desde_str(cls, datestr):
        # Se separa la cadena en sus partes y se convierte a entero
        year, month, day = map(int, datestr.split("-"))
        # Se retorna la clase, lo que equivale a llamar BetterDate.__init__(year, month, day)
        return cls(year, month, day)

# Al momento de crear el objeto se debe de indicar 
# el método de clase y pasar sus argumentos, 
# en la sintaxis ClassName.method_name(args):
fecha = Fecha.desde_str('2020-04-30')   
print(fecha.year)
print(fecha.month)
print(fecha.day)
```

---
### Métodos estáticos:

Son un tipo de método de clase, el método se asocia con la clase, no con las instancias de objectos. para crear uno se usa el decorator `@staticmethod`:
```python
@staticmethod
def method_name([args]):
    # Definición del método
    ...
```
- Los métodos estáticos no tienen el argumento `self` porque `self` se asocia a las instancias.
- Los métodos estáticos no pueden acceder los valores de atributos de instancias o métodos de instancias.

Para usar un método estático usar:
```
ClassName.method_name([args])
```

## Data Classes

Son un clases especiales que utilizar el decorator `@dataclass`. Estas clases agregan de manera automática métodos como `__init__()` y `__repr__()`. Es recomendado para clases pequeñas con pocos atributos y detalles.
```python
@dataclass(*, init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False)
class ClassName:
    # Sintaxis para atributos de clase:
    class_attr1: ClassVar[type1] = value
    ...
    
    # Sintaxis para atributos de instancia:
    attr1: type1
    attr2: type2
    ...
    
    # Definición de los métodos
    ...
```
- Se pueden indicar atributos de clase e instancia.
- Los métodos se definen de la misma manera que en las clases normales.

---
## Funciones útiles:
Algunas funciones útiles al trabajar con objetos son:
- `type()`: Retorna la clase a la que pertenece un objeto.
- `dir()`: Elista todos los atributos y métodos de la clase de un objeto.
- `isinstance()`: Verifica que un objeto pertenezca a una clase. Tener en cuenta que los objetos de las clases hijas, también son instancias de las clases padres.

---
## Métodos útiles:
Algunos métodos de clases que existen para todas las clases son:
- _ClassName_.mro(): Muestra el "method resolution order", que en esencia es el orden en el que, las clases buscarán los metodos y atributos, es decir primero buscan dentro de la misma clase y después en las clases padres, si son más de una muestra en que orden se buscan.

