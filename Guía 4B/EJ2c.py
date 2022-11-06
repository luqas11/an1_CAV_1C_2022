# Ejercicio 2c:
# Aproximar los siguientes datos con la función f(x) = 1 + a1 * sen(2 * pi * x / 12) + a2 * cos(2 * pi * x / 12) utilizando el método de cuadrados mínimos:
#    x | 0   2   4   6   8   10
# f(x) | 1.0 1.6 1.4 0.6 0.2 0.8

import numpy as np
import matplotlib.pyplot as plt

# =============================================
#             PARÁMETROS INICIALES            
# =============================================

xk = np.array([[ 0], [ 2], [4], [6], [8], [10]], dtype = float)
yk = np.array([[ 1.0], [ 1.6], [1.4], [0.6], [0.2], [0.8]], dtype = float)
c = np.zeros((3, 1), dtype = float)
A = np.zeros((len(c), len(c)), dtype = float)
b = np.zeros((len(A), 1), dtype = float)
err = 0

# Base de funciones
def phi0(x):
    return 1
def phi1(x):
    return np.sin(2 * np.pi * x / 12)
def phi2(x):
    return np.cos(2 * np.pi * x / 12)

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

# Cálculo del error
for i in range(0, len(yk)):
    y_a = 0
    for j in range(0, len(c)):
        y_a = y_a + c[j] * phi[j](xk[i])
    err = err + (yk[i] - y_a)**2

# Prints de los resultados:
print("err =\n", err, "")
print("c =\n", c, "\n")

# Plots
plt.style.use('_mpl-gallery')
fig, ax = plt.subplots()

x_a = np.linspace(-20, 20, 100)
y_a = 0
for i in range(0, len(c)):
    y_a = y_a + c[i] * phi[i](x_a)

ax.scatter(xk, yk)
ax.plot(x_a, y_a, linewidth=2.0)

ax.set(xlim=(-2, 12), ylim=(0, 2))
plt.subplots_adjust(left=0.12, bottom=0.12, right=0.94)
plt.show()
