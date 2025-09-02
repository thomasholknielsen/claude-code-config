@echo off
REM ~/.claude/scripts/notify-smart.bat
REM Windows batch wrapper for PowerShell notification script

REM Read from stdin and pass to PowerShell script
REM The script path is relative to this batch file
set SCRIPT_DIR=%~dp0
powershell.exe -ExecutionPolicy Bypass -File "%SCRIPT_DIR%notify-smart.ps1"