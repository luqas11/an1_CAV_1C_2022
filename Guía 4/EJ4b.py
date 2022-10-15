# Ejercicio 4b:
# Resolver el siguiente sistema de ecuaciones no lineales con el método de Gauss-Seidel no lineal:
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

# Conversión de array a float de n dígitos
def arr_f(x):
    for i in range(0, len(x)):
        x[i] = fm(x[i])
    return x

for i in range(0, 100):

    xk = x.copy()
    for j in range(0, len(x)):
        F_x[j] = fm(-F[j](*x)[0])
        for k in range(0, len(x)):
            J_x[j][k] = fm(J[j][k](*x)[0])

    # Cálculo de la solución por Gauss-Seidel
    for j in range(0, 100):
        valid = 1

        for k in range(0, len(J_x)):
            sum = 0
            for p in range(0, len(J_x)):
                if k != p:
                    sum = fm(sum + fm(J_x[k][p] * x[p]))

            val = fm(fm(F_x[k] - sum) / J_x[k][k])
            if (x[k] != val):
                valid = 0
            x[k] = val
        if valid:
            print("\nResuelto en", (j + 1), "iteraciones\n")
            print(x, "\n")
            break

    diff = x.copy()
    x = arr_f(x + xk)

    valid = 1
    if (x==xk).all():
        print("Resuelto en", i, "iteraciones")
        break

print("x0 = \n", x0)
print("\nx = \n", x, "\n")
