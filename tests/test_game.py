from tic_tac_toe import Game, GameResult, ComputerPlayer, HumanPlayer, GameField


GAME_RESULTS = {
    GameResult.HUMAN : 'HUMAN WIN!!!',
    GameResult.COMPUTER: 'COMPUTER WIN!!!',
    GameResult.TIE: 'TIE'
}


def init_game() -> Game:
    computer = ComputerPlayer(player_figure='x')
    human = HumanPlayer(player_figure='o')
    game_field = GameField(dimension=3)
    return Game(players=[computer, human], game_field=game_field)


def test_announce_winner_human():
    game = init_game()
    game.game_result = GameResult.HUMAN
    assert game.announce_winner() == GAME_RESULTS[GameResult.HUMAN]


def test_announce_winner_computer():
    game = init_game()
    game.game_result = GameResult.COMPUTER
    assert game.announce_winner() == GAME_RESULTS[GameResult.COMPUTER]


def test_announce_winner_tie():
    game = init_game()
    game.game_result = GameResult.TIE
    assert game.announce_winner() == GAME_RESULTS[GameResult.TIE]
