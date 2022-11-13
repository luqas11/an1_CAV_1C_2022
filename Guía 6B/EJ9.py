# Ejercicio 9:
# Integrar la siguiente función en el intervalo (0, 2) utilizando el método de Gauss con 4 puntos:
# f(x) = e^(x^2)

import time
import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.append('././modules')
from integration import gauss

# =============================================
#             PARÁMETROS INICIALES            
# =============================================

inf = 0
sup = 2
n = 4

# Función a integrar
def f(x):
    return np.exp(x**2)

# =============================================
#                 RESOLUCIÓN           
# =============================================
startTime = time.perf_counter_ns()

sum = gauss(f, n, inf, sup)

endTime = time.perf_counter_ns()
# =============================================
#                 RESULTADOS           
# =============================================

# Prints
print("Tiempo de ejecución:", (endTime - startTime) / 1000000, "ms")
print("Resultado del Gauss: ", sum)
print("Resultado exacto: 16.452627765")

# Plots
margin = 0.2
window_size = 0.5

plt.style.use('_mpl-gallery')
fig, ax = plt.subplots(figsize=(window_size * 16, window_size * 9), tight_layout=True)

width = sup - inf

x = np.linspace(inf - width * margin, sup + width * margin, 500)
y = f(x)

height = np.amax(y) - np.amin(y)

ax.set_title('Resultado: I=%f' % sum, loc='right')
ax.set_title('Método de Gauss, con n=%f' % n, loc='left')
ax.set(xlim=(inf - width * margin, sup + width * margin), ylim=(np.amin(y) - height * margin, np.amax(y) + height * margin))
ax.plot(x, y, linewidth=2.0)

plt.fill_between(x, y, where = (inf < x) & (x < sup), alpha= 0.2)
plt.subplots_adjust(left=0.12, bottom=0.12, right=0.94)
plt.show()
