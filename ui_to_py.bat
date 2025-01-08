@echo off
REM 啟動虛擬環境
call C:\Users\tec\Desktop\Jacky_Obsidian_HiPoint\Code\Python_Pyside6_PLC\env\Scripts\activate

REM 轉換 UI 文件
echo Converting UI file...
pyside6-uic main_window.ui -o main_window.py

REM 轉換 QRC 文件
echo Converting QRC file...
pyside6-rcc resource.qrc -o resource_rc.py

pause