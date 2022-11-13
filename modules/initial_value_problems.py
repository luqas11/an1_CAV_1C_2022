# Algoritmos de resolución de ecuaciones diferenciales con valores iniciales

import numpy as np
from utils import range1

def euler_explicit(f, h, un, inf, sup):
    """Retorna el conjunto de puntos `(x,y)` que son solución de la ecuación diferencial `y' = f(y,t)`, para el intervalo `[inf, sup]` y con un valor inicial de `y(inf) = un`.
    
    El cálculo utiliza el método de Euler explícito con un paso `h`.

    Parameters
    ----------
    f : function
        Función derivada de `y`.
    h : float
        Tamaño del paso a utilizar.
    un : float
        Valor inicial de `y`.
    inf : float
        Valor inicial de `t`.
    sup : float
        Valor final de `t`.

    Returns
    -------
    numpy.ndarray, numpy.ndarray
        Retorna el conjunto de puntos `(x,y)` que son solución de la ecuación diferencial definida.
    """    
    x = np.array([[]], dtype = float)
    y = np.array([[]], dtype = float)
    n = int(np.round((sup - inf) / h))

    for i in range1(0, n):
        x = np.append(x, inf + h*i)
        y = np.append(y, un)
        un1 = un + h * f(un, inf + h*i)
        un = un1
    return x, y

def rk2(f, h, un, inf, sup):
    """Retorna el conjunto de puntos `(x,y)` que son solución de la ecuación diferencial `y' = f(y,t)`, para el intervalo `[inf, sup]` y con un valor inicial de `y(inf) = un`.
    
    El cálculo utiliza el método de Runge Kutta de orden 2 con un paso `h`.

    Parameters
    ----------
    f : function
        Función derivada de `y`.
    h : float
        Tamaño del paso a utilizar.
    un : float
        Valor inicial de `y`.
    inf : float
        Valor inicial de `t`.
    sup : float
        Valor final de `t`.

    Returns
    -------
    numpy.ndarray, numpy.ndarray
        Retorna el conjunto de puntos `(x,y)` que son solución de la ecuación diferencial definida.
    """    
    x = np.array([[]], dtype = float)
    y = np.array([[]], dtype = float)
    n = int(np.round((sup - inf) / h))

    for i in range1(0, n):
        x = np.append(x, inf + h*i)
        y = np.append(y, un)
        q1 = h * f(un, h*i)
        q2 = h * f(un + q1, inf + h*(i+1))
        un1 = un + (q1 + q2)/2
        un = un1
    return x, y

def euler_implicit(enl, h, u0, inf, sup):
    """Retorna el conjunto de puntos `(x,y)` que son solución de la ecuación diferencial `y' = f(y,t)`, para el intervalo `[inf, sup]` y con un valor inicial de `y(inf) = u0`.
    
    El cálculo utiliza el método de Euler implícito con un paso `h`.

    La ecuación no lineal de cada iteración se resuelve con la función `enl`, que utiliza a la constante `un` para su definición.

    Parameters
    ----------
    enl : function
        Función que resuelve la ecuación no lineal, a la cual se le puede definir una constante `un`.
    h : float
        Tamaño del paso a utilizar.
    u0 : float
        Valor inicial de `y`.
    inf : float
        Valor inicial de `t`.
    sup : float
        Valor final de `t`.

    Returns
    -------
    numpy.ndarray, numpy.ndarray
        Retorna el conjunto de puntos `(x,y)` que son solución de la ecuación diferencial definida.
    """
    x = np.array([[]], dtype = float)
    y = np.array([[]], dtype = float)
    n = int(np.round((sup - inf) / h))
    un = u0

    for i in range1(0, n):
        x = np.append(x, inf + h*i)
        y = np.append(y, un)
        un1 = enl(un)
        un = un1
    return x, y

