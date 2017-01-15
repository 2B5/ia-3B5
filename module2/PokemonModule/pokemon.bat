@echo off
START easy_install pykemon
set /p name=Enter pokemon name:
echo Writing to file...
python testPokemon.py %1 %name%
echo.
choice /M "Do you want to open json file:"
IF ERRORLEVEL 2 goto exit
IF ERRORLEVEL 1 goto open_json
:open_json
start result.json
:exit
pause