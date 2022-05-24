def I(matrix):
    le=len(matrix)
    def helper(y,x,path):
        if y < 0 or x < 0 or y == le or x == le:return 0
        if len(path) !=0:
            if matrix[y][x] <= matrix[path[len(path)-1][0]][path[len(path)-1][1]]: return len(path)
            print("start from ", path[0])
        print("x =",x,", y =",y,", n =", matrix[y][x])
        route = [[y-1,x],[y+1,x],[y,x-1],[y,x+1]]
        path.append([y,x])
        res = -1
        for item in route:
            if item not in path:
                res = max(res, helper(item[0],item[1],path))
        print("res = ", res)
        return res 

    r=-1
    for i in range(le):
        for j in range(le):
            P=[]
            r = max(r, helper(i,j,P))
    return r

def main():
    M = [[9,9,4],[6,6,8],[2,1,1]]
    print(I(M))
    # M =[[3,4,5],[3,2,6],[2,2,1]]
    # print(I(M))

main()