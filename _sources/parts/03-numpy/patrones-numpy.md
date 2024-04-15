# Patrones útiles

En esta sección se revisas algunas operaciones y procedimientos comunes que se hacen con objetos de la librería `numpy`.

## Matemáticas

Operaciones y procedimientos de caracter matemático comunes con objetos de la librería `numpy`.

### Distancia entre puntos

Para calcular todas las distancias al cuadrado entre una serie puntos, considerando un `ndarray` bidimensional de _shape_ `(k, 2)`, donde la primer columna son las coordenadas de $x$ y la segunda columna son las coordenadas de $y$ usar:

```python
# Calcular matriz de distancias entre los puntos pi y pj
dist_sq = np.sum((X[:, np.newaxis, :] - X[np.newaxis, :, :]) ** 2, axis=-1)
```
- El valor retornado será una matriz simétrica, que indica la distancia de cada punto $p_i$ con respecto a cada punto $p_j$.
- La diagonal principal está conformada por valores cero, esto es así porque la distancia de cada punto consigo mismo es cero.
- Para entender cómo funciona este patrón considerar que el objetivo es calcular $(x_2-x_1)^2 + (y_2-y_1)^2$, para cada par de puntos $P_i$ y $P_j$ en la matriz, entonces:
    1. Se convierte la matriz `(m, n)` en `(m, 1, n)` (tensor columna) y `(1, m, n)` (un tipo tensor fila), esto para facilitar el siguiente paso.
    2. Por medio de broadcasting se convertirá la operación en `(10, 10, 2)`, donde la primer rebanada es el producto cartesiano de las coordenadas $x$ y la segunda rebanada es el producto cartesiano de las coordenadas $y$. Con la sustracción (`-`) los valores son la resta de cada par ordenado en los productos cartesianos, en su respectiva rebanada, es decir cada $(x_i-x_j)$ en la primer rebajada y cada $(y_i-y_j)$ en la segunda rebanada.
    3. Se aplica la exponenciación al cuadrado _element-wise_, es decir cada $(x_i-x_j)^2$ en la primer rebajada y cada $(y_i-y_j)^2$ en la segunda rebanada.
    4. Finalmente al sumar en el eje 2 (`axis=-1`), se suma efectivamente $(x_i-x_j)^2 + (y_i-y_j)^2$ porque recordar que la primer rebanada son las coordenadas $x$ y la segunda rebanada son las coordenadas $y$.