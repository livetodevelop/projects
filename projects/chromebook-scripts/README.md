# Chromebook Scripts (School Workarounds)

⚠️ **use at your own risk** ⚠️

scripts and tricks for getting around school chromebook restrictions. worked on my school's lenovo 100e chromebooks (2023).

## what's here

### `enable-dev-mode.sh`
instructions for enabling developer mode. **warning**: this wipes your local files and shows a scary screen on boot. teachers might notice.

### `crosh-commands.txt`
list of crosh commands that still work even when admin console is locked down. mostly useless but `ping` and `tracepath` can help test if sites are blocked or just down.

### `linux-setup-guide.md`
how to enable Linux (Crostini) even when it's "disabled by administrator". the workaround involves changing DNS settings temporarily.

### `extension-unblocker.py`
python script that generates a list of extension IDs that aren't blocked yet. you'd need to run this on a personal computer first, then sideload the extensions.

## disclaimers

- i'm not responsible if you get in trouble
- some of these might not work on your school's setup
- don't be stupid, like actually installing malware
- the linux workaround got patched last month but there might be others

## why i made these

mostly bored during study hall. also needed to run VS Code for a project and school wouldn't let me install anything.

## better alternatives

honestly? just ask your teacher for permission to install stuff for class projects. most teachers don't care as long as you're actually working.
