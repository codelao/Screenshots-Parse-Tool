@echo off

chcp 65001
cls

:banner
echo       #######        ##### ##      /###           / 
echo     /       ###   ######  /###    /  ############/  
echo    /         ##  /#   /  /  ###  /     #########    
echo    ##        #  /    /  /    ### #     /  #         
echo     ###             /  /      ##  ##  /  ##         
echo    ## ###          ## ##      ##     /  ###         
echo     ### ###        ## ##      ##    ##   ##         
echo       ### ###    /### ##      /     ##   ##         
echo         ### /## / ### ##     /      ##   ##         
echo           #/ /##   ## ######/       ##   ##         
echo            #/ ##   ## ######         ##  ##         
echo             # /    ## ##              ## #      /   
echo   /##        /     ## ##               ###     /    
echo  /  ########/      ## #/                ######/     
echo /     #####        ## /                   ###  
echo                      by Lao
echo                Licensed under MIT

:installation
python3 --version
if not %errorlevel% == 0 (
    cls
    echo ! Sript can't check Python3 version before continuing
    exit /b 1
) else (
    git clone https://github.com/codelao/Screenshots-Parse-Tool.git
    if not %errorlevel% == 0 (
        cls
        echo ! Script can't clone SPT repository
        exit /b 1
    ) else (
        pip3 install Screenshots-Parse-Tool\.
        if not %errorlevel% == 0 (
            cls
            echo ! Pip can't install SPT
            exit /b 1
        ) else (
            rmdir /s /q Screenshots-Parse-Tool
            echo SPT successfully installed.
            exit /b 0
        )
    )
)


:banner
:installation
