# create player startup prompt, accept input s
from helper import createBoard
from helper import displayMovesAndSaveInput
from helper import acceptMoveAndToggle
from helper import initializePlayers

#Solvers
from solvers import winners
players = {}
players = initializePlayers(players)

board = createBoard()
currentMove = displayMovesAndSaveInput(board, players)


def game():
    while not winners(board):
        currentMove = displayMovesAndSaveInput(board, players)
        acceptMoveAndToggle(currentMove, board, players)
    if players['playerOneTurn'] == False:
        return 'Player One Wins'
    elif players['playerTwoTurn'] == False:
        return 'Player Two Wins'
    else:
        pass

game()


