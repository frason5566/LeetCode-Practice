def W(properties):
    p = sorted(properties, key = lambda x: (-x[0],x[1]))
    print(p)
    cnt = 0
    mxattack=p[0][0]
    mxdefense=p[0][1]
    for i in range(1,len(p)):
        if p[i][0]<mxattack and p[i][1]<mxdefense:
            cnt+=1
        else:
            mxattack=p[i][0]
            mxdefense=p[i][1]
    return cnt


def main():
    P = [[5,5],[5,4],[6,4],[2,3],[3,6],[6,3],[2,2]]
    print(W(P))

main()