# analyzer.spec
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['gui.py'],
    pathex=['.'],
    binaries=[],
    datas=[],
    hiddenimports=['morfeusz2'],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)
exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='analyzer',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,  # Change to False if UPX causes issues
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    icon=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=False,  # Change to False if UPX causes issues
    upx_exclude=[],
    name='analyzer',
)
