import pytest
from evaluate_function import evaluate

   # Define different test scenarios
board_x_won = "xooxxxoox"
board_o_won = "oxxoooxxo"
board_full = "xoxxoooxx"
board_not_full = "x-oxxoo-o-"
    
def test_evaluate():
    # Test for x won
    assert evaluate(board_x_won) == True
    # Test for o won
    assert evaluate(board_o_won) == True
    # Test for board full
    assert evaluate(board_full) == True
    # Test for board not full
    assert evaluate(board_not_full) == False

