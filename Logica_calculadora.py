# ---------------------------------------------------------------------------
# NUCLEO DE LA CALCULADORA
# ---------------------------------------------------------------------------

def calcular_cuota(P: float, i: float, n: int) -> float:
    """Calcula la cuota fija periodica (salida).

    Parametros
    ----------
    P : monto del prestamo o ahorro
    i : tasa de interes por periodo (decimal, ej. 0.031 = 3.1%)
    n : numero de cuotas/periodos

    """
    try:
        if n == 1:
            return P
        if i == 0:
            return P / n
        return P * i / (1 - (1 + i) ** -n)
    except ZeroDivisionError:
        return 0.0


