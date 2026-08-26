import sys
sys.path.append("src")  


import unittest
from model import logica_calculadora

class TestLogicaAhorro(unittest.TestCase):

    def test_caso_1_meta_1anio_sin_abono(self):

        # 1 Entradas
        meta = 10000000
        tasa = 0.015
        plazo = 12
        abono_extra = 0

        # 2 Salidas esperadas
        cuota_esperada = 766799.93

        # 3 Funcionalidad
        cuota_calculada = logica_calculadora.CalculadoraAhorro(meta, tasa, plazo, abono_extra).calcular_cuota()

        # 4 Verificar
        self.assertAlmostEqual(cuota_esperada, cuota_calculada, 2)

    def test_caso_2_meta_2anios_sin_abono(self):

        # 1 Entradas
        meta = 5000000
        tasa = 0.01
        plazo = 24
        abono_extra = 0

        # 2 Salidas esperadas
        cuota_esperada = 185367.36

        # 3 Funcionalidad
        cuota_calculada = logica_calculadora.CalculadoraAhorro(meta, tasa, plazo, abono_extra).calcular_cuota()

        # 4 Verificar
        self.assertAlmostEqual(cuota_esperada, cuota_calculada, 2)

    def test_caso_3_meta_18meses_con_abono(self):

        # 1 Entradas
        meta = 20000000
        tasa = 0.02
        plazo = 18
        abono_extra = 2000000

        # 2 Salidas esperadas
        cuota_esperada = 840637.84

        # 3 Funcionalidad
        cuota_calculada = logica_calculadora.CalculadoraAhorro(meta, tasa, plazo, abono_extra).calcular_cuota()

        # 4 Verificar
        self.assertAlmostEqual(cuota_esperada, cuota_calculada, 2)

    def test_caso_4_plazo_un_periodo(self):

        # 1 Entradas
        meta = 1000000
        tasa = 0.02
        plazo = 1
        abono_extra = 0

        # 2 Salidas esperadas
        cuota_esperada = 1000000

        # 3 Funcionalidad
        cuota_calculada = logica_calculadora.CalculadoraAhorro(meta, tasa, plazo, abono_extra).calcular_cuota()

        # 4 Verificar
        self.assertAlmostEqual(cuota_esperada, cuota_calculada, 2)

    def test_caso_5_abono_casi_igual_meta(self):

        # 1 Entradas
        meta = 10000000
        tasa = 0.015
        plazo = 12
        abono_extra = 9999999

        # 2 Salidas esperadas
        cuota_esperada = 0.0767

        # 3 Funcionalidad
        cuota_calculada = logica_calculadora.CalculadoraAhorro(meta, tasa, plazo, abono_extra).calcular_cuota()

        # 4 Verificar
        self.assertAlmostEqual(cuota_esperada, cuota_calculada, 2)

    def test_caso_6_plazo_360meses(self):

        # 1 Entradas
        meta = 500000000
        tasa = 0.008
        plazo = 360
        abono_extra = 0

        # 2 Salidas esperadas
        cuota_esperada = 240799.85

        # 3 Funcionalidad
        cuota_calculada = logica_calculadora.CalculadoraAhorro(meta, tasa, plazo, abono_extra).calcular_cuota()

        # 4 Verificar
        self.assertAlmostEqual(cuota_esperada, cuota_calculada, 2)

    def test_caso_7_meta_invalida(self):

        # 1 Entradas
        meta = -5000000
        tasa = 0.015
        plazo = 12
        abono_extra = 0


        # 4 Verificar
        with self.assertRaises(logica_calculadora.MetaInvalida):
            logica_calculadora.CalculadoraAhorro(meta, tasa, plazo, abono_extra).calcular_cuota()

    def test_caso_8_tasa_invalida(self):

        # 1 Entradas
        meta = 10000000
        tasa = -0.01
        plazo = 12
        abono_extra = 0


        # 4 Verificar
        with self.assertRaises(logica_calculadora.TasaInteresInvalida):
            logica_calculadora.CalculadoraAhorro(meta, tasa, plazo, abono_extra).calcular_cuota()

    def test_caso_9_periodos_invalidos(self):

        # 1 Entradas
        meta = 10000000
        tasa = 0.015
        plazo = 3.5
        abono_extra = 0


        # 4 Verificar
        with self.assertRaises(logica_calculadora.PeriodosInvalidos):
            logica_calculadora.CalculadoraAhorro(meta, tasa, plazo, abono_extra).calcular_cuota()

    def test_caso_10_abono_invalido(self):

        # 1 Entradas
        meta = 10000000
        tasa = 0.015
        plazo = 12
        abono_extra = 10000000

        # 4 Verificar
        with self.assertRaises(logica_calculadora.AbonoExtraInvalido):
            logica_calculadora.CalculadoraAhorro(meta, tasa, plazo, abono_extra).calcular_cuota()

if __name__ == "__main__":
    unittest.main(verbosity=2)
