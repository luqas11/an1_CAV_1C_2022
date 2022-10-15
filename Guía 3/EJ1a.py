# Ejercicio 1a:
# Obtener la descomposición LU del sistema de ecuaciones Ax=b y resolverlo.

import numpy as np

# =============================================
#             PARÁMETROS INICIALES            
# =============================================

np.set_printoptions(formatter={'float': '{: 0.3f}'.format})

A = np.array([[ 1,  2,  3, 4], [ 1,  4,  9, 16], [ 1,  8,  27, 64], [1, 16, 81, 256]], dtype = float)
b = np.array([[ 2], [ 10], [44], [190]], dtype = float)
x = np.zeros((len(A), 1), dtype = float)
y = np.zeros((len(A), 1), dtype = float)

L = np.identity(len(A), dtype = float)
U = A.copy()

solution = np.linalg.solve(A,b)

# =============================================
#                 RESOLUCIÓN           
# =============================================

# Descomposición LU
for i in range(0, len(U)):
    for j in range(i+1, len(U)):
        m = (U[j][i] / U[i][i])
        L[j][i] = m
        U[j] = U[j] - U[i] * m

# Cálculo de y
for i in range(0, len(L)):
    sum = 0
    for j in range(0, i):
        sum = sum + L[i][j] * y[j]
    y[i] = (b[i] - sum) / L[i][i]

# Cálculo de x
for i in reversed(range(0, len(U))):
    sum = 0
    for j in range(i+1, len(U)):
        sum = sum + U[i][j] * x[j]
    x[i] = (y[i] - sum) / U[i][i]
    
print("A = \n", A)
print("L = \n", L)
print("U = \n", U)
print("\nb = \n", b)
#print("\nx = \n", solution)
print("\nSolución = \n", x, "\n")
