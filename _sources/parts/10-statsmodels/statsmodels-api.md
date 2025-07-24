# API Principal

Es la interfaz principal de _statsmodels_, que proporciona acceso a una amplia gama de modelos estadísticos y herramientas de análisis. Entre las funcionalidades principales están:
- Modelos lineales (_OLS_, regresión lineal generalizada).
- Modelos de datos panel y modelos mixtos.
- Pruebas estadísticas y diagnósticos.

Es necesario importar el módulo:

```python
# Importar api
import statsmodels.api as sm

# Importar clase específica
from statsmodels.api import ClassName

# Importar función específica
from statsmodels.api import func_name
```
- _sm_ es el nombre por convención.
- _ClassName_ o _func_name_ es el nombre de la clase o función respectivamente.

:::{note}
Para más información visitar la [documentación](https://www.statsmodels.org/stable/api.html#statsmodels-api) de _statsmodels_.
:::

A continuación se presenta un resumen de cada una de las secciones:
- **Modelos Discretos y de Conteo**: Modelos estadísticos para datos discretos o de conteo, como regresión Poisson, binomial negativa y logit.
- **Ecuaciones de Estimación Generalizadas (GEE)**: Métodos para modelar datos correlacionados o agrupados, como en estudios longitudinales o clínicos.
- **Modelos Lineales Generalizados (GLM)**: Extensión de los modelos lineales para trabajar con distribuciones no normales, como binomial, Poisson o gamma.
- **Gráficos**: Herramientas para visualización de datos y diagnósticos de modelos.
- **Imputación**: Métodos para manejar datos faltantes, como la imputación múltiple o por regresión.
- **Modelos Multivariados**: Técnicas para analizar múltiples variables dependientes, como _MANOVA_ o análisis de componentes principales (_PCA_).
- **Otros Modelos**: Incluye modelos especializados, como modelos de duración (_survival analysis_) o modelos no paramétricos.
- **Regresión**: Modelos de regresión clásicos, como regresión lineal (_OLS_), regresión robusta y regresión ponderada.
- **Estadísticas**: Funciones para pruebas estadísticas, análisis descriptivo y cálculo de medidas resumidas.
- **Herramientas**: Utilidades generales para el análisis de datos, como manipulación de fórmulas, validación de modelos y generación de datos sintéticos.

<br/>

## Modelos Discretos y de Conteo

Modelos estadísticos para datos discretos o de conteo, como regresión Poisson, binomial negativa y _logit—.

:::{note}
Notar que todas son clases.
:::

```{list-table}
:header-rows: 1

* - Constructor
  - Descripción
* - [ConditionalLogit](https://www.statsmodels.org/stable/generated/statsmodels.discrete.conditional_models.ConditionalLogit.html)(endog, exog, ...)
  - Ajusta un modelo de regresión logística condicional a datos agrupados.
* - [ConditionalMNLogit](https://www.statsmodels.org/stable/generated/statsmodels.discrete.conditional_models.ConditionalMNLogit.html)(endog, exog, ...)
  - Ajusta un modelo logit multinomial condicional a los datos agrupados.
* - [ConditionalPoisson](https://www.statsmodels.org/stable/generated/statsmodels.discrete.conditional_models.ConditionalPoisson.html)(endog, exog, ...)
  - Ajusta un modelo de regresión de Poisson condicional a datos agrupados.
* - [GeneralizedPoisson](https://www.statsmodels.org/stable/generated/statsmodels.discrete.discrete_model.GeneralizedPoisson.html)(endog, exog, ...)
  - Modelo de Poisson generalizado.
* - [Logit](https://www.statsmodels.org/stable/generated/statsmodels.discrete.discrete_model.Logit.html)(endog, exog, ...)
  - Modelo logit.
* - [MNLogit](https://www.statsmodels.org/stable/generated/statsmodels.discrete.discrete_model.MNLogit.html)(endog, exog, ...)
  - Modelo logit multinomial.
* - [NegativeBinomial](https://www.statsmodels.org/stable/generated/statsmodels.discrete.discrete_model.NegativeBinomial.html)(endog, exog, ...)
  - Modelo binomial negativo.
* - [NegativeBinomialP](https://www.statsmodels.org/stable/generated/statsmodels.discrete.discrete_model.NegativeBinomialP.html)(endog, exog, ...)
  - Modelo binomial negativo generalizado (NB-P).
* - [OrderedModel](https://www.statsmodels.org/stable/generated/statsmodels.miscmodels.ordinal_model.OrderedModel.html)(endog, exog, ...)
  - Modelo ordinal basado en la distribución logística o normal.
* - [Poisson](https://www.statsmodels.org/stable/generated/statsmodels.discrete.discrete_model.Poisson.html)(endog, exog, ...)
  - Modelo de Poisson.
* - [Probit](https://www.statsmodels.org/stable/generated/statsmodels.discrete.discrete_model.Probit.html)(endog, exog, ...)
  - Modelo probit.
* - [ZeroInflatedGeneralizedPoisson](https://www.statsmodels.org/stable/generated/statsmodels.discrete.count_model.ZeroInflatedGeneralizedPoisson.html)(endog, exog)
  - Modelo de Poisson generalizado inflado cero.
* - [ZeroInflatedNegativeBinomialP](https://www.statsmodels.org/stable/generated/statsmodels.discrete.count_model.ZeroInflatedNegativeBinomialP.html)(endog, exog, ...)
  - Modelo binomial negativo generalizado inflado cero.
* - [ZeroInflatedPoisson](https://www.statsmodels.org/stable/generated/statsmodels.discrete.count_model.ZeroInflatedPoisson.html)(endog, exog, ...)
  - Modelo de Poisson inflado  Zero.
```

<br/>

## Ecuaciones de Estimación Generalizadas (GEE)

Métodos para modelar datos correlacionados o agrupados, como en estudios longitudinales o clínicos.

:::{note}
Notar que todas son clases.
:::

```{list-table}
:header-rows: 1

* - Constructor
  - Descripción
* - [GEE](https://www.statsmodels.org/stable/generated/statsmodels.genmod.generalized_estimating_equations.GEE.html)(endog, exog, groups, ...)
  - Modelo de regresión marginal utilizando ecuaciones de estimación generalizadas.
* - [NominalGEE](https://www.statsmodels.org/stable/generated/statsmodels.genmod.generalized_estimating_equations.NominalGEE.html)(endog, exog, groups, ...)
  - _Nominal Response Marginal Regression Model_ usando GEE.
* - [OrdinalGEE](https://www.statsmodels.org/stable/generated/statsmodels.genmod.generalized_estimating_equations.OrdinalGEE.html)(endog, exog, groups, ...)
  - _Ordinal Response Marginal Regression Model_ usando GEE.
```

<br/>

## Modelos Lineales Generalizados (GLM)

Extensión de los modelos lineales para trabajar con distribuciones no normales, como binomial, Poisson o gamma.

:::{note}
Notar que todas son clases.
:::

```{list-table}
:header-rows: 1

* - Constructor
  - Descripción
* - [BinomialBayesMixedGLM](https://www.statsmodels.org/stable/generated/statsmodels.genmod.bayes_mixed_glm.BinomialBayesMixedGLM.html)(endog, exog, exog_vc, ...)
  - Modelo mixto lineal generalizado con estimación bayesiana.
* - [GLM](https://www.statsmodels.org/stable/generated/statsmodels.genmod.generalized_linear_model.GLM.html)(endog, exog, ...)
  - Modelos lineales generalizados.
* - [GLMGam](https://www.statsmodels.org/stable/generated/statsmodels.gam.generalized_additive_model.GLMGam.html)(endog, ...)
  - Modelos aditivos generalizados (GAM).
* - [PoissonBayesMixedGLM](https://www.statsmodels.org/stable/generated/statsmodels.genmod.bayes_mixed_glm.PoissonBayesMixedGLM.html)(endog, exog, exog_vc, ident)
  - Modelo mixto lineal generalizado con estimación bayesiana.
```

<br/>

## Gráficos

Herramientas para visualización de datos y diagnósticos de modelos.

### Clases

Clases para visualización de datos

```{list-table}
:header-rows: 1

* - Constructor
  - Descripción
* - [ProbPlot](https://www.statsmodels.org/stable/generated/statsmodels.graphics.gofplots.ProbPlot.html)(data, ...)
  - Gráficos de probabilidad _Q-Q_ y _P-P_.
```

### Funciones

Funciones para visualización de datos y diagnósticos de modelos.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [qqline](https://www.statsmodels.org/stable/generated/statsmodels.graphics.gofplots.qqline.html)(ax, line, ...)
  - Grafica una línea de referencia para un _Qqplot_.
* - [qqplot](https://www.statsmodels.org/stable/generated/statsmodels.graphics.gofplots.qqplot.html)(data, ...)
  - Gráfico _Q-Q_ de los cuantiles de _x_ versus los cuantiles/ppf de una distribución.
* - [qqplot_2samples](https://www.statsmodels.org/stable/generated/statsmodels.graphics.gofplots.qqplot_2samples.html)(data1, data2, ...)
  - Gráfico _Q-Q_ de cuantiles de dos muestras.
```

<br/>

## Imputación

Métodos para manejar datos faltantes, como la imputación múltiple o por regresión. 

:::{note}
Notar que todas son clases.
:::

```{list-table}
:header-rows: 1

* - Constructor
  - Descripción
* - [BayesGaussMI](https://www.statsmodels.org/stable/generated/statsmodels.imputation.bayes_mi.BayesGaussMI.html)(data, ...)
  - Imputación bayesiana utilizando un modelo gaussiano.
* - [MI](https://www.statsmodels.org/stable/generated/statsmodels.imputation.bayes_mi.MI.html)(imp, model, ...)
  - _MI_ realiza una imputación múltiple utilizando un objeto imputador proporcionado.
* - [MICE](https://www.statsmodels.org/stable/generated/statsmodels.imputation.mice.MICE.html)(model_formula, model_class, data, ...)
  - Imputación múltiple con ecuaciones encadenadas.
* - [MICEData](https://www.statsmodels.org/stable/generated/statsmodels.imputation.mice.MICEData.html)(data, ...)
  - Envuelva un conjunto de datos para permitir el manejo de datos faltante con _MICE_.
```

<br/>

## Modelos Multivariados

Técnicas para analizar múltiples variables dependientes, como MANOVA o análisis de componentes principales (PCA).

:::{note}
Notar que todas son clases.
:::

```{list-table}
:header-rows: 1

* - Constructor
  - Descripción
* - [Factor](https://www.statsmodels.org/stable/generated/statsmodels.multivariate.factor.Factor.html)(...)
  - Análisis factorial.
* - [MANOVA](https://www.statsmodels.org/stable/generated/statsmodels.multivariate.manova.MANOVA.html)(endog, exog, ...)
  - Análisis de varianza multivariado.
* - [PCA](https://www.statsmodels.org/stable/generated/statsmodels.multivariate.pca.PCA.html)(data, ...)
  - Análisis de componentes principales.
```

<br/>

## Otros Modelos

Incluye modelos especializados, como modelos de duración (survival analysis) o modelos no paramétricos.

:::{note}
Notar que todas son clases.
:::

```{list-table}
:header-rows: 1

* - Constructor
  - Descripción
* - [BetaModel](https://www.statsmodels.org/stable/generated/statsmodels.othermod.betareg.BetaModel.html)(endog, exog, ...)
  - Regresión beta.
* - [MixedLM](https://www.statsmodels.org/stable/generated/statsmodels.regression.mixed_linear_model.MixedLM.html)(endog, exog, groups, ...)
  - Modelo de efectos mixtos lineales.
* - [PHReg](https://www.statsmodels.org/stable/generated/statsmodels.duration.hazard_regression.PHReg.html)(endog, exog, ...)
  - Modelo de regresión de riesgos proporcionales de Cox.
* - [QuantReg](https://www.statsmodels.org/stable/generated/statsmodels.regression.quantile_regression.QuantReg.html)(endog, exog, **kwargs)
  - Regresión cuantil.
* - [RLM](https://www.statsmodels.org/stable/generated/statsmodels.robust.robust_linear_model.RLM.html)(endog, exog, ...)
  - Modelo lineal robusto.
* - [SurvfuncRight](https://www.statsmodels.org/stable/generated/statsmodels.duration.survfunc.SurvfuncRight.html)(time, status, ...)
  - Estimación e inferencia para una función de supervivencia.
```

<br/>

## Regresión

Modelos de regresión clásicos, como regresión lineal (_OLS_), regresión robusta y regresión ponderada.

:::{note}
Notar que todas son clases.
:::

```{list-table}
:header-rows: 1

* - Constructor
  - Descripción
* - [GLS](https://www.statsmodels.org/stable/generated/statsmodels.regression.linear_model.GLS.html)(endog, exog, ...)
  - Mínimos cuadrados generalizados.
* - [GLSAR](https://www.statsmodels.org/stable/generated/statsmodels.regression.linear_model.GLSAR.html)(endog, ...)
  - Mínimos cuadrados generalizados con estructura de covarianza AR.
* - [OLS](https://www.statsmodels.org/stable/generated/statsmodels.regression.linear_model.OLS.html)(endog, ...)
  - Mínimos cuadrados ordinarios.
* - [RecursiveLS](https://www.statsmodels.org/stable/generated/statsmodels.regression.recursive_ls.RecursiveLS.html)(endog, exog, ...)
  - Mínimos cuadrados recursivos.
* - [RollingOLS](https://www.statsmodels.org/stable/generated/statsmodels.regression.rolling.RollingOLS.html)(endog, exog, ...)
  - _Rolling Ordinary Least Squares_.
* - [RollingWLS](https://www.statsmodels.org/stable/generated/statsmodels.regression.rolling.RollingWLS.html)(endog, exog, ...)
  - _Rolling Weighted Least Squares_.
* - [WLS](https://www.statsmodels.org/stable/generated/statsmodels.regression.linear_model.WLS.html)(endog, exog, ...)
  - Mínimos cuadrados ponderados.
```

<br/>

### Notas de OLS

[OLS](https://www.statsmodels.org/stable/generated/statsmodels.regression.linear_model.OLS.html): Crea una modelo de regresión por el método de mínimos cuadrados, desde dos vectores.
```python
# Sintaxis de llamada
sm.ols(endog, exog=None, missing='none', hasconst=None, **kwargs)
```
**Parámetros:**
- **endog** - `array-like 1D`: Variable dependiente (Y).
- **exog** - `array-like`: Variable(s) independiente(s) (X). La intercepción no está incluida por default y debe ser proveída por el usuario manualmente con la función `statsmodels.api.add_constant`, esto es si quieres la regresión líneal con una intercepción, entonces debes de proveer una columna constante de 1s como primer columna.
- **missing** - `Str`: Para indicar como manejar los valores perdidos:
    - _'none'_: No se revisa si hay valores perdidos.
    - _'drop'_: Cualquier observación con `NaN` se elimina.
    - _'raise'_: Se arroja un error si hay valores perdidos.
- **hasconst** - `None` o `Bool`: Indica si el RHS incluye una constante proveída por el usuario.

<br/>

#### Uso

```python

# Importación
import statsmodels.api as sm

# Añadir constante (intercepción) a las variables independientes
X = sm.add_constant(X)  # Opcional

# Inicializar y ajustar el modelo OLS
modelo_ols = sm.OLS(
    endog=y,  # Variable dependiente (y)
    exog=X,   # Variables independientes (X, con constante si es necesario)
)
resultados = modelo_ols.fit()  # Ajustar el modelo a los datos

# Resumen completo del modelo (coeficientes, p-valores, R², etc.)
print(resultados.summary())

# Obtener coeficientes del modelo
coeficientes = resultados.params
print("Coeficientes:", coeficientes)

# Obtener predicciones
y_pred = resultados.predict(X_new)  # Predicciones para nuevos datos
print("Predicciones:", y_pred)

# Obtener residuos (errores)
residuos = resultados.resid
print("Residuos:", residuos)

# Pruebas de hipótesis (ej: t-test para un coeficiente específico)
print("Valor t del intercepto:", resultados.tvalues[0])

# Atributos importantes del objeto resultados (opcional)
print("R²:", resultados.rsquared)  # Coeficiente de determinación
print("R² ajustado:", resultados.rsquared_adj)
print("Número de observaciones:", resultados.nobs)
```
- `sm.add_constant(X)`: Si la variable independiente _X_ no tiene una columna de constantes se agrega en este paso.

<br/>

#### Atributos

Atributos de la clase `OLS`. 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [df_model](https://www.statsmodels.org/stable/generated/statsmodels.regression.linear_model.OLS.df_model.html)
  - El grado de libertad del modelo.
* - [df_resid](https://www.statsmodels.org/stable/generated/statsmodels.regression.linear_model.OLS.df_resid.html)
  - El grado de libertad del residual.
* - [endog_names](https://www.statsmodels.org/stable/generated/statsmodels.regression.linear_model.OLS.endog_names.html)
  - Nombres de variables endógenas.
* - [exog_names](https://www.statsmodels.org/stable/generated/statsmodels.regression.linear_model.OLS.exog_names.html)
  - Nombres de variables exógenas.
```

#### Métodos

Métodos de la clase `OLS`. 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - [fit](https://www.statsmodels.org/stable/generated/statsmodels.regression.linear_model.OLS.fit.html)(...)
  - Ajuste completo del modelo.
* - [fit_regularized](https://www.statsmodels.org/stable/generated/statsmodels.regression.linear_model.OLS.fit_regularized.html)(...)
  - Retorna un ajuste regularizado a un modelo de regresión lineal.
* - [from_formula](https://www.statsmodels.org/stable/generated/statsmodels.regression.linear_model.OLS.from_formula.html)(formula, data, ...)
  - Crea un modelo a partir de una fórmula y `DataFrame`.
* - [get_distribution](https://www.statsmodels.org/stable/generated/statsmodels.regression.linear_model.OLS.get_distribution.html)(params, scale, ...)
  - Construye un generador de números aleatorios para la distribución predictiva.
* - [hessian](https://www.statsmodels.org/stable/generated/statsmodels.regression.linear_model.OLS.hessian.html)(params, ...)
  - Evalúa la función _Hessiana_ en un punto dado.
* - [hessian_factor](https://www.statsmodels.org/stable/generated/statsmodels.regression.linear_model.OLS.hessian_factor.html)(params, ...)
  - Calcula los pesos para el Hessiano.
* - [information](https://www.statsmodels.org/stable/generated/statsmodels.regression.linear_model.OLS.information.html)(params)
  - Matriz de información de _Fisher_ del modelo.
* - [initialize](https://www.statsmodels.org/stable/generated/statsmodels.regression.linear_model.OLS.initialize.html)()
  - Inicializa los componentes del modelo.
* - [loglike](https://www.statsmodels.org/stable/generated/statsmodels.regression.linear_model.OLS.loglike.html)(params, ...)
  - La función de probabilidad para el modelo _OLS_.
* - [predict](https://www.statsmodels.org/stable/generated/statsmodels.regression.linear_model.OLS.predict.html)(params, ...)
  - Retorna valores linealmente predichos de una matriz.
* - [score](https://www.statsmodels.org/stable/generated/statsmodels.regression.linear_model.OLS.score.html)(params, ...)
  - Evalúa la función de puntaje en un punto dado.
* - [whiten](https://www.statsmodels.org/stable/generated/statsmodels.regression.linear_model.OLS.whiten.html)(x)
  - El modelo _OLS_ Whitener no hace nada.
```

<br/>

## Estadísticas

Funciones para pruebas estadísticas, análisis descriptivo y cálculo de medidas resumidas.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [Description](https://www.statsmodels.org/stable/generated/statsmodels.stats.descriptivestats.Description.html)(data, ...)
  - (Clase) Estadísticas descriptivas extendidas para datos.
* - [describe](https://www.statsmodels.org/stable/generated/statsmodels.stats.descriptivestats.describe.html)(data, ...)
  - Estadísticas descriptivas extendidas para datos.
```

<br/>

## Herramientas

Utilidades generales para el análisis de datos, como manipulación de fórmulas, validación de modelos y generación de datos sintéticos.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [add_constant](https://www.statsmodels.org/stable/generated/statsmodels.tools.tools.add_constant.html)(data, ...)
  - Agrega una columna de unos a una matriz.
* - [load_pickle](https://www.statsmodels.org/stable/generated/statsmodels.iolib.smpickle.load_pickle.html)(fname)
  - Carga un objeto previamente guardado.
* - [show_versions](https://www.statsmodels.org/stable/generated/statsmodels.tools.print_version.show_versions.html)(...)
  - Enlista las versiones de _statsmodels_ y cualquier dependencia instalada.
* - [test](https://www.statsmodels.org/stable/dev/generated/statsmodels.__init__.test.html)(...)
  - Ejecuta la suite de prueba.
* - [webdoc](https://www.statsmodels.org/stable/generated/statsmodels.tools.web.webdoc.html)(...)
  - Abre un navegador y muestra documentación en línea.
```

<br/>

