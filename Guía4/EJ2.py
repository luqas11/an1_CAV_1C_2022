# Ejercicio 2:
# Resolver el siguiente sistema de ecuaciones no lineales con el método de Newton-Raphson:
# 1.021 * (x^2 / y) = -4.953
# 5.040 * x * y = -0.05440
# Partir de los valores (0.3, -0.03) para (x, y) e iterar hasta obtener una precisión de 4 dígitos significativos.

import math
import numpy as np

# =============================================
#             PARÁMETROS INICIALES            
# =============================================

x0 = np.array([[ 0.3], [ -0.03]], dtype = float)
x = x0.copy()
y = np.zeros((len(x), 1), dtype = float)
F_x = np.zeros((len(x), 1), dtype = float)
J_x = np.zeros((len(x), len(x)), dtype = float)

PRECISION = 4

# Funciones a resolver
def f(x, y):
    return 1.021 * (x**2 / y) + 4.953
def g(x, y):
    return 5.040 * x * y + 0.05440

# Funciones derivadas
def fx(x, y):
    return 2.042 * x / y
def fy(x, y):
    return - 1.021 * x**2 / y**2
def gx(x, y):
    return 5.040 * y
def gy(x, y):
    return 5.040 * x

# Obtener el orden de magnitud de un número
def mag(x):
    return math.floor(math.log10(abs(x)))

F = [f, g]
J = [[fx, fy], [gx, gy]]

# =============================================
#                 RESOLUCIÓN           
# =============================================

for i in range(0, 30):

    xk = x.copy()

    for j in range(0, len(x)):
        F_x[j] = -F[j](*x)[0]
        for k in range(0, len(x)):
            J_x[j][k] = J[j][k](*x)[0]

    U = J_x.copy()
    L = np.identity(len(J_x), dtype = float)

    # Descomposición LU
    for j in range(0, len(U)):
        for k in range(j+1, len(U)):
            m = (U[k][j] / U[j][j])
            L[k][j] = m
            U[k] = U[k] - U[j] * m

    # Cálculo de y
    for j in range(0, len(L)):
        sum = 0
        for k in range(0, j):
            sum = sum + L[j][k] * y[k]
        y[j] = (F_x[j] - sum) / L[j][j]

    # Cálculo de x
    for j in reversed(range(0, len(U))):
        sum = 0
        for k in range(j+1, len(U)):
            sum = sum + U[j][k] * x[k]
        x[j] = (y[j] - sum) / U[j][j]

    diff = x.copy()
    x = x + xk

    valid = 1
    for j in range(0, len(diff)):
        if abs(mag(diff[j]) - mag(x[j])) <= PRECISION:
            valid = 0
    if valid:
        print("Resuelto en", i, "iteraciones")
        break

print("x0 = \n", x0)
print("\nx = \n", x, "\n")