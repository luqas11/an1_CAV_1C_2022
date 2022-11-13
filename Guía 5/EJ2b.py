# Ejercicio 2b:
# Discretizar la siguiente ecuación diferencial con condiciones iniciales utilizando el método de Euler implícito:
# y' + e^y = 0
# y(0) = 0
# Estimar los valores del intervalo (0, 10) con un paso de 1

import time
import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.append('././modules')
from initial_value_problems import euler_implicit
from non_linear_equations import newton_raphson

# =============================================
#             PARÁMETROS INICIALES            
# =============================================

inf = 0
sup = 10
h = 1
un = 0

# Fábrica de ENLs a resolver en cada iteración, usando Newton-Raphson
def fnr(un):
    def gnr(un1):
        return un1 - (-un1 + un - h * np.exp(un1)) / (-1 - h * np.exp(un1))
    return newton_raphson(gnr, -0.75)

# Solución exacta
def fe(t):
    return -np.log(t + 1)

# =============================================
#                 RESOLUCIÓN           
# =============================================
startTime = time.perf_counter_ns()

x, y = euler_implicit(fnr, h, un, inf, sup)

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

xe = np.linspace(max(inf - width * margin, -0.5), sup + width * margin, 500)
ye = fe(xe)

ax.set_title('Método de Euler implícito, con h=%f' % h, loc='left')
ax.set(xlim=(start, end), ylim=(bottom, top))
ax.scatter(x, y)
ax.plot(xe, ye, linewidth=2.0)

plt.subplots_adjust(left=0.12, bottom=0.12, right=0.94)
plt.show()
