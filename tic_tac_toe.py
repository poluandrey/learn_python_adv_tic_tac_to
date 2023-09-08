import random
from enum import Enum


def handle_dimension_input() -> int:
    while True:
        try:
            return int(input('Please input game field dimension'))
        except ValueError:
            print('Please use only number')


def handle_human_input(direction, dimension) -> int:
    while True:
        try:
            human_input = int(input(f'Enter a {direction} number within the range 1 and {dimension}:'))
            if validate_input(human_input, dimension):
                return human_input
            print("Input is outside the specified range. Try again.")
        except ValueError:
            print('Enter a number!')


def validate_input(human_input: int, dimension) -> bool:
    if not 1 <= human_input <= dimension:
        return False
    return True


class GameField:
    """represent game field"""

    def __init__(self, dimension):
        self.dimension: int = dimension
        self.field: list[list[str]] = self.create_empty_field()

    def collect_game_lines(self) -> list[list[str]]:
        """collect lines from the game field for the game_result checking"""
        lines = []
        diagonals = []
        columns = []
        # collect row
        lines.extend(self.field)
        # collect column
        for row_idx in range(self.dimension):
            for col_idx in range(self.dimension):
                columns.append(self.field[col_idx][row_idx])
            lines.append(columns)
            columns = []
        # collect diagonals
        for i in range(self.dimension):
            diagonals.append(self.field[i][i])
        lines.append(diagonals)
        diagonals = []
        for i in range(self.dimension):
            diagonals.append(self.field[i][self.dimension - i - 1])
        lines.append(diagonals)
        return lines

    def create_empty_field(self) -> list[list[str]]:
        return [['*' for _ in range(self.dimension)] for _ in range(self.dimension)]

    def __str__(self):
        return '\n'.join([' '.join(row) for row in self.field])

    def is_empty_cell_exists(self) -> bool:
        for row in self.field:
            if '*' in row:
                return True
        return False

    @staticmethod
    def determinate_winner(line: list) -> str | None:
        x_win = ['x', 'x', 'x']
        o_win = ['o', 'o', 'o']
        if line == x_win:
            return 'x'
        if line == o_win:
            return 'o'

    def check_winner(self) -> str | None:
        for line in self.collect_game_lines():
            if winner := self.determinate_winner(line):
                return winner


class PlayerType(Enum):
    HUMAN = 1
    COMPUTER = 0


class Player:
    """represent player"""

    def __init__(self, player_type: PlayerType, player_figure: str):
        self.type = player_type
        self.figure = player_figure

    def __str__(self):
        return 'first_player' if self.type else 'second_player'


class HumanPlayer(Player):

    def __init__(self, player_type: PlayerType, player_figure: str):
        super().__init__(player_type, player_figure)

    def make_move(self, game_field: GameField) -> None:
        row = handle_human_input('row', game_field.dimension)
        column = handle_human_input('column', game_field.dimension)
        while game_field.field[row - 1][column - 1] != '*':
            print('choose another cell!')
            print(game_field)
            row = handle_human_input('row', game_field.dimension)
            column = handle_human_input('column', game_field.dimension)
        game_field.field[row - 1][column - 1] = self.figure


class ComputerPlayer(Player):
    def _init(self, player_type: PlayerType, player_figure: str):
        super().__init__(player_type, player_figure)

    def make_move(self, game_field: GameField):
        empty_cells = [
            (row_idx, col_idx) for col_idx in range(game_field.dimension)
            for row_idx in range(game_field.dimension) if game_field.field[row_idx][col_idx] == '*'
        ]
        row_idx, column_idx = random.choice(empty_cells)
        game_field.field[row_idx][column_idx] = self.figure


class GameResult(Enum):
    HUMAN = 1
    COMPUTER = 0
    TIE = 2


class Game:
    """represent game"""

    def __init__(self, players: list[HumanPlayer | ComputerPlayer], game_field: GameField):
        self.players = players
        self.game_field = game_field
        self.game_result = None

    def player_move(self, player: ComputerPlayer | HumanPlayer) -> None:
        player.make_move(self.game_field)
        print(self.game_field)

    def start(self) -> None:
        print(self.game_field)
        while not self.game_result:
            for player in self.players:
                player.make_move(self.game_field)
                print(self.game_field)
                self.game_result = self.check_game_result()
                if self.game_result:
                    break
        self.announce_winner()

    def check_game_result(self) -> GameResult | None:
        winner_figure = self.game_field.check_winner()
        empty_cell_exists = self.game_field.is_empty_cell_exists()
        if not winner_figure and empty_cell_exists:
            return None
        if winner_figure:
            winner = [player for player in self.players if player.figure == winner_figure][0]
            return GameResult.HUMAN if winner.type == PlayerType.HUMAN else GameResult.COMPUTER
        return GameResult.TIE

    def announce_winner(self) -> None:
        if self.game_result in [GameResult.HUMAN, GameResult.COMPUTER]:
            print(f'{self.game_result.name} WIN!!!')
            return
        print(self.game_result.name)


def main():
    dimension = handle_dimension_input()
    first_player_figure = 'x' if random.randint(0, 1) else 'o'
    second_player_figure = 'o' if first_player_figure == 'x' else 'x'

    human = HumanPlayer(player_type=PlayerType.HUMAN, player_figure=first_player_figure)
    computer = ComputerPlayer(player_type=PlayerType.COMPUTER, player_figure=second_player_figure)

    if first_player_figure == 'x':
        players = [human, computer]
    else:
        players = [computer, human]

    print(f'You will play {human.figure}')
    game_field = GameField(dimension=dimension)

    game = Game(players=players, game_field=game_field)
    game.start()


if __name__ == '__main__':
    main()
