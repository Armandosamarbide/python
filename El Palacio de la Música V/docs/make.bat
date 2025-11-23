@ECHO OFF
REM make.bat compatible con Python 3.13.7 (invoca sphinx como módulo)

pushd "%~dp0"

REM Ajustá la ruta si tu python está en otra ubicación
set "PYTHON=C:\Program Files\Python\Python313.7\python.exe"

REM Directorios por defecto (los que genera sphinx-quickstart)
set "SOURCEDIR=source"
set "BUILDDIR=build"

REM SPHINXBUILD usará python -m sphinx salvo que la variable esté definida
if "%SPHINXBUILD%"=="" (
    set "SPHINXBUILD=\"%PYTHON%\" -m sphinx"
)

REM Comprobación rápida: ¿funciona el comando?
%PYTHON% -m sphinx --version >NUL 2>NUL
if errorlevel 1 (
    echo.
    echo The 'sphinx-build' command was not found using python -m sphinx.
    echo Asegurate de que "%PYTHON%" existe y que Sphinx esta instalado en ese Python.
    echo Ejecuta: "%PYTHON%" -m pip show sphinx
    exit /b 1
)

if "%1"=="" goto help

REM Usamos CALL para ejecutar correctamente desde un .bat
CALL %SPHINXBUILD% -M %1 "%SOURCEDIR%" "%BUILDDIR%" %SPHINXOPTS% %O%
goto end

:help
CALL %SPHINXBUILD% -M help "%SOURCEDIR%" "%BUILDDIR%" %SPHINXOPTS% %O%

:end
popd
