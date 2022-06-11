def M(m,n,indices):
    M = [[0 for i in range(n)] for i in range(m)] 
    res = 0
    for item in indices:
        for i in range(n):
            M[item[0]][i] +=1
        for i in range(m):
            M[i][item[1]] +=1
    for i in range(m):
        for j in range(n):
            if M[i][j] % 2 == 1:
                res += 1
    return res

def MM(m,n,indices):
    Y = [0 for i in range(m)]
    X = [0 for i in range(n)]
    for item in indices:
        X[item[1]] = (X[item[1]] + 1) % 2
        Y[item[0]] = (Y[item[0]] + 1) % 2
    res = 0
    for i in range(m):
        for j in range(n):
            if X[j] + Y[i] == 1:
                res += 1
    return res

def main():
    print(MM(2,3,[[0,1],[1,1]]))
    print(MM(2,2,[[0,0],[1,1]]))
main()
