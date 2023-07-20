@echo off

chcp 65001 > 0

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
set delete_error=! Error deleting unnecessary files
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
echo %delete_error%
) else if not exist Unix (
cls
echo %delete_error%
) else if not exist configure.sh (
cls
echo %delete_error%
) else if not exist README.md (
cls
echo %delete_error%
) else if not exist CHANGELOG.md (
cls
echo %delete_error%
) else if not exist readme_images (
cls
echo %delete_error%
) else if not exist LICENSE (
cls
echo %delete_error%
) else if not exist .gitignore (
cls
echo %delete_error%
) else if not exist .git (
cls
echo %delete_error%
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
rmdir /s /q Windows
rmdir /s /q Unix
rmdir /s /q readme_images
rmdir /s /q .git
del /f configure.sh
del /f README.md
del /f CHANGELOG.md
del /f LICENSE
del /f .gitignore
echo SPT successfully configured.
)
)
)
)
)
