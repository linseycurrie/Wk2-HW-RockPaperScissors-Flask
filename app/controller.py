from flask import render_template, request, redirect
from app import app
from app.models.play_game import *
from app.models.player import *

@app.route('/')
def index():
    return render_template('index.html', title='Home')

@app.route('/add-players', methods=['POST'])
def add_new_players():
    name1 = request.form['name1']
    name2 = request.form['name2']
    add_players(name1, name2)
    return render_template('/index.html', title='Home')

@app.route('/player-moves', methods=['POST'])
def player1_make_move():
    print("set move")
    set_player1_move(move)
    return render_template('/index.html', title='Home')

# @app.route('/player/rock/<name>', methods=['POST'])
# def player2_make_move():
