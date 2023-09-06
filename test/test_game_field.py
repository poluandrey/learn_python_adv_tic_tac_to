from tic_tac_toe import GameField


def test_gamefield_create_empty_field():
    empty_field = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]
    game_field = GameField(dimension=3)
    assert game_field.field == empty_field


def test_gamefield_is_empty_cell_exists():
    empty_game_field = GameField(dimension=3)
    assert empty_game_field.is_empty_cell_exists()
    not_empty_game_field = GameField(dimension=3)
    not_empty_game_field.field = [['x', 'x', 'x'], ['x', 'x', 'x'], ['x', 'x', 'x']]
    print(not_empty_game_field.field)
    assert not not_empty_game_field.is_empty_cell_exists()


def test_gamefield_collect_game_lines():
    game_field = GameField(dimension=3)
    assert len(game_field.lines) == 8
