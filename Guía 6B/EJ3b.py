# Ejercicio 3a:
# Integrar la función f(x) = sen(x) en el intervalo (0, pi/2) utilizando el método de Simpson con los siguientes valores:
#    x | 0       pi/12   pi/6    pi/4    pi/3    5*pi/12 pi/2
# f(x) | 0.0000  0.2587  0.5000  0.7071  0.8660  0.9659  1.0000

import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.append('././modules')
from integration import simpson_discrete

# =============================================
#             PARÁMETROS INICIALES            
# =============================================

x = np.array([[ 0], [ np.pi/12], [ np.pi/6], [ np.pi/4], [ np.pi/3], [ 5*np.pi/12], [ np.pi/2]], dtype = float)
y = np.array([[ 0.0000], [ 0.2587], [ 0.5000], [ 0.7071], [ 0.8660], [ 0.9659], [ 1.0000]], dtype = float)

inf = x[0]
sup = x[len(x) - 1]
h = x[1] - x[0]

# =============================================
#                 RESOLUCIÓN           
# =============================================

sum = simpson_discrete(x, y)

# =============================================
#                 RESULTADOS           
# =============================================

# Prints
print("Resultado: ", sum)
print("Resultado exacto: 1")

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

ax.set_title('Resultado: I=%f' % sum, loc='right')
ax.set_title('Método de Simpson, con h=%f' % h, loc='left')
ax.set(xlim=(start, end), ylim=(bottom, top))
ax.scatter(x, y)

plt.vlines(x = inf, ymin = bottom, ymax = top)
plt.vlines(x = sup, ymin = bottom, ymax = top)
plt.subplots_adjust(left=0.12, bottom=0.12, right=0.94)
plt.show()
