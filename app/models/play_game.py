from app.models.player import *

player1 = Player("Jill")
player2 = Player("Jack")


def add_players(name1, name2):
    player1.name = name1
    player2.name = name2

def set_player1_move(move):
    player1.move = move

def set_player2_move(move):
    player2.move = move


def result():
    if player1.move == player2.move:
        return print("Draw")
    elif (player1.move == "rock" and player2.move == "scissors"):
        return print("Player 1 wins")
    elif(player1.move == "scissors" and player2.move == "paper"):
        return print("Player 1 wins")
    elif(player1.move == "paper" and player2.move == "rock"):
        return print("Player 1 wins")
    else:
        return print("Player 2 wins")
    