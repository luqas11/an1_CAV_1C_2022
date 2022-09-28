# Algoritmo utilizado: Eliminación Gaussiana con pivoteo parcial y sin descomposición LU

import numpy as np

# =============================================
#             PARÁMETROS INICIALES            
# =============================================

A = np.array([[ 0.003152, -15.28], [ -0.009413, 45.60]], dtype = float)
b = np.array([[ 14.98], [ -44.75]], dtype = float)
x = np.zeros((len(A), 1), dtype = float)

P = np.identity(len(A), dtype = float)

solution = np.linalg.solve(A,b)

# =============================================
#                 RESOLUCIÓN           
# =============================================

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
        b[j] = b[j] - b[i]  * (A[j][i] / A[i][i])
        A[j] = A[j] - A[i] * (A[j][i] / A[i][i])

# Cálculo de la solución
for i in reversed(range(0, len(A))):
    sum = 0
    for j in range(i+1, len(A)):
        sum = sum + A[i][j] * x[j]
    x[i] = (b[i] - sum) / A[i][i]
    
print("A = \n", A)
print("\nb = \n", b)
#print("\nx = \n", solution)
print("\nSolución = \n", x, "\n")