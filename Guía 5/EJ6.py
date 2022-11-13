# Ejercicio 6:
# Discretizar la siguiente ecuación diferencial con condiciones iniciales utilizando el método de Euler explícito:
# y' = y - a
# y(0) = 0
# a = 293
# Estimar los valores del intervalo (0, 6) con un paso de 0.3

import time
import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.append('././modules')
from initial_value_problems import euler_explicit

# =============================================
#             PARÁMETROS INICIALES            
# =============================================

inf = 0
sup = 6
h = 0.3
un = 313

a = 293

# Derivada de la función y
def f(y, t):
    return a - y

# Solución exacta
def fe(t):
    return -a * np.exp(-t) + 313 * np.exp(-t) + a

# =============================================
#                 RESOLUCIÓN           
# =============================================
startTime = time.perf_counter_ns()

x, y = euler_explicit(f, h, un, inf, sup)

endTime = time.perf_counter_ns()
# =============================================
#                 RESULTADOS           
# =============================================
# Prints
print("Tiempo de ejecución:", (endTime - startTime) / 1000000, "ms")
print("Resultados:")
print(np.matrix([x, y]).T)

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

ax.set_title('Método de Euler explícito, con h=%f' % h, loc='left')
ax.set(xlim=(start, end), ylim=(bottom, top))
ax.scatter(x, y)
ax.plot(xe, ye, linewidth=2.0)

plt.subplots_adjust(left=0.12, bottom=0.12, right=0.94)
plt.show()
