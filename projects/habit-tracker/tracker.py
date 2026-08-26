#!/usr/bin/env python3
"""simple habit tracker with streaks"""

import json
import os
from datetime import datetime, timedelta

DATA_FILE = "habits.json"

def load_data() -> dict:
    """loads habit data from file"""
    if not os.path.exists(DATA_FILE):
        return {"habits": {}}
    
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def save_data(data: dict):
    """saves habit data to file"""
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def get_today() -> str:
    """returns today's date as string"""
    return datetime.now().strftime("%Y-%m-%d")

def calculate_streak(dates: list) -> int:
    """calculates current streak from list of dates"""
    if not dates:
        return 0
    
    # sort dates newest first
    sorted_dates = sorted(dates, reverse=True)
    today = get_today()
    yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
    
    # check if streak is active (done today or yesterday)
    if sorted_dates[0] != today and sorted_dates[0] != yesterday:
        return 0
    
    streak = 1
    for i in range(1, len(sorted_dates)):
        prev_date = datetime.strptime(sorted_dates[i-1], "%Y-%m-%d")
        curr_date = datetime.strptime(sorted_dates[i], "%Y-%m-%d")
        
        if (prev_date - curr_date).days == 1:
            streak += 1
        else:
            break
    
    return streak

def add_habit(data: dict, name: str):
    """adds a new habit"""
    if name in data["habits"]:
        print(f"habit '{name}' already exists!")
        return
    
    data["habits"][name] = {
        "created": get_today(),
        "completed_dates": []
    }
    save_data(data)
    print(f"added habit: {name}")

def mark_done(data: dict, name: str = None):
    """marks habit(s) as done for today"""
    today = get_today()
    
    if name:
        if name not in data["habits"]:
            print(f"habit '{name}' not found")
            return
        
        if today in data["habits"][name]["completed_dates"]:
            print(f"'{name}' already marked for today")
            return
        
        data["habits"][name]["completed_dates"].append(today)
        save_data(data)
        print(f"marked '{name}' as done!")
    else:
        # show all habits and let user pick
        print("\nhabits to mark done:")
        for i, habit_name in enumerate(data["habits"].keys(), 1):
            completed = today in data["habits"][habit_name]["completed_dates"]
            status = "✓" if completed else " "
            print(f"  {i}. [{status}] {habit_name}")
        
        print("\nEnter habit number (or 0 to cancel):")
        try:
            choice = int(input("> "))
            if choice == 0:
                return
            
            habit_name = list(data["habits"].keys())[choice - 1]
            mark_done(data, habit_name)
        except (ValueError, IndexError):
            print("invalid choice")

def show_stats(data: dict):
    """shows all habits with their streaks"""
    if not data["habits"]:
        print("no habits tracked yet. add one with 'add <name>'")
        return
    
    print("\n=== habit stats ===\n")
    
    for name, habit in data["habits"].items():
        streak = calculate_streak(habit["completed_dates"])
        total = len(habit["completed_dates"])
        created = habit["created"]
        
        print(f"{name}:")
        print(f"  streak: {streak} days")
        print(f"  total completions: {total}")
        print(f"  created: {created}")
        print()

def show_history(data: dict, name: str):
    """shows completion history for a habit"""
    if name not in data["habits"]:
        print(f"habit '{name}' not found")
        return
    
    habit = data["habits"][name]
    dates = sorted(habit["completed_dates"], reverse=True)
    
    print(f"\nhistory for '{name}':\n")
    
    if not dates:
        print("  no completions yet")
        return
    
    # show last 30 entries
    for date in dates[:30]:
        print(f"  - {date}")
    
    if len(dates) > 30:
        print(f"  ... and {len(dates) - 30} more")

def main():
    print("=== habit tracker ===\n")
    
    data = load_data()
    
    while True:
        print("commands: add <name>, done, stats, history <name>, exit")
        cmd = input("> ").strip().split()
        
        if not cmd:
            continue
        
        if cmd[0] == "exit" or cmd[0] == "quit":
            print("bye! keep up your habits!")
            break
        
        elif cmd[0] == "add":
            if len(cmd) < 2:
                print("usage: add <habit name>")
                continue
            name = " ".join(cmd[1:])
            add_habit(data, name)
        
        elif cmd[0] == "done":
            name = " ".join(cmd[1:]) if len(cmd) > 1 else None
            mark_done(data, name)
        
        elif cmd[0] == "stats":
            show_stats(data)
        
        elif cmd[0] == "history":
            if len(cmd) < 2:
                print("usage: history <habit name>")
                continue
            name = " ".join(cmd[1:])
            show_history(data, name)
        
        else:
            print(f"unknown command: {cmd[0]}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\ninterrupted")
