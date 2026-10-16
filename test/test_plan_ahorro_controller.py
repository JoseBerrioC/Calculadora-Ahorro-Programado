import unittest
import sys
sys.path.append("src")

from model.plan_ahorro import PlanAhorro
from controller.plan_ahorro_controller import PlanAhorroController

class TestPlanAhorroController(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Test Fixture: recrea la tabla en PostgreSQL antes de iniciar las pruebas."""
        PlanAhorroController.borrar_tabla()
        PlanAhorroController.crear_tabla()

    def test_insert_and_search_normal_1(self):
        """Caso 1 (Normal): Inserción y búsqueda de un plan regular sin abono extra."""
        plan = PlanAhorro("PLAN-001", "Viaje Graduacion", 5000000.0, 0.015, 12, 0.0, 384000.0)
        PlanAhorroController.insertar(plan)
        recuperado = PlanAhorroController.buscar_por_id("PLAN-001")
        self.assertIsNotNone(recuperado)
        self.assertTrue(recuperado.is_equal(plan))

    def test_insert_and_search_normal_2(self):
        """Caso 2 (Normal): Inserción y búsqueda de un plan con abono extra."""
        plan = PlanAhorro("PLAN-002", "Cuota Inicial Moto", 8000000.0, 0.02, 24, 1000000.0, 250000.0)
        PlanAhorroController.insertar(plan)
        recuperado = PlanAhorroController.buscar_por_id("PLAN-002")
        self.assertIsNotNone(recuperado)
        self.assertTrue(recuperado.is_equal(plan))

    def test_insert_and_search_normal_limite(self):
        """Caso 3 (Normal / Límite): Inserción y búsqueda de un plan a 1 solo periodo."""
        plan = PlanAhorro("PLAN-003", "Ahorro Emergencia", 1000000.0, 0.01, 1, 0.0, 1000000.0)
        PlanAhorroController.insertar(plan)
        recuperado = PlanAhorroController.buscar_por_id("PLAN-003")
        self.assertIsNotNone(recuperado)
        self.assertTrue(recuperado.is_equal(plan))

    def test_error_primary_key_duplicada(self):
        """Caso 4 (Error): Dispara excepción al intentar insertar un ID duplicado (Primary Key)."""
        plan1 = PlanAhorro("PLAN-DUP", "Original", 3000000.0, 0.01, 6, 0.0, 480000.0)
        plan2 = PlanAhorro("PLAN-DUP", "Copia", 4000000.0, 0.02, 12, 0.0, 300000.0)
        PlanAhorroController.insertar(plan1)
        # Debe fallar por violación de clave primaria
        with self.assertRaises(Exception):
            PlanAhorroController.insertar(plan2)

    def test_error_buscar_inexistente(self):
        """Caso 5 (Error): Buscar un registro que no existe retorna None."""
        resultado = PlanAhorroController.buscar_por_id("PLAN-NO-EXISTE-999")
        self.assertIsNone(resultado)

if __name__ == "__main__":
    unittest.main()