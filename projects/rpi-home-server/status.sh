#!/bin/bash

# quick status check for the server

echo "=== RPi5 Server Status ==="
echo ""

echo "CPU Temp: $(vcgencmd measure_temp | cut -d= -f2)"
echo "CPU Load: $(cat /proc/loadavg | cut -d' ' -f1-3)"
echo ""

echo "RAM Usage:"
free -h | grep Mem
echo ""

echo "Disk Usage:"
df -h / /mnt/external-drive 2>/dev/null | tail -n +2
echo ""

echo "Minecraft Server:"
if screen -list | grep -q mc; then
    echo "  RUNNING (screen session: mc)"
    MEM=$(ps aux | grep java | grep -v grep | awk '{print $6}' | head -1)
    echo "  Java memory: $((MEM / 1024))MB"
else
    echo "  OFFLINE"
fi
echo ""

echo "Pi-hole Status:"
if systemctl is-active --quiet pihole-FTL; then
    echo "  Running"
    echo "  Ads blocked today: $(pihole status json 2>/dev/null | grep -o '"ads_blocked_today":[0-9]*' | cut -d: -f2 || echo 'unknown')"
else
    echo "  Not running (try: pihole restartdns)"
fi
