import pytest
from move_function import move

def test_move():
    #invalid_position = -2
    board = 20 * "-"
    with pytest.raises(ValueError, match="Invalid position"):
        move(board, "o", -2)