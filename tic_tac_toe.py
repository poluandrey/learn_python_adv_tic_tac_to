import random


class GameField:
    """represent game field"""
    def __init__(self, dimension):
        self.dimension: int = dimension
        self.field: list[list[str]] = [['*' for _ in range(self.dimension)] for _ in range(self.dimension)]

    def __repr__(self):
        return '\n'.join([' '.join(row) for row in self.field])

    def is_empty_sell_exists(self) -> bool:
        empty_sell_exists = True
        for row in self.field:
            if '*' in row:
                empty_sell_exists = True
                break
            empty_sell_exists = False
        return empty_sell_exists

    @staticmethod
    def determinate_winner(line: list) -> str | None:
        winner = None
        x_win = ['x', 'x', 'x']
        o_win = ['o', 'o', 'o']
        if line == x_win:
            winner = 'x'
        if line == o_win:
            winner = 'o'
        return winner

    def check_winner(self) -> str | None:

        # check row
        for row in self.field:
            winner = self.determinate_winner(row)
            if winner:
                return winner
        # check column
        line = []
        for row_idx in range(self.dimension):
            for col_idx in range(self.dimension):
                line.append(self.field[col_idx][row_idx])
            winner = self.determinate_winner(line)
            if winner:
                return winner
            line = []
        # check first diagonal
        for i in range(self.dimension):
            line.append(self.field[i][i])
        winner = self.determinate_winner(line)
        if winner:
            return winner
        line = []
        # check second diagonal
        for i in range(self.dimension):
            line.append(self.field[i][self.dimension - 1 - i])
        winner = self.determinate_winner(line)
        if winner:
            return winner


class Player:
    """represent player"""
    def __init__(self, player_type, player_figure):
        self.type = player_type
        self.figure = 'x' if player_figure else 'o'

    def __repr__(self):
        return 'human' if self.type else 'computer'

    @staticmethod
    def input(direction) -> int:
        while True:
            try:
                value = int(input(f'Enter a {direction} number within the range 1 and {game_field.dimension}:'))
                if 1 <= value <= game_field.dimension:
                    break
                else:
                    print("Input is outside the specified range. Try again.")
            except ValueError:
                print('Enter a number!')
        return value

    def make_move(self, game_field: GameField) -> None:
        if self.type:
            row = self.input('row')
            column = self.input('column')
            while game_field.field[row - 1][column - 1] != '*':
                print('choose another cell!')
                print(game_field)
                row = self.input('row')
                column = self.input('column')
            game_field.field[row - 1][column - 1] = self.figure
        else:
            empty_cell = [
                (row_idx, col_idx) for col_idx in range(game_field.dimension)
                for row_idx in range(game_field.dimension) if game_field.field[row_idx][col_idx] == '*']
            computer_choose = random.choice(empty_cell)
            row_idx, column_idx = computer_choose
            game_field.field[row_idx][column_idx] = self.figure


class Game:
    """represent game"""
    def __init__(self, player_1: Player, player_2: Player, game_field: GameField):
        if player_1.figure == 'x':
            self.first_player = player_1
            self.second_player = player_2
        else:
            self.first_player = player_2
            self.second_player = player_1
        self.game_field = game_field
        self.winner = None

    def start(self) -> None:
        print(game_field)
        while True:
            self.first_player.make_move(self.game_field)
            print(game_field)
            self.check_winner()
            if self.winner:
                break
            self.second_player.make_move(self.game_field)
            print(game_field)
            self.check_winner()
            if self.winner:
                break
        self.announce_winner()

    def check_winner(self) -> None:
        if not self.game_field.is_empty_sell_exists():
            self.winner = 'TIE'
            return
        winner_figure = game_field.check_winner()
        if winner_figure:
            self.winner = player_1 if winner_figure == player_1.figure else player_2

    def announce_winner(self) -> None:
        if isinstance(self.winner, Player):
            print(f'{self.winner} WIN!!!')
            return
        print(self.winner)


if __name__ == '__main__':
    first_player_figure = random.randint(0, 1)
    second_player_figure = 0 if first_player_figure else 1
    player_1 = Player(player_type=1, player_figure=first_player_figure)
    player_2 = Player(player_type=0, player_figure=second_player_figure)
    print(player_1.figure, player_2.figure)
    game_field = GameField(dimension=3)

    game = Game(player_1=player_1, player_2=player_2, game_field=game_field)
    game.start()
