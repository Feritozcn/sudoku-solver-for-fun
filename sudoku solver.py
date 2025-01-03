##empty spaces "."
#9x9
# full string
def check_valid(row,col,num):
    for i in range(9):
        if board[row][i]==str(num):
            return False
        if board[i][col]==str(num):
            return False
    start_row=row//3*3
    start_col=col//3*3
    for i in range(start_row,start_row+3):
        for j in range(start_col,start_col+3):
            if board[i][j]==str(num):
                return False
    return True

def backtrack():
    for row in range(9):
        for col in range(9):
            if board[row][col]==".":
                for num in range(1,10):
                    if check_valid(row,col,num):
                        board[row][col]=str(num)
                        if backtrack():
                            return True
                        board[row][col]="."
                        
                return False
    return True

board=[["5","3",".",".","7",".",".",".","."],
       ["6",".",".","1","9","5",".",".","."],
       [".","9","8",".",".",".",".","6","."],
       ["8",".",".",".","6",".",".",".","3"],
       ["4",".",".","8",".","3",".",".","1"],
       ["7",".",".",".","2",".",".",".","6"],
       [".","6",".",".",".",".","2","8","."],
       [".",".",".","4","1","9",".",".","5"],
       [".",".",".",".","8",".",".","7","9"]]
## you can change the board for checking or filling the board

if backtrack():
    print(board)
else:
    print("No valid solution exists")



