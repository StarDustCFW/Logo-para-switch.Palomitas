@echo off
rem By Kronos2308
mode con:lines=13 cols=65
title Logo para switch by D3fau4 y Kronos2308 -.-
rmdir ips /s/q>nul
mkdir ips>nul
cls
echo               PNG To IPS Logo Creator 1.0.0-10.1.0
echo.
echo                  Give me the logo, drag it here
echo                   Dame el logo, Arrastralo aqui
echo                       "PNG" "308x350" "RGBA"
set /p "a=>"
copy %a% temp.png>nul
cls
echo Convirtiendo PNG A IPS

for /f "delims=" %%i in ('dir AAA\*/b') do (
echo Procesando en segundo plano %%i 
color 07
start /MIN pito.exe AAA\%%i temp.png
%windir%\system32\timeout 01>nul
color 0a
)
%windir%\system32\timeout 03>nul
color 07
:loop
cls
echo - %msg% -
set /a cou=0
for /f "delims= " %%i in ('tasklist /fi "imagename eq pito.exe"') do (
if /i "%%i" equ "pito.exe" set /a cou+=1
set e=%%i)
set msg= Esperando por: %cou% tareas
if /i "%e%" neq "pito.exe" goto:end
%windir%\system32\timeout 01>nul
goto:loop


:end
mkdir ips\atmosphere\exefs_patches\logo
mkdir ips\sxos\exefs_patches\logo
echo Preparando para uso
copy ips\* ips\atmosphere\exefs_patches\logo\>nul
move /y ips\* ips\sxos\exefs_patches\logo\>nul
color 0a
echo ---------------------------------------------
echo Copia el contenido de ips a la raiz de tu SD
echo ---------------------------------------------
%windir%\system32\timeout 05>nul
echo 0 >>ips\Copia_eso_de_arriba_a_la_raiz_del_sd
explorer ips
exit
