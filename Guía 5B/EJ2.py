# Ejercicio 2:
# Calcular f(0) interpolando los siguientes datos con la fórmula de Newton:
#    x | 0.1   0.2   0.4   0.8
# f(x) | 64987 62055 56074 43609

import numpy as np
import matplotlib.pyplot as plt

# =============================================
#             PARÁMETROS INICIALES            
# =============================================

xk = np.array([[ 0.1], [ 0.2], [0.4], [0.8]], dtype = float)
yk = np.array([[ 64987], [ 62055], [56074], [43609]], dtype = float)
c = np.zeros((4, 1), dtype = float)

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
print("f(0) =\n", pn(0), "\n")
print("c =\n", c, "\n")

# Plots
plt.style.use('_mpl-gallery')
fig, ax = plt.subplots()

x_a = np.linspace(-2, 2, 500)
y_a = pn(x_a)

ax.scatter(xk, yk)
ax.plot(x_a, y_a, linewidth=2.0)

ax.set(xlim=(-0.1, 1), ylim=(40000, 70000))
plt.subplots_adjust(left=0.12, bottom=0.12, right=0.94)
plt.show()
