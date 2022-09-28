# Algoritmo utilizado: Método de eliminación de Gauss y método de Gauss-Seidel

import numpy as np

# =============================================
#             PARÁMETROS INICIALES            
# =============================================

A = np.array([[ 2, -1, 0, 0], [ -1, 2, -1, 0], [ 0, -1, 2, -1], [ 0, 0, -1, 2]], dtype = float)
b = np.array([[ 1], [ 1], [ 1], [ 1]], dtype = float)
x_g = np.zeros((len(A), 1), dtype = float)
x_gs = np.array([[ 1], [ 2], [3], [4]], dtype = float)

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
        sum = sum + A[i][j] * x_g[j]
    x_g[i] = (b[i] - sum) / A[i][i]

print("--- Inicio del ciclo ---")
for i in range(0, 5):    

    print("\n", x_gs)
    # Cálculo de la solución por Gauss-Seidel  
    for j in range(0, len(A)):
        sum = 0
        for k in range(0, len(A)):
            if j != k:
                sum = sum + A[j][k] * x_gs[k]
        x_gs[j] = (b[j] - sum) / A[j][j]

print("\n", x_gs)
print("\nResuelto en 6 iteraciones\n")
print("--- Fin del ciclo ---\n")
        
print("A = \n", A)
print("\nb = \n", b)
#print("\nx = \n", solution)
print("\nSolución por Gauss = \n", x_g, "\n")
print("\nSolución por Gauss-Seidel = \n", x_gs, "\n")
