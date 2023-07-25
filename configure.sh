#!/bin/bash

export LC_CTYPE=en_US.UTF-8

banner() {
printf "╭━━━┳━━━┳━━━━╮\n"
printf "┃╭━╮┃╭━╮┃╭╮╭╮┃\n"
printf "┃╰━━┫╰━╯┣╯┃┃╰╯\n"
printf "╰━━╮┃╭━━╯ ┃┃\n"
printf "┃╰━╯┃┃    ┃┃\n"
printf "╰━━━┻╯    ╰╯\n"
printf "\033[1;31mby Lao\033[0m\n"
printf "\033[31mLicensed under MIT\033[0m\n"
}


installation() {
delete_error="\033[31m! Error deleting unnecessary files\033[0m"
if [ -d "/usr/local/bin/spt" ]; then
clear
echo -e "\033[31m! SPT is already configured\nDelete 'spt' file from /usr/local/bin and try again.\033[0m"
exit 1
elif [ -d "/usr/local/share/ScreenshotsParseTool" ]; then
clear
echo -e "\033[31m! SPT is already configured\nDelete 'ScreenshotsParseTool' directory from /usr/local/share and try again.\033[0m"
exit 1
elif ! python3 --version; then
clear
echo -e "\033[31m! SPT requires Python3 to be installed in your system first\033[0m"
exit 1
elif ! pip3 install PyQt6 requests lxml setproctitle; then
clear
echo -e "\033[31m! Error installing dependencies\033[0m"
exit 1
elif ! [ -d "Windows" ]; then
clear
echo -e $delete_error
exit 1
elif ! [ -d "Unix" ]; then
clear
echo -e $delete_error
exit 1
elif ! [ -f "configure.bat" ]; then
clear
echo -e $delete_error
exit 1
elif ! [ -f "README.md" ]; then
clear
echo -e $delete_error
exit 1
elif ! [ -f "CHANGELOG.md" ]; then
clear
echo -e $delete_error
exit 1
elif ! [ -d "readme_images" ]; then
clear
echo -e $delete_error
exit 1
elif ! [ -f "LICENSE" ]; then
clear
echo -e $delete_error
exit 1
elif ! sudo mv Unix/spt /usr/local/bin; then
clear
echo -e "\033[31m! Script don't have enough rights to move SPT files to /usr/local/bin\033[0m"
exit 1
elif ! sudo mv ScreenshotsParseTool /usr/local/share; then
clear
echo -e "\033[31m! Script don't have enough rights to move SPT files to /usr/local/share\033[0m"
exit 1
elif ! chmod +x /usr/local/share/ScreenshotsParseTool /usr/local/bin/spt; then
clear
echo -e "\033[31m! Error giving execution rights to SPT files\033[0m"
exit 1
else
rm -r Windows
rm -r Unix
rm -r readme_images
rm configure.bat
rm README.md
rm CHANGELOG.md
rm LICENSE
echo -e "\033[32mSPT successfully configured.\033[0m"
exit 0
fi
}


banner
installation
