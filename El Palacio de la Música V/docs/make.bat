@ECHO OFF
REM make.bat limpio y compatible con cualquier Python

pushd "%~dp0"

REM Ruta fija al Python que tiene Sphinx instalado
set "PYTHON=C:\Program Files\Python\Python314\python.exe"

set "SOURCEDIR=source"
set "BUILDDIR=build"

"%PYTHON%" -m sphinx --version >NUL 2>NUL
if errorlevel 1 (
    echo.
    echo No se encontró sphinx usando python -m sphinx
    echo Verificá que esté instalado en este Python:
    echo "%PYTHON%" -m pip show sphinx
    exit /b 1
)

if "%1"=="" goto help

CALL "%PYTHON%" -m sphinx -M %1 "%SOURCEDIR%" "%BUILDDIR%"
goto end

:help
CALL "%PYTHON%" -m sphinx -M help "%SOURCEDIR%" "%BUILDDIR%"

:end
popd
