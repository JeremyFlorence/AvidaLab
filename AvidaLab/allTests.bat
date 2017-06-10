@ECHO off

title Django Tests
echo Waiting for server to Run...
set time=2
:loop
set /a time=%time%-1
if %time%==0 goto tests
echo %time%
ping localhost -n 2 > nul
goto loop
:tests
coverage run manage.py test && coverage report