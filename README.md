# Calculadora de Ahorro Programado

Aplicación que calcula el valor de la cuota mensual constante que debe depositar una
persona en una entidad financiera para alcanzar una meta de ahorro al final de un
plazo pactado, dada una tasa de interés fija. Permite además incluir un abono extra
en la última cuota.

1. Entradas

M	Meta de ahorro (valor futuro deseado)	M > 0
i	Tasa de interés periódica (mensual, en decimal)	i > 0
n	Número de periodos (meses) del plan	entero > 0
AE	Abono extra en la última cuota (opcional, por defecto 0)	AE ≥ 0 y AE < M

Si la tasa se entrega en forma nominal anual (j) o efectiva anual (EA), debe
convertirse a periódica mensual antes de ingresarla:

Nominal: i = j / 12
Efectiva anual: i = (1 + EA)^(1/12) - 1
2. Proceso

Validación de entradas (en este orden):

M <= 0 → Error: La meta de ahorro (M) debe ser mayor que cero
i <= 0 → Error: La tasa de interés (i) debe ser mayor que cero
n no entero o n <= 0 → Error: El número de periodos (n) debe ser un entero positivo
AE >= M (o AE < 0) → Error: El abono extra (AE) debe ser menor que la meta de ahorro (M)

Cálculo de la cuota mensual (A):

A = (M - AE) * i / [ (1+i)^n - 1 ]

Cálculo de la tabla de acumulación, periodo a periodo (k = 1 … n):

Interes_k = Saldo_(k-1) * i

Saldo_k = Saldo_(k-1) * (1+i) + A                   para k = 1 … n-1
Saldo_n = Saldo_(n-1) * (1+i) + A + AE              (último periodo, incluye el abono extra)

Cálculo de totales, sumando toda la tabla:

Total cuotas       = Σ A
Total interés       = Σ Interes_k
Total abono extra   = AE
Total aportado      = Total cuotas + Total abono extra
Saldo final          = Saldo_n   (debe ser ≈ M)
3. Salidas
Cuota mensual de ahorro requerida (A), o el mensaje de error correspondiente.

Totales:
cuota mensual
Total aportado
Total de interés ganados

Casos de prueba

El proyecto incluye 10 casos de prueba en Excel, para las entradas y salidas esperadas del código:

3 normales: cálculo estándar de la cuota, con y sin abono extra.
3 excepcionales: plazo de un solo periodo, abono extra casi igual a la meta,
plazo muy largo (360 meses). Son válidos y no deben lanzar error.
4 de error: meta inválida, tasa inválida, número de periodos inválido, abono
extra igual o mayor a la meta.

 [Casos Prueba calculadora.xlsx](https://github.com/user-attachments/files/30966363/Casos.Prueba.calculadora.xlsx)

entrevista a experto:
  

https://github.com/user-attachments/assets/5cab3eb8-5e3b-4e5b-8952-a8fa483446e5





