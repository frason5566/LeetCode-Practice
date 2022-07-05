def C(ratings): # Time limit
    C = [1 for i in range(len(ratings))]
    flag = True
    # cnt = 1
    while flag == True:
        flag = False
        # print(cnt)
        # cnt += 1
        for i in range(len(ratings)):
            if i != len(ratings) - 1:
                if ratings[i] > ratings[i+1] and C[i] <=C[i+1]:
                    C[i] += 1
                    flag = True
            if i != 0:
                if ratings[i] > ratings[i-1] and C[i] <=C[i-1]:
                    C[i] += 1
                    flag = True
    # print(C)
    return sum(C)

def CC(ratings):
    L, R = [1 for i in range(len(ratings))],[1 for i in range(len(ratings))]
    for i in range(1,len(ratings)):
        if ratings[i] > ratings[i-1]:
            L[i] = L[i-1] +1
    for i in range(len(ratings)-2,-1,-1):
        if ratings[i]> ratings[i+1]:
            R[i] = R[i+1] +1
    res = 0
    for i in range(len(ratings)):
        res += max(L[i],R[i])
    return res

def main():
    R = [1,0,2]
    print(CC(R))
    R = [1,2,2]
    print(CC(R))
    R = [1,2,3,4,5,2,5,5,5,6]
    print(CC(R))


main()
