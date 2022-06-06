def G(lo,hi,k):
    ori = [i for i in range(lo,hi+1)]
    # print (ori)
    power = []
    for i in range(len(ori)):
        temp = ori[i]
        cnt = 0
        while temp != 1:
            if temp % 2 == 0:
                temp //= 2
            else: 
                temp = temp * 3 + 1
            cnt +=1
        power.append((ori[i],cnt))
    power = sorted(power, key = lambda x: x[1] )
    print(power)
    return power[k-1][0]


def main():
    print(G(12,15,2))
    print(G(7,11,4))
    print(G(18,25,3))
    print(G(111,156,23))


main()