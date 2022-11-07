# Ejercicio 11:
# Hallar un polinomio que interpole los siguientes datos utilizando la fórmula de Newton y una precisión de 4 dígitos:
#    x |  0     1      3
# f(x) | -1.201 0.8204 2.253

import numpy as np
import matplotlib.pyplot as plt

# =============================================
#             PARÁMETROS INICIALES            
# =============================================

xk = np.array([[0], [1], [3]], dtype = float)
yk = np.array([[-1.201], [0.8204], [2.253]], dtype = float)
c = np.zeros((len(xk), 1), dtype = float)

precision = 4

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

# Print del polinomio interpolante
pol = "P(x) = " + str(float(fm(c[0])))
for i in range(1, len(c)):
    pol = pol + " + "
    pol = pol + str(float(fm(c[i])))
    for j in range (0, i):
        pol = pol + "(x - " + str(float(fm(xk[j]))) + ")"
print(pol)

# Prints de los resultados:
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
