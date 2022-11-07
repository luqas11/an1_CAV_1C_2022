# Ejercicio 14a:
# Hallar un polinomio que interpole los siguientes datos utilizando el método de Lagrange:
#    x | 1930   1940   1950   1960   1970   1980
# f(x) | 123203 131669 150697 179323 203212 226505

import numpy as np
import matplotlib.pyplot as plt

# =============================================
#             PARÁMETROS INICIALES            
# =============================================

xk = np.array([[1930], [1940], [1950], [1960], [1970], [1980]], dtype = float)
yk = np.array([[123203], [131669], [150697], [179323], [203212], [226505]], dtype = float)

# =============================================
#                 RESOLUCIÓN           
# =============================================

# Polinomio interpolante
def pn(x):
    y = 0
    for i in range(0, len(xk)):
        w = yk[i]
        for j in range (0, len(xk)):
            if i != j:
                w = w * (x - xk[j]) / (xk[i] - xk[j])
        y =  y + w
    return y

# Plots
plt.style.use('_mpl-gallery')
fig, ax = plt.subplots()

height = np.amax(yk) - np.amin(yk)
width = np.amax(xk) - np.amin(xk)
margin = 0.4

x_a = np.linspace(np.amin(xk) - width * margin, np.amax(xk) + width * margin, 500)
y_a = np.zeros((len(x_a), 1), dtype = float)
for i in range(0, len(x_a)):
    y_a[i] = pn(x_a[i])

ax.scatter(xk, yk)
ax.plot(x_a, y_a, linewidth=2.0)

ax.set(xlim=(np.amin(xk) - width * margin, np.amax(xk) + width * margin), ylim=(np.amin(yk) - height * margin, np.amax(yk) + height * margin))
plt.subplots_adjust(left=0.12, bottom=0.12, right=0.94)
plt.show()
