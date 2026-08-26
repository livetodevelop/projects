#!/usr/bin/env python3
"""
Extension ID Unblocker (run on personal computer)

this script fetches a list of chrome extensions and checks which ones
aren't blocked by your school's admin console yet.

requires: requests, beautifulsoup4
install: pip install requests beautifulsoup4

WARNING: this is kinda sketchy and might violate school policies.
use at your own risk.
"""

import requests
from bs4 import BeautifulSoup
import json

# popular extension IDs (you'd need to find these yourself)
# i'm not including actual IDs here because that's asking for trouble
EXTENSION_IDS = [
    # add extension IDs here from chrome web store URLs
    # example: https://chrome.google.com/webstore/detail/EXTENSION_ID_HERE
]

def check_extension(extension_id):
    """check if an extension is blocked"""
    url = f"https://clients2.google.com/service/update2/crx?response=redirect&prodversion=98.0&acceptformat=crx2,crx3&x=id%3D{extension_id}%26uc"
    
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return True  # not blocked
        else:
            return False  # blocked or doesn't exist
    except:
        return False

def main():
    print("Extension Unblocker")
    print("=" * 40)
    print("Run this on a personal computer, not school chromebook!")
    print()
    
    unblocked = []
    
    for ext_id in EXTENSION_IDS:
        print(f"Checking {ext_id}...", end=" ")
        if check_extension(ext_id):
            print("✓ Not blocked")
            unblocked.append(ext_id)
        else:
            print("✗ Blocked")
    
    print()
    print(f"Results: {len(unblocked)}/{len(EXTENSION_IDS)} extensions not blocked")
    
    if unblocked:
        print("\nUnblocked extensions:")
        print(json.dumps(unblocked, indent=2))
        print("\nTo install: go to chrome://extensions/, enable Developer Mode,")
        print("click 'Load unpacked' and point to the extension folder.")

if __name__ == "__main__":
    main()
