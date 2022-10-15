# Ejercicio 3a:
# Aplicando el método de eliminación de Gauss y realizando pivoteo parcial, resolver el sistema de ecuaciones Ax=b.
# Utilizar aritmética de punto flotante con 3 dígitos de precisión.

import numpy as np

# =============================================
#             PARÁMETROS INICIALES            
# =============================================

A = np.array([[ 2.15, -0.924, -1.29], [ -4.12, 2.29, 0.294], [ 1.01, 0.872, -3.25]], dtype = float)
b = np.array([[ 1.22], [ -3.56], [ -0.972]], dtype = float)
x = np.zeros((len(A), 1), dtype = float)

P = np.identity(len(A), dtype = float)

solution = np.linalg.solve(A,b)

precision = 3

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

# Triangulación
for i in range(0, len(A)):

    max_row = 0
    max_val = 0
    for j in range(i, len(A)):
        if abs(A[j][i]) > max_val:
            max_row = j
            max_val = abs(A[j][i])

    A = permute(A, max_row, i)
    b = permute(b, max_row, i)

    for j in range(i+1, len(A)):
        b[j] = arr_f(b[j] - arr_f(b[i]  * f(A[j][i] / A[i][i])))
        A[j] = arr_f(A[j] - arr_f(A[i] * f(A[j][i] / A[i][i])))

# Cálculo de la solución
for i in reversed(range(0, len(A))):
    sum = 0
    for j in range(i+1, len(A)):
        sum = f(sum + f(A[i][j] * x[j]))
    x[i] = f(f(b[i] - sum) / A[i][i])
    
print("A = \n", A)
print("\nb = \n", b)
#print("\nx = \n", solution)
print("\nSolución calculada = \n", x, "\n")
