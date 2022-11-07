# Ejercicio 15:
# Hallar un polinomio que interpole la función f(x) = sen(x) utilizando el método de Hermite con los siguientes datos:
#    x | 0.30    0.32    0.33    0.35   
# f(x) | 0.29552 0.31457 0.32404 0.34290
#
#    x  | 0.30    0.32    0.33    0.35   
# f'(x) | 0.95534 0.00000 0.00000 0.93937
# Estimar el valor de f(0.34)

import numpy as np
import matplotlib.pyplot as plt

# =============================================
#             PARÁMETROS INICIALES            
# =============================================

xk = np.array([[0.30], [0.30], [0.32], [0.33], [0.35], [0.35]], dtype = float)
xk_1 = np.array([[0.95534], [0.95534], [0], [0],[0.93937], [0.93937]], dtype = float)
yk = np.array([[0.29552], [0.29552], [0.31457], [0.32404], [0.34290], [0.34290]], dtype = float)
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

# Función a interpolar
def f(x):
    return np.sin(x)

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
print("f(0.34) =\n", pn(0.34), "\n")
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
