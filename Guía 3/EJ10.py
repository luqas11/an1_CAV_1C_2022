# Algoritmo utilizado: Métodos de Jacobi y Gauss-Seidel. NO CONVERGE, por tener radio espectral ≥ 1.

import numpy as np

# =============================================
#             PARÁMETROS INICIALES            
# =============================================

A = np.array([[ 1, 0, 0, 1], [ 1, 4, 0, -1], [ 1, 0, 1, 0], [ 0, 0, 1, 1]], dtype = float)
b = np.array([[ 2], [ 4], [ 2], [ 2]], dtype = float)
x_j = np.array([[ 1], [ 2], [3], [4]], dtype = float)
x1_j = np.zeros((len(A), 1), dtype = float)
x_gs = np.array([[ 1], [ 2], [3], [4]], dtype = float)

solution = np.linalg.solve(A,b)

# =============================================
#                 RESOLUCIÓN           
# =============================================

print("--- Inicio del ciclo ---")
for i in range(0, 10):    

    # Cálculo de la solución por Jacobi
    x1_j = x_j.copy()
    for j in range(0, len(A)):
        sum = 0
        for k in range(0, len(A)):
            if j != k:
                sum = sum + A[j][k] * x1_j[k]
        x_j[j] = (b[j] - sum) / A[j][j]

    # Cálculo de la solución por Gauss-Seidel  
    for j in range(0, len(A)):
        sum = 0
        for k in range(0, len(A)):
            if j != k:
                sum = sum + A[j][k] * x_gs[k]
        x_gs[j] = (b[j] - sum) / A[j][j]

    print("\n", x_j)
    print("\n", x_gs)
print("\n--- Fin del ciclo ---\n")

print("A = \n", A)
print("\nb = \n", b)
#print("\nx = \n", solution)
print("\nSolución J = \n", x_j, "\n")
print("\nSolución GS = \n", x_gs, "\n")
