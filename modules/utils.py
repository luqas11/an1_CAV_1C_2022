# Utilidades auxiliares

def range1(start, end):
    """Retorna la evaluación de la función `range()` para los valores `start` y `end`, pero considerando al valor `end` como parte del intervalo.

    Parameters
    ----------
    start : int
        Valor inicial del intervalo.
    end : int
        Valor final del intervalo.

    Returns
    -------
    range
        Resultado de la evaluación de la función range, considerando al valor `end` como parte del intervalo.
    """    
    return range(start, end+1)
