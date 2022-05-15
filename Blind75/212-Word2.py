class Trie:
    def __init__(self):
        self.level = {}

    def insert(self, word):
        nextLevel = self.level
        for c in word:
            if not c in nextLevel: 
                nextLevel[c] = {}
            nextLevel = nextLevel[c]
        nextLevel['end'] = True

def S(board, words):
    m = len(board)
    n = len(board[0])
    # l = len(word)
    res = []
    trie = Trie()
    for word in words:
        trie.insert(word)
    def helper(b,y,x,level,word):
        if 'end' in level: True
        else:
            if y < 0 or y >= m or x < 0 or x >= n:
                return False
            if board[y][x] not in level:
                return False
            level = level[board[y][x]]
            word += b[y][x]
            tmp = board[y][x]
            b[y][x] = '#'
            found = helper(b,y-1,x,level,word) or helper(b,y+1,x,level,word) or helper(b,y,x-1,level,word) or helper(b,y,x+1,level,word)
            b[y][x] = tmp
            return found
    for word in words:
        l = len(word)
        for i in range(m):
            for j in range(n):
                    if helper(board,i,j,trie.level,''):
                        if word not in res:
                            res.append(word)
    return res

def main():
    M =[['A','A','B','D'],
        ['J','G','C','E'],
        ['F','F','D','H'],
        ['L','E','E','K']]
    for i in range(len(M)):
        print(M[i])
    W=['ABCDEE',"ABCD","DD",'DEHKK']
    print(S(M,W))

    # M =[['A','A','B','D'],
    #     ['J','G','C','E'],
    #     ['F','F','D','H']]
    # for i in range(len(M)):
    #     print(M[i])
    
    # print(S(M,'JGAB'))
main()