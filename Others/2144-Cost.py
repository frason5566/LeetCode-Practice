def C(cost):
    cost.sort(reverse = True)
    res = 0
    for i in range(0,len(cost),3):
        res += cost[i]
        if i+1 < len(cost):
            res += cost[i+1]

    return res


def main():
    M = [5,5]
    print(C(M))
    M = [1,2,3]
    print(C(M))
    M = [1,2,3,4]
    print(C(M))
    M = [6,5,7,9,2]
    print(C(M))

main()