@echo off
title Generador de Ejecutable - Calculadora de Ahorro Programado
echo ====================================================
echo  Generando ejecutable .exe (Modo Carpeta Optimizada)
echo ====================================================
echo.

if not exist ".\venv\Scripts\pyinstaller.exe" (
    echo [ERROR] No se encontro PyInstaller en el entorno virtual.
    pause
    exit /b 1
)

.\venv\Scripts\pyinstaller.exe calculadora.spec --noconfirm

echo.
echo ====================================================
echo  Listo! El ejecutable se encuentra en:
echo  dist\CalculadoraAhorro\CalculadoraAhorro.exe
echo ====================================================
pause
