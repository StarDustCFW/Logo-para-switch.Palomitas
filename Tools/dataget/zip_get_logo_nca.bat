@echo off
SETLOCAL EnableDelayedExpansion
title AUNPSK ALL
cd /d %~dp0
if not exist -.-\prod.keys (
echo.
echo ------------------------
echo No existen las prod.keys 
echo -----------------------
echo.
pause
exit
)

title Extrayendo %1
-.-\unzip -j %1 -d "nca"

title Extraer nca para Logo...
echo Extraer nca para Logo...
for /F %%I IN ('dir /b "nca\*.nca"') DO ( call :ncainf nca\%%I %1)

:end
rmdir /s/q nca
echo extraido
title Completado


pause
exit
:ncainf
for /f "delims=" %%i in ('.\-.-\hactool.exe -i -k .\-.-\prod.keys %1') do (
	set z=%%i
rem echo %%i
	if "!z:~0,11!" == "Content ID:" set f=!z:~12!
	if "!z:~0,9!" == "Title ID:" set a=!z:~-16!
	if "!z:~0,13!" == "Content Type:" set c=!z:~36!
rem	if "!z:~0,29!" == "Application Version(APP_VER):" set c=A!z:~30,2!!z:~33!

)
title !a! %1

if !a! equ 010000000000002d (
    if "%c%" neq "Meta" (
        echo %1
        -.-\hactool.exe -x -k -.-\prod.keys --exefsdir="Data\%~n2" "%1"
        py dataget.py "Data\%~n2"
        goto:end
    )
)
exit /b
