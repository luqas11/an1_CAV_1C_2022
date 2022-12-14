# Algoritmos de resolución de ecuaciones no lineales

BISECTION_ITERATIONS = 15

def bisection(f, inf, sup):
    """Retorna la raíz de la función `f`, calculada mediante el método de bisección.
    Para calcularla, el método parte del intervalo `[inf, sup]`.

    Parameters
    ----------
    f : function
        Función a resolver.
    inf : float
        Valor inicial del intervalo inicial.
    sup : float
        Valor final del intervalo inicial.

    Returns
    -------
    float
        Valor de la raíz de la función.
    """    
    a_n = inf
    b_n = sup
    midpoint = (a_n + b_n) / 2

    x = midpoint
    for i in range(0, BISECTION_ITERATIONS):
        f_midpoint = f(midpoint)
        f_an = f(a_n)
        if f_midpoint * f_an < 0:
            b_n = midpoint
        else:
            a_n = midpoint
        midpoint = (a_n + b_n)/2
        x = midpoint
    return x

def newton_raphson(f, seed):
    """Retorna la raíz de la función `f`, calculada mediante el método de Newton-Raphson.

    Para calcularla, el método utiliza la semilla `seed`. La función `f` debe ser una función de Newton-Raphson, donde la raíz buscada sea un punto fijo.

    Parameters
    ----------
    f : function
        Función a resolver.
    seed : float
        Semilla de la cual parte el método.

    Returns
    -------
    float
        Valor de la raíz de la función.
    """    
    x = seed

    for i in range(0, 15):
        x = f(x)
    return x
