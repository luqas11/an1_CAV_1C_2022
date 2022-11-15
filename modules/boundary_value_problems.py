# Algoritmos de resolución de ecuaciones diferenciales con valores de contorno

import numpy as np
from linear_systems import gauss

def pvc2(fc, b, h, inf, sup, fcn=False):
    """Retorna el conjunto de puntos `(x,y)` que son solución del problema de valores de contorno establecido por la matriz tridiagonal que se genera a partir de los coeficientes `c`, que a su vez surgen de la discretización de la ecuación diferencial mediante operadores.

    El cálculo utiliza un paso `h`, para el intervalo `[inf, sup]` y con valores de contorno de `u(inf) = ui` y `u(sup) = uf`.

    El vector b es el término independiente del SEL que surge de la discretización.

    Parameters
    ----------
    fc : numpy.ndarray
        Función que genera el array de coeficientes para construir la matriz tridiagonal.
    b : numpy.ndarray
        Array de coeficientes para el término independiente.
    h : float
        Tamaño del paso a utilizar.
    inf : float
        Valor inicial de `x`.
    sup : float
        Valor final de `x`.
    fcn : numpy.ndarray, optional
        Función que genera el array de coeficientes para construir la última fila de la matriz (opcional, por defecto una fila identidad).

    Returns
    -------
    numpy.ndarray, numpy.ndarray
        Retorna el conjunto de puntos `(x,y)` que son solución del sistema de ecuaciones diferenciales definido.
    """  
    n = int(np.round((sup - inf) / h))
    A = np.zeros((n+1, n+1), dtype = float)
    A[0][0] = 1
    A[len(A)-1][len(A)-1] = 1
    
    for i in range(1, len(A)-1):
        for j in range(0, 3):
            A[i][j+i-1] = fc(i*h)[j]

    if not(isinstance(fcn, bool) and fcn == False):
        for j in range(0, 2):
            A[len(A)-1][j+len(A)-2] = fcn((len(A)-1)*h)[j]

    y = gauss(A, b)
    x = np.zeros((len(y), 1), dtype = float)
    for i in range(0, len(x)):
        x[i] = h*i
    return x, y
