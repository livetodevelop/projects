#!/bin/bash

# setup script for rpi5 home server
# run as root or it'll complain a lot

echo "updating packages..."
apt update && apt upgrade -y

echo "installing basics..."
apt install -y git curl wget htop vim samba ufw

echo "setting up pi-hole..."
curl -sSL https://install.pi-hole.net | bash

echo "installing java for minecraft..."
apt install -y openjdk-17-jre-headless

echo "creating minecraft user..."
useradd -m -s /bin/bash mcserver
mkdir -p /home/mcserver/server
chown mcserver:mcserver /home/mcserver/server

echo "setting up samba share..."
cat >> /etc/samba/smb.conf << EOF
[backups]
   path = /srv/backups
   browseable = yes
   read only = no
   guest ok = no
   create mask = 0755
EOF

mkdir -p /srv/backups
chmod 755 /srv/backups

echo "enabling firewall..."
ufw allow 22
ufw allow 80
ufw allow 53
ufw allow 25565
ufw --force enable

echo "done! reboot now and then run mc-setup.sh"
echo "also change the default password pls"
