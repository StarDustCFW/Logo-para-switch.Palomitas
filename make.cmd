@echo off 
set rar="C:\Program Files\WinRAR\Rar.exe"
set upx=C:\Users\Krono\Programas\upx-4.2.4-win64
cd PYPK

title compile Mandanga.py
rem PyInstaller Mandanga.py --windowed -i icon.ico -y 
if exist C:\Users\Krono\Programas\upx-4.2.4-win64 (
    pyinstaller --noconfirm --onefile --upx-dir %upx%  --noconsole --icon "icon.ico" --add-data "data.txt;." --add-data "logo.png;." --add-data "temp.png;." --add-data "icon.ico;."  "Mandanga.py"
) else (
    pyinstaller --noconfirm --onefile --noconsole --icon "icon.ico" --add-data "data.txt;." --add-data "logo.png;." --add-data "temp.png;." --add-data "icon.ico;."  "Mandanga.py"
)
cmd -k
title build exe file
%rar% a ..\Logo-para-switch.Palomitas-v%ver%.rar * Data dist -m5 -sfx..\SFX\My.sfx -z"..\SFX\xfs.conf" -s -k 
cd ..
