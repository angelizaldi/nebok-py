# Sets

Son objetos iterables para almacener múltiples elementos en una sola variable. Algunas características del tipo de dato` set` son:
- Se pueden almacenar diferentes tipos de datos en un `set`.
- Los elementos no están ordenados (no están indexados), por lo tanto no se puede acceder a ellos por medio de índices.
- No permite valores duplicados.
- No se pueden modificar los elementos una vez creado el `set`. 

---
## Creación

Para crear un `set` poner los elementos, separados por coma, dentro de llaves `{}`:
```python
X = {x1, x2, ..., xn}
```

---
## Selección de elementos

No se puede extraer los elementos de un set. La única forma para acceder a los elementos de un set es en un `for loop` o conviertiendo el `set` en `list`:

---
##  Agregrar y eliminar elementos:

Para agregar y eliminar elementos de un `set` usar los siguientes métodos:
- Agregar:
 - Agregar un elemento al set usar el método `set.add`.
 - Concatenar sets usar el método `set.update`.
- Eliminar:
 - Eliminar todos los elementos usar el método `set.clear`.
 - Eliminar un elemento específico usar el método `set.discard`.
 - Eliminar y retornar un elemento específico usar el método `set.pop`.
 - Eliminar un elemento específico y retornar error si no existe usar el método `set.remove`.
 
```{note}
Para más información de esos métodos consultar la sección de métodos de sets.
```

Para eliminar todo el `set` se puede usar la palabra reservada `del`:
```python
# Si X es un set
del X
```

---
## Modificar valores de un set:
Los sets no se pueden modificar una vez creados. Un truco para modificar un valor es convertir el set en una lista y después volverlo a convertir en un set. Notar que el nuevo valor no puede existir ya en el `set`.

---
## Iteración en sets:
Para interar sobre todos los elementos de una `set` se puede usar un `for loop`. 
```python
# Iterar sobre los elementos de la lista X:
for ele in X:
    ...
```

```{caution} Como los sets no están indexados el orden en el que aparecen los elementos puede diferir de una iteración a otra.
```



