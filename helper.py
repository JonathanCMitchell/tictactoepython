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
    print('spot taken')
    return displayMovesAndSaveInput(matrix)



def acceptMoveAndToggle(num, matrix, players, attempts):
  if players['playerOneTurn']:
    if 1<= num <= 3:
      if not matrix[1][num] == players['playerOneSymbol']:
        matrix[0][num] = players['playerOneSymbol']
        players['playerOneTurn'] = False
        return matrix
      else:
        if attempts < 10:
          tryAgain(num, matrix, players, attempts + 1)
        else:
          pass
    if 4 <= num <= 6:
      if not matrix[1][num] == players['playerOneSymbol']:
        matrix[1][num] = players['playerOneSymbol']
        players['playerOneTurn'] = False
        return matrix
      else:
        if attempts < 10:
          tryAgain(num, matrix, players, attempts + 1)
        else:
          pass
    if 7 <= 8 <= 9:
      if not matrix[2][num] == players['playerOneSymbol']:
        matrix[2][num] = players['playerOneSymbol']
        players['playerOneTurn'] = False
        return matrix
      else:
        if attempts < 10:
          tryAgain(num, matrix, players, attempts + 1) 
        else:
          pass  
  elif players['playerTwoTurn'] and players['playerOneTurn'] == False:
    if 1<= num <= 3:
      if not matrix[0][num] == players['playerTwoSymbol']:
        matrix[0][num] = players['playerTwoSymbol']
        players['playerTwoTurn'] = False
        return matrix
      else: 
        if attempts < 10:
          tryAgain(num, matrix, players, attempts + 1)
        else:
          pass
    if 4 <= num <= 6:
      if not matrix[1][num] == players['playerTwoSymbol']:
        matrix[1][num] = players['playerTwoSymbol']
        players['playerTwoTurn'] = False
        return matrix
      else: 
        if attempts < 10:
          tryAgain(num, matrix, players, attempts + 1)
        else:
          pass
    if 7 <= 8 <= 9:
      if not matrix[2][num] == players['playerTwoSymbol']:
        matrix[2][num] = players['playerTwoSymbol']
        players['playerTwoTurn'] = False
        return matrix
      else:
        if attempts < 10:
          tryAgain(num, matrix, players, attempts + 1)
        else:
          pass
  else:
    print('not an acceptable move')
    acceptMoveAndToggle(num, matrix, players)
    pass

  def tryAgain(num, matrix, players, count):
    print('That spot has already been taken, Please try again')
    return acceptMoveAndToggle(num, matrix, players, count)

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

