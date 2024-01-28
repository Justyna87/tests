import pytest
from move_function import move


def test_move():
    board = 20 * "-"
    assert move(board, "x",6)== "------x-------------"

