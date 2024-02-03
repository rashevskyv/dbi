# DBI 
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
  1. [Install title from DBIbackend](#install-title-from-dbibackend)
  1. [Home server](#home-server)
  1. [Browse installed applications](#browse-installed-applications)
     * [Titles Context menu](#title-context-menu)
     * [Detailed game menu](#detailed-game-menu)
      * [Content records](#content-records)
      * [Tickets](#tickets)
      * [Saves](#saves)
     * [Records Context menu](#records-context-menu)
  1. [Browse tickets](#browse-tickets)
     * [Tickets context menu](#tickets-context-menu)
  1. [Tools](#tools)
  1. [Browse saves](#browse-saves)
      * [Context menu Installed and Uninstalled](#context-menu-installed-and-uninstalled)
      * [Backups context menu](#backups-context-menu)
  1. [Run MTP responder](#run-mtp-responder)
  1. [Activity Log](#activity-log)
    * [Applications](#applications)
    * [Activity](#activity)
  1. [Configuration and dbi.config parameters](#configuration-and-dbiconfig-parameters)
     * [General (`[General]`)](#general-general)
     * [Main menu (`[MainMenu]`)](#main-menu-mainmenu)
     * [Applications (`[Applications]`)](#applications-applications)
     * [Install options (`[Install]`)](#install-options-install)
     * [MTP options (`[MTP]`)](#mtp-options-mtp)
     * [MTP storages (`[MTP Storages]`)](#mtp-storages-mtp-storages)
     * [FTP options (`[FTP]`)](#ftp-options-ftp)
     * [Access point (`[Access point]`)](#access-point-access-point)
     * [Exists in Config, but not in menu](#exists-in-config-but-not-in-menu)
      * [Network sources](#network-sources)
      * [Local sources](#local-sources)
      * [MTP custom storages](#mtp-custom-storages)
      * [Title name override](#title-name-override)
  1. [Exit](#exit)
1. [Warnings and Errors](#warnings-and-errors)
	1. [Warnings](#warnings)
	1. [Errors](#errors)
   1. [Color codes](#color-codes)
1. [dbi.config](#dbiconfig)
1. [Other options](#other-options)
      * [Mounting the content of installed titles via MTP](#монтирование-содержимого-установленных-игр-по-mtp)
      * [Backup and Restore Saves via MTP](#бекап-и-восстановление-сохранений-по-mtp)
      * [Using DBI to Install Mods](#использование-dbi-для-установки-модификаций)
      * [USB 3.0](#usb-30)
      * [Restoring clean user saves from backup](#восстановление-бекапа-чистых-пользовательских-сохранений)
      * [Set picture as avatar](#set-picture-as-avatar)
      * [Editing and Viewing Files](#editing-and-viewing-files)
1. [Acknowledgements](#acknowledgements)

## Installation 

Copy `dbi.nro` and `dbi.config` to your SD card at `sdmc:/switch/DBI/` DBI can be then be launched in either applet mode (from Album) or application mode (title override), however it is primarily designed to be used in applet mode. 

*If you have successfully launched DBI in applet mode you will see a blue background, launching in application mode will display a black background.*

## Usage 

### Interface
![2021041010520200](https://user-images.githubusercontent.com/18294541/114262830-d7643e00-99ea-11eb-8dbb-c8e0996577e5.jpg)
* **Browse SD Card** —  installation of `NSP`/`NSZ`/`XCI`/`XCZ` files from the memory card.
* **Browse USB0 Drive** — installation of `NSP`/`NSZ`/`XCI`/`XCZ` files from an external exFAT/FAT32 USB drive, such as a flash drive, hard drive, etc.
* **Install title from DBIbackend** installation of NSP/NSZ/XCI/XCZ files from a PC via USB 2.0 or 3.0 cable using the included program dbibackend. *Hotkey* for this option: **(Y)** button.
* **Install title from Gamecard** — this option appears when a game card is inserted into the Switch and allows for the installation of a game from the game card to the console's SD card or internal NAND memory.
* **Home server** — starting with version v150, it is possible to install games over the network (HTTP) via WiFi without wires or a LAN-USB adapter. More details about this below.
* **Browse installed applications** — view installed games, the total number of games installed, view time spent on a game and the number of times it has been launched, check for errors, transfer game data between internal memory, memory card, and back, selectively or continuously delete games and accompanying LayeredFS mods, view the presence of updates and DLC, manually remove DLC/updates/LayeredFS (LFS) mod, and the Reset Required version function to reset the system update check for a selected game. *Hotkey* for this option: **(L)** button.
* **Cleanup orphaned files** — automatic cleaning of unnecessary deleted game files, if any.
* **Browse tickets** — view and manually delete game system tickets.
* **Browse saves** - view and delete game saves.
* **Run MTP responder** — enables the internal MTP server to connect the Switch to a PC or Android device (phone/tablet/etc., tested with Pixel 3, Xiaomi Mi A1, Lenovo Tab 4 7" TB-7304X), where you can view and work with the memory card (1: SD Card) and internal console memory, view installed games (4: Installed games), backup game saves to a PC (7: Saves), and dump a game card (full/trimmed/certificate) to a PC/Android with an inserted game card (9: Gamecard). *Hotkey* for this option: **(X)** button
* **Run FTP server** - enables the DBI FTP server for accessing SD files through port 5000 or installing files through port 6000.
* **Exit** — exits the program. *Hotkey* for this option: **(+)** button.

The bottom left corner of DBI displays the total amount of data currently on your SD card along with the full capacity. The bottom right corner gives you the same information for your NAND's usable space in HOS.

Bottom center (dbi: XXX) is the DBI version number - you should always use the most recent version.

### Buttons

* **(А)** - select or confirm
* **(B)** - cancel, exits the program **from the main menu**
* **(X)** - select file. On the main screen - hotkey for mounting MTP (menu item "[Run MTP responder](#run-mtp-responder)")
* **(Y)** - invert selection, select all if nothing is selected. On the main screen - installation via USB using dbibackend (menu item "[Install title from DBIbackend](#install-title-from-dbibackend)")
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

### Install title from DBIbackend

If you cannot use DBI's MTP responder this is another convenient method for installing titles over USB. Installing over USB allows you to transfer files directly from your PC for example, which avoids the inconvenience and of having to first move the file to your SD card and then install it.

*Main menu hotkey for this option*: **(Y)** button

In order to use this option you will first require dbibackend (`dbibackend.exe` for Windows, or the `dbibackend` script for all operating systems). Launch dbibackend, select the files to install, select Start server, connect a USB-C cable from your PC to your Switch and select **Install title from DBIbackend** in DBI.

For proper operation of dbibackend on Windows, you need to install the "**libusbK (v3.1.0.0)**" drivers. They can be installed through the [Zadig program](https://zadig.akeo.ie/) by entering DBI into the "**Install title from DBIbackend**" mode and selecting the device that appears in the program.

From here you can select and install your files on the Switch in the same fashion as using Browse SD Card/Browse USB0 Drive.

To quickly send files or folders with games for installation, right-click on them, select `Send from dbibackend` and the installation files will be immediately placed in dbibackend's queue. To configure this in Windows, press `Win + R`, enter `shell: sendto` and create a shortcut for `dbibackend.exe` in the folder.

There are alternative clients for working with DBIbackend, for example [headless implementation](https://github.com/cyb3rwarden/dbibackend/blob/0885ef67edf28cbca30fb2c193ad7ab9a62786f7/dbibackend/dbibackend.py), [NSW-DBI 2.0.0 on nodegui](https://4pda.to/forum/index.php?showtopic=939714&st=6080#entry100701109) (requires installation of libusb driver for Linux or WinUSB (libusb) for Windows via Zadig).

You can pass commands to the script by running it from the command line and then specifying the path to the game or games you need to install. For example:

```
python ~/dbi/dbibackend ~/Switch/File1.nsp ~/Switch/File2.nsp ~/Switch/File3.nsp
```

```
dbibackend.exe "e:\Switch\Games\File1.nsp" "e:\Switch\Games\File2.nsp" "e:\Switch\Games\File3.nsp"
```

#### Dependencies that may be required to run on MacOS or Linux

```bash
brew install python-tk
pip3 install pyusb
```

#### Install instructions for Ubuntu 22.04.3

This will install DBI dependencies and create a udev rule to allow a non-root user to access a Switch connected via USB.

```pip3 install pyusb
sudo apt install python-tk
echo 'SUBSYSTEM=="usb", ATTRS{idVendor}=="057e", ATTRS{idProduct}=="3000", MODE="0666"' | sudo tee /etc/udev/rules.d/nintendo-switch.rules
sudo udevadm control --reload-rules
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

* **N/S/M/G** - NAND/SD/Mixed/Gamecart - Location of installed files, Mixed denotes that installed files were detected on both NAND and SD card
* **b** - BASE - the base game
* **u** - Update - update installed
* **d** - DLC - DLC installed
* **l** - LayeredFS mod - LayeredFS mods or cheats for the game were detected at `sdmc:/atmosphere/contents/%titleID%/`

You can quick launch a game directly from the list by highlighting it and pressing **(L3)**.

**Please note!** If the game is **highlighted in red** only an update and/or DLC is installed, the game itself is NOT installed.

#### Title context menu

![2021062719354100](https://user-images.githubusercontent.com/18294541/123554557-3b480880-d789-11eb-9235-d547f2c588bd.jpg)

Displayed by clicking on **(+)** on the selected title(s).

* **Delete title** - delete selected titles
* **Move title to SD/NAND** - move the selected titles to SD card or NAND, depending on where the title is currently located. If content is installed to both locations then both options will be displayed
* **Reset required version** - resets the system version check required to run the title (debug must be enabled in Atmosphere)
* **Check integrity** - checks the data integrity of the selected titles
* **Expose contents via MTP** - mount the content of the selected titles via MTP 
* **Dump to SD** - dump all available content (game, DLC, update) to a SD card using the path specified in the config (default is `switch/DBI/dumps`)
* **Content info** - display additional information about the content (SDK version, required key generation, ID, patch information, and more)

If you press the **(A)** button on the title, the **detailed game menu** will open.

### Detailed game menu

The **detailed game menu** opens when you press the **(A)** button on a title while in the menu for browsing installed games (**Browse installed applications**)

![2021062719353600](https://user-images.githubusercontent.com/18294541/123554561-400cbc80-d789-11eb-8d81-e3403f33b365.jpg)

The game's icon, TitleID, name, author, version, supported languages, and the presence of an LFS mod are displayed in the detailed game menu, which can be accessed by pressing the **(A)** button on the game's tile while in the browse installed applications menu.

Additionally, the menu displays the total playtime, total launches, total occupied space, space in NAND and on SD, total saves size, and the game's forced language.

Below that, there are three tabs that can be switched between using the **(L)** and **(R)** buttons:

* **Content records**
* **Tickets**
* **Saves**

#### Content records

The information is displayed in the following format:

[Location] Type | version [version number] | Size

**Location** - **NAND** or **SD**, depending on where the content is installed
**Type** - **Application** for the base game, **Update** for updates, **Addon** for DLC, and the number of the DLC will be indicated next to it
**version [version number]** - the content version in dec and [hex] (for example, 786432 is 0.12.0.0)
**Size** - occupied space

By pressing the **(A)** button on the content, you can view its contents. The content can be copied by selecting the corresponding item in the context menu (which opens by pressing the **(+)** button). The content opens in "read-only" mode.

When you press the (+) button on the selected content, you can access the context menu, which includes:

* **Delete record** - delete the selected record
* **Move records to SD/NAND** - move the selected record to NAND or the memory card, depending on where it is currently located. If parts of the title are located in both places, both options will be displayed.
* **Reset required version** - reset the required system version check for launching the title (debug must be enabled in Atmosphere). This will not help if the game was built on a new SDK version.
* **Force language** - allows you to forcibly launch the game with a selected language. By default, the game runs with the same language selected in the system, if it is not available in the game, depending on the console region. The selected language will be displayed next to the game icon in the **Forced Language** field.
* **Check integrity** - checks the integrity of the selected title data.
* **Expose contents via MTP** - mounts the content of the selected titles via MTP.
* **Dump to SD** - dumps all available content (game, DLC, update) to the SD card according to the path specified in the config (default: switch/DBI/dumps).
* **Content info** - displays additional information about the content, including the SDK version, required key generation, ID, patch information, and much more.

#### Tickets

A **ticket (or encrypted title key)** is a unique encrypted information about the rights to launch game content that is installed in the system during the installation of each game (ending in **000** in the titleID)/update (ending in **800** in the titleID)/DLC.

Installed tickets for content are displayed, including:

* **Personalized ticket** - a ticket given when installing a game from the eShop, which is personalized and unique for each account.
* **Common ticket** - a general ticket that exists for updates and is also used as a workaround in pirated games.

The game databases on Nintendo servers are encrypted with the same key, but this key is encrypted with its own unique key for each game purchaser (generated on the console). Therefore, the key for decrypting the game can only be obtained from the personalized ticket on the console for which it was created. Thus, while personalized tickets differ for each purchaser, they all contain the same decryption key. Common tickets do not have encryption, only a signature.

By clicking the **(+)** button on the selected content, you can access a context menu where you can delete selected tickets. 

In some cases, if a specific error occurs and you are sure of what you are doing, you can delete it for a specific game and its updates/DLC. However, it is generally better to leave the tickets alone to avoid errors when launching games.

#### Saves

Viewing and deleting saves. If there is no save, it can be created through the context menu (button (+)) for the selected account. If there is a save:

* **Backup** - make a backup of the save. By default, it will be located in the `switch/DBI/saves` folder.
* **Restore** - restore the backup of the save.
* **Save info...** - detailed information about the save, such as type, size, account name, etc.
* **Increase save size** - increases the space allocated for the save by a specified value.
* **Delete** - delete the save.

### Browse tickets
View and delete game tickets. **Ticket (or encrypted title key)** is a special encrypted unique information about the rights to launch the content of the game, which is installed in the system during the installation of each game (**000** at the end of the titleID) / update (**800** at the end of titleID) / of each DLC.

* **+** means there is an installed game
* **[c]** (**Personalized ticket**) - a ticket that is given when installing a game from the eShop, it is personalized, meaning it is encrypted with a unique key from your console.
* **[p]** (**Common ticket**) - a common type of ticket that is used for updates and also used as a workaround for pirated games.

Game databases on Nintendo servers are encrypted with the same key, but this key is encrypted with a unique key for each purchased game (this key is generated on the console itself), so it is only possible to obtain the decryption key for a game from a Personalized ticket on the console it was created for.
This means that all Personalized tickets purchased are different, but they contain the same decryption key for the game.
Common tickets, on the other hand, do not have encryption, only a signature.

Sometimes if a specific error occurs and you know exactly what you are doing, it can be removed from a specific game and its update/DLC.

In most cases it is better not to touch anything here, in order to avoid errors when starting games.

#### Tickets context menu

Displayed by clicking on **(+)** on selected tickets

The number of selected tickets is displayed at the top of the context window.

* **Delete tickets** - delete selected tickets

* **Select same game** - highlight all tickets related to the selected game

### Tools

* **Cleanup orphaned files** - cleaning up lost files. Automatically cleans up unnecessary game files, files from interrupted/failed game installations, officially downloaded firmware updates and all unused game tickets if found.
* **Delete parental controls** - completely removes parental controls. No reboot required.
* **Delete user...** - completely removes the selected user from the system (the removed user's saves remain in the system).
* **Run random game** - launches a random game from those installed.
* **NTP time sync** - Synchronizes the console's time with a remote time synchronization server. Internet connection and correctly set timezone in the console settings are required for operation.
* **Check for title updates** - checks for updates and new DLC for installed games. The database for checking is set in the settings.

### Browse saves

View, backup and delete saves.

In general, saves are displayed in the following format:

`[Account] Game-Name Backup-date Size`

* **Account** - shows the name of the account for which the save was created, if the save type is Account, if the save type is other, it shows its type
* **Game-Name** - shows the name of the game for which the save was created
* **Backup-date** - shows the date when the backup was created, only displayed in the Backup tab
* **Size** - the size of the save or backup

Below, there are three tabs that can be switched using the **(L)** and **(R)** buttons:

* **Installed** - shows saves for all installed games
* **Uninstalled** - shows saves for all uninstalled games
* **Backups** - shows created backups

#### Context menu Installed and Uninstalled

Displayed when **(+)** is pressed on selected saves

* **Backup** - creates backups of the selected saves
* **Open** - opens the save
* **Save info...** - shows information about the save (Id, type, size, creation time, etc.)
* **Delete** - deletes the selected saves
* **Select same app** - selects all saves related to the selected game
* **Browse app(s)** - goes to the [content record card](#content-records) of the selected games. You can switch between cards using the **(ZL)**/**(ZR)** buttons. Only available in the **Installed** tab.

#### Backups context menu

Displayed by clicking on **(+)** on selected saves

* **Validate saves** - check the integrity of saves
* **Restore** - restore selected backup saves
* **Open** - open the selected save
* **Delete** - deletes the selected saves
* **Browse app(s)** - goes to the [content record card](#content-records) of the selected games. You can switch between cards using the **(ZL)**/**(ZR)** buttons. Only available in the **Installed** tab.
* **Select same user** - select all saves belonging to a specific user.

If multiple backups are selected for one game and user in the list, only the most recent backup will be restored.

### Run MTP responder 

**Run MTP responder** activates the built-in MTP server in DBI for exchanging data with a PC or an Android device via USB-C OTG (phone/tablet/other devices). *Hotkey to call this option from the main menu*: the **(X)** button (also used to exit MTP). After connecting the USB cable to the PC and starting the MTP server in DBI, the following window will appear on the PC:

![image](https://user-images.githubusercontent.com/18294541/114265006-054f7f80-99f7-11eb-86c9-1a20d588e616.png)

1: **SD Card** - for viewing, copying and deleting files and folders from/to a PC and from/to your SD card. Drop a file larger than 4GB onto the SD card and DBI will automatically split the file into an archived folder which allows the Switch to see it as a single file, with this you can for example very easily add a >4GB .XCI for use in SX OS or add a >4GB movie for watching in NXMP or pPlay.

2: **NAND User** - view and copy files and folders to a PC from the Switch's internal memory USER partition (this partition is read-only).

3: **NAND System** - view and copy files and folders to a PC from the Switch's internal memory SYSTEM partition (the partition is read-only).

4: **Installed games** - all installed games are displayed from both NAND (internal memory of the Switch) and SD card. To dump installed games to your PC in NSP format, just copy the folder with the name of the game from Installed games to your PC. A common ticket with completely cleared personal information is generated based on your personalized ticket. Your dump will be in separate files - the game itself, the update and any DLC files. If cheats or mods have been installed for the game, they will be located in the `Mods & Cheats` folder. You can also dump a single combined multicontent file containing the game itself, the update and all DLC, these files are located at the root of the **Installed games** directory.

5: **SD install** - Drop or copy your **NSP**/**NSZ**/**XCI** or **XCZ** files in this folder. When the transfer is complete the game will be installed on the **SD card** of your console. When installing NSZ or XCZ files, keep in mind that their actual size may differ greatly from their original size after installation: so if for example you start with 2GB free on your SD card and you do not have enough space to install an NSZ of 1GB in size, that is because NSZ and XCZ files are compressed and must be decompressed for installation.

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

### Activity Log

Displays activity graphs in games by dates for all existing users for each specific game.

Upon launch, two tabs are shown, which can be switched between using the (L) and (R) buttons:

Hotkeys:
* (L)/(R) - switch to the neighboring tab
* (ZL)/(ZR) - change the date
* (Y) - change the display period: all time, day, month, year
* (X) - sorting: by game title, by number of launches, by time spent in the game
* (+) - select a user for display

#### Applications

A list of games for which there is launch statistics is shown. At the top of the window is a status line of the following type:

`[player] period. Total: number of hours (sorting method)`. For example, the line `[All players] 2023 January. Total: 72 hours (by play time)` means that the screen displays statistics **for all players for January 2023, sorted by game time, where 72 hours have been played**

The window is divided into three columns. From left to right:
  * Game title
  * Number of launches
  * Amount of time spent in the game

When you press (A) on a game, you enter the **Activity** for the current game, where statistics for the selected game are shown. When you press (A) on an item, you will go deeper (year -> month -> day -> hour)

#### Activity

Activity is shown as a diagram for all games at once. To go to the diagram for a specific game, go to the **Applications** tab and select a game to display.

### Configuration and dbi.config parameters

The program configuration manager allows easy configuration of the program without editing `dbi.config`.

Below are the configuration items through GUI / The corresponding items in `dbi.config` will be indicated in parentheses.

**true** in the configuration corresponds to **Yes** in the settings, **false** - **No**

#### General (`[General]`)

* **Use external USB drives** (`UseLibUsbHsFS`) - true enables the [libusbhsfs](https://github.com/DarkMatterCore/libusbhsfs) library for working with external USB drives through USB-OTG on the Switch, false disables it.
* **Direct exit to homescreen** (`ExitToHomeScreen`) - if **false**, exiting DBI will go to hbmenu, if **true**, to the Switch home screen.
* **Log events & operations** (`LogEvents`) - whether or not to save logs for "*Install*", "*Check integrity*", and "*Cleanup*" events.
* **Highlight update files** (`HighlightUpdates`) - whether or not to highlight updates for installed games in the file manager.
* **Rotate screen upside down** (`RotateScreen`) - rotates the screen by 180 degrees.
* **Rotate joycon upside down** (`RotateJoycon`) - flips the controls to match the flipped screen.
* **Use under/over clock** (`OptimizeClockSpeed`) - disables optimization of the SoC frequency during idle time. Disabled by default because it **may cause lag on the startup screen when exiting DBI incorrectly**! The correct exit method is through the **Exit** menu item.
* **Browse saves in RO mode** (`ROSaveFS`) - view saves in read-only mode.
* **Show 'Update From Here'** (`ShowUpdateFromHere`) - show the "Update all titles" button in the context menu for automatically updating installed games from all available sources (SD/USB/HTTP/FTP).
* **Save backup folder** (`SavesFolder`) - folder for storing save backups.
* **Logs folder** (`LogsFolder`) - folder for storing logs.
* **Title dumps folder** (`DumpsFolder`) - folder on the memory card to which games will be dumped.
* **Version info URL** (`VersionsURL`) - can accept a direct link to a file on a remote server or a file on the memory card. Examples:` https://raw.githubusercontent.com/blawar/titledb/master/versions.txt` or `sdmc:/versions.txt`.
* **Show cache warming indicator** (`ShowCacheWarmingIndicator`) - show a notification when caching information about installed programs.
* **Put cursor down after selection** (`MoveDownAfterX`) - whether or not to move the cursor down after marking a game with the **(X)** button.
* **Screen idle time in seconds** (`ScreenIdleTimeout`) - screen shutdown timeout.
* **Autorepeat buttons when holding** / **Автоповтор кнопки при удержании** (`Autorepeat`) - navigate through the menu by holding the button
* **Cursor on both panels** / **Курсор на обеих панелях** (`Secondcursor`) - whether to display the cursor on the inactive panel or not

**Exists in the config, but not in the menu:**

* **AppSorting** - options for sorting the list of applications
* **SaveSorting** - options for sorting saves

#### Main menu (`[MainMenu]`)

Settings for the menu items that will be displayed in the main DBI menu. **Yes** in the settings corresponds to **true** in the config, **No** corresponds to **false**.

* **Browse SD Card** (`BrowseSD`) - menu item "[Browse SD Card and Browse USB0 Drive](#browse-sd-card--browse-usb0-drive)", for installing games from an SD card
* **Browse System** (`BrowseSystem`) - allows browsing and copying files from the SYSTEM partition
* **Browse User** (`BrowseUser`) - allows browsing and copying files from the USER partition
* **Browse USB** (`USBHost`) - menu item "**Browse USB0 Drive**", for installing games from an external USB drive
* **Install from USB** (`BackendInstall`) - menu item "[Install title from DBIbackend](#install-title-from-dbibackend)", for installing titles from the DBI backend
* **Install from Gamecard** (`GameCard`) - menu item "**Install title from Gamecard**", for installing content from game cartridges to the console memory
* **Browse Network** (`Network`) - menu item "**Home server**", for installing games from a home web server
* **Browse SD shortcuts** (`Local`) - whether to show links to folders in the [Local sources](#local-sources) section or not
* **Browse applications** (`BrowseApps`) - menu item "[Browse installed applications](#browse-installed-applications)", for managing installed applications
* **Cleanup orphaned files** (`Cleanup`) - menu item "[Cleanup orphaned files](#cleanup-orphaned-files)", for cleaning up orphaned files from the memory card
* **Check title updates** (`UpdateCheck`) - menu item "**Check for title updates**", for checking for updates and DLC for installed games
* **Browse tickets** (`Tickets`) - menu item "[Browse tickets](#browse-tickets)", for managing tickets
* **Browse saves** (`Saves`) - [Browse saves](#browse-saves)
* **Run MTP responder** (`MTP`) - menu item "[Run MTP responder](#run-mtp-responder)", for starting MTP
* **Run FTP server** (`FTP`) - menu item "**Run FTP server**", for starting FTP

#### Applications / Installed games (`[Applications]`)

* **Show LFS folder size (slow)** (`CalculateLFSSize`) - Enables or disables the calculation of the size of installed LFS mods. If enabled, it may affect the speed of opening the "*Browse installed applications*" menu.

##### Install options (`[Install]`)

* **Check hash during install** (`CheckHash`) - When set to **true**, the hash of `.nca` files is checked during game installation on the Switch. When set to **false**, it is not checked.
* **Chunked HTTP/FTP transfer** (`ChunkedTransfer`) - Enables or disables chunked transfer of data over HTTP.

#### MTP options (`[MTP]`)

* **Show combined NSP** (`ShowCombinedNSPInInstalledGames`) - When set to **false**, multi-title .NSP files are not shown in the Installed games menu in MTP mode.
* **Show 'Mods & Cheats' folder** (`ShowMACInInstalledGames`) - When set to false, the virtual directory **Mods & cheats** in the Installed games menu in MTP mode is not shown, which redirects to `sdmc:/atmosphere/contents/TITLEID/` on the memory card.
* **Use TitleID for 'Mods & Cheats'** (`MACasTID`) - Displays the "Mods & Cheats" folder in MTP mode as a TitleID.
* **Turn off screen** (`TurnOffScreen`) - Enables or disables turning off the console screen when connected in MTP mode.
* **Android extensions** (`ReportAndroidExtension`) - whether to use the corresponding command set when working with MTP. Sometimes PC clients based on libmtp (Mac or Linux) do not correctly recognize the device, which may result in a decrease in data transfer speed. In such cases, it is recommended to try changing this setting.

**In the config but not in the menu:**

* **LogAllFiles** - When set to **false**, files smaller than 4 MB are not logged when working with MTP. When set to **true**, all files are logged.

#### MTP Storages (`[MTP Storages]`)

Displays the corresponding items when using [MTP Responder](#run-mtp-responder) with a PC/Android. By default, all items are enabled for display.

**true** - display in the main menu, **false** - do not display.

The names of the items correspond to the section names.

* **SD Card** (`1: SD Card`)
* **Nand USER** (`2: Nand USER`)
* **Nand SYSTEM** (`3: Nand SYSTEM`)
* **Installed games** (`4: Installed games`)
* **SD install** (`5: SD install`)
* **NAND install** (`6: NAND install`)
* **Saves** (`7: Saves`)
* **Album** (`8: Album`)
* **Gamecard** (`9: Gamecard`)
* **Show custom storages** (`CustomStorages`) - show or hide custom menu items specified in the MTP custom storages section.

#### FTP Options (`[FTP]`)

* **Turn off screen** (`TurnOffScreen`) - turn off the screen when entering FTP mode.
* **Start local Access point** (`UseAP`) - enable Switch to work as an access point that FTP clients can connect to directly. Below are settings for this access point.
* **Read file date** / **Читать дату файлов** (`ReadMT`) - whether to read the file modification date or not

#### Access Point (`[Access point]`)

* **SSID** (`SSID`) - the name of the access point.
* **Password** (`Password`) - the password.
* **Use 5 GHz** (`Use5GHz`) - whether to use 5 GHz. If turned off, it will work in 2.4 GHz mode.
* **Use hidden SSID** (`Hidden`) - hide the SSID for search. This means that it can only be connected to by entering the specified SSID.

#### Exists in Config, but not in menu

##### [Network sources](#network-sources)
Names and addresses for setting up network installs (via WiFi/LAN adapter)

**NSP Indexer** - address for indexing NSP ([details](https://github.com/rashevskyv/dbi/issues/44))

##### **Local sources**

Create menu items with quick access to selected folders on the memory card configured in the config (like "shortcuts"), for example:

`Homebrew Shortcut=sdmc:/switch` will create a "**Homebrew Shortcut**" menu item that opens the `sdmc:/switch` folder.

##### **MTP custom storages**

Custom items for MTP mode for quick access to folders on your memory card. Format: `<displayed_folder_name>=<path>`, for example: `Homebrew=sdmc:/switch`.
In MTP mode, a `Homebrew` folder will appear that links to the `switch` folder on your memory card.

##### **Title name override**

Allows you to change the displayed title name. For example, if you specify `10023901191C000=Naheulbeuk`, then in the application, instead of `The Dungeon of Naheulbeuk: The Amulet of Chaos`, it will display simply `Naheulbeuk`.

### Exit

**Exit** - exits the program to HOS, bypassing hbmenu, or to hbmenu (configurable in dbi.config); if dbi was launched from a title/forwarder, the program will reboot or remain on a black screen.

## Warnings and errors
### Warnings

Displayed in orange. These are NOT errors!

* **[SIGNATURE: Invalid]**, **[SIGNATURE: XCI->NSP]**, **[HASH NOT MATCHED TO META]**, **[HASH FIXED IN META]** — these are NOT errors, but notifications of signature mismatch in headers, for example, when using conversion or editing, custom NSP, forwarder.
* **HASH MISMATCH** — most often, this is NOT an error, the game was converted from a cartridge (then everything is fine), sometimes there are problems with file integrity, re-download/re-hash it, data transfer via USB cable/port/during installation between PC and Switch.
If the game does not launch or launches with an error, try to reinstall it again, check or replace the USB cable/SD/change USB port.
* **[DELTA SKIPPED]** — this is NOT an error, but a notification that unnecessary fragments in the update file were skipped if they were in it, as it should have been.
* **No tickets found** — this is NOT an error, it does not affect the game's functionality, but informs that the game is without tickets. It may be a dump from a .XCI cartridge or converted to Standard Crypto.
* **Application uses AddonContent titleId**, **Application uses Update titleId** — this is NOT an error, usually indicating a homebrew game in .NSP, created not to standard, for example, when AddonContent flag (DLC) was added to the Application title (main game, v0).
If such a game launches and works, then everything is fine.
* **This application base is not stand alone. Make sure you installed update** - when installing new Sparse Storage games — this is NOT an error, do not forget, in addition to the game's base file, to also install an update to it before launching.

### ERRORs

* **USB communication failed** - check/replace USB cable and USB port on PC.
* **Cannot parse content meta**:
  * **Old firmware** - your firmware is too outdated to analyze the metafile. Update CFW and system software to the latest versions
  * **Unexpected error** - the file is corrupted. Check and re-download the file.
* **Invalid PFS0 magic!** - redownload the game installer file and check its integrity, as this file is corrupted.
* **[INVALID NCA MAGIC]** - update to the latest version of OFW and CFW, and if the error persists, double-check the integrity of the game installer file.
* **Installation aborted** - data transmission error, double-check and if necessary, replace the USB cable/USB port between the Switch and PC. Also, make sure that you have installed the latest version of the software, as in this post.
* **Nothing to install** - in the file selection window, rename the file without special characters, hieroglyphs, or Cyrillic in the name and path to it.
* **Transfer error**, **[TRANSFER CRC ERROR]**, **[TRANSFER ABORTED]** - check the USB-C cable connection and USB port, check with other USB-C cables, check the integrity of the game file and memory card for errors. When installing via MTP, launch dbi through any game (title) while holding down the (R) button, rather than in applet mode through albums.
* **Error occurred: Invalid argument** - update your dbi to the latest version.
* **SOME CONTENTS ARE MISSING. APPLICATION WILL BE UNUSABLE** - a corrupt file system on the memory card or a non-working/poor quality flash drive. Check it with chkdsk and h2testw; if there are no errors, reformat to FAT32.
* **[NOT ENOUGH SPACE]**, **[CAN NOT CREATE PLACEHOLDER]** - there is not enough space on the memory card/NAND, free up more space or check the memory card. Check it with chkdsk and h2testw; if there are no errors, reformat to FAT32.
* **Extra buffers exceeded. Media write speed is too low** - when installing via MTP, launch dbi through any game (title) while holding down the **(R)** button. Alternatively, use an NSP-forwarder and a faster SD card with a different USB cable/port.
* **No tickets found but they are required** - an incorrect (incomplete, without a ticket but with titlerights) game dump, find another.
* **Invalid personalized ticket** - This error occurs at the end of game installation when installing a .tik ticket, indicating that an incorrect game dump was used where a personalized ticket from the console on which the game was purchased was left instead of a common ticket. Please download another correct dump.
* **No ES sigpatches!** - This error message means that the ES sigpatches are either outdated, incorrect, or not installed on the console. Please install the latest version of the ES sigpatches.

### Color codes:

* In all menus
  * <span style="color:#ffffff; background-color: black;">WHITE on BLACK BG</span> - focused
  * <span style="color:#008578; background-color: #000084;">BLUE</span> - selected (with **(X)** button)
* In "**Browse SD Card**"
  * <span style="color:#c7c6d6; background-color: #000084;">WHITE</span> - folder 
  * <span style="color:#80878f; background-color: #000084;">LIGHT GREY</span> - file
  * <span style="color:#414e54; background-color: #000084;">DARK GREY</span> - installed game
  * <span style="color:#3bce28; background-color: #000084;">GREEN</span> - update or DLC for installed game
* In "**Browse installed applications**"
  * <span style="color:#cebfde; background-color: #000084;">WHITE</span> - installed game
  * <span style="color:#8e0000; background-color: #000084;">RED</span> - installed update or DLC without game
* **In logs** on installation: 
  * <span style="color:#00ff02; background-color: #000084;">GREEN</span> - no errors
  * <span style="color:#fa7f08; background-color: #000084;">ORANGE</span> - no errors, but warnings (for example, installed NSP is XCI convert, or hash was fixed on meta)
  * <span style="color:#f80100; background-color: #000084;">RED</span> - [errors](#errors). File was not installed
* **In logs** after installation: 
  * <span style="color:#00ff02; background-color: #000084;">GREEN</span> - ended with no errors
  * <span style="color:#f6ff05; background-color: #000084;">YELLOW</span> - ended with no errors but with warnings
  * <span style="color:#f80100; background-color: #000084;">RED</span> - ended with errors

## dbi.config
The `dbi.config` file is responsible for storing program settings. It is located next to `DBI.nro`

Let's take a look at its contents:
```
; General settings
[General]
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
; Auto repeat nav. buttons when holding
Autorepeat=true
; Show cursors on both panels in two-panel browsinig mode
Secondcursor=false
; Backup saves before delete
FoolproofSaveDelete=true

; Visibility of main menu items
[MainMenu]
; Browse and install files from SD card
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
; Report android extension (some initiators thinks that android has bugs)
ReportAndroidExtension=true

; FTP options
[FTP]
; Turn screen off on start FTP mode
TurnOffScreen=false
; Start local access point for FTP server
UseAP=false
; Read file modification time (can slow down on large dirs)
ReadMT=false

; Access point options
[Access point]
SSID=
Password=
Use5GHz=true
Hidden=false

;Enable or disable various MTP storages
[MTP Storages]
1: SD Card=true
2: Nand USER=false
3: Nand SYSTEM=false
4: Installed games=true
5: SD Card install=true
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

The description of each item separately can be found in the [DBI settings](#configuration-and-dbiconfig-parameters) section.

## Other options

### Mounting the content of installed titles via MTP

Go to "**Browse installed applications**" -> Choose apps you need to mount with **(X)** -> Press **(+)** -> "**Expose contents via MTP**"

### Backup and Restore Saves via MTP

1. Connect your console in MTP mode via DBI.
1. Navigate to the **Saves** folder on your PC.
1. You can either copy your saves to your PC or restore them by simply dragging them into this folder.

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

### Restoring clean user saves from backup

These are decrypted saves that are located in the `USER:/saves` folder. In case the emunand is damaged, these saves can be retrieved through a PC or Tegra Explorer and restored through DBI.

You can place these saves in the backup saves folder of DBI (`/switch/dbi/saves` by default) and restore them through the standard save restoration menu (the user's name will be enclosed in curly brackets `{}` in this case), or through the context menu invoked on the file of such a save.

### Set picture as avatar

Hover over the desired picture and bring up the context menu with the (+) button. Select "**Set as avatar...**". The selected image will be set as your avatar. The image will be automatically resized to square proportions and scaled down to the necessary size. If you want the image to maintain its original aspect ratio, prepare it in advance.

### Editing and Viewing Files 

Any file can be opened as a text or as HEX. Non-empty files are opened in viewing mode, however, the (L3) key will switch to editing mode. Let's consider both modes separately. 

You can also create an empty text file from the context menu (called by the (+) button > **Create a new file...**). When opening an empty text file, the editor will start automatically.

#### File Viewing Mode 

**Hotkeys:** 
* **DPAD / Left Stick / Right Stick** - text scrolling 
* **(L) / (R) / (ZL) / (ZR)** - next / previous page (screen)
* **(R3)** - switch between text or HEX viewing modes
* **(L3)** - switch to editing mode
* **(+)** - context menu

**Context Menu:**
* **Editing** - switch to editing mode
* **Encoding** - change text encoding. Note that when changing the encoding in viewing mode, when the file is closed and reopened, the encoding will not change
* **Line Wrapping** - whether or not to wrap text to a new line when it reaches the edge of the screen

#### File Editing Mode 

You can edit text by moving around the keyboard with the right stick and selecting a letter with the (A) button.

**Hotkeys:** 
* **Right Stick** - move around the keyboard
* **DPAD / Left Stick** - move around the text
* **(A)** - select the highlighted character on the keyboard
* **(X)** - delete character (Backspace)
* **(B)** - file saving menu
* **(Y)** - space
* **(L)+(LEFT)** - Go to the beginning of the line (HOME)
* **(L)+(RIGHT)** - Go to the end of the line (END)
* **(R)+(LEFT)** - Go to the next word
* **(R)+(RIGHT)** - Go to the previous word
* **(ZL)** - change case 
* **(ZR)** - move to the next line (Enter)
* **(R3)** - switch language 
* **(L3)** - switch to viewing mode 

When closing a file or switching to viewing mode, you can choose whether or not to save changes if changes were made to the file.

## Acknowledgements
Thanks to [SciresM](https://github.com/SciresM) for [hactool](https://github.com/SciresM/hactool) (licensed under [ISC](https://en.wikipedia.org/wiki/ISC_license)) - DBI uses some data struct definitions from there
