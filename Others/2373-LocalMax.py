def L(grid):
    l, r = 1, len(grid)-2
    ans = [[0 for _ in range(r)]for _ in range(r)] 
    
    def findMax(y, x):
        return max(grid[y][x], grid[y+1][x+1], grid[y+1][x], grid[y+1][x-1], grid[y][x+1], grid[y][x-1], grid[y-1][x+1], grid[y-1][x], grid[y-1][x-1])

    for i in range(r):
        for j in range(r):
            ans[j][i] = findMax(l+j, l+i)
    return ans

    



def main():
    M = [[9,9,8,6],[4,2,5,3],[6,2,3,8],[1,3,4,5]]
    print(M[0])
    print(M[1])
    print(M[2])
    print(M[3])
    print(L(M))

main()