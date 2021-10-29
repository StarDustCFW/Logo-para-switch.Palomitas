@echo off 
set root="C:\Program Files (x86)\WinRAR\"
cd PK
set ver=1.7
echo %ver%>V

title compile pito.py
PyInstaller pito.py -i icon.ico -y

title build exe file
%root%rar a ..\Logo-para-switch.Palomitas-v%ver%.rar * AAA dist -m5 -sfx..\SFX\My.sfx -z"..\SFX\xfs.conf" -s -k 
cd ..
cmd -k