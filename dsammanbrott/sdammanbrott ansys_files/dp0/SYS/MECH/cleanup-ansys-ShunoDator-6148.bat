@echo off
set LOCALHOST=%COMPUTERNAME%
if /i "%LOCALHOST%"=="ShunoDator" (taskkill /f /pid 6156)
if /i "%LOCALHOST%"=="ShunoDator" (taskkill /f /pid 3644)
if /i "%LOCALHOST%"=="ShunoDator" (taskkill /f /pid 9480)
if /i "%LOCALHOST%"=="ShunoDator" (taskkill /f /pid 6148)

del /F cleanup-ansys-ShunoDator-6148.bat
