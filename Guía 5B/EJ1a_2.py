# Ejercicio 1a 2:
# Calcular f(3) interpolando los siguientes datos con la fórmula de Newton:
#    x | 2  4  5
# f(x) | 2  12 21

import numpy as np
import matplotlib.pyplot as plt

# =============================================
#             PARÁMETROS INICIALES            
# =============================================

xk = np.array([[ 2], [ 4], [5]], dtype = float)
yk = np.array([[ 2], [ 12], [21]], dtype = float)
c = np.zeros((3, 1), dtype = float)

# Base de funciones
def phi(n, x):
    y = 1
    for i in range (0, n):
        y = y * (x - xk[i])
    return y

# Fórmula de diferencias divididas
def dd(min, max):
    if min != max:
        return (dd(min + 1, max) - dd(min, max - 1)) / (xk[max] - xk[min])
    else:
        return yk[min]

# =============================================
#                 RESOLUCIÓN           
# =============================================

for i in range(0 ,len(c)):
    c[i] = dd(0, i)

# Polinomio interpolante
def pn(x):
    y = 0
    for i in range(0, len(c)):
        y = y + c[i] * phi(i, x)
    return y

# Prints de los resultados:
print("f(3) =\n", pn(3))
print("c =\n", c, "\n")

# Plots
plt.style.use('_mpl-gallery')
fig, ax = plt.subplots()

x_a = np.linspace(-5, 10, 500)
y_a = pn(x_a)

ax.scatter(xk, yk)
ax.plot(x_a, y_a, linewidth=2.0)

ax.set(xlim=(-2, 8), ylim=(-3, 24))
plt.subplots_adjust(left=0.12, bottom=0.12, right=0.94)
plt.show()
