from helper import board

def rowWinner(matrix):
    for row in matrix:
        col_countX = 0
        col_countO = 0
        for col in row:
            if col == 'X':
                col_countX+=1
            if col_countX >= 3:
                return True
            elif col == 'O':
                col_countO+=1
            if col_countO >= 3:
                return True
    else:
        return False

def colWinner(matrix):
    for i in range(len(matrix)):
        row_countX = 0
        row_countO = 0
        for j in range(0, len(matrix)):
            print('rowi is ', matrix[j][i])
            if matrix[j][i] == 'X':
                row_countX += 1
            if row_countX >= 3:
                return True
            elif matrix[j][i] == 'O':
                row_countO += 1
            if row_countO >= 3:
                return True
    else:
        return False

board[0] = ['O',1,'X']
board[1] = ['X', 'X', 'O']
board[2] = ['X', 'X', 'X']
print(board)

print(colWinner(board))
