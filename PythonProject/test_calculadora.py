import unittest

from logica_calculadora import calcular_totales

def mostrar_resultado(nombre, P, i, n, salida, total_abonos, total_intereses):
    print(f"\n{nombre}")
    print(f"  P = {P:,.0f}  |  i = {i:.2%}  |  n = {n}")
    print(f"  Salida (cuota):   ${salida:,.2f}")
    print(f"  Total Abonos:     ${total_abonos:,.2f}")
    print(f"  Total Intereses:  ${total_intereses:,.2f}")

class TestCasosNormales(unittest.TestCase):

    def test_caso_normal(self):
       
        P, i, n = 200_000, 0.031, 36

        salida_esperada = 9297.96
        total_abonos_esperado = 334_726.53
        total_intereses_esperado = 134_726.53

        salida, total_abonos, total_intereses = calcular_totales(P, i, n)
        mostrar_resultado("Caso Normal", P, i, n, salida, total_abonos, total_intereses)

        self.assertAlmostEqual(salida_esperada, salida, 2)
        self.assertAlmostEqual(total_abonos_esperado, total_abonos, 2)
        self.assertAlmostEqual(total_intereses_esperado, total_intereses, 2)

    def test_caso_normal_2(self):
       
        P, i, n = 850_000, 0.034, 24

        salida_esperada = 52_377.50
        total_abonos_esperado = 1_257_059.97
        total_intereses_esperado = 407_059.97

        salida, total_abonos, total_intereses = calcular_totales(P, i, n)
        mostrar_resultado("Caso Normal 2", P, i, n, salida, total_abonos, total_intereses)

        self.assertAlmostEqual(salida_esperada, salida, 1)
        self.assertAlmostEqual(total_abonos_esperado, total_abonos, 1)
        self.assertAlmostEqual(total_intereses_esperado, total_intereses, 1)

    def test_caso_normal_3(self):
       
        P, i, n = 350_000, 0.022, 18

        salida_esperada = 23_758.26
        total_abonos_esperado = 427_648.72
        total_intereses_esperado = 77_648.72

        salida, total_abonos, total_intereses = calcular_totales(P, i, n)
        mostrar_resultado("Caso Normal 3", P, i, n, salida, total_abonos, total_intereses)

        self.assertAlmostEqual(salida_esperada, salida, 1)
        self.assertAlmostEqual(total_abonos_esperado, total_abonos, 1)
        self.assertAlmostEqual(total_intereses_esperado, total_intereses, 1)

class TestCasosExcepcionales(unittest.TestCase):

    def test_cuota_unica(self):
        # 1. Entradas
        P, i, n = 90_000, 0.024, 1

        # 2. Salidas esperadas
        salida_esperada = 90_000
        total_abonos_esperado = 90_000
        total_intereses_esperado = 0

        # 3. Funcionalidad
        salida, total_abonos, total_intereses = calcular_totales(P, i, n)
        mostrar_resultado("Cuota unica", P, i, n, salida, total_abonos, total_intereses)

        # 4. Verificar
        self.assertAlmostEqual(salida_esperada, salida, 2)
        self.assertAlmostEqual(total_abonos_esperado, total_abonos, 2)
        self.assertAlmostEqual(total_intereses_esperado, total_intereses, 2)

    def test_tasa_cero(self):
        # 1. Entradas
        P, i, n = 480_000, 0.0, 48

        # 2. Salidas esperadas
        salida_esperada = 10_000
        total_abonos_esperado = 480_000
        total_intereses_esperado = 0

        # 3. Funcionalidad
        salida, total_abonos, total_intereses = calcular_totales(P, i, n)
        mostrar_resultado("Tasa cero", P, i, n, salida, total_abonos, total_intereses)

        # 4. Verificar
        self.assertAlmostEqual(salida_esperada, salida, 2)
        self.assertAlmostEqual(total_abonos_esperado, total_abonos, 2)
        self.assertAlmostEqual(total_intereses_esperado, total_intereses, 2)

    def test_plazo_largo(self):
        # 1. Entradas
        P, i, n = 1_500_000, 0.015, 84

        # 2. Salidas esperadas
        salida_esperada = 31_526.76
        total_abonos_esperado = 2_648_247.59
        total_intereses_esperado = 1_148_247.59

        # 3. Funcionalidad
        salida, total_abonos, total_intereses = calcular_totales(P, i, n)
        mostrar_resultado("Plazo largo", P, i, n, salida, total_abonos, total_intereses)

        # 4. Verificar
        self.assertAlmostEqual(salida_esperada, salida, 2)
        self.assertAlmostEqual(total_abonos_esperado, total_abonos, 2)
        self.assertAlmostEqual(total_intereses_esperado, total_intereses, 2)

    def test_tasa_muy_baja(self):
        # 1. Entradas
        P, i, n = 600_000, 0.0005, 60

        # 2. Salidas esperadas
        salida_esperada = 10_153.25
        total_abonos_esperado = 609_194.98
        total_intereses_esperado = 9_194.98

        # 3. Funcionalidad
        salida, total_abonos, total_intereses = calcular_totales(P, i, n)
        mostrar_resultado("Tasa muy baja", P, i, n, salida, total_abonos, total_intereses)

        # 4. Verificar
        self.assertAlmostEqual(salida_esperada, salida, 2)
        self.assertAlmostEqual(total_abonos_esperado, total_abonos, 2)
        self.assertAlmostEqual(total_intereses_esperado, total_intereses, 2)

