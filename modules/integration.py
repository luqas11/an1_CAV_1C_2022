# Algoritmos de integración numérica

import numpy as np
from utils import range1

def trapezoidal(f, h, inf, sup):
    """Retorna el valor de una integral calculada mediante el método de los trapecios.

    La integral se aplica a la función `f` desde el límite inferior `inf` hasta el límite superior `sup`.

    El método utiliza un paso `h` y la cantidad de intervalos `n` se deduce de `h`, `inf` y `sup`.

    Parameters
    ----------
    f : function
        Función a integrar.
    h : float
        Tamaño del paso a utilizar.
    inf : float
        Límite inferior de la integral.
    sup : float
        Límite superior de la integral.

    Returns
    -------
    float
        Resultado del cálculo de la integral.
    """
    n = int(np.round((sup - inf) / h))

    sum = h/2 * (f(inf) + f(sup))
    for i in range(1, n):
        sum += h * f(inf + i*h)
    return sum

def trapezoidal_discrete(x, y):
    """Retorna el valor de una integral calculada mediante el método de los trapecios.

    La integral se aplica al conjunto de puntos `(x,y)`, entre los puntos extremos del intervalo de las `x`.

    El método utiliza un paso `h` y una cantidad de intervalos `n` que se deducen del conjunto.

    Parameters
    ----------
    x : numpy.ndarray
        Valores discretos del dominio de la función a integrar.
    y : numpy.ndarray
        Valores discretos de la imagen de la función a integrar.

    Returns
    -------
    float
        Resultado del cálculo de la integral.
    """
    h = x[1] - x[0]
    n = len(x) - 1

    sum = h/2 * (y[0] + y[n])
    for i in range(1, n):
        sum += h * y[i]
    return sum

def simpson(f, h, inf, sup):
    """Retorna el valor de una integral calculada mediante el método de Simpson.

    La integral se aplica a la función `f` desde el límite inferior `inf` hasta el límite superior `sup`.

    El método utiliza un paso `h` y la cantidad de intervalos `n` se deduce de `h`, `inf` y `sup`.

    Parameters
    ----------
    f : function
        Función a integrar.
    h : float
        Tamaño del paso a utilizar.
    inf : float
        Límite inferior de la integral.
    sup : float
        Límite superior de la integral.

    Returns
    -------
    float
        Resultado del cálculo de la integral.

    Raises
    ------
    Exception
        El método no puede ser aplicado si la cantidad de intervalos es impar.
    """
    n = int(np.round((sup - inf) / h))
    if n % 2 != 0:
        raise Exception('El método de Simpson requiere un valor de n par. Valor dado: %i' % n)

    sum = f(inf) + f(sup)
    for i in range1(1, int(n/2 - 1)):
        sum += 2 * f(inf + h*2*i)
    for i in range1(1, int(n/2)):
        sum += 4 * f(inf + h*(2*i-1))
    sum = sum * h/3
    return sum

def simpson_discrete(x, y):
    """Retorna el valor de una integral calculada mediante el método de los trapecios.

    La integral se aplica al conjunto de puntos `(x,y)`, entre los puntos extremos del intervalo de las `x`.
    
    El método utiliza un paso `h` y una cantidad de intervalos `n` que se deducen del conjunto.

    Parameters
    ----------
    x : numpy.ndarray
        Valores discretos del dominio de la función a integrar.
    y : numpy.ndarray
        Valores discretos de la imagen de la función a integrar.

    Returns
    -------
    float
        Resultado del cálculo de la integral.

    Raises
    ------
    Exception
        El método no puede ser aplicado si la cantidad de intervalos es impar.
    """
    h = x[1] - x[0]
    n = len(x) - 1
    if n % 2 != 0:
        raise Exception('El método de Simpson requiere un valor de n par. Valor dado: %i' % n)

    sum = x[0] + x[n]
    for i in range1(1, int(n/2 - 1)):
        sum += 2 * y[2*i]
    for i in range1(1, int(n/2)):
        sum += 4 * y[2*i-1]
    sum = sum * h/3
    return sum

def richardson(i1, i2, p):
    """Retorna el resultado del cálculo de la extrapolación de Richardson para dos integrales `i1` e `i2`, considerando que fueron calculadas con un orden `p`.

    Parameters
    ----------
    i1 : float
        Resultado de la integral para un paso h.
    i2 : float
        Resultado de la integral para un paso h/2.
    p : int
        Orden del método de cálculo de las integrales i1 e i2.

    Returns
    -------
    float
        Resultado del cálculo de la extrapolación.
    """    
    return i1 + (i1 - i2) / ((0.5)**p - 1)

