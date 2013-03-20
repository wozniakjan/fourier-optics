from cx_Freeze import setup, Executable

includes = ["sip","re","atexit","PyQt4.QtCore"]

exe = Executable(
    script = "main.py",
    base = "Win32GUI"
)

setup(
    options = {"build_exe": {"includes": includes}},
    executables = [exe]
)
