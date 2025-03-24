from cx_Freeze import setup, Executable

setup(
    name = "Calculator",
    version = "0.1",
    description = "None",
    # если приложение консольное то пишем - base=None
    # если приложение с графическим интерфейсом то пишем - base='Win32GUI'
    executables = [Executable("main.py" , base="Win32GUI" , icon="icon_py.ico")]
)