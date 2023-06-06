@echo off
rem                         ╭━━━┳━━━┳━━━━╮
rem                         ┃╭━╮┃╭━╮┃╭╮╭╮┃
rem                         ┃╰━━┫╰━╯┣╯┃┃╰╯
rem                         ╰━━╮┃╭━━╯ ┃┃
rem                         ┃╰━╯┃┃    ┃┃
rem                         ╰━━━┻╯    ╰╯
rem
rem                            by Lao
rem                      Licensed under MIT

python3 --version
if %ERRORLEVEL% == 0 (
    pip3 install PyQt6 requests lxml
    cls
    python3 app/menu.py
) else (
    color 04
    echo App requires Python3 to be installed in your system first.
)
