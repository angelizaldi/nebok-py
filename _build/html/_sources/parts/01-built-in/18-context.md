# Context Managers

Un “administrador de contextos” es una función especial, que permite establecer un contexto, ejecutar código y remover el contexto de manera automática. La forma de utilizarlo es con la palabra reservada `with`:
```python
with context_manager(args) as variable-name:
    expression
```
- `_context-manager_`: Es la función, por ejemplo `open()`.
- `_args_`: Son los argumentos del _context-manager_.
- `_variable-name_`: Es el nombre con el que se hará referencia al _context-manager_ la _expression_. No es obligatorio ponerlo, pero se recomienda si _context-manager_ retorna un objeto.
- Algunos context managers comunes son: `open()`, `pandas.ReadExcel()`, etc.

## Crear un administrador de contextos:

Para crear un context manager basado en un función, se debe de definir la función y usar un "_decorator_":
```python
@contextlib.contextmanager
def my_context():
    # Agregar cualquier código para configurar el contexto.
    expression
    
    yield
    
    # Agregar cualquier código para finalizar el contexto.
    expression
```
- `@contextlib.contextmanager`: El decorator.
- `_my_context_`: Nombre que tendrá el administrador de contextos.
- `yield` es para retornar el control al bloque del administrador de contextos. También se puede utilizar para retorna un objeto.
- Se puede agregar código para inicializar el administrador. Por ejemplo, establecer una conexión con un archivo.
- Se puede agregar código para finalizar el administrador. Por ejemplo, finalizar una conexión con un archivo.


## Patrones:

Los administradores de contextos suelen seguir unos patrones dependiendo de la acción que realicen, es decir, si realizan la primera deben realizar la segunda, algunos son:
- Open \- Close.
- Lock \- Release.
- Change \- Reset.
- Enter \- Exit.
- Stat \- End.
- Setup \- Teardown.
- Connect \- Disconnect.
