def L(text1,text2):
    dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]
    print(dp)
    for i in range(len(text1) - 1, -1, -1):
        for j in range(len(text2) - 1, -1, -1):
            if text1[i] == text2[j]:
                dp[i][j] = 1 + dp[i + 1][j + 1]
            else:
                dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])
            print(dp)
    
    return dp[0][0]

def main():
    T1="abcde"
    T2="ace"
    print(L(T1,T2))


main()