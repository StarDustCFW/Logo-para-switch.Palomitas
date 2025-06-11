@echo off 
set upx=%~dp0Tools\upx-4.2.4-win64
title compile Mandanga.py
rem PyInstaller Mandanga.py --windowed -i icon.ico -y 

    pyinstaller --noconfirm --onefile --upx-dir %upx%  --noconsole --icon "icon.ico" --add-data "data.txt;." --add-data "logo.png;." --add-data "temp.png;." --add-data "open-folder.png;." --add-data "icon.ico;."  "Logo-para-switch.Palomitas.py"



timeout 10
exit

