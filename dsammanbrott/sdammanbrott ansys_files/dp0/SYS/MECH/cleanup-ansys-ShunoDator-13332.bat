@echo off
set LOCALHOST=%COMPUTERNAME%
if /i "%LOCALHOST%"=="ShunoDator" (taskkill /f /pid 12320)
if /i "%LOCALHOST%"=="ShunoDator" (taskkill /f /pid 27964)
if /i "%LOCALHOST%"=="ShunoDator" (taskkill /f /pid 7612)
if /i "%LOCALHOST%"=="ShunoDator" (taskkill /f /pid 13332)

del /F cleanup-ansys-ShunoDator-13332.bat
