def M(mat,k):
    res = [0] * len(mat)
    for i in range(len(mat)):
        if 0 in mat[i]:
            res[i] = [mat[i].index(0),i]
        else:
            res[i] = [float("INF"),i]
    sorted_s = sorted(range(len(res)), key = lambda k : res[k]) 
    return sorted_s[:k]


def main():
    m = [[1,1,0,0,0],
        [1,1,1,1,0],
        [1,0,0,0,0],
        [1,1,0,0,0],
        [1,1,1,1,1]]
    print(M(m,3))

main()