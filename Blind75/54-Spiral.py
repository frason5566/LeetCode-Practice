def S(matrix):
    res = []
    l,t,b,r = 0,0,len(matrix),len(matrix[0])
    d = 1
    while l<r and t<b:
        
        if d == 1:
            for i in range(l,r):
                res.append(matrix[t][i])
            t+=1
        elif d == 2:
            for i in range(t,b):
                res.append(matrix[i][r-1])
            r-=1
        elif d == 3:
            for i in range(r-1,l-1,-1):
                res.append(matrix[b-1][i])
            b-=1
        elif d == 4:
            for i in range(b-1,t-1,-1):
                res.append(matrix[i][l])
            l+=1
        d += 1
        if d > 4: d-=4
        
    return res


def main():
    M =[[1,2,3],
        [4,0,6],
        [0,8,9],
        [1,2,3]]
    print(M)
    print(S(M))
    print("[1, 2, 3, 6, 9, 3, 2, 1, 0, 4, 0, 8]")
    print("****************************")
    M =[[1,2,3,5],
        [4,0,6,7],
        [0,8,9,9]]
    print(S(M))
    print("[1, 2, 3, 5, 7, 9, 9, 8, 0, 4, 0, 6]")
main()