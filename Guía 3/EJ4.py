# Algoritmo utilizado: Resolución de un sistema a partir de la descomposición LU

import numpy as np

# =============================================
#             PARÁMETROS INICIALES            
# =============================================

L = np.array([[ 1, 0, 0], [ -0.5, 1, 0], [ 0.5, 0.2, 1]], dtype = float)
U = np.array([[ 4, 1, 0], [ 0, 5/2, 1], [ 0, 0, 4/5]], dtype = float)
b = np.array([[ 1], [ -2], [ 7]], dtype = float)
P = np.array([[ 0, 1, 0], [ 0, 0, 1], [ 1, 0, 0]], dtype = float)

# =============================================
#                 RESOLUCIÓN           
# =============================================

x_a = np.linalg.solve(np.dot(L, U), np.dot(P, b))

A = np.dot(np.linalg.inv(P), np.dot(L, U))

x_b = np.linalg.solve(A, b)

print("L = \n", L)
print("U = \n", U)
print("P = \n", P)
print("b = \n", b)
print("\nA = \n", A)
print("\nSolución calculada para el ejercicio a = \n", x_a, "\n")
print("\nSolución calculada para el ejercicio b = \n", x_b, "\n")
