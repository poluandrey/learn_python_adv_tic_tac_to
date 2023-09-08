from tic_tac_toe import GameField


def test_init_empty_field():
    empty_field = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]
    game_field = GameField(dimension=3)
    assert game_field.field == empty_field


def test_is_empty_cell_exists_for_new_field():
    game_field = GameField(dimension=3)
    assert game_field.is_empty_cell_exists()


def test_is_empty_cell_exists_for_full_filled_field():
    game_field = GameField(dimension=3)
    game_field.field = [['x', 'x', 'x'], ['x', 'x', 'x'], ['x', 'x', 'x']]
    assert not game_field.is_empty_cell_exists()


def test_is_empty_cell_exists_for_part_filled_field():
    game_field = GameField(dimension=3)
    game_field.field = [['x', '*', 'x'], ['x', 'x', 'x'], ['x', 'x', '*']]
    assert game_field.is_empty_cell_exists()


def test_collect_game_lines():
    game_field = GameField(dimension=3)
    assert len(game_field.collect_game_lines()) == 8
