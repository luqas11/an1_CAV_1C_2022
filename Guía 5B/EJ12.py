# Ejercicio 12 1:
# Aproximar los siguientes datos utilizando una función polinómica de grado 2 y aplicando el método de cuadrados mínimos:
#    x | 0.00   0.25   0.50   0.75   1.00
# f(x) | 1.0000 1.2840 1.6487 2.1170 2.7183
# Indicar el error cometido en la aproximación.

import numpy as np
import matplotlib.pyplot as plt

# =============================================
#             PARÁMETROS INICIALES            
# =============================================

xk = np.array([[0.00], [0.25], [0.50], [0.75], [1.00]], dtype = float)
yk = np.array([[1.0000], [1.2840], [1.6487], [2.1170], [2.7183]], dtype = float)
c = np.zeros((3, 1), dtype = float)
A = np.zeros((len(c), len(c)), dtype = float)
b = np.zeros((len(A), 1), dtype = float)
err = 0

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
    err_n = (yk[i] - y_a)**2
    print("err_n", i, "=", err_n)
    err = err + err_n

# Prints de los resultados:
print("\nerr =\n", err, "")
print("c =\n", c, "\n")

# Plots
plt.style.use('_mpl-gallery')
fig, ax = plt.subplots()

height = np.amax(yk) - np.amin(yk)
width = np.amax(xk) - np.amin(xk)
margin = 0.4

x_a = np.linspace(np.amin(xk) - width * margin, np.amax(xk) + width * margin, 500)
y_a = 0
for i in range(0, len(c)):
    y_a = y_a + c[i] * phi[i](x_a)

ax.scatter(xk, yk)
ax.plot(x_a, y_a, linewidth=2.0)

ax.set(xlim=(np.amin(xk) - width * margin, np.amax(xk) + width * margin), ylim=(np.amin(yk) - height * margin, np.amax(yk) + height * margin))
plt.subplots_adjust(left=0.12, bottom=0.12, right=0.94)
plt.show()
