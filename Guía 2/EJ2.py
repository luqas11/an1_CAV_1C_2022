# Ejercicio 2:
# Hallar la raíz de la función f(x)=x^2/4-sen(x).
# Calcular mediante el método de bisección, a partir de un intervalo adecuado y con un error absoluto menor a 0.02.

import numpy as np

# =============================================
#             PARÁMETROS INICIALES            
# =============================================

# Función a resolver
def f(x):
    return np.power(x, 2) / 4 - np.sin(x)

# Intervalo inicial
A = 1.5
B = 2.5

# Error máximo admitido
MAX_ERR = 0.02

# =============================================
#                 RESOLUCIÓN           
# =============================================

# Cotas de cada intervalo
a_n = A
b_n = B

# Valor medio de cada intervalo
midpoint = (a_n + b_n) / 2
delta_m = (b_n - a_n) / 2

print ("{:<3} {:<7} {:<7} {:<10} {:<10} {:<7}".format("i", "a_n", "b_n", "vm", "Δm", "f_vm"))
for i in range(0, 1000):
    print ("{:<3} {:0.3f}   {:0.3f}   {:0.6f}   {:0.6f}   {:0.3f}".format(i, a_n, b_n, midpoint, delta_m, f(midpoint)))
    if delta_m < MAX_ERR:
        print("Resultado válido en", i, "iteraciones", "\n")
        break

    f_midpoint = f(midpoint)
    f_an = f(a_n)

    if f_midpoint * f_an < 0:
        b_n = midpoint
    else:
        a_n = midpoint

    midpoint = (a_n + b_n) / 2
    delta_m = (b_n - a_n) / 2
