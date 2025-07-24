# Derivación e Integración

En esta sección se presentan los módulos _differentiate_ e _integrate_.

## Módulo _differentiate_

Proporciona funciones para realizar la diferenciación numérica finitas en funciones _black-box_. Para usar este submódulo es necesario importarlo:

```python
# Importar differentiate
from scipy import differentiate

# Importar función específica
from scipy.differentiate import function_name
```
- _function_name_ es el nombre de la función que se desea importar.

:::{note}
Para más información visitar la [documentación](https://docs.scipy.org/doc/scipy/reference/differentiate.html) de _SciPy_.
:::

### Funciones

Funciones impementadas en el módulo _differentiate_.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [derivative](https://docs.scipy.org/doc/scipy/reference/generated/scipy.differentiate.derivative.html)(f, x, ...)
  - Evalúa la derivada _element-wise_ de una función escalar real numéricamente.
* - [hessian](https://docs.scipy.org/doc/scipy/reference/generated/scipy.differentiate.hessian.html)(f, x, ...)
  - Evalúa la Hessiana de una función numéricamente.
* - [jacobian](https://docs.scipy.org/doc/scipy/reference/generated/scipy.differentiate.jacobian.html)(f, x, ...)
  - Evalúa el jacobiano de una función numéricamente.
```

<br/>

## Módulo _integrate_

Proporciona funciones para realizar integrales, resolver ecuaciones diferenciales ordinales, sumatorias, entre otros.

```python
# Importar integrate
from scipy import integrate

# Importar función específica
from scipy.integrate import function_name
```
- _function_name_ es el nombre de la función que se desea importar.

:::{note}
Para más información visitar la [documentación](https://docs.scipy.org/doc/scipy/reference/integrate.html) de _SciPy_.
:::

A continuación se presenta un resumen de las secciones de este módulo:
- **Integración de funciones con muestras fijas**: Métodos para integrar funciones cuando se tienen muestras discretas de los datos (por ejemplo, usando la regla del trapecio o Simpson).
- **Integración con objetos de función**: Métodos para integrar funciones cuando se tiene acceso a la función como un objeto (por ejemplo, usando `quad` para integración numérica).
- **EDO - Valores en la frontera**: Métodos para resolver sistemas de ecuaciones diferenciales ordinarias (EDO) con condiciones de frontera (por ejemplo, `solve_bvp`).
- **Resolución de problemas de valores iniciales para sistemas de EDO**: Métodos para resolver sistemas de ecuaciones diferenciales ordinarias (EDO) con condiciones iniciales (por ejemplo, `solve_ivp`).
- **Sumatoria**: Funciones para calcular sumas numéricas, como la suma de Riemann o sumas ponderadas.

<br/>

### Integración con muestras fijas

Métodos para integrar funciones cuando se tienen muestras discretas de los datos (por ejemplo, usando la regla del trapecio o Simpson).

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [cumulative_simpson](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.cumulative_simpson.html)(y, ...)
  - Integra acumulativamente $y(x)$ utilizando la regla 1/3 compuesta de Simpson.
* - [cumulative_trapezoid](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.cumulative_trapezoid.html)(y, ...)
  - Integra acumulativamente $y(x)$ utilizando la regla trapezoidal compuesta.
* - [romb](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.romb.html)(y, ...)
  - Integración de Romberg utilizando muestras de una función.
* - [simpson](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.simpson.html)(y, ...)
  - Integra $y(x)$ usando muestras a lo largo del eje dado y la regla de la compuesta de Simpson.
* - [trapezoid](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.trapezoid.html)(y, ...)
  - Integra a lo largo del eje dado utilizando la regla trapezoidal compuesta.
```

<br/>

### Integración con objetos de función

Métodos para integrar funciones cuando se tiene acceso a la función como un objeto (por ejemplo, usando `quad` para integración numérica).

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [cubature](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.cubature.html)(f, a, b, ...)
  - Cubatura adaptativa de la función multidimensional matricial.
* - [dblquad](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.dblquad.html)(func, a, b, gfun, hfun, ...)
  - Calcula una doble integral.
* - [fixed_quad](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.fixed_quad.html)(func, a, b, ...)
  - Calcula una integral definida utilizando la cuadratura gaussiana de orden fijo.
* - [lebedev_rule](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.lebedev_rule.html)(n)
  - Cuadratura Lebedev.
* - [newton_cotes](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.newton_cotes.html)(rn, ...)
  - Retorna los pesos y el coeficiente de error para la integración de Newton-Cotes.
* - [nquad](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.nquad.html)(func, ranges, ...)
  - Integración sobre múltiples variables.
* - [qmc_quad](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.qmc_quad.html)(func, a, b, ...)
  - Calcula una integral en N-dimensiones utilizando la cuadratura _Quasi-Monte Carlo_.
* - [quad](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.quad.html)(func, a, b, ...)
  - Calcula una integral definitiva.
* - [quad_vec](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.quad_vec.html)(f, a, b, ...)
  - Integración adaptativa de una función vectorial.
* - [tanhsinh](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.tanhsinh.html)(f, a, b, ...)
  - Evalúa una integral convergente numéricamente utilizando cuadratura de Tanh-Sinh.
* - [tplquad](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.tplquad.html)(func, a, b, gfun, hfun, qfun, rfun)
  - Calcula una integral triple (definitiva).
```

<br/>

### EDO - Valores en la frontera

Métodos para resolver sistemas de ecuaciones diferenciales ordinarias (EDO) con condiciones de frontera.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [solve_bvp](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_bvp.html)(fun, bc, x, y, ...)
  - Resuelve un problema de valor de frontera para un sistema de ecuaciones diferenciales ordinarias.
```

<br/>

### Resolución de problemas de valores iniciales para sistemas de EDO

Métodos para resolver sistemas de ecuaciones diferenciales ordinarias (EDO) con condiciones iniciales.

#### Funciones

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [solve_ivp](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html)(fun, t_span, y0, ...)
  - Resuelve un problema de valor inicial para un sistema de ecuaciones diferenciales ordinarias.
```

#### Clases

Estos _solvers_ están implementaos como clases individuales, que pueden ser usados directamente o a través de una función conveniente.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [BDF](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.BDF.html)(fun, t0, y0, t_bound, ...)
  - Método implícito basado en fórmulas de _backward-differentiation_.
* - [DOP853](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.DOP853.html)(fun, t0, y0, t_bound, ...)
  - Método explícito Runge-Kutta de orden 8.
* - [DenseOutput](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.DenseOutput.html)(t_old, t)
  - Clase base para el paso interpolante local realizado por un solucionador ODE.
* - [LSODA](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.LSODA.html)(fun, t0, y0, t_bound, ...)
  - Método ADAMS/BDF con detección y conmutación de rigidez automática.
* - [OdeSolution](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.OdeSolution.html)(ts, interpolants, ...)
  - Solución de ODE continua.
* - [OdeSolver](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.OdeSolver.html)(fun, t0, y0, t_bound, vectorized)
  - Clase base para solucionadores ODE.
* - [RK23](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.RK23.html)(fun, t0, y0, t_bound, ...)
  - Método explícito Runge-Kutta de orden 3(2).
* - [RK45](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.RK45.html)(fun, t0, y0, t_bound, ...)
  - Método explícito Runge-Kutta de orden 5 (4).
* - [Radau](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.Radau.html)(fun, t0, y0, t_bound, ...)
  - Método implícito de Runge-Kutta de la familia de orden de IIA Radau de orden 5.
```

#### API Antigua

Estas son las rutinas desarrolladas anteriormente para _SciPy_. Incluyen solucionadores más antiguos implementados en Fortran. Si bien la interfaz para ellos no es particularmente conveniente y faltan ciertas características en comparación con la nueva API, los solucionadores en sí son de buena calidad y funcionan rápido como código Fortran compilado. En algunos casos, podría valer la pena utilizar esta antigua API.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [ODEintWarning](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.ODEintWarning.html)()
  - Advertencia arrojada durante la ejecución de `odeint`.
* - [complex_ode](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.complex_ode.html)(f, ...)
  - Un envoltorio de ODE para sistemas complejos.
* - [ode](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.ode.html)(f, ...)
  - Una clase de interfaz genérica para integradores numéricos.
* - [odeint](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.odeint.html)(func, y0, t, ...)
  - Integra un sistema de ecuaciones diferenciales ordinarias.
```

<br/>

### Sumatoria

Funciones para calcular sumas numéricas.

```{list-table}
:header-rows: 1

* - Función
  - Descripción
* - [nsum](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.nsum.html)(f, a, b, ...)
  - Evalúa una serie convergente finita o infinita.
```
