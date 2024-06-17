class Player:
    def __init__(self, order):
        self.player_num = order
        self.has_won = False
        self.set_symbol()
        self.locations = []
        self.winning_locations = [
            set([(1, 1), (1, 2), (1, 3)]),
            set([(2, 1), (2, 2), (2, 3)]),
            set([(3, 1), (3, 2), (3, 3)]),
            set([(1, 1), (2, 1), (3, 1)]),
            set([(1, 2), (2, 2), (3, 2)]),
            set([(1, 3), (2, 3), (3, 3)]),
            set([(1, 1), (2, 2), (3, 3)]),
            set([(1, 3), (2, 2), (3, 1)]),
        ]

    def set_symbol(self):
        self.symbol = "X" if self.player_num == 1 else "O"

    def check_for_win(self):
        player_loc_set = set(self.locations)
        subsets = [i.issubset(player_loc_set) for i in self.winning_locations]
        self.has_won = any(subsets)
