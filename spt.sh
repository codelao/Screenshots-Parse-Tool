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

set -e

pip3 install PyQt6 requests lxml
clear
python3 app/menu.py