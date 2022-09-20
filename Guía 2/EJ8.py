# Ejercicio 8:
# Hallar la raíz de la función f(x)=0.5-e^-x.
# Utilizar el método de Newton-Raphson con un valor inicial de 0.25 hasta alcanzar un error relativo menor al 1%.

import numpy as np

# =============================================
#             PARÁMETROS INICIALES            
# =============================================

# Función a resolver
def gnr(x):
    return x - 0.5 / np.exp(-x) + 1

# Valor inicial
X = 0.25

# Máximo error relativo aceptable
MAX_ERR = 0.01

# =============================================
#                 RESOLUCIÓN           
# =============================================

# Valor medio de cada intervalo
x = X
delta_x = 0
rel_error = np.inf

print ("{:<3} {:<10} {:<10} {:<10}".format("i", "x", "Δx", "Δx / x"))
for i in range(0, 100):
    print ("{:<3} {:0.6f}   {:0.6f}   {:0.6f}".format(i, x, delta_x, rel_error))
    if rel_error < MAX_ERR:
        print("RESULTADO VÁLIDO EN", i, "ITERACIONES", "\n")
        break
    delta_x = abs(gnr(x) - x)
    rel_error = abs(gnr(x) - x) / gnr(x)
    x = gnr(x)
