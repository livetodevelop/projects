# habit tracker

tracks habits and shows streaks. made this because i kept forgetting to practice guitar and stuff.

## setup
```bash
pip install -r requirements.txt
python tracker.py
```

## features
- add habits you want to track
- mark habits as done for today
- see your current streak
- simple text-based interface
- saves data to json file

## usage
when you run it, you can:
- `add <habit>` - add a new habit
- `done` - mark habits as complete for today
- `stats` - show all habits with streaks
- `history <habit>` - show completion history
- `exit` - quit

## data
all data is stored in `habits.json`. you can edit it manually if needed but the program should handle everything.

## todo
- maybe add a gui later
- export data to csv or something
- reminders? idk if thats possible
