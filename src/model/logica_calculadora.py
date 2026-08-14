def calcular_cuota(m: float, i: float, n: float, ae: float = 0) -> float:

    if m <= 0:
        raise ValueError("La meta de ahorro (M) debe ser mayor que cero")

    if i <= 0:
        raise ValueError("La tasa de interés (i) debe ser mayor que cero")

    if n <= 0 or n != int(n):
        raise ValueError("El número de periodos (n) debe ser un entero positivo")

    if ae < 0 or ae >= m:
        raise ValueError("El abono extra (AE) debe ser menor que la meta de ahorro (M)")

    n = int(n)
    cuota = (m - ae) * i / ((1 + i) ** n - 1)
    return cuota


def generar_tabla_acumulacion(m: float, i: float, n: float, ae: float = 0) -> list:
  
    cuota = calcular_cuota(m, i, n, ae)
    n = int(n)

    tabla = []
    saldo_inicial = 0.0
    for k in range(1, n + 1):
        interes = saldo_inicial * i
        abono_extra = ae if k == n else 0.0
        saldo_final = saldo_inicial + cuota + interes + abono_extra

        tabla.append({
            "periodo": k,
            "saldo_inicial": saldo_inicial,
            "cuota": cuota,
            "interes_ganado": interes,
            "abono_extra": abono_extra,
            "saldo_final": saldo_final,
        })

        saldo_inicial = saldo_final

    return tabla


def calcular_totales(tabla: list) -> dict:

    total_cuotas = sum(fila["cuota"] for fila in tabla)
    total_interes = sum(fila["interes_ganado"] for fila in tabla)
    total_abono_extra = sum(fila["abono_extra"] for fila in tabla)
    saldo_final = tabla[-1]["saldo_final"] if tabla else 0.0

    return {
        "total_cuotas": total_cuotas,
        "total_interes": total_interes,
        "total_abono_extra": total_abono_extra,
        "total_aportado": total_cuotas + total_abono_extra,
        "saldo_final": saldo_final,
    }
