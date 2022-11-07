# Ejercicio 12 2:
# Hallar un polinomio que interpole los siguientes datos utilizando el método de Lagrange en los nodos 0, 0.5 y 1:
#    x | 0.00   0.25   0.50   0.75   1.00
# f(x) | 1.0000 1.2840 1.6487 2.1170 2.7183
# Indicar el error cometido en cada nodo al interpolar.

import numpy as np
import matplotlib.pyplot as plt

# =============================================
#             PARÁMETROS INICIALES            
# =============================================

xk = np.array([[0.00], [0.25], [0.50], [0.75], [1.00]], dtype = float)
yk = np.array([[1.0000], [1.2840], [1.6487], [2.1170], [2.7183]], dtype = float)

xk_0 = np.array([[0.00], [0.50], [1.00]], dtype = float)
yk_0 = np.array([[1.0000], [1.6487], [2.7183]], dtype = float)

# =============================================
#                 RESOLUCIÓN           
# =============================================

# Polinomio interpolante
def pn(x):
    y = 0
    for i in range(0, len(xk_0)):
        w = yk_0[i]
        for j in range (0, len(xk_0)):
            if i != j:
                w = w * (x - xk_0[j]) / (xk_0[i] - xk_0[j])
        y =  y + w
    return y

# Cálculo del error
for i in range(0, len(yk)):
    err_n = (yk[i] - pn(xk[i]))**2
    print("err_n", i, "=", err_n)

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
