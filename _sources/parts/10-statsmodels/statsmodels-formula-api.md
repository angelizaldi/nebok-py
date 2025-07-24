# API de Fórmulas

Proporciona una interfaz basada en fórmulas para especificar modelos estadísticos, similar a la sintaxis de R.
- Permite especificar modelos usando fórmulas (por ejemplo, `y ~ x1 + x2`).
- Soporta modelos lineales, generalizados y mixtos.
- Facilita la creación de modelos interactivos en entornos como _Jupyter Notebook_.

Es necesario importar el módulo:

```python
# Importar api
import statsmodels.formula.api  as smf

# Importar función específica
from statsmodels.formula.api import func_name
```
- _smf_ es el nombre por convención.
- func_name_ es el nombre de la función.

:::{note}
Para más información visitar la [documentación](https://www.statsmodels.org/stable/api.html#statsmodels-formula-api) de _statsmodels_.
:::

A continuación se presenta un resumen de cada una de las clasificaciones:
- **Modelos Discretos y de Conteo**: Modelos estadísticos para datos discretos o de conteo, como regresión Poisson, binomial negativa y logit.
- **Ecuaciones de Estimación Generalizadas (GEE)**: Métodos para modelar datos correlacionados o agrupados, como en estudios longitudinales o clínicos.
- **Modelos Lineales Generalizados (GLM)**: Extensión de los modelos lineales para trabajar con distribuciones no normales, como binomial, Poisson o gamma.
- **Otros Modelos**: Incluye modelos especializados, como modelos de duración (survival analysis) o modelos no paramétricos.
- **Regresión**: Modelos de regresión clásicos, como regresión lineal (OLS), regresión robusta y regresión ponderada.


## Funciones

Funciones implementadas en _formula.api_.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - **Modelos Discretos y de Conteo**
  -
* - [conditional_logit](https://www.statsmodels.org/stable/generated/statsmodels.formula.api.conditional_logit.html)(formula, data, ...)
  - Crea un [ConditionalLogit](https://www.statsmodels.org/stable/generated/statsmodels.discrete.conditional_models.ConditionalLogit.html) a partir de una fórmula y un `DataFrame`.
* - [conditional_mnlogit](https://www.statsmodels.org/stable/generated/statsmodels.formula.api.conditional_mnlogit.html)(formula, data, ...)
  - Crea un [ConditionalMNLogit](https://www.statsmodels.org/stable/generated/statsmodels.discrete.conditional_models.ConditionalMNLogit.html) a partir de una fórmula y un `DataFrame`.
* - [conditional_poisson](https://www.statsmodels.org/stable/generated/statsmodels.formula.api.conditional_poisson.html)(formula, data, ...)
  - Crea un [ConditionalPoisson](https://www.statsmodels.org/stable/generated/statsmodels.discrete.conditional_models.ConditionalPoisson.html) a partir de una fórmula y un `DataFrame`.
* - [logit](https://www.statsmodels.org/stable/generated/statsmodels.formula.api.logit.html)(formula, data, ...)
  - Crea un [Logit](https://www.statsmodels.org/stable/generated/statsmodels.discrete.discrete_model.Logit.html) a partir de una fórmula y un `DataFrame`.
* - [mnlogit](https://www.statsmodels.org/stable/generated/statsmodels.formula.api.mnlogit.html)(formula, data, ...)
  - Crea un [MNLogit](https://www.statsmodels.org/stable/generated/statsmodels.discrete.discrete_model.MNLogit.html) a partir de una fórmula y un `DataFrame`.
* - [negativebinomial](https://www.statsmodels.org/stable/generated/statsmodels.formula.api.negativebinomial.html)(formula, data, ...)
  - Crea un [NegativeBinomial](https://www.statsmodels.org/stable/generated/statsmodels.discrete.discrete_model.NegativeBinomial.html) a partir de una fórmula y un `DataFrame`.
* - [poisson](https://www.statsmodels.org/stable/generated/statsmodels.formula.api.poisson.html)(formula, data, ...)
  - Crea un [Poisson](https://www.statsmodels.org/stable/generated/statsmodels.discrete.discrete_model.Poisson.html) a partir de una fórmula y un `DataFrame`.
* - [probit](https://www.statsmodels.org/stable/generated/statsmodels.formula.api.probit.html)(formula, data, ...)
  - Crea un [Probit](https://www.statsmodels.org/stable/generated/statsmodels.discrete.discrete_model.Probit.html) a partir de una fórmula y un `DataFrame`.
* - **Ecuaciones de Estimación Generalizadas (GEE)**
  -
* - [gee](https://www.statsmodels.org/stable/generated/statsmodels.formula.api.gee.html)(formula, groups, data, ...)
  - Crea un [GEE](https://www.statsmodels.org/stable/generated/statsmodels.genmod.generalized_estimating_equations.GEE.html) a partir de una fórmula y un `DataFrame`.
* - [nominal_gee](https://www.statsmodels.org/stable/generated/statsmodels.formula.api.nominal_gee.html)(formula, groups, data, ...)
  - Crea un [NominalGEE](https://www.statsmodels.org/stable/generated/statsmodels.genmod.generalized_estimating_equations.NominalGEE.html) a partir de una fórmula y un `DataFrame`.
* - [ordinal_gee](https://www.statsmodels.org/stable/generated/statsmodels.formula.api.ordinal_gee.html)(formula, groups, data, ...)
  - Crea un [OrdinalGEE](https://www.statsmodels.org/stable/generated/statsmodels.genmod.generalized_estimating_equations.OrdinalGEE.html) a partir de una fórmula y un `DataFrame`.
* - **Modelos Lineales Generalizados (GLM)**
  -
* - [glm](https://www.statsmodels.org/stable/generated/statsmodels.formula.api.glm.html)(formula, data, ...)
  - Crea un [GLM](https://www.statsmodels.org/stable/generated/statsmodels.genmod.generalized_linear_model.GLM.html) a partir de una fórmula y un `DataFrame`.
* - [glmgam](https://www.statsmodels.org/stable/generated/statsmodels.formula.api.glmgam.html)(formula, data, ...)
  - Crea un [GLMGam](https://www.statsmodels.org/stable/generated/statsmodels.gam.generalized_additive_model.GLMGam.html) a partir de una fórmula y un `DataFrame`.
* - **Regresión**
  -
* - [gls](https://www.statsmodels.org/stable/generated/statsmodels.formula.api.gls.html)(formula, data, ...)
  - Crea un [GLS](https://www.statsmodels.org/stable/generated/statsmodels.regression.linear_model.GLS.html) a partir de una fórmula y un `DataFrame`.
* - [glsar](https://www.statsmodels.org/stable/generated/statsmodels.formula.api.glsar.html)(formula, data, ...)
  - Crea un [GLSAR](https://www.statsmodels.org/stable/generated/statsmodels.regression.linear_model.GLSAR.html) a partir de una fórmula y un `DataFrame`.
* - [ols](https://www.statsmodels.org/stable/generated/statsmodels.formula.api.ols.html)(formula, data, ...)
  - Crea un [OLS](https://www.statsmodels.org/stable/generated/statsmodels.regression.linear_model.OLS.html) a partir de una fórmula y un `DataFrame`.
* - [wls](https://www.statsmodels.org/stable/generated/statsmodels.formula.api.wls.html)(formula, data, ...)
  - Crea un [WLS](https://www.statsmodels.org/stable/generated/statsmodels.regression.linear_model.WLS.html) a partir de una fórmula y un `DataFrame`.
* - **Otros Modelos**
  -
* - [mixedlm](https://www.statsmodels.org/stable/generated/statsmodels.formula.api.mixedlm.html)(formula, data, ...)
  - Crea un [MixedLM](https://www.statsmodels.org/stable/generated/statsmodels.regression.mixed_linear_model.MixedLM.html) a partir de una fórmula y un `DataFrame`.
* - [phreg](https://www.statsmodels.org/stable/generated/statsmodels.formula.api.phreg.html)(formula, data, ...)
  - Crea un [PHReg](https://www.statsmodels.org/stable/generated/statsmodels.duration.hazard_regression.PHReg.html) de regresión de riesgos proporcionales a partir de una fórmula y un `DataFrame`.
* - [quantreg](https://www.statsmodels.org/stable/generated/statsmodels.formula.api.quantreg.html)(formula, data, ...)
  - Crea un [QuantReg](https://www.statsmodels.org/stable/generated/statsmodels.regression.quantile_regression.QuantReg.html) a partir de una fórmula y un `DataFrame`.
* - [rlm](https://www.statsmodels.org/stable/generated/statsmodels.formula.api.rlm.html)(formula, data, ...)
  - Crea un [RLM](https://www.statsmodels.org/stable/generated/statsmodels.robust.robust_linear_model.RLM.html) a partir de una fórmula y un `DataFrame`.
```