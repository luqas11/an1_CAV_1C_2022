# Ejercicio 1c:
# Hallar la raíz de la ecuación e^(-2x)=1-x que se encuentra en el intervalo (0, 1.6).
# Utilizar el método de bisección hasta alcanzar un error absoluto menor a 0.2.

import numpy as np

# =============================================
#             PARÁMETROS INICIALES            
# =============================================

# Función a resolver
def f(x):
    return 1 - x - np.exp(-2*x)

# Intervalo incial
A = 0.1
B = 1.6

# Error máximo admitido
MAX_ERR = 0.02

# =============================================
#                 RESOLUCIÓN           
# =============================================

# Cotas de cada intervalo
a_n = A
b_n = B
# Valor medio de cada intervalo
valor_medio = (a_n + b_n) / 2
delta_m = (b_n - a_n) / 2

print ("{:<3} {:<7} {:<7} {:<7} {:<7} {:<7}".format("i", "a_n", "b_n", "vm", "Δm", "f_vm"))
for i in range(0, 1000):
    print ("{:<3} {:0.3f}   {:0.3f}   {:0.3f}   {:0.3f}   {:0.3f}".format(i, a_n, b_n, valor_medio, delta_m, f(valor_medio)))
    if delta_m < MAX_ERR:
        print("RESULTADO VÁLIDO EN", i, "ITERACIONES", "\n\n")
        break

    f_valor_medio = f(valor_medio)
    f_an = f(a_n)

    if f_valor_medio * f_an < 0:
        b_n = valor_medio
    else:
        a_n = valor_medio

    valor_medio = (a_n+b_n)/2
    delta_m = (b_n - a_n) / 2
