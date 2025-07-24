# Statsmodels

Librería con diversos módulos que provee de clases y funciones para la estimación de muchos modelos estadísticos, pruebas estadísticas y exploración de datos estadísticos. 

Para utilizar `statsmodels` es necesario instalarlo. Desde la terminal usar:
```
# Con pip
pip install statsmodels

# Con conda
conda install statsmodels
```

Una vez instalado se debe de importar. Se recomienda importar los módulos individualmente en lugar de toda la librería:
```python
# Importar statsmodels
import statsmodels

from statsmodels import module_name
```
- _module_name_ es el nombre del módulo que se desea importar. Algunas opciones son:
    - {doc}`./statsmodels-api`: Modelos y métodos de estudios transversales. Se importa por convención como _sm_.
    - {doc}`./statsmodels-tsa-api`: Modelos y métodos de series de tiempo. Se importa por convención como _tsa_.
    - {doc}`./statsmodels-formula-api`: Interface para especificar modelos estadísticos usando cadenas y `DataFrame`. Se importa por convención usando _smf_.

:::{warning}
En este sitio no se recopilan todos los módulos de _statsmodels_. Para más información visitar la [documentación](https://www.statsmodels.org/stable/api.html) y [guía de usuario](https://www.statsmodels.org/stable/user-guide.html#) de _statsmodels_.
:::

---
## Tabla de contenido

```{tableofcontents}
````