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
python3 --version > nul 2>&1
if not %errorlevel% == 0 (
    cls
    echo ! Sript can't check Python3 version before continuing
    exit /b 1
) else (
    git clone https://github.com/codelao/Screenshots-Parse-Tool.git > nul 2>&1
    if %errorlevel% == 0 (
        pip3 install Screenshots-Parse-Tool\. > nul 2>&1
        if %errorlevel% == 0 (
            rmdir /s /q Screenshots-Parse-Tool
            echo SPT successfully installed.
            exit /b 0
        ) else (
            cls
            echo ! Pip can't install SPT package
            exit /b 1
        )
    ) else (
        cls
        echo ! Script can't clone SPT repository
        exit /b 1
    )
)


:banner
:installation
