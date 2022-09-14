# Ejercicio 4:
# Hallar la raíz de la ecuación x=cos(x).
# Utilizar el método de Newton-Raphson partiendo de un valor inicial adecuado y hasta alcanzar un error relativo menor a 10^-10.

import numpy as np

# =============================================
#             PARÁMETROS INICIALES            
# =============================================

# Función a resolver
def gnr(x):
    return x - (x - np.cos(x)) / (1 + np.sin(x))

# Valor incial
X = 0.75

# Máximo error relativo aceptable
MAX_ERR = 0.0000000001

# =============================================
#                 RESOLUCIÓN           
# =============================================

# Valor medio de cada intervalo
x = X
delta_x = 0
rel_error = np.inf

print ("{:<3} {:<14} {:<14} {:<14}".format("i", "x", "Δx", "Δx / x"))
for i in range(0, 100):
    print ("{:<3} {:0.10f}   {:0.10f}   {:0.10f}".format(i, x, delta_x, rel_error))
    if rel_error < MAX_ERR:
        print("RESULTADO VÁLIDO EN", i, "ITERACIONES", "\n\n")
        break
    delta_x = abs(gnr(x) - x)
    rel_error = abs(gnr(x) - x) / gnr(x)
    x = gnr(x)
    