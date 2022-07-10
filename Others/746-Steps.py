def S(cost):
    dp = [0]*(len(cost)+1)
    for i in range(2,len(cost)+1):
        dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
    return dp[-1]

def main():
    C = [10,15,20]
    print(S(C))
    C=[1,100,1,100,1,1,1,100,1,1,100]
    print(S(C))


main()
