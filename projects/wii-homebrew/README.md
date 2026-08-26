# Wii Homebrew Stuff

collection of homebrew apps and configs for my Wii (v4.3U). installed via LetterBomb.

## what's installed

- **Priiloader** - region free, skip disc update, block updates
- **USB Loader GX** - plays games from USB hard drive
- **Nintendont** - GameCube games on Wii
- **Homebrew Channel** - duh
- **SysCheck HDE** - made a backup of my sysmenu before touching anything

## priiloader hacks enabled

- region free gaming (PAL games work on NTSC Wii)
- skip disc update prompts
- block online updates
- remove health screen (saves 2 seconds)
- enable launch menu with home button

## usb loader gx config

games stored on 1TB USB drive, FAT32 format with WBFS folder. took forever to convert all my ISOs but worth it.

theme is the minimal black one, didn't want flashy colors everywhere.

## nintendont settings

- memory card emulation: ON (saves work!)
- video mode: auto
- widescreen: depends on the game

## warnings

- don't update your wii if you're on 4.3, brick risk
- make a nand backup BEFORE installing anything
- use an sd card under 32GB or it might not work (FAT32 issues)

## files included

- `priiloader_hacks.ini` - my hack settings
- `syscheck.txt` - backup of my system info before modding
- `usbloader_config.txt` - USB Loader GX settings
