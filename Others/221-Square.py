def S(matrix):
    res = 0
    dp = [[0]*(len(matrix[0])+1) for i in range (len(matrix)+1)]
    for y in range(1,len(matrix)+1):
        for x in range(1,len(matrix[0])+1):
            if matrix[y-1][x-1] == '1':
                dp[y][x] = min(dp[y-1][x], dp[y-1][x-1], dp[y][x-1] )+1
                res = max(res, dp[y][x])
    # print(dp)
    return res ** 2


def main():
    M = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    for i in M:
        print(i)
    print(S(M))
    M = [["0","1"],["1","0"]]
    for i in M:
        print(i)
    print(S(M))

main()


