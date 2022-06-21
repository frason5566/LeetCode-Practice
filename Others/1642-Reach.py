import heapq


def R(heights, bricks, ladders):
    dis = []
    for i in range(1,len(heights)):
        dif = heights[i]- heights[i-1]
        if dif > 0:
            heapq.heappush(dis,dif)
        if len(dis) > ladders:
            bricks -= heapq.heappop(dis)
        
        if bricks < 0:
            return i-1

        
    return len(heights) -1

def main():
    h = [4,2,7,6,9,14,12]
    print(R(h,5,1))

main()