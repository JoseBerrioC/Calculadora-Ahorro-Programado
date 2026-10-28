import sys
sys.path.append("src")

from controller.plan_ahorro_controller import PlanAhorroController

print("=== BUSCAR PLAN DE AHORRO PROGRAMADO ===")
try:
    id_plan = input("Ingrese el identificador del plan a consultar: ").strip()
    if not id_plan:
        print("Error: El identificador no puede estar vacío.")
    else:
        plan = PlanAhorroController.buscar_por_id(id_plan)
        print("\n--- Plan Encontrado ---")
        print(f"ID: {plan.id_plan}")
        print(f"Meta: {plan.nombre_meta}")
        print(f"Monto Meta: ${plan.meta:,.2f}")
        print(f"Tasa Interés: {plan.tasa_interes * 100:.2f}%")
        print(f"Periodos: {plan.periodos} meses")
        print(f"Abono Extra: ${plan.abono_extra:,.2f}")
        print(f"Cuota Mensual: ${plan.cuota_mensual:,.2f}")
except Exception as err:
    print(f"\nNo es posible buscar el plan: {err}")
