def T(boxTypes, truckSize):
    boxTypes = sorted(boxTypes, key = lambda x: x[1], reverse = True)
    # print(boxTypes)
    t = 0
    res = 0
    while truckSize > 0 and t < len(boxTypes):
        if truckSize >= boxTypes[t][0]:
            res += boxTypes[t][0] * boxTypes[t][1]
            truckSize -= boxTypes[t][0]
            t += 1
        else: 
            res += truckSize * boxTypes[t][1]
            truckSize -= boxTypes[t][0]
            t += 1

    return res


def main():
    B = [[1,3],[2,2],[3,1]]
    print(T(B,4))
    B = [[5,10],[2,5],[4,7],[3,9]]
    print(T(B,10))


main()