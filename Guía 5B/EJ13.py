# Ejercicio 13:
# Hallar un polinomio que interpole la función f(x) = 1/x en los nodos 2, 2.5 y 4 aplicando el método de Lagrange.
# Indicar el error cometido en los nodos 0.5 y 1/3 al interpolar.

import numpy as np
import matplotlib.pyplot as plt

# =============================================
#             PARÁMETROS INICIALES            
# =============================================

xk = np.array([[2], [2.5], [4]], dtype = float)
yk = np.array([[1/2], [2/5], [1/4]], dtype = float)

x_err = np.array([[1/2], [1/3]], dtype = float)

# Función a interpolar
def f(x):
    return 1/x
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

# Cálculo del error
for i in range(0, len(x_err)):
    err_n = (f(x_err[i]) - pn(x_err[i]))**2
    print("err_n", x_err[i], "=>", err_n)

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

x_f = np.linspace(np.amin(xk) - width * margin, np.amax(xk) + width * margin, 500)
y_f = f(x_f)

ax.scatter(xk, yk)
ax.plot(x_a, y_a, linewidth=2.0)
ax.plot(x_f, y_f, linewidth=2.0)

ax.set(xlim=(np.amin(xk) - width * margin, np.amax(xk) + width * margin), ylim=(np.amin(yk) - height * margin, np.amax(yk) + height * margin))
plt.subplots_adjust(left=0.12, bottom=0.12, right=0.94)
plt.show()
