# Ejercicio 5:
# Resolver el siguiente sistema de ecuaciones no lineales con el método de Newton-Raphson:
# x * y * z = 4.188
# x + y + z = 3.677
# x + 1.258 * y = 0
# Partir de los valores (1, -1, 3) para (x, y, z).

import numpy as np

# =============================================
#             PARÁMETROS INICIALES            
# =============================================

x0 = np.array([[ 1], [ -1], [ 3]], dtype = float)
x = x0.copy()
y = np.zeros((len(x), 1), dtype = float)
F_x = np.zeros((len(x), 1), dtype = float)
J_x = np.zeros((len(x), len(x)), dtype = float)

# Funciones a resolver
def f(x, y, z):
    return x * y * z - 4.188
def g(x, y, z):
    return x + y + z - 3.677
def h(x, y, z):
    return x + 1.258 * y

# Funciones derivadas
def fx(x, y, z):
    return y * z
def fy(x, y, z):
    return x * z
def fz(x, y, z):
    return x * y
def gx(x, y, z):
    return np.array([1])
def gy(x, y, z):
    return np.array([1])
def gz(x, y, z):
    return np.array([1])
def hx(x, y, z):
    return np.array([1])
def hy(x, y, z):
    return np.array([1.258])
def hz(x, y, z):
    return np.array([0])

F = [f, g, h]
J = [[fx, fy, fz], [gx, gy, gz], [hx, hy, hz]]

# =============================================
#                 RESOLUCIÓN           
# =============================================

for i in range(0, 40):

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
            m = U[k][j] / U[j][j]
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

    #print(J_x)
    #print(F_x)
    #print(x, "\n")
    x = x + xk

print("x0 = \n", x0)
print("\nx = \n", x, "\n")
