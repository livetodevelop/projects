#!/bin/bash

# minecraft server backup script
# runs via cron every 6 hours

BACKUP_DIR="/mnt/external-drive/mc-backups"
SERVER_DIR="/home/mcserver/server"
WORLD_DIR="$SERVER_DIR/world"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)

echo "starting backup at $TIMESTAMP"

# tell server to save
screen -S mc -X stuff "save-all\n"

sleep 5

# create backup
tar -czf "$BACKUP_DIR/world_$TIMESTAMP.tar.gz" -C "$SERVER_DIR" world

# delete backups older than 7 days
find "$BACKUP_DIR" -name "world_*.tar.gz" -mtime +7 -delete

echo "backup finished, $(ls -lh $BACKUP_DIR | wc -l) backups stored"
