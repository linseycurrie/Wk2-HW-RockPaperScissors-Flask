from flask import render_template, request, redirect
from app import app
from app.models.play_game import *
from app.models.player import *


@app.route('/')
def index():
    return render_template('index.html', title='Home', players=players)

@app.route('/players', methods=['POST'])
def add_two_players():
    name1 = request.form['name1']
    name2 = request.form['name2']
    add_players(name1, name2)
    return render_template('/moves.html', title='Home', players=players)

@app.route('/moves', methods=['POST'])
def two_player_make_moves():
    move1 = request.form['move1']
    move2 = request.form['move2']
    set_moves(move1, move2)
    return render_template('/result.html', title='Home', players=players)

@app.route('/result', methods=['POST'])
def show_the_winner():
    display_result = result()
    return render_template('/result.html', title='Home', display_result=display_result)