# Ejercicio 8:
# Discretizar el siguiente sistema de ecuaciones diferenciales con condiciones iniciales utilizando el método de Euler explícito:
# u' + u*v = 0
# v' + v^2 = 0
# u(0) = a
# v(0) = 1
# Estimar los valores del intervalo (0, 10) con un paso de 0.2

import time
import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.append('././modules')
from initial_value_problems import euler_explicit_2

# =============================================
#             PARÁMETROS INICIALES            
# =============================================

inf = 0
sup = 10
h = 0.2

a = 1

un = a
vn = 1

# Derivada de la función u
def fu(un, vn, tn):
    return un - h * (un * vn)

# Derivada de la función v
def fv(un, vn, tn):
    return vn - h * (vn**2)

# Solución exacta
def fe(t):
    return a / (t + 1)

# =============================================
#                 RESOLUCIÓN           
# =============================================
startTime = time.perf_counter_ns()

x, y = euler_explicit_2(fu, fv, h, un, vn, inf, sup)

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
windowSize = 0.5

plt.style.use('_mpl-gallery')
fig, ax = plt.subplots(figsize=(windowSize * 16, windowSize * 9), tight_layout=True)

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
