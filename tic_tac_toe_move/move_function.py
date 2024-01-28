def move(board, mark, position):
  if position <0:
    raise ValueError("Invalid position")
  
  new_board = board[:position] + mark + board[position+1:]
  return new_board
