@echo off

:banner
echo ╭━━━┳━━━┳━━━━╮
echo ┃╭━╮┃╭━╮┃╭╮╭╮┃
echo ┃╰━━┫╰━╯┣╯┃┃╰╯
echo ╰━━╮┃╭━━╯ ┃┃
echo ┃╰━╯┃┃    ┃┃
echo ╰━━━┻╯    ╰╯
echo by Lao
echo Licensed under MIT


:start
if exist %ProgramData%\ScreenshotsParseTool (
cls
echo ! SPT is already configured.
echo Delete 'ScreenshotsParseTool' directory from %ProgramData% and try again.
) else if exist %systemroot%\System32\spt.bat (
cls
echo ! SPT is already configured.
echo Delete 'spt.bat' file from %systemroot%\System32 and try again.
) else (
python3 --version
if not %errorlevel% == 0 (
cls
echo ! SPT requires Python3 to be installed in your system first
) else (
pip3 install PyQt6 requests lxml setproctitle
if not %errorlevel% == 0 (
cls
echo ! Error installing dependencies
) else if not exist Windows (
cls
echo ! Error deleting unnecessary files
) else if not exist Unix (
cls
echo ! Error deleting unnecessary files
) else if not exist configure.sh (
cls
echo ! Error deleting unnecessary files
) else (
move ScreenshotsParseTool %ProgramData%
if not %errorlevel% == 0 (
cls
echo ! Error moving SPT to %ProgramData%
) else (
move Windows\spt.bat %systemroot%\System32
if not %errorlevel% == 0 (
cls
echo ! Error moving SPT to %systemroot%\System32
) else (
rmdir /s /q Unix
rmdir /s /q Windows
del /f configure.sh
echo SPT successfully configured.
)
)
)
)
)
