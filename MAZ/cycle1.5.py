#implemntation of n queen problem
n = int(
    input("Number of queens and order of the board in which the game is going to be played is equal hence enter the "
          "number:"))
assert n >= 4, "The N-Queens problem only works for board having a minimum of 16 cells"
board = [[0 for i in range(n)] for i in range(n)]


def column_check(board, row, column):
    """Checking whether there is no attack column wise """
    for i in range(row, -1, -1):
        if board[i][column] == 1:
            return False
    return True


def diagonal_check(board, row, column):
    """Checking whether there is no attack diagonal wise (The diagonals checked here are upper left and upper right)"""
    for i, j in zip(range(row, -1, -1), range(column, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(column, n)):
        if board[i][j] == 1:
            return False
    return True


def N_QUEEN(board, row):
    """This the place we try to backtrack the program.
    Here we try to check if the queen can be placed in the corresponding location"""
    if row == n:
        return True
    for i in range(n):
        if column_check(board, row, i) == True and diagonal_check(board, row, i) == True:
            board[row][i] = 1
            if N_QUEEN(board, row + 1):
                return True
            board[row][i] = 0
    return False


N_QUEEN(board, 0)

for row in board:
    print(row)
