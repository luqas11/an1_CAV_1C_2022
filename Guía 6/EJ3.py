# Ejercicio 3:
# Una barra unidimensional de 2m de longitud tiene una fuente de calor interna dada por la función R(x) = 1 + x, e intercambia calor con el ambiente a través de sus extremos.
# La temperatura a lo largo de la barra está determinada por la función T(x) que es solución de la ecuación diferencial T''(x) + R(x) = 0
# El flujo de calor en el extremo derecho está dado por la función T'(2) = T_inf - T(2) (siendo T_inf la temperatura del entorno en que se encuentra).
# La temperatura en el extremo izquierdo de la barra es de 10ºC y la temperatura ambiente es de 5ºC.
# Estimar los valores de temperatura en la barra, discretizando la ecuación diferencial mediante operadores de derivada de orden 2 y utilizando un paso de 1m.

# Interpretación del enunciado:
# y'' + 1 + x = 0
# y(0) = 10
# y'(2) = - y(2) + 5

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
sup = 2
h = 1

ui = 10

# Solución exacta
def fe(x):
    return -(x**3)/6 - (x**2)/2 + 7*x/9 + 10

# Función que genera los coeficientes para la construcción de la matriz tridiagonal
def fc(x):
    return np.array([[ 1/h**2], [ -2/h**2], [ 1/h**2]], dtype = float)

# Función que genera los coeficientes para la construcción de la última fila de la matriz tridiagonal
def fcn(x):
    return np.array([[ -4/h**2], [ -2*(-2 - 2*h)/h**2]], dtype = float)
    
# =============================================
#                 RESOLUCIÓN           
# =============================================
startTime = time.perf_counter_ns()

# Vector b a aplicar en la resolución del SEL de la matriz tridiagonal
n = int(np.round((sup - inf) / h))
b = np.zeros((n+1, 1), dtype = float)
b[0] = ui
for i in range(1, n):
    b[i] = -1 - i*h
b[n] = - 1 - n*h + 20/h

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
