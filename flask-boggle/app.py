from boggle import Boggle
from flask import Flask, request, render_template, redirect, jsonify, flash, session, render_template_string

app = Flask(__name__)
app.secret_key = 'your_secret_key' 


boggle_game = Boggle()
with open('words.txt') as file:
    word_list = file.readlines()
    words = list(map(lambda x: x.strip(), word_list))

@app.route('/', methods=['GET','POST'])
def index():
    # game_board = boggle_game.make_board()
    if request.method == 'GET':
        game_board = boggle_game.make_board()
        session['game'] = game_board
    else:
        game_board = session.get('game')
    # session['game'] = game_board
    if request.method == 'POST':
        data = request.get_json()
        #! why make me check if it's in words if the function check_valid_word does it already?
        if data["guessWord"] in words:
            result = boggle_game.check_valid_word(game_board, data["guessWord"])
            return jsonify({'result': result}), 200
        return jsonify({"result": "not-a-word"}), 200
    
    return render_template('index.html', game_board = session['game'])

# @app.route('/', methods=['POST'])
# def receive_data():

@app.route('/score', methods=['POST'])
def receive_score():
    if 'recent_scores' not in session:
        session['recent_scores'] = []
    # if 'game_stats' not in session:
    #     session["game_stats"] = {"best_score":0, "total_games":0}
        
        
    data = request.get_json()
    
    # currently not using recent_score
    if len(session["recent_scores"]) < 7:
        session["recent_scores"] = session["recent_scores"] + [data["score"]]
    else:
        session["recent_scores"] = session["recent_scores"][1:] + [data["score"]]
    
    best_score = max(data["score"], session["game_stats"]["best_score"])
    total_games = session["game_stats"]["total_games"] + 1
    
    session["game_stats"] = {"best_score": best_score, "total_games": total_games}
    
    scores = {
        "best_score": best_score,
        "total_games": total_games,
    }

    return jsonify(scores)
@app.route('/start')
def start():
    if "game_stats" not in session:
        session["game_stats"] = {"best_score":0, "total_games":0}

    return session["game_stats"]


if __name__ == "__main__":
   app.run(debug=True)