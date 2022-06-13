def T(triangle):
    if len(triangle) == 1: return triangle[0][0]
    
    for i in range(len(triangle)-2, -1, -1):
        for j in range(len(triangle[i])):
            triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])

    return triangle[0][0]

def main():
    t = [[2],[3,4],[6,5,7],[4,1,8,3]]
    print(T(t))



main()