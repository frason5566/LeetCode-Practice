def R (s):
    res = 0
    for i in range (len(s)):
        print(s[i], end=',')
        if s[i] == "M":
            res +=1000
        elif s[i] == "D":
            res += 500
        elif s[i] == "C":
            if i == len(s)-1:
                res += 100
            elif s[i+1] == "D" or s[i+1] == "M":
                res -=100
            else:
                res +=100
        elif s[i] == "L":
            res += 50
        elif s[i] == "X":
            if i == len(s)-1:
                res += 10
            elif s[i+1] == "L" or s[i+1] == "C":
                res -=10
            else:
                res += 10
        elif s[i] == "V":
            res += 5
        elif s[i] =="I":
            if i == len(s)-1:
                res += 1
            elif s[i+1] == "X" or s[i+1] == "V":
                res -=1
            else:
                res += 1
        print(res)
    return res


    # I             1
    # V             5
    # X             10
    # L             50
    # C             100
    # D             500
    # M             1000
def main():
    S = "XII"  #12
    print(R(S))
    S = "XLIX"  # 49
    print(R(S))
    S = "MCMXCIV"   #1994
    print(R(S))
    S = "MMMCMXCIX" #3999
    print(R(S))


main()