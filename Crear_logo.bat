@echo off
rem By Kronos2308
mode con:lines=11 cols=65
title Logo para switch by D3fau4 y Kronos2308 -.-
mkdir exefs_dir>nul
rmdir ips /s/q>nul
mkdir ips>nul
cls
echo               PNG To IPS Logo Creator 1.0.0-10.0.2
echo.
echo                  Give me the logo, drag it here
echo                   Dame el logo, Arrastralo aqui
echo                       "PNG" "308x350" "RGBA"
set /p "a=>"
copy %a% temp.png>nul
cls
echo Convirtiendo PNG A IPS

for /f "delims=" %%i in ('dir AAA\*/b') do (
echo Procesando %%i 
copy AAA\%%i\main exefs_dir\main>nul
copy AAA\%%i\main.npdm exefs_dir\main.npdm>nul
color 07
pito.exe exefs_dir temp.png
color 0a
)

mkdir ips\atmosphere\exefs_patches\logo
mkdir ips\sxos\exefs_patches\logo
echo Preparando para uso
copy ips\* ips\atmosphere\exefs_patches\logo\>nul
move /y ips\* ips\sxos\exefs_patches\logo\>nul
color 0a
echo ---------------------------------------------
echo Copia el contenido de ips a la raiz de tu SD
echo ---------------------------------------------
echo 0 >>ips\Copia_eso_de_arriba_a_la_raiz_del_sd
rmdir exefs_dir /s/q
explorer ips
exit
