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


def calcular_totales(P: float, i: float, n: int) -> tuple[float, float, float]:
    """Calcula (salida, total_abonos, total_intereses)."""
    salida = calcular_cuota(P, i, n)
    total_abonos = salida * n
    total_intereses = total_abonos - P
    return salida, total_abonos, total_intereses


# ---------------------------------------------------------------------------
# PRESENTACION EN CONSOLA
# ---------------------------------------------------------------------------

def mostrar_caso(nombre: str, P: float, i: float, n: int) -> None:
    """Muestra un caso puntual."""
   
    salida, total_abonos, total_intereses = calcular_totales(P, i, n)

    print(f"{nombre}")
    print(f"  P = {P:,.0f}  |  i = {i:.2%}  |  n = {n}")
    print(f"  Salida (cuota):   ${salida:,.2f}")
    print(f"  Total Abonos:     ${total_abonos:,.2f}")
    print(f"  Total Intereses:  ${total_intereses:,.2f}")
    print()


