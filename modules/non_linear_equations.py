# Algoritmos de resolución de ecuaciones no lineales

ITERACIONES_BISECCIÓN = 15

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
    valor_medio = (a_n + b_n) / 2

    x = valor_medio
    for i in range(0, ITERACIONES_BISECCIÓN):
        f_valor_medio = f(valor_medio)
        f_an = f(a_n)
        if f_valor_medio * f_an < 0:
            b_n = valor_medio
        else:
            a_n = valor_medio
        valor_medio = (a_n + b_n)/2
        x = valor_medio
    return x

def newton_raphson(f, sem):
    """Retorna la raíz de la función `f`, calculada mediante el método de Newton-Raphson.

    Para calcularla, el método utiliza la semilla `sem`. La función `f` debe ser una función de Newton-Raphson, donde la raíz buscada sea un punto fijo.

    Parameters
    ----------
    f : function
        Función a resolver.
    sem : float
        Semilla de la cual parte el método.

    Returns
    -------
    float
        Valor de la raíz de la función.
    """    
    x = sem

    for i in range(0, 15):
        x = f(x)
    return x
