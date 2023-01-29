# DBI by **[duckbill](https://github.com/duckbill007)**
![Github latest downloads](https://img.shields.io/github/downloads/rashevskyv/dbi/total.svg)

This guide is based on [Brikachu's work](https://4pda.to/forum/index.php?showtopic=939714&st=1100#Spoil-86288632-5).

[РУССКИЙ / Russian guide](README.md)

The ultimate solution to install `NSP`, `NSZ`, `XCI` and `XCZ` and work with Nintendo Switch. Supports installation over MTP, USB, http (from your personal server), external USB and more. Support for viewing images in `jpg`, `png` and `psd` formats. Support for working with `zip` and `rar` archives, as well as with `cbr`/`cbz` containers. Support for text files, plain text view and hex view. Can be used as a file manager (copy, move, delete files and folders, create folders). Work with saves (including backup and restore) and much more.

## Content: 

1. [Installation](#installation)
1. [Usage](#usage)
  1. [Interface](#interface)
  1. [Buttons](#buttons)
  1. [Browse SD Card / Browse USB0 Drive](#browse-sd-card--browse-usb0-drive)
  1. [Install title from USB](#install-title-from-usb)
  1. [Home server](#home-server)
  1. [Browse installed applications](#browse-installed-applications)
     * [Titles Context menu](#title-context-menu)
     * [Detailed game menu](#detailed-game-menu)
       * [Records Context menu](#records-context-menu)
  1. [Cleanup orphaned files](#cleanup-orphaned-files)
  1. [Browse tickets](#browse-tickets)
     * [Tickets Context menu](#tickets-context-menu)
  1. [Browse saves](#browse-saves)
     * [Saves Context menu](#saves-context-menu)
  1. [Run MTP responder](#run-mtp-responder)
  1. [Exit](#exit)
1. [Warnings and Errors](#warnings-and-errors)
	1. [Warnings](#warnings)
	1. [Errors](#errors)
1. [dbi.config](#dbiconfig)
1. [Other options](#other-options)
1. [Acknowledgements](#acknowledgements)

## Installation 

Copy `dbi.nro` and `dbi.config` to your SD card at `sdmc:/switch/DBI/` DBI can be then be launched in either applet mode (from Album) or application mode (title override), however it is primarily designed to be used in applet mode. 

*If you have successfully launched DBI in applet mode you will see a blue background, launching in application mode will display a black background.*

## Usage 

### Interface
![2021041010520200](https://user-images.githubusercontent.com/18294541/114262830-d7643e00-99ea-11eb-8dbb-c8e0996577e5.jpg)
* **Browse SD Card** - installation of NSP/NSZ/XCI/XCZ files from your SD card
* **Browse USB0 Drive** - installation of NSP/NSZ/XCI/XCZ files from an external FAT32 or exFAT formatted USB drive (will only appear if a USB drive is connected)
* **Install title from USB** - installation of NSP/NSZ/XCI/XCZ from a PC via USB 2.0 or 3.0 cable using the included dbibackend script. *Main menu hotkey for this option*: **(Y)** button
* **Install title from Gamecard** - install a game from gamecard to the console's internal NAND or SD card (will only appear if a gamecard is inserted)
* **Home server** - install games over your local network (HTTP) using a LAN USB adapter or WiFi network. For full details see **[Home server](#home-server)**
* **Browse installed applications** - view installed titles including base, update, DLC and whether or not a LayeredFS mod is present. Launch titles directly. Displays your total play time and how many times you've launched the title. Check file integrity for errors, transfer game data between internal NAND and SD card, delete individual or multiple titles and their LayeredFS mods with one click, individually remove updates and DLC and use the `Reset Required version` function to restore the system update check for the selected game back to base. *Main menu hotkey for this option*: **(L)** button
* **Cleanup orphaned files** - removes all orphaned installed content, tickets and pending firmware updates from the system with one click
* **Browse tickets** - view and manually delete system tickets for games
* **Browse saves** - view, backup and delete game save data for all games
* **Run MTP responder** - enables DBI's internal MTP server to connect the Switch to a PC or to an Android device (Some tested phone/tablet devices: Pixel 3, Xiaomi Mi A1, Lenovo Tab 4 7 "TB-7304X). On your device you will be presented with several virtual MTP drives for installation and many advanced features for file management on your SD card and NAND. Please see **[Run MTP Responder](#run-mtp-responder)** for a full overview
* **Run FTP server** - enables DBI's FTP server for microSD file access on port 5000 or file installation on port 6000
* **Exit** - exit from the program. *Main menu hotkey for this option*: **(+)** button

The bottom left corner of DBI displays the total amount of data currently on your SD card along with the full capacity. The bottom right corner gives you the same information for your NAND's usable space in HOS.

Bottom center (dbi: XXX) is the DBI version number - you should always use the most recent version.

### Buttons

* **(А)** - select or confirm
* **(B)** - cancel, exits the program **from the main menu**
* **(X)** - file selection, hotkey for mounting MTP **on the main menu** (menu option "**Run MTP responder**")
* **(Y)** - invert selection (selects everything if nothing is selected), hotkey for launching USB installation via dbibackend **on the main menu** (menu option "**Install title from USB**")
* **(ZL)** and **(ZR)** - scroll pages in menus, scroll through individual games when in detailed game menu
* **(L)** - **on the main menu** the hotkey for the menu option "**Browse installed applications**"
* **(R)** - change the displayed sort order of files/titles
* **(L3)** - click left stick to launch games from the application list or detailed game menu
* **(+)** on the right joycon - display context menus to allow you to perform operations such as deleting, resetting the required firmware version, mounting via MTP and more
* **(-)** on the left joycon - turn the screen on/off when MTP mode is activated/when installing titles

### Browse SD Card / Browse USB0 Drive

Select these options if you want to install games, updates and DLC from files present on your SD card or from an external USB drive.
Press **(A)** to open the folder and **(B)** to return. After opening the folder containing your installation files use the **(X)** button to select single or multiple files for installation. The **(Y)** button inverts your selections and the color of the name of the selected files will change from white to light blue.

Press the **(A)** button to confirm. A window with installation options will appear:

![2021041011441100](https://user-images.githubusercontent.com/18294541/114264183-18138580-99f2-11eb-8c7b-536b4b831195.jpg)

* **Total transfer size** - the total amount of data (NSP/NSZ/XCI/XCZ files) selected for installation
* **Total install size** - the amount of free space required to install the selected files
* **Install target** - select installation location: **NAND** - internal memory of the Nintendo Switch console, **SD** - SD card, **AUTO** - by default this will install to your SD card but if you don't have enough space the installation will fall back to NAND (internal memory)
* **Delete after install** - deletes installation files (NSP/NSZ/XCI/XCZ files) from the source after they have been successfully installed; for this to work, the "Read-only" attribute must be removed from files if present. By default files are not deleted. The option is visible only when installing from an SD card/external USB drive
* **Turn off screen** - turns off the screen during installation to conserve battery, after installation successfully completes the screen will automatically turn back on. This option only works in handheld mode
* Select **Start install** to begin the installation. After a successful installation "**Installation Complete. Press B to return**" will appear

*DBI will automatically and immediately remove old updates when installing a new update for a game, so you don't have to worry about the extra space they occupy.*

You can also navigate to your homebrew files and launch .nro files directly by highlighting them and pressing **(A)**.

### Install title from USB

If you cannot use DBI's MTP responder this is another convenient method for installing titles over USB. Installing over USB allows you to transfer files directly from your PC for example, which avoids the inconvenience and of having to first move the file to your SD card and then install it.

*Main menu hotkey for this option*: **(Y)** button

In order to use this option you will first require dbibackend (`dbibackend.exe` for Windows, or the `dbibackend` script for all operating systems). Launch dbibackend, select the files to install, select Start server, connect a USB-C cable from your PC to your Switch and select **Install title from USB** in DBI.

From here you can select and install your files on the Switch in the same fashion as using Browse SD Card/Browse USB0 Drive.

To quickly send files or folders with games for installation, right-click on them, select `Send from dbibackend` and the installation files will be immediately placed in dbibackend's queue. To configure this in Windows, press `Win + R`, enter `shell: sendto` and create a shortcut for `dbibackend.exe` in the folder.

#### Dependencies that may be required to run on MacOS or Linux

```bash
brew install python-tk
pip3 install pyusb
```

### Home server

The **"Home server"** option will appear if the **Network install sources** section has been configured in **[dbi.config](#dbiconfig)**. You can specify the name of the option as required in the configuration file.

To install games over your network, edit the dbi.config file located in the `sdmc:/switch/DBI/` folder as required. For example:

```
; Network install sources
[Network sources]
; <display name>=<type>|<URL>
Home server=ApacheHTTP|http://192.168.1.47/Nintendo/Switch/
```

Install any HTTP server with DirectoryListing enabled on your PC: Apache, Mongoose, Python SimpleHTTP, sheret, rclone, etc.

Example for nginx on Windows:
Edit the file `/nginx/conf/nginx.conf`, registering the address of your Switch in `location`, instead of the `127.0.0.1` specified in the example (or your entire subnet like 192.168.1.1/24 or 192.168.0.0/16); it can be found on Switch in **System Preferences** > **Internet**:

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

For the server address in `dbi.config`, you can also use a domain name, for example, your remote VPS - suggested to use with HTTP Basic authentication e.g.: `http://user:password@host:port/Nintendo/Switch/`

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

In **Browse installed applications** you can see a list of installed programs, updates and DLC with their occupied space, version (display version and hex version), their titleID, the total game time and the number of launches and the presence of installed LayeredFS mods for the game (for Atmosphére). 

*Main menu hotkey for this option*: **(L)** button

At the top center, the total number of installed games and the sorting type is displayed.

![2021062719353200](https://user-images.githubusercontent.com/18294541/123554546-32efcd80-d789-11eb-8d3f-3124448624e0.jpg)

On the left hand side in square brackets, information on the game installation location, installed file type and the presence of LayeredFS mods or cheats is denoted:

* **N/S/M** - NAND/SD/Mixed - Location of installed files, Mixed denotes that installed files were detected on both NAND and SD card
* **b** - BASE - the base game
* **u** - Update - update installed
* **d** - DLC - DLC installed
* **l** - LayeredFS mod - LayeredFS mods or cheats for the game were detected at `sdmc:/atmosphere/contents/titleID/`

You can quick launch a game directly from the list by highlighting it and pressing **(L3)**.

**Please note!** If the game is **highlighted in red** only an update and/or DLC is installed, the game itself is NOT installed.

#### Title context menu

![2021062719354100](https://user-images.githubusercontent.com/18294541/123554557-3b480880-d789-11eb-9235-d547f2c588bd.jpg)

Displayed by clicking on **(+)** on the selected title(s).

* **Delete title** - delete selected titles
* **Move title to MicroSD/NAND** - move the selected titles to SD card or NAND, depending on where the title is currently located. If content is installed to both locations then both options will be displayed
* **Reset required version** - resets the system version check required to run the title (debug must be enabled in Atmosphere)
* **Check integrity** - checks the data integrity of the selected titles
* **Expose contents via MTP** - mount the content of the selected titles via MTP 

If you press the **(A)** button on the title, the detailed game menu will open.

### Detailed game menu

![2021062719353600](https://user-images.githubusercontent.com/18294541/123554561-400cbc80-d789-11eb-8d81-e3403f33b365.jpg)

Here you will be presented with the Game icon, **TitleID**, display title (**name**), developer/publisher (**Author**), display version (**Version**), supported languages (**Language**) and presence of a LayeredFS mod or cheat (**LFS mod**).

Here you can also see the amount of time you've spent playing the title (**Total play time**), how many times the game was launched (**Total launches**), total installation size (**Total occupied space**) as well as how much space it occupies on NAND (**Space in NAND**) and/or on SD card (**Space on MicroSD**), the size of the saves (**Total saves size**) and what language is active for the game ( **Forced Language**).

You can quick launch a game directly from here by pressing **(L3)**.

You can quickly scroll through games individually without returning to the installed applications list by using **(ZL)** and **(ZR)**.

#### Records context menu

![2021062719354800](https://user-images.githubusercontent.com/18294541/123554565-41d68000-d789-11eb-9c59-621275895075.jpg)

Displayed by clicking on **(+)** on selected records.

The top of the context window displays the number of selected records and their size.

* **Delete record** - delete selected entry
* **Move records to MicroSD/NAND** - move the selected titles to SD card or NAND, depending on where the title is currently located. If content is installed to both locations then both options will be displayed
* **Reset required version** - reset the system version check required to run the title (debug must be enabled in Atmosphere)
* **Force language** - allows you to force the game to start in the selected language. By default the game will run based on the system language, if that language is not present in the game then it will run as per the region of the console. The selected language will be displayed next to the game icon in the **Forced Language** field
* **Check integrity** - checks data integrity of selected titles
* **Expose contents via MTP** - mount the content of the selected titles by MTP

### Cleanup orphaned files

**Cleanup orphaned files** automatically cleans up unnecessary game files, files from interrupted/failed game installations, officially downloaded firmware updates and all unused game tickets if found.

### Browse tickets
View and delete unnecessary game tickets. **Ticket (or encrypted title key)** is a special encrypted unique information about the rights to launch the content of the game, which is installed in the system during the installation of each game (**000** at the end of the titleID) / update (**800** at the end of titleID) / of each DLC.

* **+** means there is an installed game
* **[c]** — common-ticket (installed game dump or update)
* **[p]** — personalized ticket (purchased from the game eShop)

Sometimes if a specific error occurs and you know exactly what you are doing, it can be removed from a specific game and its update/DLC.

In most cases it is better not to touch anything here, in order to avoid errors when starting games.


#### Tickets context menu

Displayed by clicking on **(+)** on selected tickets

The number of selected tickets is displayed at the top of the context window.

* **Delete tickets** - delete selected tickets

* **Select same game** - highlight all tickets related to the selected game

### Browse saves

View, backup and delete saves.

Saves for deleted games are highlighted in yellow.

#### Saves context menu

Displayed by clicking on **(+)** on selected saves

The number of selected saves is displayed at the top of the context window

* **Backup saves** - backup selected saves
* **Delete saves** - delete selected tickets
* **Select same game** - highlight all saves related to the selected game
* **Select all uninstalled** - select all saves for uninstalled games

### Run MTP responder 
**Run MTP responder** run the built-in DBI MTP server to connect to your PC or Android device via USB-C OTG (phone/tablet/other devices). *Main menu hotkey for this option*: **(X)**  button (same button to exit MTP mode). After successfully connecting the USB cable to the PC and starting the MTP server in DBI, you'll see the following on your computer:

![изображение](https://user-images.githubusercontent.com/18294541/114265006-054f7f80-99f7-11eb-86c9-1a20d588e616.png)

1: **External SD Card** - for viewing, copying and deleting files and folders from/to a PC and from/to your SD card. Drop a file larger than 4GB onto the SD card and DBI will automatically split the file into an archived folder which allows the Switch to see it as a single file, with this you can for example very easily add a >4GB .XCI for use in SX OS or add a >4GB movie for watching in NXMP or pPlay.

2: **NAND User** - view and copy files and folders to a PC from the Switch's internal memory USER partition (this partition is read-only).

3: **NAND System** - view and copy files and folders to a PC from the Switch's internal memory SYSTEM partition (the partition is read-only).

4: **Installed games** - all installed games are displayed from both NAND (internal memory of the Switch) and SD card. To dump installed games to your PC in NSP format, just copy the folder with the name of the game from Installed games to your PC. A common ticket with completely cleared personal information is generated based on your personalized ticket. Your dump will be in separate files - the game itself, the update and any DLC files. If cheats or mods have been installed for the game, they will be located in the `Mods & Cheats` folder. You can also dump a single combined multicontent file containing the game itself, the update and all DLC, these files are located at the root of the **Installed games** directory.

5: **MicroSD install** - Drop or copy your **NSP**/**NSZ**/**XCI** or **XCZ** files in this folder. When the transfer is complete the game will be installed on the **SD card** of your console. When installing NSZ or XCZ files, keep in mind that their actual size may differ greatly from their original size after installation: so if for example you start with 2GB free on your SD card and you do not have enough space to install an NSZ of 1GB in size, that is because NSZ and XCZ files are compressed and must be decompressed for installation.

6: **NAND install** - Drop or copy your **NSP**/**NSZ**/**XCI** or **XCZ** files in this folder. When the transfer is complete the game will be installed on the **internal memory** of your console.

7: **Saves** - Access to all save types stored in the internal memory of the Switch: accounts **(Account)**, system programs **(System)**, Background Content Asymmetric synchronized delivery and Transmission (**BCAT**, for example: events in ACNH), temporary **(Temporary)**, cache (**Cache**, for example: addons in DOOM), system BCAT **(SystemBCAT)** and Device Saves **(Device)** 

Backup, restore and manage save data for both installed and uninstalled games. You can make a backup of them by copying them to a PC and also delete saves that you no longer want or need - to do this open the folder with the name of the game you need, then delete the required save folder.
In order to restore saves, copy them to the appropriate folder from your PC. DBI does not require pre-launching the game before restoring a save.

8: **Album** - direct access to official Album screenshots and videos per game/title, similar to the official feature added in OFW 11.0.0.

9: **Gamecard** - with a gamecard inserted into the Switch you can dump to .XCI or trimmed .XCI on the PC, along with the update built into it if present. The personal RSA certificate automatically removed and is dumped separately.

After activating the MTP server on the Switch a window will appear with your account nickname and its UID, as well as the number of game saves: 

![2021041013152900](https://user-images.githubusercontent.com/18294541/114266673-27013480-9a00-11eb-81ba-f1ff1c3c5abb.jpg)

#: **Custom Storage** - If you have defined a custom virtual MTP drive in the **[dbi.config](#dbiconfig)** file it will appear here.

To turn off the MTP server and exit to the main menu, press either the **(X)** or **(B)** button.

### Exit
Exit - closes DBI and returns to either to hbmenu or bypasses hbmenu to go directly to your homescreen (this is configured in dbi.config). If DBI was launched from a title/forwarder, the program will restart or remain on a black screen

## Warnings and errors

### Warnings

* **"SIGNATURE: Invalid" / "SIGNATURE: GC-> eShop" / "HASH NOT MATCHED TO META"** are NOT ERRORS but notifications about a signature mismatch in headers, for example: conversions, custom NSPs, forwarders
* **"HASH MISMATCH"** - usually this is NOT an ERROR and the game was simply converted from an .XCI and everything is in order. If there are problems with a file redownload it and verify it with verification tools such as NSCB before installing. If the game still does not start or starts with an error try reinstalling it, or check or replace the USB cable/SD card, or use a different USB port
* **"DELTA SKIPPED"** - this is NOT an ERROR but a notification that unnecessary and unused delta fragments in the update file were skipped during installation
* **"No tickets found. Possibly this NSP was converted from XCI."** - this is NOT an ERROR and the performance of the game will not be affected. This informs you that the files do not include tickets, they may have been dumped from an .XCI file or converted to Standard Crypto
* **"WARNING title marked as Application but has AddonContent"** - this is NOT an ERROR and usually it indicates a non-standard .NSP homebrew game, for example if an AddonContent flag (DLC) was added to the Application title (main game, v0). If the application starts and works then everything is in order
* **"This application base is not stand alone. Make sure you installed update"** when installing Sparse Storage games is NOT an ERROR but a reminder that an update is required to launch these types of games. Install the latest update immediately after installing the base game

### ERRORs

* **“Read: USB communication failed”** - check/replace USB cable or try a different USB port on PC
* **"Cannot parse content meta. Corrupted file or old firmware"** - Either the file is corrupt or your firmware is too outdated to parse the meta file. Verify the file and update to the latest cfw and latest supported firmware version
* **"Can not find file for ncaid"** - The installation file of the game is corrupt (it does not contain the required .nca from the .cnmt list)
* **"Invalid PFS0 magic!"** - the file is corrupt, redownload the installation file and check its integrity
* **"Invalid NCA magic!"** - verify the file and update to the latest cfw and latest supported firmware version
* **"Received less data than expected"** or **"Installation aborted"** - data transfer error, check and if necessary replace the USB cable or use a different USB port between the Switch and the PC. Also make sure you have the most recent version of DBI installed
* **"std::bad_alloc"** - rename the file without special characters and Cyrillic in the filename and path to the file, plus make sure that you are using the latest version of DBI and update to the latest cfw and latest supported firmware version
* **"Nothing to install"** in the file selection window - rename the file without special characters, hieroglyphs or Cyrillic in the filename and path to the file
* **"INVALID LENGTH"** - check the USB-C cable connection to your USB port, try with another USB-C cable, verify the integrity of the game file and check the SD card for errors, when installing via MTP - try to run DBI in application mode (title override) holding the R button while launching a title
* **"INVALID DECOMPRESSED LENGTH"** together with **"TRANSFER ERROR"** when installing from SD card/external drives/dbibackend - free up more space on the SD card and delete unnecessary files from the card (you may experience this with more than 20,000 files on the SD card)
* **"[FAILED] Unknown error"** when installing .tik (ticket) - add the latest sigpatches for Atmosphére
* **"605: Content or placeholder path not exists"** or **"SOME CONTENTS ARE MISSING"** - broken file system on your SD card, or a non-working/low-quality flash drive. Check it in chkdsk and h2testw, if there are no errors reformat to FAT32
* **"Can not create placeholder"** - there is not enough space on the SD card/NAND, free up space and try again
* **"WARNING! Extra buffers exceeded"** - when installing via MTP - try to run DBI in application mode (title override) holding the R button while launching a title or alternatively via NSP forwarder and use a faster microSD card with a different USB cable/port
* **"No tickets found but they are required"** - incorrect (incomplete, no ticket but with titlerights) dump of the game, use another one
* **"SOME CONTENTS ARE MISSING. APPLICATION WILL BE UNUSABLE"** - container is incomplete, check the integrity of the game installation file
* **"Invalid personalized ticket"** - a dump of the game where instead of a common-ticket a personalized ticket from the console on which the game was purchased was included, obtain a proper dump
* **"No ES or other sigpatches"** - missing, outdated or bad sigpatches, obtain and install the latest versions to the correct locations 

## dbi.config
The `dbi.config` file was added starting with version 253. It is located next to DBI.nro and replaces the old flags files `dbi.default.ascii` and `dbi.network.config` and also adds several new options for easy customization of settings for the user.

Let's take a look at its contents:
```
; General settings
[General]
; Use libnx's default font for ASCII symbols
DefaultASCII=true
; Use libusbhsfs for access to USB mass storage drives connected to switch or dock
UseLibUsbHsFS=true
; Direct exit to homescreen
ExitToHomeScreen=false
; Folder where saves backups are stored
SavesFolder=sdmc:/switch/DBI/saves/
; Log "Install", "Check integrity" and "Cleanup" processes
LogEvents=false
; Folder where logs are stored
LogsFolder=sdmc:/switch/DBI/logs/
; Folder where game dumps are stored
DumpsFolder=sdmc:/switch/DBI/dumps/
; Sorting options for application list
AppSorting=LastPlayed,InstallLocation,Size,Name
; Sorting options for save list
SaveSorting=AppLastPlayed,AppName,UserUid,Size,SaveId
; Highlight files with updates to curently instaled titles in file browsers
HighlightUpdates=true
; Rotate screen upside down
RotateScreen=false
; Rotate joycons
RotateJoycon=false
; Underclock CPU in menues to reduce battery usage
OptimizeClockSpeed=false
; URL with title versions in format <id>|<rightsId>|[version]
VersionsURL=https://raw.githubusercontent.com/blawar/titledb/master/versions.txt
;VersionsURL=sdmc:/versions.txt
;Browse saves FS in Read-only mode
ROSaveFS=true
; Show "Update all items from here..." in context menu of file browsers
ShowUpdateFromHere=false
; Show cache warming spinner
ShowCacheWarmingIndicator=true
; Move cursor down after selection
MoveDownAfterX=true
; Screen idle timeout in seconds
ScreenIdleTimeout=0

; Visibility of main menu items
[MainMenu]
; Browse and install files from MicroSD card
BrowseSD=true
; Browse and copy files from SYSTEM partition
BrowseSystem=false
; Browse and copy files from USER partition
BrowseUser=false
; Browse and install files from USB flash drives and HDD
USBHost=true
; Browse and install files from PC via dbibackend
BackendInstall=true
; Install game from inserted game cartridge
GameCard=true
; Browse and install files from configured network sources
Network=true
; Browse and install files from configured sd card folders
Local=true
; Browse installed applications
BrowseApps=true
; Clean up files left from bad installs/old updates/unused tickets and so on
Cleanup=true
; Check for app updates
UpdateCheck=true
; View where you can view or delete installed tickets
Tickets=false
; View where you can view or delete game saves
Saves=true
; MTP responder
MTP=true
; FTP Server
FTP=true

[Applications]
; Whether check or not LFS mod size
CalculateLFSSize=false

; Install options
[Install]
; Check NCA hash during install
CheckHash=true
; Use chunked HTTP transfer (good in bad environments)
ChunkedTransfer=true

; MTP options
[MTP]
; Log all files, if disabled transfer shows only for files >= 2M
LogAllFiles=false
; Show or not NSP that includes base game, latest update and all DLC in single multi-title file
ShowCombinedNSP=true
; Show or not virtual "Mods & cheats" folder that redirects to sdmc:/atmosphere/contents/TITLEID
ShowMAC=true
; Use TitleID for "Mods & cheats" folder
MACasTID=true
; Show user defined shortcuts to MircoSD folders as separate storages
CustomStorages=true
; Turn screen off on start MTP mode
TurnOffScreen=false

; FTP options
[FTP]
; Turn screen off on start FTP mode
TurnOffScreen=false

;Enable or disable various MTP storages
[MTP Storages]
1: External SD Card=true
2: Nand USER=false
3: Nand SYSTEM=false
4: Installed games=true
5: MicroSD install=true
6: NAND install=true
7: Saves=true
8: Album=true
9: Gamecard=true

; Network install sources
[Network sources]
; <display name>=<type>|<URL>
; NSP Indexer=URLList|http://192.168.1.47/nspindexer/index.php?DBI
; Home server=ApacheHTTP|http://192.168.1.47/Nintendo/Switch/
; Test FTP=FTP|ftp://anonymous:password@192.168.1.24:2121/

; Main menu shortcuts to SD card locations
[Local sources]
; <display name>=<path>
Homebrew=sdmc:/switch
; Contents=sdmc:/atmosphere/contents
; DBILogs=sdmc:/switch/DBI/logs

[MTP custom storages]
; <display name>=<path>
Homebrew=sdmc:/switch/
Screenshots=sdmc:/Nintendo/Album/

; Override for display name
; <UPPERCASED TID>=<Desired name>
[Title name override]
; 010023901191C000=Naheulbeuk
```

### General settings
* **DefaultASCII** - **true** uses the standard font, **false** activates an alternative font
* **UseLibUsbHsFS** - **true** enables [libusbhsfs](https://github.com/DarkMatterCore/libusbhsfs) library to activate support for any connected external USB drives, **false** disables it
* **ExitToHomeScreen** - when **false** DBI will exit to hbmenu, when **true** DBI will exit directly to the Switch's homescreen
* **SavesFolder** - folder for storing save dumps
* **LogEvents** - enable logging for "*Install*", "*Check integrity*" and "*Cleanup*" events
* **LogsFolder** - folder for storing logs
* **DumpsFolder** - folder where game dumps are stored
* **AppSorting** - options for sorting the list of applications
* **SaveSorting** - options for sorting saves
* **HighlightUpdates** - highlights available updates for currently installed titles in DBI's file browser
* **RotateScreen** - rotate the screen 180 degrees
* **RotateJoycon** - rotate controls for rotated screen
* **OptimizeClockSpeed** - enable or disable SoC frequency optimization when idle,  disabled by default. **DO NOT** exit DBI improperly if enabled (e.g. by pressing the home button from applet mode) as default clock speeds will not be properly restored and your Switch will be laggy due to being in a low performance mode
* **VersionsURL** - accept a direct link to a file on a remote server, or to a file on a memory card. Examples: `https://raw.githubusercontent.com/blawar/titledb/master/versions.txt` или `sdmc:/versions.txt`
* **ROSaveFS** - browse saves FS in Read-only mode
* **ShowUpdateFromHere** - show "Update all items from here..." in context menu of file browsers
* **ShowCacheWarmingIndicator** - show a notification about caching information about installed programs
* **MoveDownAfterX** - move or not cursor after chacking game with (X)
* **ScreenIdleTimeout** - display timeout

### MainMenu
**Visibility of main menu options** - customize which options will appear in DBI's main menu: **true** - display in main menu, **false** - hide from main menu.

* **BrowseSD** - display **Browse SD card**, to install games from SD card
* **BrowseSystem** - browse and copy files from SYSTEM partition
* **BrowseUser** - browse and copy files from USER partition
* **USBHost** - display **Browse USB0 Drive**, to install games from a external USB drive if connected
* **BackendInstall** - display **Install title from USB**, for installing games from PC via dbibackend
* **GameCard** - display **Install title from Gamecard**, to install a game from an inserted gamecard to your console
* **Network** - display **Home server**, to install games from a configured home web server
* **Local** - show or not links to folders from the section [Local sources](#local-sources)
* **BrowseApps** - display **Browse installed applications**, to browse and manage installed applications
* **Cleanup** - display **Cleanup orphaned files**, to clean up 'orphaned' files from the SD card
* **UpdateCheck** - display "**Check for title updates**", to check for updates and DLC for installed games
* **Tickets** - display **Browse tickets**, to manage tickets
* **Saves** - display **Browse saves**, to manage save games
* **MTP** - display **Run MTP responder**, to start MTP mode
* **FTP** - display **Run FTP server**, to start FTP mode

### Applications
* **CalculateLFSSize** - enables or disables the size check for LayeredFS mods, if enabled depending on the size of the mod a delay may occur when opening a game's information screen in **Installed applications** 

### Install
* **CheckHash** - when **true**, hashes of .nca files are checked when installing games
* **ChunkedHTTP** - Use chunked HTTP transfer (good in bad environments)

### MTP
* **LogAllFiles** - **false** disables logging of all files in MTP mode, if **true** all files are logged, even those that are less than 2MB
* **ShowCombinedNSPInInstalledGames** - **false** disables display of combined (multi-title .NSP-file) titles
* **ShowMACInInstalledGames** - **false** turns off the display of the **"Mods & cheats"** directory under `Installed games` in MTP mode, which redirects to the path `sdmc:/atmosphere/contents/TITLEID/`
* **CustomStorages** - display custom virtual MTP drives defined by the user under [MTP custom storages]
* **MACasTID** - display "Mods & Cheats" folder on MTP with TitleID
* **TurnOffScreen** - automatically turns off the screen when MTP mode is activated

### [MTP Storages](#run-mtp-responder)
Define which virtual MTP drives will be displayed when MTP Responder is running on PC/Android.

**true** - display the virtual drive in MTP mode, **false** - disable the display of the virtual drive in MTP mode

### FTP
* **TurnOffScreen** - turn screen off on start FTP mode

### [Network sources](#home-server)
Enter your network installation sources for installing games over the network (via WiFi/LAN adapter).

**NSP Indexer** - address for NSP index page ([more info here](https://github.com/rashevskyv/dbi/issues/44))

### Local sources

Create menu items with quick access to the folders selected in the config on the memory card, for example:

`Homebrew Shortcut=sdmc:/switch` will create an item "**Homebrew Shortcut**" which will open the folder`sdmc:/switch`

### MTP custom storages
Define your own custom virtual MTP drives for quick access to folders on your SD card. 

Format: `<folder display name>=<path>`

For example: `Homebrew=sdmc:/switch`
In MTP mode, a `Homebrew` virtual MTP drive will now be available, which will directly open the `sdmc:/switch` folder on your SD card.

### Title name override

Allows you to change the name of the displayed title in DBI itself and in MTP mode (this can be particularly useful for e.g. Japanese games). 

For example, if you specify `10023901191C000 = Naheulbeuk`, then the application will display just` Naheulbeuk` instead of `The Dungeon of Naheulbeuk: The Amulet of Chaos`

## Other options

### Mounting the content of installed titles via MTP
Go to "*Browse installed applications*" -> Choose apps you need to mount with `X` -> Press `+` -> "*Expose contents via MTP*"

### Using DBI to Install Mods
1. Connect to your computer via MTP mode in DBI
1. Go to **Installed Games**, in the folder with the name of your game
1. Go to **Mods & Cheats** folder
1. Place your mod in the **Mods & Cheats** folder
* **Be careful**, you need to ensure that you copy the contents of the titleID folder and not the titleID folder itself! For example, you downloaded a translation for the game Cadence of Hyrule, in the form of the archive `Cadence of Hyrule.rar`. Inside this archive you see a folder with the titleID of the game - `01000B900D8B0000`. You need to extract the archive, go to the folder `01000B900D8B0000` and copy the entire **contents** of the folder to **Mods & Cheats**! Not the folder `01000B900D8B0000` itself, but everything inside it! In this example (and in most cases), that would be the `romfs` folder

### USB 3.0 

DBI supports USB 3.0. If you are using kefir, then USB 3.0 is active by default. Otherwise, you need to activate this function by uncommenting and editing the Atmosphere system settings configuration file at `sdmc:/atmosphere/config/system_settings.ini` as follows:

```
[usb]
usb30_force_enabled = u8!0x1
```

**Important** - activating USB 3.0 can interfere with bluetooth and 2.4GHz wifi connections. If you experience any connection issues with your wireless controllers or 2.4GHz wifi networks then you should not activate USB 3.0. 5GHz wifi connections should be generally unaffacted.

## Acknowledgements
Thanks to [SciresM](https://github.com/SciresM) for [hactool](https://github.com/SciresM/hactool) (licensed under [ISC](https://en.wikipedia.org/wiki/ISC_license)) - DBI uses some data struct definitions from there
