#!/bin/bash

export LC_CTYPE=en_US.UTF-8
clear

banner() {
printf "      #######        ##### ##      /###           /\n" 
printf "    /       ###   ######  /###    /  ############/ \n"  
printf "   /         ##  /#   /  /  ###  /     #########   \n"    
printf "   ##        #  /    /  /    ### #     /  #        \n"         
printf "    ###             /  /      ##  ##  /  ##        \n"         
printf "   ## ###          ## ##      ##     /  ###        \n"         
printf "    ### ###        ## ##      ##    ##   ##        \n"         
printf "      ### ###    /### ##      /     ##   ##        \n"         
printf "        ### /## / ### ##     /      ##   ##        \n"         
printf "          #/ /##   ## ######/       ##   ##        \n"         
printf "           #/ ##   ## ######         ##  ##        \n"         
printf "            # /    ## ##              ## #      /  \n"   
printf "  /##        /     ## ##               ###     /   \n"    
printf " /  ########/      ## #/                ######/    \n"     
printf "/     #####        ## /                   ###      \n" 
printf "                     \033[1;31mby Lao\033[0m       \n"
printf "               \033[31mLicensed under MIT\033[0m   \n"
}

installation() {
if ! python3 --version; then
    clear
    printf "\033[31m! Script can't check Python3 version before continuing\033[0m\n"
    exit 1
else
    if ! git clone https://github.com/codelao/Screenshots-Parse-Tool.git; then
        clear
        printf "\033[31m! Script can't clone SPT repository\033[0m\n"
        exit 1
    else
        if ! pip3 install Screenshots-Parse-Tool/.; then
            clear
            printf "\033[31m! Pip can't install SPT\033[0m\n"
            exit 1
        else
            rm -rf Screenshots-Parse-Tool
            printf "\033[32mSPT successfully installed.\033[0m\n"
            exit 0
        fi
    fi
fi
}


banner
installation
