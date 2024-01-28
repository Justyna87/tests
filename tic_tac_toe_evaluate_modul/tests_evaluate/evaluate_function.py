
def evaluate (board): # checks the board, if it is full, not full, somebody won?
 if x_won in board:
   print("x won")  #if true - must be stopped
   return True
 elif o_won in board:
   print("o won") # if true -must be stopped
   return True
 elif element3 not in board:
   print("board is full, end of the game \n")  # if true - must be stopped
   return True
 else:
   print("\n")
   return False

empty_board = 20 * "-"
x_won = "xxx"
o_won ="ooo"
element3 = "-"