import sys
sys.path.append("src")

from model.plan_ahorro import PlanAhorro
from model.logica_calculadora import calcular_cuota
from controller.plan_ahorro_controller import PlanAhorroController

print("=== CREAR NUEVO PLAN DE AHORRO PROGRAMADO ===")
id_plan = input("Identificador único del plan (ej: PLAN-01): ").strip()
nombre_meta = input("Nombre o propósito de la meta: ").strip()
meta = float(input("Meta de ahorro deseada ($): "))
tasa_pct = float(input("Tasa de interés periódica mensual (%): "))
periodos = int(input("Número de periodos (meses): "))
abono_txt = input("Abono extra en la última cuota (deje vacío para 0): ").strip()
abono_extra = float(abono_txt) if abono_txt else 0.0

tasa_decimal = tasa_pct / 100.0
cuota_calculada = calcular_cuota(meta, tasa_decimal, periodos, abono_extra)

plan = PlanAhorro(id_plan, nombre_meta, meta, tasa_decimal, periodos, abono_extra, cuota_calculada)
PlanAhorroController.insertar(plan)

print(f"\n¡Plan '{nombre_meta}' registrado exitosamente con una cuota mensual de: ${cuota_calculada:,.2f}!")