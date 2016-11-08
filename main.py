# create player startup prompt, accept input s
from helper import createBoard
from helper import displayMovesAndSaveInput
from helper import acceptMoveAndToggle
from helper import initializePlayers
# from helper import checkRowWinner
players = {}
players = initializePlayers(players)

# create a while loop to show that nobody has won yet
board = createBoard()
currentMove = displayMovesAndSaveInput(board)
# acceptMoveAndToggle(currentMove, board, players)

acceptMoveAndToggle(currentMove, board, players)
print('Board after first input save: ', board)
print('players after first input save: ', players)
