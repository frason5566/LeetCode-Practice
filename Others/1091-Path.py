def S(grid):
    l=len(grid)
    if grid[0][0] == 1 or grid[l-1][l-1] == 1: return -1
    def helper(y,x,path,itr):
        print("itr = ",itr)
        if y < 0 or x < 0 or y>=l or x >=l:return float("inf")
        elif grid[y][x] == 1 :return float("inf")
        elif y == l-1 and x == l-1:
            path.append([y,x])
            print("y:",y,"x:",x)
            print(path)
            return len(path)
        else:
            path.append([y,x])
            print("y:",y,"x:",x)
            print(path)
            d1,d2,d3,d4,d5,d6,d7,d8 = float("inf"), float("inf"), float("inf"), float("inf"), float("inf"), float("inf"), float("inf"), float("inf")
            # if [y+1,x-1] not in path: 
            #     d6=helper(y+1,x-1,path,itr+1)
            #     print("d6=",d6)
            
            # if [y-1,x-1] not in path:
            #     d1=helper(y-1,x-1,path,itr+1)
            #     print("d1=",d1)
            # if [y-1,x] not in path:
            #     d2=helper(y-1,x,path,itr+1)
            #     print("d2=",d2)
            # if [y-1,x+1] not in path:
            #     d3=helper(y-1,x+1,path,itr+1)
            #     print("d3=",d3)
            # if [y,x-1] not in path:
            #     d4=helper(y,x-1,path,itr+1)
            #     print("d4=",d4)
            if [y,x+1] not in path:
                d5=helper(y,x+1,path,itr+1)
                print("d5=",d5)
            if [y+1,x] not in path:
                d7=helper(y+1,x,path,itr+1)
                print("d7=",d7)
            if [y+1,x+1] not in path:
                d8=helper(y+1,x+1,path,itr+1)
                print("d8=",d8) 

            return min(d1,d2,d3,d4,d5,d6,d7,d8)
    res = helper(0,0,[],0)

    return res if res != float("inf") else -1

def main():
    G = [[0,0,0],
         [1,1,0],
         [1,1,0]]
    print(S(G))
    # G = [[0,0,0,1],
    #      [1,1,0,0],
    #      [1,0,1,1],
    #      [1,0,0,0]]
    # print(S(G))

main()