def gauss_points(n):
    """Retorna el conjunto de abscisas de Gauss para órdenes de entre 2 y 6.

    Parameters
    ----------
    n : int
        Orden del método

    Returns
    -------
    numpy.ndarray
        Array de abscisas de Gauss para el orden indicado.

    Raises
    ------
    Exception
        Sólo están definidos los abscisas de Gauss para órdenes de entre 2 y 6.
    """    
    match n:
        case 2:
            return np.array([[-0.577350269], [ 0.577350269]], dtype = float)
        case 3:
            return np.array([[-0.774596669], [ 0.000000000], [ 0.774596669]], dtype = float)
        case 4:
            return np.array([[-0.861136312], [-0.339981044], [ 0.339981044], [ 0.861136312]], dtype = float)
        case 5:
            return np.array([[-0.906179846], [-0.538469310], [ 0.000000000], [ 0.538469310], [ 0.906179846]], dtype = float)
        case 6:
            return np.array([[-0.932469514], [-0.661209386], [-0.238619186], [ 0.238619186], [ 0.661209386], [ 0.932469514]], dtype = float)
        case _:
            raise Exception('El número de puntos indicado no está definido. Valor dado: %i' % n)

def gauss_weights(n):
    """Retorna el conjunto de pesos de Gauss para órdenes de entre 2 y 6.

    Parameters
    ----------
    n : int
        Orden del método

    Returns
    -------
    numpy.ndarray
        Array de pesos de Gauss para el orden indicado.

    Raises
    ------
    Exception
        Sólo están definidos los pesos de Gauss para órdenes de entre 2 y 6.
    """    
    match n:
        case 2:
            return np.array([[ 1.0000000], [ 1.0000000]], dtype = float)
        case 3:
            return np.array([[ 0.5555556], [ 0.8888889], [ 0.5555556]], dtype = float)
        case 4:
            return np.array([[ 0.3478548], [ 0.6521452], [ 0.6521452], [ 0.3478548]], dtype = float)
        case 5:
            return np.array([[ 0.2369269], [ 0.4786287], [ 0.5688889], [ 0.4786287], [ 0.2369269]], dtype = float)
        case 6:
            return np.array([[ 0.1713245], [ 0.3607616], [ 0.4679139], [ 0.4679139], [ 0.3607616], [ 0.1713245]], dtype = float)
        case _:
            raise Exception('El número de puntos indicado no está definido. Valor dado: %i' % n)

def gauss(f, n, inf, sup):
    """Retorna el valor de una integral calculada mediante el método de Gauss.

    La integral se aplica a la función `f` desde el límite inferior `inf` hasta el límite superior `sup`.

    El método utiliza una cantidad de puntos de Gauss `n`.

    Parameters
    ----------
    f : function
        Función a integrar.
    n : int
        Cantidad de puntos de Gauss a utilizar.
    inf : float
        Límite inferior de la integral.
    sup : float
        Límite superior de la integral.

    Returns
    -------
    float
        Resultado del cálculo de la integral.
    """    
    sum = 0
    j = (sup - inf) / 2

    def phi(u):
        return f((sup - inf) * u/2 + (inf + sup) / 2)
    for i in range(0, n):
        ui = gauss_points(n)[i]
        ci = gauss_weights(n)[i]
        sum += ci * phi(ui)
    sum = sum * j
    return sum

def romberg(f, h, inf, sup):
    """Retorna el valor de una integral calculada mediante el método de Romberg.

    La integral se aplica a la función `f` desde el límite inferior `inf` hasta el límite superior `sup`.

    El método utiliza una paso inicial `h`, reduciéndolo 4 veces y calculando 4 órdenes del método de Romberg. La razón de la reducción es siempre 1/2.

    Parameters
    ----------
    f : function
        Función a integrar.
    h : float
        Tamaño del paso a utilizar.
    inf : float
        Límite inferior de la integral.
    sup : float
        Límite superior de la integral.

    Returns
    -------
    numpy.ndarray
        Tabla de dimensiones 4x4 con todos los resultados parciales del método de Romberg.
    """    
    romberg_table = np.zeros((4, 4), dtype = float)

    for i in range(0, 4):
        _h = h/(2**i)
        romberg_table[i][0] = trapezoidal(f, _h, inf, sup)
    for i in range(0,3):
        for j in range(i+1,4):
            romberg_table[j][i+1] = richardson(romberg_table[j-1][i], romberg_table[j][i], 2*(i+1))
    return romberg_table