def rk2_2(fu, fv, h, un, vn, inf, sup):
    """Retorna el conjunto de puntos `(x,y)` que son solución del sistema de ecuaciones diferenciales dado por

    `u' = fu(u, v, t)`

    `v' = fv(u, v, t)`

    para el intervalo `[inf, sup]` y con un valor inicial de `u(inf) = un` y `v(inf) = vn`.
    
    El cálculo utiliza el método de Runge Kutta de orden 2 con un paso `h`.

    Parameters
    ----------
    fu : function
        Función derivada de `u`.
    fv : function
        Función derivada de `v`.
    h : float
        Tamaño del paso a utilizar.
    un : float
        Valor inicial de `fu`.
    vn : float
        Valor inicial de `fv`.
    inf : float
        Valor inicial de `t`.
    sup : float
        Valor final de `t`.

    Returns
    -------
    numpy.ndarray, numpy.ndarray
        Retorna el conjunto de puntos `(x,y)` que son solución del sistema de ecuaciones diferenciales definido.
    """   
    x = np.array([[]], dtype = float)
    y = np.array([[]], dtype = float)
    n = int(np.round((sup - inf) / h))

    for i in range1(0, n):
        x = np.append(x, inf + h*i)
        y = np.append(y, un)
        q1u = h * fu(un, vn, h*i)
        q1v = h * fv(un, vn, h*i)
        q2u = h * fu(un + q1u, vn + q1v, inf + h*(i+1))
        q2v = h * fv(un + q1u, vn + q1v, inf + h*(i+1))
        un1 = un + (q1u + q2u)/2
        vn1 = vn + (q1v + q2v)/2        
        un = un1
        vn = vn1
    return x, y

def euler_implicit_2(fm, fsel, h, un, vn, inf, sup):
    """Retorna el conjunto de puntos `(x,y)` que son solución del sistema de ecuaciones diferenciales lineales dado por la matriz generada con la función `fm`.

    El cálculo utiliza el método de Euler implícito con un paso `h`, para el intervalo `[inf, sup]` y con valores iniciales de `u(inf) = un` y `v(inf) = vn`.

    Parameters
    ----------
    fm : function
        Función que genera las matrices a resolver en cada punto.
    fsel : function
        Función que resuelve los SELs.
    h : float
        Tamaño del paso a utilizar.
    un : float
        Valor inicial de `u`.
    vn : float
        Valor inicial de `v`.
    inf : float
        Valor inicial de `t`.
    sup : float
        Valor final de `t`.

    Returns
    -------
    numpy.ndarray, numpy.ndarray
        Retorna el conjunto de puntos `(x,y)` que son solución del sistema de ecuaciones diferenciales definido.
    """   
    x = np.array([[]], dtype = float)
    y = np.array([[]], dtype = float)
    n = int(np.round((sup - inf) / h))

    xn = np.array([[ un], [ vn]], dtype = float)
    for l in range(0, n):
        A, b = fm(xn[0], xn[1], inf + h*l)
        x = np.append(x, inf + h*l)
        y = np.append(y, xn[0])
        xn = fsel(A, b, xn)        
    return x, y

def euler_explicit_2(fu, fv, h, un, vn, inf, sup):
    """Retorna el conjunto de puntos `(x,y)` que son solución del sistema de ecuaciones diferenciales `(u,v)` cuyas funciones derivadas son `(fu,fv)` respectivamente.

    El cálculo utiliza el método de Euler explícito con un paso `h`, para el intervalo `[inf, sup]` y con valores iniciales de `u(inf) = un` y `v(inf) = vn`.

    Parameters
    ----------
    fu : function
        Función derivada de la función `u`.
    fv : function
        Función derivada de la función `v`.
    h : float
        Tamaño del paso a utilizar.
    un : float
        Valor inicial de `u`.
    vn : float
        Valor inicial de `v`.
    inf : float
        Valor inicial de `t`.
    sup : float
        Valor final de `t`.

    Returns
    -------
    numpy.ndarray, numpy.ndarray
        Retorna el conjunto de puntos `(x,y)` que son solución del sistema de ecuaciones diferenciales definido.
    """   
    x = np.array([[]], dtype = float)
    y = np.array([[]], dtype = float)
    n = int(np.round((sup - inf) / h))

    xn = np.array([[ un], [ vn]], dtype = float)
    for l in range1(0, n):
        x = np.append(x, inf + h*l)
        y = np.append(y, xn[0])
        un1 = fu(xn[0], xn[1], inf + h*(l+1))
        vn1 = fv(xn[0], xn[1], inf + h*(l+1))
        xn[0] = un1
        xn[1] = vn1
    return x, y
