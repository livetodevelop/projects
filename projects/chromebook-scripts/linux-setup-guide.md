# Linux (Crostini) Setup Guide

⚠️ this workaround was patched recently but might still work on older chromebooks

## the problem

school admins block "Enable Linux (Beta)" in settings. grayed out.

## the workaround (might not work anymore)

### step 1: change DNS

1. click network icon in bottom right
2. click on your wifi network
3. under "Name servers", select "Custom name servers"
4. add: `8.8.8.8` and `8.8.4.4` (Google DNS)
5. click away to save

### step 2: force enable crostini

1. open a new tab
2. go to: `chrome://flags/#enable-experimental-crostini-ui`
3. enable it
4. restart chromebook

### step 3: try enabling linux

1. go to Settings > Developers > Linux development environment
2. click "Turn On"
3. if it works, follow the setup wizard

### step 4: restore DNS

change DNS back to automatic so teachers don't get suspicious

## what you can do with linux

- install VS Code: `sudo apt install code` (or download .deb)
- run python without web-based IDEs
- use git properly
- run local web servers

## if it doesn't work

the admin policy might be too strict. alternatives:

- use Replit or GitHub Codespaces (browser-based)
- ask teacher for permission
- wait until you're on a personal computer

## warning

if linux suddenly stops working, the school might have pushed a new policy. don't try to fight it, you'll just get in trouble.
