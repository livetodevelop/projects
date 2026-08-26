#!/usr/bin/env python3
"""website scraper for price tracking"""

import requests
from bs4 import BeautifulSoup
import json
import os
from datetime import datetime

HISTORY_FILE = "price_history.json"

def load_config():
    """load config from json"""
    if not os.path.exists("config.json"):
        print("config.json not found!")
        return None
    
    with open("config.json", "r") as f:
        return json.load(f)

def save_history(product_name, price):
    """save price to history file"""
    history = {}
    
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            history = json.load(f)
    
    if product_name not in history:
        history[product_name] = []
    
    history[product_name].append({
        "price": price,
        "timestamp": datetime.now().isoformat()
    })
    
    # keep only last 100 entries per product
    history[product_name] = history[product_name][-100:]
    
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=2)

def scrape_product(product):
    """scrape price from a product page"""
    name = product.get("name", "unknown")
    url = product.get("url")
    selector = product.get("selector")
    
    if not url or not selector:
        print(f"[{name}] missing url or selector")
        return None
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # try to find element with price
        element = soup.select_one(selector)
        
        if not element:
            print(f"[{name}] could not find price element")
            return None
        
        # extract text and try to parse as number
        price_text = element.get_text(strip=True)
        
        # remove currency symbols and commas
        import re
        price_match = re.search(r'[\d,]+\.?\d*', price_text.replace(',', ''))
        
        if not price_match:
            print(f"[{name}] could not parse price: {price_text}")
            return None
        
        price = float(price_match.group())
        print(f"[{name}] ${price:.2f}")
        
        return price
    
    except requests.RequestException as e:
        print(f"[{name}] error: {e}")
        return None

def send_discord_webhook(webhook_url, product_name, old_price, new_price):
    """send notification to discord webhook"""
    if old_price is None or new_price >= old_price:
        return
    
    drop = old_price - new_price
    percent = (drop / old_price) * 100
    
    message = {
        "content": f"🔥 Price Drop Alert!",
        "embeds": [{
            "title": product_name,
            "color": 3066993,
            "fields": [
                {"name": "Old Price", "value": f"${old_price:.2f}", "inline": True},
                {"name": "New Price", "value": f"${new_price:.2f}", "inline": True},
                {"name": "Drop", "value": f"${drop:.2f} ({percent:.1f}%)", "inline": True}
            ]
        }]
    }
    
    try:
        requests.post(webhook_url, json=message, timeout=5)
        print(f"sent discord notification for {product_name}")
    except:
        print("failed to send discord notification")

def add_product_interactive():
    """add new product to config interactively"""
    print("\nadd new product to track:\n")
    
    name = input("product name: ")
    url = input("product url: ")
    selector = input("css selector for price (e.g., .price): ")
    
    try:
        target = float(input("target price (optional, 0 to skip): "))
    except:
        target = 0
    
    config = load_config()
    
    if not config:
        config = {"products": [], "discord_webhook": ""}
    
    config["products"].append({
        "name": name,
        "url": url,
        "selector": selector,
        "target_price": target if target > 0 else None
    })
    
    with open("config.json", "w") as f:
        json.dump(config, f, indent=2)
    
    print(f"\nadded {name} to config!")

def show_history(product_name=None):
    """show price history"""
    if not os.path.exists(HISTORY_FILE):
        print("no history yet")
        return
    
    with open(HISTORY_FILE, "r") as f:
        history = json.load(f)
    
    if product_name:
        if product_name not in history:
            print(f"no history for {product_name}")
            return
        
        print(f"\nprice history for {product_name}:")
        for entry in history[product_name][-10:]:  # last 10
            time = entry["timestamp"][:16].replace("T", " ")
            print(f"  {time} - ${entry['price']:.2f}")
    else:
        for name in history:
            count = len(history[name])
            latest = history[name][-1]["price"] if history[name] else 0
            print(f"{name}: {count} entries, latest: ${latest:.2f}")

def main():
    import sys
    
    config = load_config()
    
    if not config:
        return
    
    # handle command line args
    if "--add" in sys.argv:
        add_product_interactive()
        return
    
    if "--history" in sys.argv:
        product = sys.argv[sys.argv.index("--history") + 1] if len(sys.argv) > 2 else None
        show_history(product)
        return
    
    use_discord = "--discord" in sys.argv
    webhook = config.get("discord_webhook", "")
    
    print("checking prices...\n")
    
    for product in config.get("products", []):
        name = product.get("name", "unknown")
        target = product.get("target_price")
        
        # get previous price
        old_price = None
        if os.path.exists(HISTORY_FILE):
            with open(HISTORY_FILE, "r") as f:
                history = json.load(f)
                if name in history and history[name]:
                    old_price = history[name][-1]["price"]
        
        # scrape new price
        new_price = scrape_product(product)
        
        if new_price is not None:
            save_history(name, new_price)
            
            # check if below target
            if target and new_price <= target:
                print(f"  *** {name} is below target (${target:.2f})! ***")
            
            # send discord notification
            if use_discord and webhook:
                send_discord_webhook(webhook, name, old_price, new_price)
        
        # be nice to servers
        import time
        time.sleep(2)
    
    print("\ndone!")

if __name__ == "__main__":
    main()
