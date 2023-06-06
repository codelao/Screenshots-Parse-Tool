#!/bin/bash
#                         ╭━━━┳━━━┳━━━━╮
#                         ┃╭━╮┃╭━╮┃╭╮╭╮┃
#                         ┃╰━━┫╰━╯┣╯┃┃╰╯
#                         ╰━━╮┃╭━━╯ ┃┃
#                         ┃╰━╯┃┃    ┃┃
#                         ╰━━━┻╯    ╰╯
#
#                            by Lao
#                      Licensed under MIT

if ! python3 --version; then
    echo -e "\033[31mApp requires Python3 to be installed in your system first.\033[0m"
else
    pip3 install PyQt6 requests lxml
fi

clear
python3 app/menu.py
