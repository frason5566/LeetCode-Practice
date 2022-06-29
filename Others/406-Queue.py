def R(people):
    people.sort(key=lambda x: (-x[0], x[1]))
    res = []
    for a in people:
        res.insert(a[1],a)
        print(res)
    return res


def main():
    P = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
    print(R(P))
    P = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
    print(R(P))

main()