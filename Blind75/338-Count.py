def C(n):
    if n == 0: return [0]
    res = [0]
    for i in range(1,n+1):
        x = i
        cnt = 0
        while x > 0:
            cnt += x % 2
            x = x >>1
        res.append(cnt)
    return res

def CC(n): # best
    if n == 0: return [0]
    res = [0]*(n+1)
    for i in range(1,n+1):
        res[i] = res[i>>1] + (i&1)
    return res

def main():

    # s=11
    # for i in range (10):
    #     print("i=",i,",i&1 = ",i&1)
    # print(s&1)
    n=8
    print(CC(n))
    n=10
    print(CC(n))


main()