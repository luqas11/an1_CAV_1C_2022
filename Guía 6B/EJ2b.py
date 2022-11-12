# Ejercicio 2b:
# Integrar la siguiente función en el intervalo (1.00, 1.03) utilizando el método de Simpson:
# f(x) = sqrt(x)

import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.append('././modules')
from integration import simpson

# =============================================
#             PARÁMETROS INICIALES            
# =============================================

inf = 1
sup = 1.3
h = 0.05

# Función a integrar
def f(x):
    return np.sqrt(x)

# =============================================
#                 RESOLUCIÓN           
# =============================================

sum = simpson(f, h, inf, sup)

# =============================================
#                 RESULTADOS           
# =============================================

# Prints
print("Resultado: ", sum)
print("Resultado exacto: 0.3214853684")

# Plots
margin = 0.2
windowSize = 0.5

plt.style.use('_mpl-gallery')
fig, ax = plt.subplots(figsize=(windowSize * 16, windowSize * 9), tight_layout=True)

width = sup - inf

x = np.linspace(inf - width * margin, sup + width * margin, 500)
y = f(x)

height = np.amax(y) - np.amin(y)

ax.set_title('Resultado: I=%f' % sum, loc='right')
ax.set_title('Método de Simpson, con h=%f' % h, loc='left')
ax.set(xlim=(inf - width * margin, sup + width * margin), ylim=(np.amin(y) - height * margin, np.amax(y) + height * margin))
ax.plot(x, y, linewidth=2.0)

plt.fill_between(x, y, where = (inf < x) & (x < sup), alpha= 0.2)
plt.subplots_adjust(left=0.12, bottom=0.12, right=0.94)
plt.show()
