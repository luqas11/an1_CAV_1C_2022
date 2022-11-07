# Ejercicio 15:
# Hallar un polinomio que interpole la función f(x) = sen^2(x) utilizando el método de Hermite en los nodos 0, pi/2 y pi.
# Utilizar aritmética de 5 dígitos de precisión y obtener el error cometido por la interpolación en los nodos 0.2 y 0.5.

import numpy as np
import matplotlib.pyplot as plt

# =============================================
#             PARÁMETROS INICIALES            
# =============================================

xk = np.array([[0], [0], [np.pi/2], [np.pi], [np.pi], [5 * np.pi/4]], dtype = float)
yk = np.zeros((len(xk), 1), dtype = float)
xk_1 = np.array([[0], [0], [0], [0], [0]], dtype = float)
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
        if xk[min] == xk[max]:
            return xk_1[min]
        return (dd(min + 1, max) - dd(min, max - 1)) / (xk[max] - xk[min])
    return yk[min]

# Función a interpolar
def f(x):
    return (np.sin(x))**2

# Asignación de y
for i in range(0, len(xk)):
    yk[i] = f(xk[i])

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

# Polinomio del error
def p_err(x):
    return c_err * phi(len(c), x)

# Prints de los resultados:
def error_print(x):
    print("f(", x, ") =", fm(f(x)))
    print("pn(", x, ") =", fm(pn(x)))
    print("err(", x, ") =", fm(p_err(x)), "\n")

error_print(0.2)
error_print(0.5)
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
y_f = f(x_f)

ax.scatter(xk, yk)
ax.plot(x_a, y_a, linewidth=2.0)
ax.plot(x_f, y_f, linewidth=2.0)

ax.set(xlim=(np.amin(xk) - width * margin, np.amax(xk) + width * margin), ylim=(np.amin(yk) - height * margin, np.amax(yk) + height * margin))
plt.subplots_adjust(left=0.12, bottom=0.12, right=0.94)
plt.show()
