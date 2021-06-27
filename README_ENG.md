# DBI by **[duckbill](https://github.com/duckbill007)**
![Github latest downloads](https://img.shields.io/github/downloads/rashevskyv/dbi/total.svg)

This guide is based on [Brikachu's work](https://4pda.ru/forum/index.php?showtopic=939714&st=1100#entry86288632).

[РУССКИЙ / Russian guide](README.md)

The ultimate solution for NSP/NSZ/XCI installation along with many more advanced features to enhance your Nintendo Switch experience! DBI supports installation from SD card, via USB MTP, USB cable (using the dbibackend script or dbi-nsw tool), network (using your own http server) and external USB drives.

## Content: 

1. [Installation](#installation)
1. [Usage](#usage)
  1. [Interface](#interface)
  1. [Buttons](#buttons)
  1. [Browse SD Card / Browse USB0 Drive](#browse-sd-card--browse-usb0-drive)
  1. [Install title from USB](#install-title-from-usb)
  1. [Home server](#home-server)
  1. [Browse installed applications](#browse-installed-applications)
     * [Titles Context menu](#titles-context-menu)
     * [Detailed game menu](#detailed-game-menu)
       * [Records Context menu](#records-context-menu)
  1. [Cleanup orphaned files](#cleanup-orphaned-files)
  1. [Browse tickets](#browse-tickets)
     * [Tickets Context menu](#tickets-context-menu)
  1. [Browse saves](#browse-saves)
     * [Saves Context menu](#saves-context-menu)
  1. [Run MTP responder](#run-mtp-responder)
  1. [Exit](#exit)
1. [Errors and warnings](#errors-and-warnings)
	1. [Notifications](#warnings)
	1. [Errors](#errors)
1. [dbi.config](#dbiconfig)
1. [Other possibilities](#other-possibilities)
1. [Acknowledgements](#acknowledgements)

## Installation 

Copy `dbi.nro` and `dbi.config` to your SD card at `/switch/DBI/` DBI can be then be launched in either applet mode (from Album) or application mode (title override), however it is primarily designed to be used in applet mode. 

*If you have successfully launched DBI in applet mode you will see a blue background, launching in application mode will display a black background.*

## Usage 

### Interface
![2021041010520200](https://user-images.githubusercontent.com/18294541/114262830-d7643e00-99ea-11eb-8dbb-c8e0996577e5.jpg)
* **Browse SD Card** - installation of .NSP / .NSZ / .XCI files from your SD card.
* **Browse USB0 Drive** - installation of .NSP / .NSZ / .XCI files from an external FAT32 or exFAT formatted USB drive (will only appear if a USB drive is connected)
* **Install title from USB** - installation of .NSP / .NSZ / .XCI from a PC via USB 2.0 or 3.0 cable using the included dbibackend script. *Main menu hotkey for this option*: **Y** button.
* **Install title from Gamecard** - install a game from gamecard to the console's internal NAND or SD card (will only appear if a gamecard is inserted)
* **Home server** - install games over your local network (HTTP) using a LAN USB adapter or WiFi network. For full details see **[Home server](#home-server)**
* **Browse installed applications** - view installed titles including base, update, DLC and whether or not a LayeredFS mod is present. Displays your total play time and how many times you've launched the title. Check file integrity for errors, transfer game data between internal NAND and SD card, delete individual or multiple titles and their LayeredFS mods with one click, individually remove updates and DLC and use the `Reset Required version` function to restore the system update check for the selected game back to base. *Main menu hotkey for this option*: **L** button.
* **Cleanup orphaned files** - removes all orphaned installed content, tickets and pending firmware updates from the system with one click.
* **Browse tickets** - view and manually delete system tickets for games.
* **Run MTP responder** - enables DBI's internal MTP server to connect the Switch to a PC or to an Android device (Some tested phone/tablet devices: Pixel 3, Xiaomi Mi A1, Lenovo Tab 4 7 "TB-7304X). On your device you will be presented with several virtual drives for installation and many advanced features for file management on your SD card and NAND. Please see **[Run MTP Responder](#run-mtp-responder)** for a full overview.
* **Exit** - exit from the program. *Main menu hotkey for this option*: **+** button

The bottom left corner of DBI displays the total amount of data on your currently on your SD card along with the full capacity. The bottom right corner gives you the same information for your NAND's usable space in HOS.

Bottom center (dbi: XXX) is the DBI version number - you should always use the most recent version.

### Buttons

* **(А)** - select, confirm

* **(B)** - cancel. **On the main screen** - exit the program

* **(X)** - file selection. **On the main screen** - hotkey for mounting MTP (menu item "**Run MTP responder**")

* **(Y)** - invert selection, select everything if nothing is selected. **On the main screen** - installation via USB using dbibackend (menu item "**Install title from USB **")
* **(ZL)**, **(ZR)** - fast movement through the menu
* **(L)** - **on the main screen** - (menu item "**Browse installed applications**")
* **(R)** - change the order of displaying files / titles

* **(+)** on the right joycon - a context menu that allows you to perform context operations, such as deleting, resetting the required firmware version, mounting via MTP, etc.
* **(-)** on the left joycon, when installing applications, turns off / turns on the screen

### Browse SD Card / Browse USB0 Drive

Select this option if you want to install games, updates and DLC from files that exist on your SD card or external USB drive.
Press **(A)** to open the folder and **(B)** to go back. After opening the folder containing your installation files use the **(X)** button to select single or multiple files for installation. The **(Y)** button inverts your selections and the color of the name of the selected files will change from white to light blue.

Press the **(A)** button to confirm. A window with installation options will appear:

![2021041011441100](https://user-images.githubusercontent.com/18294541/114264183-18138580-99f2-11eb-8c7b-536b4b831195.jpg)

* **Total transfer size** - the total amount of data (.NSP / .NSZ / .XCI files) selected for installation.
* **Total install size** - the amount of free space required to install the selected files.
* **Install target** - data installation location: **NAND** - internal memory of the Nintendo Switch console, **SD** - SD card, **AUTO** - by default this will install to your SD card but if you don't have enough space the installation will fall back to NAND (internal memory).
* **Delete after install** - deletes installation files (.NSP / .NSZ / .XCI files) from the source after they have been successfully installed; for this to work, the "Read-only" attribute must be removed from files if present. By default, files are not deleted. The option is visible only when installing from an SD card / external USB drive.
* **Turn off screen** - turns off the screen during installation to conserve battery, after installation successfully completes the screen will automatically turn back on. This option only works in handheld mode.  
* Select **Start install** to begin the installation. After a successful installation *Installation Complete. Press B to return* will appear.

*DBI will automatically and immediately remove old updates when installing a new update for a game, so you don't have to worry about the extra space they occupy.*

### Install title from USB

If you cannot use DBI's MTP responder this is another convenient method for installing titles over USB. Installing over USB allows you to transfer files directly from your PC for example, which avoids the inconvenience and of having to first move the file to your SD card and then install it. Compared to using the MTP responder this mode will also allow direct installation of .XCI files.

*Main menu hotkey for this option*: **Y** button.

In order to use this option you will first require dbibackend (`dbibackend.exe` for Windows, `dbibackend` from `dbibackend.tar.xz` for all). Launch dbibackend, select the files to install, select Start server, connect a USB-C cable from your PC to your Switch and select **Install title from USB** in DBI.

From here you will select and install your files on the Switch in the same fashion as using Browse SD Card / Browse USB0 Drive

To quickly send files or folders with games for installation, right-click on them, select Send from dbibackend and the installation files will be immediately placed in dbibackend's queue. To configure this in Windows, press `Win + R`, enter `shell: sendto` and create a shortcut for `dbibackend.exe` in the folder.

### Home server

The **"Home server"** option will appear if the **Network install sources** section has been configured in `dbi.config` (more about this file below). You can specify the name of the option as required in the configuration file

To install games over your network, edit the dbi.config file located in the `/switch/DBI/` folder, following the example:

```
; Network install sources
[Network sources]
; <display name>=<type>|<URL>
Home server=ApacheHTTP|http://192.168.1.47/Nintendo/Switch/
```

Install any other HTTP server with DirectoryListing enabled on your PC: Apache, Mongoose, Python SimpleHTTP, sheret, rclone, etc.

Example for nginx on Windows:
edit the file `/nginx/conf/nginx.conf`, registering the address of your Switch in `location`, instead of the `127.0.0.1` specified in the example (or your entire subnet like 192.168.1.1/24 or 192.168.0.0/16); it can be found on Switch in **System Preferences** > **Internet**:

```
location / {
root html;
index index.html index.htm;
}
location /Nintendo/Switch/ {
allow 127.0.0.1;
deny all;
autoindex on;
}
```

Save the config, run `nginx.exe`, allow the program to access the network, then copy the desired game to the local `/nginx/html/Nintendo/Switch/` folder on your PC, and on the Switch select “Home server”.
You will now be presented with the usual interface for installing files and you can start installing files over the network. You can stop the web server via nginx -s stop.

FFor the server address in `dbi.config`, you can also use a domain name, for example, your remote VPS - suggested to use with HTTP Basic authentication e.g.: `http://user:password@host:port/Nintendo/Switch/`

For example:
```
ApacheHTTP|Network repo|http://127.0.0.1/Nintendo/Switch/
ApacheHTTP|WWW VPS repo|http://www.myveryownswitchvpsdomain.su/Nintendo/Switch/
```

Generate the htpasswd file, put it in /nginx/conf/, then adjust the nginx.conf file as follows:

```
        location /Nintendo/Switch/ {
			   satisfy all;
			   allow 127.0.0.1;
			   deny all;
			   auth_basic "Password Protected Area";
			   auth_basic_user_file htpasswd; 
               autoindex on;
        }
```

Login "switch", password "pwd":

htpasswd-file:
```
switch:{SHA}N/omUzCtg+qoee+x4ttjgIls9jk=
```

### Browse installed applications

In **Browse installed applications** you can see a list of installed programs, updates and DLC with their occupied space, version (display version and hex version), their titleID, the total game time and the number of launches, the presence of installed LayeredFS mods for the game (for Atmosphére). 

*Main menu hotkey for this option*: **L** button:Сверху в центре написано общее количество установленных игр и тип сортировки

At the top in the center, the total number of installed games and the type of sorting are written

![2021062719353200](https://user-images.githubusercontent.com/18294541/123554546-32efcd80-d789-11eb-8d3f-3124448624e0.jpg)

In square brackets before the name of the game, basic information about the installation location, composition and availability of the game mod is written. Only what is installed is displayed. That is, if the letter b is not in square brackets, then the game itself does not have the base part installed (in this case, the line will be colored red)

* **N / S / M** - NAND / SD / Mixed - means the place where the game is installed. If parts of the game are on different media, Mixed is displayed
* **b** - BASE - the game itself
* **u** - Update - update the game
* **d** - DLC
* **l** - LayeredFS mod - the presence of modifications, cheats or translation

**Please note!** If the game is **highlighted in red**, then its base part is not installed, but only an update or DLC is installed

#### Title context menu![2021062719354100](https://user-images.githubusercontent.com/18294541/123554557-3b480880-d789-11eb-9235-d547f2c588bd.jpg)

Displayed by clicking on **(+)** on the selected titles (or title)

* **Delete title** - delete selected titles
* **Move title to MicroSD \ NAND** - move the selected titles to NAND or to a memory card, depending on where the title is currently located. If title parts are both there and there, both options will be displayed
* **Reset required version** - reset the check of the system version required to run the title (debug must be enabled in Atmosphere)
* **Check integrity** - checking the data integrity of the selected titles
* **Expose contents via MTP** - mount the content of the selected titles by MTP 

If you press the **(A)** button on the title, the detailed game menu will open

### Detailed game menu

![2021062719353600](https://user-images.githubusercontent.com/18294541/123554561-400cbc80-d789-11eb-8d81-e3403f33b365.jpg)

Game icon, **TitleID**, title (**name**), author (**Author **), version (**Version **), supported languages (**Language **) and availability of LFS- mod (**LFS-mod **)

Here you can also find out the amount of time spent in the game (**Total play time **), how many times the game was launched (**Total launches **), how much it weighs (in general (**Total occupied space **) , as well as how much space it takes in NAND (**Space in NAND **) and on SD (**Space on MicroSD **)), the size of the saves (**Total saves size **) and what language the game has active ( **Forced Language **)

#### Records context menu

![2021062719354800](https://user-images.githubusercontent.com/18294541/123554565-41d68000-d789-11eb-9c59-621275895075.jpg)

isplayed by clicking on **(+) ** on selected records

The top of the context window displays the number of selected records and their size

* **Delete record** - delete selected entry
* **Move records to MicroSD \ NAND** - move the selected entry to NAND or to a memory card, whichever is where it is currently located. If title parts are both there and there, both options will be displayed
* **Reset required version** - reset the check of the system version required to run the title (debug must be enabled in Atmosphere)
* **Force language** - allows you to force the game to start in the selected language. By default, the game starts with the same language that is selected in the system, if there is none in the game, then depending on the region of the console. The selected language will be displayed next to the game icon in the **Forced Language ** field
* **Check integrity** - checking the data integrity of the selected titles
* **Expose contents via MTP** - mount the content of the selected titles by MTP

### Cleanup orphaned files

**Cleanup orphaned files** automatically cleans unnecessary game files, files from interrupted game installations, downloaded (officially) OFW firmware updates and all unused game tickets if found.

### Browse tickets
View and delete unnecessary game tickets. **Ticket (or encrypted title key) ** is a special encrypted unique information about the rights to launch the content of the game, which is installed in the system during the installation of each game (**000 ** at the end of the titleID) / update (**800 ** at the end of titleID) / of each DLC.

* **+** means there is an installed game
* **[c]** — common-ticket (installed game dump or update)
* **[p]** — personalized ticket (purchased from the game eShop)

Sometimes, if a specific error occurs, and you know exactly and are sure what you are doing, it can be removed from a specific game and its update / DLC.

In all other cases, it is better not to touch anything here, in order to avoid errors in starting games.


#### Tickets context menu

Displayed by clicking on **(+) ** on selected tickets

* The number of selected tickets is displayed at the top of the context window

  ***Delete tickets** - delete selected tickets

* **Select same game** - highlight all tickets related to the selected game

### Browse saves

View and delete saves.

Saves for deleted games are highlighted in yellow.

#### Saves context menu

Displayed by clicking on **(+) ** on selected saves

The number of selected saves is displayed at the top of the context window

* **Delete saves** - delete selected tickets
* **Select same game** - highlight all tickets related to the selected game
* **Select all uninstalled** - select all saves for remote games

### Run MTP responder 
**Run MTP responder** run the built-in DBI MTP server to connect to your PC or Android device via USB-C OTG (phone / tablet / other devices). *Main menu hotkey for this option*: **X**  button (same button to exit MTP mode). After successfully connecting the USB cable to the PC and starting the MTP server in DBI, you'll see the following on your computer:

![изображение](https://user-images.githubusercontent.com/18294541/114265006-054f7f80-99f7-11eb-86c9-1a20d588e616.png)

1: **External SD Card** - for viewing, copying and deleting files and folders from/to a PC and from/to your SD card. Drop a file larger than 4GB onto the SD card and DBI will automatically split the file into an archived folder, which allows the Switch to see it as a single file, with this you can for example very easily add a >4GB .xci for use in SX OS, or add a >4GB movie for watching in pPlay.

2: **NAND User** - viewing, copying files and folders on a PC from the Switch's internal memory to its USER system partition (this partition is read-only).

3: **NAND System**, viewing, copying files and folders on a PC from the internal memory of the Switch to its SYSTEM system partition (the partition is read-only).

4: **Installed games** all installed games are displayed from both in NAND (internal memory of the Switch) and SD card. To dump installed games to your PC in .NSP format, just copy the folder with the name of the game from Installed games to your PC. A common ticket with completely cleared personal information is generated based on your personalized ticket. Your dump will be in separated files - the game itself, the update and DLC. If cheats or mods have been installed for the game, they will be located in the `Mods & Cheats` folder. You can also dump a single combined multicontent file containing the game itself, the update and all DLC. This file is located right at the root of the **Installed games** section.

5: **MicroSD install** - Drop or copy your **NSP** or **NSZ** files in this folder. When the transfer is complete the game will be installed on the **SD card** of your console. When installing NSZ files, keep in mind that their actual size may differ greatly from their original size after installation: so if for example you start with 2GB free on your memory card and you do not have enough space to install an NSZ of 1GB in size, that is because NSZ files are compressed and must be decompressed for installation.

6: **NAND install** - Drop or copy your **NSP** or **NSZ** files in this folder. When the transfer is complete the game will be installed on the **internal memory** of your console. When installing NSZ files, keep in mind that their actual size may differ greatly from their original size after installation: so if for example you start with 2GB free on your memory card and you do not have enough space to install an NSZ of 1GB in size, that is because NSZ files are compressed and must be decompressed for installation.

7: **Saves** - Access to all game saves - in accounts (Account), system programs (System), in Background Content Asymmetric synchronized delivery and Transmission (BCAT, for example: events in ACNH), temporary (Temporary), cache (Cache, for example: addons in DOOM), system BCAT (SystemBCAT), - stored in the internal memory of the Switch; in the Installed games folder - save for the currently installed games, Uninstalled games - save from deleted games that were previously launched. From here, you can make a backup of them by copying them to a PC, and also delete unnecessary ones - for this, open the folder with the name of the game you need, then delete the folder with the nickname of your account / Device-save.
In order to restore the save, copy them to the appropriate folder from your PC. DBI does not require pre-launching the game to restore a save, however this only applies to regular saves. BCAT or Cache saves require a pre-launch of the game before restoring.

8: **Album** - access to screenshots and videos (Album), similar to Nintendo's feature added OFW 11.0.0.

9: **Gamecard** - with a gamecard inserted into the Switch you can dump to .XCI or trimmed .XCI on the PC, along with the update built into it if it exists. The personal RSA certificate automatically removed and is dumped separately.

After activating the MTP server on the Switch a window will appear with your account nickname and its UID, as well as the number of game saves: 

![2021041013152900](https://user-images.githubusercontent.com/18294541/114266673-27013480-9a00-11eb-81ba-f1ff1c3c5abb.jpg)

#: **Custom Storage** - If you have defined a custom MTP storage in the **[`dbi.config`](#dbiconfig)** file it will appear here.

To turn off the MTP server and exit to the main menu, press the **X** button.

### Exit
Exit - closes DBI and returns to either to hbmenu or bypasses hbmenu to go directly to your homescreen (this is configured in dbi.config). If DBI was launched from a title / forwarder, the program will restart or remain on a black screen

## Errors and warnings

### Warnings

* **«HASH MISMATCH»** — usually this is NOT an ERROR and the game was simply converted from an .XCI and everything is in order. Sometimes if there are problems with the integrity of the file, download it, rehash it, transferring data via a USB cable / port / during the installation process between the PC and the Switch.
    If the game still does not start or starts with an error, try reinstalling it again, check or replace the USB cable / SD card / change the USB port.
* **DELTA SKIPPED** — this is NOT an ERROR but a notification that unnecessary and unused delta fragments in the update file were skipped during installation.
* **«No tickets found. Possibly this NSP was converted from XCI.»** — this is NOT an ERROR and the performance of the game will not be affected. This informs you that the files do not include tickets, they may have been dumped from an .XCI file or converted to Standard Crypto.
* **«WARNING» title marked as Application but has AddonContent** — this is NOT an ERROR and usually it indicates a non-standard .NSP homebrew game, for example if an AddonContent flag (DLC) was added to the Application title (main game, v0).
    If the application starts and works then everything is in order.

### ERRORs

* **«Can not find file for ncaid»** — The installation file of the game is corrupt (it does not contain the required .nca from the .cnmt list).
* **«Invalid PFS0 magic!»** — download the installation file of the game and check its integrity, this file is corrupt.
* **«Received less data than expected»** or **Installation aborted** — data transfer error, recheck and if necessary replace the USB cable / USB port between the Switch and the PC. Also make sure you have the most recent version of the DBI installed.
* **«std::bad_alloc»** — rename the file without special characters and Cyrillic in the name and path to it, plus make sure that you are using the latest version of DBI and that the latest supported version of OFW and CFW is installed on the console.
* **«Nothing to install»** in the file selection window - rename the file without special characters, hieroglyphs or Cyrillic in the name and path to it.
* **«INVALID LENGTH»** — check the USB-C cable connection to your USB port, try with another USB-C cable, check the integrity of the game file and the SD card for errors, when installing via MTP - try to run DBI in application mode (title override) holding the R button while launching a title.
* **«[FAILED] Unknown error»** when installing .tik (ticket) - add the latest sigpatches for Atmosphére.
* **«605: Content or placeholder path not exists»** or **«SOME CONTENTS ARE MISSING»** — broken file system on your SD card, or a non-working / low-quality flash drive. Check it in chkdsk and h2testw, if there are no errors reformat to FAT32.
* **WARNING! Extra buffers exceeded**, when installing via MTP - try to run DBI in application mode (title override) holding the R button while launching a title or alternatively via NSP forwarder and use a faster microSD card with a different USB cable / port.
* **No tickets found but they are required** — incorrect (incomplete, no ticket but with titlerights) dump of the game, use another one.
* **SOME CONTENTS ARE MISSING. APPLICATION WILL BE UNUSABLE** — container is incomplete, check the integrity of the game installation file.
## dbi.config
The `dbi.config` file was added starting with version 253. It is located next to DBI.nro and replaces the old flags files `dbi.default.ascii` and `dbi.network.config` and also adds several new options for easy customization of settings for the user.

Let's take a look at its contents:
```
; General settings
[General]
; Use libnx's default font for ASCII symbols
DefaultASCII=false
; Use libusbhsfs for access to USB mass storage drives connected to switch or dock
UseLibUsbHsFS=true
; Direct exit to homescreen
ExitToHomeScreen=false

; Visibility of main menu items
[MainMenu]
; Browse and install files from MicroSD card
BrowseSD=true
; Browse and install files from USB flash drives and HDD
USBHost=true
; Browse and install files from PC via dbibackend
BackendInstall=true
; Install game from inserted game cartridge
GameCard=true
; Browse and install files from configured network sources
Network=true
; Browse installed applications
BrowseApps=true
; Clean up files left from bad installs/old updates/unused tickets and so on
Cleanup=true
; View where you can view or delete installed tickets
Tickets=false
; View where you can view or delete game saves
Saves=true
; MTP responder
MTP=true


[Applications]
; Whether check or not LFS mod size
CalculateLFSSize=true


; Install options
[Install]
; Check NCA hash during install
CheckHash=true

; MTP options
[MTP]
; Log all files, id disabled transfer shows only for files >= 4M
LogAllFiles=false
; Show or not NSP that includes base game, latest update and all DLC in single multi-title file
ShowCombinedNSP=true
; Show or not virtual "Mods & cheats" folder that redirects to sdmc:/atmosphere/contents/TITLEID
ShowMAC=true
; Show user defined shortcuts to MircoSD folders as separate storages
CustomStorages=true
; Enable NAND install if run in emunand
EnableNANDInstallOnEmunand=false
; Turn screen off on start MTP mode
TurnOffScreen=false

; Enable or disable various MTP storages
[MTP Storages]
1: External SD Card=true
2: Nand USER=true
3: Nand SYSTEM=true
4: Installed games=true
5: MicroSD install=true
6: NAND install=true
7: Saves=true
8: Album=true
9: Gamecard=true

; Network install sources
[Network sources]
; <display name>=<type>|<URL>
; Home server=ApacheHTTP|http://192.168.1.47/Nintendo/Switch/

[MTP custom storages]
; <display name>=<path>
; Homebrew=sdmc:/switch
```
### General settings
* **DefaultASCII** - **true** includes a standard font, **false** includes an alternative font
* **UseLibUsbHsFS** - **true** enables [libusbhsfs](https://github.com/DarkMatterCore/libusbhsfs) library for working with external USB drives via USB-OTG on Switch, **false** disables it.
* **ExitToHomeScreen** — if **false**, the exit from DBI occurs in the hbmenu, if **true**, to the Switch's home menu
* **Visibility of main menu items** - customize which options will appear in DBI's main menu, you can prevent an option from appearing in the main menu by editing the item to **false**

### MainMenu
Shows the corresponding menu items.

**true** - display in main menu, **false** - hide from main menu

* BrowseSD - item "**Browse SD card**, to install games from Sd card
* USBHost - item "**Browse USB0 Drive**, to install games from an external USB
* BackendInstall - item "**Install title from USB**, for installing games from PC via backend
* GameCard - item "**Install title from Gamecard**, to install the contents of the cartridge in the memory of the console
* Network - item "**Home server**, to install games from a home web server
* BrowseApps - item "**Browse installed applications**, to manage installed applications
* Cleanup - item "**Cleanup orphaned files**, to clean up" orphaned "files from the memory card
* Tickets - item "**Browse tickets**, to manage tickets
* MTP - item "**Run MTP responder**, to start MTP

### Install
* **CheckHash** — if **true**, hashes of .nca files are checked when installing games on the Switch, if **false**, no.

### Applications

* **CalculateLFSSize** — включает или отключает подсчёт размера установленных LFS-модов. Если включено, может повлиять на скорость открытия меню "*Browse installed applications*"

### MTP
* **LogAllFiles** — **false** disables logging of all files when working with MTP; if **true**, all files are logged, even those that are less than 4MB.
* **ShowCombinedNSPInInstalledGames** — **false** disables display of combined (multi-title .NSP-file) titles.
* **ShowMACInInstalledGames** — **false** turns off the display of the virtual directory **"Mods & cheats"** in the Installed games item in the MTP, redirecting along the path `/atmosphere/contents/%titleid_game%` to the memory card.
* **CustomStorages** - show or hide storages, listed on **MTP custom storages** section
* **EnableNANDInstallOnEmunand** - allows or denies the installation of games in NAND file EmuNAND (not relevant after the release of Atmosphere 0.19.3) 
* **TurnOffScreen** - отключать или нет экран консоли при подключении её в режиме MTP

### [MTP Storages](#run-mtp-responder)
Show relevant items when MTP Responder is running on PC / Android, by default all items are enabled for display.

**true** - display in MTP on PC, **false** - no

The item names correspond to the titles of the sections

### [Network sources](#home-server)
Names and addresses are set for installing games over the network (via WiFi / LAN adapter)

### MTP custom storages
Custom items for MTP mode for quick access to folders on your memory card. Format: `<folder display name> = <path>`, for example: `Homebrew = sdmc: / switch`.
In MTP mode, a `Homebrew` folder will appear, referring to the` switch` folder on your memory card

## Other possibilities

### Mounting the content of installed titles via MTP
Go to "*Browse installed applications*" -> Choose apps you need to mount with `X` -> Press `+` -> "*Expose contents via MTP*"

### Backup and restore saves

1. Connect the set-top box in MTP mode via DBI
2. Go to **Saves ** folder on your PC
3. You can either copy the saves to your PC or restore them by simply dragging them into this folder

### Using DBI to Install Mods:
1. Connect the set-top box in MTP mode via DBI
1. Go to **Installed Games**, in the folder with the name of your game
1. Go to **Mods & Cheats** folder
1. Place your mod in the **Mods & Cheats** folder
* **Be careful**, you need to put not the folder with the titleID of the game, but its contents! For example, you have downloaded the translation for the game Cadence of Hyrule, in the form of the archive `Cadence of Hyrule.rar`. Inside this archive you see a folder with the TitleID of the game - `01000B900D8B0000`. You need to unpack the archive, go to the folder `01000B900D8B0000` and copy the entire contents of the folder to **Mods & Cheats**! Not the folder `01000B900D8B0000` itself, but everything that is in it! In this example, the `romfs` folder

### USB 3.0 

DBI supports USB 3.0. If you are using kefir, then USB 3.0 is active by default. Otherwise, you need to activate this function through the Atmosphere configuration files by writing in `atmosphere \ config \ system_settings.ini`:

```
[usb]
usb30_force_enabled = u8!0x1
```

## Acknowledgements
Thanks to [SciresM](https://github.com/SciresM) for [hactool](https://github.com/SciresM/hactool) (licensed under [ISC](https://en.wikipedia.org/wiki/ISC_license)) - DBI uses some data struct definitions from there
