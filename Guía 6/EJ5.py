# Ejercicio 5:
# La ecuación de flexión a lo largo de una viga que sostiene un determinado peso está dada por la función V(x) que es solución de la ecuación diferencial V'' = (L * 5x - 5x^2) * (1 + V'^2)^(3/2) (donde L es la longitud de la viga).
# La viga mide 1m y en sus extremos la flexión es nula.
# Estimar la longitud de la flexión en la viga, discretizando la ecuación diferencial mediante operadores de derivada de orden 2 y utilizando un paso de (1/3)m.

# Interpretación del enunciado:
# y'' = (5x - 5x^2) * (1 + y'^2)^(3/2)
# y(0) = 0
# y(1) = 0

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
sup = 1
h = (1/3)

ui = 0
uf = 0

# Solución aproximada, despreciando el término (1 + y'^2)^(3/2)
def fe(x):
    return -5/12 * (x**4 - 2*x**3 + x)

# Función que genera los coeficientes para la construcción de la matriz tridiagonal
def fc(x):
    return np.array([[ 1/h**2], [ -2/h**2], [ 1/h**2]], dtype = float)

# =============================================
#                 RESOLUCIÓN           
# =============================================
startTime = time.perf_counter_ns()

# Vector b a aplicar en la resolución del SEL de la matriz tridiagonal
n = int(np.round((sup - inf) / h))
b = np.zeros((n+1, 1), dtype = float)
b[0] = ui
for i in range(1, n):
    b[i] = 5*i*h - 5 * (i*h)**2
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
