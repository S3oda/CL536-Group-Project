import json

DATA_FILE = 'data.json'

def load_games():
    try:
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_games(games):
    with open(DATA_FILE, 'w') as file:
        json.dump(games, file, indent=4)
