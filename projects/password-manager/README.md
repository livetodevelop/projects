# password manager thing

a simple password manager i made because browser password managers are kinda sketchy. stores everything encrypted in a json file.

## features
- encrypts passwords with a master password
- can generate random passwords
- stores usernames and notes too
- everything is in one file so its easy to backup

## setup
```bash
pip install -r requirements.txt
python passman.py
```

## usage
when you run it, it will ask for your master password. if this is your first time, just enter a new password and it will create the vault.

commands:
- `add` - add a new entry
- `list` - show all entries (passwords hidden)
- `show <name>` - show password for an entry
- `gen` - generate a random password
- `exit` - quit

## security note
im not like a security expert or anything but it uses aes encryption so it should be pretty good. just dont forget your master password because theres no recovery lol

## warning
this is probably not as secure as bitwarden or 1password but its good enough for school accounts and stuff
