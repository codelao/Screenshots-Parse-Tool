@echo off
rem                ╭━━━┳━━━┳━━━━╮
rem                ┃╭━╮┃╭━╮┃╭╮╭╮┃
rem                ┃╰━━┫╰━╯┣╯┃┃╰╯
rem                ╰━━╮┃╭━━╯ ┃┃
rem                ┃╰━╯┃┃    ┃┃
rem                ╰━━━┻╯    ╰╯
rem
rem                    by Lao
rem              Licensed under MIT

:start 
if exist %ProgramData%\ScreenshotsParseTool (
cls
echo ! SPT is already configured.
echo Delete 'ScreenshotsParseTool' directory from %ProgramData% and try again.
) else if exist %USERPROFILE%\Desktop\"Screenshots Parse Tool.exe" (
cls
echo ! SPT is already configured.
echo Delete 'Screenshots Parse Tool.exe' file from %USERPROFILE%\Desktop and try again.
) else (
python3 --version
if not %errorlevel% == 0 (
cls
echo ! SPT requires Python3 to be installed in your system first
) else (
pip3 install PyQt6 requests lxml
if not %errorlevel% == 0 (
cls
echo ! Error installing dependencies
) else if not exist Windows (
cls
echo ! Error deleting unnecessary files
) else if not exist Unix (
cls
echo ! Error deleting unnecessary files
) else (
move ScreenshotsParseTool %ProgramData%
if not %errorlevel% == 0 (
cls
echo ! Error moving SPT to %ProgramData%
) else (
move Windows\"Screenshots Parse Tool.exe" %userprofile%\Desktop
if not %errorlevel% == 0 (
cls
echo ! Error moving SPT to %userprofile%\Desktop
) else (
rmdir /s /q Unix
rmdir /s /q Windows
echo SPT successfully configured.
)
)
)
)
)
