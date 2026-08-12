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