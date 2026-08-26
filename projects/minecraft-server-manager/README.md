# Minecraft Server Manager

cli tool to manage my minecraft server. made this because i kept forgetting commands and my friends would get mad when the server was down

## features

- start/stop/restart server
- check player count
- backup world files
- view console logs
- auto-restart if it crashes

## requirements

- python 3.8+
- a running minecraft server (paper/spigot/vanilla)
- server.properties in the same folder

## setup

```bash
pip install -r requirements.txt
```

edit `config.json` with your server path and stuff

## usage

```bash
python manager.py start      # start the server
python manager.py stop       # graceful shutdown
python manager.py restart    # restart
python manager.py status     # check if running + player count
python manager.py backup     # create world backup
python manager.py logs       # show last 20 log lines
python manager.py console    # interactive console
```

## config

```json
{
  "server_path": "/home/user/minecraft_server",
  "jar_file": "paper.jar",
  "ram_mb": 4096,
  "backup_folder": "./backups",
  "auto_restart": true
}
```

## known bugs

- backup sometimes fails if server is lagging
- console mode doesnt handle ctrl+c well
- ram detection is wrong on windows (works fine on linux tho)

planning to add web ui eventually but thats a lot of work
