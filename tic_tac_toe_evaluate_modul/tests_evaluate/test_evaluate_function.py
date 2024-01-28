import pytest
from evaluate_function import evaluate
x_won = 'xxx'
board = 20 * "-"

@pytest.mark.parametrize("board,expected", [("xooxxxo-x", True), ("oxxoooxxo", True), ("xoxxoooxx", True), ("x-oxxoo-o-", False)])
def test_evaluate(board, expected):
    assert evaluate(board) == expected

      # Define different test scenarios
   # board_x_won = "xooxxxoox"
    #board_o_won = "oxxoooxxo"
    #board_full = "xoxxoooxx"
    #board_not_full = "x-oxxoo-o-"
    

    # Test for x won
    #assert evaluate(board_x_won) == True
    # Test for o won
    #assert evaluate(board_o_won) == True
    # Test for board full
    #assert evaluate(board_full) == True
    # Test for board not full
    #assert evaluate(board_not_full) == False


  #assert evaluate('----xxx-----o-o-o---') == expected
  #assert evaluate(x_won) == True
  #assert evaluate('---------ooo---x-o-x') == True
  #assert evaluate('xooxxooxxooxxoxoxoxx') == True
  #assert evaluate('--o--x--o--x-o--o--x') == False