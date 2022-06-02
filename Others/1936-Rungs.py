def A(rungs, dist):
    res = 0
    s = 0
    for item in rungs:
        if s + dist >= item:
            s = item
        else:
            res += (item - s - 1) // dist
            s = item
    return res

def main():
    R=[1,3,5,12,18]
    print(A(R,2))
    R=[3,6,8,10]
    print(A(R,3))
    R=[3,4,6,7]
    print(A(R,2))

main()

