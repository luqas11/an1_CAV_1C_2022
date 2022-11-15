# Ejercicio 1:
# Resolver el siguiente sistema de ecuaciones no lineales con el método de Newton-Raphson:
# f(x,y) = x^2 + y^2 - 4 = 0
# g(x,y) = x*y - 1 = 0
# Partir de los valores (2, 0) para (x, y).

import numpy as np

# =============================================
#             PARÁMETROS INICIALES            
# =============================================

x0 = np.array([[ 2], [ 0]], dtype = float)
x = x0.copy()
y = np.zeros((len(x), 1), dtype = float)
F_x = np.zeros((len(x), 1), dtype = float)
J_x = np.zeros((len(x), len(x)), dtype = float)

MAX_ERR = 1e-12

# Funciones a resolver
def f(x, y):
    return x**2 + y**2 - 4
def g(x, y):
    return x * y - 1

# Funciones derivadas
def fx(x, y):
    return 2 * x
def fy(x, y):
    return 2 * y
def gx(x, y):
    return y
def gy(x, y):
    return x

F = [f, g]
J = [[fx, fy], [gx, gy]]

# =============================================
#                 RESOLUCIÓN           
# =============================================

for i in range(0, 100):

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
    if np.linalg.norm(diff) < MAX_ERR:
        print("Resuelto en", i, "iteraciones")
        break


print("x0 = \n", x0)
print("\nx = \n", x, "\n")
