@echo off

python3 %ProgramData%\ScreenshotsParseTool\scripts\menu.py
if %ERRORLEVEL% == 0 (
    exit 0
) else (
    cls
    echo ! Startup error
)
