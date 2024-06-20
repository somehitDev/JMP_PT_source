# -*- coding: utf-8 -*-
import jmp
from jmp import ModelingType
from jmp import DataType


# jmp package's API version
print("= versions ====================")
print(f"jmp version: {jmp.__jmp_version__}")
print(f"jmp-python version: {jmp.__version__}")
print("===============================\n")

print("= jmp variables ===============")
print("jmp home: ", jmp.ALL_HOME)
print("jmp builtin scripts: ", jmp.BUILTIN_SCRIPTS)
print(f"jmp sample apps: {jmp.SAMPLE_APPS}")
print(f"jmp sample data: {jmp.SAMPLE_DATA}")
print(f"jmp sample images: {jmp.SAMPLE_IMAGES}")
print(f"jmp sample import data: {jmp.SAMPLE_IMPORT_DATA}")
print(f"jmp sample project: {jmp.SAMPLE_PROJECTS}")
print(f"jmp sample scripts: {jmp.SAMPLE_SCRIPTS}")
print(f"jmp temp directory: {jmp.TEMP}\n")

print(f"python executable: {jmp.PYTHON_EXE}")
print(f"python user appdir: {jmp.PY_USER_APPDIR}\n")

print(f"user home: {jmp.HOME}")
print(f"user desktop: {jmp.DESKTOP}")
print(f"user documents: {jmp.DOCUMENTS}")
print(f"user downloads: {jmp.DOWNLOADS}")
print(f"user appdata: {jmp.USER_APPDATA}")
print("===============================\n")

print("= Types(Data/Modeling) ========")
print(f"DataTypes: {list(map(lambda c: c.name, DataType))}")
print(f"ModelingType: {list(map(lambda c: c.name, ModelingType))}")
print("===============================\n")
