# Stats

Es un módulo de con distribuciones de probabilidad, pruebas de hipótesis, estimaciones de densidades de kernel, funciones de correlación, medidas de tendencia central y desviación, estaísticas descriptivas, entre otras. Para usar este submódulo es necesario importarlo:

```python
# Importar linalg
from scipy import stats

# Importar función específica
from scipy.stats import function_name
```
- _function_name_ es el nombre de la función que se desea importar.

:::{note}
Para más información visitar la [documentación](https://docs.scipy.org/doc/scipy/reference/stats.html) de _scipy_.
:::

A continuación se presenta un resumen de cada sección:
- **Distribuciones de probabilidad**: Funciones generales para trabajar con distribuciones de probabilidad, tanto continuas como discretas.
- **Distribuciones continuas**: Funciones para trabajar con distribuciones de probabilidad continuas, como la normal, exponencial y t de Student.
- **Distribuciones discretas**: Funciones para trabajar con distribuciones de probabilidad discretas, como la binomial, Poisson y geométrica.
- **Distribuciones multivariadas**: Funciones para trabajar con distribuciones de probabilidad multivariadas, como la normal multivariada.
- **Estadísticas descriptivas**: Funciones para calcular medidas resumidas, como media, mediana, varianza y percentiles.
- **Estadísticas de frecuencia**: Métodos para analizar frecuencias y tablas de contingencia, como pruebas de chi-cuadrado.
- **Métodos de remuestreo y Monte Carlo**: Técnicas para estimar distribuciones y estadísticas mediante remuestreo y simulación.
- **Pruebas de asociación y correlación**: Métodos para evaluar la relación entre variables, como coeficientes de correlación y pruebas de independencia.
- **Pruebas de muestras independientes**: Las pruebas de muestras independientes se utilizan normalmente para evaluar si se extrajeron varias muestras de forma independiente de la misma distribución o de distribuciones diferentes con una propiedad compartida.
- **Pruebas de múltiples hipótesis y meta-análisis**: Técnicas para ajustar y combinar resultados de múltiples pruebas.
- **Pruebas de una muestra y en pares**: Las pruebas de una muestra se utilizan normalmente para evaluar si una sola muestra se extrajo de una distribución específica o de una distribución con propiedades específicas.
- **Variables aleatorias**: Herramientas para crear y manipular variables aleatorias a partir de distribuciones.

## Distribuciones de probabilidad

Funciones generales para trabajar con distribuciones de probabilidad, tanto continuas como discretas.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [rv_continuous](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.rv_continuous.html)([momtype, a, b, xtol, ...])
  - Una clase de variable aleatoria continua genérica destinada a subclasificar.
* - [rv_discrete](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.rv_discrete.html)([a, b, name, badvalue, ...])
  - Una clase variable aleatoria discreta genérica destinada a subclasificar.
* - [rv_histogram](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.rv_histogram.html)(histogram, *args, ...)
  - Genera una distribución dada por un histograma.
```

### Clase _rv_continuous_

Una clase de variable aleatoria continua genérica destinada a subclasificar.

(rv_continuous-methods)=
#### Métodos

Métodos de la clase `rv_continuous`. 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - **Principales métodos**
  -
* - [cdf](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.rv_continuous.cdf.html)(x, *args, **kwds)
  - Función de distribución acumulativa.
* - [isf](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.rv_continuous.isf.html)(q, *args, **kwds)
  - Función de supervivencia inversa (inversa de `sf`).
* - [mean](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.rv_continuous.mean.html)(*args, **kwds)
  - Media de la distribución.
* - [median](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.rv_continuous.median.html)(*args, **kwds)
  - Mediana de la distribución.
* - [moment](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.rv_continuous.moment.html)(order, *args, **kwds)
  - Momento no central de distribución del orden especificado.
* - [pdf](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.rv_continuous.pdf.html)(x, *args, **kwds)
  - Función de densidad de probabilidad.
* - [ppf](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.rv_continuous.ppf.html)(q, *args, **kwds)
  - Inversa de `cdf`.
* - [rvs](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.rv_continuous.rvs.html)(*args, **kwds)
  - Valores aleatorios de la variable aleatoria.
* - [sf](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.rv_continuous.sf.html)(x, *args, **kwds)
  - Función de supervivencia (1 - `cdf` ).
* - [stats](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.rv_continuous.stats.html)(*args, **kwds)
  - Estadísticas descriptivas.
* - [std](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.rv_continuous.std.html)(*args, **kwds)
  - Desviación estándar de la distribución.
* - [support](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.rv_continuous.support.html)(*args, **kwargs)
  - Soporte de la distribución.
* - [var](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.rv_continuous.var.html)(*args, **kwds)
  - Varianza de la distribución.
* - **Otros métodos**
  - 
* - [\_\_call__](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.rv_continuous.__call__.html)(*args, **kwds)
  - Congela la distribución para los argumentos dados.
* - [entropy](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.rv_continuous.entropy.html)(*args, **kwds)
  - Entropía diferencial.
* - [expect](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.rv_continuous.expect.html)([func, args, loc, scale, lb, ub, ...])
  - Calcula el valor esperado de una función con respecto a la distribución por integración numérica.
* - [fit](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.rv_continuous.fit.html)(data, *args, **kwds)
  - Retorna las estimaciones de los parámetros de forma (si corresponde), la ubicación y los parámetros de escala de los datos.
* - [fit_loc_scale](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.rv_continuous.fit_loc_scale.html)(data, *args)
  - Estima los parámetros _loc_ y _scale_ de los datos utilizando los momentos 1 y 2.
* - [interval](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.rv_continuous.interval.html)(confidence, *args, **kwds)
  - Intervalo de confianza con áreas iguales alrededor de la mediana.
* - [logcdf](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.rv_continuous.logcdf.html)(x, *args, **kwds)
  - Logaritmo de la función de distribución acumulada.
* - [logpdf](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.rv_continuous.logpdf.html)(x, *args, **kwds)
  - Logaritmo de la función de densidad de probabilidad.
* - [logsf](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.rv_continuous.logsf.html)(x, *args, **kwds)
  - Logaritmo de la función de supervivencia.
* - [nnlf](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.rv_continuous.nnlf.html)(theta, x)
  - Función negativa _loglikelihood_.
```


### Clase _rv_discrete_

Una clase variable aleatoria discreta genérica destinada a subclasificar.

(rv_discrete-methods)=
#### Métodos

Métodos de la clase `rv_discrete`. 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - **Principales métodos**
  -
* - [cdf](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.rv_discrete.cdf.html)(k, *args, **kwds)
  - Función de distribución acumulativa.
* - [isf](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.rv_discrete.isf.html)(q, *args, **kwds)
  - Función de supervivencia inversa (inversa de `sf`).
* - [mean](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.rv_discrete.mean.html)(*args, **kwds)
  - Media de la distribución.
* - [median](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.rv_discrete.median.html)(*args, **kwds)
  - Mediana de la distribución.
* - [moment](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.rv_discrete.moment.html)(order, *args, **kwds)
  - Momento no central de distribución del orden especificado.
* - [pmf](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.rv_discrete.pmf.html)(k, *args, **kwds)
  - Función de masa de probabilidad.
* - [ppf](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.rv_discrete.ppf.html)(q, *args, **kwds)
  - Inversa de `cdf`.
* - [rvs](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.rv_discrete.rvs.html)(*args, **kwargs)
  - Valores aleatorios de la variable aleatoria.
* - [sf](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.rv_discrete.sf.html)(k, *args, **kwds)
  - Función de supervivencia (1 - `cdf`).
* - [stats](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.rv_discrete.stats.html)(*args, **kwds)
  - Estadísticas descriptivas.
* - [std](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.rv_discrete.std.html)(*args, **kwds)
  - Desviación estándar de la distribución.
* - [support](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.rv_discrete.support.html)(*args, **kwargs)
  - Soporte de la distribución.
* - [var](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.rv_discrete.var.html)(*args, **kwds)
  - Varianza de la distribución.
* - **Otros métodos**
  - 
* - [\_\_call__](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.rv_discrete.__call__.html)(*args, **kwds)
  - Congela la distribución para los argumentos dados.
* - [entropy](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.rv_discrete.entropy.html)(*args, **kwds)
  - Entropía diferencial.
* - [expect](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.rv_discrete.expect.html)([func, args, loc, lb, ub, ...])
  - Calcula el valor esperado de una función con respecto a la distribución por suma numérica.
* - [interval](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.rv_discrete.interval.html)(confidence, *args, **kwds)
  - Intervalo de confianza con áreas iguales alrededor de la mediana.
* - [logcdf](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.rv_discrete.logcdf.html)(k, *args, **kwds)
  - Logaritmo de la función de distribución acumulada.
* - [logpmf](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.rv_discrete.logpmf.html)(k, *args, **kwds)
  - Logaritmo de la función de masa de probabilidad.
* - [logsf](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.rv_discrete.logsf.html)(k, *args, **kwds)
  - Logaritmo de la función de supervivencia.
```

<br/>

## Distribuciones continuas

Distribuciones de probabilidad continuas, como la normal, exponencial y t de Student. Son instancias de `rv_continuous`.

:::{caution}
Revisar los {ref}`rv_continuous-methods` de `rv_continuous` o dirigirse a la documentación de cada distribución.
:::

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - **Principales distribuciones**
  - 
* - [beta](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.beta.html)
  - Una variable aleatoria continua _beta_.
* - [cauchy](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.cauchy.html)
  - Una variable aleatoria continua de _Cauchy_.
* - [chi](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.chi.html)
  - Una variable aleatoria continua _chi_.
* - [chi2](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.chi2.html)
  - Una variable aleatoria continua _chi cuadrado_.
* - [erlang](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.erlang.html)
  - Una variable aleatoria continua de _Erlang_.
* - [expon](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.expon.html)
  - Una variable aleatoria continua exponencial.
* - [f](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.f.html)
  - Una variable aleatoria continua F.
* - [gamma](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.gamma.html)
  - Una variable aleatoria continua _gamma_.
* - [logistic](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.logistic.html)
  - Una variable aleatoria continua _logística_ (o SECH-cuadrado).
* - [lognorm](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.lognorm.html)
  - Una variable aleatoria continua lognormal.
* - [norm](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.norm.html)
  - Una variable aleatoria continua _normal_.
* - [norminvgauss](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.norminvgauss.html)
  - Una variable aleatoria continua _gaussiana inversa normal_.
* - [pareto](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.pareto.html)
  - Una variable aleatoria continua de _Pareto_.
* - [rayleigh](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.rayleigh.html)
  - Una variable aleatoria continua de Rayleigh.
* - [t](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.t.html)
  - La variable aleatoria continua de _Student's t_.
* - [uniform](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.uniform.html)
  - Una variable aleatoria continua uniforme.
* - **Otras distribuciones**
  - 
* - [alpha](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.alpha.html)
  - Una variable aleatoria continua _alpha_.
* - [anglit](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.anglit.html)
  - Una variable aleatoria continua _anglit_.
* - [arcsine](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.arcsine.html)
  - Una variable aleatoria continua _arcsine_.
* - [argus](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.argus.html)
  - Distribución _argus_.
* - [betaprime](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.betaprime.html)
  - Una variable aleatoria continua _beta prime_.
* - [bradford](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.bradford.html)
  - Una variable aleatoria continua de _Bradford_.
* - [burr](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.burr.html)
  - Una variable aleatoria continua de _Burr_ (tipo III).
* - [burr12](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.burr12.html)
  - Una variable aleatoria continua de _Burr_ (tipo XII).
* - [cosine](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.cosine.html)
  - Una variable aleatoria continua de _coseno_.
* - [crystalball](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.crystalball.html)
  - Distribución de _cristalball_.
* - [dgamma](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.dgamma.html)
  - Una variable aleatoria continua _gamma doble_.
* - [dpareto_lognorm](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.dpareto_lognorm.html)
  - Una variable aleatoria continua doble de _Pareto_ lognormal.
* - [dweibull](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.dweibull.html)
  - Una variable aleatoria continua doble de _Weibull_.
* - [exponnorm](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.exponnorm.html)
  - Una variable aleatoria continua exponencialmente modificada normal.
* - [exponpow](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.exponpow.html)
  - Una variable aleatoria continua de potencia exponencial.
* - [exponweib](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.exponweib.html)
  - Una variable aleatoria continua de Weibull exponenciada.
* - [fatiguelife](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.fatiguelife.html)
  - Una variable aleatoria continua de _fatigue-life_ (Birnbaum-Saunders).
* - [fisk](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.fisk.html)
  - Una variable aleatoria continua _Fisk_.
* - [foldcauchy](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.foldcauchy.html)
  - Una variable aleatoria continua de Cauchy plegada.
* - [foldnorm](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.foldnorm.html)
  - Una variable aleatoria continua normal plegada.
* - [gausshyper](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.gausshyper.html)
  - Una variable aleatoria continua _hipergeométrica Gauss_.
* - [genexpon](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.genexpon.html)
  - Una variable aleatoria continua exponencial generalizada.
* - [genextreme](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.genextreme.html)
  - Una variable aleatoria continua de valor extremo generalizado.
* - [gengamma](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.gengamma.html)
  - Una variable aleatoria continua gamma generalizada.
* - [genhalflogistic](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.genhalflogistic.html)
  - Una variable aleatoria continua _half-logistic_ generalizada.
* - [genhyperbolic](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.genhyperbolic.html)
  - Una variable aleatoria continua hiperbólica generalizada.
* - [geninvgauss](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.geninvgauss.html)
  - Una variable aleatoria continua gaussiana inversa generalizada.
* - [genlogistic](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.genlogistic.html)
  - Una variable aleatoria continua de logística generalizada.
* - [gennorm](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.gennorm.html)
  - Una variable aleatoria continua normal generalizada.
* - [genpareto](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.genpareto.html)
  - Una variable aleatoria continua de Pareto generalizada.
* - [gibrat](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.gibrat.html)
  - Una variable aleatoria continua _gibrat_.
* - [gompertz](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.gompertz.html)
  - Una variable aleatoria continua de _Gompertz_ (o _Gumbel truncado_).
* - [gumbel_l](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.gumbel_l.html)
  - Una variable aleatoria continua de _Gumbel_ sesgada a la izquierda.
* - [gumbel_r](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.gumbel_r.html)
  - Una variable aleatoria continua de _Gumbel_ sesgada a la derecha.
* - [halfcauchy](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.halfcauchy.html)
  - Una variable aleatoria continua de _Half-Cauchy_.
* - [halfgennorm](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.halfgennorm.html)
  - La mitad superior de una variable aleatoria continua normal generalizada.
* - [halflogistic](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.halflogistic.html)
  - Una variable aleatoria continua _half-logistic_.
* - [halfnorm](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.halfnorm.html)
  - Una variable aleatoria continua _half-normal_.
* - [hypsecant](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.hypsecant.html)
  - Una variable aleatoria continua secante hiperbólica.
* - [invgamma](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.invgamma.html)
  - Una variable aleatoria continua _gamma_ invertida.
* - [invgauss](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.invgauss.html)
  - Una variable aleatoria continua _gaussiana_ invertida.
* - [invweibull](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.invweibull.html)
  - Una variable aleatoria continua de _Weibull_ invertida.
* - [irwinhall](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.irwinhall.html)
  - Una variable aleatoria continua _Irwin-Hall_ (suma uniforme).
* - [jf_skew_t](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.jf_skew_t.html)
  - Distribución _Jones y Faddy skew-t_.
* - [johnsonsb](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.johnsonsb.html)
  - Una variable aleatoria continua de _Johnson SB_.
* - [johnsonsu](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.johnsonsu.html)
  - Una variable aleatoria continua _Johnson Su_.
* - [kappa3](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.kappa3.html)
  - Distribución _Kappa_ de 3 parámetros.
* - [kappa4](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.kappa4.html)
  - Distribución _Kappa_ de 4 parámetros.
* - [ksone](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ksone.html)
  - Distribución estadística de prueba unilateral de _Kolmogorov-Smirnov_.
* - [kstwo](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.kstwo.html)
  - Distribución estadística de prueba de dos lados de _Kolmogorov-Smirnov_.
* - [kstwobign](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.kstwobign.html)
  - Distribución limitante de la estadística de prueba de dos lados de _Kolmogorov-Smirnov_ escalado.
* - [landau](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.landau.html)
  - Una variable aleatoria continua de _Landau_.
* - [laplace](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.laplace.html)
  - Una variable aleatoria continua de _Laplace_.
* - [laplace_asymmetric](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.laplace_asymmetric.html)
  - Una variable aleatoria continua asimétrica de _Laplace_.
* - [levy](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.levy.html)
  - Una variable aleatoria continua de _Levy_.
* - [levy_l](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.levy_l.html)
  - Una variable aleatoria continua de _Levy_ sesgada a la izquierda.
* - [levy_stable](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.levy_stable.html)
  - Una variable aleatoria continua estable de _Levy_.
* - [loggamma](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.loggamma.html)
  - Una variable aleatoria continua _gamma log_.
* - [loglaplace](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.loglaplace.html)
  - Una variable aleatoria continua _log-Laplace_.
* - [loguniform](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.loguniform.html)
  - Una variable aleatoria continua _loguniform_ o recíproca.
* - [lomax](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.lomax.html)
  - Una variable aleatoria continua _Lomax_ (Pareto del segundo tipo).
* - [maxwell](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.maxwell.html)
  - Una variable aleatoria continua de _Maxwell_.
* - [mielke](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.mielke.html)
  - Una variable aleatoria continua de _Mielke Beta-Kappa/Dagum_.
* - [moyal](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.moyal.html)
  - Una variable aleatoria continua _Moyal_.
* - [nakagami](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.nakagami.html)
  - Una variable aleatoria continua de _Nakagami_.
* - [ncf](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ncf.html)
  - Una variable aleatoria continua no central de distribución F.
* - [nct](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.nct.html)
  - Una variable aleatoria continua _Student's t_ no central.
* - [ncx2](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ncx2.html)
  - Una variable aleatoria continua de _chi cuadrado_ no central.
* - [pearson3](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.pearson3.html)
  - Una variable aleatoria continua de _Pearson_ tipo III.
* - [powerlaw](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.powerlaw.html)
  - Una variable aleatoria continua de la función de potencia.
* - [powerlognorm](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.powerlognorm.html)
  - Una variable aleatoria continua normal de potencia _log-normal_.
* - [powernorm](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.powernorm.html)
  - Una variable aleatoria continua de potencia _normal_.
* - [rdist](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.rdist.html)
  - Una variable aleatoria continua distribuida-R (beta simétrica).
* - [recipinvgauss](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.recipinvgauss.html)
  - Una variable aleatoria continua _gaussiana_ inversa recíproca.
* - [rel_breitwigner](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.rel_breitwigner.html)
  - Una variable aleatoria relativista de _Breit-Wigner_.
* - [rice](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.rice.html)
  - Una variable aleatoria continua de Rice.
* - [semicircular](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.semicircular.html)
  - Una variable aleatoria continua _semicircular_.
* - [skewcauchy](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.skewcauchy.html)
  - Una variable aleatoria de Cauchy sesgada.
* - [skewnorm](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.skewnorm.html)
  - Una variable aleatoria _normal_ sesgada.
* - [studentized_range](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.studentized_range.html)
  - Una variable aleatoria continua de rango _studentized_.
* - [trapezoid](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.trapezoid.html)
  - Una variable aleatoria continua _trapezoidal_.
* - [triang](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.triang.html)
  - Una variable aleatoria continua _triangular_.
* - [truncexpon](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.truncexpon.html)
  - Una variable aleatoria continua _exponencial_ truncada.
* - [truncnorm](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.truncnorm.html)
  - Una variable aleatoria continua _normal_ truncada.
* - [truncpareto](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.truncpareto.html)
  - Una variable aleatoria continua de _Pareto_ truncada superior.
* - [truncweibull_min](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.truncweibull_min.html)
  - Una variable aleatoria mínima continua de _Weibull_ doblemente truncada.
* - [tukeylambda](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.tukeylambda.html)
  - Una variable aleatoria continua de _Tukey-Lamdba_.
* - [vonmises](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.vonmises.html)
  - Una variable aleatoria continua de _Von Mises_.
* - [vonmises_line](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.vonmises_line.html)
  - Una variable aleatoria continua de _Von Mises_.
* - [wald](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.wald.html)
  - Una variable aleatoria continua _Wald_.
* - [weibull_max](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.weibull_max.html)
  - Una variable aleatoria continua de _Weibull maximum_.
* - [weibull_min](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.weibull_min.html)
  - Una variable aleatoria continua de _Weibull minimum.
* - [wrapcauchy](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.wrapcauchy.html)
  - Una variable aleatoria continua de _Cauchy_ envuelta.
```

<br/>

## Distribuciones discretas

Funciones para trabajar con distribuciones de probabilidad discretas, como la binomial, Poisson y geométrica. Son instancias de `rv_discrete`.

:::{caution}
Revisar los {ref}`rv_discrete-methods` de `rv_discrete` o dirigirse a la documentación de cada distribución.
:::

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - **Principales distribuciones**
  - 
* - [bernoulli](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.bernoulli.html)
  - Una variable aleatoria discreta de _Bernoulli_.
* - [binom](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.binom.html)
  - Una variable aleatoria discreta _binomial_.
* - [geom](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.geom.html)
  - Una variable aleatoria discreta _geométrica_.
* - [hypergeom](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.hypergeom.html)
  - Una variable aleatoria discreta _hipergeométrica_.
* - [nbinom](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.nbinom.html)
  - Una variable aleatoria discreta _binomial negativa_.
* - [poisson](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.poisson.html)
  - Una variable aleatoria discreta de _Poisson_.
* - [randint](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.randint.html)
  - Una variable aleatoria discreta _uniforme_.
* - **Otras distribuciones**
  - 
* - [betabinom](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.betabinom.html)
  - Una variable aleatoria discreta _beta-binomial_.
* - [betanbinom](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.betanbinom.html)
  - Una variable aleatoria discreta _binomial beta-negativa_.
* - [boltzmann](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.boltzmann.html)
  - Una variable aleatoria _Boltzmann_ (exponencial discreta truncada).
* - [dlaplace](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.dlaplace.html)
  - Una variable aleatoria discreta _Laplaciana_.
* - [logser](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.logser.html)
  - Una variable aleatoria discreta _logarítmica_ (_Log-Series, Series_).
* - [nchypergeom_fisher](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.nchypergeom_fisher.html)
  - La variable aleatoria discreta hipergeométrica no central de _Fisher_.
* - [nchypergeom_wallenius](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.nchypergeom_wallenius.html)
  - Una variable aleatoria discreta hipergeométrica no central de _Wallenius_.
* - [nhypergeom](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.nhypergeom.html)
  - Una variable aleatoria discreta _hipergeométrica_ negativa.
* - [planck](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.planck.html)
  - Una variable aleatoria exponencial discreta de _Planck_.
* - [poisson_binom](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.poisson_binom.html)
  - Una variable aleatoria discreta binomial de _Poisson_.
* - [skellam](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.skellam.html)
  - Una variable aleatoria discreta _skellam_.
* - [yulesimon](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.yulesimon.html)
  - Una variable aleatoria discreta _Yule-Simon_.
* - [zipf](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.zipf.html)
  - Una variable aleatoria discreta _Zipf_ (Zeta).
* - [zipfian](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.zipfian.html)
  - Una variable aleatoria discreta Zipfian.
```

<br/>

## Distribuciones multivariadas

Funciones para trabajar con distribuciones de probabilidad multivariadas, como la normal multivariada.

:::{caution}
Para ver los métodos de cada distribución dirigirse a la documentación de cada distribución.
:::

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - **Principales distribuciones**
  - 
* - [multinomial](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.multinomial.html)
  - Una variable aleatoria _multinomial_.
* - [multivariate_hypergeom](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.multivariate_hypergeom.html)
  - Una variable aleatoria _hipergeométrica_ multivariada.
* - [multivariate_normal](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.multivariate_normal.html)
  - Una variable aleatoria _normal_ multivariada.
* - [multivariate_t](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.multivariate_t.html)
  - Una variable aleatoria distribuida _T_ multivariada.
* - **Otras distribuciones**
  - 
* - [dirichlet](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.dirichlet.html)
  - Una variable aleatoria de _Dirichlet_.
* - [dirichlet_multinomial](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.dirichlet_multinomial.html)
  - Una variable aleatoria multinomial de _Dirichlet_.
* - [invwishart](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.invwishart.html)
  - Una variable aleatoria inversa de _Wishart_.
* - [matrix_normal](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.matrix_normal.html)
  - Una variable aleatoria de matriz _normal_.
* - [normal_inverse_gamma](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.normal_inverse_gamma.html)
  - Distribución _normal-inversa-gamma_.
* - [ortho_group](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ortho_group.html)
  - Una variable aleatoria de matriz ortogonal _(O(N))_.
* - [random_correlation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.random_correlation.html)
  - Una matriz de correlación aleatoria.
* - [random_table](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.random_table.html)
  - Tablas de contingencia de muestras independientes con sumas marginales fijas.
* - [special_ortho_group](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.special_ortho_group.html)
  - Una variable aleatoria de matriz ortogonal especial _(SO(n))_.
* - [uniform_direction](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.uniform_direction.html)
  - Una dirección uniforme con valor vectorial.
* - [unitary_group](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.unitary_group.html)
  - Una variable aleatoria de matriz _U(N)_.
* - [vonmises_fisher](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.vonmises_fisher.html)
  - Una variable _von Mises-Fisher_.
* - [wishart](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.wishart.html)
  - Una variable aleatoria de _Wishart_.
```

<br/>

## Estadísticas descriptivas

Funciones para calcular medidas resumidas, como media, mediana, varianza y percentiles.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [bayes_mvs](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.bayes_mvs.html)(data, ...)
  - Intervalos de confianza bayesianos para la media, varianza y desviación estándar.
* - [describe](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.describe.html)(a, ...)
  - Calcula varias estadísticas descriptivas.
* - [differential_entropy](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.differential_entropy.html)(values, ...)
  - Dada una muestra de una distribución, estime la entropía diferencial.
* - [entropy](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.entropy.html)(pk, ...)
  - Calcula la entropía de Shannon de la distribución.
* - [expectile](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.expectile.html)(a, ...)
  - Calcula el _expectile_ en el nivel especificado.
* - [find_repeats](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.find_repeats.html)(arr)
  - Encuentra repeticiones y recuentos de repeticiones.
* - [gmean](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.gmean.html)(a, ...)
  - Calcula la media geométrica ponderada a lo largo del eje especificado.
* - [gstd](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.gstd.html)(a, ...)
  - Calcula la desviación estándar geométrica de una matriz.
* - [hmean](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.hmean.html)(a, ...)
  - Calcula la media armónica ponderada a lo largo del eje especificado.
* - [iqr](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.iqr.html)(x, ...)
  - Calcula el rango intercuartil de los datos a lo largo del eje especificado.
* - [kstat](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.kstat.html)(data, ...)
  - Retorna el i-ésimo k-estadístico (`1<=n<=4`).
* - [kstatvar](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.kstatvar.html)(data, ...)
  - Retorna un estimador no sesgado de la varianza del k-estadístico.
* - [kurtosis](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.kurtosis.html)(a, ...)
  - Calcula la curtosis (Fisher o Pearson) de un conjunto de datos.
* - [lmoment](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.lmoment.html)(sample, ...)
  - Calcula los momentos _L_ de una muestra a partir de una distribución continua.
* - [median_abs_deviation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.median_abs_deviation.html)(x, ...)
  - Calcula la desviación absoluta mediana de los datos a lo largo del eje dado.
* - [mode](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.mode.html)(a, ...)
  - Retorna una matriz del valor modal (más común) en el arreglo dado.
* - [moment](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.moment.html)(a, ...)
  - Calcula el enésimo momento alrededor de la media para una muestra.
* - [mvsdist](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.mvsdist.html)(data)
  - Distribuciones 'congeladas' para media, varianza y desviación estándar de datos.
* - [pmean](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.pmean.html)(a, p, ...)
  - Calcula la media de potencia ponderada a lo largo del eje especificado.
* - [rankdata](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.rankdata.html)(a, ...)
  - Asigna ranks a los datos, tratando con empates adecuadamente.
* - [sem](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.sem.html)(a, ...)
  - Calcula el error estándar de la media.
* - [skew](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.skew.html)(a, ...)
  - Calcula la asimetría de la muestra de un conjunto de datos.
* - [tiecorrect](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.tiecorrect.html)(rankvals)
  - Factor de corrección de empate para las pruebas de _Mann-Whitney U_ y _Kruskal-Wallis H_.
* - [tmax](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.tmax.html)(a, ...)
  - Calcula el máximo recortado.
* - [tmean](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.tmean.html)(a, ...)
  - Calcula la media recortada.
* - [tmin](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.tmin.html)(a, ...)
  - Calcula el mínimo recortado.
* - [trim_mean](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.trim_mean.html)(a, proportiontocut, ...)
  - Media de la matriz después de recortar una fracción especificada de valores extremos.
* - [tsem](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.tsem.html)(a, ...)
  - Calcula el error estándar recortado de la media.
* - [tstd](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.tstd.html)(a, ...)
  - Calcula la desviación estándar de la muestra recortada.
* - [tvar](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.tvar.html)(a, ...)
  - Calcula la varianza recortada.
* - [variation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.variation.html)(a, ...)
  - Calcula el coeficiente de variación.
```

<br/>

## Estadísticas de frecuencia

 Métodos para analizar frecuencias y tablas de contingencia.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [cumfreq](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.cumfreq.html)(a, ...)
  - Retorna un histograma de frecuencia acumulada, utilizando la función de histograma.
* - [percentileofscore](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.percentileofscore.html)(a, score, ...)
  - Calcula el rank de percentil de una puntuación en relación con un `list` de puntajes.
* - [relfreq](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.relfreq.html)(a, ...)
  - Retorna un histograma de frecuencia relativa, utilizando la función de histograma.
* - [scoreatpercentile](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.scoreatpercentile.html)(a, per, ...)
  - Calcula la puntuación en un percentil dado de la secuencia de entrada.
```

<br/>

## Métodos de remuestreo y Monte Carlo

Técnicas para estimar distribuciones y estadísticas mediante remuestreo y simulación.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [bootstrap](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.bootstrap.html)(data, statistic, ...)
  - Calcula un intervalo de confianza de _bootstrap_ bilateral de una estadística.
* - [monte_carlo_test](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.monte_carlo_test.html)(data, rvs, statistic, ...)
  - Realiza una prueba de hipótesis de _Monte Carlo_.
* - [permutation_test](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.permutation_test.html)(data, statistic, ...)
  - Realiza una prueba de permutación de una estadística dada sobre datos proporcionados.
* - [power](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.power.html)(test, rvs, n_observations, ...)
  - Simula la potencia de una prueba de hipótesis bajo una hipótesis alternativa.
```

<br/>

## Pruebas de asociación, correlación y regresión

Métodos para evaluar la relación entre variables, como coeficientes de correlación y pruebas de independencia. Algunas de estas funciones trabajan con muestras en forma de tablas de contingencia.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [barnard_exact](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.barnard_exact.html)(table, ...)
  - Prueba exacta de _Barnard_ en una tabla de contingencia 2x2.
* - [boschloo_exact](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.boschloo_exact.html)(table, ...)
  - Prueba exacta de _Boschloo_ en una tabla de contingencia 2x2.
* - [chatterjeexi](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.chatterjeexi.html)(x, y, ...)
  - Calcula la correlación _xi_ y realiza una prueba de independencia.
* - [chi2_contingency](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.chi2_contingency.html)(observed, ...)
  - Prueba de independencia de variable _Chi-square_ en una tabla de contingencia.
* - [fisher_exact](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.fisher_exact.html)(table, ...)
  - Prueba exacta de _Fisher_ en una tabla de contingencia.
* - [kendalltau](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.kendalltau.html)(x, y, ...)
  - Calcula la tau de Kendall, una medida de correlación para datos ordinales.
* - [linregress](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.linregress.html)(x, ...)
  - Calcula una regresión lineal de mínimos cuadrados para dos conjuntos de mediciones.
* - [multiscale_graphcorr](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.multiscale_graphcorr.html)(x, y, ...)
  - Calcula la estadística de prueba de correlación de gráficos multiescala (MGC).
* - [page_trend_test](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.page_trend_test.html)(data, ...)
  - Realiza la prueba de Page, una medida de tendencia en las observaciones entre tratamientos.
* - [pearsonr](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.pearsonr.html)(x, y, ...)
  - El coeficiente de correlación de Pearson y el p-valor para probar la no correlación.
* - [pointbiserialr](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.pointbiserialr.html)(x, y)
  - Calcula un coeficiente de correlación biserial puntual y su p-valor.
* - [siegelslopes](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.siegelslopes.html)(y, ...)
  - Calcula el estimador Siegel para un conjunto de puntos (x, y).
* - [somersd](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.somersd.html)(x, ...)
  - Calcula la _D_ de Somers, una medida asimétrica de la asociación ordinal.
* - [spearmanr](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.spearmanr.html)(a, ...)
  - Calcula un coeficiente de correlación de Spearman con el p-valor asociado.
* - [theilslopes](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.theilslopes.html)(y, ...)
  - Calcula el estimador de Theil-Sen para un conjunto de puntos _(x, y)_.
* - [weightedtau](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.weightedtau.html)(x, y, ...)
  - Calcula una versión ponderada del _tau_ de Kendall.
```

### Notas de _linregress_

[linregress](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.linregress.html): Calcula una regresión lineal de mínimos cuadrados para dos conjuntos de mediciones.
```python
# Sintaxis de llamada
stats.linregress(x, y=None, alternative='two-sided')
```
- **Parámetros:**
    - **x**, **y** - `array-like`: Vectores donde está almacenado la información en sus respectivas coordenadas, deben de tener la misma longitud. Si `y = None`, entonces _x_ debe de tener dos dimensiones.
    - **alternative** - {'two-sided', 'less', 'greater'}: Define la hipótesis alternativa.
	- 'two-sided': La pendiente de la recta de regresión no es cero.
	- 'less': La pendiente de la recta de regresión es menor a cero.
	- 'greater: La pendiente de la recta de regresión es mayor a cero.
	- 
- **Retorna:**
    - `LinRegressResult`. El objeto retornado tiene los siguientes atributos:
	- _slope_ - `float`: Pendiente de la recta.
	- _intercept_ - `float`: Intersección de la recta con el eje y.
	- _rvalue_ - `float`: Coeficiente de correlación de Pearson.
	- _pvaue_ - `float`: p-valor para la prueba de hipótesis.
	- _stderr_ - `float`: Error estándar de la pendiente estimada.
	- _intercept_stderr_ - `float`: Error estándar de la intercepción estimada.

**Uso**:

```python
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Usar linregress para regresión lineal
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)

# Imprimir resultados
print(f"Pendiente: {slope}")
print(f"Intercepto: {intercept}")
print(f"Valor r: {r_value}")
print(f"Valor p: {p_value}")
print(f"Error estándar: {std_err}")

# Crear línea de regresión
line = slope * x + intercept

# Graficar datos y regresión
plt.figure()
plt.plot(x, y, 'o', label='Datos') # Graficar datos
plt.plot(x, line, 'r-', label='Regresión lineal') # Graficar regresión
plt.xlabel('x')
plt.ylabel('y')
plt.title('Regresión Lineal con linregress')
plt.legend()
plt.grid(True)
plt.show()
```

<br/>

## Pruebas de muestras independientes

Las pruebas de muestras independientes se utilizan normalmente para evaluar si se extrajeron varias muestras de forma independiente de la misma distribución o de distribuciones diferentes con una propiedad compartida. Se dividen en pruebas para dos y múltiples muestras.

**Pruebas para dos muestras**

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [ansari](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ansari.html)(x, y, ...)
  - Realiza la prueba _Ansari-Bradley_ para igualdad de parámetros de escala.
* - [brunnermunzel](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.brunnermunzel.html)(x, y, ...)
  - Calcula la prueba _Brunner-Munzel_ en las muestras _x_ e _y_.
* - [bws_test](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.bws_test.html)(x, y, ...)
  - Realiza la prueba _Baumgartner-Weiss-Schindler_ en dos muestras independientes.
* - [cramervonmises_2samp](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.cramervonmises_2samp.html)(x, y, ...)
  - Realiza la prueba de _Cramér-Von Misses_ de dos muestras para la bondad de ajuste.
* - [epps_singleton_2samp](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.epps_singleton_2samp.html)(x, y, ...)
  - Calcula la estadística de prueba _EPPS-Singleton_ (ES).
* - [ks_2samp](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ks_2samp.html)(data1, data2, ...)
  - Realiza la prueba de _Kolmogorov-Smirnov_ de dos muestras para la bondad de ajuste.
* - [kstest](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.kstest.html)(rvs, cdf, ...)
  - Realiza la prueba de _Kolmogorov-Smirnov_ (de una muestra o dos muestras) para la bondad de ajuste.
* - [mannwhitneyu](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.mannwhitneyu.html)(x, y, ...)
  - Realiza la prueba de rango _Mann-Whitney U_ en dos muestras independientes.
* - [mood](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.mood.html)(x, y, ...)
  - Realiza la prueba de _Mood_ para igualdad de parámetros de escala.
* - [poisson_means_test](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.poisson_means_test.html)(k1, n1, k2, n2, ...)
  - Realiza la prueba de _Poisson_ para la media, también conocido como la "E-test".
* - [ranksums](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ranksums.html)(x, y, ...)
  - Calcula la estadística de suma de rango _Wilcoxon_ para dos muestras.
* - [ttest_ind](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_ind.html)(a, b, ...)
  - Calcula la prueba t para obtener para la media de dos muestras independientes de puntajes.
* - [ttest_ind_from_stats](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_ind_from_stats.html)(mean1, std1, nobs1, ...)
  - Prueba t para la media de dos muestras independientes de estadísticas descriptivas.
```

**Pruebas para múltiples muestras**

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [alexandergovern](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.alexandergovern.html)(*samples[,  nan_policy,  ...])
  - Realiza la prueba de _Alexander Govern_.
* - [anderson_ksamp](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.anderson_ksamp.html)(samples[,  midrank,  method])
  - La prueba de _Anderson-Darling_ para _K_ muestras.
* - [bartlett](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.bartlett.html)(*samples[,  axis,  nan_policy,  keepdims])
  - Realiza la prueba de _Bartlett_ para varianzas iguales.
* - [dunnett](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.dunnett.html)(*samples,  control[,  alternative,  rng])
  - Prueba de _Dunnett_: comparaciones múltiples de medias contra un grupo de control.
* - [f_oneway](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.f_oneway.html)(*samples[,  axis,  nan_policy,  keepdims])
  - Realiza ANOVA unidireccional.
* - [fligner](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.fligner.html)(*samples[,  center,  proportiontocut,  ...])
  - Realiza la prueba _Fligner-Killeen_ para la igualdad de varianza.
* - [friedmanchisquare](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.friedmanchisquare.html)(*samples[,  axis,  ...])
  - Calcula la prueba de _Friedman_ para muestras repetidas.
* - [kruskal](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.kruskal.html)(*samples[,  nan_policy,  axis,  keepdims])
  - Calcula la prueba _H_ de _Kruskal-Wallis_ para muestras independientes.
* - [levene](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.levene.html)(*samples[,  center,  proportiontocut,  ...])
  - Realiza la prueba de _Levene_ para varianzas iguales.
* - [median_test](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.median_test.html)(*samples[,  ties,  correction,  ...])
  - Realizar una prueba _Mood_ de medias.
* - [tukey_hsd](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.tukey_hsd.html)(*args)
  - Realiza la prueba de _HSD_ de _Tukey_ para la igualdad de medias durante múltiples tratamientos.
```

<br/>

## Pruebas de múltiples hipótesis y meta-análisis

Técnicas para ajustar y combinar resultados de múltiples pruebas.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [combine_pvalues](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.combine_pvalues.html)(pvalues, ...)
  - Combine los valores _p_ de las pruebas independientes que tienen la misma hipótesis.
* - [false_discovery_control](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.false_discovery_control.html)(ps, ...)
  - Ajusta los valores _p_ para controlar la tasa de descubrimiento falso.
```

<br/>

## Pruebas de una muestra y en pares

Las pruebas de una muestra se utilizan normalmente para evaluar si una sola muestra se extrajo de una distribución específica o de una distribución con propiedades específicas. Las pruebas de muestras pareadas (`ttest_rel` y `wilcoxon`) se utilizan a menudo para evaluar si dos muestras se extrajeron de la misma distribución; Se diferencian de las pruebas de muestras independientes que aparecen a continuación en que cada observación de una muestra se trata como si estuviera emparejada con una observación estrechamente relacionada de la otra muestra.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [anderson](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.anderson.html)(x, ...)
  - Prueba _Anderson-Darling_ para probar los datos provenientes tienen distribución particular.
* - [binomtest](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.binomtest.html)(k, n, ...)
  - Realiza una prueba que la probabilidad de éxito es _p_.
* - [chisquare](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.chisquare.html)(f_obs, ...)
  - Realiza la prueba de _chi cuadrado de Pearson_.
* - [cramervonmises](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.cramervonmises.html)(rvs, cdf, ...)
  - Realiza la prueba de una muestra de _Cramér-Von Mises_ para la bondad de ajuste.
* - [goodness_of_fit](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.goodness_of_fit.html)(dist, data, ...)
  - Realiza una prueba de bondad de ajuste comparando datos con una familia de distribución.
* - [jarque_bera](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.jarque_bera.html)(x, ...)
  - Realiza la prueba de bondad de ajuste _Jarque-Bera_ en datos de muestra.
* - [ks_1samp](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ks_1samp.html)(x, cdf, ...)
  - Realiza la prueba de _Kolmogorov-Smirnov_ de una muestra para la bondad de ajuste.
* - [kurtosistest](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.kurtosistest.html)(a, ...)
  - Prueba si un conjunto de datos tiene curtosis de una normal.
* - [normaltest](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.normaltest.html)(a, ...)
  - Prueba si una muestra difiere de una distribución normal.
* - [power_divergence](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.power_divergence.html)(f_obs, ...)
  - Estadística de divergencia de potencia de _Cressie-Read_ y prueba de bondad de ajuste.
* - [quantile_test](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.quantile_test.html)(x, ...)
  - Realiza una prueba de cuantil y calcula un intervalo de confianza del cuantil.
* - [shapiro](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.shapiro.html)(x, ...)
  - Realiza la prueba de _Shapiro-Wilk_ para la normalidad.
* - [skewtest](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.skewtest.html)(a, ...)
  - Prueba si el sesgo es diferente de la distribución normal.
* - [ttest_1samp](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_1samp.html)(a, popmean, ...)
  - Calcula la prueba t para la media de un grupo de puntajes.
* - [ttest_rel](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_rel.html)(a, b, ...)
  - Calcula la prueba y en dos muestras relacionadas de puntajes.
* - [wilcoxon](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.wilcoxon.html)(x, ...)
  - Realiza una prueba _Wilcoxon_ de _signed-rank_.
```

<br/>

## Variables aleatorias

Herramientas para crear y manipular variables aleatorias a partir de distribuciones.

### Clases

Herramientas para crear variables aleatorias.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [Mixture](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.Mixture.html)(components, ...)
  - Representación de una distribución de mezcla.
* - [Normal](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.Normal.html)([mu, sigma])
  - Distribución normal con media y desviación estándar prescrita.
* - [Uniform](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.Uniform.html)(...)
  - Distribución uniforme.
```

<br/>


#### Normal

Distribución normal con media y desviación estándar prescrita.

##### Atributos

Atributos de la clase `Normal`. 

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - **mu**
  - Media de la distribución.
* - **sigma**
  - Varianza de la distribución.
```

##### Métodos

Métodos de la clase `Normal`.  

```{list-table}
:header-rows: 1

* - Método
  - Descripción
* - **Principales métodos**
  -
* - [ccdf](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.Normal.ccdf.html)(x, ...)
  - Función de distribución acumulativa complementaria (1-cdf).
* - [cdf](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.Normal.cdf.html)(x, ...)
  - Función de distribución acumulativa.
* - [iccdf](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.Normal.iccdf.html)(p, /, ...)
  - Función de distribución acumulativa complementaria inversa.
* - [icdf](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.Normal.icdf.html)(p, /, ...)
  - Inversa de la función de distribución acumulada.
* - [kurtosis](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.Normal.kurtosis.html)(...)
  - Curtosis (cuarto momento estandarizado).
* - [mean](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.Normal.mean.html)(...)
  - Media (primer momento sobre el origen).
* - [median](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.Normal.median.html)(...)
  - Mediana (percentil 50).
* - [mode](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.Normal.mode.html)(...)
  - Moda (valor más probable).
* - [moment](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.Normal.moment.html)([order, kind, method])
  - Momento crudo, central o estándar de orden entero positivo.
* - [pdf](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.Normal.pdf.html)(x, /, ...)
  - Función de densidad de probabilidad.
* - [plot](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.Normal.plot.html)([x, y, t, ax])
  - Grafica una función de la distribución.
* - [sample](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.Normal.sample.html)([shape, method, rng])
  - Muestra aleatoria de la distribución.
* - [skewness](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.Normal.skewness.html)(...)
  - Asimetría (tercer momento estandarizado).
* - [standard_deviation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.Normal.standard_deviation.html)(...)
  - Desviación estándar (raíz cuadrada del segundo momento central).
* - [support](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.Normal.support.html)()
  - Soporte de la variable aleatoria.
* - [variance](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.Normal.variance.html)(...)
  - Varianza (segundo momento central).
* - **Otros métodos**
  - 
* - [entropy](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.Normal.entropy.html)(...)
  - Entropía diferencial.
* - [ilogccdf](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.Normal.ilogccdf.html)(logp, /, ...)
  - Inversa del logaritmo de la función de distribución acumulativa complementaria.
* - [ilogcdf](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.Normal.ilogcdf.html)(logp, /, ...)
  - Inversa del logaritmo de la función de distribución acumulada.
* - [logccdf](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.Normal.logccdf.html)(x, ...)
  - Logaritmo de la función de distribución acumulativa complementaria.
* - [logcdf](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.Normal.logcdf.html)(x, ...)
  - Logaritmo de la función de distribución acumulada.
* - [logentropy](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.Normal.logentropy.html)(...)
  - Logaritmo de la entropía diferencial.
* - [logpdf](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.Normal.logpdf.html)(x, /, ...)
  - Logatirmo de la función de densidad de probabilidad.
```

<br/>


### Funciones

Herramientas para manipular variables aleatorias a partir de distribuciones.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [abs](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.abs.html)(X, /)
  - Valor absoluto de una variable aleatoria.
* - [exp](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.exp.html)(X, /)
  - Exponencial natural de una variable aleatoria.
* - [log](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.log.html)(X, /)
  - Logaritmo natural de una variable aleatoria no negativa.
* - [make_distribution](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.make_distribution.html)(dist)
  - Genera una distribución continua a partir de una instancia de `rv_continuous`.
* - [order_statistic](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.order_statistic.html)(X, /, , ...)
  - Distribución de probabilidad de una estadística de orden.
* - [truncate](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.truncate.html)(X, ...)
  - Truncar el soporte de una variable aleatoria.
```