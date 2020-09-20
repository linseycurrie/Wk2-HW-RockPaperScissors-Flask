from app.models.player import *
import random 

player1 = Player("PLayer 1")
player2 = Player("Player 2")
players = [player1, player2]

def one_player(name1):
    player1.name = name1
    player2.name = "Computer"

def add_players(name1, name2):
    player1.name = name1
    player2.name = name2

def random_move(self):
    options = ["rock", "paper", "scissors"]
    move = random.choice(options)
    return move

def set_moves(move1, move2):
    player1.move = move1
    player2.move = move2


def result():
    if player1.move == player2.move:
        return "Oooh it's a draw"
    elif (player1.move == "rock" and player2.move == "scissors"):
        return players[0].name + " wins"
    elif(player1.move == "scissors" and player2.move == "paper"):
        return players[0].name + " wins"
    elif(player1.move == "paper" and player2.move == "rock"):
        return players[0].name + " wins"
    else:
        return players[1].name + " wins"
    