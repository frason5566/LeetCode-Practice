def V(board):
    for i in range(9):
        check = []
        for j in range(9):
            if board[i][j] != '.':
                if board[i][j] not in check:
                    check.append(board[i][j])
                else:
                    return False
    for i in range(9):
        check = []
        for j in range(9):
            if board[j][i] != '.':
                if board[j][i] not in check:
                    check.append(board[j][i])
                else:
                    return False
    for i in range(1, 8, 3):
        for j in range(1, 8, 3):
            check = []
            for k in range(-1,2):
                for l in range(-1,2):
                    if board[i+k][j+l] != '.':
                        if board[i+k][j+l] not in check:
                            check.append(board[i+k][j+l])
                        else:
                            return False
    return True

def VV(board):
    col = [[]*9 for i in range (9)]
    row = [[]*9 for i in range (9)]
    nine = [[]*9 for i in range (9)]
    for i in range(9):
        for j in range(9):
            if board[i][j] != '.':
                if board[i][j] not in col[i]:
                    col[i].append(board[i][j])
                else:
                    return False
                if board[i][j] not in row[j]:
                    row[j].append(board[i][j])
                else:
                    return False
                ni = i // 3 + j // 3 * 3
                if board[i][j] not in nine[ni]:
                    nine[ni].append(board[i][j])
                else:
                    return False
    return True


                


def main():

    S = [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]

    print(VV(S))

main()