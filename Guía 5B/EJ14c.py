# Ejercicio 14c:
# Calcular f(1920), f(1965) y f(2000) interpolando los siguientes datos con la fórmula de Newton:
#    x | 1930   1940   1950   1960   1970   1980
# f(x) | 123203 131669 150697 179323 203212 226505

import numpy as np
import matplotlib.pyplot as plt

# =============================================
#             PARÁMETROS INICIALES            
# =============================================

x_f = np.array([[1920], [1965], [2000]], dtype = float)
y_f = np.zeros((len(x_f), 1), dtype = float)
xk = np.array([[1930], [1940], [1950], [1960], [1970], [1980]], dtype = float)
yk = np.array([[123203], [131669], [150697], [179323], [203212], [226505]], dtype = float)
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

# Cálculo de las y interpoladas
for i in range(0, len(x_f)):
    y_f[i] = pn(x_f[i])
    print("x_f", x_f[i], "=>", pn(x_f[i]))

# Prints de los resultados:
print("c =\n", c, "\n")

# Plots
plt.style.use('_mpl-gallery')
fig, ax = plt.subplots()

height = np.amax(y_f) - np.amin(y_f)
width = np.amax(x_f) - np.amin(x_f)
margin = 0.4

x_a = np.linspace(np.amin(x_f) - width * margin, np.amax(x_f) + width * margin, 500)
y_a = pn(x_a)

ax.scatter(xk, yk)
ax.scatter(x_f, y_f)
ax.plot(x_a, y_a, linewidth=2.0)

ax.set(xlim=(np.amin(x_f) - width * margin, np.amax(x_f) + width * margin), ylim=(np.amin(y_f) - height * margin, np.amax(y_f) + height * margin))
plt.subplots_adjust(left=0.12, bottom=0.12, right=0.94)
plt.show()
