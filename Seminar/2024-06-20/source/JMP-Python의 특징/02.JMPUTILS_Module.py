# -*- coding: utf-8 -*-
import sys, pathlib, jmputils

print("= function list ===============")
print([
    mname
    for mname in dir(jmputils)
    if not mname.startswith("_") and not mname.endswith("_") and not mname in ( "os", "sys", "Path", "platform", "site", "subprocess", "zipfile", "jmp" )
])
print("===============================\n")

print("= create_jpip ================")
jpip_dir = pathlib.Path("/Volumes/Dev/00_ongoing/JMP/PT_sources/Seminar/2024-06-20/source/JMP-PYTHON의 특징").resolve()
jpip_file = jpip_dir.joinpath("jpip" if sys.platform == "darwin" else "jpip.cmd")
print(f"jpip file: {jpip_dir.joinpath('jpip' if sys.platform == 'darwin' else 'jpip.cmd')}")

jmputils.create_jpip(str(jpip_dir))

print(f"created: {jpip_file.exists()}")
print("===============================\n")

print("= jpip ========================")
jmputils.jpip("install --upgrade", "pandas scipy")
print("===============================\n")
