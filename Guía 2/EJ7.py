# Ejercicio 7:
# Hallar la raíz no nula de la función f(x)=x^2/4-sen(x).
# Utilizar el método de la secante hasta alcazar un error relativo menor al 0.1%. Determinar un intervalo inicial adecuado.

import numpy as np

# =============================================
#             PARÁMETROS INICIALES            
# =============================================

# Función a resolver
def f(x):
    return np.power(x, 2) / 4 - np.sin(x)
# Derivada de la función a resolver
def df(xn, xn_1):
    return (f(xn) - f(xn_1)) / (xn - xn_1)
# Función de Newton-Raphson
def gnr(xn, xn_1):
    return xn - f(xn) / df(xn, xn_1)

# Intervalo inicial
A = 1
B = 3

# Máximo error relativo aceptable
MAX_ERR = 0.00001

# =============================================
#                 RESOLUCIÓN           
# =============================================

# Valores de cada intervalo
xn_1 = A
xn = B
delta_x = 0
rel_error = np.inf

print ("{:<3} {:<10} {:<10} {:<10} {:<10} {:<10}".format("i", "xn-1", "xn", "xn+1", "Δx", "Δx/x"))
for i in range(0, 100):
    print ("{:<3} {:0.6f}   {:0.6f}   {:0.6f}   {:0.6f}   {:0.6f}".format(i, xn_1, xn, gnr(xn, xn_1), delta_x, rel_error))
    if rel_error < MAX_ERR:
        print("Resultado válido en", i, "iteraciones", "\n")
        break
    new_xn = gnr(xn, xn_1)
    delta_x = abs(new_xn - xn) / 2
    rel_error = delta_x / new_xn
    xn_1 = xn
    xn = new_xn
