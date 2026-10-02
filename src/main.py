"""Punto de entrada para el empaquetado en Android.

Buildozer (Android) ejecuta este archivo como punto de entrada de la
aplicacion. Reutiliza la misma interfaz grafica Kivy del escritorio
(src/view/gui/gui_main.py), de modo que todos los dispositivos comparten
exactamente la misma interfaz y la misma logica.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from view.gui.gui_main import CalculadoraAhorroApp  # noqa: E402


def main():
    CalculadoraAhorroApp().run()


if __name__ == "__main__":
    main()