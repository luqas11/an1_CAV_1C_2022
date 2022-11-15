# Ejercicio 3:
# Hallar la raíz de la función f(x)=sen(x)-0.5*raíz(x) que se encuentra en el intervalo (0, 2] con un error relativo menor al 1%.
# Calcular mediante un método de punto fijo, partiendo de un valor inicial adecuado y utilizando la función g(x)=x-F(x).

import numpy as np

# =============================================
#             PARÁMETROS INICIALES            
# =============================================

# Función a resolver
def g(x):
    return x - np.sin(x) + 0.5 * np.sqrt(x)

# Valor inicial
X = 0.3

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
for i in range(0, 1000):
    print ("{:<3} {:0.6f}   {:0.6f}   {:0.6f}".format(i, x, delta_x, rel_error))
    if rel_error < MAX_ERR:
        print("Resultado válido en", i, "iteraciones", "\n")
        break
    delta_x = abs(g(x) - x)
    rel_error = abs(g(x) - x) / g(x)
    x = g(x)
