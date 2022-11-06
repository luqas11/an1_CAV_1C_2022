# Ejercicio 1b:
# Aproximar la función y = e^x utilizando la recta tangente en el punto medio del intervalo (0, 1).

import numpy as np
import matplotlib.pyplot as plt

# =============================================
#             PARÁMETROS INICIALES            
# =============================================

# Función a aproximar
def f(x):
    return np.exp(x)

# =============================================
#                 RESOLUCIÓN           
# =============================================

# Plots
plt.style.use('_mpl-gallery')
fig, ax = plt.subplots()

x_f = np.linspace(-10, 10, 100)
y_f = f(x_f)

x_a = np.linspace(-10, 10, 100)
y_a = np.sqrt(np.e) * x_a + 0.5 * np.sqrt(np.e)

ax.plot(x_f, y_f, linewidth=2.0)
ax.plot(x_a, y_a, linewidth=2.0)

ax.set(xlim=(-3, 3), ylim=(-1, 5))
plt.subplots_adjust(left=0.12, bottom=0.12, right=0.94)
plt.show()
