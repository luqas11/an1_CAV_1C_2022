# Ejercicio 4:
# Discretizar la siguiente ecuación diferencial con condiciones iniciales utilizando el método de Euler implícito:
# y'' + a*y = t^2
# y(0) = 1
# y'(0) = 0
# a > 0
# Estimar los valores del intervalo (0, 5) con un paso de 0.5

import time
import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.append('././modules')
from initial_value_problems import euler_implicit_2
from linear_systems import jacobi

# =============================================
#             PARÁMETROS INICIALES            
# =============================================

inf = 0
sup = 5
h = 0.5

a = 1

un = 1
vn = 0

# Función que fabrica matrices y vector b del sistema a resolver
def fm(un, vn, t):
    A = np.array([[ 1, -h], [ h * a, 1]], dtype = float)
    b = np.array([[ un], [ vn + h * ((t + h)**2)]], dtype = float)
    return A, b

# Función que fabrica funciones que resuelven SELs.
def fsel(A, b, xi):
    return jacobi(A, b, xi)

# Solución exacta
def fe(t):
    return (t**2)/a + (1 + 2/(a**2)) * np.cos(np.sqrt(a) * t) - 2/(a**2)

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

ax.set_title('Método de Euler implícito, con h=%f' % h, loc='left')
ax.set(xlim=(start, end), ylim=(bottom, top))
ax.scatter(x, y)
ax.plot(xe, ye, linewidth=2.0)

plt.subplots_adjust(left=0.12, bottom=0.12, right=0.94)
plt.show()
