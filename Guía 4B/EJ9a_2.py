# Ejercicio 9a 2:
# Aproximar la función f(x) = x^2 - 2*x + 3 en el intervalo [0, 1] mediante un polinomio de grado 2.

import numpy as np
import matplotlib.pyplot as plt

# =============================================
#             PARÁMETROS INICIALES            
# =============================================

c = np.zeros((3, 1), dtype = float)
A = np.zeros((len(c), len(c)), dtype = float)
b = np.zeros((len(A), 1), dtype = float)

# Base de funciones
def phi0(x):
    return 1
def phi1(x):
    return x
def phi2(x):
    return x**2

# Funciones resultantes de los PIs
phi0f = 7/3
phi1f = 13/12
phi2f = 7/10

# Función a aproximar
def f(x):
    return x**2 - 2*x + 3

phi = [phi0, phi1, phi2]
pi = np.array([[1, 1/2, 1/3], [1/2, 1/3, 1/4], [1/3, 1/4, 1/5]], dtype = float)
pi_y = np.array([[phi0f], [phi1f], [phi2f]], dtype = float)

# =============================================
#                 RESOLUCIÓN           
# =============================================

# Asignación de PIs
b = pi_y.copy()
A = pi.copy()

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
print("c =\n", c, "\n")

# Plots
plt.style.use('_mpl-gallery')
fig, ax = plt.subplots()

x_a = np.linspace(-5, 5, 500)
y_a = 0
for i in range(0, len(c)):
    y_a = y_a + c[i] * phi[i](x_a)

x_f = np.linspace(-5, 5, 500)
y_f = f(x_f)

ax.plot(x_f, y_f, linewidth=2.0)
ax.plot(x_a, y_a, linewidth=2.0)

ax.set(xlim=(-0.5, 1.5), ylim=(0, 6))
plt.subplots_adjust(left=0.12, bottom=0.12, right=0.94)
plt.show()
