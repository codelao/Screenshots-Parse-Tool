@echo off

chcp 65001

:banner
echo ╭━━━┳━━━┳━━━━╮
echo ┃╭━╮┃╭━╮┃╭╮╭╮┃
echo ┃╰━━┫╰━╯┣╯┃┃╰╯
echo ╰━━╮┃╭━━╯ ┃┃
echo ┃╰━╯┃┃    ┃┃
echo ╰━━━┻╯    ╰╯
echo by Lao
echo Licensed under MIT


:installation
set delete_error=! Error deleting unnecessary files
if exist %ProgramData%\ScreenshotsParseTool (
cls
echo ! SPT is already configured
echo Delete 'ScreenshotsParseTool' directory from %ProgramData% and try again.
exit /b 1
) else if exist %systemroot%\System32\spt.bat (
cls
echo ! SPT is already configured
echo Delete 'spt.bat' file from %systemroot%\System32 and try again.
exit /b 1
) else (
python3 --version
if not %errorlevel% == 0 (
cls
echo ! SPT requires Python3 to be installed in your system first
exit /b 1
) else (
pip3 install PyQt6 requests lxml setproctitle
if not %errorlevel% == 0 (
cls
echo ! Error installing dependencies
exit /b 1
) else if not exist Windows (
cls
echo %delete_error%
exit /b 1
) else if not exist Unix (
cls
echo %delete_error%
exit /b 1
) else if not exist configure.sh (
cls
echo %delete_error%
exit /b 1
) else if not exist README.md (
cls
echo %delete_error%
exit /b 1
) else if not exist CHANGELOG.md (
cls
echo %delete_error%
exit /b 1
) else if not exist readme_images (
cls
echo %delete_error%
exit /b 1
) else if not exist LICENSE (
cls
echo %delete_error%
exit /b 1
) else if not exist .gitignore (
cls
echo %delete_error%
exit /b 1
) else if not exist .git (
cls
echo %delete_error%
exit /b 1
) else (
move Windows\spt.bat %systemroot%\System32
if not %errorlevel% == 0 (
cls
echo ! Script don't have enough rights to move SPT files to %systemroot%\System32
exit /b 1
) else (
move ScreenshotsParseTool %ProgramData%
if not %errorlevel% == 0 (
cls
echo ! Error moving SPT files to %ProgramData%
exit /b 1
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
exit /b 0
)
)
)
)
)


:banner
:installation
