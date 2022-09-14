# Ejercicio 5b:
# Aplicando el método de Newton-Raphson, hallar el arcoseno de un número a.
# Verificar con a=0.5 y un valor inicial adecuado, tomando tres dígitos significativos.

import numpy as np

# =============================================
#             PARÁMETROS INICIALES            
# =============================================

# Constante a utilizar
a = 0.5

# Función a resolver
def gnr(x):
    return x + (a - np.sin(x)) / np.cos(x)

# Valor incial
X = 1

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
