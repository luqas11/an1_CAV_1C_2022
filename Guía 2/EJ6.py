# Ejercicio 6:
# Hallar la raíz de la función f(x)=sen(x) que se encuentra en el intervalo 3<x<3.3.
# Utilizar el método de Newton-Raphson con un valor inicial de 3 y hasta alcanzar 6 dígitos significativos de precisión.

import numpy as np

# =============================================
#             PARÁMETROS INICIALES            
# =============================================

# Función a resolver
def gnr(x):
    return x - round(np.sin(x), 4) / round(np.cos(x), 4)

# Valor inicial
X = 3

# Máximo error absoluto aceptable
MAX_ERR = 0.0000005

# =============================================
#                 RESOLUCIÓN           
# =============================================

# Valor medio de cada intervalo
x = X
delta_x = np.inf

print ("{:<3} {:<10} {:<10}".format("i", "x", "Δx"))
for i in range(0, 100):
    print ("{:<3} {:0.6f}   {:0.6f}".format(i, x, delta_x))
    if delta_x < MAX_ERR:
        print("RESULTADO VÁLIDO EN", i, "ITERACIONES", "\n")
        break
    delta_x = abs(gnr(x) - x) / 2
    x = gnr(x)
