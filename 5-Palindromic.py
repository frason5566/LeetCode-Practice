def O(s):
    start,end =0,0
    pd = [[False] * len(s) for _ in range(len(s))]
    for i in range(len(s)):
        pd[i][i] = True
    for j in range(len(s)):
        for i in range (0,j+1):
            if s[i]==s[j] and (j-i+1<=2 or (j-i+1>2 and pd[i+1][j-1])):
                pd[i][j]=True
                if end-start+1 < j-i+1:
                    start,end = i,j
    print(start,end)
    for j in range(len(s)):
        for i in range ((len(s))):
            print(pd[i][j],end='  ')if pd[i][j] else print(pd[i][j],end=' ')
        print()
    return s[start:end+1]

def P(s):
    temp = ''
    maxp = ''
    for i in range (len(s)):
        temp += s[i]
        for j in range (len(temp)):
            if temp[j] == s[i] and s[j:i+1] == s[j:i+1][::-1] and len(s[j:i+1])>len(maxp):
                maxp = s[j:i+1]
                break
    return maxp

def Q(s):
    if len(s)==0: return ""
    maxL = 1
    flag = 1
    res = s[0]
    for i in range (len(s)-1):
        # print("i = " , i)
        ex = 1
        L = 1
        flag = 1
        while (flag == 1 and (i + ex < len(s)) and (i - ex >= 0)):
            if s[i+ex] == s[i-ex]:
                L += 2
                ex += 1
                # print("ex = ", ex)
            else :
                flag = 0
        # print("L = ",L)
        if maxL < L:
            res = s[i-ex+1:i+ex]
            maxL = L
        ex = 0
        L = 0
        flag = 1
        while (flag == 1 and (i + ex + 1 < len(s)) and (i - ex >= 0)):
            if s[i+ex+1] == s[i-ex]:
                L += 2
                ex += 1
            else :
                flag = 0

        if maxL < L:
            res = s[i-ex+1:i+ex+1]
            maxL = L

    return res


def main():
    S1="bafabad"
    S2="bb"
    # print(S1.index("d"))
    print(Q(S1))
    print(Q(S2))


main()