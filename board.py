class TicTacToeBoard:
    def __init__(self):
        self.build_board()
        self.locations = [(i, j) for i in range(1, 4) for j in range(1, 4)]
        self.available_locations = self.locations.copy()

    def build_board(self):
        self.col_ids = "  1   2   3 \n"
        self.div_row = " ___________\n"
        self.div_col = "   |   |   "
        self.board = [
            self.col_ids,
            "1" + self.div_col,
            self.div_row,
            "2" + self.div_col,
            self.div_row,
            "3" + self.div_col,
        ]

    def display_board(self):
        print("\n".join(self.board))

    def update_board(self, selected_loc, symbol):
        self.col_mapping = {1: 2, 2: 6, 3: 10}
        self.row_mapping = {1: 1, 2: 3, 3: 5}
        row = self.row_mapping.get(selected_loc[0])
        col = self.col_mapping.get(selected_loc[1])
        updated_row = self.board[row][:col] + symbol + self.board[row][col + 1 :]  # type: ignore
        self.board[row] = updated_row  # type: ignore
        self.available_locations.remove(selected_loc)
