# Plotting API

API que contiene funciones para graficar árboles y otras funcionalidades.

:::{note}
Para más información visitar la [documentación](https://xgboost.readthedocs.io/en/stable/python/python_api.html#module-xgboost.plotting) de _XGBoost_.
:::

## Funciones

Funciones implementadas en la _Plotting API_. 

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [xgboost.plot_importance](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.plot_importance)(booster,  ax=None,  ...)
  - Grafica la cantidad de veces que un _feature_ se separo (_split_) en todos los _boosting rounds_ como una gráfica de barras. Sirve para identificar los _features_ más importantes.
* - [xgboost.plot_tree](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.plot_tree)(booster,  fmap='',  ...)
  - Grafica el árbol especificado.
* - [xgboost.to_graphviz](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.to_graphviz)(booster,  fmap='',  ...)
  - Convierte el árbol especificado en una instancia `GraphViz`. IPython puede grafica automáticamente la instancia `GraphViz` devuelta. De lo contrario, se debe llamar al método `.render()` de la instancia `GraphViz` devuelta.
```

<br/>

### Notas de _plot_importances_

[xgboost.plot_importance](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.plot_importance): Gráfica un la cantidad de veces que un feature se separo (split) en todos los boosting rounds como una gráfica de barras. Sirve para identificar los features más importantes.
```python
# Sintaxis de llamada
xgb.plot_importances(booster, ax=None, height=0.2, xlim=None, ylim=None, 
                     title='Feature importance', xlabel='F score', ylabel='Features', 
                     fmap='', importance_type='weight', max_num_features=None, 
                     grid=True, show_values=True, values_format='{v}', **kwargs)
```
**Parámetros:**
- **booster** - `Booster`, `XGBModel` o `dict`: Modelo que contiene los árboles.

<br/>

### Notas de _plot_tree_

[xgboost.plot_tree](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.plot_tree): Gráfica un árbol en específico de gradient boosting.
```python
# Sintaxis de llamada
xgb.plot_tree(booster, fmap='', num_trees=0, rankdir=None, ax=None, **kwargs)
```
**Parámetros:**
- **booster** - `Booster`, `XGBModel`: Modelo que contiene los árboles.
- **num_trees** - `int`: El índicel del árbol a graficar, la indexación empieza en cero, y máximo es _num_boost_roung-1_.
- **rankdir** - `str`: Se pasa a `GraphViz` a través de _graph_attr_.

<br/>

