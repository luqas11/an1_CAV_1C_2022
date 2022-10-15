# Ejercicio 12:
# Aplicando el método de Gauss-Seidel, resolver el sistema de ecuaciones Ax=b.
# Realizar las modificaciones necesarias en el sistema para garantizar la convergencia del método y utilizar aritmética de punto flotante con 4 dígitos de precisión.

import numpy as np

# =============================================
#             PARÁMETROS INICIALES            
# =============================================

A = np.array([[ 3.210, 0.943, 1.020], [ 0.745, 0, -1.290], [ 0.875, -2.540, 0.247]], dtype = float)
b = np.array([[ 2.300], [ 0.740], [ 3.390]], dtype = float)
x = np.array([[ 1], [ 2], [ 3]], dtype = float)

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

permute(A, 1, 2)
permute(b, 1, 2)

print("--- Inicio del ciclo ---")
# Cálculo de la solución
for i in range(0, 100):
    print("\n", x)
    x1 = x.copy()
    for j in range(0, len(A)):
        sum = 0
        for k in range(0, len(A)):
            if j != k:
                sum = f(sum + f(A[j][k] * x[k]))
        x[j] = f(f(b[j] - sum) / A[j][j])
    if np.array_equal(x, x1):
        print("\n", x)
        print("\nResuelto en", (i + 1), "iteraciones\n")
        break
print("--- Fin del ciclo ---\n")

print("A = \n", A)
print("\nb = \n", b)
#print("\nx = \n", solution)
print("\nSolución = \n", x, "\n")
