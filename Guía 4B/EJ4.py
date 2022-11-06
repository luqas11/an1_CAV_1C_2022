# Ejercicio 4:
# Aproximar los siguientes datos con una función exponencial utilizando el método de cuadrados mínimos:
#    x | 1  2  3  4
# f(x) | 7 11 17 27

import numpy as np
import matplotlib.pyplot as plt

# =============================================
#             PARÁMETROS INICIALES            
# =============================================

xk = np.array([[ 1], [ 2], [3], [4]], dtype = float)
yk = np.array([[ 7], [ 11], [17], [27]], dtype = float)
c = np.zeros((2, 1), dtype = float)
A = np.zeros((len(c), len(c)), dtype = float)
b = np.zeros((len(A), 1), dtype = float)
err = 0

# Base de funciones
def phi0(x):
    return 1
def phi1(x):
    return x

phi = [phi0, phi1]

# =============================================
#                 RESOLUCIÓN           
# =============================================

# Linealización
yk = np.log(yk)

# Cálculo de PIs discretos
def pi(f, g):
    sum = 0
    for i in range(len(xk)):
        sum = sum + f(xk[i]) * g(xk[i])
    return float(sum)

# Cálculo de PIs contra yk
def pi_y(f):
    sum = 0
    for i in range(len(xk)):
        sum = sum + f(xk[i]) * yk[i]
    return float(sum)

# Matriz de PIs
for i in range (0, len(A)):
    b[i] = pi_y(phi[i])
    for j in range (0, len(A)):
        A[i][j] = pi(phi[i], phi[j])

# Triangulación
for i in range(0, len(A)):
    for j in range(i+1, len(A)):
        b[j] = b[j] - b[i]  * (A[j][i] / A[i][i])
        A[j] = A[j] - A[i] * (A[j][i] / A[i][i])

# Cálculo de la solución
for i in reversed(range(0, len(A))):
    sum = 0
    for j in range(i, len(A)):
        sum = sum + A[i][j] * c[j]
    c[i] = (b[i] - sum) / A[i][i]

# Deslinealización
yk = np.exp(yk)
c[0] = np.exp(c[0])

# Cálculo del error
for i in range(0, len(yk)):
    y_a = c[0] * np.exp(c[1] * xk[i])
    err = err + (yk[i] - y_a)**2

# Prints de los resultados:
print("err =\n", err, "")
print("c =\n", c, "\n")

# Plots
plt.style.use('_mpl-gallery')
fig, ax = plt.subplots()

x_a = np.linspace(0, 50, 500)
y_a = c[0] * np.exp(c[1] * x_a)

ax.scatter(xk, yk)
ax.plot(x_a, y_a, linewidth=2.0)

ax.set(xlim=(0, 5), ylim=(5, 30))
plt.subplots_adjust(left=0.12, bottom=0.12, right=0.94)
plt.show()
