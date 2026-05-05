@echo off
set LOCALHOST=%COMPUTERNAME%
if /i "%LOCALHOST%"=="ShunoDator" (taskkill /f /pid 16064)
if /i "%LOCALHOST%"=="ShunoDator" (taskkill /f /pid 2248)
if /i "%LOCALHOST%"=="ShunoDator" (taskkill /f /pid 22000)
if /i "%LOCALHOST%"=="ShunoDator" (taskkill /f /pid 9636)

del /F cleanup-ansys-ShunoDator-9636.bat
