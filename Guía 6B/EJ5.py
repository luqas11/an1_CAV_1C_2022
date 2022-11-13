# Ejercicio 5:
# Integrar la siguiente función en el intervalo (0, 4) utilizando el método de Romberg con los siguientes valores:
#    x |  0      0.5    1      1.5    2      2.5    3      3.5    4
# f(x) | -4.271 -2.522 -0.499  1.795  4.358  7.187  10.279 13.633 17.247

import time
import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.append('././modules')
from integration import richardson

# =============================================
#             PARÁMETROS INICIALES            
# =============================================

x = np.array([[ 0], [ 0.5], [ 1], [ 1.5], [ 2], [ 2.5], [ 3], [ 3.5], [ 4]], dtype = float)
y = np.array([[-4.271], [-2.522], [-0.499], [ 1.795], [ 4.358], [ 7.187], [ 10.279], [ 13.633], [ 17.247]], dtype = float)

inf = x[0]
sup = x[len(x) - 1]
h = sup - inf

n = len(x) - 1

# =============================================
#                 RESOLUCIÓN           
# =============================================
startTime = time.perf_counter_ns()

hr = h/8
nr = n
romberg_table = np.zeros((4, 4), dtype = float)

# Cálculo de los trapecios
for j in range(0, 4):
    _h = h/(2**j)
    _sum = _h/2 * (y[0] + y[nr])
    _n = int(np.round((sup - inf) / _h))

    for k in range(1, _n):
        _sum += _h * y[k*(2**(3-j))]

    romberg_table[j][0] = _sum

# Aplicación de Romberg
for i in range(0,3):
    for j in range(i+1,4):
        romberg_table[j][i+1] = richardson(romberg_table[j-1][i], romberg_table[j][i], 2*(i+1))

print(romberg_table, "\n")

endTime = time.perf_counter_ns()
# =============================================
#                 RESULTADOS           
# =============================================

# Prints
print("Tiempo de ejecución:", (endTime - startTime) / 1000000, "ms")
print("Resultado del Romberg: ", romberg_table[3][3])
print("Resultado exacto: desconocido")


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

ax.set_title('Resultado: I=%f' % romberg_table[3][3], loc='right')
ax.set_title('Método de Romberg, con h=%f' % h, loc='left')
ax.set(xlim=(start, end), ylim=(bottom, top))
ax.scatter(x, y)

plt.vlines(x = inf, ymin = bottom, ymax = top)
plt.vlines(x = sup, ymin = bottom, ymax = top)
plt.subplots_adjust(left=0.12, bottom=0.12, right=0.94)
plt.show()
