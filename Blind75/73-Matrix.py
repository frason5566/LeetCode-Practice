def S(matrix):
    y = len(matrix)
    x = len(matrix[0])
    temp = []
    for i in range(y):
        for j in range(x):
            if matrix[i][j] == 0:
                temp.append([i,j])
    # print(temp)
    if len(temp) > 0:
        for item in temp:
            matrix[item[0]] = [0] * x
            for i in range(y):
                matrix[i][item[1]]=0
            
            
    
def main():
    M = [[1,2,3],
        [4,0,6],
        [0,8,9],
        [1,2,3]]
    print(M)
    S(M)
    print(M)
    M = [[1,2,3],
        [4,5,6],
        [7,8,9]]
    print(M)
    S(M)
    print(M)
main()  
