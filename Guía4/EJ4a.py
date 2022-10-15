# Ejercicio 4a:
# Resolver el siguiente sistema de ecuaciones no lineales con el método de Newton-Raphson:
# x * y^2 = 11.2
# x + y = -1.83
# Partir de los valores (1, -3) para (x, y) y utilizar aritmética de punto flotante con 3 dígitos de precisión.

import numpy as np

# =============================================
#             PARÁMETROS INICIALES            
# =============================================

x0 = np.array([[ 1], [ -3]], dtype = float)
x = x0.copy()
y = np.zeros((len(x), 1), dtype = float)
F_x = np.zeros((len(x), 1), dtype = float)
J_x = np.zeros((len(x), len(x)), dtype = float)

precision = 3

# Funciones a resolver
def f(x, y):
    return x * y**2 - 11.2
def g(x, y):
    return x + y + 1.83

# Funciones derivadas
def fx(x, y):
    return y**2
def fy(x, y):
    return 2 * x * y
def gx(x, y):
    return np.array([1])
def gy(x, y):
    return np.array([1])

F = [f, g]
J = [[fx, fy], [gx, gy]]

# =============================================
#                 RESOLUCIÓN           
# =============================================

# Conversión a float de n dígitos
def fm(x):
    return float(np.format_float_scientific(x, precision = precision - 1))

# Conversión f() array a float de n dígitos
def arr_f(x):
    for i in range(0, len(x)):
        x[i] = fm(x[i])
    return x

for i in range(0, 30):

    xk = x.copy()

    for j in range(0, len(x)):
        F_x[j] = fm(-F[j](*x)[0])
        for k in range(0, len(x)):
            J_x[j][k] = fm(J[j][k](*x)[0])

    U = J_x.copy()
    L = np.identity(len(J_x), dtype = float)

    # Descomposición LU
    for j in range(0, len(U)):
        for k in range(j+1, len(U)):
            m = fm(U[k][j] / U[j][j])
            L[k][j] = m
            U[k] = arr_f(U[k] - arr_f(U[j] * m))

    # Cálculo de y
    for j in range(0, len(L)):
        sum = 0
        for k in range(0, j):
            sum = fm(sum + fm(L[j][k] * y[k]))
        y[j] = fm(fm(F_x[j] - sum) / L[j][j])

    # Cálculo de x
    for j in reversed(range(0, len(U))):
        sum = 0
        for k in range(j+1, len(U)):
            sum = fm(sum + fm(U[j][k] * x[k]))
        x[j] = fm(fm(y[j] - sum) / U[j][j])

    diff = x.copy()
    x = arr_f(x + xk)

    valid = 1
    if (x==xk).all():
        print("Resuelto en", i, "iteraciones")
        break

print("x0 = \n", x0)
print("\nx = \n", x, "\n")
