import subprocess
import json
import os
import shutil
from datetime import datetime

# load config
with open("config.json", "r") as f:
    config = json.load(f)

SERVER_PATH = config["server_path"]
JAR_FILE = config["jar_file"]
RAM_MB = config["ram_mb"]
BACKUP_FOLDER = config["backup_folder"]

def get_server_process():
    """check if server is running"""
    try:
        result = subprocess.run(
            ["pgrep", "-f", JAR_FILE],
            capture_output=True,
            text=True
        )
        return result.stdout.strip()
    except:
        return None

def start_server():
    """start the minecraft server"""
    if get_server_process():
        print("server already running!")
        return
    
    os.chdir(SERVER_PATH)
    cmd = f"java -Xmx{RAM_MB}M -Xms{RAM_MB}M -jar {JAR_FILE} nogui"
    
    # start in background
    subprocess.Popen(cmd, shell=True)
    print("server starting...")

def stop_server():
    """graceful shutdown"""
    pid = get_server_process()
    if not pid:
        print("server not running")
        return
    
    # send stop command via rcon would be better but this works
    os.kill(int(pid), 15)  # SIGTERM
    print("stopping server...")

def restart_server():
    """restart the server"""
    stop_server()
    import time
    time.sleep(5)  # wait for shutdown
    start_server()

def get_status():
    """show server status"""
    pid = get_server_process()
    
    if not pid:
        print("server: offline")
        return
    
    print(f"server: online (pid: {pid})")
    
    # try to get player count from server.properties
    try:
        with open(os.path.join(SERVER_PATH, "server.properties"), "r") as f:
            for line in f:
                if line.startswith("max-players"):
                    max_players = line.split("=")[1].strip()
                    print(f"max players: {max_players}")
                    break
    except:
        pass

def backup_world():
    """create world backup"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"world_backup_{timestamp}"
    backup_path = os.path.join(BACKUP_FOLDER, backup_name)
    
    os.makedirs(BACKUP_FOLDER, exist_ok=True)
    
    world_folder = os.path.join(SERVER_PATH, "world")
    
    if not os.path.exists(world_folder):
        print("world folder not found!")
        return
    
    try:
        shutil.copytree(world_folder, backup_path)
        print(f"backup created: {backup_name}")
    except Exception as e:
        print(f"backup failed: {e}")

def show_logs(lines=20):
    """show recent logs"""
    log_file = os.path.join(SERVER_PATH, "logs", "latest.log")
    
    if not os.path.exists(log_file):
        # try old location
        log_file = os.path.join(SERVER_PATH, "server.log")
    
    if not os.path.exists(log_file):
        print("no log file found")
        return
    
    with open(log_file, "r") as f:
        all_lines = f.readlines()
        recent = all_lines[-lines:]
        
        for line in recent:
            print(line.strip())

def main():
    if len(os.sys.argv) < 2:
        print("usage: python manager.py [start|stop|restart|status|backup|logs]")
        return
    
    command = os.sys.argv[1].lower()
    
    commands = {
        "start": start_server,
        "stop": stop_server,
        "restart": restart_server,
        "status": get_status,
        "backup": backup_world,
        "logs": show_logs
    }
    
    if command in commands:
        commands[command]()
    else:
        print(f"unknown command: {command}")

if __name__ == "__main__":
    main()
