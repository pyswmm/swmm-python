::
::  before_build.bat - Prepares for swmm toolkit and output module builds
::
::  Date Created: 12/21/2018
::
::  Author: Michael E. Tryby
::          US EPA - ORD/NRMRL
::

set PROJECT_PATH=%~1

set TOOLKIT_PATH=\swmm_python\toolkit\swmm\toolkit
set OUTPUT_PATH=\swmm_python\output\swmm\output


mkdir buildlib
cd buildlib
git clone --branch=feature-wrapper https://github.com/michaeltryby/Stormwater-Management-Model.git swmm
cd swmm


mkdir buildprod
cd buildprod
cmake -G"Visual Studio 14 2015 Win64" -DBUILD_TESTS=0 ..
cmake --build . --config Release


copy /Y .\bin\Release\swmm5.dll  %PROJECT_PATH%\%TOOLKIT_PATH%
copy /Y .\lib\Release\swmm5.lib  %PROJECT_PATH%\%TOOLKIT_PATH%
copy /Y ..\include\*.h  %PROJECT_PATH%\%TOOLKIT_PATH%

copy /Y .\bin\Release\swmm-output.dll  %PROJECT_PATH%\%OUTPUT_PATH%
copy /Y .\lib\Release\swmm-output.lib  %PROJECT_PATH%\%OUTPUT_PATH%
copy /Y ..\tools\swmm-output\include\*.h  %PROJECT_PATH%\%OUTPUT_PATH%

cd %PROJECT_PATH%
