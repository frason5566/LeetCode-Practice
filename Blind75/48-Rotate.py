from re import L


def R(matrix):
    l = len(matrix)-1
    e=(l+1)//2
    print("len =",l,", e =",e)
    for i in range(e):
        for j in range(i, l-i):
            print("i =",i,", j =",j)
            # tmp = matrix[i][j]
            matrix[i][j],matrix[l-j][i],matrix[l-i][l-j],matrix[j][l-i] = matrix[l-j][i], matrix[l-i][l-j],matrix[j][l-i],matrix[i][j]
            
    
def main():
    M =[[1,2,3,4],
        [4,0,6,4],
        [0,8,9,4],
        [1,2,3,4]]
    for i in range(len(M)):
        print(M[i])
    R(M)
    for i in range(len(M)):
        print(M[i])
    M =[[1,2,3],
        [4,0,6],
        [0,8,9]]
    for i in range(len(M)):
        print(M[i])
    R(M)
    for i in range(len(M)):
        print(M[i])
main()