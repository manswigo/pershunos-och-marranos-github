@echo off
set LOCALHOST=%COMPUTERNAME%
if /i "%LOCALHOST%"=="ShunoDator" (taskkill /f /pid 11588)
if /i "%LOCALHOST%"=="ShunoDator" (taskkill /f /pid 10812)
if /i "%LOCALHOST%"=="ShunoDator" (taskkill /f /pid 2088)
if /i "%LOCALHOST%"=="ShunoDator" (taskkill /f /pid 9628)

del /F cleanup-ansys-ShunoDator-9628.bat
