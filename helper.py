def initializePlayers(players):
  players = {}
  playerOneName = input('Enter your name player one')
  if not playerOneName in players:
    players['playerOneScore'] = 0
    players['playerOneTurn'] = True
    players['playerOneSymbol'] = 'X'
    players['playerOneName'] = playerOneName

  playerTwoName = input('Enter your name player Two')
  if not playerTwoName in players:
    players['playerTwoScore'] = 0
    players['playerTwoTurn'] = False
    players['playerTwoSymbol'] = 'O'
    players['playerTwoName'] = playerTwoName
  return players


def createBoard():
  matrix = [None, None, None]
  matrix[0] = [0, 1, 2]
  matrix[1] = [3, 4, 5]
  matrix[2] = [6, 7 ,8]
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



def acceptMoveAndToggle(num, matrix, players):
  if players['playerOneTurn']:
    if 0<= num <= 2:
      if not matrix[1][num] == players['playerOneSymbol']:
        matrix[0][num] = players['playerOneSymbol']
        togglePlayers(players)
        return matrix
    elif 3 <= num <= 5:
      if not matrix[1][num] == players['playerOneSymbol']:
        matrix[1][num] = players['playerOneSymbol']
        togglePlayers(players)
        return matrix
    elif 6 <= 7 <= 8:
      if not matrix[2][num] == players['playerOneSymbol']:
        matrix[2][num] = players['playerOneSymbol']
        togglePlayers(players)
        return matrix
  elif players['playerTwoTurn'] and players['playerOneTurn'] == False:
    if 0<= num <= 2:
      if not matrix[0][num] == players['playerTwoSymbol']:
        matrix[0][num] = players['playerTwoSymbol']
        togglePlayers(players)
        return matrix
    elif 3 <= num <= 5:
      if not matrix[1][num] == players['playerTwoSymbol']:
        matrix[1][num] = players['playerTwoSymbol']
        togglePlayers(players)
        return matrix
    elif 6 <= num <= 8:
      if not matrix[2][num] == players['playerTwoSymbol']:
        matrix[2][num] = players['playerTwoSymbol']
        togglePlayers(players)
        return matrix
  else:
    print('not an acceptable move')
    acceptMoveAndToggle(num, matrix, players)
    pass

def togglePlayers(players):
  if players['playerTwoTurn'] == True:
    players['playerTwoTurn'] = False
  elif players['playerTwoTurn'] == False:
    players['playerTwoTurn'] = True
  if players['playerOneTurn'] == True:
    players['playerOneTurn'] = False
  elif players['playerOneTurn'] == False:
    players['playerOneTurn'] = True
  return players

def rowWinner(matrix):
  for i in matrix:
    print('i in matrix is: ', i)
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

