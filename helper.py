def createBoard():
  matrix = [None, None, None]
  matrix[0] = [1, 2, 3]
  matrix[1] = [4, 5, 6]
  matrix[2] = [7, 8 ,9]
  return matrix

board = createBoard()

def displayMovesAndSaveInput(matrix):
  print(repr(matrix[0]).rjust(2) + '\n', repr(matrix[1]).rjust(3) + '\n', repr(matrix[2]).rjust(4) + '\n')
  selected = input('Your move: ')
  if 1 <= int(selected) <= 9:
    return int(selected)
  else: 
    print('You have selected something not in range please try again')
    displayMovesAndSaveInput(matrix)



def acceptMoveAndToggle(num, matrix, players):
  if players['playerOneTurn']:
    if 1<= num <= 3:
      matrix[0][num] = players['playerOneSymbol']
      players['playerOneTurn'] = False
      return matrix
    if 4 <= num <= 6:
      matrix[1][num] = players['playerOneSymbol']
      players['playerOneTurn'] = False
      return matrix
    if 7 <= 8 <= 9:
      matrix[2][num] = players['playerOneSymbol']
      players['playerOneTurn'] = False
      return matrix
  elif players['playerTwoTurn'] and players['playerOneTurn'] == False:
    if 1<= num <= 3:
      matrix[0][num] = players['playerTwoSymbol']
      players['playerTwoTurn'] = False
      return matrix
    if 4 <= num <= 6:
      matrix[1][num] = players['playerTwoSymbol']
      players['playerTwoTurn'] = False
      return matrix
    if 7 <= 8 <= 9:
      matrix[2][num] = players['playerTwoSymbol']
      players['playerTwoTurn'] = False
      return matrix
  else:
    print('not an acceptable move')
    pass

# yourMoveNumber = int(displayMovesAndSaveInput(board))
# print('your move number yype', type(yourMoveNumber))
# acceptMoveAndToggle(1, board, {'playerOneSymbol': 'X', 'playerOneName': 'jj', 'playerTwoName': 'kk', 'playerTwoScore': 0, 'playerTwoTurn': False, 'playerOneTurn': True, 'playerOneScore': 0, 'playerTwoSymbol': 'O'})

# acceptMoveAndToggle(yourMoveNumber, board, players

#while (there is no winner):
# play()
# inside play function do the checks and the prompts and everything

# def checkRowWinner()
# def checkColWinner()
# def checkDiagWinner()

