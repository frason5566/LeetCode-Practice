def C (s):
    res = 0
    temp=[]
    for i in range (len(s)+1):
        if i == len(s):
            if res !=0:
                temp.append(res)
        elif s[i] == '1':
            res += 1
        elif s[i] == '0' and i < len(s)-1:
            temp.append(res)
            res = 0
    res = 0
    if len(temp)==0: return 0
    for item in temp:
        if item == 1:
            res +=1
        else:
            res += ((item+1)*item) // 2
    return res%(1000000007)

def CC (s):
    res = 0
    temp = 0

    for i in range (len(s)+1):
        if i == len(s):
            if temp !=0:
                res += ((temp+1)*temp) // 2
                temp = 0
        elif s[i] == '1':
            temp += 1
        elif s[i] == '0' and i < len(s)-1:
            res += ((temp+1)*temp) // 2
            temp = 0
    return res%(1000000007)

def CCC(s):
    res = 0
    cnt = 0
    if s[len(s)-1] == "1":
        s= s + "0"
    for i in range (len(s)):
        if s[i] == "1":
            cnt += 1
        else:
            res += ((cnt + 1) * cnt) // 2
            cnt = 0
    return res%(1000000007)

def main():
    S = "1001100111"
    print(CCC(S))
    S = "010011001110"
    print(CCC(S))
    S = "10011010111"
    print(CCC(S))


main()