# create player startup prompt, accept input s
from helper import createBoard
from helper import displayMovesAndSaveInput
from helper import acceptMoveAndToggle
# from helper import checkRowWinner

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

players = {}
players = initializePlayers(players)
# create a while loop to show that nobody has won yet
board = createBoard()
currentMove = displayMovesAndSaveInput(board)
acceptMoveAndToggle(currentMove, board, players, 0)

currentMove = displayMovesAndSaveInput(board)
acceptMoveAndToggle(currentMove, board, players, 0)
currentMove = displayMovesAndSaveInput(board)
acceptMoveAndToggle(currentMove, board, players, 0)
currentMove = displayMovesAndSaveInput(board)
acceptMoveAndToggle(currentMove, board, players, 0)
currentMove = displayMovesAndSaveInput(board)
acceptMoveAndToggle(currentMove, board, players, 0)
currentMove = displayMovesAndSaveInput(board)
acceptMoveAndToggle(currentMove, board, players, 0)

# checkRowWinner(board)

print('Board after first input save: ', board)
# checkRowWinner(board)
