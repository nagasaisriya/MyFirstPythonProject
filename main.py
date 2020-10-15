#Game board

board=["-","-","-",
       "-","-","-",
       "-","-","-"]

#if game still game_still_going
game_still_going=True

#who won or tie
winner=None

#whos turn is it?
current_player="X"

def display_board():
  print(board[0]+" | "+board[1]+" | "+board[2])
  print(board[3]+" | "+board[4]+" | "+board[5])
  print(board[6]+" | "+board[7]+" | "+board[8])

#play a game of tic tac toe
def play_game():
  display_board()

  while game_still_going:

    #handle a single turn of an arbitrary palyer
    handle_turn(current_player)

    #check if game has ended
    check_if_game_over()
    
    #to flip to other players
    flip_player()

  #if game is ended
  if winner=="X" or winner=="O":
    print(winner+" won.")
  elif winner==None:
    print("Tie.")

#handle a single turn of arbitrary player
def handle_turn(player):

  print(player+"'s turn.")
  position=input("Choose a position from 1-9:")

  valid=False
  while not valid:

    while position not in ["1","2","3","4","5","6","7","8","9"]:
      position=input("Choose a position from 1-9:")

    position=int(position)-1

    if board[position]=="-":
      valid=True
    else:
      print("The position is already filled,Choose a different position.")

  board[position]=player
  display_board()


def check_if_game_over():
  check_for_winner()
  check_if_tie()

def check_for_winner():

  global winner
  #check row
  row_winner=check_rows()
  #check column
  column_winner=check_columns()
  #check diagonal
  diagonal_winner=check_diagonals()
  if row_winner:
    #theres a win
    winner=row_winner
  elif column_winner:
    #there is a win
    winner=column_winner
  elif diagonal_winner:
    #there is a win
    winner=diagonal_winner
  else:
    #there is no win
    winner=None


  return

def check_rows():
  #set up global variables
  global game_still_going

  #check if any row has same value
  row_1=board[0] == board[1] == board[2] != "-"
  row_2=board[3] == board[4] == board[5] != "-"
  row_3=board[6] == board[7] == board[8] != "-"

  if row_1 or row_2 or row_3:
    game_still_going=False

  #return winner x or o
  if row_1:
    return board[0]
  elif row_2:
    return board[3]
  elif row_3:
    return board[6]

  return

def check_columns():
  global game_still_going

  #check if any column has same value
  col_1=board[0] == board[3] == board[6] != "-"
  col_2=board[1] == board[4] == board[7] != "-"
  col_3=board[2] == board[5] == board[8] != "-"

  if col_1 or col_2 or col_3:
    game_still_going=False

  #return winner x or o
  if col_1:
    return board[0]
  elif col_2:
    return board[1]
  elif col_3:
    return board[2]
  return

def check_diagonals():
  global game_still_going
  #check if any diagonal has same value
  dia_1=board[0] == board[4] == board[8] != "-"
  dia_2=board[2] == board[4] == board[6] != "-"

  if dia_1 or dia_2 :
    game_still_going=False

  #return winner x or o
  if dia_1:
    return board[0]
  elif dia_2:
    return board[2]
  
  return

def check_if_tie():
  global game_still_going
  if "-" not in board:
    game_still_going=False

  return

def flip_player():
  #global variables
  global current_player
  #if current_player was X change it to O
  if current_player=="X":
    current_player="O"
  #if current_player was O change it to X
  elif current_player=="O":
    current_player="X"
  return

play_game()

#display_board()