#!/usr/bin/env python3
"""simple password manager with encryption"""

import json
import getpass
import base64
import random
import string
from hashlib import sha256
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
import os

VAULT_FILE = "vault.json"

def derive_key(password: str, salt: bytes) -> bytes:
    """derives encryption key from password"""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))

def encrypt_data(data: str, password: str) -> bytes:
    """encrypts data with password"""
    salt = os.urandom(16)
    key = derive_key(password, salt)
    f = Fernet(key)
    encrypted = f.encrypt(data.encode())
    return salt + encrypted

def decrypt_data(encrypted_data: bytes, password: str) -> str:
    """decrypts data with password"""
    salt = encrypted_data[:16]
    ciphertext = encrypted_data[16:]
    key = derive_key(password, salt)
    f = Fernet(key)
    return f.decrypt(ciphertext).decode()

def load_vault(password: str) -> dict:
    """loads and decrypts the vault"""
    if not os.path.exists(VAULT_FILE):
        return {}
    
    with open(VAULT_FILE, 'rb') as f:
        encrypted = f.read()
    
    try:
        decrypted = decrypt_data(encrypted, password)
        return json.loads(decrypted)
    except:
        raise ValueError("wrong password or corrupted vault")

def save_vault(vault: dict, password: str):
    """encrypts and saves the vault"""
    data = json.dumps(vault, indent=2)
    encrypted = encrypt_data(data, password)
    
    with open(VAULT_FILE, 'wb') as f:
        f.write(encrypted)

def generate_password(length=16, use_special=True) -> str:
    """generates a random password"""
    chars = string.ascii_letters + string.digits
    if use_special:
        chars += "!@#$%^&*()-_=+"
    
    return ''.join(random.choice(chars) for _ in range(length))

def main():
    print("=== password manager ===\n")
    
    # get master password
    if os.path.exists(VAULT_FILE):
        password = getpass.getpass("master password: ")
    else:
        print("no vault found. creating new one.")
        password = getpass.getpass("set master password: ")
        confirm = getpass.getpass("confirm password: ")
        if password != confirm:
            print("passwords dont match!")
            return
    
    # load vault
    try:
        vault = load_vault(password)
    except ValueError:
        print("error: wrong password or corrupted file")
        return
    
    # main loop
    while True:
        print("\ncommands: add, list, show <name>, gen, exit")
        cmd = input("> ").strip().split()
        
        if not cmd:
            continue
        
        if cmd[0] == "exit" or cmd[0] == "quit":
            save_vault(vault, password)
            print("vault saved. bye!")
            break
        
        elif cmd[0] == "add":
            name = input("entry name: ").strip()
            if name in vault:
                print(f"entry '{name}' already exists!")
                continue
            
            username = input("username: ").strip()
            entry_password = getpass.getpass("password: ").strip()
            notes = input("notes (optional): ").strip()
            
            vault[name] = {
                "username": username,
                "password": entry_password,
                "notes": notes
            }
            print(f"added '{name}'")
        
        elif cmd[0] == "list":
            if not vault:
                print("vault is empty")
            else:
                print("\nsaved entries:")
                for name in vault:
                    print(f"  - {name} ({vault[name]['username']})")
        
        elif cmd[0] == "show":
            if len(cmd) < 2:
                print("usage: show <name>")
                continue
            
            name = cmd[1]
            if name not in vault:
                print(f"'{name}' not found")
            else:
                entry = vault[name]
                print(f"\n  name: {name}")
                print(f"  username: {entry['username']}")
                print(f"  password: {entry['password']}")
                if entry.get('notes'):
                    print(f"  notes: {entry['notes']}")
        
        elif cmd[0] == "gen":
            length = input("length (default 16): ").strip()
            length = int(length) if length else 16
            pwd = generate_password(length)
            print(f"\ngenerated: {pwd}\n")
        
        else:
            print(f"unknown command: {cmd[0]}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\ninterrupted")
