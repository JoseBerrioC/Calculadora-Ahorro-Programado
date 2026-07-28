# Calculadora-Ahorro-Programado

Herramienta que calcula la cuota periódica fija de un préstamo o ahorro
programado, junto con el total pagado y el total de intereses generados durante el plazo pactado. 

Principalmente se hace en bancos (prestas al banco cierto dinero a ciertos meses y obtienes un beneficio), el beneficio depende de la cantidad de meses y de los intereses que el banco paga al usuario.

ENTRADAS

P (Monto):
    Capital inicial del préstamo o ahorro (debe ser mayor a 0).

i (Tasa de interés):
    Tasa de interés POR PERIODO (mensual, no anual), expresada como
    decimal. Ej: 3.10% se ingresa como 0.031.

n (Numero de cuotas):
    Cantidad de periodos/pagos pactados.

IMPORTANTE PARA EL BUEN FUNCIONAMIENTO DE LA CALCULADORA Y PREEVER ERRORES: la tasa i debe corresponder al mismo periodo que n.
Si n esta en meses, i debe ser la tasa mensual. Si se tiene una tasa
efectiva anual, debe convertirse antes con:

i_mensual = (1 + i_anual) ** (1/12) - 1

PROCESO (formulas aplicadas)

Formula base:

salida = P * i / (1 - (1 + i) ** -n)

Con dos casos especiales para evitar errores matemáticos:

- Si n == 1:  salida = P
      (un solo pago, no alcanza a generar interés)

- Si i == 0:  salida = P / n
      (se reparte el monto en partes iguales, sin interés)


- Caso general (n > 1 e i > 0): se aplica la formula completa.

A partir de la cuota (salida) se calculan los totales:

total_abonos    = salida * n
total_intereses = total_abonos - P

SALIDAS

salida:
    Cuota fija pagada o ganada en cada periodo.

total_abonos:
    Suma de todas las cuotas pagadas durante los n periodos.

total_intereses:
    Total de intereses pagados (total_abonos - P).

CASOS DE PRUEBA

- Casos normales: entradas típicas y validas (montos, tasas y plazos
  comunes).
- Casos excepcionales: entradas validas pero en los limites de la
  formula (n=1, i=0, tasas muy bajas, plazos muy largos).
- Casos de error: entradas invalidas (monto <= 0, n=0, n negativo),
  donde la formula devuelve resultados numéricos fuera de lo esperado
  en lugar de detener el calculo, evidenciando por que se necesita
  validar las entradas antes de calcular.
