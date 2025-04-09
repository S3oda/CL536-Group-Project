from flask import Flask, jsonify, request
from models import load_games, save_games

app = Flask(__name__)
games = load_games()

@app.route('/')
def home():
    return "Welcome to the Mobile Game Marketplace API!"

@app.route('/games', methods=['GET'])
def get_games():
    return jsonify(games)

@app.route('/games', methods=['POST'])
def add_game():
    new_game = request.get_json()
    games.append(new_game)
    save_games(games)
    return jsonify({"message": "Game added successfully!"}), 201

if __name__ == '__main__':
    app.run(debug=True)
