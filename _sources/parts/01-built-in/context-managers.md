# Context Managers

Un “administrador de contextos” es una función especial, que permite establecer un contexto, ejecutar código y remover el contexto de manera automática, útil en casos como leer archivos o conectarse a bases de datos. Normalmente se utilizan con la palabra reservada `with`:
```python
# Usando context_manager con with 
with context_manager(args) as variable-name:
    # with body
```
- _context-manager_: Es una función, por ejemplo `open()`, que retorna un objeto que implementa los métodos `.__enter__()` y `.__exit__()`.
- _args_: Son los argumentos del _context-manager_.
- _variable-name_: Es el nombre con el que se hará referencia al objeto retornado por _context-manager_ en _expression_. No es obligatorio ponerlo, pero se recomienda si _context-manager_ retorna un objeto.
- `with` gestiona automáticamente la entrada y la salida del contexto.
- Algunos context managers comunes son: `open()`, `pandas.ReadExcel()`, etc.

<br/>

---
## Crear un administrador de contextos

Para crear un _context manager_ basado en una función, se debe de definir un _generator_ y usar el _decorator_ `@contextlib.contextmanager`:

:::{note}
Un administrador de contextos también se puede definir como una clase. Para ello simplemente se deben de definir los métodos `__enter__` y `__exit__`
:::

```python
# Decorator
@contextlib.contextmanager
def my_context():
    # Agregar cualquier código para configurar el contexto.
    print("Entrando al contexto.")
    expressions
    
    yield object
    
    # Agregar cualquier código para finalizar el contexto.
    print("Saliendo del contexto.")
    expressions

# Alternativamente se puede usar clases para definir el administrador de contextos
class MyContext:
    def __enter__(self):
        # Agregar cualquier código para configurar el contexto.
        print("Entrando al contexto.")
        expressions
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # Agregar cualquier código para finalizar el contexto.
        print("Saliendo del contexto.")
        expressions
```
- `@contextlib.contextmanager`: Es el decorator.
- _my_context_: Nombre que tendrá el administrador de contextos.
- Se puede agregar código para inicializar el contexto. Por ejemplo, establecer una conexión con un archivo.
- `yield` se utiliza para retornar el control ya dentro del contexto y opcionalmente retornar un objeto que es el que se utiliza junto con `with ... as ...`.
- Se puede agregar código para finalizar el contexto. Por ejemplo, finalizar una conexión con un archivo.

**Ejemplo 1**

En este ejemplo se define un administrador de contexto de que conecta a una base de datos, retornando la conexión con la base de datos y posteriormente maneja la desconexión.

```python
# Definir administrador de contextos
@contextlib.contextmanager
def database(url):
    # Establecer conexión
    db = postgres.connect(url)

    # Retornar control al adminstrador
    yield db
    
    # Eliminar conexión
    db.disconnect()

# Utilizar administrador de contextos con with
with database(url) as my_db:
    my_list = my_db.execute('SELECT * FROM source')
```

**Ejemplo 2**

En este ejemplo se define un administrador de contexto que no retorna ningún objetos, simplemente se cambia de directorio y al finalizar retornar al directorio original.

```python
# Definir administador de contextos
@contextlib.contextmanager
def in_dir(path):
    # Guardar directorio actual
    old_dir = os.getcwd()
    
    # Cambiar al directorio del argumento
    os.chdir(path)
    yield
    
    # Retornar al directorio original
    os.chdir(old_dir)

# Utilizar administrador de contextos con with
with in_dir('/data/project_1/'):
    project_files = os.listdir()
```

<br/>

---
## Patrones

Los administradores de contextos suelen seguir unos patrones dependiendo de la acción que realicen, es decir, si realizan la primera deben realizar la segunda, algunos son:
- Open \- Close.
- Lock \- Release.
- Change \- Reset.
- Enter \- Exit.
- Start \- End.
- Setup \- Teardown.
- Connect \- Disconnect.
