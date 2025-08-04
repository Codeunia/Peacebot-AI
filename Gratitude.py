# gratitude.py

import json
import datetime
import os

DATA_FILE = "gratitude_log.json" 

def log_gratitude():
    print("Let's do a quick gratitude practice 🌈")
    gratitude_list = []
    for i in range(1, 4):
        item = input(f"Thing {i} you're grateful for: ")
        gratitude_list.append(item)

    entry = {
        "timestamp": str(datetime.datetime.now()),
        "gratitude": gratitude_list
    }
    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []

    data.append(entry)

    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

    return "Your gratitude list is saved 💛 Take a moment to feel the warmth."
