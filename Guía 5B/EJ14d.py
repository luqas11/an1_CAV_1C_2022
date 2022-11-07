# Ejercicio 14d:
# Hallar un polinomio que interpole de los siguientes datos utilizando el método de Newton:
#    x | 1930   1940   1950   1960   1970   1980   1920
# f(x) | 123203 131669 150697 179323 203212 226505 105711
# Indicar el error cometido en los nodos 1965 y 2000 al interpolar.

import numpy as np
import matplotlib.pyplot as plt

# =============================================
#             PARÁMETROS INICIALES            
# =============================================

x_f = np.array([[1920], [1965], [2000]], dtype = float)
y_f = np.zeros((len(x_f), 1), dtype = float)
xk = np.array([[1930], [1940], [1950], [1960], [1970], [1980], [1920]], dtype = float)
yk = np.array([[123203], [131669], [150697], [179323], [203212], [226505], [105711]], dtype = float)
c = np.zeros((len(xk) - 1, 1), dtype = float)
c_err = 0

precision = 5
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

# Asignación de coeficientes
for i in range(0 ,len(c)):
    c[i] = dd(0, i)
c_err = dd(0, len(c))

# Polinomio interpolante
def pn(x):
    y = 0
    for i in range(0, len(c)):
        y = y + c[i] * phi(i, x)
    return y

# Cálculo de las y interpoladas
for i in range(0, len(x_f)):
    y_f[i] = pn(x_f[i])

# Polinomio del error
def p_err(x):
    return c_err * phi(len(c), x)

# Prints de los resultados:
def error_print(x):
    print("pn(", x, ") =", fm(pn(x)))
    print("err(", x, ") =", fm(p_err(x)), "\n")

error_print(1920)
error_print(1965)
error_print(2000)
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
