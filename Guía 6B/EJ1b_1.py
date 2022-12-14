# Ejercicio 1b 1:
# Integrar la siguiente función en el intervalo (0, 2*pi) utilizando el método de Simpson con paso de pi/2:
# f(x) = pi/2 * e^(2 - 0.5 * sen(x))

import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.append('././modules')
from integration import simpson

# =============================================
#             PARÁMETROS INICIALES            
# =============================================

inf = 0
sup = 2*np.pi
h = np.pi/2

# Función a integrar
def f(x):
    return (np.pi/2)*np.exp(2 - 0.5*np.sin(x))

# =============================================
#                 RESOLUCIÓN           
# =============================================

sum = simpson(f, h, inf, sup)

# =============================================
#                 RESULTADOS           
# =============================================

# Prints
print("Resultado: ", sum)
print("Resultado exacto: 77.55671621")

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
ax.set_title('Método de Simpson, con h=%f' % h, loc='left')
ax.set(xlim=(inf - width * margin, sup + width * margin), ylim=(np.amin(y) - height * margin, np.amax(y) + height * margin))
ax.plot(x, y, linewidth=2.0)

plt.fill_between(x, y, where = (inf < x) & (x < sup), alpha= 0.2)
plt.subplots_adjust(left=0.12, bottom=0.12, right=0.94)
plt.show()
