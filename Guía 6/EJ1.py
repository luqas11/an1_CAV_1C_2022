# Ejercicio 1:
# Discretizar la siguiente ecuación diferencial con valores de contorno utilizando operadores de derivada de orden 2:
# y'' + y = 0
# y(0) = 1
# y(pi/2) = 0
# Estimar los valores del intervalo dado con un paso de pi/8

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
sup = np.pi/2
h = np.pi/8

ui = 1
uf = 0

# Solución exacta
def fe(t):
    return np.cos(t)

# Función que genera los coeficientes para la construcción de la matriz tridiagonal
def fc(x):
    return np.array([[ 1/h**2], [ 1 - 2/h**2], [ 1/h**2]], dtype = float)

# =============================================
#                 RESOLUCIÓN           
# =============================================
startTime = time.perf_counter_ns()

# Vector b a aplicar en la resolución del SEL de la matriz tridiagonal
n = int(np.round((sup - inf) / h))
b = np.zeros((n+1, 1), dtype = float)
b[0] = ui
b[n] = uf

# Resolución del PVC
x, y = pvc2(fc, b, h, inf, sup)

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
