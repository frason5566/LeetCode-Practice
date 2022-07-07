def II(s1,s2,s3): # 2D DP
    if len(s1)+len(s2) != len(s3): return False
    test = [[0 for i in range(len(s2)+1)] for i in range(len(s1)+1)]
    for i in range(len(test)):
        for j in range(len(test[0])):
            if i == 0 and j == 0:
                test[0][0] = True
            elif i == 0:
                test[i][j] = test[i][j-1] and (s2[j-1] == s3[i+j-1])
            elif j == 0:
                test[i][j] = test[i-1][j] and (s1[i-1] == s3[i+j-1])
            else:
                test[i][j] = (test[i][j-1] and (s2[j-1] == s3[i+j-1])) or (test[i-1][j] and (s1[i-1] == s3[i+j-1]))
    # print(test)

    return test[-1][-1]

def I(s1,s2,s3): # 1D DP
    if len(s1)+len(s2) != len(s3): return False
    test = [0 for i in range(len(s2)+1)] 
    for i in range(len(s1)+1):
        for j in range(len(s2)+1):
            if i == 0 and j == 0:
                test[j] = True
            elif i == 0:
                test[j] = test[j-1] and (s2[j-1] == s3[i+j-1])
            elif j == 0:
                test[j] = test[j] and (s1[i-1] == s3[i+j-1])
            else:
                test[j] = (test[j-1] and (s2[j-1] == s3[i+j-1])) or (test[j] and (s1[i-1] == s3[i+j-1]))
    # print(test)

    return test[-1]

def main():
    s1 = 'aabcc'
    s2 = 'dbbca'
    s3 = 'aadbbcbcac'
    print(I(s1,s2,s3))
    s1 = 'aabcc'
    s2 = 'dbbca'
    s3 = 'aadbbbaccc'
    print(I(s1,s2,s3))
    s1 = ''
    s2 = ''
    s3 = ''
    print(I(s1,s2,s3))




main()