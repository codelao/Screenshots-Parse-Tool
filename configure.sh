#!/bin/bash
#                         ╭━━━┳━━━┳━━━━╮
#                         ┃╭━╮┃╭━╮┃╭╮╭╮┃
#                         ┃╰━━┫╰━╯┣╯┃┃╰╯
#                         ╰━━╮┃╭━━╯ ┃┃
#                         ┃╰━╯┃┃    ┃┃
#                         ╰━━━┻╯    ╰╯
#
#                             by Lao
#                       Licensed under MIT

start() {
if [ -d "/usr/local/bin/spt" ]; then
clear
echo -e "\033[31m! SPT is already configured\nDelete 'spt' file from /usr/local/bin and try again.\033[0m"
elif [ -d "/usr/local/share/ScreenshotsParseTool" ]; then
clear
echo -e "\033[31m! SPT is already configured\nDelete 'ScreenshotsParseTool' directory from /usr/local/share and try again.\033[0m"
elif ! python3 --version; then
clear
echo -e "\033[31m! SPT requires Python3 to be installed in your system first\033[0m"
elif ! pip3 install PyQt6 requests lxml; then
clear
echo -e "\033[31m! Error installing dependencies\033[0m"
elif ! [ -d "Windows" ]; then
clear
echo -e "\033[31m! Error deleting unnecessary files"
elif ! [ -d "Unix" ]; then
clear
echo -e "\033[31m! Error deleting unnecessary files"
elif ! chmod +x Unix/spt ScreenshotsParseTool; then
clear
echo -e "\033[31m! Error giving rights\033[0m"
elif ! sudo mv Unix/spt /usr/local/bin; then
clear
echo -e "\033[31m! Error moving SPT to /usr/local/bin\033[0m"
elif ! sudo mv ScreenshotsParseTool /usr/local/share; then
clear
echo -e "\033[31m! Error moving SPT to /usr/local/share\033[0m"
else
rm Windows
rm Unix
echo -e "\033[32mSPT successfully configured.\033[0m"
fi
}


start
