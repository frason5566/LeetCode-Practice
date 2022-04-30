def M (intervals):
    if len(intervals) == 1: return intervals
    intervals.sort(key=lambda x:x[0])
    res = [intervals[0]]
    
    for i in range(1,len(intervals)):
        temp = res[-1]
        print("temp = ",temp)
        if temp[1] >= intervals[i][0]:
            temp = [temp[0], max(intervals[i][1],temp[1])]
            res.append(temp)
            res = res[1:]
        else:
            res.append(intervals[i])
    
    return res

def MM(intervals):
    if len(intervals) == 1: return intervals
    ans = []
    start = []
    end = []
    for item in intervals:
        start.append(item[0])
        end.append(item[1])
    s = e = 0
    flag = 0
    while e == len(end):
        while True:
            st = start[s]
            s += 1


    return ans


def main():
    I = [[1,3],[2,6],[8,10],[15,18]]
    print(MM(I))
    I = [[1,5],[2,6],[8,20],[23,26]]
    print(MM(I))
    I = [[1,4],[5,6]]
    print(MM(I))
    I = [[1,4],[1,4]]
    print(MM(I))

main()