def T(matrix):
    m = len(matrix)
    n = len(matrix[0])
    res = [[0 ]*m for i in range (n) ] 
    print(res)

    for i in range(m):
        for j in range(n):
            res[j][i] = matrix[i][j]

    return res

def main():

    M = [[1,2,3],[4,5,6],[7,8,9]]
    print(T(M))
    M = [[1,2,3],[4,5,6]]
    print(T(M))

main()