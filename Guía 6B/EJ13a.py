# Ejercicio 13a:
# Integrar la siguiente función en el intervalo (0, 1) utilizando el método de Romberg con una precisión de 4 dígitos significativos:
# f(x) = 2/sqrt(pi) * e^(-x^2)

import time
import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.append('././modules')
from integration import romberg

# =============================================
#             PARÁMETROS INICIALES            
# =============================================

inf = 0
sup = 1
h = 0.5

# Función a integrar
def f(x):
    return 2/np.sqrt(np.pi) * np.exp(-x**2)

# =============================================
#                 RESOLUCIÓN           
# =============================================
startTime = time.perf_counter_ns()

rTable = romberg(f, h, inf, sup)

endTime = time.perf_counter_ns()
# =============================================
#                 RESULTADOS           
# =============================================

# Prints
print(rTable, "\n")
print("Tiempo de ejecución:", (endTime - startTime) / 1000000, "ms")
print("Resultado del Romberg: ", rTable[3][3])
print("Resultado exacto: 0.8427007929")

# Plots
margin = 0.2
windowSize = 0.5

plt.style.use('_mpl-gallery')
fig, ax = plt.subplots(figsize=(windowSize * 16, windowSize * 9), tight_layout=True)

width = sup - inf

x = np.linspace(inf - width * margin, sup + width * margin, 500)
y = f(x)

height = np.amax(y) - np.amin(y)

ax.set_title('Resultado: I=%f' % rTable[3][3], loc='right')
ax.set_title('Método de Romberg, con h=%f' % h, loc='left')
ax.set(xlim=(inf - width * margin, sup + width * margin), ylim=(np.amin(y) - height * margin, np.amax(y) + height * margin))
ax.plot(x, y, linewidth=2.0)

plt.fill_between(x, y, where = (inf < x) & (x < sup), alpha= 0.2)
plt.subplots_adjust(left=0.12, bottom=0.12, right=0.94)
plt.show()
