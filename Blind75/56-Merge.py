def M (intervals):
    if len(intervals)==1:return intervals
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
    if len(intervals)==1:return intervals
    res = [0] * 10001
    ans = []
    temp = [0] * 2
    for item in intervals:
        for i in range(item[0],item[1]+1):
            res [i] += 1
    flag = 0
    for i in range(10001):
        if res[i] == 0 and flag == 0:
            continue
        elif res[i] == 1 and flag == 0:
            temp[0] = i
            flag =1
        elif res[i] == 1 and flag == 1:
            continue
        elif res[i] == 0 and flag == 1:
            temp[1] = i-1
            flag = 0
            ans.append(temp)
    
    return ans


def main():
    I = [[1,3],[2,6],[8,10],[15,18]]
    print(MM(I))
    I = [[1,5],[2,6],[8,20],[23,26]]
    print(MM(I))
    I = [[1,4],[4,5]]
    print(MM(I))
    I = [[1,6],[4,8],[7,10]]
    print(MM(I))

main()