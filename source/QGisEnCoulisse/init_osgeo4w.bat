
rem @echo off
rem Root OSGEO4W home dir to the same directory this script exists in
set OSGEO4W_ROOT=c:\osgeo4w
rem Convert double backslashes to single
rem set OSGEO4W_ROOT=%OSGEO4W_ROOT:\\=\%
echo. & echo OSGEO4W home is %OSGEO4W_ROOT% & echo.

set PATH=%OSGEO4W_ROOT%\bin;%PATH%
set PATH=%OSGEO4W_ROOT%\apps\qgis-ltr\bin;%PATH%

rem Add application-specific environment settings
for %%f in ("%OSGEO4W_ROOT%\etc\ini\*.bat") do call "%%f"

rem List available o4w programs
rem but only if osgeo4w called without parameters
rem @echo on
rem @if [%1]==[] (echo run o-help for a list of available commands & cmd.exe /k) else (cmd /c "%*")



call “%OSGEO4W_ROOT%“\bin\o4w_env.bat
rem call “%OSGEO4W_ROOT%“\apps\grass\grass-6.4.2\etc\env.bat
rem set GDAL_DRIVER_PATH=%OSGEO4W_ROOT%\bin\gdalplugins\1.9
path %PATH%;%OSGEO4W_ROOT%\apps\qgis-ltr\bin
rem path %PATH%;%OSGEO4W_ROOT%\apps\grass\grass-6.4.2\lib
path %PATH%;”%OSGEO4W_ROOT%\apps\Python27\Scripts\”
set PYTHONPATH=%PYTHONPATH%;%OSGEO4W_ROOT%\apps\qgis-ltr\python;%OSGEO4W_ROOT%\bin
set PYTHONPATH=%PYTHONPATH%;%OSGEO4W_ROOT%\apps\Python27\Lib\site-packages
set QGISPATH=%OSGEO4W_ROOT%\apps\qgis-ltr

