import os

from board import TicTacToeBoard
from player import Player


class TicTacToe:
    def __init__(self):
        self.board = TicTacToeBoard()
        self.player1 = Player(1)
        self.player2 = Player(2)
        self.max_rounds = 9
        self.current_round = 0
        self.current_player = self.player1

    def clean_input(self):
        if len(self.loc_input) == 3:
            choice = self.loc_input.split(",")
            row = int(choice[0])
            col = int(choice[1])
            self.selected_location = (row, col)

    def play_round(self):
        os.system("clear")
        self.board.display_board()

        self.loc_input = input(
            f"Player {self.current_player.player_num}, where would you like to play? "
            "Enter the row number and column number separated by a comma.\n"
        )
        if self.loc_input == "Q":
            print("Exiting Game")
            return False

        self.clean_input()

        if self.selected_location in self.board.available_locations:
            self.board.update_board(self.selected_location, self.current_player.symbol)
            self.current_player.locations.append(self.selected_location)
            self.current_player.check_for_win()
            self.current_round += 1
            self.current_player = (
                self.player1 if self.current_round % 2 == 0 else self.player2
            )
            return self.check_for_winner()
        else:
            print("That is not a valid location, try again.")
            return self.play_round()

    def check_for_winner(self):
        if self.player1.has_won:
            os.system("clear")
            print("Player 1 has won!")
            self.board.display_board()
            return False
        elif self.player2.has_won:
            os.system("clear")
            print("Player 2 has won!")
            self.board.display_board()
            return False
        elif self.current_round == self.max_rounds:
            os.system("clear")
            print("Tie game, no winner.")
            self.board.display_board()
            return False
        else:
            return True
