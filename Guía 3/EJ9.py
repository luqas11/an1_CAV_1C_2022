# Ejercicio 9:
# Aplicando el método de Gauss-Seidel, resolver el sistema de ecuaciones Ax=b.
# Iterar hasta alcanzar un error absoluto menor a 0.02 en las tres variables del sistema.

import numpy as np

# =============================================
#             PARÁMETROS INICIALES            
# =============================================

A = np.array([[ 10, 2, 6], [ 1, 10, 4], [ 2, -7, -10]], dtype = float)
b = np.array([[ 28], [ 7], [ -17]], dtype = float)
x = np.array([[ 1], [ 2], [3]], dtype = float)

solution = np.linalg.solve(A,b)

MAX_ERR = 0.02

# =============================================
#                 RESOLUCIÓN           
# =============================================

print("--- Inicio del ciclo ---")
# Cálculo de la solución
for i in range(0, 100):
    print("\n", x)
    valid = 1
      
    for j in range(0, len(A)):
        sum = 0
        for k in range(0, len(A)):
            if j != k:
                sum = sum + A[j][k] * x[k]

        val = (b[j] - sum) / A[j][j]
        if abs(x[j] - val) > MAX_ERR:
            valid = 0
        x[j] = val
        
    if valid:
        print("\nResuelto en", (i + 1), "iteraciones\n")
        print(x, "\n")
        break
print("--- Fin del ciclo ---\n")

print("A = \n", A)
print("\nb = \n", b)
#print("\nx = \n", solution)
print("\nSolución = \n", x, "\n")
