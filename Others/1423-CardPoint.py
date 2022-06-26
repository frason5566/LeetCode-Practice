def S(cardPoints,k):
    if len(cardPoints) == k:
        return sum(cardPoints)
    w = len(cardPoints) - k
    for i in range(len(cardPoints)-w+1):
        if i == 0:
            ws = sum(cardPoints[0:w])
            res = ws
        else:
            ws = ws - cardPoints[i-1] + cardPoints[i+w-1]
            print(i+k-1)
            res = min(res,ws)
    return sum(cardPoints) - res


def main():
    # c = [1,2,3,4,5,6,1]
    # print(S(c,3))
    # c = [2,2,2,2]
    # print(S(c,2))
    c = [1,79,80,1,1,1,200,1]
    print(S(c,3))

main()

