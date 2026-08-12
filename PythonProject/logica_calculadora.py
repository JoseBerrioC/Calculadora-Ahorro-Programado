def calcular_cuota(P: float, i: float, n: int) -> float:

    try:
        if n == 1:
            return P
        if i == 0:
            return P / n
        return P * i / (1 - (1 + i) ** -n)
    except ZeroDivisionError:
        return 0.0


def calcular_totales(P: float, i: float, n: int) -> tuple[float, float, float]:
    salida = calcular_cuota(P, i, n)
    total_abonos = salida * n
    total_intereses = total_abonos - P
    return salida, total_abonos, total_intereses