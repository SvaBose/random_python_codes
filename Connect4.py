# Author: Svanik Bose

Player1 = input("Player Yellow, please enter your name ")
Player2 = input("Player Red, please enter your name ")


def chip_place(board, col, player):
  for i in range(5, -1, -1):
    if board[i][col] == 0:
      board[i][col] = player
      break

  return board

def check_draw(board):
  counter = 0
  for row in board:
    for piece in row:
      if piece == 0: counter += 1

  if counter == 0:
    return True
  return None


def print_board(board):
  print("1 2 3 4 5 6 7" )
  for row in board:
    tmp_row = []
    for piece in row:
      if piece == 0:
        tmp_row.append(".")
      else:
        tmp_row.append(piece)
    print(" ".join(tmp_row))

  if not checkWinnerVertic(board) == None:
    return True
  if not checkWinnerHoriz(board) == None:
    return True
  if not checkWinnerDiagonal(board) == None:
    return True
  if check_draw(board) == True:
    return True


print("Instructions to play Connect 4: Once the game has started, keep placing your respective letters in a column. Once a player has placed 4 chips that are all connected, diagonally, vertically, or horizontaly, then that player wins the game! Good luck!")



def game(board): 
    print_board(board)
    col = input(Player1 + ", enter a column: ")
    if str.isdigit(col) and int(col) > 0 and int(col) <= 7:
        board = chip_place(board, int(col) - 1, 'Y')
    else:
        print("Invalid input, skipping turn")

    
    if print_board(board) == True:
      return True

    col = input(Player2 + ", enter a column: ")
    if str.isdigit(col) and int(col) > 0 and int(col) <= 7:
        board = chip_place(board, int(col) - 1, 'R')
    else:
        print("Invalid input, skipping turn")
        
    if print_board(board) == True:
      return True
    
    return board


def checkWinnerHoriz(board):
  for row in board:
    for i in range(len(row) - 3):
      if row[i] == row[i+1] and row[i+1] == row[i+2] and row[i+2] == row[i+3] and not row[i] == 0:
        return row[i]

def checkWinnerVertic(board):
    for r in range(len(board[0]) - 3): 
        for c in range(len(board) - 3):
            if board[c][r] == board[c + 1][r] and board[c+1][r] == board[c + 2][r] and board[c+2][r] == board[c + 3][r] and not board[c][r] == 0:
                return board[c][r]


def checkWinnerDiagonal(board):
    for r in range(len(board) - 3): 
        for c in range(len(board[0]) - 3):
            if board[r][c] == board[r + 1][c + 1]  and board[r+1][c+1] == board[r + 2][c + 2]  and board[r+2][c+2] == board[r + 3][c + 3] and not board[r][c] == 0:
              return board[r][c]
            if board[r + 3][c] == board[r + 2][c + 1]  and board[r+2][c+1] == board[r + 1][c + 2]  and board[r+1][c+2] == board[r][c + 3] and not board[r + 3][c] == 0:
              return board[r][c]

def main():
    board = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
    ]

    winner = None

    while True:
      game(board)
      winner = checkWinnerHoriz(board) or checkWinnerVertic(board) or checkWinnerDiagonal(board) or check_draw(board)

      if not winner == None:
        break

    if winner == True:
      print("Tie!")
    elif winner == "Y":
      print(Player1 + " won!")
    else:
      print(Player2 + " won!")

  



#Main Code
main()
