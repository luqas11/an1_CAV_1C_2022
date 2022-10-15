# Ejercicio 8:
# Aplicando el método de Jacobi, resolver el sistema de ecuaciones Ax=b.
# Realizar las modificaciones necesarias en el sistema para garantizar la convergencia del método.

import numpy as np

# =============================================
#             PARÁMETROS INICIALES            
# =============================================

A = np.array([[ 0.01235, -2.387], [ 5.462, 0.008406]], dtype = float)
b = np.array([[ 1.370], [ 10.85]], dtype = float)
x = np.array([[ 1], [ 2]], dtype = float)
x1 = np.zeros((len(A), 1), dtype = float)

solution = np.linalg.solve(A,b)

precision = 5

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

permute(A, 0, 1)
permute(b, 0, 1)

print("--- Inicio del ciclo ---")
# Cálculo de la solución
for i in range(0, 100):
    print("\n", x)
    x1 = x.copy()
    for j in range(0, len(A)):
        sum = 0
        for k in range(0, len(A)):
            if j != k:
                sum = f(sum + f(A[j][k] * x1[k]))
        x[j] = f(f(b[j] - sum) / A[j][j])
    if np.array_equal(x, x1):
        print("\nResuelto en", (i + 1), "iteraciones\n")
        print(x, "\n")
        break
print("--- Fin del ciclo ---\n")

print("A = \n", A)
print("\nb = \n", b)
#print("\nx = \n", solution)
print("\nSolución = \n", x, "\n")
