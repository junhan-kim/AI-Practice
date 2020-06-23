import random
import time

def get_h_cost(board):   # if collision occurs, add h value
  h = 0
  for i in range(len(board)):
    for j in range(i + 1,len(board)):
      if board[i] == board[j]:
        h += 1
      offset = j - i
      if board[i] == board[j] - offset or board[i] == board[j] + offset:
        h += 1     
  return h

def make_move_steepest_hill(board):
  moves = {}
  for col in range(len(board)):
    best_moves = board[col]
     
    for row in range(len(board)):
      if board[col] == row:
        continue        
      board_copy = list(board)
      board_copy[col] = row
      moves[(col,row)] = get_h_cost(board_copy)  # h_cost = the number of attacking queens
  
  best_moves = []
  h_to_beat = get_h_cost(board)
  for k,v in moves.items():
    if v < h_to_beat:   # get minimum value of attacking queens 
      h_to_beat = v
        
  for k,v in moves.items():
    if v == h_to_beat:  # move to minimum value
      best_moves.append(k)
    
  if len(best_moves) > 0:  # if not ended
    pick = random.randint(0,len(best_moves) - 1)   # random pick
    col = best_moves[pick][0]
    row = best_moves[pick][1]
    board[col] = row    
  return board

board = [2,2,1,2,1]

start_time = time.time()
while sorted(set(board)) != sorted(board):  # queens are in conflict
  board = make_move_steepest_hill(board)
print(board)
print("--- %s seconds ---" % (time.time() - start_time))