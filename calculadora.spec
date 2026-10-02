# -*- mode: python ; coding: utf-8 -*-
import sys
import os
from PyInstaller.building.build_main import Analysis, PYZ, EXE, COLLECT
from PyInstaller.building.datastruct import Tree
from kivy_deps import sdl2, glew, angle
from kivy.tools.packaging.pyinstaller_hooks import get_deps_minimal, hookspath, runtime_hooks

block_cipher = None

src_dir = os.path.abspath('src')

kivy_deps_dict = get_deps_minimal(video=None, audio=None)
hidden_imports = list(set(kivy_deps_dict.get('hiddenimports', []) + ['model', 'model.logica_calculadora']))
excluded_imports = list(set(kivy_deps_dict.get('excludes', []) + ['tkinter', '_tkinter', 'twisted', 'test']))

a = Analysis(
    ['src/view/gui/gui_main.py'],
    pathex=[src_dir, '.'],
    binaries=kivy_deps_dict.get('binaries', []),
    datas=[('src/model', 'model')],
    hiddenimports=hidden_imports,
    hookspath=hookspath(),
    hooksconfig={},
    runtime_hooks=runtime_hooks(),
    excludes=excluded_imports,
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

# Configuración de ejecutable (modo Onedir - recomendado para Kivy por velocidad de arranque)
exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='CalculadoraAhorro',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins + angle.dep_bins)],
    strip=False,
    upx=True,
    upx_exclude=[],
    name='CalculadoraAhorro',
)
