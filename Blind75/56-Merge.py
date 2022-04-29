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

class ITV:
    def __init__(self):
        self.val = 0
        self.isEnd = False

def MM(intervals):
    if len(intervals)==1:return intervals
    res = [ITV] * 10001
    ans = []
    
    for item in intervals:
        for i in range(item[0],item[1]+1):
            temp = ITV()
            res[i] = temp
            temp.val += 1
            if i == item[1]:
                res[i].isEnd = True
    flag = 0
    for i in range(10001):
        T = res[i]
        if T.val == 0 and flag == 0:
            continue
        elif T.val >= 1 and flag == 0:
            temp = [0] * 2
            temp[0] = i
            flag = 1
        elif T.val >= 1 and flag == 1:
            if T.isEnd == True:
                temp[1] = i-1
                flag = 0
                ans.append(temp)
        elif T.val == 0 and flag == 1:
            temp[1] = i-1
            flag = 0
            ans.append(temp)
    
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