# 3DS Theme & Homebrew Tools

stuff for my New 3DS XL. running Luma3DS v13 and custom themes.

## installed

- **Luma3DS** - latest version, autoboots to home menu
- **FBI** - install .cia files, region free games
- **Checkpoint** - backup saves (used this to move Pokemon saves)
- **Anemone3DS** - theme manager
- **Rosalia Menu** - access homebrew without rebooting

## themes made

made a couple minimal themes with Anemone:

- **MonoBlue** - dark gray background, blue accents, simple icons
- **CleanWhite** - light gray, black text, very basic

both are in the `themes/` folder as .zip files. install with Anemone3DS.

## luma config

- Autoboot: Enabled (to Home Menu)
- Show NAND: Disabled
- Disable ARM11 exception handlers: Enabled (for homebrew compat)
- Enable game patching: Enabled (for region free)

## warnings

- don't update firmware if you're on 11.17, that's the last one
- make a NAND backup with GodMode9 BEFORE doing anything
- SD card needs to be under 128GB or format might fail

## files

- `themes/` - custom theme files
- `luma_config.bin` - my Luma settings
- `boot.firm` - don't touch this unless you know what you're doing
