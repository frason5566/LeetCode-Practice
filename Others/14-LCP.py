def L(strs):
    if len(strs) ==1: return strs[0]
    res = ""
    L=len(strs[0])
    flag = 1
    for item in strs:
        if L > len(item): L = len(item)
    if L == 0: return ""
    i = 0
    while flag == 1 and i < L:
        flag = 0
        temp = strs[0][i]
        cnt = 0
        for item in strs:
            if item[i] == temp:
                cnt +=1
        if cnt == len(strs):
            res += strs[0][i]
            flag =1
        i+=1
    return res

def main():
    S=["dog","dope","dot"]
    print(L(S))
    S=["car","dope","dot"]
    print(L(S))
    S=["gocart","goddess","gate"]
    print(L(S))
    S=["","b"]
    print(L(S))



main()