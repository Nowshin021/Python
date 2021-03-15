# takes a location i , j in the matrix:
def is_danger(rowNo, colNo):
    # check the rows cols if there is any queen present (queen==1)
    for i in range(0, n):
        if board[rowNo][i] == 1 or board[i][colNo] == 1:
            return True  # queen present here
    # check diagonal:
    for i in range(0, n):
        for j in range(0, n):
            if (i + j == colNo + rowNo) or (i - j == rowNo - colNo):
                if board[i][j] == 1:
                    return True  # there is a queen in diagonal
    return False  # no queen in diagonal or row or column


# n=number of column :
# logic: take a column
def N_queen(colNum):
    # base case :
    if colNum == 0:
        return True
    for i in range(0, n):
        for j in range(0, n):
            if (not (is_danger(i, j)) and (board[i][j] != 1)):

                # place the queen
                board[i][j] = 1

                # recurse for the privious colimn and check all the rows of each column
                if N_queen(colNum - 1) == True:
                    return True
                # else backtrack : take out the privious queen:
                board[i][j] = 0
    return False


n = int(input("Enter the number of queens : "))

# chesboard nXn
board = [[0] * n for _ in range(n)]

N_queen(n)
for i in board:
    print(i)



