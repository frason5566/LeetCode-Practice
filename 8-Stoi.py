def A (s):
    res = 0
    flag = 0
    N = 0
    mf = 0
    for i in range (len(s)):
        if s[i] == ' '  and flag == 0:
            continue
        elif s[i]=='-' and flag == 0 and mf ==0:
            N = 1
            mf =1
            if i < len(s)-1 and s[i+1] not in "0123456789":
                flag = 1
        elif s[i]=='+' and flag == 0 and mf ==0:
            N = 0
            mf = 1
            if i < len(s)-1 and s[i+1] not in "0123456789":
                flag = 1
        elif s[i] in "0123456789" and flag == 0:
            res = res*10 + int(s[i])
            if i < len(s)-1 and s[i+1] not in "0123456789":
                flag = 1
        else:
            flag = 1
    if N == 1: res = -res 
    # print(res)
    if res > 2 ** 31 -1: res = 2 ** 31 -1
    if res < -2 ** 31 : res = -2 ** 31 
    return res

def main():
    S="123456"
    print(A(S))
    S="-91283472332"
    print(A(S))
    S="123  456"
    print(A(S))
    S="+1"
    print(A(S))
main()