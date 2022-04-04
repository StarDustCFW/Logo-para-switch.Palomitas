@echo off 
set rar="C:\Program Files\WinRAR\Rar.exe"
cd PK
set ver=2.3
echo %ver%>V

title compile pito.py
rem PyInstaller pito.py -i icon.ico -y

title build exe file
%rar% a ..\Logo-para-switch.Palomitas-v%ver%.rar * Data dist -m5 -sfx..\SFX\My.sfx -z"..\SFX\xfs.conf" -s -k 
cd ..
cmd -k