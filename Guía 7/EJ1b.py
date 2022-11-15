# Ejercicio 1:
# Una barra unidimensional de longitud 3m se encuentra inicialmente a una temperatura de 500ºK.
# En el instante t = 0 sus extremos se ponen en contacto hielo, fijando su temperatura a 273ºK.
# La distribución de temperatura a lo largo del tiempo sobre la longitud de la barra está dada por la ecuación T(x, t) que es solución de la ecuación diferencial T_t = 5*T_xx.
# Estimar los valores de temperatura en la barra en el intervalo (0, 0.02), discretizando la ecuación diferencial mediante operadores de derivada de orden 2 y utilizando un paso espacial de 0.5m y un paso temporal de 0.01s.

# Interpretación del enunciado:
# T_t = 5*T_xx
# T(0, 0) = 273
# T(0, 3) = 273
# T(0, x) = 500, con x perteneciente a (0, 3)
# Estimar los valores de los intervalos dados con un paso espacial de 0.5 y un paso temporal de 0.01

import time
import numpy as np
import matplotlib.pyplot as plt

# =============================================
#             PARÁMETROS INICIALES            
# =============================================

inf = 0
sup = 3
h = 0.5
k = 0.01
u0 = 273
un = 273
nt = 3

# Condición inicial para t = 0
def f0(x):
    return 500

# =============================================
#                 RESOLUCIÓN           
# =============================================
startTime = time.perf_counter_ns()

n = int(np.round((sup - inf) / h))

# Ecuación a resolver en cada paso temporal
def step(y):
    _x = np.array([[inf]], dtype = float)
    _y = np.array([[u0]], dtype = float)
    for i in range(1, n):
        un1 = y[i] + k * ((5/(h**2)) * ((y[i+1]) - 2 * y[i] + y[i-1]))
        _x = np.append(_x, inf + h*i)
        _y = np.append(_y, un1)
    _x = np.append(_x, sup)
    _y = np.append(_y, un)

    return [_x, _y]

# Construcción de las condiciones iniciales para t = 0
x = np.array([[inf]], dtype = float)
y = np.array([[u0]], dtype = float)
for i in range(1, n):
    x = np.append(x, inf + h*i)
    y = np.append(y, f0(inf + h*i))
x = np.append(x, sup)
y = np.append(y, un)
matrix = [x, y]

# Resolución
matrices = []
for i in range(1, nt+1):
    matrices.append(matrix)
    matrix = step(matrices[i-1][1])

endTime = time.perf_counter_ns()
# =============================================
#                 RESULTADOS           
# =============================================

# Prints
print("Tiempo de ejecución:", (endTime - startTime) / 1000000, "ms")
print("Resultados:")

# Plots
margin = 0.2
window_size = 0.5

plt.style.use('_mpl-gallery')
fig, ax = plt.subplots(figsize=(window_size * 16, window_size * 9), tight_layout=True)

width = sup - inf
height = np.amax(y) - np.amin(y)

start = inf - width * margin
end = sup + width * margin
top = np.amax(y) + height * margin
bottom = np.amin(y) - height * margin

ax.set_title('EDDP con h=%f, k=%f, nt=%f' % (h, k, nt), loc='left')
ax.set(xlim=(start, end), ylim=(bottom, top))
for i in range(0, nt):
    print('\nTiempo:', i*k)
    print(np.matrix(matrices[i]).T)
    ax.plot(matrices[i][0], matrices[i][1])

plt.subplots_adjust(left=0.12, bottom=0.12, right=0.94)
plt.show()
