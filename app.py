from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Basic game state (in-memory for now)
game_state = {
    "location": "a cold, dark room",
    "log": ["You awaken in a cold, dark room."],
}

@app.route('/')
def index():
    return render_template("index.html", state=game_state)

@app.route('/action', methods=['POST'])
def action():
    data = request.get_json()
    command = data.get("command", "").lower()

    response = handle_command(command)
    game_state["log"].append(response)
    return jsonify(game_state)

def handle_command(cmd):
    if cmd == "light fire":
        return "You light a small fire. The room feels a little warmer."
    elif cmd == "look":
        return "It's too dark to see anything. You hear the wind outside."
    else:
        return f"You try to '{cmd}', but nothing happens."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

