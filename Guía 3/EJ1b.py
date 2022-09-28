# Ejercicio 1b:
# Aplicando el método de eliminación de Gauss, resolver el sistema de ecuaciones Ax=b.

import numpy as np

# =============================================
#             PARÁMETROS INICIALES            
# =============================================

np.set_printoptions(formatter={'float': '{: 0.3f}'.format})

A = np.array([[ 1,  2,  3, 4], [ 1,  4,  9, 16], [ 1,  8,  27, 64], [1, 16, 81, 256]], dtype = float)
b = np.array([[ 2], [ 10], [44], [190]], dtype = float)
x = np.zeros((len(A), 1), dtype = float)

solution = np.linalg.solve(A,b)

# =============================================
#                 RESOLUCIÓN           
# =============================================

# Triangulación
for i in range(0, len(A)):
    for j in range(i+1, len(A)):
        b[j] = b[j] - b[i]  * (A[j][i] / A[i][i])
        A[j] = A[j] - A[i] * (A[j][i] / A[i][i])

# Cálculo de la solución
for i in reversed(range(0, len(A))):
    sum = 0
    for j in range(i, len(A)):
        sum = sum + A[i][j] * x[j]
    x[i] = (b[i] - sum) / A[i][i]
    
print("A = \n", A)
print("\nb = \n", b)
#print("\nx = \n", solution)
print("\nSolución = \n", x, "\n")
