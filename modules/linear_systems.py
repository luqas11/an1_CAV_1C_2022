# Algoritmos de resolución de sistemas de ecuaciones lineales

import numpy as np

ITERACIONES_JACOBI = 4

def jacobi(A, b, xi):
    """Retorna el vector solución del sistema `Ax = b`, calculado por el método de Jacobi.

    Para calcularlo, el método parte de la semilla `xi`, realizando una cantidad `ITERACIONES_JACOBI` de iteraciones.

    Parameters
    ----------
    A : numpy.ndarray
        Matriz del sistema.
    b : numpy.ndarray
        Vector independiente del sistema.
    xi : numpy.ndarray
        Vector semilla.

    Returns
    -------
    numpy.ndarray
        Vector solución del sistema.
    """
    x = xi.copy()
    x1 = np.zeros((len(x), 1), dtype = float)

    for i in range(0, ITERACIONES_JACOBI):
        x1 = x.copy()
        for j in range(0, len(A)):
            sum = 0
            for k in range(0, len(A)):
                if j != k:
                    sum = sum + A[j][k] * x1[k]
            x[j] = (b[j] - sum) / A[j][j]
    return x

def gauss(A, b):
    """Retorna el vector solución del sistema `Ax = b`, calculado por el método de eliminación de Gauss sin pivoteo.

    Parameters
    ----------
    A : numpy.ndarray
        Matriz del sistema.
    b : numpy.ndarray
        Vector independiente del sistema.

    Returns
    -------
    numpy.ndarray
        Vector solución del sistema.
    """
    x = np.zeros((len(A), 1), dtype = float)

    for i in range(0, len(A)):
        for j in range(i+1, len(A)):
            b[j] = b[j] - b[i]  * A[j][i] / A[i][i]
            A[j] = A[j] - A[i] * A[j][i] / A[i][i]

    for i in reversed(range(0, len(A))):
        sum = 0
        for j in range(i+1, len(A)):
            sum = sum + A[i][j] * x[j]
        x[i] = (b[i] - sum) / A[i][i]

    return x
