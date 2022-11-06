# Ejercicio 6e 1:
# Aproximar los siguientes datos utilizando una función potencial y aplicando el método de cuadrados mínimos:
#    x | 4.0    4.2    4.5    4.7    5.1    5.5    5.9    6.3    6.8    7.1
# f(x) | 102.56 113.18 130.11 142.05 167.53 195.14 224.87 256.73 299.50 326.72
# Indicar el error cometido en la aproximación.

import numpy as np
import matplotlib.pyplot as plt

# =============================================
#             PARÁMETROS INICIALES            
# =============================================

xk = np.array([[4.0], [4.2], [4.5], [4.7], [5.1], [5.5], [5.9], [6.3], [6.8], [7.1]], dtype = float)
yk = np.array([[102.56], [113.18], [130.11], [142.05], [167.53], [195.14], [224.87], [256.73], [299.50], [326.72]], dtype = float)
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
xk = np.log(xk)

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
xk = np.exp(xk)
c[0] = np.exp(c[0])

# Cálculo del error
for i in range(0, len(yk)):
    y_a = c[0] * np.power(xk[i], c[1])
    err = err + (yk[i] - y_a)**2

# Prints de los resultados:
print("err =\n", err, "")
print("c =\n", c, "\n")

# Plots
plt.style.use('_mpl-gallery')
fig, ax = plt.subplots()

x_a = np.linspace(0, 50, 500)
y_a = c[0] * np.power(x_a, c[1])

ax.scatter(xk, yk)
ax.plot(x_a, y_a, linewidth=2.0)

ax.set(xlim=(3, 8), ylim=(80, 340))
plt.subplots_adjust(left=0.12, bottom=0.12, right=0.94)
plt.show()
