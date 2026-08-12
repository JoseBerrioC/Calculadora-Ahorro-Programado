import unittest

from test_calculadora import (
    TestCasosNormales,
    TestCasosExcepcionales,
    TestCasosDeError,
)


def ejecutar_suite(titulo: str, clase_prueba) -> None:
    print(f"=== {titulo} ===\n")
    suite = unittest.TestLoader().loadTestsFromTestCase(clase_prueba)
    unittest.TextTestRunner(verbosity=2).run(suite)
    print("-" * 45 + "\n")


if __name__ == "_main_":
    ejecutar_suite("Casos Normales", TestCasosNormales)
    ejecutar_suite("Casos Excepcionales", TestCasosExcepcionales)
    ejecutar_suite("Casos de Error", TestCasosDeError)