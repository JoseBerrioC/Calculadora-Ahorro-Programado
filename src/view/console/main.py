import sys
sys.path.append("src")  


from model import logica_calculadora



try:
    print("Este programa le permite calcular la cuota mensual a ahorrar")
    print("para alcanzar una meta de ahorro programado\n")

    meta = float(input("Meta de ahorro (M): "))
    tasa = float(input("Tasa de interés periódica (mensual, en %): ")) / 100
    plazo = float(input("Número de cuotas (meses) del plan de ahorro: "))
    abono_extra_txt = input("Abono extra en la última cuota (Enter para omitir): ")
    abono_extra = float(abono_extra_txt) if abono_extra_txt.strip() != "" else 0.0

    cuota = round(logica_calculadora.calcular_cuota(meta, tasa, plazo, abono_extra), 2)
    print(f"\nLa cuota mensual de ahorro requerida es de: {cuota}")

    tabla = logica_calculadora.generar_tabla_acumulacion(meta, tasa, plazo, abono_extra)
    totales = logica_calculadora.calcular_totales(tabla)

    print("\nPeriodo\tSaldo Inicial\tCuota\t\tInterés\t\tAbono Extra\tSaldo Final")
    for fila in tabla:
        print(
            f"{fila['periodo']}\t"
            f"{round(fila['saldo_inicial'], 2)}\t"
            f"{round(fila['cuota'], 2)}\t"
            f"{round(fila['interes_ganado'], 2)}\t"
            f"{round(fila['abono_extra'], 2)}\t\t"
            f"{round(fila['saldo_final'], 2)}"
        )

    print(f"\nTotal aportado: {round(totales['total_aportado'], 2)}")
    print(f"Total de interés generado: {round(totales['total_interes'], 2)}")
    print(f"Saldo final (debe ser ≈ M): {round(totales['saldo_final'], 2)}")

except Exception as error:
    print("No se pudo calcular la cuota")
    print(str(error))
