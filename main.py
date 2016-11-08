# create player startup prompt, accept input s
# from helper import createBoard
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


print (players)
# board = createBoard()
# print ('board in mainpy is: ', board)



