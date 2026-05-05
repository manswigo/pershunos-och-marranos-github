@echo off
set LOCALHOST=%COMPUTERNAME%
if /i "%LOCALHOST%"=="ShunoDator" (taskkill /f /pid 16468)
if /i "%LOCALHOST%"=="ShunoDator" (taskkill /f /pid 13028)
if /i "%LOCALHOST%"=="ShunoDator" (taskkill /f /pid 17288)
if /i "%LOCALHOST%"=="ShunoDator" (taskkill /f /pid 13212)

del /F cleanup-ansys-ShunoDator-13212.bat
