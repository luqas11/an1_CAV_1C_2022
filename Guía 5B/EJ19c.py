# Ejercicio 19c:
# Hallar un polinomio que interpole la función f(x) = e^x aplicando el método de Lagrange con los siguientes valores:
#    x | 0     1.0     2.0
# f(x) | 1.00000 2.71828 7.38906
# Estimar el valor de f(0.75) y f(0.25)

import numpy as np
import matplotlib.pyplot as plt

# =============================================
#             PARÁMETROS INICIALES            
# =============================================

xk = np.array([[0.0], [1.0], [2.0]], dtype = float)
yk = np.array([[1.00000], [2.71828], [7.38906]], dtype = float)

# Función a interpolar
def f(x):
    return np.exp(x)
    
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

# Prints de los resultados
print("f(0.25) =\n", pn(0.25))
print("f(0.75) =\n", pn(0.75), "\n")

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
