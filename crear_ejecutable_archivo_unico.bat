@echo off
title Generador de Ejecutable Unico (.exe solitario)
echo ====================================================
echo  Generando ejecutable .exe en UN SOLO ARCHIVO
echo ====================================================
echo.

if not exist ".\venv\Scripts\pyinstaller.exe" (
    echo [ERROR] No se encontro PyInstaller en el entorno virtual.
    pause
    exit /b 1
)

.\venv\Scripts\pyinstaller.exe calculadora_un_archivo.spec --noconfirm

echo.
echo ====================================================
echo  Listo! Tu archivo ejecutable unico se encuentra en:
echo  dist\CalculadoraAhorro_Unico.exe
echo ====================================================
pause
