# Ejercicio 16:
# Hallar un polinomio que interpole los siguientes datos utilizando el método de Hermite:
#    x | 0.00 3.00  5.00   8.00   13.00
# f(x) | 0.00 67.50 114.90 186.90 297.90
#
#    x  | 0.00  3.00  5.00  8.00  13.00
# f'(x) | 22.50 23.10 24.00 22.20 21.60
# Estimar el valor de f(10) y f'(10)

import numpy as np
import matplotlib.pyplot as plt

# =============================================
#             PARÁMETROS INICIALES            
# =============================================

xk = np.array([[0.00], [0.00], [3.00], [3.00], [5.00], [5.00], [8.00], [8.00], [13.00], [13.00]], dtype = float)
yk = np.array([[0.00], [0.00], [67.50], [67.50], [114.90], [114.90], [186.90], [186.90], [297.90], [297.90]], dtype = float)
xk_1 = np.array([[22.50], [22.50], [23.10], [23.10], [24.00], [24.00], [22.20], [22.20], [21.60], [21.60]], dtype = float)
c = np.zeros((len(xk), 1), dtype = float)

# Base de funciones
def phi(n, x):
    y = 1
    for i in range (0, n):
        y = y * (x - xk[i])
    return y

# Fórmula de diferencias divididas
def dd(min, max):
    if min != max:
        if xk[min] == xk[max]:
            return xk_1[min]
        return (dd(min + 1, max) - dd(min, max - 1)) / (xk[max] - xk[min])
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
print("f(10) =\n", pn(10), "\n")
print("c =\n", c, "\n")

# Plots
plt.style.use('_mpl-gallery')
fig, ax = plt.subplots()

height = np.amax(yk) - np.amin(yk)
width = np.amax(xk) - np.amin(xk)
margin = 0.4

x_a = np.linspace(np.amin(xk) - width * margin, np.amax(xk) + width * margin, 500)
y_a = pn(x_a)

x_f = np.linspace(np.amin(xk) - width * margin, np.amax(xk) + width * margin, 500)
y_f = pn(x_f)

ax.scatter(xk, yk)
ax.plot(x_a, y_a, linewidth=2.0)
ax.plot(x_f, y_f, linewidth=2.0)

ax.set(xlim=(np.amin(xk) - width * margin, np.amax(xk) + width * margin), ylim=(np.amin(yk) - height * margin, np.amax(yk) + height * margin))
plt.subplots_adjust(left=0.12, bottom=0.12, right=0.94)
plt.show()
