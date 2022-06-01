def U(obstacleGrid): # Only for 1 obstacle
    m=len(obstacleGrid)
    n=len(obstacleGrid[0])
    if m == 0 or n == 0: return 1
    if m == 1:
        for i in range(n):
            if obstacleGrid[0][i]==1: 
                return 0
        return 1
    if n == 1:
        for i in range(m):
            if obstacleGrid[i][0]==1: 
                return 0
        return 1
    for i in range(m):
        for j in range(n):
            if obstacleGrid[i][j]==1:
                x=j
                y=i
    print("x+1 =",x+1,"y+1=",y+1)
    D = m + n - 2
    C = n - 1
    res = 1
    c = 1
    for i in range(C, 0, -1):
        res *= D
        c *= i
        D -= 1
    # print("c = ",c)
    res //= c

    D = x + y
    C = x
    m1=1
    c=1
    for i in range(C, 0, -1):
        m1 *= D
        c *= i
        D -= 1
    m1 //= c

    D = m + n - x - y -2
    C = n - y-1
    m2 = 1
    c = 1
    for i in range(C, 0, -1):
        m2 *= D
        c *= i
        D -= 1
    m2 //= c
    print("res =",res,", m1 =",m1,", m2 =",m2)
    
    return res-m1*m2

def UU(obstacleGrid):
    if obstacleGrid[0][0] == 1:
        return 0
    
    m, n = len(obstacleGrid), len(obstacleGrid[0])        
    
    obstacleGrid[0][0] = 1
    for i in range(1,m):
        obstacleGrid[i][0] = 1 if obstacleGrid[i][0] == 0 and obstacleGrid[i-1][0] == 1 else 0
    for i in range(m):
        print(obstacleGrid[i])
    print()
    for i in range(1,n):
        obstacleGrid[0][i] = 1 if obstacleGrid[0][i] == 0 and obstacleGrid[0][i-1] == 1 else 0
    for i in range(m):
        print(obstacleGrid[i])    
    print()
    for row in range(1, m):
        for col in range(1, n):                
            obstacleGrid[row][col] = obstacleGrid[row-1][col] + obstacleGrid[row][col-1] if obstacleGrid[row][col] == 0 else 0
    for i in range(m):
        print(obstacleGrid[i])    
    return obstacleGrid[-1][-1]

def main():
    # G=[[0,0,0],[0,1,0],[0,0,0]]
    # print(U(G))
    # G=[[0,1],[0,0]]
    # print(U(G))
    G=[[0,0,1,0],[0,0,0,0],[1,1,1,0],[0,0,0,0]]
    print(UU(G))
    # G=[[0,0,0,1,0]]
    # print(U(G))




main()