:: WINDOWS BATCH FILE
::   if running on linux, please install and run with "wine"

@ECHO off
title RUN SERVER
cls
set port=8000
:c
cls
echo "*--------------------------*"
echo "|  AvidaLab Django SERVER  |"
echo "*--------------------------*"  
echo "| 1 | PORT selection       |"
echo "| 2 | SERVER start         |"
echo "| 3 | TESTING              |"
echo "| 0 | QUITs                |"
echo "*--------------------------*"
echo Current Port = %port%
echo ______________________________
set /p ans="Please enter the selection to continue: "

:: Selects the Port to be used
if %ans%==1 (
set /p port=Select Port Number:
goto c
)

:: Runs the Server
if %ans%==2 (
python AvidaLab/manage.py runserver %port%
pause
exit
)

:: Calls another batch file for the test and runs server
if %ans%==3 (
start cmd.exe @cmd /k "cd AvidaLab/ & allTests.bat"
python AvidaLab/manage.py runserver %port%
exit
)
exit