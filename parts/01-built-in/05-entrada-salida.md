# Entrada y salida de datos

En esta sección se cubren las funciones para impimir valores en la consola o para solicitar el ingreso de datos desde la consola.

**print**:

`print()`: Imprime en la consola objetos de python. Para ello utiliza los métodos `__str__()` o `__repr__()` de cada clase de cada objeto.
```python
print(*objects, sep=' ', end='\n', file=None, flush=False)
```

**Parámetros:**
- **`value`** \- `object`: Puede ser más de un objeto separado por coma.
- **`sep`** \- `str`: Es para indicar cómo separar cada objeto, por default es un espacio en blanco.
- **`end`** \- `str`: Es para indicar como terminar la impresión, por default es una nueva línea.

**Retorna:**
-  `None`.

---
**input**:

`input()`: Solicita ingresar datos al usuario mientras se ejecuta el programa.
```python
input(prompt)
```

**Parámetros:**
- **`prompt`** \- `str`: Es el mensaje que se le mostrará al usuario al momento de solicitar que ingrese datos.

**Retorna:**
-  `object`.

