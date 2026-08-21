def calcular_cuota(meta: float, tasa_interes: float, periodos: float, abono_extra: float = 0) -> float:

    if meta <= 0:
        raise ValueError("La meta de ahorro (M) debe ser mayor que cero")

    if tasa_interes <= 0:
        raise ValueError("La tasa de interés (tasa_interes) debe ser mayor que cero")

    if periodos <= 0 or periodos != int(periodos):
        raise ValueError("El número de periodos (periodos) debe ser un entero positivo")

    if abono_extra < 0 or abono_extra >= meta:
        raise ValueError("El abono extra (AE) debe ser menor que la meta de ahorro (M)")

    periodos = int(periodos)
    cuota = (meta - abono_extra) * tasa_interes / ((1 + tasa_interes) ** periodos - 1)
    return cuota


def generar_tabla_acumulacion(meta: float, tasa_interes: float, periodos: float, abono_extra: float = 0) -> list:
  
    cuota = calcular_cuota(meta, tasa_interes, periodos, abono_extra)
    periodos = int(periodos)

    tabla = []
    saldo_inicial = 0.0
    for k in range(1, periodos + 1):
        interes = saldo_inicial * tasa_interes
        abono_extra = abono_extra if k == periodos else 0.0
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
