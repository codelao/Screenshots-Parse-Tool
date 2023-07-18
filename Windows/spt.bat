@echo off

python3 %ProgramData%\ScreenshotsParseTool\scripts\menu.py
if %ERRORLEVEL% == 0 (
    exit 0
) else (
    cls
    echo ! Process or startup error
)
