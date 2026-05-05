@echo off
set LOCALHOST=%COMPUTERNAME%
if /i "%LOCALHOST%"=="ShunoDator" (taskkill /f /pid 14312)
if /i "%LOCALHOST%"=="ShunoDator" (taskkill /f /pid 22536)
if /i "%LOCALHOST%"=="ShunoDator" (taskkill /f /pid 13204)
if /i "%LOCALHOST%"=="ShunoDator" (taskkill /f /pid 23596)

del /F cleanup-ansys-ShunoDator-23596.bat
