# XGBoost

Es una librería de _gradient boosting_ optimizado. Tiene _APIs_ en múltiples lenguajes como Python, R, Scala, Julia, Java, etc. Es muy rápido y su algoritmo es paralelizable. 

Para utilizar `xgboost` es necesario instalarlo. Desde la terminal usar:
```
# Con pip
pip install xgboost

# Con conda
conda install xgboost
```

Una vez instalado se debe de importar:
```python
# Importar xgboost
import xgboost as xgb
```
- _xgb_ es el nombre por convención.

:::{note}
Para más información visitar la [documentación](https://xgboost.readthedocs.io/en/stable/python/python_api.html) de _XGBoost_.
:::

Es recomendable usar esta librería si se cumplen las siguientes características.
- Se tiene muchos _training samples_ (>1000) y menos de 100 _features_.
- El número de _features_ es menor que el número de _samples_ (del _training_).
- Se tienen datos categóricos y numéricos o solo numéricos.

Esta librería no está recomendada para:
- Reconocimiento de imágenes.
- _Computer vision_.
- _NLP_.
- El número de _samples_ es menor que el número de _features_.

<br/>

---
## Conceptos importantes

A continuación se definen algunos conceptos importantes al trabajar con esta librería.

- **Objective** hace referencia a la _function loss_, para medir la diferencia entre los valores verdaderos y los predichos, la intención es minimizar esta función. Correponde al parámetro _objective_.
- **Base Learner**: Los _base learners_ son los modelos individuales del _gradient boosting_, correponde al parámetro _booster_. Existen dos algoritmos base en _XGBoost_:
    - **Lineal**: Casi no se utiliza, el _base learner_ es la suma lineal de términos. El _ensamble model_ también es una suma ponderada de modelos lineales, que por sí solo también es lineal, por lo tanto, en el resultado final no hay combinanciones no lineales de los _features_, por lo que se podría tener resultados identicos con un modelo lineal regular.
    - **Tree**: El más utilizado. El _base learner_ es un árbol de decisión, el _ensamble model_ final es una suma ponderada de árboles de decisión. El resultado final se convierte en una función no lineal de cada árbol.

<br/>

---
## XGboost Parameters.
Son los parámetros por aplicar, corresponden al argumento _params_ en _Learning API_. Existen tres tipos de parámentros:

### Parámetros generales.
Definen la funcionalidad general de _XGBoost_.
- **booster** - {gbtree, gblinear, dart}: Indica el _booster_ a usar (el _base learner_ del modelo a usar en cada iteración)
    - _gbtree_ (default) y _dart_ son modelos basados en árboles.
    - _gblinear_ utiliza funciones lineales.

### Parámetros del booster
Son los parámetros propios del _base learner_ del _booster_ elegido. Dependen si son modelos basados en árboles o en funciones lineales.

### Tree booster:
Parámetros de modelos basados en árboles.

- **eta | learning_rate** - `float: [0,1]`, _default=0.3_: Controla qué tan rápido el modelo ajusta los errores residuales usando _base learners_ adicionales. Valores más bajos requerirán mayores _boosting rounds_ para reducir los errores residuales.
- **max_depth** - `int >= 0`, _default=6_: Profundidad máxima de un árbol. Entre más grande, más complejo y probable que cause _overfit_. Utilizar 0 para indicar que no haya limite en la profundidad. Se debe optimizar usando _CV_.
- **alpha** - _defaut=0_: Regularización L1 de las ponderaciones de las hojas. Entre más alto, mayor será la regularización, por lo que algunas ponderaciones serán cero.
- **lambda** - _default=1_: Regularización L2 de las ponderaciones de las hojas. Valores más altos significan más regularización, por lo que algunas ponderaciones tenderán a cero.
- **gamma** - _default=0_: Reducción mínima de ls _loss function_ permitida para que ocurra un _split_ (de una hoja).  Valores más altos implican menos _splits_.
- **subsample** - `float: [0,1]`, _default=1_: Tamaño (en %) de las observaciones (_samples_) que cada iteración del _boosting_ puede usar para cada árbol. Valores muy bajos pueden provocar _underfitting_, valores muy altos pueden provocar _overfitting_.
- **colsample_bytree** - `float: [0,1]`, _default=1_: Tamaño en %, de los _features_ en cada iteración para cada árbol. Valores más bajos podrían interpretarse como una regularización, valores muy altos, en algunos casos, podrían provocar _overfitting_.

#### Linear booster:
Parámetros de modelos basados en funciones lineales.

- **alpha** - _defaut=0_: Regularización L1 de las ponderaciones de las hojas. Entre más alto, mayor será la regularización, por lo que algunas ponderaciones serán cero.
- **lambda** - _default=1_: Regularización L2 de las ponderaciones de las hojas. Valores más altos significan más regularización, por lo que algunas ponderaciones tenderán a cero.

### Parámetros de la tarea de aprendizaje.
Especifican la tarea de aprendizaje y su correspondiente objetivo. Algunos parámetros imporantes son:
- **Objective**: Define la función de pérdida a minimizar, es decir, la _loss function_ o _objective_. Algunas opciones son:
    - _reg:squarederror_ (default): Usado en problemas de regresión. Anteriormente se llamaba _reg:linear_.
    - _reg:logistic_: Regresión logística.
    - _binary:logistic_: Regresión logística para una clasificación binaria, donde el _output_ serán probabilidades.

```{note}
Para más información sobre los parámetros consultar la [documentación](https://xgboost.readthedocs.io/en/stable/parameter.html#learning-task-parameters).
```

<br/>

---
## Tabla de contenido

```{tableofcontents}
````
