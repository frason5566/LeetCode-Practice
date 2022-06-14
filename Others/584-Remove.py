def R (word1, word2):
    dp = [0] * (len(word2)+1)
    for i in range(len(word1)+1):
        temp = [0] * (len(word2)+1)
        for j in range(len(word2)+1):
            if i == 0 or j == 0:
                temp[j] = i+j
            elif word1[i-1] == word2[j-1]:
                temp[j] = dp[j-1]
            else:
                temp[j] = min(dp[j], temp[j-1]) + 1
        dp = temp
        print(dp)

    return dp[len(word2)]


def main():

    s1 = 'leetcode'
    s2 = 'etco'
    print(R(s1,s2))

main()