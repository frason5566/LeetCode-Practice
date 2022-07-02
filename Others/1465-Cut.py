def C(h, w, horizontalCuts, verticalCuts):
    horizontalCuts.append(h)
    verticalCuts.append(w)
    horizontalCuts.sort()
    verticalCuts.sort()

    mh, mv = horizontalCuts[0], verticalCuts[0]

    for i in range(1,len(horizontalCuts)):
        mh = max(mh,horizontalCuts[i]-horizontalCuts[i-1])
        
    for i in range(1,len(verticalCuts)):
        mv = max(mv,verticalCuts[i]-verticalCuts[i-1])
    return mh * mv


def main():
    H = [1,2,4]
    W = [1,3]
    print(C(5,4,H,W))


main()
