# Ejercicio 5c:
# Evaluar el logaritmo natural de un número a sin usar la función de logaritmo natural.
# Verificar para a=1.2 con un valor inicial adecuado.

import numpy as np

# =============================================
#             PARÁMETROS INICIALES            
# =============================================

# Constante a utilizar
a = 1.2

# Función a resolver
def gnr(x):
    return x + a / np.exp(x) - 1

# Valor inicial
X = 2

# Máximo error absoluto aceptable
MAX_ERR = 0.00005

# =============================================
#                 RESOLUCIÓN           
# =============================================

# Valor medio de cada intervalo
x = X
delta_x = np.inf

print ("{:<3} {:<8} {:<8}".format("i", "x", "Δx"))
for i in range(0, 100):
    print ("{:<3} {:0.4f}   {:0.4f}".format(i, x, delta_x))
    if delta_x < MAX_ERR:
        print("Resultado válido en", i, "iteraciones", "\n")
        break
    delta_x = abs(gnr(x) - x) / 2
    x = gnr(x)
