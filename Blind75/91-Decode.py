def D(s):
    if s[0]=='0':return 0
    L = len(s)
    count=[0] * (1+L)
    count[0]=1
    count[1]=1
    for i in range(2,L+1):
        if 0< int(s[i-1]) <= 9:
            count[i]+=count[i-1]
        if 10<= int(s[i-2:i])<=26:
            count[i]+=count[i-2]


    return count[L]

def main():

    S = "12"
    print(D(S))
    S = "226"
    print(D(S))
    S = "1406"
    print(D(S))
    S = "111222"
    print(D(S))

main()