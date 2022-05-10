def S(board, word):
    m = len(board)
    n = len(board[0])
    l = len(word)
    res = False
    def helper(b,y,x,w,windex):
        if windex == l:
            return True
        else:
            if y < 0 or y >= m or x < 0 or x >= n:
                return False
            if board[y][x] != w[windex]:
                return False
            if b[y][x] == w[windex]:
                b[y][x] = '#'
                found = helper(b,y-1,x,w,windex+1) or helper(b,y+1,x,w,windex+1) or helper(b,y,x-1,w,windex+1) or helper(b,y,x+1,w,windex+1)
                # b[y][x] = w[windex]
            return found
    for i in range(m):
        for j in range(n):
            if helper(board,i,j,word,0):
                return True
    return res

def main():
    M =[['A','A','B','D'],
        ['J','G','C','E'],
        ['F','F','D','H'],
        ['L','E','E','K']]
    for i in range(len(M)):
        print(M[i])
    
    print(S(M,'ABCDEEE'))

    M =[['A','A','B','D'],
        ['J','G','C','E'],
        ['F','F','D','H']]
    for i in range(len(M)):
        print(M[i])
    
    print(S(M,'JGAB'))
main()