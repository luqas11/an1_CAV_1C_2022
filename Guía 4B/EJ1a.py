# Ejercicio 1a:
# Aproximar la función y = e^x con una recta utilizando el método de cuadrados mínimos sobre los puntos -1, -0.5, 0, 0.5 y 1.

import numpy as np
import matplotlib.pyplot as plt

# =============================================
#             PARÁMETROS INICIALES            
# =============================================

xk = np.array([[ -1], [ -0.5], [0], [0.5], [1]], dtype = float)
yk = np.zeros((len(xk), 1), dtype = float)
c = np.zeros((2, 1), dtype = float)
A = np.zeros((len(c), len(c)), dtype = float)
b = np.zeros((len(A), 1), dtype = float)

# Base de funciones
def phi0(x):
    return 1
def phi1(x):
    return x

# Función a aproximar
def f(x):
    return np.exp(x)

# Asignación de los valores de y
for i in range(0, len(xk)):
    yk[i] = f(xk[i])

phi = [phi0, phi1]

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
    b[i] = pi(f, phi[i])
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

# Prints de los resultados:
print(c, "\n")

# Plots
plt.style.use('_mpl-gallery')
fig, ax = plt.subplots()

x_f = np.linspace(-10, 10, 100)
y_f = f(x_f)

x_a = np.linspace(-10, 10, 100)
y_a = 0
for i in range(0, len(c)):
    y_a = y_a + c[i] * phi[i](x_a)

print(c[0] * phi0(1) + c[1] * phi1(1))

ax.scatter(xk, yk)
ax.plot(x_f, y_f, linewidth=2.0)
ax.plot(x_a, y_a, linewidth=2.0)

ax.set(xlim=(-3, 3), ylim=(-1, 5))
plt.subplots_adjust(left=0.12, bottom=0.12, right=0.94)
plt.show()
