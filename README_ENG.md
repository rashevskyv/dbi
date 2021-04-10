# DBI by **[duckbill](https://github.com/duckbill007)**
![Github latest downloads](https://img.shields.io/github/downloads/rashevskyv/dbi/total.svg)

Guide based on [Brikachu's work](https://4pda.ru/forum/index.php?showtopic=939714&st=1100#entry86288632). Translated from Russian using google translate. Edits are welcome

[РУССКИЙ](README.md)

Ultimate solution for NSP\NSZ\XCI installation. Supports installing via MTP, USB (with DBI backend script or dbi-nsw tool), http (from your own server), installing from external USB and more.

## Содержание: 

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
	1. [Уведомления](#warnings)
	1. [Errors](#errors)
1. [dbi.config](#dbiconfig)

## Installation 

Put `dbi.nro` and `dbi.config` into `/switch/DBI/`. Run it from РИД on applet mode (from Albums)

## Usage 

### Interface
![2021041010520200](https://user-images.githubusercontent.com/18294541/114262830-d7643e00-99ea-11eb-8dbb-c8e0996577e5.jpg)
* **Browse SD Card** — installation of .NSP / .NSZ / .XCI files from the memory card.
* **Browse USB0 Drive** — installation of .NSP / .NSZ / .XCI files from an external USB drive to exFAT / FAT32: flash drive, hard drive, etc.
* **Install title from USB** — installation of .NSP / .NSZ / .XCI from a PC via USB 2.0 and 3.0-wire, through the supplied program dbibackend. *Hotkey for this option*: **Y** button.
* **Install title from Gamecard** — this item appears when a game cartridge is inserted into the Switch - to install a game from an existing game cartridge into a microSD card or the console's internal NAND memory.
* **Home server** — starting from version v150, it is possible to install games over the network (HTTP), via WiFi without a wire or a LAN-USB adapter. More on this below.
* **Browse installed applications** — viewing installed games, their total installed number, see the time spent on the game and the number of its launches, check (verify) for errors, transfer game data between the built-in memory, memory card and vice versa, the possibility of their selective or streaming deletion along with the attached LayeredFS-mods , viewing if they have updates and DLCs, manual removal of DLC / updates / LaryeredFS (LFS) mod, the Reset Required version function to reset the system update check for the selected game. *Hotkey for this option*: **L** button.
* **Cleanup orphaned files** — automatic cleaning of unnecessary deleted game files, if any
* **Browse tickets** — viewing and manual deletion of system tickets for games.
* **Run MTP responder** — enabling the internal MTP server to connect the Switch to a PC or to an Android device (phone / tablet / etc., Pixel 3 tested, Xiaomi Mi A1, Lenovo Tab 4 7 "TB-7304X), you can: view and work with a memory card ( 1: External SD Card) and the internal memory of the console, view installed games (4: Installed games), make a backup of game saves on a PC (7: Saves), with a game cartridge inserted, dump it (full / trimmed / certificate) on PC / Android (9: Gamecard) *Hotkey for this option*: **X** button (same to quit MTP).
* **Exit** — exit from the program. *Hotkey for this option*: **+** button


In the lower left corner (SD) it is written about the occupied data size on the card / total card size. In the lower right corner (NAND) is the occupied data size in the Switch on-board memory / Switch on-board shared memory.
At the bottom center (dbi: XXX) is the dbi version number - try to always use the most recent version of the program

### Browse SD Card / Browse USB0 Drive

Select this item if you want to install games / updates / DLC from existing files on a memory card / external USB.
The **A** button opens the folder, the **B** button returns back, after opening the folder with the files for installation, the **X** button can select only the necessary files, the **Y** buttons to invert the selection. In this case, the color of the name of the selected files will change from white to light blue

Then press the **A** button to confirm. A window with installation options will appear:

![2021041011441100](https://user-images.githubusercontent.com/18294541/114264183-18138580-99f2-11eb-8c7b-536b4b831195.jpg)

**Total transfer size** — the amount of installation distributions (.NSP / .NSZ / .XCI files) selected and ready for installation.
**Total install size** — the amount of free space that is required to install the selected files.
**Install target** — data installation location: **NAND** - internal memory of the Nintendo Switch console, **SD** - microSD memory card, **AUTO** - default option to always install on a microSD memory card, but if there is not enough on it places, the data will be installed in the internal memory.
**Delete after install** — this is the option to remove installation distributions (.NSP / .NSZ / .XCI files) from the card after they have been successfully installed; For it to work, the "Read-only" attribute must be removed from the files. By default, files are not deleted. The option is visible only when installing from a memory card / external USB
**Turn off screen** — the ability to turn off the screen during installation to save battery power, immediately after a successful installation, the screen will automatically turn on. This option only works in handheld mode.
Click **Start install** to start the installation. After successful installation, *Installation Complete. Press B to return* will appear at the bottom..

The program has a built-in automatic function for removing old updates when installing a new update for the game, so you don't have to worry about the extra space they occupy.

### Install title from USB

Through Install title from USB, it is very convenient to install games, updates and DLCs to them directly directly via a USB cable from a PC to the Switch, bypassing the need to remove the card and spend double time downloading distributions (.NSP / .NSZ / .XCI files) to memory card and installing them from there. *Hotkey for calling this option from the main menu*: **Y** button.
To work, first you need to download dbibackend on your PC (`dbibackend.exe` for Windows,` dbibackend` from `dbibackend.tar.xz` for all), start it, select the games to install, click Start server, then connect the USB-C cable to PC and Switch, select Install title from USB in dbi and install all the necessary games.

The selection of files, as well as their installation, is carried out in the same way as from the item Browse SD Card / Browse USB0 Drive

To quickly send files or folders with games for installation, right-click on them, select Send> dbibackend, the installation files are immediately placed in the dbibackend queue. To configure this in Windows, press `Win + R`, enter` shell: sendto`, put a shortcut for `dbibackend.exe` in the folder

### Home server

The **"Home server"** item appears if there is a configured section **Network install sources** in `dbi.config` (more about this file below). Moreover, the name of this item will change depending on the name specified in the configuration file

To install games over the network, edit the dbi.config file located in the `/ switch / DBI /` folder, according to the example

```
; Network install sources
[Network sources]
; <display name>=<type>|<URL>
Home server=ApacheHTTP|http://192.168.1.47/Nintendo/Switch/
```

Install any other HTTP server with DirectoryListing enabled on your PC: Apache, Mongoose, Python SimpleHTTP, sheret, rclone, etc.,

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

Save the config, run `nginx.exe`, allowing the program to access the network, then copy the desired game to the local / nginx / html / Nintendo / Switch / folder on your PC, and on the Switch select the line “Home server”.
We get the usual interface for installing files, and you can start installing all the games over the network, after which, if desired, the web server can be stopped via nginx -s stop.

As a server address, you can also use a domain name on the Internet, for example, your remote VPS - better with HTTP Basic authentication like http: // user: password @ host: port / Nintendo / Switch /

For example:
```
ApacheHTTP|Network repo|http://127.0.0.1/Nintendo/Switch/
ApacheHTTP|WWW VPS repo|http://www.myveryownswitchvpsdomain.su/Nintendo/Switch/
```

Generate the htpasswd file, put it in `/nginx/conf/`, then change in `nginx.conf` in the block (example):

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

In **Browse installed applications** you can see a list of installed programs, updates, DLCs to them, separately their occupied volume and version, ordinal and in HEX format, their titleID, see the total game time and the number of launches, the presence of installed LayeredFS- mod for the game (for Atmosphére). *Hotkey for calling this option from the main menu*: **L** button:

![2021041012101400](https://user-images.githubusercontent.com/18294541/114264832-e3093200-99f5-11eb-9e7a-acc7b0f7444c.jpg)

The total number of games installed is written in the top center; any installed game data can be transferred between the built-in memory, microSD memory card and vice versa, it is possible to selectively (or stream) uninstall games **(b)** / updates **(u)** / DLC **(d)** together with the attached LayeredFS-mods **(l)** to the game in `/ atmosphere/contents/` or just it separately; here you can manually delete unnecessary DLCs / updates to the game; there is a **Reset Required version** function to reset system check for updates of the selected game (it is also automatically activated upon installation, removal of game updates):

![2021041012102700](https://user-images.githubusercontent.com/18294541/114264843-f74d2f00-99f5-11eb-8cf0-a3fc383ac322.jpg)

By pressing the **R** button, you can select the desired sorting of games - alphabetically (by default), or by their last use.
Press the **A** button to enter the menu of the selected game, the **-** button deletes the game and its (non-personalized) ticket, the D-pad selects games, the left stick scrolls the list of games, the **ZR** and **ZL** buttons you can flip through the list of games screen by screen.

You can also check (verify) games for their integrity by selecting it and then ** Check integriy **

### Cleanup orphaned files
**Cleanup orphaned files** automatically cleans unnecessary game files, files from interrupted game installations, downloaded (officially) OFW firmware update and all unused game tickets if found.

### Browse tickets
View and delete unnecessary game tickets. **Ticket (or encrypted title key)** is a special encrypted unique information about the rights to launch the content of the game, which is installed in the system during the installation of each game (000 at the end of titleID) / update (800 at the end of titleID) / each DLC. + means the presence of an installed game, **[c]** - common-ticket (installed game dump or update), **[p]** - personalized-ticket (game purchased from the eShop)

Sometimes, if there are specials. errors (for example), and you know exactly and are sure what you are doing, it can be removed from a specific game and its update / DLC.
In all other cases, it is better not to touch anything here, in order to avoid errors in starting games.

### Run MTP responder 
**Run MTP responder** run a built-in dbi MTP server for exchanging data from a PC or to an Android device via USB-C OTG (phone / tablet / other devices). *Hot key for calling this option from the main menu*: button **X** (it is the same to exit MTP). After connecting the USB cable to the PC and starting the MTP server in dbi, the following window will appear on the PC:

![изображение](https://user-images.githubusercontent.com/18294541/114265006-054f7f80-99f7-11eb-86c9-1a20d588e616.png)

Где:
1: **External SD Card**, for viewing, copying and deleting files and folders from / to a PC and from / to a microSD memory card

2: **NAND User**, viewing, copying files and folders on a PC from the Switch's internal memory, to its USER system partition (the section is read-only).

3: **NAND System**,viewing, copying files and folders on a PC from the internal memory of the Switch, to its SYSTEM system partition (the section is read-only).

4: **Installed games**, to view installed games.

В **Installed games** all games are displayed both in NAND, the internal memory of the Switch, and installed on the memory card, all together. To make a dump (distribution) of an installed game on your PC in .NSP format, just copy the folder with the name of the game from Installed games to your PC, and a common common ticket with completely cleared personal information is generated based on your personalized ticket. You will receive a dump of this game in the form of separate files - the game itself, the update and DLC separately. If cheats or mods have been installed for the game, they will be located in the `Mods & Cheats` folder. You can also get a combined dump in which the game itself, all its DLC and update will be glued into one file. This file is located right at the root of the **Installed games** section.
The generated dbi `InstalledApplications.csv` is also stored here, with a table of the list of installed games, their TitleID and the current version.

5: **MicroSD install**
Copy your **NSP** or **NSZ** to this folder. At the end of copying, the game will be installed on the **memory card** of your console. When installing NSZ files, keep in mind that their actual size may differ greatly from the size after installation, so if, with 2GB free on your memory card, you, for example, do not have enough space to install an NSZ of, say, 1GB in size, do not be surprised. because the NSZ container is compressed.

6: **NAND install**: Copy your **NSP** or **NSZ** to this folder. After copying is complete, the game will be installed in the **internal memory** of your console. When installing NSZ files, keep in mind that their actual size may differ greatly from the size after installation, so if, with 2GB free on your memory card, you, for example, do not have enough space to install an NSZ of, say, 1GB in size, do not be surprised. because the NSZ container is compressed.

7: **Saves**: Access to all game saves - in accounts (Account), system programs (System), in Background Content Asymmetric synchronized delivery and Transmission (BCAT, for example: events in ACNH), temporary (Temporary), cache (Cache, for example: addons in DOOM), system BCAT (SystemBCAT), - stored in the internal memory of the Switch; in the Installed games folder - save for the currently installed games, Uninstalled games - save from deleted games that were previously launched. From here, you can make a backup of them by copying them to a PC, and also delete unnecessary ones - for this, open the folder with the name of the game you need, then delete the folder with the nickname of your account / Device-save.
In order to restore the save, copy them to the appropriate folder from your PC. DBI does not require pre-launching the game to restore a save, however this only applies to regular save. BCAT or Cache saves require a pre-launch of the game before restoring.

8: **Album**: access to screenshots and videos (Album), just like Nintendo's OFW 11.0.0.

9: **Gamecard**: when the game cartridge is inserted into the Switch, it becomes possible to copy its dump to .XCI or trimmed .XCI on the PC, along with the update built into it, if any, with its personal RSA certificate already removed; in addition, it is possible to separately export its certificate

Also, on the Switch display after turning on the MTP server, a window will appear with your account nickname and its UID, as well as the number of game saves: ![2021041013152900](https://user-images.githubusercontent.com/18294541/114266673-27013480-9a00-11eb-81ba-f1ff1c3c5abb.jpg)

To turn off the MTP server and exit to the main menu, press the **X** button.

### Exit
Exit - exit from the program in HOS, bypassing hbmenu, or in hbmenu (this is configured in dbi.config); if dbi was launched from a title / forwarder, the program will restart or remain on a black screen.

## Errors and warnings

### Warnings

* **«HASH MISMATCH»** — most often, this is NOT an ERROR, the game was converted from a cartridge (then everything is in order), sometimes - there are problems with the integrity of the file, download it, rehash it, transferring data via a USB cable / port / during the installation process between the PC and the Switch.
    If the game does not start or starts with an error, try reinstalling it again, check or replace the USB cable / microSD / change the USB port.
* **DELTA SKIPPED** — this is NOT an ERROR, but a notification that unnecessary fragments in the update file were skipped, if they were in it, as they should.
* **«No tickets found. Possibly this NSP was converted from XCI.»** — this is NOT an ERROR, the performance of the game will not be affected, but informing that the game is without tickets. It can be dumped from an .XCI cartridge or converted to Standard Crypto.
* **«WARNING» title marked as Application but has AddonConten** — this is NOT an ERROR, usually it indicates a non-standard .NSP homebrew game, for example, when an AddonContent flag (DLC) was added to the Application title (main game, v0).
    If such a game starts and works, then everything is in order.

### ERRORs

* **«Can not find file for ncaid»** — The installation file of the game is damaged (it does not contain the required .nca from the .cnmt list).
* **«Invalid PFS0 magic!»** — download the installation file of the game and check its integrity, this file is damaged.
* **«Received less data than expected»** or **Installation aborted** — data transfer error, recheck and if necessary replace the USB cable / USB port between the Switch and the PC. Also, make sure you have the most recent version of the program installed, like in this post.
* **«std::bad_alloc»** — rename the file without special characters and Cyrillic in the name and path to it, plus make sure that you are using the latest version of the program, as in the post, the latest version of OFW and CFW is installed on the console.
* **«Nothing to install»** in the file selection window - rename the file without special characters, hieroglyphs or Cyrillic in the name and path to it.
* **«INVALID LENGTH»** — check the connection of the USB-C cable and the USB port, check with other USB-C cables, the integrity of the game file and the memory card for errors, when installing via MTP - run dbi through any game (title) while holding the R button, and not in applet mode through albums.
* **«Error occurred: Invalid argument»** — update your dbi to the latest version.
* **«[FAILED] Unknown error»** when installing .tik (ticket) - install the latest sigpatch for Atmosphére.
* **«605: Content or placeholder path not exists»** or **«SOME CONTENTS ARE MISSING»** — broken file system of a memory card, or a non-working / low-quality flash drive. Check it in chkdsk and h2testw, if there are no errors, reformat to FAT32.
* **WARNING! Extra buffers exceeded**, when installing via MTP - run dbi via title = via any game, holding down the R button while starting it; alternatively via NSP forwarder, and use a faster microSD card with a different USB cable / port.
* **No tickets found but they are required** — incorrect (incomplete, no ticket but with titlerights) dump of the game, find another one.
* **SOME CONTENTS ARE MISSING. APPLICATION WILL BE UNUSABLE** — container is incomplete, check the integrity of the game installation file.
    
## dbi.config
The dbi.config file was added starting with version 253. It is located next to DBI.nro, and replaces the old flags files dbi.default.ascii and dbi.network.config, and also adds several new options for easy customization of settings for the user ...

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
* **LogAllFiles** — **false** disables logging of all files when working with MTP; if **true**, all files are logged, even those that are less than 4 MB.
* **ShowCombinedNSPInInstalledGames** — **false** disables display of combined (multi-title .NSP-file) titles.
* **ShowMACInInstalledGames** — **false** turns off the display of the virtual directory **"Mods & cheats"** in the Installed games item in the MTP, redirecting along the path `/atmosphere/contents/%titleid_game%` to the memory card.
* In the **[[MTP Storages]](#run-mtp-responder)** section, enable (**true**) and disable (**false**) the display of the corresponding elements when the MTP Responder is working with a PC / Android, by default all items are enabled for display.
* In the **[[Network sources]](#home-server)** section, names and addresses for installing games over a network (via a WiFi / LAN adapter) are set, more details.
