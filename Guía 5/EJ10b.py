# Ejercicio 10b:
# Discretizar la siguiente ecuación diferencial con condiciones iniciales utilizando el método de Euler implícito:
# y'' + y' + y * y = t
# y(0) = 1
# y'(0) = 1
# Estimar los valores del intervalo (0, 10) con un paso de 2

import time
import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.append('././modules')
from initial_value_problems import euler_implicit_2
from linear_systems import gauss

# =============================================
#             PARÁMETROS INICIALES            
# =============================================

inf = 0
sup = 10
h = 2

un = 1
vn = 1

# Función que fabrica matrices y vector b del sistema a resolver
def fm(un, vn, tn):
    A = np.array([[ 1, -h], [  h, 1 + h]], dtype = float)
    b = np.array([[ un], [ vn + h * (tn + h)]], dtype = float)
    return A, b

# Función que fabrica funciones que resuelven SELs.
def fsel(A, b, xi):
    return gauss(A, b)

# Solución exacta
def fe(t):
    return np.exp(-t/2) * (2 * np.cos(t * np.sqrt(3)/2) + (2/np.sqrt(3)) * np.sin(t * np.sqrt(3)/2)) + t - 1

# =============================================
#                 RESOLUCIÓN           
# =============================================
startTime = time.perf_counter_ns()

x, y = euler_implicit_2(fm, fsel, h, un, vn, inf, sup)

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

ax.set_title('Método de Euler implícito, con h=%f' % h, loc='left')
ax.set(xlim=(start, end), ylim=(bottom, top))
ax.scatter(x, y)
ax.plot(xe, ye, linewidth=2.0)

plt.subplots_adjust(left=0.12, bottom=0.12, right=0.94)
plt.show()
