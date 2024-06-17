import os

from art import logo
from gamemanager import TicTacToe


def play_game():
    print(logo)
    start_game = input(
        "Ready to play? Press Y to continue. At any point, press Q to exit.\n"
    ).upper()
    if start_game == "Y":
        game_on = True
        game = TicTacToe()
        while game_on:
            game_on = game.play_round()
    elif start_game == "Q":
        os.system("clear")


if __name__ == "__main__":
    play_game()
