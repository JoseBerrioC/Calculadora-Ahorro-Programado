import logica_calculadora

try:
    print("Este programa le permite calcular la cuota fija pagada por un prestamo o ahorro programado")
    monto = float(input("Monto: "))
    tasa = float(input("Tasa de interes por periodo: ")) / 100
    plazo = int(input("Numero de cuotas: "))

    cuota, total_abonos, total_intereses = logica_calculadora.calcular_totales(monto, tasa, plazo)

    print(f"La cuota pagada por el banco es de:     {round(cuota, 2)}")
    print(f"Total Abonos:               {round(total_abonos, 2)}")
    print(f"Total Intereses:            {round(total_intereses, 2)}")
except Exception as err:
    print("No se pudo calcular la cuota")
    print(str(err))
