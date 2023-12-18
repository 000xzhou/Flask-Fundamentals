from boggle import Boggle
from flask import Flask, request, render_template, redirect, jsonify, flash, session

app = Flask(__name__)
app.secret_key = 'your_secret_key' 

boggle_game = Boggle()
game_board = boggle_game.make_board()
with open('words.txt') as file:
    word_list = file.readlines()
    words = list(map(lambda x: x.strip(), word_list))

@app.route('/')
def index():
    session['game'] = game_board
    session["game_count"] = []
    print(session["game_count"])
    return render_template('index.html', game_board = session['game'], game_count = session["game_count"])

@app.route('/', methods=['POST'])
def receive_data():
    data = request.get_json()
    #! why make me check if it's in words if the function check_valid_word does it already?
    if data["guessWord"] in words:
        result = boggle_game.check_valid_word(game_board, data["guessWord"])
        return jsonify({'result': result}), 200
    return jsonify({"result": "not-a-word"}), 200

@app.route('/score', methods=['POST'])
def receive_score():
    data = request.get_json()
    print(data)
    session["game_count"].append(data)
    new_game_board = boggle_game.make_board()
    session['game'] = new_game_board
    response = {
        "scoreData": data,
        "newGameBoard": new_game_board
    }
    return jsonify(response)


if __name__ == "__main__":
   app.run(debug=True)