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


def main():

    I = [[1,5],[2,6],[8,20],[23,26]]
    print(M(I))
    I = [[1,4],[4,5]]
    print(M(I))
    I = [[1,6],[4,8],[7,10]]
    print(M(I))
main()