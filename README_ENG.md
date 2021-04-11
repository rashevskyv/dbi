# DBI by **[duckbill](https://github.com/duckbill007)**
![Github latest downloads](https://img.shields.io/github/downloads/rashevskyv/dbi/total.svg)

This guide is based on [Brikachu's work](https://4pda.ru/forum/index.php?showtopic=939714&st=1100#entry86288632).

[РУССКИЙ / Russian guide](README.md)

The ultimate solution for NSP/NSZ/XCI installation along with many more advanced features to enhance your Nintendo Switch experience! DBI supports installation via MTP, USB (using DBI backend script or dbi-nsw tool), network (using your own http server) and external USB drives.

## Content: 

1. [Installation](#installation)
1. [Usage](#usage)
	1. [Interface](#interface)
	1. [Browse SD Card / Browse USB0 Drive](#browse-sd-card--browse-usb0-drive)
	1. [Install title from USB](#install-title-from-usb)
	1. [Home server](#home-server)
	1. [Browse installed applications](#browse-installed-applications)
	1. [Cleanup orphaned files](#cleanup-orphaned-files)
	1. [Browse tickets](#browse-tickets)
	1. [Run MTP responder](#run-mtp-responder)
	1. [Exit](#exit)
1. [Errors and warnings](#errors-and-warnings)
	1. [Notifications](#warnings)
	1. [Errors](#errors)
1. [dbi.config](#dbiconfig)

## Installation 

Copy `dbi.nro` and `dbi.config` to your SD card at `/switch/DBI/`. DBI can be then be launched in either applet mode (from Album) or application mode (title override), however it is primarily designed to be used in applet mode. 

*If you have successfully launched DBI in applet mode you will see a blue background, launching in application mode will display a black background.*

## Usage 

### Interface
![2021041010520200](https://user-images.githubusercontent.com/18294541/114262830-d7643e00-99ea-11eb-8dbb-c8e0996577e5.jpg)
* **Browse SD Card** — installation of .NSP / .NSZ / .XCI files from your SD card.
* **Browse USB0 Drive** — installation of .NSP / .NSZ / .XCI files from an external FAT32 or exFAT formatted USB drive (will only appear if a USB drive is connected)
* **Install title from USB** — installation of .NSP / .NSZ / .XCI from a PC via USB 2.0 or 3.0 cable using the included dbibackend script. *Main menu hotkey for this option*: **Y** button.
* **Install title from Gamecard** — install a game from gamecard to the console's internal NAND or SD card (will only appear if a gamecard is inserted)
* **Home server** — install games over your local network (HTTP) using a LAN USB adapter or WiFi network. For full details see https://github.com/rashevskyv/dbi/blob/main/README_ENG.md#home-server
* **Browse installed applications** — view installed titles including base, update, DLC and whether or not a LayeredFS mod is present. Displays your total play time and how many times you've launched the title. Check file integrity for errors, transfer game data between internal NAND and SD card, delete individual or multiple titles and their LayeredFS mods with one click, individually remove updates and DLC and use the `Reset Required version` function to restore the system update check for the selected game back to base. *Main menu hotkey for this option*: **L** button.
* **Cleanup orphaned files** — removes all orphaned installed content, tickets and pending firmware updates from the system with one click.
* **Browse tickets** — view and manually delete system tickets for games.
* **Run MTP responder** — enables DBI's internal MTP server to connect the Switch to a PC or to an Android device (Some tested phone/tablet devices: Pixel 3, Xiaomi Mi A1, Lenovo Tab 4 7 "TB-7304X). On your device you will be presented with several virtual drives for installation and many advanced features for file management on your SD card and NAND. Please see https://github.com/rashevskyv/dbi/blob/main/README_ENG.md#run-mtp-responder for a full overview.
* **Exit** — exit from the program. *Main menu hotkey for this option*: **+** button

The bottom left corner of DBI displays the total amount of data on your currently on your SD card along with the full capacity. The bottom right corner gives you the same information for your NAND's usable space in HOS.

Bottom center (dbi: XXX) is the dbi version number - you should always use the most recent version.

### Browse SD Card / Browse USB0 Drive

Select this option if you want to install games, updates and DLC from files that exist on your SD card or external USB drive.
Press **A** to open the folder and **B** to go back. After opening the folder containing your installation files the **X** button can select single or multiple files individually. The **Y** button inverts your selections and the color of the name of the selected files will change from white to light blue.

Prsss the **A** button to confirm. A window with installation options will appear:

![2021041011441100](https://user-images.githubusercontent.com/18294541/114264183-18138580-99f2-11eb-8c7b-536b4b831195.jpg)

**Total transfer size** — the total amount of data (.NSP / .NSZ / .XCI files) selected for installation.
**Total install size** — the amount of free space required to install the selected files.
**Install target** — data installation location: **NAND** - internal memory of the Nintendo Switch console, **SD** - SD card, **AUTO** - by default this will install to your SD card but if you don't have enough space the installation will fall back to NAND (internal memory).
**Delete after install** — deletes installation files (.NSP / .NSZ / .XCI files) from the source after they have been successfully installed; for this to work, the "Read-only" attribute must be removed from files if present. By default, files are not deleted. The option is visible only when installing from an SD card / external USB drive.
**Turn off screen** — turns off the screen during installation to conserve battery, after installation successfully completes the screen will automatically turn back on. This option only works in handheld mode.
Select **Start install** to begin the installation. After a successful installation *Installation Complete. Press B to return* will appear.

*DBI will automatically and immediately remove old updates when installing a new update for a game, so you don't have to worry about the extra space they occupy.*

### Install title from USB

If you cannot use DBI's MTP responder this is another convenient method for installing titles over USB. Installing over USB allows you to transfer files directly from your PC for example, which avoids the inconvenience and of having to first move the file to your SD card and then install it. Compared to using the MTP responder this mode will also allow direct installation of .XCI files.

*Main menu hotkey for this option*: **Y** button.

In order to use this option you will first require dbibackend (`dbibackend.exe` for Windows,` dbibackend` from `dbibackend.tar.xz` for all). Launch dbibackend, select the files to install, select Start server, connect a USB-C cable from your PC to your Switch and select Install title from USB in dbi.

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

Example for ngnix on Windows:
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

For the server address in dbi.config, you can also use a domain name, for example, your remote VPS - suggested to use with HTTP Basic authentication e.g.: `http://user:password@host:port/Nintendo/Switch/`

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

In **Browse installed applications** you can see a list of installed programs, updates and DLC with their occupied space, version (display version and hex version), their titleID, the total game time and the number of launches, the presence of installed LayeredFS mods for the game (for Atmosphére). *Main menu hotkey for this option*: **L** button:

![2021041012101400](https://user-images.githubusercontent.com/18294541/114264832-e3093200-99f5-11eb-9e7a-acc7b0f7444c.jpg)

The total number of installed applications (e.g. games and homebrew nsps) is displayed at the top of the screen. Any installed data can be transferred between internal NAND and SD card, it is possible to individually select and uninstall multiple games **(b)** / updates **(u)** / DLC **(d)** together with their associated LayeredFS mods **(l)** (detected at `/atmosphere/contents/`) or you can individually select updates and DLC for deletion. The **Reset Required version** function will force restore the system update check for the selected game back to base (this is also done automatically with installation or removal of game updates):

![2021041012102700](https://user-images.githubusercontent.com/18294541/114264843-f74d2f00-99f5-11eb-8cf0-a3fc383ac322.jpg)

By pressing the **R** button you can sort the game list as you prefer - alphabetically (default) or by last usage.
Press the **A** button to enter the menu of the selected game, the **-** button deletes the game and its (non-personalized) ticket, the D-pad selects games, the left stick scrolls through the list of games and the **ZR** and **ZL** buttons flip through the list of games screen by screen.

You can also check (verify) games for their integrity by selecting the file to check and then selecting ** Check integriy **

### Cleanup orphaned files
**Cleanup orphaned files** automatically cleans unnecessary game files, files from interrupted game installations, downloaded (officially) OFW firmware updates and all unused game tickets if found.

### Browse tickets
View and delete game tickets. **Ticket (or encrypted title key)** is special encrypted unique information about the rights to launch the content of the game which is installed in the system during the installation of each game (000 at the end of titleID) / update (800 at the end of titleID) / each DLC. + means the presence of an installed game, **[c]** - common-ticket (installed game dump or update), **[p]** - personalized-ticket (game purchased from the eShop)

You may be able to resolve certain errors with this for example if you know exactly what you are doing. You can remove individual tickets from a specific game and/or its update/DLC.

In most case it's better not to touch anything here in order to avoid errors in starting games.

### Run MTP responder 
**Run MTP responder** run the built-in DBI MTP server to connect to your PC or Android device via USB-C OTG (phone / tablet / other devices). *Main menu hotkey for this option*: **X**  button (same button to exit MTP mode). After successfully connecting the USB cable to the PC and starting the MTP server in DBI, you'll see the following on your computer:

![изображение](https://user-images.githubusercontent.com/18294541/114265006-054f7f80-99f7-11eb-86c9-1a20d588e616.png)

1: **External SD Card**, for viewing, copying and deleting files and folders from/to a PC and from/to your SD card. Drop a file larger than 4GB onto the SD card and DBI will automatically split the file into an archived folder, which allows the Switch to see it as a single file, with this you can for example very easily add a >4GB .xci for use in SX OS, or add a >4GB movie for watching in pPlay.

2: **NAND User**, viewing, copying files and folders on a PC from the Switch's internal memory to its USER system partition (this partition is read-only).

3: **NAND System**, viewing, copying files and folders on a PC from the internal memory of the Switch to its SYSTEM system partition (the partition is read-only).

4: **Installed games**, to view installed games.

В **Installed games** all installed games are displayed from both in NAND (internal memory of the Switch) and SD card. To dump installed games to your PC in .NSP format, just copy the folder with the name of the game from Installed games to your PC. A common ticket with completely cleared personal information is generated based on your personalized ticket. Your dump will be in separated files - the game itself, the update and DLC. If cheats or mods have been installed for the game, they will be located in the `Mods & Cheats` folder. You  can also dump a single combined multicontent file containing the game itself, the update and all DLC. This file is located right at the root of the **Installed games** section.
The generated dbi `InstalledApplications.csv` is also stored here, with a table of the list of installed games, their TitleID and the current version.

5: **MicroSD install**
Drop or copy your **NSP** or **NSZ** files in this folder. When the transfer is complete the game will be installed on the **SD card** of your console. When installing NSZ files, keep in mind that their actual size may differ greatly from their original size after installation: so if for example you start with 2GB free on your memory card and you do not have enough space to install an NSZ of 1GB in size, that is because NSZ files are compressed and must be decompressed for installation.

6: **NAND install**: Drop or copy your **NSP** or **NSZ** files in this folder. When the transfer is complete the game will be installed on the **internal memory** of your console. When installing NSZ files, keep in mind that their actual size may differ greatly from their original size after installation: so if for example you start with 2GB free on your memory card and you do not have enough space to install an NSZ of 1GB in size, that is because NSZ files are compressed and must be decompressed for installation.

7: **Saves**: Access to all game saves - in accounts (Account), system programs (System), in Background Content Asymmetric synchronized delivery and Transmission (BCAT, for example: events in ACNH), temporary (Temporary), cache (Cache, for example: addons in DOOM), system BCAT (SystemBCAT), - stored in the internal memory of the Switch; in the Installed games folder - save for the currently installed games, Uninstalled games - save from deleted games that were previously launched. From here, you can make a backup of them by copying them to a PC, and also delete unnecessary ones - for this, open the folder with the name of the game you need, then delete the folder with the nickname of your account / Device-save.
In order to restore the save, copy them to the appropriate folder from your PC. DBI does not require pre-launching the game to restore a save, however this only applies to regular saves. BCAT or Cache saves require a pre-launch of the game before restoring.

8: **Album**: access to screenshots and videos (Album), similar to Nintendo's feature added OFW 11.0.0.

9: **Gamecard**: with a gamecard inserted into the Switch you can dump to .XCI or trimmed .XCI on the PC, along with the update built into it if it exists. The personal RSA certificate automatically removed and is dumped separately.

After activating the MTP server on the Switch a window will appear with your account nickname and its UID, as well as the number of game saves: ![2021041013152900](https://user-images.githubusercontent.com/18294541/114266673-27013480-9a00-11eb-81ba-f1ff1c3c5abb.jpg)

To turn off the MTP server and exit to the main menu, press the **X** button.

### Exit
Exit - exit from the program in HOS, either to hbmenu or bypassing hbmenu directly to the homescreen (this is configured in dbi.config). If dbi was launched from a title / forwarder, the program will restart or remain on a black screen.

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
* **«INVALID LENGTH»** — check the USB-C cable connection to your USB port, try with another USB-C cable, check the integrity of the game file and the SD card for errors, when installing via MTP - try to run dbi in application mode (title override) holding the R button while launching a title.
* **«[FAILED] Unknown error»** when installing .tik (ticket) - add the latest sigpatches for Atmosphére.
* **«605: Content or placeholder path not exists»** or **«SOME CONTENTS ARE MISSING»** — broken file system on your SD card, or a non-working / low-quality flash drive. Check it in chkdsk and h2testw, if there are no errors reformat to FAT32.
* **WARNING! Extra buffers exceeded**, when installing via MTP - try to run dbi in application mode (title override) holding the R button while launching a title or alternatively via NSP forwarder and use a faster microSD card with a different USB cable / port.
* **No tickets found but they are required** — incorrect (incomplete, no ticket but with titlerights) dump of the game, use another one.
* **SOME CONTENTS ARE MISSING. APPLICATION WILL BE UNUSABLE** — container is incomplete, check the integrity of the game installation file.
    
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

;Enable or disable various MTP storages
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
Home server=ApacheHTTP|http://192.168.1.47/Nintendo/Switch/
```

* **DefaultASCII** - **true** includes a standard font, **false** includes an alternative font
* **UseLibUsbHsFS** - **true** enables [libusbhsfs](https://github.com/DarkMatterCore/libusbhsfs) library for working with external USB drives via USB-OTG on Switch, **false** disables it.
* **ExitToHomeScreen** — if **false**, the exit from dbi occurs in the hbmenu, if **true**, to the Switch's home menu
* **CheckHash** — if **true**, hashes of .nca files are checked when installing games on the Switch, if **false**, no.
* **LogAllFiles** — **false** disables logging of all files when working with MTP; if **true**, all files are logged, even those that are less than 4MB.
* **ShowCombinedNSPInInstalledGames** — **false** disables display of combined (multi-title .NSP-file) titles.
* **ShowMACInInstalledGames** — **false** turns off the display of the virtual directory **"Mods & cheats"** in the Installed games item in the MTP, redirecting along the path `/atmosphere/contents/%titleid_game%` to the memory card.
* In the **[[MTP Storages]](#run-mtp-responder)** section, enable (**true**) and disable (**false**) the display of the corresponding elements of the MTP Responder on PC / Android, by default all items will be displayed.
* In the **[[Network sources]](#home-server)** section, names and addresses for installing games over a network (via a WiFi / LAN adapter) are set.
