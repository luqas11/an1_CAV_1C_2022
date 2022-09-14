# Ejercicio 5a:
# Aplicando el método de Newton-Raphson, hallar la raíz cúbica de un número positivo c.
# Verificar con un determinado c y un valor inicial adecuado.

import numpy as np

# =============================================
#             PARÁMETROS INICIALES            
# =============================================

# Constante a utilizar
c = 1.2

# Función a resolver
def gnr(x):
    return x - (np.power(x, 3) - c) / (3 * np.power(x, 2))

# Valor incial
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
        print("RESULTADO VÁLIDO EN", i, "ITERACIONES", "\n\n")
        break
    delta_x = abs(gnr(x) - x) / 2
    x = gnr(x)
