# Ejercicio 2b:
# Obtener la descomposición LU del sistema de ecuaciones Ax=b, aplicar pivoteo parcial y resolverlo.
# Utilizar aritmética de punto flotante con 4 dígitos de precisión y redondeo simétrico para todas las operaciones.

import numpy as np

# =============================================
#             PARÁMETROS INICIALES            
# =============================================

A = np.array([[ 3.241, 160], [ 10200, 1540]], dtype = float)
b = np.array([[ 163.2], [ 11740]], dtype = float)
x = np.zeros((len(A), 1), dtype = float)
y = np.zeros((len(A), 1), dtype = float)

L = np.zeros((len(A), len(A)), dtype = float)
U = A.copy()

P = np.identity(len(A), dtype = float)

solution = np.linalg.solve(A,b)

precision = 4

# =============================================
#                 RESOLUCIÓN           
# =============================================

# Conversión a float de n dígitos
def f(x):
    return float(np.format_float_scientific(x, precision = precision - 1))

# Conversión de array a float de n dígitos
def arr_f(x):
    return np.array(list(map(f, x)))

# Permutación de filas de matrices
def permute(M, first, second):
    temp = M[first].copy()
    M[first] = M[second].copy()
    M[second] = temp.copy()
    return M

# Descomposición LU+P
for i in range(0, len(U)):

    max_row = 0
    max_val = 0
    for j in range(i, len(U)):
        if abs(U[j][i]) > max_val:
            max_row = j
            max_val = abs(U[j][i])
            
    U = permute(U, max_row, i)
    P = permute(P, max_row, i)
    L = permute(L, max_row, i)

    for j in range(i+1, len(U)):
        m = f(U[j][i] / U[i][i])
        L[j][i] = m
        U[j] = arr_f(U[j] - arr_f(U[i] * m))

# Adición de la identidad a L
L = L + np.identity(len(A), dtype = float)

# Permutación de b
b = np.dot(P, b)

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

print("A = \n", A)
print("L = \n", L)
print("U = \n", U)
print("P = \n", P)
print("\nb = \n", b)
#print("\nx = \n", solution)
print("\nSolución = \n", x, "\n")
