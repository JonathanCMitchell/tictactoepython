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

def majorDiagWinner(matrix):
    count_diagX = 0
    count_diagO = 0
    for i in range(len(matrix)):
       if matrix[i][i] == 'X':
           count_diagX += 1
       if count_diagX >= 3:
            return True
       elif matrix[i][i] == 'O':
           count_diagO += 1
       if count_diagO >= 3:
            return True
    else:
        return False

def minorDiagWinner(matrix):
    count_diagX = 0
    count_diagO = 0
    length = len(matrix)
    for i in range(0, length):
        print('i is : ', i)
        if matrix[length-1 - i][i] == 'X':
            count_diagX += 1
        if count_diagX >= 3:
            return True
        elif matrix[length-1 - i][i] == 'O':
            count_diagO += 1
        if count_diagO >= 3:
            return True
    else:
        return False

def winners(matrix):
    if colWinner(matrix) or rowWinner(matrix) or minorDiagWinner(matrix) or majorDiagWinner(matrix):
        return True
    else:
        pass