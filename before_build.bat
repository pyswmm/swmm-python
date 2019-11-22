::
::  before_build.bat - Prepares for swmm toolkit and output module builds
::
::  Date Created: 12/21/2018
::
::  Author: Michael E. Tryby
::          US EPA - ORD/NRMRL
::
:: Requires:
::     CMake
::     Visual Studio 2015
::     SWIG
::
:: Note:
::     This script must be located at the root of the project folder
:      in order to work correctly.
::


:: Determine project path and strip trailing \ from path
set "PROJECT_PATH=%~dp0"
IF %PROJECT_PATH:~-1%==\ set "PROJECT_PATH=%PROJECT_PATH:~0,-1%"

set "TOOLKIT_PATH=swmm-toolkit\swmm\toolkit"
set "OUTPUT_PATH=swmm-output\swmm\output"
set "INSTALL_PATH=.\build\install"


:: Build swmm-solver
cd swmm-solver
call tools\make.cmd /g "Visual Studio 14 2015 Win64"


:: Copy files required for python package build
copy /Y %INSTALL_PATH%\bin\swmm5.dll  %PROJECT_PATH%\%TOOLKIT_PATH%
copy /Y %INSTALL_PATH%\lib\swmm5.lib  %PROJECT_PATH%\%TOOLKIT_PATH%
copy /Y %INSTALL_PATH%\include\swmm5.h  %PROJECT_PATH%\%TOOLKIT_PATH%

copy /Y %INSTALL_PATH%\bin\swmm-output.dll  %PROJECT_PATH%\%OUTPUT_PATH%
copy /Y %INSTALL_PATH%\lib\swmm-output.lib  %PROJECT_PATH%\%OUTPUT_PATH%
copy /Y %INSTALL_PATH%\include\swmm_output*.h  %PROJECT_PATH%\%OUTPUT_PATH%


:: Generate swig wrappers
cd %PROJECT_PATH%\%TOOLKIT_PATH%
swig -python -py3 toolkit.i
cd %PROJECT_PATH%\%OUTPUT_PATH%
swig -python -py3 output.i


:: Return to project root
cd %PROJECT_PATH%
