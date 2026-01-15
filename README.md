<p align="center">
  <img src="https://i.imgur.com/L3TYF0n.png" width="75%">
</p>

<h1 align="center">
  SPT
</h1>

* [Usage](#usage)
  * [Disclaimer](#disclaimer)
  * [Important notice](#important-notice-for-all-users-of-spt)
* [Installation](#installation)
* [Uninstallation](#uninstallation)
* [Popular errors](#popular-errors)


### Themes:
#### macOS
<p style="white-space: nowrap;">
 <img src="https://i.imgur.com/xuX7zhk.png" width="30%">
 <img src="https://i.imgur.com/fa1fx77.png" width="30%">
</p>

#### Windows
<p style="white-space: nowrap;">
 <img src="https://i.imgur.com/RiLIt8V.png" width="30%">
 <img src="https://i.imgur.com/TnIQIIh.png" width="30%">
</p>

#### Linux
<p style="white-space: nowrap;">
 <img src="https://i.imgur.com/WwQN824.png" width="30%">
 <img src="https://i.imgur.com/0YHHAV1.png" width="30%">
</p>

### Parsing:
<img src="https://i.imgur.com/8y94Cui.png" width="40%"></br>
<img src="https://i.imgur.com/EogpkyV.png" width="40%"></br>
<img src="https://i.imgur.com/p0LkeAo.png" width="40%">

### Output folders:
<img src="https://i.imgur.com/gvsGjgz.png" width="60%">


## Usage
SPT (Screenshots Parse Tool) "exploits" the «Lightshot» app's option of saving screenshots to the public cloud. This app is pretty popular and that's why it has over 4 billion public screenshots saved by users on purpose or by accident.
SPT generates unique links to this screenshots, parses them and after saves them to the auto-created directory on your Desktop. You can see how it looks [here](#directories). 

### Disclaimer! 
**This application does NOT exploit any real vulnerabilities which lead to unathorized access to private materials of other users in the internet. All information that could be possibly obtained through this application is publicly available. Author is not responsible for any attempts of using it for malicious purposes.**

### Important notice for all users of SPT
Please note that only you are responsible for any actions made within this tool.

Also, be aware that some people can use the feature of this tool in order to deceive the users by posting fake enticing screenshots, for example, containing login data to some unknown and unsafe website. Avoid getting caught in your own web.


## Installation
### macOS/Linux
*Note:* you need to have Python3 and Git installed in your system before moving to the program installation steps.
#### Manual installation
1. Download [install.sh](https://github.com/codelao/Screenshots-Parse-Tool/releases) script from the latest release.
2. Open terminal in the directory with downloaded script and run the following command:
```
bash install.sh
```
3. Finally, now you can always run SPT using this command:
```
spt
```

#### Easy installation
*This method requires 'wget' to be installed in your system first.*
1. Run the following command:
```
wget https://github.com/codelao/Screenshots-Parse-Tool/raw/main/install.sh && bash install.sh
```
2. Finally, now you can always run SPT using this command:
```
spt
```

### Windows 10, 11
*Note:* you need to have Python3 and Git installed in your system before moving to the program installation steps.
#### Manual installation
1. Download [install.bat](https://github.com/codelao/Screenshots-Parse-Tool/releases) script from the latest release.
2. Open cmd in the directory with downloaded script and run the following command:
```
install
```
3. Finally, now you can always run SPT using this command:
```
spt
```
*Note:* you might face popular Windows error while running the program for the first time. You can easily fix it using the command listed [here](#installation-errors).

#### Easy installation
*This method requires 'wget' to be installed in your system first.*
1. Run the following command:
```
wget https://github.com/codelao/Screenshots-Parse-Tool/raw/main/install.bat && install
```
2. Finally, now you can always run SPT using this command:
```
spt
```
*Note:* you might face popular Windows error while running the program for the first time. You can easily fix it using the command listed [here](#installation-errors).


## Uninstallation
As installation scripts automatically delete all unnecessary files, you can uninstall SPT only using this command:
```
pip3 uninstall Screenshots-Parse-Tool
```


## Popular errors
### Installation errors:
- '*WARNING: The script spt.exe is installed in '\your\path\here' which is not on PATH.*
*Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.*'

**This error usually occurs on Windows.**
**You can fix it using this command:**
```
setx PATH "%PATH%;\your\path\here"
```
**Replace '*\your\path\here*' with the real path, which is specified in the error message.**

### Program errors:
- '*Check your internet connection or try again.*'
- Program crashes after clicking on ***Launch*** button

**This errors may occure not only because you don't have internet connection, but also because your internet is too slow.**

- Conflict between **PyQt5** and **PyQt6**

**If program doesn't work because you have PyQt5 installed in your system, you should fully uninstall it before running the program next time.**

### System errors:
- Nothing happens or an error occurs after running SPT

**In this case you should try reinstalling SPT. Please, make sure that you don't get any installation errors.**
**If you still can't fix this error, please report a bug [here](https://github.com/codelao/Screenshots-Parse-Tool/issues).**

- Program crashes during parsing process

**This error may occure because your internet connection is too slow.**

#### Note:
**Connecting your computer to the mobile internet can also cause problems with the program.**
