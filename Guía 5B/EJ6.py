# Ejercicio 6:
# Calcular f(1.01) y f(1.28) con tres dígitos significativos interpolando los siguientes datos con la fórmula de Newton:
#    x | 1.00    1.05    1.10    1.15    1.20    1.25    1.30
# f(x) | 1.00000 1.02470 1.04881 1.07238 1.09544 1.11803 1.14017

import numpy as np
import matplotlib.pyplot as plt

# =============================================
#             PARÁMETROS INICIALES            
# =============================================

xk = np.array([[ 1.00], [ 1.05], [1.10], [1.15], [1.20], [1.25], [1.30]], dtype = float)
yk = np.array([[ 1.00000], [ 1.02470], [1.04881], [1.07238], [1.09544], [1.11803], [1.14017]], dtype = float)
c = np.zeros((7, 1), dtype = float)

precision = 3

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

# Conversión a float de n dígitos
def fm(x):
    return float(np.format_float_scientific(x, precision = precision - 1))

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
print("f(1.01) =\n", fm(pn(1.01)))
print("f(1.28) =\n", fm(pn(1.28)), "\n")
print("c =\n", c, "\n")

# Plots
plt.style.use('_mpl-gallery')
fig, ax = plt.subplots()

height = np.amax(yk) - np.amin(yk)
width = np.amax(xk) - np.amin(xk)
margin = 0.4

x_a = np.linspace(np.amin(xk) - width * margin, np.amax(xk) + width * margin, 500)
y_a = pn(x_a)

ax.scatter(xk, yk)
ax.plot(x_a, y_a, linewidth=2.0)

ax.set(xlim=(np.amin(xk) - width * margin, np.amax(xk) + width * margin), ylim=(np.amin(yk) - height * margin, np.amax(yk) + height * margin))
plt.subplots_adjust(left=0.12, bottom=0.12, right=0.94)
plt.show()
