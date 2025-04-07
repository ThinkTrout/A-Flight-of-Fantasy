from flask import Flask, render_template, request, jsonify
from os import system

app = Flask(__name__)

# Game state (in-memory)
game_state = {
    "log": ["You awaken in a cold, dark room."]
}

class Player:
    def __init__(self):
        self.stamina = 5
        self.strength = 5
        self.charisma = 5
        self.luck = 5
        self.intelligence = 5
        self.health = 50
        self.mana = 0
        self.wealth = 5

        self.status_effects = {
            "exhausted": False,
            "reeking": False,
            "famished": False,
            "bleeding": False,
            "poisoned": False,
            "intoxicated": False,
            "wanted": False,
        }

        self.reputation = {
            "Rathgard": "neutral",
            "Aramorn": "neutral",
            "Caeralon": "neutral",
            "Saramond": "neutral",
            "Thalidan": "neutral",
            "Belaneth": "neutral",
            "Ninespire": "neutral",
        }

@app.route("/")
def index():
    return render_template("index.html", state={"log": []}, player=player)

if __name__ == '__main__':
    player = Player()
    app.run(host='0.0.0.0', port=5000, debug=True)
