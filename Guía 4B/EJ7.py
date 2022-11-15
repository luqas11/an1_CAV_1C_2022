# Ejercicio 7:
# Obtener la matriz de productos internos que requiere el método cuadrados mínimos para aproximar mediante una parábola los siguientes datos:
# x | -2  -1  0  1  2

import numpy as np

# =============================================
#             PARÁMETROS INICIALES            
# =============================================

xk = np.array([[-2], [-1], [0], [1], [2]], dtype = float)
c = np.zeros((3, 1), dtype = float)
A = np.zeros((len(c), len(c)), dtype = float)

# Base de funciones
def phi0(x):
    return 1
def phi1(x):
    return x
def phi2(x):
    return x**2

phi = [phi0, phi1, phi2]

# =============================================
#                 RESOLUCIÓN           
# =============================================

# Cálculo de PIs discretos
def pi(f, g):
    sum = 0
    for i in range(len(xk)):
        sum = sum + f(xk[i]) * g(xk[i])
    return float(sum)

# Matriz de PIs
for i in range (0, len(A)):
    for j in range (0, len(A)):
        A[i][j] = pi(phi[i], phi[j])

print(A)