class TestCasosDeError(unittest.TestCase):

    def test_usura(self):
        # 1. Entradas
        P, i, n = 50_000, 0.124, 60

        # 2. Salidas esperadas
        salida_esperada = 6205.58
        total_abonos_esperado = 372_334.93
        total_intereses_esperado = 322_334.93

        # 3. Funcionalidad
        salida, total_abonos, total_intereses = calcular_totales(P, i, n)
        mostrar_resultado("Usura", P, i, n, salida, total_abonos, total_intereses)

        # 4. Verificar
        self.assertAlmostEqual(salida_esperada, salida, 2)
        self.assertAlmostEqual(total_abonos_esperado, total_abonos, 2)
        self.assertAlmostEqual(total_intereses_esperado, total_intereses, 2)

    def test_error_compra(self):
        # 1. Entradas
        P, i, n = 0, 0.024, 60

        # 2. Salidas esperadas
        salida_esperada = 0
        total_abonos_esperado = 0
        total_intereses_esperado = 0

        # 3. Funcionalidad
        salida, total_abonos, total_intereses = calcular_totales(P, i, n)
        mostrar_resultado("Error Compra", P, i, n, salida, total_abonos, total_intereses)

        # 4. Verificar
        self.assertAlmostEqual(salida_esperada, salida, 2)
        self.assertAlmostEqual(total_abonos_esperado, total_abonos, 2)
        self.assertAlmostEqual(total_intereses_esperado, total_intereses, 2)

    def test_error_cuotas(self):
        # 1. Entradas
        P, i, n = 80_000, 0.024, 0

        # 2. Salidas esperadas
        salida_esperada = 0
        total_abonos_esperado = 0
        total_intereses_esperado = -80_000

        # 3. Funcionalidad
        salida, total_abonos, total_intereses = calcular_totales(P, i, n)
        mostrar_resultado("Error Cuotas", P, i, n, salida, total_abonos, total_intereses)

        # 4. Verificar
        self.assertAlmostEqual(salida_esperada, salida, 2)
        self.assertAlmostEqual(total_abonos_esperado, total_abonos, 2)
        self.assertAlmostEqual(total_intereses_esperado, total_intereses, 2)

    def test_error_negativo(self):
        # 1. Entradas
        P, i, n = 50_000, 0.01, -10

        # 2. Salidas esperadas
        salida_esperada = -4779.10
        total_abonos_esperado = 47_791.04
        total_intereses_esperado = -2_208.96

        # 3. Funcionalidad
        salida, total_abonos, total_intereses = calcular_totales(P, i, n)
        mostrar_resultado("Error Negativo", P, i, n, salida, total_abonos, total_intereses)

        # 4. Verificar
        self.assertAlmostEqual(salida_esperada, salida, 2)
        self.assertAlmostEqual(total_abonos_esperado, total_abonos, 2)
        self.assertAlmostEqual(total_intereses_esperado, total_intereses, 2)

if __name__ == "__main__":
    unittest.main(verbosity=2)
