# RPi5 Home Server

running a bunch of stuff on my Raspberry Pi 5 (16GB model). mostly for learning and hosting games for friends.

## what's running

- **Minecraft server** - Fabric 1.20.4, about 8 players max before lag
- **Pi-hole** - blocks ads for my whole house, parents think I'm a genius
- **file server** - Samba share for backups and stuff
- **discord bot host** - runs 24/7 so my bots don't go offline

## setup notes

- using official Pi 5 case with active cooler (REQUIRED, this thing gets HOT)
- booting from NVMe SSD via HAT, way faster than SD card
- allocated 8GB RAM to Minecraft, rest for system
- static IP: 192.168.1.50

## scripts

### `setup.sh`
installs all the dependencies. needs to be run as root lol

### `mc-backup.sh`
backs up the world every 6 hours to an external drive. cron job is set up

### `status.sh`
shows CPU temp, RAM usage, and if Minecraft is running

## problems

- Pi 5 uses USB-C power, make sure you have the official 27W supply or it throttles
- NVMe HAT gets warm too, added a small fan
- WiFi is okay but ethernet is way more stable for the MC server
- sometimes Pi-hole breaks after updates, just `pihole restartdns`

## todo

- [ ] set up Grafana dashboard to monitor everything
- [ ] maybe add Home Assistant?
- [ ] learn Docker properly instead of running everything natively
