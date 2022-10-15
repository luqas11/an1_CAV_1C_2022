# Ejercicio 5b:
# Obtener la descomposición LU del sistema de ecuaciones Ax=b y resolverlo refinando iterativamente la solución.
# Utilizar aritmética de punto flotante con 4 dígitos de precisión.

import numpy as np

# =============================================
#             PARÁMETROS INICIALES            
# =============================================

A = np.array([[ 31.69, 14.31], [ 13.11, 5.890]], dtype = float)
b = np.array([[ 45.00], [ 19.00]], dtype = float)
x = np.zeros((len(A), 1), dtype = float)
y = np.zeros((len(A), 1), dtype = float)
r = np.zeros((len(A), 1), dtype = float)
y_e = np.zeros((len(A), 1), dtype = float)
err = np.zeros((len(A), 1), dtype = float)

L = np.zeros((len(A), len(A)), dtype = float)
U = A.copy()

solution = np.linalg.solve(A,b)

precision = 4

# =============================================
#                 RESOLUCIÓN           
# =============================================

# Conversión a float de n dígitos
def f(x):
    return float(np.format_float_scientific(x, precision = precision - 1))

# Conversión a float de n dígitos con doble precisión
def d_f(x):
    return float(np.format_float_scientific(x, precision = precision * 2 - 1))

# Conversión de array a float de n dígitos
def arr_f(x):
    return np.array(list(map(f, x)))

# Descomposición LU
for i in range(0, len(U)):

    for j in range(i+1, len(U)):
        m = f(U[j][i] / U[i][i])
        L[j][i] = m
        U[j] = arr_f(U[j] - arr_f(U[i] * m))

# Adición de la identidad a L
L = L + np.identity(len(A), dtype = float)

# Cálculo de y
for i in range(0, len(L)):
    sum = 0
    for j in range(0, i):
        sum = sum + f(L[i][j] * y[j])
    y[i] = f(f(b[i] - sum) / L[i][i])

# Cálculo de x
for i in reversed(range(0, len(U))):
    sum = 0
    for j in range(i+1, len(U)):
        sum = sum + f(U[i][j] * x[j])
    x[i] = f(f(y[i] - sum) / U[i][i])

for i in range(0, 100):
    valid = 1
    # Cálculo del residuo
    for i in range(0, len(A)):
        sum = 0
        for j in range(0, len(A)):
            sum = d_f(sum + d_f(A[i][j] * x[j]))
        r[i] = f(b[i] - sum)

    # Cálculo de y_e, para obtener el error
    for i in range(0, len(L)):
        sum = 0
        for j in range(0, i):
            sum = f(sum + f(L[i][j] * y_e[j]))
        y_e[i] = f(f(r[i] - sum) / L[i][i])

    # Cálculo del error
    for i in reversed(range(0, len(U))):
        sum = 0
        for j in range(i+1, len(U)):
            sum = f(sum + f(U[i][j] * err[j]))
        err[i] = f(f(y_e[i] - sum) / U[i][i])

    for i in range(0, len(x)):
        x[i] = f(x[i] + err[i])
        if abs(err[i]) > pow(10, -precision):
            valid = 0

    if valid:
        print("\nRefinado en", (i + 1), "iteraciones\n")
        break

print("A = \n", A)
print("L = \n", L)
print("U = \n", U)
print("\nb = \n", b)
print("\nr = \n", r)
print("err = \n", err)
#print("\nx = \n", solution)
print("\nSolución = \n", x, "\n")