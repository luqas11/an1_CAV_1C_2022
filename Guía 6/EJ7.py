# Ejercicio 7:
# Discretizar la siguiente ecuación diferencial con valores de contorno utilizando operadores de derivada de orden 2:
# (25 + 20x) * y'' + 20y' + 10 = 0
# y(0) = 40
# y'(1.5) = 0
# Estimar los valores del intervalo dado con un paso de 0.5

import time
import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.append('././modules')
from boundary_value_problems import pvc2

# =============================================
#             PARÁMETROS INICIALES            
# =============================================

inf = 0
sup = 1.5
h = 0.5

ui = 40

# Solución exacta
def fe(x):
    return 1/8 * (-4*x + 11 * np.log(4*x + 5) + 320 - 11*np.log(5))

# Función que genera los coeficientes para la construcción de la matriz tridiagonal
def fc(x):
    return np.array([[ (2.5 + 2*x)/h**2 - 1/h], [ -2*(2.5 + 2*x)/h**2], [ 1/h + (2.5 + 2*x)/h**2]], dtype = float)

# Función que genera los coeficientes para la construcción de la última fila de la matriz tridiagonal
def fcn(x):
    return np.array([[ 2*(2.5 + 2*x)/h**2], [ -2*(2.5 + 2*x)/h**2]], dtype = float)

# =============================================
#                 RESOLUCIÓN           
# =============================================
startTime = time.perf_counter_ns()

# Vector b a aplicar en la resolución del SEL de la matriz tridiagonal
n = int(np.round((sup - inf) / h))
b = np.zeros((n+1, 1), dtype = float)
b[0] = ui
for i in range(1, n+1):
    b[i] = -1

# Resolución del PVC
x, y = pvc2(fc, b, h, inf, sup, fcn)

endTime = time.perf_counter_ns()
# =============================================
#                 RESULTADOS           
# =============================================
# Prints
print("Tiempo de ejecución:", (endTime - startTime) / 1000000, "ms")
print("Resultados:")
print(np.matrix([x.reshape(-1), y.reshape(-1)]).T)

# Plots
margin = 0.2
window_size = 0.5

plt.style.use('_mpl-gallery')
fig, ax = plt.subplots(figsize=(window_size * 16, window_size * 9), tight_layout=True)

width = sup - inf
height = np.amax(y) - np.amin(y)

start = inf - width * margin
end = sup + width * margin
top = np.amax(y) + height * margin
bottom = np.amin(y) - height * margin

xe = np.linspace(inf - width * margin, sup + width * margin, 500)
ye = fe(xe)

ax.set_title('Operadores de orden 2, con h=%f' % h, loc='left')
ax.set(xlim=(start, end), ylim=(bottom, top))
ax.scatter(x, y)
ax.plot(xe, ye, linewidth=2.0)

plt.subplots_adjust(left=0.12, bottom=0.12, right=0.94)
plt.show()
