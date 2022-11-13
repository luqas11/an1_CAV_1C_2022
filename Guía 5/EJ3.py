# Ejercicio 3:
# Discretizar la siguiente ecuación diferencial con condiciones iniciales utilizando el método de Runge Kutta 2:
# y'' = a
# y(0) = 0
# y'(0) = b
# Estimar los valores del intervalo (0, 10) con un paso de 1

import time
import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.append('././modules')
from initial_value_problems import rk2_2

# =============================================
#             PARÁMETROS INICIALES            
# =============================================

inf = 0
sup = 10
h = 1

a = 1
b = 1

un = 0
vn = b

# Derivada de la función u
def fu(u, v, t):
    return v

# Derivada de la función v
def fv(u, v, t):
    return a

# Solución exacta
def fe(t):
    return a * (t**2) / 2 + b * t

# =============================================
#                 RESOLUCIÓN           
# =============================================
startTime = time.perf_counter_ns()

x, y = rk2_2(fu, fv, h, un, vn, inf, sup)

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

ax.set_title('Método de Runge Kutta 2, con h=%f' % h, loc='left')
ax.set(xlim=(start, end), ylim=(bottom, top))
ax.scatter(x, y)
ax.plot(xe, ye, linewidth=2.0)

plt.subplots_adjust(left=0.12, bottom=0.12, right=0.94)
plt.show()
