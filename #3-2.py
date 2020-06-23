import math
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

def annealing(board):
  steps = 0
  temp = len(board)**2
  anneal_rate = 0.95
  new_h_cost = get_h_cost(board)
   
  while new_h_cost > 0:
    board = make_annealing_move(board,new_h_cost,temp)
    new_h_cost = get_h_cost(board)
    new_temp = max(temp * anneal_rate,0.01)
    temp = new_temp
    steps += 1
    if steps >= 50000:
      break
  return board

def make_annealing_move(board,h_to_beat,temp):
  board_copy = list(board)
  found_move = False
 
  while not found_move:
    board_copy = list(board)
    new_row = random.randint(0,len(board)-1)
    new_col = random.randint(0,len(board)-1)
    board_copy[new_col] = new_row
    new_h_cost = get_h_cost(board_copy)
    if new_h_cost < h_to_beat:  # next state better than current one
      found_move = True
    else:
      delta_e = h_to_beat - new_h_cost
      accept_probability = min(1,math.exp(delta_e/temp))
      found_move = random.random() <= accept_probability   # move to the next state only with that probability
   
  return board_copy

board = [2,2,1,2,1]

start_time = time.time()
print(annealing(board))
print("--- %s seconds ---" % (time.time() - start_time))
