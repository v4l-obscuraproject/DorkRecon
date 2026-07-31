@ECHO OFF

pushd %~dp0

REM Obscura Documentation Build Script
REM Powered by Sphinx

if "%SPHINXBUILD%" == "" (
	set SPHINXBUILD=sphinx-build
)
set SOURCEDIR=source
set BUILDDIR=build

if "%1" == "" goto help

%SPHINXBUILD% >NUL 2>NUL
if errorlevel 9009 (
	echo.
	echo. [ERROR] Sphinx build system was not found.
	echo.
	echo. Obscura documentation requires Sphinx to be installed.
	echo. Install Sphinx or set the SPHINXBUILD variable to the
	echo. correct location of the sphinx-build executable.
	echo.
	exit /b 1
)

echo.
echo Building Obscura documentation...
echo.
%SPHINXBUILD% -M %1 %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%
echo.
echo Obscura documentation build completed.
echo.
goto end

:help
echo.
echo Obscura Documentation Builder
echo.
echo Usage:
echo   make ^<target^>
echo.
echo Available targets:
echo   html       Build HTML documentation
echo   clean      Remove generated files
echo   help       Display this message
echo.
%SPHINXBUILD% -M help %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%

:end
popd
